# AML/KYC Client Risk Review Assistant
*(working name: AML/KYC Document Triage Assistant)*

**What it is:** A structured LLM workflow that reads corporate structure/ownership documents (synthetic, for demo) and extracts the Ultimate Beneficial Owner (UBO) chain, flagging red flags against FATF-style risk indicators — before a compliance officer does full manual due diligence.

**Why it matters:** UBO tracing through layered corporate structures is one of the most time-consuming parts of onboarding due diligence. This workflow doesn't make the compliance decision — it structures the information and flags what a human needs to look at first.

## Files

- `prompt-template.md` — the reusable prompt
- `sample-structure.md` — a synthetic multi-layer ownership structure with planted red flags
- `sample-output.md` — the extracted UBO chain + flags
- `cv-summary.md` — CV line, LinkedIn post, interview talking points
