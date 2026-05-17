# User Research Synthesis — Newcomers to Canada Navigator

**Project:** AI companion for Latino newcomers navigating the Canadian job market
**Last updated:** 2026-05-16
**Interviews completed:** 3 of 5+ planned

---

## Participants

| # | Name | Track | Background | Time in Canada | Status |
|---|------|-------|------------|----------------|--------|
| 1 | Martin F. | B (Transitioned) | Analytics/ML Director, Peru → MBA Western (Ivey) | 3.5 years | Now at Scotiabank |
| 2 | Maria | B (Transitioned) | Data Analyst/AI, Colombia → Mohawk College → Canadian Tire → Deloitte → TD → Jonas | ~5 years | Now in AI role, completing Queen's AI master's |
| 3 | Mariluz | A (Still navigating) | Clinical healthcare professional, Colombia → ICU support role | ~1.5 years (arrived Jan 2024) | Active job search, no role yet in field |

---

## Emerging Themes

### T1 — The LATAM-to-Canada Networking Mental Model Is the Core Unlock ✅ Confirmed ×3

Nobody explicitly teaches the difference. Newcomers arrive with the LATAM model (networking = who can guarantee you a job) and have to reverse-engineer the Canadian model (networking = visibility over time) through dozens of conversations.

> *"No hay manual o no se dice directamente. Se entendió después de conversar con muchas personas."* — Martin
> *"En el college era una materia obligatoria y ella no entendía lo del networking o cómo hacerlo ni por qué era importante."* — Maria
> *"Conseguir una entrevista de trabajo mediante eso"* — Mariluz (her only definition of networking success)

Mariluz is living proof of the pre-unlock state: she measures networking success solely by job interviews and can't yet see relationship quality as a valid outcome. The model mismatch is confirmed from both sides — users who've worked through it (Martin, Maria) and a user who hasn't (Mariluz).

**Implication for product:** Make this reframe explicit and early. Don't assume users understand why networking works differently here. The "why it matters" explanation needs to come with specifics — the mindset shift alone isn't enough.

---

### T2 — Latino Cultural Skills Are Suppressed, Not Leveraged ✅ Confirmed ×3 — Track A shows more severe form

Newcomers actively avoid other Latinos early in their search — fearing it looks insular or limits exposure. This backfires: Latino contacts offer the highest empathy, highest emotional support, and often highest referral conversion. In Track A, the cultural barrier combines with social anxiety to produce near-total avoidance of cold outreach.

> *"Al inicio él evitaba hacer networking con latinos para evitar hablar español, pero luego se dio cuenta que los latinos conocen las cosas por las que has pasado y son más abiertos a escuchar. No auto ponerse constraint."* — Martin
> *"Uno trae el chip colombiano de no quiero molestar a nadie, no quiero escribirle."* — Maria
> *"No es una persona muy sociable entonces la ansiedad de conocer a alguien que es la primer vez que vas a verla."* — Mariluz

Mariluz layered social anxiety on top of cultural inhibition — not just the cultural "no quiero molestar" but genuine discomfort meeting strangers, amplified by language barrier fears. She tried cold LinkedIn outreach once; got no response and stopped. She only does coffee chats when someone introduces her directly.

**Implication for product:** There are two distinct populations here — those with cultural inhibition (addressable with reframe + script) and those with social anxiety (need a warmer, lower-stakes entry point). The tool should offer both tracks. Warm introductions first, then gradually cold outreach with heavy scaffolding.

---

### T3 — "Ask for Advice, Not a Referral" Is Counterintuitive but High-Impact

The LATAM networking instinct is to ask for a referral or a recommendation. In Canada this closes relationships. Asking for feedback, suggestions, or resume review keeps them open and builds reciprocity.

> *"Pedir sugerencias o guías en vez de pedir referral."* — Martin
> *"Como latino, podemos usar la skill de sacar una chica a bailar... Toca saber manejar la distancia, decir sin decir."* — Martin

**Implication for product:** Teach the specific ask. The salsa analogy is a powerful teaching frame — it reframes indirection as Latin cultural fluency, not avoidance.

---

### T4 — Near-Quit Moments Are Repeated, Not One-Time ✅ Confirmed ×3 — Track A shows most severe form

Martin's near-quit was triggered by a specific event (promising chat → nothing). Maria had multiple near-quit moments sustained over months — cumulative frustration driven by survival pressure. Mariluz's near-quit is ongoing and existential — "volver al país de origen," "no sirvo para nada." She is living inside this experience right now.

