# Phase 2 Roadmap — Documented, Not Yet Built

These four are deliberately scoped but unbuilt. Listing them shows foresight about
where the portfolio could go next, without claiming work that hasn't happened. If
asked about any of these in an interview, the honest answer is: "That's on my roadmap
— here's how I'd scope it," followed by the paragraph below. Do not describe these as
built or tested.

---

## 1. Board Resolution & Governance Document Generator

**Scope:** A template-drafting workflow that generates board resolutions and
governance documentation (e.g., for ADGM authority submission) from structured inputs
— resolution type, parties, effective date, statutory basis — reducing repetitive
drafting for routine corporate actions.

**Risk profile:** Low. This is template population from clean, structured inputs,
similar in risk to the contract clause-risk flagger. No confidentiality issue if
built with synthetic company data, and no professional-judgment displacement since
the substance of a resolution (what the board is actually approving) still requires
a lawyer's drafting review before execution.

**Why it's Phase 2, not Phase 1:** Lower priority only because it has less "wow
factor" for a demo than the other three — it's genuinely useful but reads as
routine automation rather than a distinctive capability. Worth building if bandwidth
allows before the other two Phase 2 items below, given its low risk.

---

## 2. Shareholders' Agreement Clause Comparator

**Scope:** A workflow that compares two or more versions of a shareholders' agreement
(e.g., a term sheet vs. a long-form agreement, or successive drafts) and highlights
substantive deltas — not just redline/tracked-changes-style textual diffs, but
flagging where a change shifts risk allocation, control rights, or economic terms.

**Risk profile:** Low-moderate. Overlaps significantly with the existing
Contract Clause-Risk Flagger's precedent-grounded methodology — this is really a
comparator mode of the same underlying tool (compare draft-to-draft instead of
draft-to-reference-library). Low incremental build risk given the existing
`precedent-library.md` and prompt structure to build from.

**Why it's Phase 2:** Genuinely lower urgency since the clause-risk flagger already
demonstrates the core capability (comparison against a standard); this is a variant,
not a new capability, so it's reasonable to defer.

---

## 3. Sanctions & Adverse Media Triage Dashboard

**Scope:** A workflow that would ingest a client/counterparty name and structure a
preliminary adverse-media and sanctions-exposure summary to support first-pass
screening ahead of formal compliance sign-off.

**Explicit guardrail — read before building or demoing this one:** Real sanctions
and adverse-media screening requires licensed data feeds (e.g., Refinitiv World-Check,
Dow Jones Risk & Compliance, LexisNexis WorldCompliance) that maintain
verified, current watchlists. A general-purpose LLM has no reliable, current, or
complete view of sanctions lists and cannot substitute for a licensed screening tool
— it can hallucinate names, miss recent listings, or fabricate plausible-sounding but
false adverse-media hits. If this is ever built, it must be scoped narrowly as
"structuring and drafting a summary from search results a human has already gathered
from licensed sources" — never as the sanctions check itself. Any demo or CV
description must state this limitation up front, not as a footnote. This is the
single highest-risk item on this roadmap if mishandled, because unlike a contract
clause or a case brief, an incorrect sanctions "clearance" has real regulatory and
safety consequences.

---

## 4. Writ Petition Research & Case Strategy Assistant

**Scope:** A workflow that would assist with researching precedent and structuring
a case strategy memo for a writ petition — one step further than the argument-note
builder (Phase 1 extension of the case-summary tool), moving from organizing existing
briefs into actively researching and recommending an approach.

**Explicit guardrail — read before building or demoing this one:** "Case strategy"
edges into territory where an AI tool could be perceived as substituting for legal
judgment rather than supporting it — this is a materially different claim than
"organizes precedent for counsel's review" (the Phase 1 argument-note builder, which
stays on the safe side of this line). If built, this tool must be scoped so that it
only ever *surfaces* research (relevant statutes, precedent, procedural options) and
explicitly declines to recommend a strategy, with that boundary stated in every
output, not just in documentation. Also carries higher factual-accuracy risk than the
other three roadmap items: legal research assistants are exactly the category where
LLMs are known to hallucinate case citations that don't exist — any real build would
need a verification step (e.g., cross-checking every cited case against Manupatra/SCC
Online) before any output is trusted, let alone shown to an interviewer.

---

## How to present this roadmap in a cover letter or interview

> "Beyond what I've built, I've scoped four further tools — a board resolution
> generator, a shareholders' agreement comparator, a sanctions/adverse-media triage
> aid, and a litigation research assistant. I've deliberately not built the last two
> yet, because both carry real risks (unlicensed sanctions data, and case-strategy
> tools edging into displacing legal judgment) that need to be designed around
> carefully, not rushed past."

This answer signals seniority — most candidates either don't think about these risks
at all, or think about them but don't say so. Saying so, unprompted, is the stronger
move.
