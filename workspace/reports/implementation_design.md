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

**MVP (Sprint 2):** SofIA — a WhatsApp-based AI ally powered by Claude API.

**Sprint 3:** Web app for mentor discovery and booking (modeled on the Persica approach — volunteer mentors, bookable sessions, AI companion as prep + follow-up layer around human mentor sessions).

Distribution: settlement orgs (WILL Employment and equivalents) share the WhatsApp number at events. Secondary channel: referral from newcomers who've already used it ("este bot me ayudó antes de mi coffee chat").

### interaction_model

The WhatsApp bot lives at the intersection of proactive and conversational. It finds the user at the right moment — it doesn't wait to be opened.

The word **"networking" never appears** in early conversations. SofIA doesn't present herself as a networking tool. She presents herself as an ally who checks in after conversations, suggests who to talk to, and teaches professional etiquette through conversation — naturally, in Spanish or English.

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

**Onboarding (WhatsApp, ~4–6 exchanges):**
- Language preference (Spanish or English)
- Name, professional field, how long in Canada, city (used to set timezone for proactive messages)
- Situational assessment — bot calibrates to where the user actually is:
  - "¿Ya estás enviando aplicaciones, o estás en la etapa de explorar el mercado?"
  - If applying: "¿Has tenido respuestas, o has mandado muchas sin resultado?"
  - "¿Tienes algún contacto profesional en Canadá con quien hayas hablado, o estás empezando desde cero?"
- Based on answers: bot determines entry path (has contacts → activate them; no contacts → identify first one)
- One emotional anchor question: "¿Cuál es tu mayor reto ahora mismo?" — surfaces starting point and emotional state

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

P3's journey (Track A, the hardest case — and the transformation arc the product is designed to produce):

1. Hears about the bot — from a settlement org counselor at an event, or from a friend who used it and found it helpful. Trust is transferred: someone she already trusts told her about it.
2. Texts the number. Bot responds in Spanish. Before anything else, it tries to understand where she actually is: Has she started applying? Is she overwhelmed by silence after hundreds of applications? Is she just arriving and doesn't know where to begin? Does she have any professional contacts in Canada at all? The onboarding is situational — the bot calibrates everything that follows to her current reality, not a generic starting point.
3a. If she has contacts: bot helps her identify the strongest first conversation and prepares her for it.
3b. If she has no contacts: the bot guides her through LinkedIn step by step — how to search for alumni from her university or former employer who are now in Canada, how to use filters to find people in her field. It helps her identify one realistic first contact. Before scripting the outreach, the bot helps her write her About Me — a 3–4 sentence professional summary that captures who she is, what she did, and what she's looking for. The bot explains that both the About Me and outreach messages will be written in English — not as a rule, but as advice: writing them in English is one of the fastest ways to absorb Canadian professional etiquette, the tone, the structure, how to ask for something without sounding too direct or too formal. The rest of the conversation stays in Spanish. She confirms the About Me, it's saved to her profile, and from that point on it's reused in every coffee chat prep without her having to explain herself again. She can update it any time she asks. Then the bot scripts the first cold outreach in English using her About Me and the shared connection point — and frames the ask as low-stakes: the goal is just a conversation.
4. Bot sends a warm pre-chat nudge the evening before her first coffee chat.
5. 2 hours after the chat: *"¿Cómo te fue?"* — Socratic reflection questions follow.
6. Over the following weeks, the bot checks in after conversations she's already having. She starts to feel she is progressing — not because she's "networking," but because something is tracking her momentum and she can feel it building.
6b. After each coffee chat, the sequence of giving back unfolds over two days. The same evening, after the post-call reflection, the bot suggests one specific action: share an article on a topic the contact mentioned, comment on or re-share one of their LinkedIn posts, or send a message sharing how something they said helped her. The next morning, a separate nudge arrives: "Did you send [name] a thank-you note?" — the bot offers to draft it in English, personalised to what was discussed. Not generic. Not the same day. The right message at the right moment.
7. After a few strong coffee chats, the bot introduces the concept of mentorship: some of the people she's been talking to may be becoming something more than contacts — people who are genuinely invested in her success. The bot explains what an informal mentor is, how to recognize one (they follow up, they offer help without being asked, they share their own story), and why it matters — a mentor can accelerate your integration, open doors you didn't know existed, and help you navigate a professional culture that wasn't designed with you in mind. The concept is introduced through her own experience, not as theory.
8. She starts to understand what networking actually is — not through explanation, but through lived experience. She has met people who are genuinely curious about her. The concept becomes real.
9. She is no longer afraid to use the word "networking" — because she now understands that her objective is to build meaningful relationships, not to collect contacts.
10. She starts getting interviews. The first one doesn't go well — she feels frustrated. The bot helps her reflect: who in her network could she reach out to debrief, understand what happened, and know what to improve for next time. Her network becomes a resource for growth, not just job leads.
11. She advances to second and third interviews. Some don't convert. She feels the disappointment, but the bot helps her frame it as progress — *"next time I will move further in the process."* Resilience built through reflection, not cheerleading.
12. She receives a job offer. The bot helps her think about who in her network to reach out to for negotiation support — someone who knows the market, the company, or has been through it. Her relationships become a resource at the most important moment.
13. She lands the job and shares it with the bot. The bot celebrates genuinely. Then, at exactly the right moment, surfaces the pay-it-forward ask — not as a transaction, but as an invitation to become the person who helps the next newcomer the way her network helped her.
14. She starts working. The bot reminds her who she already knows at the company — contacts she met during her search who are now colleagues or internal allies. It prompts her to reach out intentionally during her first weeks. The bot introduces the concept of the first 90 days: the window that defines how you're perceived, how quickly you build credibility, and how effectively you integrate into the team. Her network, built during the hardest months of her search, becomes her advantage on day one.

