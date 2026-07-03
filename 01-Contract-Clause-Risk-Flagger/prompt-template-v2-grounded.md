# Prompt Template v2 — Precedent-Grounded Clause Flagger (Retrieval-Style)

**What's different from v1:** the original flagger asked the model to judge clauses
against "market standard" from its own general training knowledge. This version
retrieves specific reference clause language from `precedent-library.md` and hands it
to the model directly, so every flag is reasoned against an explicit comparator you
control — not the model's memory. This is the credible middle ground between a plain
prompt and an actual fine-tune: same underlying idea as retrieval-augmented generation
(RAG), scoped down to something you can build and explain end-to-end without training
infrastructure.

```
You are assisting a commercial lawyer with first-pass review of a contract. You will be
given (1) a small library of market-standard reference clauses and (2) the contract
under review. Your job is to compare, not to invent a market standard from memory —
ground every judgment explicitly in the reference text provided.

REFERENCE CLAUSE LIBRARY:
[PASTE RELEVANT SECTIONS OF precedent-library.md HERE — e.g., the Indemnity, Liability
Cap, Termination, Assignment, Governing Law, and Buy-Back examples]

For each clause in the contract under review that maps to a category in the reference
library, output:
- **Clause:** [name/reference in the contract]
- **Reference standard used:** [which named reference clause you compared it to]
- **What the contract says:** [1-sentence summary]
- **Comparison to reference:** [specific delta — what's missing, broader, narrower, or
  reversed relative to the reference clause language]
- **Severity:** High / Medium / Low
- **Suggested redline:** [a specific proposed replacement or amendment, drawing
  language from the reference clause where appropriate — not just a general question]

If a clause in the contract has no corresponding category in the reference library,
note it separately as "Uncategorized — no reference available" rather than guessing.

End with an overall risk summary and a redline priority order.

CONTRACT TEXT:
[CONTRACT TEXT]
```

**Why this is a stronger artifact than v1 for interviews:**
- It forces citation-style reasoning ("compared to reference X, this clause differs by
  Y") instead of an unverifiable claim of market knowledge — closer to how a real
  associate would annotate a redline.
- It's honest about its limits: anything outside the reference library is flagged as
  uncategorized rather than hallucinated.
- It's a natural bridge if you later want to explain "how this could become a real RAG
  system" (reference library → vector database of firm precedents → automatic
  retrieval) without claiming you've already built that infrastructure.

**Notes for reuse:** keep the reference library short and curated — retrieval quality
depends on having the right comparator, not the most comparators. Expand categories
incrementally as you use it on new contract types.
