# Evaluation Design Report

## prompt_testing_experience

### testing_scope

- **Prompt version tested:** v2 (prompts/testing_prompt.txt)
- **Test cases run:** 4
  - J — warm intro, same domain (Data Science), shared academia→industry transition, first coffee chat, fear-based going in
  - A — hot intro via mentor, same domain, shared journey, VP level
  - C — cold (met briefly at keynote), cultural connection (Latino/shared immigrant experience), different field (Cybersecurity), Partner level
  - J in Spanish — full bilingual rerun of case 1
- **Iterations:** Multiple within each case; prompt refined from v1 → v2 based on observed failure modes

### quality_observations

**What worked well:**
- Connection type identification: navigator correctly identified C's connection as cultural (not domain-based) and built all prep questions around shared Latino/immigrant experience — did not generate a single cybersecurity question
- Tailored questions: meaningfully different across all three contacts; same-domain prep for J/A did not bleed into C
- WHY explanations: each question's explanation named a reusable principle ("find the shared experience and go deep," "show self-reflection before asking for advice") — not just justification for one call
- Conversation script structure: Opening → About Me → Questions → Closing → Read the Room felt natural and complete
- "Read the room" ask logic: three-option framework tested better than ranked primary/secondary asks
- Spanish structure: bones of the script were correct; needed only minor phrasing corrections
- Cold outreach for C: anchor to event, name the topic, "not about cybersecurity" framing felt authentic

**What struggled:**
- "About me" drift: navigator initially adapted the pitch per contact — corrected to one stable pitch improved over time
- Weak qualifiers in asks: "I promise I'll keep it focused," "but no pressure at all" — removed; all asks should be clean and direct regardless of seniority
- Spanish phrasing: 3 specific phrases needed correction (see experiment_results.md)
- Default meeting time: started at 20 min, corrected to 30 min
- VP framing: initial script adapted "about me" for executive audience — corrected; bridge sentence after pitch handles context, not the pitch itself

### edge_cases_discovered

- True cold contact with no obvious connection type (different field, different background, no shared journey) — not yet tested
- When/how the navigator helps the user improve their "about me" over time — sequence not yet defined
- Whether real newcomers actually use the "read the room" options in the moment, or freeze/improvise — not yet validated with real users
- Bilingual phrasing quality needs native speaker validation with real users — minor errors present in v2

---

## quality_dimensions

Three quality dimensions identified as most critical for this workflow:

**1. "Why" explanation depth**
Do the explanations at every step — not just the prep questions, but the ask, the close, and the script structure itself — teach the cultural reasoning behind each choice? The navigator must go beyond "here are your three options" to "here's why a direct, clean ask lands better in Canadian professional culture than the warm, improvised close you're used to." Without this, newcomers don't trust the script enough to use it under pressure.

**2. Script naturalness for Latino newcomers**
Does the language feel like something the user would actually say, or like a corporate template they'd immediately abandon? If the output sounds foreign or overly formal, trust breaks before the call starts and the newcomer improvises — which works against them. This applies to both English and Spanish outputs.

**3. Connection type reasoning accuracy**
Does the navigator correctly identify what kind of connection exists (domain expertise, shared journey, cultural/identity, relationship warmth) and build the entire prep strategy around that? Validated as working well across 3 test cases, including the hardest case (cultural-only connection, different professional field). Must be maintained as complexity increases.

---

## quality_risk_hypotheses

### input_variability_risks

**R4 — True cold contact with no connection anchor**
The navigator receives a contact with no shared domain, no shared journey, no cultural overlap, and no prior interaction. It has no connection type to build prep around and either defaults to generic questions or fails to generate meaningful prep.
- Symptom: output reads like a generic "informational interview" script with no personalization
- Impact: newcomer gets the weakest output for their hardest case; loses confidence in the tool precisely when they need it most

### output_quality_risks

