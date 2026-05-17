# MVP Technical Specifications
# Newcomers Navigator — WhatsApp Bot (Sprint 2)

**Platform:** Pure Python — FastAPI + Anthropic SDK + Firestore + Twilio  
**Deployment:** Cloud Run (existing pattern from CookFlow)  
**Quality risks being tested:** R9 (framing), R7 (post-call reflection), R1 (connection type reasoning)

---

## development_requirements

```
Python 3.11+
fastapi
uvicorn
anthropic                  # Claude API
twilio                     # WhatsApp send/receive
google-cloud-firestore     # State and conversation persistence
python-dotenv              # Local env vars
```

**Environment variables required:**
```
ANTHROPIC_API_KEY=
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_WHATSAPP_NUMBER=    # e.g. whatsapp:+14155238886
FIRESTORE_PROJECT_ID=
CLOUD_SCHEDULER_SECRET=    # Simple shared secret to authenticate scheduler calls
```

**Project structure:**
```
app/
  main.py              # FastAPI app, route definitions
  webhook.py           # Twilio inbound message handler
  jobs.py              # Cloud Scheduler job endpoints
  claude_client.py     # Claude API wrapper, prompt assembly, tool handling
  firestore_client.py  # All Firestore read/write operations
  twilio_client.py     # Twilio send message wrapper
  prompts.py           # System prompt template
  models.py            # Pydantic models for Firestore documents
Dockerfile
requirements.txt
.env.example
```

---

## integration_specifications

### Twilio WhatsApp

**Inbound (webhook):**
- Twilio POSTs to `POST /webhook/twilio`
- Form-encoded body with fields: `From` (e.g. `whatsapp:+15551234567`), `Body` (message text), `MessageSid`
- Must return HTTP 200 with empty TwiML body within 15 seconds
- Process Claude call in `BackgroundTasks` — never block the webhook response

**Outbound (send message):**
```python
from twilio.rest import Client

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
client.messages.create(
    from_=TWILIO_WHATSAPP_NUMBER,
    to=user_phone,          # e.g. "whatsapp:+15551234567"
    body=message_text
)
```

**Idempotency:** Check `MessageSid` against a processed set in Firestore before processing — Twilio may retry on timeout.

### Anthropic Claude API

**Model tiering (cost optimization):**
- `claude-haiku-4-5-20251001` — onboarding, simple nudges, milestone celebrations, next-contact suggestions
- `claude-sonnet-4-6` — post-call reflection (R7) and connection type reasoning (R1) where coaching quality is the product

Pass the model as a parameter to `claude_client.py` so callers choose the tier; default to Haiku for nudge jobs, Sonnet for inbound message processing where full reasoning may be needed.

**Prompt caching:** The static system prompt section must use `cache_control: {"type": "ephemeral"}` to reduce latency and cost on every turn.

**Tool use:** Claude uses one tool — `update_state` — to signal state transitions and contact updates. This is the only mechanism for structured side effects; the message text is always natural language.

```python
tools = [
    {
        "name": "update_state",
        "description": "Call this when you detect the user's state has changed, or when you have new information to save about a contact after a post-call reflection.",
        "input_schema": {
            "type": "object",
            "properties": {
                "new_state": {
                    "type": "string",
                    "enum": [
                        "onboarding",
                        "first_contact_registered",
                        "first_chat_scheduled",
                        "first_chat_completed",
                        "building_momentum",
                        "deepening_relationships"
                    ],
                    "description": "The new user state. Only include if state has changed."
                },
                "milestone_type": {
                    "type": "string",
                    "description": "The milestone to record, e.g. 'first_chat_completed'. Only include if a milestone was just reached."
                },
                "contact_updates": {
                    "type": "object",
                    "description": "Fields to update on the active contact document. E.g. {\"depth_signals\": \"...\", \"post_call_notes\": \"...\"}. Only include if there are contact updates."
                }
            }
        }
    }
]
```

**Tool handling pattern:**
1. Send message to Claude with tools defined
2. If Claude returns `tool_use` block: extract `update_state` inputs, write to Firestore, then continue the conversation with `tool_result` to get the final text response
3. Send final text response via Twilio

### Firestore

**Collection structure:**
```
users/{phone_number}                    # phone_number is E.164 without "whatsapp:" prefix
  name: str
  field: str
  language: "es" | "en"
  time_in_canada: str
  current_challenge: str
  current_state: str                    # default: "onboarding"
  messages: list[dict]                  # [{role, content, timestamp}] — capped at 10
  last_active: timestamp

users/{phone_number}/contacts/{contact_id}    # contact_id = slugified name
  name: str
  role: str
  company: str
  connection_context: str               # free-text user description of relationship
  scheduled_chat_at: timestamp | None
  pre_nudge_sent_at: timestamp | None
  post_nudge_sent_at: timestamp | None
  post_call_notes: str | None
  depth_signals: str | None             # Claude-written after post-call reflection
  created_at: timestamp
```

