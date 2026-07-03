# Extension — Negotiation Playbook Generator

**Repositioning, not a new build:** this turns the existing clause-risk flagger output
into an internal negotiation playbook format — the same underlying workflow
(precedent-grounded flagging), reformatted for a different use case. Matches the
"Contract Risk Review & Negotiation Playbook Generator" framing.

**Important scope boundary:** this tool surfaces fallback positions drawn from the
precedent library — it does not decide negotiation strategy. The lawyer chooses which
fallback to deploy, in what order, and how hard to push. Any playbook output should
carry this distinction visibly; presenting it as "AI negotiation strategy" overstates
what it does and is the kind of claim that invites — and fails — scrutiny.

## Prompt Template

```
You are helping a commercial lawyer prepare an internal negotiation playbook from a
clause-risk review. For each flagged clause below, produce a playbook entry. You are
not deciding negotiation strategy — you are organizing fallback positions for the
lawyer to choose from.

For each flagged clause, output:
- **Clause:** [name]
- **Opening ask:** [the ideal position, drawn from the reference/precedent library]
- **Fallback position 1:** [a middle-ground alternative if the opening ask is rejected]
- **Fallback position 2:** [the minimum acceptable position before walking away]
- **Walk-away trigger:** [what would make this clause a deal-breaker, if anything]
- **Talking point:** [one sentence framing for why this matters commercially, not just legally]

Do not recommend which fallback to use in a live negotiation — that is the lawyer's
judgment call based on relationship, leverage, and deal context you don't have
visibility into.

FLAGGED CLAUSES (from clause-risk review):
[PASTE OUTPUT FROM prompt-template-v2-grounded.md]
```

## Worked Example (using the flagged clauses from `sample-output-v2.md`)

**Clause:** 9 — Termination
**Opening ask:** Termination without cause requires 60 days' notice; "for cause" requires a 30-day cure period; unvested equity is protected from forfeiture absent an express contrary provision (per reference clause).
**Fallback position 1:** Reduce notice to 30 days if the counterparty pushes back, but hold firm on the cure period and vesting protection.
**Fallback position 2:** Accept immediate termination for cause only if narrowly defined (fraud, gross misconduct), with unvested equity protection non-negotiable.
**Walk-away trigger:** Any version that allows termination without cause AND immediate forfeiture of unvested equity in the same clause — this combination creates unacceptable founder risk.
**Talking point:** "This isn't about distrust — it's about making sure a founder's equity reflects work actually done, which protects both sides if the relationship doesn't work out."

---

**Clause:** 15 — Governing Law & Dispute Resolution
**Opening ask:** Fix governing law and arbitration seat now, under a named institutional rules body (e.g., DIFC-LCIA).
**Fallback position 1:** Accept a different but still fixed, enforceable seat if the counterparty has a genuine reason to prefer it (e.g., their existing corporate presence).
**Fallback position 2:** Accept litigation instead of arbitration if the fixed forum is otherwise reasonable — the core issue is fixing the forum, not the mechanism.
**Walk-away trigger:** Any version that leaves the seat "to be agreed" or at one party's unilateral discretion — this isn't a negotiating position, it's an enforceability defect.
**Talking point:** "An undefined forum isn't a compromise — it's a future dispute about where to have the dispute. Fixing it now costs nothing and prevents that."

## CV / Interview Note

Frame this as a natural extension of the clause-risk flagger, not a separate build:
"After building the triage tool, I extended it into a playbook format that organizes
fallback positions for negotiation — the AI surfaces options, I decide which to use."
That sentence alone answers the "did the AI negotiate for you" question before anyone
asks it.
