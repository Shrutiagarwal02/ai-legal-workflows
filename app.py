"""
AI-Assisted Legal Workflows — Portfolio Showcase (Shruti Agarwal)

This is a STATIC showcase, not a live tool: it displays pre-run prompts, sample
inputs, and real outputs already produced and verified (see each project's README
for validation notes). It does not call any LLM API and accepts no user input beyond
navigation, by design — no cost exposure, no reliability risk, and no ambiguity about
what's "live" vs. demonstrated.
"""

import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Shruti Agarwal — AI-Assisted Legal Workflows",
    page_icon="\U0001F4C4",
    layout="wide",
)

ROOT = Path(__file__).parent

PROJECTS = [
    {
        "key": "01-Contract-Clause-Risk-Flagger",
        "title": "1. Contract Risk Review & Negotiation Playbook Generator",
        "files": [
            ("Overview", "README.md"),
            ("Prompt (v1)", "prompt-template.md"),
            ("Precedent Library", "precedent-library.md"),
            ("Prompt (v2, grounded)", "prompt-template-v2-grounded.md"),
            ("Sample Contract", "sample-contract.md"),
            ("Output (v1)", "sample-output.md"),
            ("Output (v2, grounded)", "sample-output-v2.md"),
            ("Real Example — YC SAFE", "real-example-yc-safe.md"),
            ("Playbook Extension", "playbook-extension.md"),
            ("CV Summary", "cv-summary.md"),
        ],
    },
    {
        "key": "02-AML-KYC-Triage-Assistant",
        "title": "2. AML/KYC Client Risk Review Assistant",
        "files": [
            ("Overview", "README.md"),
            ("Prompt", "prompt-template.md"),
            ("Sample Structure", "sample-structure.md"),
            ("Output", "sample-output.md"),
            ("CV Summary", "cv-summary.md"),
        ],
    },
    {
        "key": "03-ESG-Regulatory-Gap-Tracker",
        "title": "3. ESG Readiness & Governance Gap Analyzer",
        "files": [
            ("Overview", "README.md"),
            ("Prompt", "prompt-template.md"),
            ("Sample Disclosure", "sample-disclosure.md"),
            ("Output", "sample-output.md"),
            ("Real Example — ADIB", "real-example-adib.md"),
            ("CV Summary", "cv-summary.md"),
        ],
    },
    {
        "key": "04-Case-Summary-Tool",
        "title": "4. Judgment Summarizer & Argument Note Builder",
        "files": [
            ("Overview", "README.md"),
            ("Prompt", "prompt-template.md"),
            ("Sample Judgment", "sample-judgment.md"),
            ("Output", "sample-output.md"),
            ("Real Example — Calcutta HC Judgment", "real-example-jindal-v-wb.md"),
            ("Argument Note Extension", "argument-note-extension.md"),
            ("CV Summary", "cv-summary.md"),
        ],
    },
]


def load(rel_path: str) -> str:
    p = ROOT / rel_path
    if not p.exists():
        return f"*(file not found: {rel_path})*"
    return p.read_text(encoding="utf-8")


st.title("AI-Assisted Legal Workflows")
st.caption(
    "Shruti Agarwal — Contracts, Compliance & Litigation, with AI-assisted "
    "first-pass review tools built alongside practice work."
)

st.info(
    "**This is a static showcase, not a live demo.** Every prompt, sample, and "
    "output below was actually run and is displayed as-is — nothing here calls an "
    "AI model live. Full methodology note at the bottom of this page.",
    icon="ℹ️",
)

nav = st.sidebar.radio(
    "Navigate",
    ["About"] + [p["title"] for p in PROJECTS] + ["Phase 2 Roadmap", "Methodology"],
)

if nav == "About":
    st.markdown(load("00-How-To-Talk-About-This.md"))

elif nav == "Phase 2 Roadmap":
    st.markdown(load("05-Phase-2-Roadmap.md"))

elif nav == "Methodology":
    st.markdown(
        """
## Methodology Note

These are **prompting workflows** built on general-purpose LLMs (Claude/ChatGPT) —
**not fine-tuned models**. Three of the four projects are validated against real
public documents:

- The current Y Combinator Post-Money SAFE template (contract review)
- A real, current Calcutta High Court judgment (case briefing)
- Abu Dhabi Islamic Bank's public ESG overview page (ESG gap analysis)

The AML/KYC example uses clearly-labeled **synthetic data by design** — real
onboarding files require firm-approved data handling, not a general-purpose AI tool.

Two further tools are scoped but deliberately **not built** (see Phase 2 Roadmap),
pending explicit guardrails around unlicensed sanctions-screening data and the line
between research support and legal-judgment displacement.

Full prompts, sample inputs, and outputs for every project are available in this
repository and browsable in this app.
"""
    )

else:
    project = next(p for p in PROJECTS if p["title"] == nav)
    st.header(project["title"])
    tabs = st.tabs([label for label, _ in project["files"]])
    for tab, (label, filename) in zip(tabs, project["files"]):
        with tab:
            st.markdown(load(f"{project['key']}/{filename}"))

st.sidebar.markdown("---")
st.sidebar.markdown(
    "[LinkedIn](https://www.linkedin.com/) &nbsp;|&nbsp; "
    "shrutiagarwal.new@gmail.com"
)