**Message history cap:** When appending a new message, if `len(messages) >= 10`, remove the oldest entry before appending. Store as a Firestore array field on the user document.

---

## data_flow_specifications

### Inbound message processing

```
POST /webhook/twilio
  → Extract From (phone), Body (text), MessageSid
  → Return 200 immediately
  → BackgroundTasks: process_message(phone, text, message_sid)
      → Check MessageSid not already processed (idempotency)
      → Load user doc from Firestore (or create if new)
      → Load active contact doc if user has a contact registered
      → Build Claude messages array:
          [
            {"role": "user", "content": text}  # current message appended to history
          ]
      → Call Claude with: system_prompt + user context + contact context + messages
      → Handle tool_use if present (write to Firestore)
      → Extract final text response
      → Append both user message and assistant response to messages array in Firestore
      → Send response via Twilio
```

### Context assembly (claude_client.py)

```python
def build_context(user: UserDoc, contact: ContactDoc | None) -> str:
    """Injected as a user turn before the conversation history."""
    parts = [
        f"[USER PROFILE]",
        f"Name: {user.name}",
        f"Field: {user.field}",
        f"Language: {user.language}",
        f"Time in Canada: {user.time_in_canada}",
        f"Current challenge: {user.current_challenge}",
        f"Current state: {user.current_state}",
    ]
    if contact:
        parts += [
            f"\n[ACTIVE CONTACT]",
            f"Name: {contact.name}, {contact.role} at {contact.company}",
            f"Connection context: {contact.connection_context}",
            f"Chat scheduled: {contact.scheduled_chat_at}",
            f"Post-call notes: {contact.post_call_notes or 'none yet'}",
        ]
    return "\n".join(parts)
```

Context is injected as the first message in the conversation (role: "user") so it is always in scope without polluting the system prompt with dynamic content.

### Output format

Claude sends natural language only. Structured updates happen exclusively via the `update_state` tool. The backend never parses the message text for state signals.

---

## platform_implementation_requirements

### FastAPI app (main.py)

```python
app = FastAPI()
app.add_route("/webhook/twilio", webhook_router)
app.add_route("/jobs/pre-chat-nudge", jobs_router)
app.add_route("/jobs/post-chat-checkin", jobs_router)
```

### Cloud Scheduler jobs

**Pre-chat nudge — fires 8pm daily:**
```
Schedule:  0 20 * * *
Target:    GET https://{cloud-run-url}/jobs/pre-chat-nudge
Auth:      Add header X-Scheduler-Secret: {CLOUD_SCHEDULER_SECRET}
```

Job logic:
1. Query Firestore: all contacts where `scheduled_chat_at` is between `now + 12h` and `now + 36h` AND `pre_nudge_sent_at` is null
2. For each match: load user doc → build nudge prompt → Claude → Twilio → write `pre_nudge_sent_at`

**Post-chat check-in — fires every hour:**
```
Schedule:  0 * * * *
Target:    GET https://{cloud-run-url}/jobs/post-chat-checkin
Auth:      Add header X-Scheduler-Secret: {CLOUD_SCHEDULER_SECRET}
```

Job logic:
1. Query Firestore: all contacts where `scheduled_chat_at` is between `now - 3h` and `now - 1h` AND `post_nudge_sent_at` is null
2. For each match: load user doc → build check-in prompt → Claude → Twilio → write `post_nudge_sent_at`

### Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ ./app/
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

---

## system_prompt_specification

The system prompt is the most critical artifact. It determines R9, R7, and R1 quality directly.

**Structure:**
```
[IDENTITY AND ROLE]
[LANGUAGE RULES]
[CONVERSATION FLOWS]
  - Onboarding flow
  - Contact intake and prep flow
  - Pre-chat nudge flow
  - Post-call reflection flow
[QUALITY CONSTRAINTS]
[STATE TRANSITION RULES]
```

**Identity and role (critical for R9):**
```
You are a warm, bilingual companion for professionals navigating the Canadian job market.
You help people prepare for professional conversations, reflect on what happened, and
recognize when a connection has real potential.

NEVER use the word "networking" or "network" in any message. Instead use:
- "professional conversations" / "conversaciones profesionales"
- "café chats" / "conversaciones de café"
- "conocer personas" / "connecting with people"
- "tu próxima conversación"

You are not a coach, not a mentor. You are a peer who has been through it and knows
the Canadian professional context well. Your tone is warm, direct, and never corporate.
```

**Language rules:**
```
The user set their language preference during onboarding. It is stored in their profile
as "es" or "en". ALWAYS respond in that language for every message, including proactive
nudges. Never switch languages mid-conversation unless the user explicitly asks you to.
```