> *"Una persona que publicó rol, coffee chat, pidió resume — cuando hablaron del rol le dijeron que no. Eso le hizo preguntarse si realmente funciona. Unas dos semanas se paró networking por eso."* — Martin
> *"Era muy frustrante y casi se rinde. Pero tenía SÍ o SÍ que buscar el work permit. Le TOCABA."* — Maria
> *"Lo que pasa por la cabeza es devolverse al país de origen – rendirse."* — Mariluz
> *"Frustración – como la idea de 'no sirvo para nada'."* — Mariluz

Three patterns identified: (1) event-triggered setback → pause → reframe (Martin), (2) cumulative frustration sustained by external necessity (Maria), (3) ongoing existential questioning with self-worth collapse (Mariluz). The third pattern is the most dangerous and the least served by existing resources.

**Implication for product:** The tool needs three intervention modes — post-event reflection, long-arc motivation anchoring, and self-worth stabilization for active sufferers. The last one is new from Mariluz and is distinct from generic "stay motivated" messaging.

---

### T5 — Progress Needs a Metric Beyond "Getting the Job" ✅ Confirmed ×3 — R8 negative confirmed in Track A

Users who only measure success by job offers will quit. The shift to relationship quality as a progress signal is what sustains momentum — but most users don't arrive at this without outside help. Mariluz, who is actively in the search, cannot yet make this shift: job interview is her only metric.

> *"Pero le sirvió para escoger mejor con quién tener los coffee chats."* — Martin (on how a rejection reframed his approach)
> *"Networking es para fortalecer red de contactos y hacerte visible para todo momento."* — Martin
> *"Celebrar pequeños logros: primera entrevista vs segunda ronda, primeros coffee chats, en lugar de enfocarse solo en el resultado final."* — Maria
> *"Conseguir una entrevista de trabajo mediante eso pero últimamente no ha tenido suerte."* — Mariluz (only success metric she can name)

This confirms the gap is real and unsolved for active searchers. Martin and Maria developed alternative metrics retrospectively, after the job landed. Mariluz is in the state the tool needs to intervene in.

**Implication for product:** Build in explicit progress signals: quality of conversation, follow-up sent, relationship moved forward. Make these visible before the job offer comes. Consider a visible milestone tracker with specific named checkpoints (not just "you're making progress"). The tool may need to explicitly teach the metric shift — not assume users will discover it on their own.

---

### T6 — Informal Mentorship Is Widely Underused and Has Outsized Impact

Almost no networker actively pursues informal mentors. Those who do get personalized guidance, emotional support, and long-term career growth. It's a teachable, specific behavior.

> *"La importancia del mentorship informal. Pocas personas que hacen networking lo hacen. Eso te va a ayudar eventualmente a crecer profesionalmente."* — Martin

**Implication for product:** Actively coach users toward identifying and cultivating informal mentors — not just coffee chats. This is a specific, differentiated action the tool can drive.

---

### T7 — Specialization Is Counterintuitive but Necessary ✅ Confirmed ×2

Newcomers default to applying broadly, assuming more applications = more chances. In reality, a specialized profile + personalized applications outperforms mass applying even without referrals.

> *"El ratio de veces que lo llamaban era más alto aún sin conocidos si se tomaba el tiempo de personalizar el resume en vez de postular masivamente."* — Martin
> *"Se busca más la especialidad y costó entender al inicio."* — Martin
> *"No entendía que las hojas de vida deben personalizarse, que títulos idénticos tienen funciones diferentes según empresa, y que ciertas industrias predominan en ciudades específicas."* — Maria

Maria added market structure knowledge to this theme: newcomers don't know that Toronto = financial sector, that the same title means different things at different companies, or that understanding the landscape before applying changes everything.

**Implication for product:** Still adjacent to the core networking focus, but confirmed as a consistent pain point. The tool may need a "Canadian job market basics" module — even a lightweight version — because users can't network effectively without this context.

---

### T8 — "How to Do It" Matters More Than "What to Do" — NEW from Maria

The college curriculum told Maria networking mattered and assigned events. YouTube told her how to structure a message, who to approach first, and what to say. The former created compliance; the latter created competence and confidence.

> *"Que hacer y el como es lo más importante con buen nivel de detalle."* — Maria
> *"Los videos daban ideas de cómo aplicarlos."* — Maria

The specific mechanics that users need but rarely get: how to find the connection point with a stranger, what to write in a first LinkedIn message, who to contact first (same country/university as the lowest-friction entry point).

**Implication for product:** Don't just explain the strategy. Provide specific, templated how-tos for each action step. The tool's differentiation over generic advice is that it walks users through the actual execution, not just the concept.

---

### T9 — Emotional Load Management Is the #1 Missing Resource ✅ STRONGEST signal — confirmed Track A

