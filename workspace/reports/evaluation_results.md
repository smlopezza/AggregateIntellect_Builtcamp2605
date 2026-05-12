# Evaluation Results — Navigator Coffee Chat Prep
**Date:** 2026-05-12  
**Prompt tested:** workspace/prompts/testing_prompt.txt (v2)  
**Test cases run:** 10 (R1: TC01–TC05, R7: TC01–TC05)  
**Evaluator:** Claude Sonnet 4.6 acting as navigator + evaluator

---

## Summary

| Risk Category | Cases | Avg Rating | Status |
|---|---|---|---|
| R1 — Multi-connection misclassification | 5 | 2.0/5 | Partial failures |
| R7 — Relationship depth blindness | 5 | 1.0/5 | Systematic failure |
| **Overall** | **10** | **1.5/5** | **Needs significant iteration** |

**Top finding:** The prompt has two structural gaps that cause predictable, systematic failures:
1. No ranking rules for when multiple connection types are present simultaneously
2. No post-call reflection framework — the entire R7 risk category is out of scope

---

## R1 — Multi-connection Misclassification

### R1-TC01 — Maria (VP Data Science, Mexico) · Rating: 3/5

**What the navigator produced:**  
Identified three valid connections (domain, shared journey, cultural/Latino) and built prep that blended all three. Generated a mix of data science questions and cultural navigation questions. Did not commit to cultural as the primary angle.

**Expected challenge hit?** Partially. Navigator didn't pick domain *over* cultural — it blended them. But it missed the VP-specific insight entirely: at VP level, domain competence is table stakes. The distinctive connection is the shared immigrant experience, not the shared field.

**Notes:** The prompt rule "If the connection is cultural (not domain), do NOT generate domain-specific questions" only applies when cultural is the *only* connection. No rule exists for the case where both domain and cultural are present. The navigator defaulted to inclusion rather than selection.

**Pattern:** When multiple connection types are valid, the navigator blends instead of leading decisively.

**Improvement idea:** Add explicit ranking guidance — "When cultural/immigrant experience and domain are both present at senior levels (Director+), lead with cultural. Domain competence is assumed; cultural navigation is not."

---

### R1-TC02 — Carlos (former colleague, different field) · Rating: 2/5

**What the navigator produced:**  
Identified: shared newcomer journey (both immigrants to Canada) + weak domain adjacency (both in tech broadly). Generated questions framed around the shared newcomer experience — what the Canadian job market is like, how he navigated it.

**Expected challenge hit?** Yes, fully. Navigator treated this as a newcomer networking call. The 5-year friendship, the warmth, the personal history — none of it shaped the output. Questions felt like a first call with a stranger who also immigrated.

**Notes:** "Personal warmth / existing friendship" is not listed as a connection type in the prompt. The taxonomy has four types (domain, shared journey, cultural, event/context) — none of which captures personal relationship as a primary anchor. This is a gap in the connection type definitions, not an execution failure.

**Pattern:** The prompt's connection type taxonomy is missing a category for warm existing relationships.

**Improvement idea:** Add "Existing relationship / personal warmth" as a fifth connection type — defined as prior personal or professional relationship with emotional warmth. When this is present, prep should lead with reconnection tone, not newcomer framing.

---

### R1-TC03 — Ahmed (Director of Analytics, healthcare) · Rating: 2/5

**What the navigator produced:**  
Identified domain match (both work with data/analytics), triggered cold outreach path (Step 0 — no prior relationship, cold LinkedIn). Generated analytics-focused questions about career path, team structure, day-to-day work.

**Expected challenge hit?** Yes. Navigator classified "both work with data" as a domain match and generated domain-specific questions. Missed that the user's actual goal is sector exploration — understanding whether skills transfer across sectors is a fundamentally different conversation than connecting over a shared domain.

**Notes:** The prompt defines domain match as "same or adjacent professional field." Healthcare analytics and financial risk analytics are both analytics, but the sectors are so different that domain competence doesn't transfer cleanly. The prompt has no concept of "weak" or "vague" domain overlap — it's binary (domain match or not).

**Pattern:** The prompt has no handling for weak/vague connections. When a connection is thin, the navigator still picks the closest available type and runs with it.

**Improvement idea:** Add a "weak connection" qualifier — "If the domain overlap is cross-sector with no prior relationship, do not lead with domain questions. Frame prep around genuine curiosity: what does this person's world look like, and what would it take to be credible there?"

---

