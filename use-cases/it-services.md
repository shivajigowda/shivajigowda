# IT services: AI use cases I've solutioned

[← back to profile](../README.md)

<p align="center">
<a href="airlines.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-airlines-off-dark.svg"><img alt="Airlines" src="../assets/tab-airlines-off-light.svg" height="40"></picture></a>
<a href="bfsi-fintech.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-bfsi-fintech-off-dark.svg"><img alt="BFSI & Fintech" src="../assets/tab-bfsi-fintech-off-light.svg" height="40"></picture></a>
<a href="retail-d2c.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-retail-d2c-off-dark.svg"><img alt="Retail & D2C" src="../assets/tab-retail-d2c-off-light.svg" height="40"></picture></a>
<a href="automotive.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-automotive-off-dark.svg"><img alt="Automotive" src="../assets/tab-automotive-off-light.svg" height="40"></picture></a>
<a href="pharma.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-pharma-off-dark.svg"><img alt="Pharma" src="../assets/tab-pharma-off-light.svg" height="40"></picture></a>
<a href="it-services.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-it-services-on-dark.svg"><img alt="IT services" src="../assets/tab-it-services-on-light.svg" height="40"></picture></a>
<a href="marketing.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-marketing-off-dark.svg"><img alt="Marketing" src="../assets/tab-marketing-off-light.svg" height="40"></picture></a>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/uc-it-services-1-dark.svg">
  <img alt="IT services use case: Cloud managed-services support transformation. Problem: Tickets took 25–40 min of manual alert correlation and drafting. AI did: Auto-tracked incidents from observability alerts, triaged and classified, drafted replies and SOP steps. Solution did: Observability platform → auto incident tracking and AI triage; one-action workflow, P1/P2 hard block, human confirm gates. Business outcome: Under 5 min, 2x customers per team (targets). KPI: time. Architecture: Observability alerts · email · portal → Auto incident tracking → Correlation + dedupe → AI triage: classify P1–P4, draft → Humans confirm; P1/P2 human-only." src="../assets/uc-it-services-1-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/wf-it-services-1-dark.svg">
  <img alt="Solution workflow (hybrid) for Cloud managed-services support transformation: 1 trigger: Observability platform raises an alert, or a ticket arrives by email, portal or team chat → event; 2 system: Auto incident tracking: alerts are correlated, de-duplicated and opened as a tracked incident linked to affected tickets → incident; 3 workflow: Fires once on creation and calls the main agent → one AI action; 4 agent: AI triage: scans for P1/P2 emergency signals, classifies type, category, priority → structured output; 5 decision: P1/P2 or change request? yes → step 6 / no → step 7; 6 guardrail: No AI reply; route to on-call queue or approval board → human-only handling; 7 skill: Searches KB and runbooks; for alerts, graph lookup and on-demand cloud log and metric pulls → grounded context; 8 agent: Drafts the reply or customer notification and SOP checklist, or NO_RESPONSE → draft; 9 human: Reviews, personalises and approves send (100% on customer-impacting actions; supervised mode early on) → sent communication; 10 workflow: Awaiting-requester stage then auto-resolve and close after N days of silence; incident resolution closes linked tickets → closed records; 11 outcome: Alert-to-customer notice and human touch-time under 5 minutes (target) → more customers per team" src="../assets/wf-it-services-1-light.svg" width="100%">
</picture>

<details>
<summary>Workflow steps as text: Cloud managed-services support transformation</summary>

1. **Trigger** (loop step 2): Observability platform raises an alert, or a ticket arrives by email, portal or team chat → event
2. **System** (loop step 3): Auto incident tracking: alerts are correlated, de-duplicated and opened as a tracked incident linked to affected tickets → incident
3. **Workflow** (loop step 4): Fires once on creation and calls the main agent → one AI action
4. **Agent** (loop step 4): AI triage: scans for P1/P2 emergency signals, classifies type, category, priority → structured output
5. **Decision** (loop step 4): P1/P2 or change request? yes → step 6 / no → step 7
6. **Guardrail** (loop step 5): No AI reply; route to on-call queue or approval board → human-only handling
7. **Skill** (loop step 4): Searches KB and runbooks; for alerts, graph lookup and on-demand cloud log and metric pulls → grounded context
8. **Agent** (loop step 4): Drafts the reply or customer notification and SOP checklist, or NO_RESPONSE → draft
9. **Human** (loop step 5): Reviews, personalises and approves send (100% on customer-impacting actions; supervised mode early on) → sent communication
10. **Workflow** (loop step 4): Awaiting-requester stage then auto-resolve and close after N days of silence; incident resolution closes linked tickets → closed records
11. **Outcome** (loop step 7): Alert-to-customer notice and human touch-time under 5 minutes (target) → more customers per team

</details>

**Cloud managed-services support transformation** · Under 5 min, 2x customers per team (targets)

- Problem: Tickets took 25–40 min of manual alert correlation and drafting
- AI did: Auto-tracked incidents from observability alerts, triaged and classified, drafted replies and SOP steps
- Solution did: Observability platform → auto incident tracking and AI triage; one-action workflow, P1/P2 hard block, human confirm gates
- Architecture: Observability alerts · email · portal → Auto incident tracking → Correlation + dedupe → AI triage: classify P1–P4, draft → Humans confirm; P1/P2 human-only

<sub>Anonymized: industries and generic system types only. Outcomes are labelled target, achieved, proposal or pilot exactly as the source work states them.</sub>