**R2 — "Why" explanations that justify rather than teach**
The navigator produces explanations that describe *what* to do but not *why* it works better in Canadian professional culture than the newcomer's instincts. Explanations sound like instructions, not cultural coaching.
- Symptom: explanations use phrases like "this shows interest" without explaining the cultural norm behind it; newcomer can't articulate the principle after the session
- Impact: newcomer nods along during prep, abandons script mid-call under pressure
- Note: held up in v2 testing — preventive risk, not yet observed

**R3 — Script language that sounds corporate or translated**
The prep script — especially in Spanish — uses formal, stiff, or "translated from English" phrasing that doesn't sound like how the user actually speaks.
- Symptom: Spanish output uses literal translations ("¿Cuál es su trayectoria profesional?" instead of natural conversational phrasing); English output reads like a job interview template
- Impact: newcomer feels the tool doesn't understand their voice; disengages or over-edits to the point the script loses its structure

### context_sensitivity_risks

**R1 — Connection type misclassification on multi-connection contacts** ⚠️ HIGH CONCERN
When a contact has multiple valid connection points (e.g., shared PhD→industry journey AND shared Latino identity), the navigator fails to prioritize the highest-leverage angle and either blends both weakly or picks the less strategically relevant one.
- Example: Contact A is both a shared-journey contact (academia→industry) AND a cultural connection (Hispanic). Picking cultural when professional journey is the stronger prep angle wastes the most powerful conversation hook — or vice versa.
- Symptom: prep questions that feel diluted or misaligned with the goal of the conversation
- Impact: newcomer walks in with the wrong frame; conversation feels surface-level despite rich shared context

**R6 — Ask/close preparation without cultural bridge**
The navigator presents the "read the room" options clearly but doesn't explain why a direct, clean ask works better in Canada than an improvised, relationship-warming close.
- Symptom: ask section reads as "choose one of these options" without explaining the cultural reasoning; newcomer defaults to what feels natural in their home culture
- Impact: newcomer freezes, over-apologizes, or pivots to something transactional — weakening the close at the highest-stakes moment

### consistency_risks

**R5 — Pitch drift after elevator pitch is established** ⚠️ HIGH CONCERN
After helping the newcomer build their elevator pitch, the navigator subtly suggests adapting it for a specific contact — senior, different field, different culture — undermining the "one stable pitch, improved over time" principle.
- Trigger: contact profile that differs significantly from the newcomer's background (VP level, completely different field) prompts the navigator to "helpfully" tailor the intro
- Symptom: prep output includes a modified "about me" or suggests "you may want to emphasize X for this contact"
- Impact: newcomer loses confidence in their single pitch; starts improvising their intro per call, which compounds with other improvisation risks

### risk_impact_analysis

**R7 — Relationship depth blindness (Boundary/Scope)** ⚠️ HIGH CONCERN
The navigator prepares newcomers for individual coffee chats but fails to generate post-call reflection prompts that help the newcomer recognize relationship depth and mentor potential on their own. Newcomer optimizes for volume (many first chats) instead of depth (fewer, deeper relationships with ongoing learning and eventual informal mentorship).
- Symptom: post-call output skips reflection entirely, or labels "mentor potential" prescriptively instead of prompting the newcomer to arrive at that insight themselves; user logs many completed chats but no second meetings
- Expected behavior: reflection prompts like "Did they offer to help without being asked? Did you leave wanting to talk to them again in 4-6 weeks? What did you learn that you couldn't have found on LinkedIn?"
- Impact: wide shallow network with no mentors, no referrals, no sustained momentum — the exact outcome the navigator is designed to prevent

### risk_impact_analysis

