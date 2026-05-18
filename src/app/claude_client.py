import os
import anthropic
from app.models import UserDoc, ContactDoc

_client = None

HAIKU = "claude-haiku-4-5-20251001"
SONNET = "claude-sonnet-4-6"


def get_client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        _client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    return _client


def build_context(user: UserDoc, contact: ContactDoc | None) -> str:
    parts = [
        "[USER PROFILE]",
        f"Name: {user.name}",
        f"Field: {user.field}",
        f"Language: {user.language}",
        f"Time in Canada: {user.time_in_canada}",
        f"City: {user.city}",
        f"Current challenge: {user.current_challenge}",
        f"Application stage: {user.application_stage}",
        f"Current state: {user.current_state}",
    ]
    if user.about_me:
        parts.append(f"About me: {user.about_me}")
    if user.conversation_summary:
        parts.append(f"Conversation summary: {user.conversation_summary}")
    if contact:
        parts += [
            "\n[ACTIVE CONTACT]",
            f"Name: {contact.name}, {contact.role} at {contact.company}",
            f"Connection context: {contact.connection_context}",
            f"Chat scheduled: {contact.scheduled_chat_at}",
            f"Topics of interest: {', '.join(contact.topics_of_interest) if contact.topics_of_interest else 'none'}",
            f"Post-call notes: {contact.post_call_notes or 'none yet'}",
        ]
    return "\n".join(parts)


def _make_request(system: str, messages: list, model: str) -> anthropic.types.Message:
    from app.prompts import TOOLS
    return get_client().messages.create(
        model=model,
        max_tokens=1024,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        tools=TOOLS,
        messages=messages,
    )


def call_claude(system: str, messages: list, model: str = SONNET) -> tuple[str, list, str | None, dict | None]:
    """
    Returns (text, response_content, tool_use_id | None, tool_inputs | None).
    response_content is the raw assistant turn needed to continue the conversation after tool use.
    """
    response = _make_request(system, messages, model)
    text = ""
    tool_use_id = None
    tool_inputs = None
    for block in response.content:
        if block.type == "tool_use":
            tool_use_id = block.id
            tool_inputs = block.input
        elif block.type == "text":
            text = block.text
    return text, response.content, tool_use_id, tool_inputs


def continue_with_tool_result(
    system: str,
    messages: list,
    assistant_content: list,
    tool_use_id: str,
    model: str = SONNET,
) -> str:
    """Send tool_result back to Claude and return the final text response."""
    extended = messages + [
        {"role": "assistant", "content": assistant_content},
        {"role": "user", "content": [{"type": "tool_result", "tool_use_id": tool_use_id, "content": "ok"}]},
    ]
    response = _make_request(system, extended, model)
    for block in response.content:
        if block.type == "text":
            return block.text
    return ""


def generate_summary(user: UserDoc) -> str:
    response = get_client().messages.create(
        model=HAIKU,
        max_tokens=300,
        system=(
            "Summarise the conversation history in 3–5 sentences. "
            "Capture: user's current situation, key contacts discussed, "
            "important moments (milestones, emotional shifts, insights), "
            "and any open threads. Write in third person. Be concise."
        ),
        messages=[{"role": "user", "content": str(user.messages)}],
    )
    return response.content[0].text


def call_claude_simple(system: str, prompt: str, model: str = HAIKU) -> str:
    """Single-turn call without tools — used by proactive job endpoints."""
    response = get_client().messages.create(
        model=model,
        max_tokens=512,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": prompt}],
    )
    for block in response.content:
        if block.type == "text":
            return block.text
    return ""
