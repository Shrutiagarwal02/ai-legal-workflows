# Prompt Template — ESG Regulatory-Gap Tracker

```
You are assisting a regulatory/ESG advisor with a first-pass gap analysis. Compare the
company's ESG disclosure below against the following requirement checklist (adapt to
the specific regime you're advising under — this is framed generically across
ADGM/UK-style ESG and sustainability reporting expectations):

CHECKLIST:
1. GOVERNANCE — Board oversight of ESG strategy; named responsible officer/committee.
2. CLIMATE/ENVIRONMENTAL — GHG emissions disclosure (Scope 1/2, ideally Scope 3);
   climate risk assessment; environmental policy.
3. SOCIAL — Workforce diversity/inclusion metrics; health & safety policy; supply chain
   labor standards/due diligence.
4. MATERIALITY ASSESSMENT — Evidence of a formal materiality assessment identifying
   which ESG issues are relevant to the business.
5. TARGETS & KPIs — Quantified, time-bound ESG targets (not just aspirational language).
6. THIRD-PARTY ASSURANCE — Any external verification/assurance of disclosed data.
7. REPORTING FRAMEWORK ALIGNMENT — Explicit alignment with a recognized framework
   (e.g., GRI, TCFD/ISSB, SASB) or regulator-specific template.

For each checklist item, output:
- **Item:** [checklist category]
- **Status:** Present / Partial / Missing
- **Evidence found:** [quote or summary from the disclosure, or "none"]
- **Gap:** [what's missing relative to the requirement]
- **Priority to close:** High / Medium / Low

End with an overall readiness summary and the top 3 priority actions.

COMPANY ESG DISCLOSURE:
[DISCLOSURE TEXT]
```

**Notes for reuse:** Swap the checklist for the specific regime you're advising under
(e.g., substitute exact ADGM Sustainable Finance Regulations requirements, or UK
Streamlined Energy and Carbon Reporting (SECR) / TCFD requirements) — this generic
version is for demonstration purposes.
