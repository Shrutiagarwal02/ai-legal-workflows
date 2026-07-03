# Real Example — Flagger Run Against the Actual Y Combinator Post-Money SAFE

**Source:** Y Combinator official Post-Money SAFE (Valuation Cap only), downloaded
directly from [ycombinator.com/documents](https://www.ycombinator.com/documents) — a
genuine, current, publicly published financing template used industry-wide, not a
synthetic example.

**Important context before the analysis:** this is a blank template with bracketed
placeholders (e.g., `[Governing Law Jurisdiction]`, `[Purchase Amount]`), not an
executed contract. Some "gaps" below are template placeholders to be filled at
signing, not drafting defects — flagged and labeled as such rather than treated the
same as a real red flag in an executed agreement. This distinction matters and is the
kind of judgment call an AI tool won't make on its own without being told to.

---

## Flagged Output (v1 checklist method, adapted for a financing instrument rather than a shareholders' agreement)

**Clause:** Section 5(f) — Governing Law
**What it says:** "Governed by the laws of the State of [Governing Law Jurisdiction]."
**Why it's flagged:** Not a drafting defect — this is an intentional blank in the official template, to be completed per the actual company's state of incorporation (typically Delaware for US SAFEs). No action needed beyond filling it in at execution.
**Severity:** N/A (template placeholder, not a risk)

---

**Clause:** Section 5(d) — Assignment
**What it says:** Neither party may assign without the other's prior written consent, except the Investor may assign to its estate/heirs on death/disability, or to an affiliate/controlled entity.
**Why it's flagged:** This is market-standard and mutual — consistent with the reference assignment clause in `precedent-library.md` (consent required, carve-out for affiliate transfers). No issue.
**Severity:** Low / none — flagged only to confirm the check was performed, not because of a defect.

---

**Clause:** Section 1(d) — Liquidation Priority
**What it says:** SAFE ranks junior to debt, on par with other SAFEs/Preferred Stock, senior to Common Stock.
**Why it's flagged:** This is exactly the standard, expected priority stack for a SAFE instrument — no deviation. Included here to show the tool doesn't manufacture a finding where none exists.
**Severity:** None.

---

**Clause:** Section 3 — Company Representations / Section 4 — Investor Representations
**What it says:** Fairly standard mutual representations (corporate authority, no violations, accredited investor status).
**Why it's flagged:** Standard boilerplate; the one point worth a founder's attention on the Company side is 3(b)'s "subject to section 3(d)" carve-out for required consents — worth confirming those consents are actually in hand before signing, not a drafting defect.
**Severity:** Low (a diligence checklist item, not a redline).

---

## Overall Risk Summary

Unlike the synthetic co-founder agreement example (which had deliberately planted,
one-sided terms), this real YC SAFE is — as expected for a widely-used, heavily
vetted industry-standard instrument — balanced and free of the kind of drafting
defects the flagger is designed to catch. The main output here is confirmation of
market-standard status plus a small number of execution-stage diligence items
(confirm jurisdiction, confirm required consents), not redlines.

## Why this example matters more than the synthetic one

A tool that only ever finds problems isn't trustworthy — it suggests the model is
manufacturing findings to seem useful. Running it against a genuinely clean, standard
document and getting an honest "this is fine, here's why" result is actually the
stronger demonstration of judgment: it shows the workflow can correctly distinguish a
well-drafted market-standard instrument from a one-sided one, rather than flagging
everything indiscriminately.
