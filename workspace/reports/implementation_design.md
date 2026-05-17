# Implementation Design

## learning_since_last_interaction

### user_research_insights

Three interviews completed (P1, P2, P3 — two Track B transitioned, one Track A actively navigating).

The most significant finding came from P3, the only Track A participant: **emotional load management is the #1 missing resource** — not tactics, not templates, not LinkedIn tips. P3 named it explicitly: "la carga emocional es lo más importante porque sin energía el resto pierde importancia." This wasn't a retrospective observation — it came from inside the active struggle.

Secondary findings that sharpen the product scope:
- The LATAM→Canada mental model mismatch is confirmed across all three participants (T1)
- Social anxiety layered on top of cultural inhibition ("no quiero molestar") creates a more severe barrier for Track A users than originally assumed — they need a warmer, lower-stakes entry point (T2)
- "Remove networking" is the Track A user's actual ideal — the product must be framed as reducing friction from something they can't avoid, not making them better networkers (T11)
- Community is a structural need, not a nice-to-have — P2 named it "fundamental" (T10)
- The Persica model (Iranian newcomers, volunteer mentors, bookable via app) is a reference architecture worth studying — AI companion as prep + follow-up layer around human mentor sessions, not a replacement (T6)

Two interviews still to conduct (P1's wife, P3 referrals). Pending questions: does "remove networking" appear in other Track A users (if yes, framing shifts fundamentally), and does community come up at 3+ participants (if yes, belongs in v1 scope).

### evaluation_testing_results

All 10 test cases run against prompt v2. Overall rating: 1.5/5. Two risk categories:

**R1 — Multi-connection misclassification (avg 2.0/5 — partial failures):**
- When multiple connection types are present, the navigator blends them instead of committing to one (TC01, TC05)
- The connection type taxonomy has gaps: no category for personal warmth/existing friendship (TC02), cross-cultural immigrant solidarity (TC04), or existing mentorship/supervisory relationships (TC05)
- Weak domain overlaps are treated as real connection types — no "weak connection" qualifier exists (TC03)

**R7 — Relationship depth blindness (avg 1.0/5 — systematic structural failure):**
- The prompt has no post-call framework. Zero. All five R7 cases failed for the same reason.
- Navigator cannot distinguish an unprompted introduction offer (depth signal) from professional politeness (not a depth signal)
- Vague post-call notes ("it was really good") trigger generic follow-up suggestions instead of excavation prompts

### prompt_experimentation_findings

The prompt (v2) was iterated from v1 based on observed failures in the original experiment. v2 holds up well for single-connection cases — the connection type identification logic is solid when one type dominates. The cold outreach path, "about me" pitch consistency, and WHY explanation depth all performed above expectations.

What theory got wrong: it was assumed the ranking problem would be rare. Testing revealed it's the norm — real contacts have multiple connection points, and the navigator needs explicit decision rules for that case, not just taxonomy coverage.

The post-call gap was a known unknown from design but its scope was underestimated. It's not a missing section — it's a missing capability that changes the product's fundamental value proposition. Without post-call reflection, the navigator helps users have better first calls and worse long-term relationships.

### implementation_progress_status

No code written yet. The current implementation artifact is a prompt (testing_prompt.txt v2) being run manually in Claude.ai. There is no deployed system, no API integrations, no interface.

What's working: the core reasoning logic in the prompt — connection type identification, WHY explanations, conversation script structure. These are validated and should be preserved in implementation.

Where things stand: two structural prompt fixes are needed before implementation adds value — post-call framework (P1 priority) and expanded connection type taxonomy (P2 priority). Building on the current prompt without these fixes would ship the wrong product.

### updated_quality_risk_focus

The two co-priority risks (R1, R7) are confirmed, but **R7 is now the higher-leverage fix**:
- Adding the post-call framework alone would raise overall scores from 1.5/5 to ~2.5/5
- R7 is also the risk most aligned with the product's core identity: not "prep for one call" but "build meaningful relationships over time"
- R1 fixes (taxonomy expansion + ranking rules) are well-understood and surgical; R7 requires rethinking the product's interaction model

A new risk emerged from user research that wasn't in the original evaluation framework and now takes top priority: **R9 — Framing mismatch for Track A users.** If the product presents itself as a "networking companion," Track A users (who want to remove networking entirely) may never engage. This is a delivery/framing risk, not a prompt quality risk — but it's the most foundational because it determines whether users open the product at all. R7 and R1 fixes are irrelevant if R9 isn't solved first.

**Updated quality risk priority order:**
1. **R9** — Framing mismatch for Track A users (if they don't engage, nothing else matters)
2. **R7** — Relationship depth blindness (structural gap in post-call experience; highest-leverage prompt fix)
3. **R1** — Multi-connection misclassification (surgical taxonomy + ranking rule fixes)

---

## delivery_context_design

### workflow_analysis

**Pain points in the current user process:**
- No post-call reflection at all — newcomers disappear after call #1 with no structure for what just happened
- Decision paralysis about who to contact next — they stare at LinkedIn with no idea where to start
- No visibility into progress — can't see momentum even when it's building, leads to quitting
- Onboarding to a new digital tool adds friction — Track A users have social anxiety and won't seek out a product

**Flow points:**
- WhatsApp — Latino newcomers already use it as their primary communication channel; it's how they message family, friends, and community. Zero learning curve.
- In-person settlement org events (WILL Employment, etc.) — these are already trusted touchpoints where newcomers show up voluntarily

**Key insight:** The existing flow is social and messaging-based, not app-based. The tool needs to enter through a trusted channel (the settlement org) and live inside an already-used medium (WhatsApp), not ask users to adopt a new app.

### delivery_mechanism

**MVP (Sprint 2):** WhatsApp bot powered by Claude API.

**Sprint 3:** Web app for mentor discovery and booking (modeled on the Persica approach — volunteer mentors, bookable sessions, AI companion as prep + follow-up layer around human mentor sessions).

Distribution: settlement orgs (WILL Employment and equivalents) share the WhatsApp number at events. Secondary channel: referral from newcomers who've already used it ("este bot me ayudó antes de mi coffee chat").

### interaction_model

The WhatsApp bot lives at the intersection of proactive and conversational. It finds the user at the right moment — it doesn't wait to be opened.

The word **"networking" never appears** in the WhatsApp interface. The bot doesn't present itself as a networking tool. It presents itself as a companion that checks in after conversations, suggests who to talk to, and teaches professional etiquette through conversation — naturally, in Spanish or English.

### agency_vs_autonomy

**Autonomous (bot acts without being asked):**
- Sends a gentle pre-chat nudge the evening before a registered conversation
- Checks in 1–2 hours after a scheduled coffee chat ("¿Cómo te fue?")
- Suggests the next person to connect with based on goals and relationship history
- Sends an etiquette tip when relevant (first time they're doing a cold reach-out, first VP-level chat, etc.)
- Celebrates milestones ("Ya completaste 5 conversaciones — eso es momentum real")

**Agency (user makes the call):**
- User decides whether to act on a suggested next contact
- User writes all outreach messages — bot scaffolds, never drafts
- User decides next steps after post-call reflection prompts
- User chooses whether to book a mentor (Sprint 3) when the bot surfaces the option
- User sets language preference (Spanish/English) at onboarding — bot respects it throughout

### user_touchpoints

**Entry:**
- Settlement org shares WhatsApp number at event, or newcomer receives referral from a peer
- User sends first message → bot responds in their chosen language

**Onboarding (WhatsApp, ~3–4 exchanges):**
- Language preference (Spanish or English)
- Name, professional field, how long in Canada
- One question: "¿Cuál es tu mayor reto ahora mismo en tu búsqueda?" — surfaces emotional state and starting point

**Pre-chat nudge (autonomous):**
- Evening before a registered conversation: brief, warm, in their language
- e.g., *"Hola [Name], mañana hablas con [Contact]. ¿Quieres que repasemos algo antes?"*
- User can say yes (bot asks 2–3 questions to surface prep points) or no (bot wishes them luck)

**Post-chat check-in (autonomous — this is the R7 fix):**
- 1–2 hours after scheduled time: *"¿Cómo te fue con [Contact]?"*
- Bot asks Socratic reflection questions based on what the user shares
- Flags depth signals without labeling them prescriptively
- User arrives at their own insight about whether to pursue the relationship further

**Between chats:**
- Bot suggests next person to connect with ("Hay alguien en tu red que podría ser un buen siguiente paso...")
- Etiquette coaching surfaced contextually, not as a course

**Milestones:**
- Bot celebrates progress at meaningful checkpoints — framed around relationship quality, not just volume

**When ready for a human mentor (Sprint 3 hook):**
- Bot surfaces the mentor option at the right moment ("¿Has pensado en hablar con alguien que ya pasó exactamente por esto?")
- Links to web app for discovery and booking

### user_journey_notes

P3's journey (Track A, the hardest case): Attends a WILL Employment event. Facilitator mentions a WhatsApp number at the end. She texts it that evening because it's zero friction — she's already on WhatsApp. Bot responds in Spanish. Three questions. No mention of "networking." Next morning the bot sends a warm message. Over the following week, the bot checks in after two conversations she was already having. She starts to feel like something is tracking her progress even though she doesn't feel like a "networker." That's the transformation.

### integration_touchpoints

- **Where automation starts:** WhatsApp message received from user (or scheduled trigger for proactive nudges)
- **What user provides:** Contact name + scheduled time (to enable pre/post nudges); post-call notes (free-form text)
- **What user receives:** Reflection prompts, etiquette coaching, next-contact suggestions, milestone celebrations — all via WhatsApp
- **Where automation ends:** User writes their own outreach messages, decides who to contact, makes all relationship decisions

---

## backend_design

### technical_approach

Sandra is a senior ML engineer with production GCP/Cloud Run experience. Architecture is presented at full technical depth. The stack is an extension of her existing tooling — no new infrastructure primitives required.

### data_flow_architecture

**Inbound message flow:**
```
User sends WhatsApp message
→ Twilio webhook POST → Cloud Run (FastAPI)
→ Respond 200 immediately (async via BackgroundTasks)
→ Load user document from Firestore (profile + summary + last 5 messages)
→ Load active contact document if message references a known contact
→ Build Claude prompt: system prompt + user profile + linkedin context + conversation_summary + last 5 exchanges + contact context
→ Claude API call (claude-sonnet-4-6)
→ Parse response
→ Write assistant message to Firestore messages subcollection
→ Periodically update conversation_summary (every 10 exchanges or on significant events)
→ Send reply via Twilio WhatsApp API
```

**Proactive nudge flow:**
```
Cloud Scheduler (cron: nightly + post-chat check)
→ Cloud Run job
→ Query Firestore: users with scheduled_chat_at = tomorrow / chats ended 2h ago with no post-call notes
→ Per eligible user: build nudge prompt + Claude API → send WhatsApp via Twilio
→ Update Firestore: nudge_sent_at timestamp
```

### firestore_data_model

```
users/{whatsapp_number}:           # WA number IS the identity — no auth layer needed
  name: string
  field: string
  language: "es" | "en"
  time_in_canada: string
  linkedin_url: string (optional)
  conversation_summary: string      # Claude-maintained, updated every ~10 exchanges
  current_goal: string
  current_state: string             # Claude-inferred and persisted (see state lifecycle below)
  last_active: timestamp

users/{whatsapp_number}/contacts/{contactId}:
  name: string
  role: string
  company: string
  linkedin_url: string (optional)
  scheduled_chat_at: timestamp (optional)
  post_call_notes: string (optional)
  depth_signals: string             # Claude-generated reflection, updated post-call
  nudge_sent_at: timestamp (optional)
  created_at: timestamp

users/{whatsapp_number}/messages/{messageId}:
  role: "user" | "assistant"
  content: string
  contact_id: string (optional)    # links message to contact context when relevant
  timestamp: timestamp

users/{whatsapp_number}/milestones/{milestoneId}:
  type: string                      # e.g. "first_chat_completed", "first_followup_sent", "first_second_meeting"
  achieved_at: timestamp
  celebrated: bool                  # prevents double-celebration on retry
```

WhatsApp number is the primary key — no login, no auth, no session tokens. The number is the identity.

**State lifecycle (Claude-inferred, Firestore-persisted):**

Claude reads `current_state` from Firestore on each turn and the full hybrid context. It infers whether the user's state has changed — based on conversation, onboarding answers, and what the user reports. If Claude detects a state transition, it writes the new state to Firestore and writes a milestone record, then celebrates with the user in the same reply.

```
onboarding
  → first_contact_registered     (user adds their first contact)
  → first_chat_scheduled         (first coffee chat has a date)
  → first_chat_completed         (user reports back after first chat)
  → building_momentum            (3+ chats completed)
  → deepening_relationships      (first second meeting scheduled)
```

State is also used by Cloud Scheduler queries — proactive nudge jobs filter on `current_state` and contact fields (e.g., don't send pre-chat nudge to users still in `onboarding`).

### context_window_management

**Hybrid strategy: summary + last 5 exchanges**

What Claude receives per request:
1. System prompt (static, prompt-cached)
2. User profile fields (name, field, language, time in Canada, LinkedIn if provided)
3. `conversation_summary` — Claude-maintained rolling summary of older history
4. Last 5 message pairs from Firestore (most recent exchanges)
5. Active contact document (if the current message is contact-specific)

Summary update trigger: every 10 exchanges, or when a contact's post-call reflection completes. Claude writes the new summary as part of a background task — it does not block the reply.

Per-contact history is preserved in the contact document (`post_call_notes`, `depth_signals`) so R7 reflection quality is maintained across multiple conversations about the same person, even after older messages are no longer in the rolling window.

### integration_points

| Service | Purpose | SDK |
|---|---|---|
| Twilio WhatsApp API | Send/receive WhatsApp messages | `twilio` Python SDK |
| Claude API (Anthropic) | Conversation, reflection, coaching | `anthropic` Python SDK |
| Firestore | User state, contact registry, message history | `google-cloud-firestore` |
| Cloud Run | Webhook handler + nudge job | Existing deployment pattern |
| Cloud Scheduler | Trigger proactive nudge jobs | GCP console / Terraform |

### integration_notes

- **Twilio webhook timing:** Must respond HTTP 200 within 15s or Twilio retries. FastAPI `BackgroundTasks` handles Claude call + Firestore writes async; endpoint returns 200 immediately.
- **Idempotency:** Check Twilio `MessageSid` before processing — Twilio may deliver duplicates on retry.
- **Prompt caching:** System prompt is static and long — cache with `cache_control: ephemeral` to reduce latency and cost on every turn.
- **LinkedIn fields:** Optional on both user and contact. When present, included in Claude context to enrich connection type reasoning (feeds R1 fix).

### decision_points

Claude infers state from the full hybrid context (profile + stored `current_state` + summary + last 5 exchanges). It determines: what state is the user in right now, has the state changed, and what kind of response is needed (onboarding question, prep, post-call reflection, etiquette coaching, milestone celebration, or general support).

**State transition pattern (per turn):**
1. Claude reads `current_state` and full context
2. Claude generates reply
3. If Claude detects state change → structured output includes: `new_state`, `milestone_type`, response text
4. Backend writes `new_state` to user document + new milestone record (with `celebrated: false` → flip to `true` after send)
5. Celebration is woven into the reply, not a separate message

Key branching logic Claude handles:
- Language: set at onboarding, stored in user profile, referenced in every prompt — Claude always responds in the user's chosen language
- Contact routing: if user message names a known contact (fuzzy match on stored contact names), load that contact's document into context
- State transition detection: Claude compares inferred current state against stored `current_state` and flags changes
- Nudge eligibility: determined by Cloud Scheduler query on Firestore fields, not by Claude at reply time

### deferred_design_considerations

**Planning style personalization:** Some users (Track B) want to see the full roadmap upfront — all the steps, a clear plan, a target. Others (Track A) feel overwhelmed by this and disengage. This is an important UX dimension but not MVP scope.

For MVP: a single onboarding question captures preference — *"¿Prefieres que te vaya guiando paso a paso, o te ayuda ver el camino completo primero?"* — stored as `planning_style: "step_by_step" | "big_picture"` in the user document. Claude adjusts how much it reveals at once based on this flag. No extra engineering — just prompt behavior. Full personalization of the roadmap experience is a v2 design problem.

### human_judgment_points

- **Next contact suggestion:** Claude proposes one specific person and explains why; user decides whether to act
- **Pre-chat prep opt-in:** Bot offers prep the evening before; user says yes or no — no prep is pushed unsolicited
- **Post-call reflection:** Bot asks Socratic questions; user arrives at their own insight about relationship depth — bot never labels a contact as "mentor potential" prescriptively (R7 fix)
- **Outreach messages:** Bot scaffolds structure and key points; user writes every word — nothing is sent on their behalf

---

## mvp_scope_definition

### first_implementation_target

A working WhatsApp bot that onboards a Track A Spanish-speaking newcomer without ever using the word "networking," prepares them for one coffee chat, and checks in after the chat with Socratic reflection questions. The goal is not a polished product — it is evidence that R9, R7, and R1 are or aren't risks in practice.

### core_path_only

```
User texts WhatsApp number
→ Bot greets → user picks language (es/en)
→ Onboarding: 4 questions (name, field, time in Canada, current challenge)
→ User describes a contact + scheduled chat date/time
→ Bot reasons about connection type → prep questions with WHY explanations  [tests R1]
→ Cloud Scheduler fires 8pm the evening before → pre-chat nudge             [tests R9]
→ Cloud Scheduler fires 2h after scheduled chat time → "¿Cómo te fue?"     [tests R9 + R7]
→ User responds → bot asks Socratic reflection questions                    [tests R7]
```

One user. One contact. One coffee chat. One post-call reflection. That loop is the MVP.

### feature_justification

| Feature | Tests which risk? | Verdict |
|---|---|---|
| Bilingual onboarding (es/en) | R9 — framing must work in Spanish from day one | ✅ In |
| No "networking" language in any message | R9 — Track A user engagement | ✅ In |
| Contact intake + connection type reasoning | R1 — multi-connection misclassification | ✅ In |
| Prep questions with WHY explanations | R1 — does it teach or just instruct? | ✅ In |
| Pre-chat nudge (Cloud Scheduler, 8pm) | R9 — "something that finds you" | ✅ In |
| Post-chat check-in (Cloud Scheduler, +2h) | R7 — user won't self-trigger; bot must find her | ✅ In |
| Socratic post-call reflection | R7 — depth signal recognition without labeling | ✅ In |
| Claude infers + saves state | Core behaviour, no extra infra | ✅ In |
| LinkedIn fields | Doesn't change R9/R7/R1 test | ❌ Deferred |
| Conversation summary generation | Overkill for 1-2 test users | ❌ Hardcoded (last 10 messages) |
| Milestone records in Firestore | Claude celebrates inline | ❌ Deferred |
| planning_style preference | Design consideration, not quality risk test | ❌ Deferred |
| Web app / mentor booking | Sprint 3 | ❌ Out |

### hardcoded_elements

- **Conversation history:** last 10 messages stored as array in user document — no summary generation, no subcollection queries
- **Nudge eligibility:** Cloud Scheduler queries Firestore directly — no LLM call to decide who gets a nudge
- **Single contact for MVP:** user registers one contact at a time — no contact list management UI
- **No admin dashboard:** Sandra reads Firestore directly to monitor conversations
- **No error recovery flows:** basic retry on Claude API failure, simple fallback message

### definition_of_done

- [ ] A real Track A user (Spanish-speaking, active job searcher, no role yet in field) texts the WhatsApp number and completes onboarding in Spanish
- [ ] User registers one contact with a scheduled chat date and time
- [ ] Bot generates prep questions with WHY explanations tailored to the connection type
- [ ] Pre-chat nudge fires automatically the evening before — no manual trigger by Sandra
- [ ] Post-call check-in fires automatically 2 hours after the scheduled chat time
- [ ] Bot responds to post-call notes with Socratic reflection questions (not declarations)
- [ ] The word "networking" appears zero times in any bot message
- [ ] Sandra can read the full conversation transcript and score R9, R7, R1 quality

### implementation_platform_selection

**Platform:** Pure Python — FastAPI + Anthropic SDK + Firestore + Twilio on Cloud Run

**Rationale:** Sandra's existing stack extended. She has already shipped to Cloud Run with Google ADK — the deployment pattern, Firestore, and GCP tooling are all familiar. Using them here means zero new infrastructure primitives to learn during a 15-day sprint. Maximum control over prompt assembly, context management, and Claude tool use. The architecture is clean and explainable in a blog post or technical interview.

**Trade-offs discussed:**
- n8n considered and rejected: visual workflow tools hide the interesting engineering. Not appropriate for someone targeting senior AI/ML engineering roles — the portfolio story is weaker.
- LangGraph considered and rejected: good for complex state graphs, but Firestore + Cloud Scheduler already handle state management for this architecture. Adding LangGraph would introduce a framework dependency without a clear benefit.
- Google ADK considered: Sandra has prior experience, but ADK is optimized for multi-agent systems. A single WhatsApp bot with a clean webhook architecture doesn't benefit from ADK's agent coordination features.

**Alternative platforms considered:** LangGraph, n8n, Google ADK — all passed over in favour of the minimal, production-grade approach.

**Implementation timeline assessment:** ~12 hours total at Sandra's experience level. Achievable within the Sprint 2 window with focused sessions.

### deferred_features

| Feature | Why deferred |
|---|---|
| LinkedIn fields on user + contact | Not needed for first 1-2 users; add before Sprint 3 |
| Conversation summary (rolling) | Last 10 messages sufficient for MVP user volume |
| Milestone records in Firestore | Claude inline celebration is enough to validate the behaviour |
| planning_style preference question | UX refinement, not a quality risk test |
| Multiple contacts per user | One contact loop is enough to test all three risks |
| Web app + mentor booking | Sprint 3 |
| Spanish native-speaker phrasing validation | Run the conversation, collect feedback, iterate prompt |
| Proactive next-contact suggestions | Requires relationship history across contacts; Sprint 3 |