**Post-call reflection rules (critical for R7):**
```
When a user shares notes after a professional conversation, your job is to help them
reflect — not to evaluate the relationship for them.

Ask Socratic questions only. Examples of correct behaviour:
✓ "¿Hubo algo que dijo que te sorprendió?"
✓ "¿Sentiste que querías seguir hablando con ella?"
✓ "¿Ofreció algo sin que se lo pidieras?"

Never declare relationship potential:
✗ "Esta persona tiene potencial de mentora."
✗ "This sounds like a strong mentor candidate."
✗ "You should definitely keep this relationship going."

If the user's notes are vague ("fue buena conversación"), ask excavation questions first:
"¿Qué fue lo que hizo que se sintiera buena? ¿Hubo un momento específico que recuerdas?"
```

**Connection type reasoning rules (critical for R1):**
```
When a user describes a contact, identify the primary connection angle. If multiple
connection types are present, you MUST choose one and name your reasoning explicitly.

Connection type hierarchy when multiple are present:
1. Existing relationship (friend, former colleague, supervisor) — always leads
2. Cultural / immigrant experience in Canada (regardless of specific culture)
3. Shared professional journey (academia→industry, career pivot, same sector)
4. Domain overlap (same or adjacent field)
5. Event / context (met at an event, LinkedIn group)

Weak connection rule: if the only overlap is cross-sector domain (e.g., "both work with
data" but in completely different industries), do not treat this as a domain connection.
Frame prep around genuine curiosity and sector learning instead.

Always state which connection angle you chose and briefly explain why.
Prep questions must be built entirely around the chosen angle — do not split across
multiple connection types.
```

**State transition rules:**
```
After each user message, assess whether their state has changed. Call update_state
if and only if:
- A new contact has been registered (→ first_contact_registered)
- A chat date/time has been confirmed (→ first_chat_scheduled)
- The user reports back after a chat (→ first_chat_completed, or building_momentum if 3+)
- A second meeting with a contact is scheduled (→ deepening_relationships)

When a state transition occurs, weave a brief, warm celebration into your response
before moving on. Make it feel like a friend noticing something real, not a system
congratulating you.
✓ "Oye — acabas de tener tu primera conversación de café. Eso es real."
✗ "Congratulations! You have reached the 'first_chat_completed' milestone!"
```

---

## human_in_loop_requirements

- User opts in or out of pre-chat prep in response to the evening nudge (yes/no reply)
- User writes all outreach messages — bot provides structure only
- User logs post-call notes in their own words — bot asks questions, never summarizes for them
- No message is ever sent to a third party on behalf of the user

---

## quality_risk_testing_specifications

### R9 — Framing mismatch

**Test:** Show conversation transcript to someone unfamiliar with the product.
**Pass criteria:** They cannot identify the word "networking" anywhere. The bot reads as a peer companion, not a coaching product.
**Failure signal:** Any use of "networking," "network," or corporate coaching language.

### R7 — Relationship depth blindness

**Test:** Run post-call reflection with the R7 test cases from `data/evaluations_data.csv` (TC01–TC05).
**Pass criteria:** All reflection questions are Socratic (questions, not declarations). Vague notes trigger excavation questions. The false-positive case (David, no depth signals) does not generate "mentor potential" language.
**Failure signal:** Any declarative statement about relationship potential. Generic follow-up suggestions without prior excavation.

### R1 — Multi-connection misclassification

**Test:** Run contact intake with R1 test cases from `data/evaluations_data.csv` (TC01–TC05).
**Pass criteria:** Claude names the chosen connection angle and its rationale. Prep questions are built entirely around one angle. A contact with only one connection type would get meaningfully different prep.
**Failure signal:** Blended questions across multiple connection types. No explicit naming of the chosen angle.

---

## error_handling_requirements

- **Twilio webhook timeout:** Always return 200 immediately; all processing in BackgroundTasks
- **Duplicate webhook:** Check `MessageSid` in a Firestore `processed_messages` collection before processing
- **Claude API failure:** Retry once with 2s delay; if second attempt fails, send fallback message: `"Algo salió mal de mi lado — intenta de nuevo en un momento."` / `"Something went wrong on my end — try again in a moment."`
- **Scheduler job auth:** Verify `X-Scheduler-Secret` header on all job endpoints; return 403 if missing or wrong

---

## success_criteria_and_testing

**End-to-end test sequence (do this before inviting real users):**

1. Text the WhatsApp number from a test phone
2. Complete onboarding in Spanish — verify language persists
3. Register a contact with a scheduled chat time set to 30 minutes from now
4. Manually call `/jobs/pre-chat-nudge` — verify nudge arrives
5. Update `scheduled_chat_at` to 2 hours ago in Firestore — call `/jobs/post-chat-checkin` — verify check-in arrives
6. Reply with post-call notes — verify Socratic reflection questions
7. Read full transcript — verify "networking" never appears
8. Check Firestore — verify `current_state` updated correctly

**First real user test:**
Invite one Track A user (Spanish-speaking, active job searcher). Observe the full loop. Read the transcript. Score R9, R7, R1 using the evaluation rubric in `reports/evaluation_design_report.md`.