**That is the transformation.** The word "networking" should earn its way into the conversation — introduced by the bot only after the user has had the experiences that make it meaningful, not before. And the full arc ends not with a job offer — it ends with a person who is succeeding, giving back, and no longer the same person who was afraid to send a message to a stranger.

### integration_touchpoints

- **Where automation starts:** WhatsApp message received from user (or scheduled trigger for proactive nudges)
- **What user provides:** Contact name + scheduled time (to enable pre/post nudges); post-call notes (free-form text)
- **What user receives:** Reflection prompts, etiquette coaching, next-contact suggestions, milestone celebrations — all via WhatsApp
- **Where automation ends:** User writes their own outreach messages, decides who to contact, makes all relationship decisions

---

## sustainability_model

### cost_philosophy

The product is community-funded, not subscription-gated or VC-backed. Running costs are made visible to users — a simple transparent counter showing what it costs to run and what the community has contributed. This aligns with the product's values: newcomers without disposable income are never pressured, but those who can contribute are warmly invited to.

### contribution_model

**"Pay it forward" — community-funded, not subscription-gated.**

The funding ask is never a paywall. It is a celebration moment: the user lands a job or hits a meaningful milestone, the bot celebrates with them, and at that exact moment surfaces a contribution link framed as an act of solidarity — not a transaction.

- **Trigger moment:** Claude detects `job_landed` — the user explicitly shares that they got a job offer. No earlier. Never surfaced before the user has achieved the outcome the tool exists to support.
- **Message example (Spanish):** *"¡Lo lograste! Esto es real. Este bot no tiene inversionistas — lo sostiene la comunidad. Si quieres ayudar a que la próxima persona tenga este apoyo, aquí está: [link]. Si no puedes ahora, está bien — para eso existe."*
- **What contribution unlocks:** A higher daily message limit (50/day instead of 15) — not a paywall, but a meaningful thank-you. Contributors are also listed (anonymously if they prefer) in the monthly transparency note.
- **Monthly transparency note:** Total users helped, running cost, contributions received — sent as a WhatsApp broadcast. No dashboard needed. This is the portfolio story: "self-sustaining tool funded by the community it serves."
- **Implementation for MVP:** Sandra manually shares a Stripe link or Ko-fi link in WhatsApp when the trigger moment is detected by Claude. Sandra manually updates `tier: contributor` in Firestore. Automate the Stripe webhook in Sprint 3.

