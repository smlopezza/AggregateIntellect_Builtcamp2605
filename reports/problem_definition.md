# Problem Definition

## problem_statement

Latino newcomers to Canada exhaust job applications with no response, then turn to networking from a place of desperation — carrying a fundamentally wrong mental model (networking = nepotism or transactional job-getting), no execution knowledge, and no visibility into their own progress. They try once, fail quietly, and give up right before momentum would have kicked in.

## target_users

Latino newcomers to Canada, less than 5 years in the country, not yet working in their profession. Bilingual English/Spanish. Technical or non-technical backgrounds. Typically arrive at networking after exhausting job applications with no response.

## current_state

### user_process

1. Send hundreds of job applications → silence → decide to try networking
2. Approach contacts thinking "this person will get me a job"
3. Set up calls via back-and-forth emails; use phone instead of video, don't dress professionally, don't prepare questions
4. Have the call — improvised, no structure, leaves a poor impression
5. Disappear after call #1; reappear only when they want a referral
6. Get no results → conclude "networking doesn't work"
7. Feel overwhelmed, disorganized, unable to see any progress made

### user_existing_tools

Nothing, or Excel/Notion for the few who track at all. LinkedIn unused or used ineffectively.

### trigger

Wall of silence after mass job applications — hundreds sent, zero responses.

### frequency

Ongoing daily struggle. Networking attempts are sporadic and unstructured, not a regular cadence.

### friction_points

- Wrong mental model: networking confused with nepotism or corruption from home country context
- Transactional approach: reaching out to "get a job" not to build a relationship
- Execution gaps: wrong medium, no preparation, no follow-up, scheduling overhead
- No progress visibility: can't see momentum even when it's building, leads to giving up
- Skills communication: task-based not achievement-based framing
- Cultural gap: assuming what worked in their home country applies in Canada

## assumptions_analysis

### Initial Assumptions Identified

1. Users need to understand *why* networking matters before their behavior will change
2. The solution needs to address all 14 identified friction points
3. Users won't trust an AI with something this emotionally vulnerable
4. The navigator only responds when the user initiates (reactive)
5. The tool gives users scripts and answers (replaces thinking)

### Validated Constraints

- Bilingual English/Spanish, feels natural not translated — not negotiable
- Proactive: reminds, follows up, proposes topics, suggests reuse across contacts, celebrates milestones
- Persistent memory: keeps notes from every conversation, tracks relationship state per contact
- Teaches the *why* behind each action — builds independence, not dependency; user should be able to network without the tool eventually
- Focused scope: network identification → coffee chat prep → thank you email → follow-up sequence → informal mentor identification
- Does NOT replace mentor, career coach, immigration advice, or mental health support
- This is a **navigator** (not a coach, not a mentor) — a tool that walks alongside them, peer-level, no authority
- Architecture must scale beyond Latino newcomers to other demographics

### Flexible Assumptions

- ~~Mindset must come before behavior~~ → doing produces understanding; get them to their first good coffee chat fast, mindset shift follows from positive experience
- ~~Solution needs to solve all 14 problems~~ → narrow critical path is sufficient; success cascades from first good experience

### Beliefs to Test

- Will users share enough contact context for the navigator to give meaningful relationship-specific advice?
- Will proactive nudges feel supportive vs. intrusive — what cadence is right?
- How much cultural coaching does the navigator need to do vs. just mechanics?
- Will users engage with "you learned A, B, C" progress reflection, or skip it?

## solution_hypotheses

### Hypothesis 1 — AI as Assistant (Level 1)
User-initiated prep tool per coffee chat. Generates tailored prep questions with explanations of *why* each matters. Drafts thank you email template. No memory between sessions, no proactive reminders, no tracking.
- **AI does:** Prep questions + reasoning, thank you email draft
- **Human does:** All scheduling, tracking, follow-up decisions
- **Interaction:** User-initiated, per coffee chat

