# How to Talk About This Portfolio — Cover Letter & Interview Framing

## Cover letter paragraph (adapt per role/track)

> Alongside my transactional and litigation practice, I've built a small set of
> AI-assisted legal workflows — a contract clause-risk triage tool, a UBO/AML red-flag
> mapper, an ESG disclosure gap analyzer, and a case-briefing standardizer — designed to
> speed up first-pass review without displacing legal judgment. I tested the contract
> tool against the actual Y Combinator SAFE template and the case-briefing tool against
> a live Calcutta High Court judgment, so the outputs are verifiable against real,
> public source material rather than staged examples.

Trim to 2 sentences for a cover letter; the fuller version works better in a portfolio
email or LinkedIn "featured" section.

## Interview opener (when asked "tell me about a project you're proud of" or "how do you use AI in your work")

Structure: **problem → what you built → how you validated it → the limit you're honest about.**

> "First-pass contract review is repetitive — the same checklist of indemnity,
> liability, termination issues, every time. I built a structured AI prompting
> workflow that triages a contract against that checklist before I do the detailed
> read. I tested it two ways: against a synthetic contract with planted issues, where
> it correctly caught six high/medium-risk clauses, and against the actual Y Combinator
> SAFE — a genuinely well-drafted instrument — where it correctly found nothing wrong
> instead of manufacturing problems. That second result mattered more to me, honestly,
> because a tool that only ever finds issues isn't one I'd trust."

Then, if pushed further: **be ready with the limit.**

> "It's a triage aid, not a substitute for review — I wouldn't rely on it for
> anything client-facing without checking every flag myself, and I'd never put real
> client documents through a general-purpose AI tool without firm approval and a
> compliant data-handling process."

## If asked "did you fine-tune a model" (this WILL come up if you mention "AI projects" anywhere)

Say no, directly, and explain what you actually did:

> "No — I didn't fine-tune a model. I built retrieval-grounded prompting workflows,
> where the model compares the document against a curated set of reference clauses I
> provide, rather than relying on its general training knowledge. That's the same
> underlying idea behind production retrieval-augmented generation systems, just scoped
> down to something I could build and fully explain without training infrastructure or
> a large annotated dataset."

This is a stronger answer than a vague "yes" would be if you can't back it up — interviewers
who ask this question are usually testing whether you understand the difference, not
whether you've done something maximally technical.

## What NOT to say

- Don't say "I built an AI tool that does X" without immediately being ready to explain
  how, on what data, and with what limits — vague AI claims read as buzzword-chasing to
  both legal and technical interviewers.
- Don't claim you've used this on real client matters unless you actually have, with
  sign-off. If you haven't, say "personal initiative, tested on public/synthetic
  material" — that's a perfectly strong answer and it's true.
- Don't lead with the tools (Claude/ChatGPT) — lead with the legal problem and the
  checklist/methodology. The AI is the implementation detail, not the point.

## Where each artifact lives (for your own reference before an interview)

- Contract Risk Review & Negotiation Playbook Generator: `01-Contract-Clause-Risk-Flagger/` — real example: YC SAFE; playbook extension in `playbook-extension.md`
- AML/KYC Client Risk Review Assistant: `02-AML-KYC-Triage-Assistant/` — synthetic only, by design
- ESG Readiness & Governance Gap Analyzer: `03-ESG-Regulatory-Gap-Tracker/` — real example: ADIB public ESG page
- Judgment Summarizer & Argument Note Builder: `04-Case-Summary-Tool/` — real example: Calcutta HC judgment (Jindal v. WB, July 2025); argument-note extension in `argument-note-extension.md`
- Phase 2 roadmap (unbuilt, scoped): `05-Phase-2-Roadmap.md`