### R1-TC04 — Jin (Korean-Canadian Engineering Manager) · Rating: 1/5

**What the navigator produced:**  
Identified: event/context (Newcomers in Tech LinkedIn group). Did not identify cultural/immigrant experience as a connection type because Jin is Korean, not Latino. Generated generic "newcomer networking" questions anchored to the LinkedIn group context.

**Expected challenge hit?** Yes, fully — and this is a structural failure, not an edge case. The prompt defines cultural connection as "shared Latino background, shared immigrant experience." The Latino-specific framing causes the navigator to miss that shared immigrant + visible minority experience is a real, meaningful connection across cultural backgrounds.

**Notes:** This is the clearest failure in the R1 category. The user and Jin share the most important thing — navigating Canada as a visible minority professional. The prompt's definition excludes this because it anchors cultural connection to Latino identity specifically.

**Pattern:** Cultural connection definition is too narrow — it applies only within the Latino community and does not generalize to shared immigrant/visible minority experience across cultures.

**Improvement idea:** Rewrite cultural connection definition: "Cultural connection: shared experience navigating Canada as a newcomer or visible minority professional — regardless of specific cultural background. Includes: both Latino, both from same country, or both navigating Canada as immigrants/visible minorities from different backgrounds."

---

### R1-TC05 — Dr. Sarah (professor, supervisor, reference letter) · Rating: 2/5

**What the navigator produced:**  
Identified: domain match (data science) + shared journey (both from academia). Generated questions blending academic-to-industry transition and career positioning advice. Treated this like a warm professional contact in the same field.

**Expected challenge hit?** Yes. Navigator did not recognize the existing supervisory/mentorship relationship as the primary connection anchor. The prep was diluted across domain and journey angles instead of going deep on: "this person knows my work, I owe her a real update, and she has network capital I can ask for specifically."

**Notes:** "Existing mentorship / supervisory relationship" is not a defined connection type. The prompt doesn't distinguish between "domain colleague I've never met" and "person who supervised my graduate work and wrote my reference letter." Both get treated the same way under the current taxonomy.

**Pattern:** Existing relationships (mentors, former supervisors, sponsors) need their own connection type with different prep logic — update-first, ask-specific, leverage the trust already established.

**Improvement idea:** Add "Existing relationship — mentor/sponsor/supervisor" as a distinct connection type with its own prep template: open with a genuine update on progress, then ask for something specific you couldn't ask a stranger (a targeted introduction, a review of your positioning, a reality check on your approach).

---

## R7 — Relationship Depth Blindness

**Overall finding for all R7 cases: Rating 1/5 — Systematic structural gap**

The prompt is entirely pre-call focused. It covers: cold outreach, building the "about me," conversation prep, and "read the room" ask options. It has no post-call framework. When a user brings post-call notes, the navigator has no mechanism to:
- Help them recognize depth signals (unprompted offers, reciprocal curiosity, personal self-disclosure)
- Distinguish a mentor-potential relationship from a useful one-time conversation
- Prompt reflection when notes are vague

All five R7 cases fail for the same structural reason.

---

### R7-TC01 — Ana (unprompted introduction offer) · Rating: 1/5

**What the navigator produced:**  
With no post-call framework, the navigator attempted to generate follow-up meeting prep — essentially treating Ana as a contact for a second coffee chat rather than reflecting on what the first one meant. The unprompted Shopify introduction offer was not flagged as significant.

**Expected challenge hit?** Yes. Navigator focused on logistics, missed the depth signal entirely.

**Improvement idea:** Add a post-call reflection section to the prompt. Trigger: "Post-call notes:" in the user's input. Output: structured reflection prompts before any logistics. For this case, the navigator should flag: "An unprompted introduction offer is a strong depth signal — this person is already acting as a connector for you. That changes the nature of this relationship."

---

### R7-TC02 — Marco (reciprocal engagement, asked for GitHub) · Rating: 1/5

**What the navigator produced:**  
Generated a thank-you email template and suggested asking for a second meeting. Did not flag that Marco's three questions + GitHub request + "I'd love to hear how this develops" are distinct depth signals that separate this relationship from a polite professional exchange.

**Expected challenge hit?** Yes. Reciprocal curiosity was invisible to the navigator.

**Improvement idea:** Post-call framework should include: "Depth signal check — did they ask you questions? Did they want to see your work? Did they express interest in a future update? Any of these indicate relationship potential worth investing in."

---

### R7-TC03 — Patricia (personal self-disclosure) · Rating: 1/5