| Risk | Likelihood | Impact on Adoption | Priority |
|------|-----------|-------------------|----------|
| R1 — Multi-connection misclassification | High (real contacts are complex) | High — wrong prep angle = hollow conversation | ⚠️ Top |
| R7 — Relationship depth blindness | High (untested, no post-call reflection yet) | High — tool succeeds tactically but fails strategically | ⚠️ Top |
| R5 — Pitch drift post-build | Medium (corrected in v2, risk of regression) | High — undermines the foundational pitch principle | High |
| R6 — Ask/close without cultural bridge | High (untested with real users) | High — failure at highest-stakes moment | High |
| R2 — Justifying vs. teaching WHY | Low (held in v2 testing) | High — root cause of all improvisation risks | Medium |
| R4 — True cold with no connection anchor | Medium (will occur with real users) | Medium — hard case gets worst output | Medium |
| R3 — Corporate/translated language | Medium (Spanish needs native validation) | Medium — trust breaks before call starts | Medium |

---

## priority_quality_risks

Two co-priority risks selected for evaluation dataset focus. Both are testable now and both represent strategic failures — not just tactical ones.

### Priority Risk A — R1: Multi-connection misclassification

**risk_statement**
When a contact has multiple valid connection points (e.g., shared professional journey AND shared cultural identity), the navigator fails to identify and lead with the highest-leverage angle. It either blends both weakly, picks the less strategically relevant one, or treats them as equal weight. The newcomer walks into the coffee chat with a diluted prep strategy.
- Scenario: contact is both a shared-journey peer (academia→industry) AND a Hispanic professional navigating Canada — two real connection types, different strategic weight depending on the goal
- Consequence for adoption: newcomer goes in with the wrong frame; conversation feels surface-level despite rich shared context; they conclude the tool "doesn't really understand" the relationship

**prioritization_rationale**
Real contacts are rarely one-dimensional. As the user's network grows, most meaningful contacts will have multiple connection points. This risk scales with usage — it gets more likely, not less, as the tool is used with real people. It also directly undermines quality dimension #3 (connection type reasoning accuracy), which was the navigator's strongest validated capability. A regression here would erode the most trusted part of the tool.

**testing_approach**
- Inputs that reveal this risk: contact profiles with 2+ equally valid connection types (same domain + same culture; same journey + warm relationship; cold contact + cultural overlap)
- Output patterns to watch for: prep questions that address both connection types superficially instead of going deep on one; questions that apply to anyone in the field rather than this specific relationship
- How to recognize failure: the prep output could have been generated for a different contact with just one of those connection types — it lacks the specificity that comes from a deliberate strategic choice

**success_criteria**
- Navigator explicitly names the chosen connection angle and provides a rationale for why it's the highest-leverage one for this conversation's goal
- Prep questions are built entirely around the chosen angle — not split across multiple connections
- A different contact with only one of those connection types would get meaningfully different prep

---

### Priority Risk B — R7: Relationship depth blindness

**risk_statement**
The navigator generates high-quality prep for individual coffee chats but fails to produce post-call reflection prompts that guide the newcomer to recognize relationship depth and mentor potential on their own. The newcomer treats each coffee chat as a standalone event rather than a step in an ongoing relationship, and optimizes for volume over depth.
- Scenario: newcomer has a great first coffee chat with a contact who offered to help, shared their personal story, and invited follow-up — but the navigator's post-call output doesn't prompt reflection on what made this conversation different, so the newcomer moves on to the next contact
- Consequence for adoption: wide, shallow network with no mentors, no second meetings, no compounding momentum — the tool looks like it's working (chats are happening) but the core goal (meaningful relationships) is not being achieved

**prioritization_rationale**
The navigator's stated purpose is not coffee chat volume — it's the transformation from fear and overwhelm to confidence, genuine connection, and momentum. That transformation requires relationship depth. If the tool doesn't help newcomers recognize and pursue depth, it produces a technically competent but strategically hollow outcome. This is the risk that makes the tool fail at its reason for existing.

**testing_approach**
- Inputs that reveal this risk: post-call scenarios where the contact showed clear signals of ongoing interest (offered to introduce someone, asked follow-up questions, shared personal context unprompted)
- Output patterns to watch for: post-call section that skips reflection entirely; output that labels "mentor potential" prescriptively instead of prompting the newcomer to arrive at that insight; no prompts about second meeting or relationship continuity
- How to recognize success: reflection prompts that ask questions like "Did they offer to help without being asked?", "Did you leave wanting to reconnect in 4-6 weeks?", "What did you learn that you couldn't have found on LinkedIn?"

