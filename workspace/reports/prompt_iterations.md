# Prompt Iterations Log
**Project:** Navigator for Latino Newcomers to Canada  
**Prompt file:** workspace/prompts/

---

## v2 → v3 (2026-05-12)

### Baseline (v2) scores
| Test Case | Risk | Rating |
|---|---|---|
| R1-TC01 | Multi-connection: Maria VP + cultural | 3/5 |
| R1-TC02 | Multi-connection: Carlos friend | 2/5 |
| R1-TC03 | Multi-connection: Ahmed vague domain | 2/5 |
| R1-TC04 | Multi-connection: Jin cross-cultural immigrant | 1/5 |
| R1-TC05 | Multi-connection: Dr. Sarah existing mentor | 2/5 |
| R7-TC01 | Post-call: Ana unprompted offer | 1/5 |
| R7-TC02 | Post-call: Marco reciprocal curiosity | 1/5 |
| R7-TC03 | Post-call: Patricia self-disclosure | 1/5 |
| R7-TC04 | Post-call: David no signals (false positive) | 1/5 |
| R7-TC05 | Post-call: Valentina vague notes | 1/5 |
| **Average** | | **1.5/5** |

### Changes made in v3
1. **Expanded connection type taxonomy** — added "Existing relationship (mentor/supervisor/sponsor)" and "Personal warmth / existing friendship" as explicit types with their own prep logic
2. **Broadened cultural connection** — from "shared Latino background" to "shared experience navigating Canada as a newcomer or visible minority professional — regardless of specific cultural background"
3. **Added ranking hierarchy** — explicit priority order when multiple connection types are present; cultural/immigrant overrides domain at Director+ level
4. **Added weak connection handling** — cross-sector domain overlap without other connections triggers "genuine curiosity framing" instead of domain-specific prep
5. **Added post-call reflection framework (Mode B)** — triggered by past-tense input; covers depth signal check, vague notes excavation, relationship classification, and next step guidance
6. **Updated output format** — separate pre-call and post-call output templates

### Expected v3 scores (re-evaluation against same test cases)

**R1-TC01** (Maria, VP Data Science + cultural): **4/5**  
New ranking rule says cultural overrides domain at Director+ level. Navigator should now commit to cultural as primary anchor and explicitly note domain is not the prep angle. Minor remaining risk: ranking rule says "especially at senior levels" — navigator might hedge on exactly what counts as senior enough.

**R1-TC02** (Carlos, existing friend): **5/5**  
"Personal warmth / existing friendship" is now a defined connection type (#2 in hierarchy). Prep logic explicitly says: lead with reconnection, reference shared history, do not treat as newcomer networking call.

**R1-TC03** (Ahmed, cross-sector vague domain): **4/5**  
Weak connection handling now explicitly says: cross-sector domain overlap → genuine curiosity framing. Navigator should correctly identify this as a thin connection and generate sector-exploration questions instead of domain questions.

**R1-TC04** (Jin, Korean-Canadian): **5/5**  
Cultural connection definition now explicitly includes "both navigating Canada as immigrants/visible minorities from different backgrounds." Jin's case is now squarely in scope.

**R1-TC05** (Dr. Sarah, existing mentor): **5/5**  
"Existing relationship — mentor/supervisor/sponsor" is now connection type #1 with dedicated prep logic: open with genuine update, ask for something specific. Navigator should no longer treat this as a domain contact.

**R7-TC01** (Ana, unprompted offer): **5/5**  
Post-call framework now explicitly names unprompted offer as a STRONG signal and "Connector" relationship classification. Next step guidance: follow up specifically on the introduction.

**R7-TC02** (Marco, reciprocal curiosity): **5/5**  
Reciprocal curiosity is now a named depth signal. "Relationship worth investing in" classification applies. Next step: specific second conversation topic from content of first call.

**R7-TC03** (Patricia, self-disclosure): **5/5**  
Personal self-disclosure is named as a MENTOR potential signal. Classification: "Mentor potential." Next step: second conversation, not thank-you email.

**R7-TC04** (David, no signals): **5/5**  
Signal absence is explicitly checked. "Seniority is not a depth signal" is a named rule. Classification: "Useful one-time conversation." Next step: specific thank-you, no follow-up pitch.

**R7-TC05** (Valentina, vague notes): **5/5**  
Vague notes check triggers excavation prompts before any logistics. Navigator cannot skip to follow-up until user has excavated what was meaningful.

| Test Case | v2 | v3 (expected) | Delta |
|---|---|---|---|
| R1-TC01 | 3/5 | 4/5 | +1 |
| R1-TC02 | 2/5 | 5/5 | +3 |
| R1-TC03 | 2/5 | 4/5 | +2 |
| R1-TC04 | 1/5 | 5/5 | +4 |
| R1-TC05 | 2/5 | 5/5 | +3 |
| R7-TC01 | 1/5 | 5/5 | +4 |
| R7-TC02 | 1/5 | 5/5 | +4 |
| R7-TC03 | 1/5 | 5/5 | +4 |
| R7-TC04 | 1/5 | 5/5 | +4 |
| R7-TC05 | 1/5 | 5/5 | +4 |
| **Average** | **1.5/5** | **4.8/5** | **+3.3** |

### What was preserved from v2
- "About me" pitch logic (build once, improve over time, never adapt per contact)
- Conversation script structure (Opening → About Me → Questions → Closing → Read the room)
- WHY explanations for each question
- Cold outreach path (Step 0)
- No weak qualifier rule
- Spanish language notes
- Scaffold-not-script philosophy

### Remaining risks in v3
- **R1-TC01 not at 5/5**: The ranking rule says cultural overrides domain "especially at senior levels" — "especially" leaves wiggle room. Could be tightened to a hard rule at Director+ level.
- **Post-call framework is new and untested with real users**: The depth signal vocabulary (unprompted offer, reciprocal curiosity, self-disclosure) will need validation with actual newcomers to confirm it translates into their lived experience.
- **Spanish post-call output untested**: v2 Spanish testing covered pre-call only. Post-call reflection in Spanish may surface new phrasing issues.

---

## Open questions for next sprint
1. Does the post-call framework resonate with real newcomers, or does the depth signal vocabulary feel clinical?
2. At what point does the navigator help users improve their "about me" — after how many sessions, and on what trigger?
3. How does the navigator handle a contact with NO discernible connection type at all (true cold, different field, different background, no shared context)?
