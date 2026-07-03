# Contract Risk Review & Negotiation Playbook Generator
*(working name: Contract Clause-Risk Flagger)*

**What it is:** A repeatable AI-assisted workflow for first-pass contract review. Feed a contract to an LLM with a structured prompt, and it flags clauses that deviate from market-standard positions on liability, indemnity, termination, and other high-risk terms — before a human lawyer does the detailed review.

**Why it matters:** First-pass review (skimming for red flags before deep analysis) is repetitive and time-consuming. This workflow doesn't replace legal judgment — it triages, so your review time goes to the clauses that actually need it.

## How to use it

1. Take the contract text (paste it, or export from PDF/Word to plain text).
2. Use the prompt in `prompt-template.md`, replacing `[CONTRACT TEXT]` with the actual contract.
3. Run it through Claude, ChatGPT, or any capable LLM.
4. Review the flagged output against your own judgment — this is a triage tool, not a substitute for review.

## Files in this folder

- `prompt-template.md` — the reusable prompt (v1: judges against general "market standard" knowledge)
- `sample-contract.md` — a synthetic co-founder/shareholders' agreement excerpt with deliberately planted risk issues (for demo purposes only — not a real client document)
- `sample-output.md` — the flagged output when the v1 prompt is run against the sample contract
- `precedent-library.md` — a small curated set of market-standard reference clauses, used to ground v2's output in specific comparator language
- `prompt-template-v2-grounded.md` — v2 of the prompt: retrieval-style, compares clauses against the precedent library explicitly rather than relying on the model's general knowledge
- `sample-output-v2.md` — the flagged output when v2 is run against the sample contract, including redlines and an honest "uncategorized" flag where no reference clause exists
- `cv-summary.md` — a one-line, quantified summary to put on your CV/LinkedIn, plus talking points for interviews, including how to accurately describe v2 (retrieval-grounded prompting, not a fine-tune)
- `real-example-yc-safe.md` — the flagger run against the actual, current Y Combinator Post-Money SAFE template (real public document, not synthetic) — a genuinely checkable example, and notable for correctly returning a "clean, no major issues" result rather than manufacturing findings on a well-drafted instrument