### Hypothesis 2 — AI as Collaborator (Level 2) ✓ SELECTED
Proactive navigator that walks alongside the user across the full networking journey. Keeps relationship memory, drafts follow-ups, reminds about thank you emails, suggests next conversation topics, tracks progress, celebrates milestones, identifies mentor candidates. Also supports goal-setting and tracks progress toward goals. User reviews and approves all outgoing messages.
- **AI does:** Remembers conversations, drafts follow-ups, proactively reminds, tracks goals and progress, suggests mentor candidates, celebrates milestones
- **Human does:** Reviews/edits all messages, decides who to contact next
- **Interaction:** Proactive check-ins + user-initiated sessions

### Hypothesis 3 — AI as Agent (Level 3)
Autonomous networking CRM. Manages full relationship lifecycle, queues and sends messages, identifies new contacts, user reviews weekly digest only.
- **AI does:** Manages contacts, queues/sends messages, identifies new contacts
- **Human does:** Sets goals, reviews weekly summary, handles exceptions
- **Interaction:** Mostly async, weekly review

## selected_solution

### chosen_hypothesis

Hypothesis 2 — AI as Collaborator. Selected over H1 (too passive, doesn't address progress visibility) and H3 (too autonomous for something this personal; undermines trust and authenticity). H2 hits the sweet spot: proactive enough to tackle overwhelm, collaborative enough to maintain trust, scaffolded to build genuine independence.

### solution_logic

If we implement a bilingual proactive navigator that guides newcomers through goal-setting, coffee chat prep, follow-up, and progress tracking — it will produce a shift from overwhelm and avoidance to consistent, confident networking — because the navigator removes the cognitive load of "what do I do next" while teaching the reasoning behind each step through scaffolding (not scripting), so users build genuine capability over time.

### autonomous_capabilities

- Goal-setting conversations and progress tracking toward user-defined goals
- Contact identification within the user's existing network
- Coffee chat prep: provides question frameworks + explains *why* each question matters
- Post-chat: provides email structure + asks prompting questions to pull authentic content from the user (does NOT draft emails for them)
- Follow-up timing suggestions and proactive reminders
- Persistent relationship tracking: contact notes and conversation history per person
- Mentor candidate identification based on conversation patterns
- Proactive check-ins: thank you reminders, follow-up nudges, goal progress check-ins
- Milestone celebrations: "You completed 3 coffee chats this week — here's what you learned"
- Bilingual support (English/Spanish, feels natural not translated)

### human_touchpoints

- User writes all outgoing messages — navigator provides structure and feedback, not drafts
- User logs coffee chat notes and outcomes after each call
- User decides who to contact next (navigator suggests, user decides)
- User sets and confirms goals at onboarding and each sprint
- User reports confidence at weekly check-ins

### interaction_pattern

- **Proactive:** Navigator initiates reminders for thank you emails, follow-ups, and goal check-ins
- **Reactive:** User initiates prep sessions before each coffee chat
- **Weekly:** Milestone celebration + progress reflection
- **Core principle:** Scaffold, not script — navigator asks questions that pull authentic content from the user, so they learn the pattern and eventually internalize it

### success_metrics

- Number of coffee chats completed per week (target: 3/week)
- Number of contacts where a 2nd coffee chat is scheduled (relationship depth signal)
- User-reported confidence score before and after (self-assessed)

### scope_boundaries

**Primary track (networking):** Goal-setting, network contact identification, coffee chat prep frameworks, post-chat email scaffolding, follow-up reminders, relationship tracking, mentor candidate identification, progress visibility, bilingual support

**Side track — LinkedIn:** Progressive LinkedIn strategy surfaced contextually: like/comment/reshare → engage on others' content → original post creation. Navigator identifies relevant topics based on user's background and career goals.

**Side track — Dynamic goals:** If a conversation surfaces something to work on (portfolio, certifications, etc.), navigator captures and tracks it as a goal alongside networking progress. Priority always stays on networking.

**Out of scope:** Writing messages on behalf of users, immigration advice, mental health support, replacing mentor or career coach, finding contacts outside the user's existing network (initially)

## process_requirements

### process_inputs

- User's career goals and timeline
- Contact names, roles, and context (entered by user)
- Coffee chat notes and outcomes (entered by user after each call)
- User's self-reported confidence at check-ins

### process_outputs

- Personalized prep question frameworks per contact (with reasoning)
- Email structure scaffolds with guiding questions (not completed drafts)
- Follow-up reminders with suggested timing and topic prompts
- Progress reports and milestone celebrations
- Mentor candidate suggestions with reasoning
- Goal tracking visibility

## experiment_design

### core_assumption

AI can generate tailored coffee chat prep questions that explain the *why* behind each question — in a way that teaches a transferable pattern so the user eventually preps independently, without relying on the navigator.

### test_approach

In Claude.ai or ChatGPT, prompt the navigator with: the newcomer's profile + one contact at a time. Ask it to generate prep questions with reasoning for each question. Run all 3 contacts. After the 3rd, assess: could the user now prep for a 4th new contact without help?

### mock_data_examples

1. **Jessie** — Senior Manager, Data Science & Model Innovation. Successfully transitioned from academia to industry. Sandra's first mentor; Sandra was scared going in. Connection point: shared academia → industry transition. Goal: understand her journey, learn what she wished she'd known, navigate the Canadian market.

2. **Aitor** — VP, Head of Analytics & AI, Retail Banking. Also transitioned from academia to industry successfully. VP-level meeting — Sandra didn't know how prep should differ for seniority. Connection point: shared academia → industry path. Goal: understand what matters at the executive level in Canadian banking AI.

3. **Carlos** — EY Partner, Cybersecurity & Privacy. Latino from Mexico (Sandra is from Colombia) — shared cultural identity but completely different professional field. Sandra wanted to meet him but was never successful. Connection point: shared Latino experience navigating Canada, NOT professional domain. Goal: understand how to navigate Canada as a Latino professional, despite field mismatch.

### test_scenarios

- **Same-level, same-domain (Jessie):** Does it feel personal? Does it leverage the academia → industry bridge?
- **Senior-level, same-domain (Aitor):** Does it adjust tone and questions for VP-level? Does it still use the shared transition experience?
- **Senior-level, different-domain (Carlos):** Does it reason correctly that the connection is cultural, not professional? Does it avoid generic domain questions?
- **Bonus edge case:** Run Jessie's scenario in Spanish — does it sound natural or translated?

### success_criteria

- 8/10 questions feel genuinely tailored to the specific contact and connection type
- The *why* explanations teach a transferable principle (not just a script for that one call)
- After 3 sessions, user could draft questions for a new contact without help
- Navigator correctly identifies the *type* of connection (professional domain vs. shared journey vs. cultural) and adjusts prep strategy accordingly
- Spanish version sounds like a native speaker wrote it

### learning_goals

- What's easy: tailoring questions to job title and domain
- What's hard: reasoning about what *kind* of connection exists and building prep around that
- Does the AI teach a pattern or just give outputs? Can the user articulate *why* they're asking each question after 2-3 sessions?
- Where does it default to generic despite rich context?

## desired_state

### user_success_criteria

Within 4-6 weeks: user understands networking is about building meaningful relationships and learning from others — and starts genuinely enjoying it. Behavioral markers: consistent coffee chats, prepared questions, structured follow-up, visible progress tracking.

### expected_impact

From fear and overwhelm → confidence, genuine connection, and a sense of momentum. The networking process becomes something they look forward to rather than dread.

### constraints

- Bilingual experience (English/Spanish) that feels natural, not translated
- Does NOT replace a mentor or career coach
- Does NOT answer immigration questions (redirects to government resources)
- Does NOT replace mental health support (routes to appropriate resources)
- Must scale beyond Latino newcomers to other newcomer demographics in future