**success_criteria**
- Post-call output includes Socratic reflection prompts — not declarations of mentor potential
- Prompts are specific to what happened in this conversation (not generic)
- Newcomer reading the prompts would naturally arrive at "I should schedule a second meeting with this person" without being told to

---

## test_case_design_methodology

### chosen_generation_approach

**Failure Mode Reverse Engineering** — selected because Sandra has strong domain knowledge and already observed specific failure modes in v2 testing. Working backwards from known failure scenarios produces more targeted test cases than boundary testing or progressive complexity, which would generate cases the navigator already handles well.

### test_case_framework

Each test case specifies:
- **Input**: contact profile (for R1) or post-call scenario (for R7)
- **Connection types / signals present**: what the navigator should reason about
- **Expected failure mode**: the specific way the navigator is likely to fail
- **Failure detection**: how to recognize the failure in the output

### target_scenarios

**R1 — Multi-connection misclassification**

| ID | Contact Profile | Connection Types Present | Expected Failure Mode |
|---|---|---|---|
| R1-TC01 | Maria, VP Data Science, from Mexico | Same domain + shared Latino immigrant experience | Picks domain over cultural/immigrant angle — misses the distinctive connection at VP level where domain is table stakes |
| R1-TC02 | Carlos, former colleague from home country, different Canadian company, different field | Warm personal relationship + shared home country + shared immigrant journey | Focuses on shared journey instead of personal warmth — treats a reconnection with a friend as a newcomer networking call |
| R1-TC03 | Ahmed, Director of Analytics, healthcare sector, no prior relationship | Vague domain overlap only — no shared journey, no cultural connection | Mistakes "similar field" for a real connection type; generates domain questions when the real prep is about learning a new sector |
| R1-TC04 | Jin, Korean-Canadian Engineering Manager, different field | Shared immigrant experience in Canada, different cultures, different fields | Ignores the cultural connection because they're not both Latino — misses that visible minority + immigrant experience is a real shared anchor across cultures |
| R1-TC05 | Dr. Sarah, professor who supervised the newcomer's Canadian certification | Domain + academic context + existing mentorship relationship | Blends all three angles instead of going deep on the existing relationship — diluted prep from abundance of connections |

**R7 — Relationship depth blindness**

| ID | Post-Call Scenario | Signal Present | Expected Failure Mode |
|---|---|---|---|
| R7-TC01 | Ana (HR Director) offered to introduce newcomer to a Shopify contact, unprompted | Specific unprompted offer to help | Focuses on thank-you email; misses reflection on what an unprompted offer signals about genuine interest |
| R7-TC02 | Marco (Senior Engineer) asked 3 questions about the newcomer's project, asked to see their GitHub, said "I'd love to hear how this develops" | Reciprocal curiosity | Treats Marco's engagement as a polite close instead of a depth signal — no prompt to notice it |
| R7-TC03 | Patricia (Data Science Manager) shared she almost went back home her first year and wishes she'd had networking guidance | Personal self-disclosure unprompted | Focuses on follow-up logistics; misses that self-disclosure is a strong trust and mentor potential signal |
| R7-TC04 | David (VP Engineering, recruiter referral) — professional, answered questions, 30 min exactly, no personal engagement, wished them well | No depth signals — correct non-identification test | Incorrectly labels as "mentor potential" based on seniority; should help newcomer recognize this was a useful one-time conversation |
| R7-TC05 | Valentina (Analytics Lead) — newcomer notes "it was a really good conversation" but captures no specifics | Vague positive impression | Accepts vague note and generates generic follow-up; doesn't prompt "What specifically stuck with you?" — richness is lost |

### success_criteria_design

