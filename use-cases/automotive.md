# Automotive: AI use cases I've solutioned

[← back to profile](../README.md)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/tabs-automotive-dark.svg">
  <img alt="Industry tabs, Automotive selected" src="../assets/tabs-automotive-light.svg" width="100%">
</picture>

<a href="airlines.md"><img alt="Airlines" src="https://img.shields.io/badge/Airlines-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="bfsi-fintech.md"><img alt="BFSI & Fintech" src="https://img.shields.io/badge/BFSI%20%26%20Fintech-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="retail-d2c.md"><img alt="Retail & D2C" src="https://img.shields.io/badge/Retail%20%26%20D2C-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="automotive.md"><img alt="Automotive" src="https://img.shields.io/badge/Automotive-6E22FE?style=flat-square"></a> <a href="pharma.md"><img alt="Pharma" src="https://img.shields.io/badge/Pharma-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="it-services.md"><img alt="IT services" src="https://img.shields.io/badge/IT%20services-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="marketing.md"><img alt="Marketing" src="https://img.shields.io/badge/Marketing-F2ECFE?style=flat-square&labelColor=F2ECFE"></a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/uc-automotive-1-dark.svg">
  <img alt="Automotive use case: Dealer assist & navigation. Problem: Dealers hit repeat system errors with scripted fixes. AI did: Ran the right procedure from a pre-set starting turn. Solution did: Button tree, 35 handoff contracts, no-re-ask context payloads. Business outcome: Faster dealer self-service (no KPI stated). Maturity M2 · L2 (inferred); KPI: time. Architecture: Dealer-system chat widget → Greeting + 5 buttons → Handoff context payload → Agent runs procedure → Outcome + rating." src="../assets/uc-automotive-1-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/wf-automotive-1-dark.svg">
  <img alt="Solution workflow (conversational) for Dealer assist & navigation: 1 trigger: Dealer opens the support chat in the DMS → greeting and main menu; 2 user: Taps one of 5 entry buttons → use case chosen; 3 workflow: Shows 1-2 sub-menus of error, reason or option buttons (max 3 taps) → scenario identified; 4 decision: Issue listed? yes → step 5 / no → step 5 with the Others path (open describe-your-issue mode); 5 workflow: Talk-to-agent node passes context: use case, scenario, path, start turn, already-answered list → agent invoked; 6 guardrail: Dealer and branch IDs come from the DMS session and are never asked; no re-asking of menu answers → clean first turn; 7 agent: Sends the first scripted instruction or data request, then runs the procedure sheet from the set turn → resolution steps or collected details; 8 decision: Resolved by the instructions? yes → step 9 / no → agent continues the sheet or hands the details to support; 9 agent: Closes with outcome, reason and a 1-5 star rating → closing record; 10 outcome: Dealer reaches the right procedure in at most 3 taps without repeated questions → faster self-service" src="../assets/wf-automotive-1-light.svg" width="100%">
</picture>

<details>
<summary>Workflow steps as text: Dealer assist & navigation</summary>

1. **Trigger** (loop step 2): Dealer opens the support chat in the DMS → greeting and main menu
2. **User** (loop step 2): Taps one of 5 entry buttons → use case chosen
3. **Workflow** (loop step 4): Shows 1-2 sub-menus of error, reason or option buttons (max 3 taps) → scenario identified
4. **Decision** (loop step 4): Issue listed? yes → step 5 / no → step 5 with the Others path (open describe-your-issue mode)
5. **Workflow** (loop step 4): Talk-to-agent node passes context: use case, scenario, path, start turn, already-answered list → agent invoked
6. **Guardrail** (loop step 5): Dealer and branch IDs come from the DMS session and are never asked; no re-asking of menu answers → clean first turn
7. **Agent** (loop step 4): Sends the first scripted instruction or data request, then runs the procedure sheet from the set turn → resolution steps or collected details
8. **Decision** (loop step 4): Resolved by the instructions? yes → step 9 / no → agent continues the sheet or hands the details to support
9. **Agent** (loop step 4): Closes with outcome, reason and a 1-5 star rating → closing record
10. **Outcome** (loop step 7): Dealer reaches the right procedure in at most 3 taps without repeated questions → faster self-service

</details>

**Dealer assist & navigation** · M2 · L2 (inferred) · Faster dealer self-service (no KPI stated)

- Problem: Dealers hit repeat system errors with scripted fixes
- AI did: Ran the right procedure from a pre-set starting turn
- Solution did: Button tree, 35 handoff contracts, no-re-ask context payloads
- Architecture: Dealer-system chat widget → Greeting + 5 buttons → Handoff context payload → Agent runs procedure → Outcome + rating

<sub>Anonymized: industries and generic system types only. Outcomes are labelled target, achieved, proposal or pilot exactly as the source work states them.</sub>