Maria named mindset prep as important retrospectively. Mariluz named emotional load management as the single most important missing resource from inside the active experience — the first Track A confirmation, and the most powerful statement in the research so far.

> *"Uno en la vida puede escoger cómo reacciona a lo que está pasando. Cuando eres nuevo es más fácil decir que uno es la víctima. Es el default de muchos."* — Maria
> *"Algo que ayude a las personas a preparar su mente para estar acá. Algo de motivación o mindset. Para empoderarlos."* — Maria
> *"La parte de la carga emocional – encuentras videos de networking, cover letter, etc. Nadie habla de la carga emocional y estrategias para no perder la moral y el ánimo de seguir. Es la más importante porque sin energías ni ánimos para seguir el resto pierde importancia."* — Mariluz
> *"Todo mundo dice la solución (cover letter, networking, LinkedIn) — a ella no le interesa eso porque lo encuentra en internet pero necesita es mantener la motivación y con eso se llega a los recursos."* — Mariluz

This is the sharpest statement of the product's differentiator from any participant: **the tactical information is abundant and findable; what's missing is emotional sustainability.** The tool's unique value is not what it teaches but the fact that it keeps users going long enough to apply what's already available.

**Implication for product:** This should be the core of the product's identity. Not "networking coach" but "the thing that keeps you in the search." Emotional load management and motivation anchoring should be primary, not a module. The tactical content (templates, scripts, resources) is secondary — it's what a motivated user can then access.

---

### T11 — "Remove Networking" Is the Ideal, Not "Get Better at It" — NEW from Mariluz (Track A)

When asked what she would change about her networking approach, Mariluz's answer was not "be better at it" — it was "removerlo definitivamente" (remove it entirely). This is the authentic starting point for a significant portion of Track A users: networking is a burden to escape, not a skill to develop.

> *"Removerlo definitivamente."* — Mariluz (response to "if you could change one thing about your networking approach")
> *"No es una persona muy sociable."* — Mariluz

This is not a failure state — it's a valid user truth. Users who resent networking will not engage with a tool framed as "networking help." The product must meet them where they are: framing networking as a temporary, reduced-friction necessity rather than a skill set to embrace.

**Implication for product:** The value proposition for Track A users should be: "make the networking you can't avoid less painful and more effective" not "become a better networker." The goal is to lower the activation energy to the point where they take one action, then the next. Framing matters enormously — the word "networking" may itself be a barrier.

---

### T10 — Community Is a Core Feature, Not a Nice-to-Have — NEW from Maria

Job searching alone is corrosive. Maria identified community — shared frustrations, shared tips, mutual referrals — as "fundamental," not supplementary. A peer network that accompanies the search changes the emotional experience.

> *"Buscar trabajo es muy frustrante, viene con muchos alti bajos, tener una comunidad con la que las personas puedan estar rodeadas, compartir frustraciones y tips. Es fundamental."* — Maria

**Implication for product:** The current product concept is 1:1 user-to-AI. This feedback suggests a community layer (even lightweight: cohorts, shared boards, accountability partners) could dramatically increase both engagement and outcomes. Worth validating with other participants — if 3/5+ name community, it belongs in v1 scope.

---

## Quality Risk Signal Tracker

| Signal | Status | Evidence |
|--------|--------|----------|
| **R8 — Progress beyond job offer** | ✅ Confirmed ×3 — gap confirmed in Track A | Martin reframed through reflection; Maria named specific granular milestones. Mariluz (Track A) cannot articulate any metric beyond job interview — confirms this is unsolved for active searchers. |
| **R7 — Relationship depth over breadth** | ✅ Confirmed (Martin, Mariluz negative) | Martin: one 4-month relationship → role. Mariluz: has coffee chats but can't maintain relationships after them — can't find the reconnection point. The gap is confirmed from both sides. |
| **R1 — Multi-connection contacts convert better** | Preliminary signal (Martin) | Same country + social setting + domain fit = referral. Maria noted LinkedIn messages worked even "en visto." Mariluz only engages through warm intros. |
| **Emotional load as #1 gap** | ✅ Strongest signal in research | Mariluz: "la carga emocional es lo más importante porque sin energía el resto pierde importancia." Named from inside active search. Confirmed by Maria retrospectively. |
| **Community as structural need** | ✅ Partial (Maria); WILL Employment as proxy (Mariluz) | Maria named community as fundamental. Mariluz finds in-person WILL Employment events valuable for energy and encouragement but doesn't reconnect with contacts after. In-person community provides motivation; doesn't yet answer the reconnection gap. |
| **Social anxiety as distinct barrier from cultural inhibition** | ✅ NEW — Track A signal | Mariluz has genuine social anxiety layered on cultural "no molestar." This is a more severe barrier requiring a different intervention than reframe/permission alone. |

