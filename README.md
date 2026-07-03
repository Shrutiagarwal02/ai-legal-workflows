# AI-Assisted Legal Workflows

A set of AI-assisted legal workflows built alongside a contracts, compliance, and
litigation practice — designed to speed up first-pass review without displacing legal
judgment. Built and maintained by **Shruti Agarwal** (LL.M., Commercial & Corporate
Law, Queen Mary University of London).

**Live showcase:** [ai-legal-workflows.streamlit.app](https://ai-legal-workflows.streamlit.app/)

## What's here

| Project | What it does | Validation |
|---|---|---|
| **1. Contract Risk Review & Negotiation Playbook Generator** | Flags contract clauses that deviate from market-standard positions (indemnity, liability, termination, assignment, governing law, buy-back), grounded against a curated precedent library; extends into a negotiation playbook (opening ask, fallbacks, walk-away triggers). | Validated against the actual, current [Y Combinator Post-Money SAFE](https://www.ycombinator.com/documents) template. |
| **2. AML/KYC Client Risk Review Assistant** | Maps UBO ownership chains and flags FATF-aligned red flags for first-pass CDD/EDD screening. | Synthetic data only, by design — real onboarding files require firm-approved data handling, not a general-purpose AI tool. |
| **3. ESG Readiness & Governance Gap Analyzer** | Benchmarks a company's ESG disclosures against a 7-point checklist (governance, climate, social, materiality, targets, assurance, framework alignment). | Validated against [Abu Dhabi Islamic Bank's public ESG page](https://www.adib.ae/en/esg-and-sustainability). |
| **4. Judgment Summarizer & Argument Note Builder** | Converts a judgment into a structured case brief (facts, issues, holding, ratio vs. obiter), then organizes multiple briefs into an argument note for a hearing. | Validated against a real Calcutta High Court judgment ([*Jindal (India) Ltd v. State of West Bengal*](https://indiankanoon.org/doc/139122637/), July 2025). |

See [`05-Phase-2-Roadmap.md`](05-Phase-2-Roadmap.md) for four further tools that are
scoped but deliberately not yet built, with explicit reasoning for why two of them are
gated on data-licensing and legal-judgment-displacement risks.

## Important: what this is and isn't

- **These are prompting workflows on general-purpose LLMs (Claude/ChatGPT) — not
  fine-tuned models.** Every claim in this repo is scoped to match that.
- **Three of the four projects are validated against real public documents**; the
  AML/KYC project uses synthetic data only, by design, for confidentiality reasons.
- **These are triage and drafting aids, not a substitute for legal judgment.** Every
  project's README states its scope boundary explicitly.
- Full methodology notes are in [`00-How-To-Talk-About-This.md`](00-How-To-Talk-About-This.md).

## Running the showcase locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

This launches a **static showcase app** — it displays the prompts, sample inputs, and
already-generated outputs below. It does not call any LLM API live; there is no cost
exposure and no dependency on an API key to browse it.

## Repository structure

```
01-Contract-Clause-Risk-Flagger/    # Project 1: prompts, samples, real YC SAFE example
02-AML-KYC-Triage-Assistant/        # Project 2: prompts, synthetic samples
03-ESG-Regulatory-Gap-Tracker/      # Project 3: prompts, real ADIB example
04-Case-Summary-Tool/               # Project 4: prompts, real judgment example
05-Phase-2-Roadmap.md               # Scoped, unbuilt future work
00-How-To-Talk-About-This.md        # Methodology & framing notes
app.py                              # Streamlit showcase app
```

## Contact

shrutiagarwal.new@gmail.com | [LinkedIn](https://www.linkedin.com/)
