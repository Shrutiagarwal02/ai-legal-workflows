# Prompt Template — AML/KYC UBO Triage Assistant

```
You are assisting a compliance officer with first-pass triage of a client onboarding
file, under an AML/KYC/CDD framework (e.g., ADGM/FATF-aligned). You are not making the
final risk decision — you are structuring the information and flagging what needs
closer manual review.

From the corporate structure description below:

1. MAP THE OWNERSHIP CHAIN — list each entity/individual in the chain from the applicant
   entity up to the ultimate beneficial owner(s) (natural persons with ≥25% ownership or
   control, or those exercising control by other means).
2. IDENTIFY UBOs — name each natural person who qualifies as a UBO and their effective
   ownership/control percentage.
3. FLAG RED FLAGS using FATF-style indicators, including:
   - Layered structures across multiple jurisdictions with no clear commercial rationale
   - Use of nominee shareholders/directors
   - Presence of shell companies or entities in high-risk/secrecy jurisdictions
   - Politically Exposed Persons (PEPs) in the chain
   - Ownership percentages that sum to <100% or are otherwise inconsistent
   - Bearer shares or other non-transparent instruments
4. OUTPUT FORMAT:
   - **UBO chain:** [structured list, entity → entity → individual, with % at each link]
   - **Identified UBO(s):** [name, effective %, basis — ownership or control]
   - **Red flags:** [list each, with severity High/Medium/Low and why]
   - **Recommended next step:** [e.g., enhanced due diligence, source-of-wealth check,
     sanctions/PEP screening]

CORPORATE STRUCTURE:
[STRUCTURE DESCRIPTION]
```

**Notes for reuse:**
- Never input real client data into a general-purpose LLM tool without firm approval,
  a compliant enterprise agreement, and data-handling sign-off — this is a triage
  methodology demo using synthetic data only.
- This does not replace sanctions/PEP screening against actual watchlists, which
  requires a licensed screening tool, not an LLM.