**Tier model:**

| Tier | Message cap | How to reach it |
|------|-------------|-----------------|
| Free | 15 messages/day | Default for all users |
| Contributor | 50 messages/day | Pay-it-forward contribution |
| Org-sponsored | Unlimited | Settlement org partnership covers the user |

**Why this framing fits:**
- "Ayuda mutua" — mutual aid — is culturally resonant in Latino communities
- Track A users (who benefit most, least income) contribute least — intentional and okay
- The people most motivated to give back are those who just got a job — peak gratitude = peak conversion
- Contribution creates a visible alumni community, which itself is proof the tool works

### cost_reduction_strategy

**Model tiering (Haiku vs. Sonnet):**

| Interaction type | Model | Rationale |
|---|---|---|
| Onboarding questions, simple nudges, milestone celebrations, next-contact suggestions | `claude-haiku-4-5-20251001` | Low reasoning load; 10–20x cheaper per token |
| Post-call reflection (R7), connection type reasoning (R1) | `claude-sonnet-4-6` | Coaching quality directly affects product value — worth the cost |

**Prompt caching:**
- System prompt is static and long — `cache_control: ephemeral` on every turn (already in technical specs)
- Projected cache hit rate: 80%+ for active users within the 5-minute TTL window

**Token efficiency:**
- Last 10 messages cap (not unlimited history) keeps context length bounded
- Structured `depth_signals` and `post_call_notes` fields store reflection outputs without replaying full conversation history

### longer_term_sustainability_paths

| Path | Timeline | Notes |
|---|---|---|
| Community pay-it-forward (Stripe/Ko-fi) | MVP | Triggered at job milestone; covers baseline running costs; builds alumni community |
| Settlement org partnerships | Sprint 3 | WILL Employment, ACCES Employment, COSTI — IRCC-funded budgets and direct distribution reach |
| Corporate DEI sponsorship | Post-launch | Companies hiring newcomers; weaker fit with product values but worth exploring |
| Grant funding | Post-launch | IRCC digital inclusion, Google.org, Mozilla Foundation — non-dilutive but slow |

Settlement org partnerships are the strongest long-term path: they solve cost, distribution, and credibility simultaneously. Worth one exploratory conversation before Sprint 3 to set up the pipeline.

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
  → interview_stage              (user reports their first interview) ← Sprint 3
  → advancing_in_interviews      (user reaches 2nd or 3rd round)    ← Sprint 3
  → job_offer_received           (user receives an offer, needs negotiation support) ← Sprint 3
  → job_landed                   (user accepts the job and shares it) ← pay-it-forward trigger
  → first_90_days                (user starts working; bot activates internal relationship strategy) ← Sprint 3
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
| Situational onboarding (app stage + has contacts) | R9 — framing only works if bot knows where she is | ✅ In |
| State-dependent language ("networking" earns its way in) | R9 — core framing mechanism across the arc | ✅ In |
| English-only professional artifacts + explanation why | R9 — etiquette through doing, not instruction | ✅ In |
| About Me — created in English, saved, reused in every prep | R1 — enriches connection type reasoning | ✅ In |
| Contact intake + connection type reasoning | R1 — multi-connection misclassification | ✅ In |
| Prep questions with WHY explanations | R1 — does it teach or just instruct? | ✅ In |
| Pre-chat nudge (8pm local time) | R9 — "something that finds you" | ✅ In |
| Post-chat check-in (+2h, within sendable window) | R7 — user won't self-trigger; bot must find her | ✅ In |
| Socratic post-call reflection | R7 — depth signal recognition without labeling | ✅ In |
| Giving-back prompt after every post-call reflection | Completes relationship model — reciprocity not just recognition | ✅ In |
| Thank-you nudge at 7am local time (day after) | Canadian professional etiquette learned through doing | ✅ In |
| Timezone-aware quiet hours (no messages 9pm–6am local) | Respect boundary — no proactive messages while user sleeps | ✅ In |
| Claude infers + saves state | Core behaviour, no extra infra | ✅ In |
| Mentorship introduction (at deepening_relationships) | Celebrates depth milestone; names what they've built | ✅ In |
| Rolling conversation summary (Haiku, background task) | Context quality as conversations grow beyond 10 messages | ✅ In |
| Rate limiting + spending caps | Safety — before number is shared publicly | ✅ In |
| LinkedIn fields | Doesn't change R9/R7/R1 test | ❌ Deferred |
| Milestone records in Firestore | Claude celebrates inline | ❌ Deferred |
| planning_style preference | Design consideration, not quality risk test | ❌ Deferred |
| Web app / mentor booking | Sprint 3 | ❌ Out |

