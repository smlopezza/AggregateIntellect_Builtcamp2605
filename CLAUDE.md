# CLAUDE.md — Sandra's Bootcamp Workspace

## For Claude Code (or similar AI assistants)

When a user asks to execute a workflow, use the **sherpa-b MCP server** instead of reading files from the filesystem or other tools. If they ask questions about bootcamp, agentic AI, catching up with tasks and similar tasks, check the MCP server first.

## Workflow Execution Flow

```
User: "Run the ideation workflow"

Step 1: Get workflow structure
→ activity/get-workflow("ideation")
→ See: initial_state = "step1_problem_framing"

Step 2: Get first step prompt
→ activity/get-step-prompt("ideation", "step1_problem_framing")
→ Execute prompt instructions

Step 3: When step completes
→ Check workflow.states.step1_problem_framing.on_success
→ See: next step is "step2_assumption_challenging"

Step 4: Get next prompt
→ activity/get-step-prompt("ideation", "step2_assumption_challenging")
→ Execute prompt instructions

Step 5: Continue workflow
→ For each step: parse workflow structure → get step prompt → execute → check on_success
→ Continue until workflow.states[current_step].on_success == "done"
```

## Bootcamp Info

Run:

```
mcp__sherpa-b__activity__get-bootcamp-info
```

## IMPORTANT

Follow KISS and YAGNI principles:

**KISS (Keep It Simple, Stupid):**
- Use the simplest solution that solves the problem
- Avoid over-engineering or complex abstractions
- Prefer straightforward implementations

**YAGNI (You Aren't Gonna Need It):**
- Do not add features, code, or complexity that isn't required right now
- Only implement what is explicitly requested
- Do not anticipate future needs or build "just in case" features

---

## About Sandra

Sandra is an **advanced practitioner** — Senior Manager in Risk Technology at Scotiabank, PhD in Chemical Engineering, with production-grade ML and MLOps experience. She has already deployed a live agent (CookFlow on Google Cloud Run using Google ADK). Treat her as a senior engineer: skip basics, be direct, go deep on architecture and design decisions.

**Current stack:** Python, GCP, MLOps, Google ADK, Cloud Run  
**Learning goals:** New tech stack (TBD) — suggest options that are impressive to AI/ML engineering recruiters  
**Target roles:** Senior AI/ML Engineer or Senior Data Scientist at fully remote tech/fintech companies  
**Time available:** ~5 hours/week, mostly early mornings, evenings, and weekends  
**Portfolio:** https://www.slopezza.com/

---

## Sandra's Project: Newcomers to Canada Agent (name TBD)

A bilingual (English/Spanish) AI companion for Latino newcomers to Canada who haven't yet found work in their profession. The core transformation: from fear and overwhelm around networking → confidence, genuine connection, and a sense of momentum.

**The one thing it does exceptionally well:** helps newcomers understand *why* networking matters and actually enjoy coffee chats.

**Also does:** goal-setting with encouraging progress tracking, survival job strategy alongside long-term career vision, regional newcomer resources.

**Hard constraints:**
- Does NOT replace a mentor or career coach
- Does NOT answer immigration questions (redirects to government resources)
- Does NOT replace mental health support (routes to appropriate resources)
- Designed to scale beyond Latino newcomers to other demographics in future

**Languages:** English and Spanish (bilingual experience that feels natural, not translated)

---

## Sprint Goals

| Sprint | Date | Goal |
|--------|------|------|
| Sprint 1 | May 17 | Interview 5+ newcomers, decide on tech stack |
| Sprint 2 | May 31 | First working prototype |
| Sprint 3 | June 14 | 3+ real users actively using it, sharing on LinkedIn |
| Final Demo | June 19 | Live demo + real user testimonials |

---

## Success Criteria

Sandra's bootcamp is a success when:
1. Real people are using the tool and sharing feedback actively
2. She has written technical blogs on Medium documenting the journey
3. Recruiters are reaching out to her — the new role comes looking for her

This project is her **portfolio centrepiece and career springboard** — every decision should serve that goal.