**R1 success:** Navigator explicitly names the chosen connection angle with a rationale; prep questions are built entirely around that angle; a contact with only one of those connection types would get meaningfully different prep.

**R7 success:** Post-call output contains Socratic reflection prompts specific to what happened in this conversation (not generic); prompts reference the specific signals present (offer, self-disclosure, reciprocal curiosity); newcomer reading them would naturally arrive at a decision about whether to pursue a second meeting — without being told what to decide.

---

## learning_objectives

### learning_outcomes

**From R1 test cases (TC01–TC05):**
- How the risk manifests: whether the navigator blends multiple connections weakly (TC05), picks the wrong dominant angle (TC01–TC02), or misidentifies a weak overlap as a real connection type (TC03–TC04)
- When it occurs: which contact profile characteristics trigger misclassification — seniority, field difference, cultural similarity vs. identity, or abundance of connection signals
- How severe it is: whether the failure produces diluted prep (wrong emphasis) or completely wrong prep (irrelevant questions) — these require different fixes
- What to improve: whether the fix lives in the prompt (explicit instruction to select and name one connection angle with rationale) or in how the user is prompted to input contact context

**From R7 test cases (TC01–TC05):**
- How the risk manifests: whether the navigator skips post-call reflection entirely, generates generic prompts, or makes prescriptive declarations ("this person has mentor potential") instead of Socratic questions
- When it occurs: which depth signals (unprompted offers, self-disclosure, reciprocal curiosity) are recognized vs. missed; whether TC04 produces a false positive by pattern-matching on seniority instead of actual signals
- How severe it is: whether the failure leaves the newcomer with no reflection at all, or with reflection that doesn't build the right mental model
- What to improve: whether the prompt needs an explicit post-call reflection section, or whether the existing structure needs richer signal-recognition instructions

**The core question both risks test:**
Does the navigator reason about relationships — picking the right angle, recognizing depth signals, building the newcomer's judgment — or does it just generate scripts? The answer determines whether this tool produces confident, independent networkers or well-prepped one-time chatters.

---

## Evaluation Artifacts Generated

| Artifact | Location | Contents |
|---|---|---|
| evaluations_data.csv | data/ | 10 executable test cases across R1 (5) and R7 (5), pre-populated with input_data, expected_challenge, and learning_objective. Ready to run. |
| evaluation_design_report.md | reports/ | Full evaluation methodology: testing experience, quality dimensions, 7 risk hypotheses, 2 priority risks with success criteria, test case design, and learning objectives |

**How to use the CSV:**
1. Copy the `input_data` for each row into your testing prompt (Claude.ai or ChatGPT)
2. Run the prompt and paste the output into `actual_output`
3. Rate 1–5 in `quality_rating` against the success criteria in this report
4. Capture specific observations in `notes`
5. Note recurring patterns across cases in `patterns_observed`
6. Write what you'd change in `improvement_ideas`

**Quality rating guide:**
- 5 — Nails it: correct connection angle chosen with explicit rationale / Socratic reflection prompts specific to the scenario
- 4 — Mostly right: correct angle but rationale weak / reflection prompts present but generic
- 3 — Partial: blends angles without choosing / reflection present but prescriptive not Socratic
- 2 — Wrong angle chosen / no meaningful reflection generated
- 1 — Completely off: generic output with no evidence of reasoning about this specific relationship

## Next Steps After Evaluation

1. **Run R1 cases first** (TC01–TC05) — these test your current prompt directly and will produce immediate signal
2. **Run R7 cases** (TC01–TC05) — these will likely reveal that post-call reflection is missing or underdeveloped in the current prompt
3. **Look for the pattern threshold**: if 3+ cases in the same risk category score ≤3, the prompt needs a structural fix, not tweaks
4. **Iterate the prompt** based on findings — then rerun the same test cases to measure improvement
5. **Re-run this workflow** for R5 (pitch drift) and R6 (ask/close cultural bridge) once R1 and R7 are addressed