### hardcoded_elements

- **All proactive jobs run hourly** — timezone check determines whether to send, not a fixed UTC time
- **Nudge eligibility:** Cloud Scheduler queries Firestore directly — no LLM call to decide who gets a nudge
- **Single contact for MVP:** user registers one contact at a time — no contact list management UI
- **No admin dashboard:** Sandra reads Firestore directly to monitor conversations
- **No error recovery flows:** basic retry on Claude API failure, simple fallback message
- **Zero-contacts path:** skipped — first test user will have at least one contact
- **Pay-it-forward mechanics:** Sandra manually sends Stripe/Ko-fi link and flips tier in Firestore

### definition_of_done

- [ ] A Track A Spanish-speaking newcomer texts the number and completes situational onboarding in Spanish — including city (used for timezone)
- [ ] Bot correctly calibrates to application stage and contact status
- [ ] User registers one contact with a scheduled chat date and time
- [ ] Bot drafts About Me in English, explains why, user confirms, saved to Firestore — reused in prep without re-asking
- [ ] Bot generates prep questions with connection type reasoning and WHY explanations
- [ ] Pre-chat nudge fires automatically at 8pm user's local time the evening before — no manual trigger
- [ ] Post-call check-in fires automatically ~2h after scheduled time — only within 6am–9pm local window
- [ ] Bot responds with Socratic reflection questions (no declarations)
- [ ] After post-call reflection, bot suggests one specific giving-back action (LinkedIn, article, closing the loop)
- [ ] Thank-you nudge fires at 7am local time the day after — bot offers to draft the thank-you in English, personalised to the conversation
- [ ] No proactive message sent between 9pm and 6am user's local time
- [ ] If user schedules a second meeting: deepening_relationships fires, bot celebrates, mentorship concept introduced
- [ ] Conversation summary generated and saved after 10th exchange
- [ ] "networking" appears zero times in early-state messages
- [ ] Rate limits active; spending caps set in Anthropic + Twilio consoles before number is shared
- [ ] Sandra reads the full transcript and scores R9, R7, R1

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
| Zero-contacts LinkedIn path | Pick test user with ≥1 contact; add before Sprint 3 |
| Seasonal giving-back nudges (Thanksgiving, holidays) | Requires extra Cloud Scheduler jobs + cultural context; Sprint 3 |
| Milestone records in Firestore | Claude inline celebration is enough to validate the behaviour |
| planning_style preference question | UX refinement, not a quality risk test |
| Multiple contacts per user | One contact loop is enough to test all three risks |
| Web app + mentor booking | Sprint 3 |
| Spanish native-speaker phrasing validation | Run the conversation, collect feedback, iterate prompt |
| Proactive next-contact suggestions | Requires relationship history across contacts; Sprint 3 |
