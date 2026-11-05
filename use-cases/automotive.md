# Automotive: AI use cases I've solutioned

[← back to profile](../README.md)

<p align="center">
<a href="airlines.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-airlines-off-dark.svg?v=29b7f121"><img alt="Airlines" src="../assets/tab-airlines-off-light.svg?v=a5de0822" height="40"></picture></a>
<a href="bfsi-fintech.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-bfsi-fintech-off-dark.svg?v=8ee70b76"><img alt="BFSI & Fintech" src="../assets/tab-bfsi-fintech-off-light.svg?v=26bd3e6a" height="40"></picture></a>
<a href="retail-d2c.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-retail-d2c-off-dark.svg?v=de14334d"><img alt="Retail & D2C" src="../assets/tab-retail-d2c-off-light.svg?v=1cb9dfde" height="40"></picture></a>
<a href="automotive.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-automotive-on-dark.svg?v=4f8f4d96"><img alt="Automotive" src="../assets/tab-automotive-on-light.svg?v=6f309518" height="40"></picture></a>
<a href="pharma.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-pharma-off-dark.svg?v=a1e6ad0c"><img alt="Pharma" src="../assets/tab-pharma-off-light.svg?v=094b707d" height="40"></picture></a>
<a href="it-services.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-it-services-off-dark.svg?v=feae9385"><img alt="IT services" src="../assets/tab-it-services-off-light.svg?v=66745c5f" height="40"></picture></a>
<a href="marketing.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-marketing-off-dark.svg?v=35e037b3"><img alt="Marketing" src="../assets/tab-marketing-off-light.svg?v=f13446de" height="40"></picture></a>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/uc-automotive-1-dark.svg?v=b12449da">
  <img alt="Automotive use case: Dealer assist & navigation. Problem: Dealers hit repeat system errors with scripted fixes. AI did: Ran the right procedure from a pre-set starting turn. Solution did: Button tree, 35 handoff contracts, no-re-ask context payloads. Business outcome: Faster dealer self-service, no re-asking. KPI: time. Architecture: Dealer-system chat widget → Greeting + 5 buttons → Handoff context payload → Agent runs procedure → Outcome + rating." src="../assets/uc-automotive-1-light.svg?v=dbf69da1" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/wf-automotive-1-dark.svg?v=3566f0f7">
  <img alt="Solution workflow (conversational) for Dealer assist & navigation: 1 trigger: Dealer opens the support chat in the DMS → greeting and main menu; 2 user: Taps one of 5 entry buttons → use case chosen; 3 workflow: Shows 1-2 sub-menus of error, reason or option buttons (max 3 taps) → scenario identified; 4 decision: Issue listed? yes → step 5 / no → step 5 with the Others path (open describe-your-issue mode); 5 workflow: Talk-to-agent node passes context: use case, scenario, path, start turn, already-answered list → agent invoked; 6 guardrail: Dealer and branch IDs come from the DMS session and are never asked; no re-asking of menu answers → clean first turn; 7 agent: Sends the first scripted instruction or data request, then runs the procedure sheet from the set turn → resolution steps or collected details; 8 decision: Resolved by the instructions? yes → step 9 / no → agent continues the sheet or hands the details to support; 9 agent: Closes with outcome, reason and a 1-5 star rating → closing record; 10 outcome: Dealer reaches the right procedure in at most 3 taps without repeated questions → faster self-service" src="../assets/wf-automotive-1-light.svg?v=42d5da62" width="100%">
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

**Dealer assist & navigation** · Faster dealer self-service, no re-asking

- Problem: Dealers hit repeat system errors with scripted fixes
- AI did: Ran the right procedure from a pre-set starting turn
- Solution did: Button tree, 35 handoff contracts, no-re-ask context payloads
- Architecture: Dealer-system chat widget → Greeting + 5 buttons → Handoff context payload → Agent runs procedure → Outcome + rating

<sub>Anonymized: industries and generic system types only.</sub>
