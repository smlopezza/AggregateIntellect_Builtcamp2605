"""
End-to-end conversation test for SofIA.

Uses real Claude + Firestore but intercepts Twilio so replies print to terminal.
Each run gets a unique fake phone number — no cleanup needed between runs.

Usage:
    python test_e2e.py
    python test_e2e.py r9   # R9 framing check (scans for "networking" in early states)
"""

import sys
import uuid
from unittest.mock import patch
from dotenv import load_dotenv

load_dotenv()

from app.webhook import _process

SEPARATOR = "-" * 60


def chat(phone: str, text: str, replies: list[str]) -> str | None:
    """Send one message, capture SofIA's reply, return it."""
    message_sid = str(uuid.uuid4())
    captured = []

    def capture(to_phone, body):
        captured.append(body)

    with patch("app.webhook.send_message", side_effect=capture):
        _process(phone, text, message_sid)

    reply = captured[0] if captured else None
    if reply:
        replies.append(reply)
    return reply


def run_scenario(name: str, messages: list[str]) -> tuple[str, list[str]]:
    phone = "+1555" + uuid.uuid4().hex[:7]
    replies = []

    print(f"\n{SEPARATOR}")
    print(f"SCENARIO: {name}")
    print(f"Phone:    {phone}")
    print(SEPARATOR)

    for msg in messages:
        print(f"\n👤  {msg}")
        reply = chat(phone, msg, replies)
        if reply:
            print(f"\n🤖  {reply}")
        else:
            print("\n🤖  [no reply — check logs]")

    return phone, replies


def check_r9(replies: list[str], early_cutoff: int = None):
    """Scan replies for 'networking' in early-state messages."""
    print(f"\n{SEPARATOR}")
    print("R9 CHECK — 'networking' must not appear in early states")
    print(SEPARATOR)

    flagged = []
    check_replies = replies[:early_cutoff] if early_cutoff else replies
    for i, reply in enumerate(check_replies):
        lower = reply.lower()
        if "networking" in lower or "red de contactos" in lower:
            flagged.append((i + 1, reply[:120]))

    if flagged:
        for turn, snippet in flagged:
            print(f"  ❌ Turn {turn}: '{snippet}...'")
    else:
        print("  ✅ 'networking' not found in scanned replies")


# ---------------------------------------------------------------------------
# Scenarios
# ---------------------------------------------------------------------------

ONBOARDING_NO_CONTACTS = [
    "Hola",
    "Me llamo María. Soy ingeniera de software.",
    "Llegué hace 3 meses a Toronto",
    "Estoy enviando aplicaciones pero no recibo respuestas",
    "No tengo contactos profesionales en Canadá todavía",
    "Mi mayor reto es entender cómo funciona el mercado laboral aquí",
]

ONBOARDING_WITH_CONTACTS = [
    "Hi, my name is Carlos",
    "I'm a data analyst, been in Vancouver for 6 months",
    "I've been applying but mostly silence so far",
    "I do have a few contacts — a former colleague who moved here 2 years ago",
    "My biggest challenge is knowing how to reach out without feeling like a burden",
]

POST_CALL_REFLECTION = [
    "Hola",
    "Soy Ana, analista financiera, 4 meses en Toronto",
    "Ya tengo aplicaciones enviadas, tengo un contacto: Rodrigo, director de finanzas en Deloitte",
    "Acabo de tener una conversación con Rodrigo, fue bastante buena",
    "Hablamos como 45 minutos, me preguntó mucho sobre mi experiencia en México",
    "Sí ofreció presentarme a alguien de su equipo sin que yo se lo pidiera",
]


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "onboarding"

    if mode == "r9":
        phone, replies = run_scenario(
            "R9 Framing — Spanish onboarding, no contacts",
            ONBOARDING_NO_CONTACTS,
        )
        check_r9(replies)

    elif mode == "contacts":
        run_scenario(
            "Onboarding — English, has contacts",
            ONBOARDING_WITH_CONTACTS,
        )

    elif mode == "reflection":
        run_scenario(
            "Post-call reflection — R7 Socratic check",
            POST_CALL_REFLECTION,
        )

    else:
        phone, replies = run_scenario(
            "Onboarding — Spanish, no contacts (default)",
            ONBOARDING_NO_CONTACTS,
        )
        check_r9(replies)

    print(f"\n{SEPARATOR}")
    print("Done. Check Firestore to verify user doc was written correctly.")
    print(SEPARATOR)
