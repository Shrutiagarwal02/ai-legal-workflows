# Clause Precedent Library (Synthetic — for demo purposes only)

A small curated set of market-standard clause examples used to ground the flagger's
output in specific reference language, rather than the model's general knowledge alone.
This is the retrieval layer: instead of asking the model "is this clause standard?" from
memory, we hand it the actual comparison text and ask it to reason against it.

In a real deployment, this library would be built from your own firm's precedent bank
(anonymized/genericized) or a licensed clause database — never live client documents
without approval.

---

## INDEMNITY — Market-standard mutual indemnity (moderate risk allocation)

> "Each party shall indemnify, defend, and hold harmless the other party from and
> against any third-party claims, losses, and reasonable expenses (including legal
> fees) arising directly from the indemnifying party's breach of this Agreement, gross
> negligence, or willful misconduct, provided that the aggregate liability of either
> party under this indemnity shall not exceed [fees paid in the 12 months preceding the
> claim / a fixed cap], excluding claims arising from fraud, breach of confidentiality,
> or infringement of intellectual property rights."

**Key features:** mutual (not one-sided), capped, excludes consequential/indirect
losses, carve-outs limited to fraud/confidentiality/IP.

---

## LIABILITY CAP — Market-standard limitation of liability

> "Except in respect of liability arising from fraud, gross negligence, willful
> misconduct, or breach of confidentiality obligations, neither party's aggregate
> liability under this Agreement shall exceed [a fixed sum / 12 months' fees]. Neither
> party shall be liable for indirect, consequential, or special damages, including loss
> of profits or business opportunity."

**Key features:** defined cap, standard carve-outs, exclusion of consequential
damages.

---

## TERMINATION — Market-standard termination for convenience (founder/employment context)

> "Either party may terminate this Agreement for convenience upon [30/60/90] days'
> written notice. Termination for cause requires written notice specifying the breach
> and a [15/30]-day cure period, except in cases of fraud or gross misconduct, which
> permit immediate termination. Unvested equity shall be subject to the vesting
> schedule set out in Schedule [X], and no unvested equity shall be forfeited solely as
> a result of termination without cause absent an express contrary provision."

**Key features:** defined notice period, cure period for "for cause" termination,
protection against unilateral forfeiture of unvested equity.

---

## ASSIGNMENT — Market-standard assignment restriction

> "Neither party may assign this Agreement or any rights or obligations hereunder
> without the prior written consent of the other party, such consent not to be
> unreasonably withheld, except that either party may assign this Agreement without
> consent to an affiliate or in connection with a merger, acquisition, or sale of
> substantially all of its assets."

**Key features:** consent requirement (not unreasonably withheld), carve-out for
bona fide M&A/affiliate transfers only.

---

## GOVERNING LAW & DISPUTE RESOLUTION — Market-standard fixed forum clause

> "This Agreement shall be governed by and construed in accordance with the laws of
> [named jurisdiction, fixed at signing]. Any dispute arising out of or in connection
> with this Agreement shall be finally resolved by arbitration under the [named
> institutional rules, e.g., DIFC-LCIA / ADGM Arbitration Centre] rules, with the seat
> of arbitration in [named seat], in the English language."

**Key features:** governing law and seat both fixed at signing — never left "to be
agreed" or at one party's unilateral discretion.

---

## SHARE BUY-BACK — Market-standard departing-founder valuation mechanism

> "Upon a Founder's departure, the Company may repurchase that Founder's vested
> shares at Fair Market Value, as determined by an independent third-party valuer
> appointed jointly by the parties (or, failing agreement, appointed by [a named
> professional body]), whose determination shall be final and binding absent manifest
> error."

**Key features:** independent valuation, not set unilaterally by one party's board.
