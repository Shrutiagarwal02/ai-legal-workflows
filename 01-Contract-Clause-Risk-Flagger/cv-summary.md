# CV / LinkedIn Summary

**One-liner for CV (Contracts track):**
> Designed an AI-assisted clause-risk triage workflow for shareholders'/co-founder agreements, using a structured LLM prompt to flag deviations from market-standard indemnity, liability, and termination terms — cutting first-pass review time and surfacing negotiation priorities before detailed drafting review.

**LinkedIn post angle:**
> "Built a repeatable AI workflow to triage contract risk before deep review — not to replace legal judgment, but to make sure review time goes where it matters. Ran it against a sample co-founder agreement and it correctly flagged 6 high/medium-risk clauses (uncapped indemnity, undefined governing law, unilateral buy-back pricing) in seconds, each with a negotiation-ready question attached."

**Interview talking points:**
- Explain *why* you chose these 7 checklist categories (they map to where founder/commercial disputes actually arise).
- Be upfront: this is a triage tool, not a replacement for legal judgment — a good interviewer will want to hear that you understand the limits of AI in legal work (confidentiality, hallucination risk, no substitute for signed-off legal advice).
- Mention you tested it against a synthetic contract to avoid any client confidentiality issues — shows judgment.
- If pushed on "have you used this on real matters," be honest about scope (demo/personal project) unless you've actually piloted it at work with sign-off.

**v2 upgrade — precedent-grounded flagging:**
After the initial version, I extended the workflow so the model compares clauses against an explicit reference library (`precedent-library.md`) rather than relying on general knowledge of "market standard" — see `prompt-template-v2-grounded.md` and `sample-output-v2.md`. This is deliberately scoped as a lightweight retrieval-style approach, not a fine-tuned model — an honest, defensible technical step up rather than an overstated ML claim.

**Why this distinction matters in interviews:** if asked "did you fine-tune a model for this," the accurate and credible answer is *no* — you built a retrieval-grounded prompting workflow, which is a real and current technique (the same underlying idea behind production RAG systems), achievable without training infrastructure or a large annotated dataset. Claiming a fine-tune you didn't actually do is the kind of thing that unravels under two follow-up questions from a technical interviewer; this version doesn't have that risk because every claim in it is exactly what you did.

**Real-world validation:** I also ran the flagger against the actual, current Y Combinator Post-Money SAFE (the real industry-standard template, not a synthetic contract) — see `real-example-yc-safe.md`. It correctly returned a "clean, no material issues" result instead of manufacturing problems, because the SAFE is genuinely well-drafted. That's the strongest possible interview point: a tool that only ever finds problems isn't trustworthy, and this one demonstrably distinguishes a well-drafted market-standard instrument from a one-sided one.