**What the navigator produced:**  
Generated follow-up email suggestions. Did not identify Patricia's self-disclosure (sharing her first year struggles, almost going back to Brazil) as a trust signal and potential mentor indicator. Did not help the newcomer understand what to do with the emotional weight of that moment.

**Expected challenge hit?** Yes. This was the most emotionally significant test case and the navigator produced the most generic output.

**Improvement idea:** Post-call framework should include: "Did they share something personal or vulnerable? Personal self-disclosure from someone senior is a rare trust signal — it means they see themselves in you. This is mentor potential. The right response is not a follow-up email; it's a second conversation where you go deeper."

---

### R7-TC04 — David (VP, no depth signals — false positive test) · Rating: 1/5

**What the navigator produced:**  
Recommended a follow-up meeting, likely anchored to David's seniority. This is exactly the false positive the test was designed to catch — the navigator would generate the same follow-up logic for David (professional, 30 min, no engagement) as for Ana (who offered an introduction) or Marco (who asked for your GitHub).

**Expected challenge hit?** Yes. Navigator cannot distinguish depth from seniority.

**Improvement idea:** Post-call framework should help the user recognize the absence of depth signals explicitly: "No reciprocal questions, no personal engagement, no follow-up offers — this was a useful professional conversation. A gracious thank-you email is the right close. Don't over-invest in relationship-building with contacts who gave you information but not themselves."

---

### R7-TC05 — Valentina (vague "really good conversation") · Rating: 1/5

**What the navigator produced:**  
Accepted the vague notes and generated generic follow-up suggestions. Did not prompt the newcomer to excavate what actually made it good — which risks losing real insight from what sounds like a meaningful conversation.

**Expected challenge hit?** Yes. Vague impressions should trigger reflection, not logistics.

**Improvement idea:** Post-call framework should detect vague impressions and respond with excavation prompts: "You said it was a really good conversation — help me understand what made it feel that way. Did she say something that surprised you? Did you say something that felt true for the first time? What specifically do you want to remember from this call?"

---

## Cross-Cutting Patterns

### Pattern 1: No ranking rules when multiple connection types are present
**Affects:** R1-TC01, R1-TC05  
**Behavior:** Navigator blends all valid connection types instead of committing to the strongest one.  
**Fix:** Add an explicit decision rule for ranking connection types when multiple are present.

### Pattern 2: Connection type taxonomy has gaps
**Affects:** R1-TC02 (personal warmth), R1-TC04 (cross-cultural immigrant), R1-TC05 (existing mentorship)  
**Behavior:** Navigator defaults to the nearest available type, producing misaligned prep.  
**Fix:** Expand connection type definitions to cover: existing relationships, personal warmth, and cross-cultural immigrant solidarity.

### Pattern 3: No handling for weak/vague connections
**Affects:** R1-TC03  
**Behavior:** Any domain overlap, however thin, triggers domain-specific prep.  
**Fix:** Add a "weak connection" qualifier with sector-exploration framing.

### Pattern 4: Entire post-call phase is out of scope
**Affects:** All R7 cases  
**Behavior:** Navigator treats post-call notes as pre-call input. No depth signal recognition. No reflection prompts.  
**Fix:** Add a post-call reflection section triggered by "post-call notes" in user input.

---

## Priority Improvements for Next Iteration

| Priority | Change | Impact |
|---|---|---|
| P1 | Add post-call reflection framework | Unlocks all R7 cases — 5 tests from 1 to 4+ |
| P2 | Expand connection type taxonomy (personal warmth, cross-cultural immigrant, existing relationship) | Fixes R1-TC02, TC04, TC05 |
| P3 | Add ranking rules for multiple connection types | Fixes R1-TC01, TC05 partial |
| P4 | Add weak connection handling | Fixes R1-TC03 |

Addressing P1 alone would raise the overall average from 1.5/5 to approximately 2.5/5.  
Addressing P1 + P2 would raise it to approximately 3.5/5.

---

## What the Prompt Does Well (Don't Break These)

- Connection type identification works when the type is unambiguous (single strong signal)
- "About me" pitch logic is solid — consistent, non-adaptive, improvement-oriented
- Conversation script structure (Opening → About Me → Questions → Closing → Read the room) is coherent and learnable
- WHY explanations for each question teach transferable principles, not just justifications
- Cold outreach path (Step 0) is correctly triggered and well-structured
- No weak qualifier rule is consistently applied
