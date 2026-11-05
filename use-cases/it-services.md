# IT services: AI use cases I've solutioned

[← back to profile](../README.md)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/tabs-it-services-dark.svg">
  <img alt="Industry tabs, IT services selected" src="../assets/tabs-it-services-light.svg" width="100%">
</picture>

<a href="airlines.md"><img alt="Airlines" src="https://img.shields.io/badge/Airlines-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="bfsi-fintech.md"><img alt="BFSI & Fintech" src="https://img.shields.io/badge/BFSI%20%26%20Fintech-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="retail-d2c.md"><img alt="Retail & D2C" src="https://img.shields.io/badge/Retail%20%26%20D2C-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="automotive.md"><img alt="Automotive" src="https://img.shields.io/badge/Automotive-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="pharma.md"><img alt="Pharma" src="https://img.shields.io/badge/Pharma-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="it-services.md"><img alt="IT services" src="https://img.shields.io/badge/IT%20services-6E22FE?style=flat-square"></a> <a href="marketing.md"><img alt="Marketing" src="https://img.shields.io/badge/Marketing-F2ECFE?style=flat-square&labelColor=F2ECFE"></a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/uc-it-services-1-dark.svg">
  <img alt="IT services use case: Cloud managed-services support transformation. Problem: Tickets took 25–40 min of manual alert correlation and drafting. AI did: Classified, correlated alerts, drafted replies and SOP steps. Solution did: One-action workflow, alert pipeline, P1/P2 hard block, human confirm gates. Business outcome: Under 5 min, 2x customers per team (targets). Maturity M3–M4 · L4; KPI: time. Architecture: Email · portal · cloud alarms → Correlation + dedupe → Incident + knowledge graph → Agent: classify P1–P4, draft → Humans confirm; P1/P2 human-only." src="../assets/uc-it-services-1-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/wf-it-services-1-dark.svg">
  <img alt="Solution workflow (hybrid) for Cloud managed-services support transformation: 1 trigger: Ticket arrives by email, portal, team chat or legacy-ticket sync, or a correlated alert incident arrives by webhook → ticket or incident created; 2 workflow: Fires once on creation and calls the main agent → one AI action; 3 agent: Scans for P1/P2 emergency signals, classifies type, category, priority → structured output; 4 decision: P1/P2 or change request? yes → step 5 / no → step 6; 5 guardrail: No AI reply; route to on-call queue or approval board → human-only handling; 6 skill: Searches KB and runbooks; for alerts, graph lookup and on-demand cloud log and metric pulls → grounded context; 7 agent: Drafts the reply or customer notification and SOP checklist, or NO_RESPONSE → draft; 8 human: Reviews, personalises and approves send (100% on customer-impacting actions; supervised mode early on) → sent communication; 9 workflow: Awaiting-requester stage then auto-resolve and close after N days of silence; incident resolution closes linked tickets → closed records; 10 outcome: Alert-to-customer notice and human touch-time under 5 minutes (target) → more customers per team" src="../assets/wf-it-services-1-light.svg" width="100%">
</picture>

<details>
<summary>Workflow steps as text: Cloud managed-services support transformation</summary>

1. **Trigger** (loop step 2): Ticket arrives by email, portal, team chat or legacy-ticket sync, or a correlated alert incident arrives by webhook → ticket or incident created
2. **Workflow** (loop step 4): Fires once on creation and calls the main agent → one AI action
3. **Agent** (loop step 4): Scans for P1/P2 emergency signals, classifies type, category, priority → structured output
4. **Decision** (loop step 4): P1/P2 or change request? yes → step 5 / no → step 6
5. **Guardrail** (loop step 5): No AI reply; route to on-call queue or approval board → human-only handling
6. **Skill** (loop step 4): Searches KB and runbooks; for alerts, graph lookup and on-demand cloud log and metric pulls → grounded context
7. **Agent** (loop step 4): Drafts the reply or customer notification and SOP checklist, or NO_RESPONSE → draft
8. **Human** (loop step 5): Reviews, personalises and approves send (100% on customer-impacting actions; supervised mode early on) → sent communication
9. **Workflow** (loop step 4): Awaiting-requester stage then auto-resolve and close after N days of silence; incident resolution closes linked tickets → closed records
10. **Outcome** (loop step 7): Alert-to-customer notice and human touch-time under 5 minutes (target) → more customers per team

</details>

**Cloud managed-services support transformation** · M3–M4 · L4 · Under 5 min, 2x customers per team (targets)

- Problem: Tickets took 25–40 min of manual alert correlation and drafting
- AI did: Classified, correlated alerts, drafted replies and SOP steps
- Solution did: One-action workflow, alert pipeline, P1/P2 hard block, human confirm gates
- Architecture: Email · portal · cloud alarms → Correlation + dedupe → Incident + knowledge graph → Agent: classify P1–P4, draft → Humans confirm; P1/P2 human-only

<sub>Anonymized: industries and generic system types only. Outcomes are labelled target, achieved, proposal or pilot exactly as the source work states them.</sub>
