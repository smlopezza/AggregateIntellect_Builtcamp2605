# Experiment Results — Navigator Coffee Chat Prep

**Date:** 2026-05-05
**Prompt tested:** prompts/testing_prompt.txt (v2)
**Test cases run:** 4 (Jessie, Aitor, Carlos, Jessie in Spanish)

---

## experiments_conducted

1. **Jessie** — warm intro, same domain, shared academia→industry journey, first coffee chat, fear-based
2. **Aitor** — hot intro via mentor, same domain, shared journey, VP level
3. **Carlos** — cold (met briefly at keynote), cultural connection (Latino), different field, Partner level
4. **Jessie in Spanish** — same as case 1, full bilingual test

---

## successful_patterns

- **Connection type identification works:** The navigator correctly identified that Carlos's connection was cultural (Latino/shared immigrant experience), not domain-based — and built all prep questions around that. Did not generate a single cybersecurity question.
- **Questions felt tailored:** Questions were meaningfully different across all three contacts. Same domain questions for Jessie/Aitor did not work for Carlos.
- **WHY explanations teach transferable principles:** Each question's explanation named a reusable principle (e.g., "find the shared experience and go deep," "show self-reflection before asking for advice") — not just justification for one call.
- **Conversation script structure works:** Opening → About Me → Questions → Closing → Read the room felt natural and complete.
- **"Read the room" ask logic:** Three-option framework (second meeting / referral / gracious close) tested better than ranked primary/secondary asks.
- **Spanish structure was largely natural:** Bones of the script were correct; needed only minor phrasing corrections (see failure modes).
- **Cold outreach for Carlos:** Outreach message approach (anchor to event, name the topic explicitly, "not about cybersecurity") felt right and authentic.

---

## failure_modes

- **"About me" drift:** Initial test adapted the "about me" per contact. Corrected: one consistent pitch, unchanged per meeting, improved over time.
- **Weak qualifiers in asks:** First iteration included "I promise I'll keep it focused" and "but no pressure at all." These were removed. All asks should be clean and direct regardless of seniority.
- **Spanish phrasing issues (3 specific):**
  - ❌ "tenía muchas ganas de esta conversación" → ✅ "tenía muchas ganas de conocerte"
  - ❌ "Pero me gustaría..." (unnecessary contrast) → ✅ "Me gustaría..."
  - ❌ "Esto ha sido de muchísima ayuda" → ✅ "Esta conversación ha sido de muchísima ayuda"
- **Default meeting time:** Initial prompt used 20 minutes. Corrected to 30 minutes as default.
- **VP framing:** First Aitor script adapted the "about me" for executive framing — corrected. The bridge sentence after the pitch handles context, not the pitch itself.

---

## refined_approach

**Confirmed design decisions:**
- One "about me" pitch built once, improved over time — never adapted per contact
- Connection type (domain / shared journey / cultural / warmth) drives prep strategy
- Output is a conversation script, not a question list
- Ask is a "read the room" decision with 3 options
- No weak qualifiers at any seniority level
- Default ask: 30 minutes
- Cold contacts: help with outreach message before coffee chat prep
- Scaffold, not script — the goal is independence

**Open questions for next iteration:**
- Spanish needs native speaker validation with real users — phrasing errors were minor but present
- How does the navigator handle a contact where there is NO obvious connection type? (true cold, different field, different background)
- At what point in the conversation sequence does the navigator help the user improve their "about me"?
- The "read the room" options need testing with real newcomers — do they actually use them or freeze anyway?
