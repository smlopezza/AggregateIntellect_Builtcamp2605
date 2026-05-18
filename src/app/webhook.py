import logging
import re
import time
from datetime import datetime, timedelta

from fastapi import APIRouter, BackgroundTasks, Request
from fastapi.responses import Response

from app.claude_client import (
    SONNET,
    build_context,
    call_claude,
    continue_with_tool_result,
    generate_summary,
)
from app.firestore_client import (
    get_active_contact,
    is_duplicate,
    load_user,
    save_contact,
    save_user,
)
from app.prompts import SYSTEM_PROMPT
from app.twilio_client import send_message

router = APIRouter()
logger = logging.getLogger(__name__)

RATE_LIMITS = {"free": 15, "contributor": 50, "org_sponsored": 99999}

RATE_LIMIT_MSG = {
    "es": (
        "Ya usaste tus mensajes de hoy — vuelve mañana. "
        "Si quieres acceso ilimitado, puedes contribuir a la comunidad: [link]. "
        "Si no puedes, está bien."
    ),
    "en": (
        "You've used today's messages — come back tomorrow. "
        "If you'd like unlimited access, you can support the community here: [link]. "
        "No pressure if not."
    ),
}

ERROR_MSG = {
    "es": "Algo salió mal de mi lado — intenta de nuevo en un momento.",
    "en": "Something went wrong on my end — try again in a moment.",
}


@router.post("/webhook/twilio")
async def twilio_webhook(request: Request, background_tasks: BackgroundTasks):
    form = await request.form()
    phone = str(form.get("From", "")).replace("whatsapp:", "")
    text = str(form.get("Body", ""))
    message_sid = str(form.get("MessageSid", ""))

    background_tasks.add_task(_process_safely, phone, text, message_sid)
    return Response(content="", media_type="text/xml")


def _process_safely(phone: str, text: str, message_sid: str):
    try:
        _process(phone, text, message_sid)
    except Exception:
        logger.exception("Unhandled error processing message for %s", phone)


def _process(phone: str, text: str, message_sid: str):
    if is_duplicate(message_sid):
        return

    user = load_user(phone)
    now = datetime.utcnow()

    if not _check_and_increment_rate_limit(user, now):
        send_message(phone, RATE_LIMIT_MSG.get(user.language, RATE_LIMIT_MSG["es"]))
        save_user(user)
        return

    contact_id, contact = get_active_contact(phone)
    context = build_context(user, contact)
    claude_messages = _build_messages(user, context, text)

    reply = _call_with_retry(user, contact, contact_id, phone, claude_messages)
    if not reply:
        reply = ERROR_MSG.get(user.language, ERROR_MSG["es"])

    ts = now.isoformat()
    user.messages.append({"role": "user", "content": text, "timestamp": ts})
    user.messages.append({"role": "assistant", "content": reply, "timestamp": ts})
    if len(user.messages) > 10:
        user.messages = user.messages[-10:]
    user.last_active = ts
    save_user(user)

    send_message(phone, reply)

    if len(user.messages) >= 10:
        try:
            user.conversation_summary = generate_summary(user)
            user.messages = []
            save_user(user)
        except Exception:
            logger.exception("Summary generation failed for %s", phone)


def _call_with_retry(user, contact, contact_id, phone, claude_messages) -> str:
    for attempt in range(2):
        try:
            return _call_claude_and_apply(user, contact, contact_id, phone, claude_messages)
        except Exception:
            if attempt == 0:
                logger.warning("Claude call failed for %s, retrying", phone)
                time.sleep(2)
            else:
                logger.exception("Claude retry failed for %s", phone)
    return ""


def _call_claude_and_apply(user, contact, contact_id, phone, claude_messages) -> str:
    reply, assistant_content, tool_use_id, tool_inputs = call_claude(
        SYSTEM_PROMPT, claude_messages, model=SONNET
    )

    if tool_inputs and tool_use_id:
        state_changed = _apply_tool_use(user, contact, tool_inputs)
        save_user(user)
        if contact and contact_id and state_changed:
            save_contact(phone, contact_id, contact)

        reply = continue_with_tool_result(
            SYSTEM_PROMPT, claude_messages, assistant_content, tool_use_id, model=SONNET
        )

    return reply


def _build_messages(user, context: str, new_text: str) -> list:
    """Build Claude messages with context injected as prefix of the first user turn."""
    history = [{"role": m["role"], "content": m["content"]} for m in user.messages]
    if history:
        first = history[0]
        history[0] = {"role": "user", "content": f"{context}\n\n{first['content']}"}
        return history + [{"role": "user", "content": new_text}]
    return [{"role": "user", "content": f"{context}\n\n{new_text}"}]


def _check_and_increment_rate_limit(user, now: datetime) -> bool:
    """Returns True if within limit. Mutates user to reset counter if needed and increment."""
    if user.message_count_reset_at is None or user.message_count_reset_at < now.isoformat():
        user.message_count_today = 0
        next_midnight = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        user.message_count_reset_at = next_midnight.isoformat()

    limit = RATE_LIMITS.get(user.tier, 15)
    if user.message_count_today >= limit:
        return False

    user.message_count_today += 1
    return True


def _apply_tool_use(user, contact, tool_inputs: dict) -> bool:
    """Apply update_state tool inputs. Returns True if current_state changed."""
    state_changed = False

    new_state = tool_inputs.get("new_state")
    if new_state:
        user.current_state = new_state
        state_changed = True

    about_me = tool_inputs.get("about_me")
    if about_me and not user.about_me:
        user.about_me = about_me

    country_of_origin = tool_inputs.get("country_of_origin")
    if country_of_origin and not user.country_of_origin:
        user.country_of_origin = country_of_origin

    contact_updates = tool_inputs.get("contact_updates")
    if contact_updates and contact:
        for field, value in contact_updates.items():
            if hasattr(contact, field):
                setattr(contact, field, value)

    return state_changed
