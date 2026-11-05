# Airlines: AI use cases I've solutioned

[← back to profile](../README.md)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/tabs-airlines-dark.svg">
  <img alt="Industry tabs, Airlines selected" src="../assets/tabs-airlines-light.svg" width="100%">
</picture>

<a href="airlines.md"><img alt="Airlines" src="https://img.shields.io/badge/Airlines-6E22FE?style=flat-square"></a> <a href="bfsi-fintech.md"><img alt="BFSI & Fintech" src="https://img.shields.io/badge/BFSI%20%26%20Fintech-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="retail-d2c.md"><img alt="Retail & D2C" src="https://img.shields.io/badge/Retail%20%26%20D2C-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="automotive.md"><img alt="Automotive" src="https://img.shields.io/badge/Automotive-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="pharma.md"><img alt="Pharma" src="https://img.shields.io/badge/Pharma-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="it-services.md"><img alt="IT services" src="https://img.shields.io/badge/IT%20services-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="marketing.md"><img alt="Marketing" src="https://img.shields.io/badge/Marketing-F2ECFE?style=flat-square&labelColor=F2ECFE"></a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/uc-airlines-1-dark.svg">
  <img alt="Airlines use case: Payments desk transformation. Problem: Paid-but-unbooked cases took 15–30 min across three systems. AI did: Searched, reserved, enrolled, billed, retrieved booking, closed case. Solution did: Integrated three systems; human confirm gates; escalation matrix and audits. Business outcome: Under 5 min per case (target). Maturity M3 · L3; KPI: time. Architecture: CRM case → AI workspace chat → Payment gateway + reservation system → Human confirms → Payment link → booking ref → CRM auto-close." src="../assets/uc-airlines-1-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/wf-airlines-1-dark.svg">
  <img alt="Solution workflow (hybrid) for Payments desk transformation: 1 trigger: Desk agent enters the case number in the AI workspace → case fetched from the CRM; 2 system: Queries the payment gateway and reservation system for payment and existing booking → status shown; 3 decision: Booking already exists? yes → step 9 / no → step 3a: payment failed? yes → [HUMAN] escalate to team lead / no → step 4; 4 skill: Searches flights on route and date, shows options → option list; 5 human: Agent confirms the flight, consulting the passenger if needed → selection; 6 skill: Reserves seats and enrols each passenger; applies senior discount; asks for infant allocation → enrolled passengers; 7 human: Agent confirms contact details ('yes') and the booking summary ('confirm') → approved summary; 8 skill: Generates payment link and sends by email and SMS; agent calls the passenger → link sent; 9 system: Detects payment, retrieves booking reference, updates and closes the CRM case → closed case with audit trail; 10 guardrail: Payment taken but no booking, or an integration down → critical escalation to team lead and platform support in parallel; 11 outcome: Rebooked passenger and closed case in under 5 minutes (target) → less manual system switching" src="../assets/wf-airlines-1-light.svg" width="100%">
</picture>

<details>
<summary>Workflow steps as text: Payments desk transformation</summary>

1. **Trigger** (loop step 2): Desk agent enters the case number in the AI workspace → case fetched from the CRM
2. **System** (loop step 3): Queries the payment gateway and reservation system for payment and existing booking → status shown
3. **Decision** (loop step 4): Booking already exists? yes → step 9 / no → step 3a: payment failed? yes → [HUMAN] escalate to team lead / no → step 4
4. **Skill** (loop step 4): Searches flights on route and date, shows options → option list
5. **Human** (loop step 5): Agent confirms the flight, consulting the passenger if needed → selection
6. **Skill** (loop step 4): Reserves seats and enrols each passenger; applies senior discount; asks for infant allocation → enrolled passengers
7. **Human** (loop step 5): Agent confirms contact details ('yes') and the booking summary ('confirm') → approved summary
8. **Skill** (loop step 4): Generates payment link and sends by email and SMS; agent calls the passenger → link sent
9. **System** (loop step 3): Detects payment, retrieves booking reference, updates and closes the CRM case → closed case with audit trail
10. **Guardrail** (loop step 5): Payment taken but no booking, or an integration down → critical escalation to team lead and platform support in parallel
11. **Outcome** (loop step 7): Rebooked passenger and closed case in under 5 minutes (target) → less manual system switching

</details>

**Payments desk transformation** · M3 · L3 · Under 5 min per case (target)

- Problem: Paid-but-unbooked cases took 15–30 min across three systems
- AI did: Searched, reserved, enrolled, billed, retrieved booking, closed case
- Solution did: Integrated three systems; human confirm gates; escalation matrix and audits
- Architecture: CRM case → AI workspace chat → Payment gateway + reservation system → Human confirms → Payment link → booking ref → CRM auto-close

<sub>Anonymized: industries and generic system types only. Outcomes are labelled target, achieved, proposal or pilot exactly as the source work states them.</sub>
