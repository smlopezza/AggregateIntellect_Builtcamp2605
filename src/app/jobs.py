import logging
import os
from datetime import datetime, timedelta

from fastapi import APIRouter, Header, HTTPException

from app.claude_client import HAIKU, SONNET, call_claude_simple
from app.firestore_client import get_all_contacts, get_all_users, load_user, save_contact, save_user
from app.twilio_client import send_message
from app.utils import is_sendable, local_hour

router = APIRouter()
logger = logging.getLogger(__name__)

SECRET = os.getenv("CLOUD_SCHEDULER_SECRET", "")

THANK_YOU_MSG = {
    "es": "¿Ya le mandaste un mensaje de agradecimiento a {name}? Es un gesto pequeño que hace una diferencia real. ¿Quieres que te ayude a escribirlo?",
    "en": "Did you send {name} a thank-you note? It's a small gesture that goes a long way. Want me to help you draft one?",
}

PRE_NUDGE_SYSTEM = (
    "You are SofIA, a warm bilingual ally for Latino newcomers to Canada. "
    "Generate a short, encouraging pre-chat nudge message for a user who has a professional "
    "coffee chat scheduled tomorrow. Include 2–3 specific prep questions tailored to the "
    "contact context provided. Keep it under 150 words. Never use the word 'networking'."
)

POST_CHECKIN_SYSTEM = (
    "You are SofIA, a warm bilingual ally for Latino newcomers to Canada. "
    "The user just had a professional coffee chat about 2 hours ago. "
    "Send a warm check-in asking how it went. Ask exactly ONE open Socratic question — "
    "never declare what the relationship means or should be. Under 80 words."
)


def _verify(secret: str):
    if secret != SECRET:
        raise HTTPException(status_code=403, detail="Forbidden")


def _now_iso() -> str:
    return datetime.utcnow().isoformat()


@router.post("/jobs/pre-chat-nudge")
def pre_chat_nudge(x_scheduler_secret: str = Header(...)):
    _verify(x_scheduler_secret)
    now = datetime.utcnow()
    window_start = (now + timedelta(hours=12)).isoformat()
    window_end = (now + timedelta(hours=36)).isoformat()

    for phone, contact_id, contact in get_all_contacts():
        if not contact.scheduled_chat_at:
            continue
        if not (window_start <= contact.scheduled_chat_at <= window_end):
            continue
        if contact.pre_nudge_sent_at is not None:
            continue

        user = load_user(phone)
        if not is_sendable(user.timezone) or local_hour(user.timezone) != 20:
            continue

        lang = "es" if user.language == "es" else "en"
        prompt = (
            f"User: {user.name}, field: {user.field}, language: {lang}.\n"
            f"Contact: {contact.name}, {contact.role} at {contact.company}.\n"
            f"Connection context: {contact.connection_context}.\n"
            f"Chat scheduled: {contact.scheduled_chat_at}.\n"
            f"Write the nudge in {lang}."
        )
        try:
            message = call_claude_simple(PRE_NUDGE_SYSTEM, prompt, model=HAIKU)
            send_message(phone, message)
            contact.pre_nudge_sent_at = _now_iso()
            save_contact(phone, contact_id, contact)
        except Exception:
            logger.exception("Pre-chat nudge failed for %s / %s", phone, contact.name)

    return {"status": "ok"}


@router.post("/jobs/post-chat-checkin")
def post_chat_checkin(x_scheduler_secret: str = Header(...)):
    _verify(x_scheduler_secret)
    now = datetime.utcnow()
    window_start = (now - timedelta(hours=3)).isoformat()
    window_end = (now - timedelta(hours=1)).isoformat()

    for phone, contact_id, contact in get_all_contacts():
        if not contact.scheduled_chat_at:
            continue
        if not (window_start <= contact.scheduled_chat_at <= window_end):
            continue
        if contact.post_nudge_sent_at is not None:
            continue

        user = load_user(phone)
        if not is_sendable(user.timezone):
            continue

        lang = "es" if user.language == "es" else "en"
        prompt = (
            f"User: {user.name}, field: {user.field}, language: {lang}.\n"
            f"Contact: {contact.name}, {contact.role} at {contact.company}.\n"
            f"They had a chat about 2 hours ago. Write the check-in in {lang}."
        )
        try:
            message = call_claude_simple(POST_CHECKIN_SYSTEM, prompt, model=SONNET)
            send_message(phone, message)
            contact.post_nudge_sent_at = _now_iso()
            save_contact(phone, contact_id, contact)
        except Exception:
            logger.exception("Post-chat check-in failed for %s / %s", phone, contact.name)

    return {"status": "ok"}


@router.post("/jobs/thank-you-nudge")
def thank_you_nudge(x_scheduler_secret: str = Header(...)):
    _verify(x_scheduler_secret)
    now = datetime.utcnow()
    window_start = (now - timedelta(hours=36)).isoformat()
    window_end = (now - timedelta(hours=12)).isoformat()

    for phone, contact_id, contact in get_all_contacts():
        if not contact.scheduled_chat_at:
            continue
        if not (window_start <= contact.scheduled_chat_at <= window_end):
            continue
        if contact.thank_you_nudge_sent_at is not None:
            continue
        if contact.post_nudge_sent_at is None:
            continue

        user = load_user(phone)
        if local_hour(user.timezone) != 7:
            continue

        lang = user.language if user.language in THANK_YOU_MSG else "es"
        message = THANK_YOU_MSG[lang].format(name=contact.name)
        try:
            send_message(phone, message)
            contact.thank_you_nudge_sent_at = _now_iso()
            save_contact(phone, contact_id, contact)
        except Exception:
            logger.exception("Thank-you nudge failed for %s / %s", phone, contact.name)

    return {"status": "ok"}


@router.post("/jobs/reset-rate-limits")
def reset_rate_limits(x_scheduler_secret: str = Header(...)):
    _verify(x_scheduler_secret)
    now_iso = datetime.utcnow().isoformat()
    reset_count = 0

    for user in get_all_users():
        if user.message_count_reset_at and user.message_count_reset_at < now_iso:
            user.message_count_today = 0
            next_midnight = (datetime.utcnow() + timedelta(days=1)).replace(
                hour=0, minute=0, second=0, microsecond=0
            )
            user.message_count_reset_at = next_midnight.isoformat()
            save_user(user)
            reset_count += 1

    return {"status": "ok", "reset": reset_count}