---

## Resources Mentioned

| Resource | Type | Notes |
|----------|------|-------|
| Western (Ivey) career services | University | Resume review, mock interviews, alumni DB. Only available during enrollment. |
| HispanoTech | Non-profit | Latino professional network with mentorship programs |
| ALPFA | Non-profit | Latino professional association, mentorship programs |
| Strengths assessment (name TBD) | Tool | Used at Western, helped identify standout strengths. Martin to follow up with name. |
| Madeleine Mann (YouTube) | Content creator | Job search / networking how-tos. Maria credits her as the single most impactful resource. Two N's in Madeleine. |
| Mohawk College Professional Development | College program | Forced networking at 3 events, mock interviews, resume tailoring. Maria says she wouldn't have done any of it otherwise — the obligation was the value. |
| IIBA Chapter (volunteering) | Professional org | Maria became president of a local chapter — built confidence for talking to strangers through forced repetition. |
| LinkedIn coaches (free content) | Social media | Maria consumed free posts from job search coaches; didn't pay for coaching but got value from public content. |
| WILL Employment Solutions | Non-profit / settlement org | Mariluz attends workshops and conferences for internationally trained professionals. Valued for encouragement and key practical points. In-person events more effective than virtual for her. |
| Career coach (unnamed) | Professional coaching | Mariluz has a career coach. Helps with the search but doesn't fill the emotional load gap she described. |

---

## Open Questions

- [x] Does the LATAM networking model mismatch show up consistently across participants? → **Yes, confirmed by Maria and Mariluz. Not cohort-specific.**
- [x] How do Track A participants describe the near-quit moment? → **Ongoing and existential for Mariluz: "volver al país de origen," "no sirvo para nada." More severe than Track B patterns.**
- [x] What does "progress" look like to someone still in the search — can they articulate any metric beyond job offer? → **No. Mariluz's only metric is a job interview via networking. The gap is real and unresolved.**
- [x] Does the Latino-network-avoidance pattern appear in Track A participants too? → **Yes and stronger: Mariluz adds social anxiety on top of cultural inhibition. Cold outreach = one try, no response, stopped.**
- [x] How do Track A participants respond to the mindset/resilience framing? → **Strongly resonates. Mariluz named emotional load management as the #1 missing resource — more important than any tactical content.**
- [ ] Is informal mentorship something users will actively pursue if the tool suggests it, or does it feel overwhelming? → Still open. (Mariluz already has a career coach but it doesn't fill the emotional gap.)
- [ ] Does community come up again at 3+ participants? → Partial signal (WILL Employment events for Mariluz), but not named as "community" explicitly. Still open.
- [ ] Is forced engagement a pattern? (Maria: college obligation was essential. Can the tool create that same structure without institutional enforcement?)
- [ ] NEW: Does the "remove networking" ideal show up in other Track A participants? If common, the tool's framing needs to shift fundamentally.

---

## Next Interviews

**Martin's wife** — Track A (currently navigating the transition). Scheduled TBD.
**Referrals from Mariluz** — she may know others in similar situation. Worth asking.

---

## Signal Strength Summary (3 interviews)

| Theme | Strength | Track coverage |
|-------|----------|---------------|
| T1 — Mental model mismatch | Strong | B, B, A |
| T2 — Cultural suppression / "no molestar" + social anxiety | Strong | B, B, A (more severe in A) |
| T3 — Ask for advice, not referral | Moderate | B only |
| T4 — Near-quit moments (three distinct patterns) | Very strong | B, B, A (most severe in A) |
| T5 — Progress metrics beyond job offer | Very strong | B, B, A (gap confirmed in A) |
| T6 — Informal mentorship | Weak | B only |
| T7 — Specialization required | Strong | B, B |
| T8 — HOW matters more than WHAT | Strong | B (Maria primary) |
| T9 — Emotional load management as #1 gap | **Strongest in research** | B (Maria), A (Mariluz) |
| T10 — Community as structural need | Moderate | B (Maria), A (partial: WiL) |
| T11 — "Remove networking" as user ideal | NEW — Track A signal | A only (Mariluz) |

**Updated priority for upcoming interviews:** T11 (framing), T10 (community), T3 (Track A version of "advice not referral"). T9 is now the product's clearest differentiator — hold as confirmed.

**Critical insight from 3 interviews:** The tactical content gap (T8) is real but secondary. The emotional sustainability gap (T9) is primary and completely unserved by existing resources — including career coaches. The product's core identity should be built around this.
