# Pharma: AI use cases I've solutioned

[← back to profile](../README.md)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/tabs-pharma-dark.svg">
  <img alt="Industry tabs, Pharma selected" src="../assets/tabs-pharma-light.svg" width="100%">
</picture>

<a href="airlines.md"><img alt="Airlines" src="https://img.shields.io/badge/Airlines-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="bfsi-fintech.md"><img alt="BFSI & Fintech" src="https://img.shields.io/badge/BFSI%20%26%20Fintech-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="retail-d2c.md"><img alt="Retail & D2C" src="https://img.shields.io/badge/Retail%20%26%20D2C-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="automotive.md"><img alt="Automotive" src="https://img.shields.io/badge/Automotive-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="pharma.md"><img alt="Pharma" src="https://img.shields.io/badge/Pharma-6E22FE?style=flat-square"></a> <a href="it-services.md"><img alt="IT services" src="https://img.shields.io/badge/IT%20services-F2ECFE?style=flat-square&labelColor=F2ECFE"></a> <a href="marketing.md"><img alt="Marketing" src="https://img.shields.io/badge/Marketing-F2ECFE?style=flat-square&labelColor=F2ECFE"></a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/uc-pharma-1-dark.svg">
  <img alt="Pharma use case: Production planning & plant / machine optimization. Problem: 16–17 planners took 10 days on monthly batch and machine plans in spreadsheets. AI did: Applied batch rules, checked readiness and equipment qualification, grouped batches, drafted machine-level plan. Solution did: Linked custom objects, shadow run, zero-violation guardrail, accuracy and ROI measurement. Business outcome: Plan in about 1 hour, 80%+ effort cut, fewer batches and changeovers (targets). Maturity M2 · L2; KPI: time. Architecture: ERP + quality exports → 11 linked custom objects → Planning agent: readiness + batch skills → Plan pack → Planner + QA approve." src="../assets/uc-pharma-1-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/wf-pharma-1-dark.svg">
  <img alt="Solution workflow (hybrid) for Production planning & plant / machine optimization: 1 trigger: Planner asks in chat, or the monthly/weekly schedule fires → planning request; 2 system: Exports from ERP, validated-batch-size system, quality-event system and validation planner load as-is into linked objects → reconciled data; 3 skill: Readiness skill checks master documents, MES recipe, open quality items, equipment requalification and materials per line → Ready / At risk / Blocked with blocker and owner; 4 skill: Batch-and-machine skill applies R1-R3 to demand and rounds to whole batches → batch sizes; 5 guardrail: Only equipment validated for the batch size and in date on requalification is used; others flagged with reason → compliant assignment; 6 skill: Groups batches sharing a blend to reduce non-serial changeovers → sequence and changeover saving; 7 decision: Any line blocked or equipment lapsed? yes → flag with source record for the owner / no → include in draft plan; 8 agent: Produces the machine-level draft plan with rationale per batch → plan pack; 9 human: Planner and quality SME review and approve; no write-back to source systems → approved plan; 10 outcome: Draft in about one hour and plan ready earlier, with zero violations (targets) → planner capacity released" src="../assets/wf-pharma-1-light.svg" width="100%">
</picture>

<details>
<summary>Workflow steps as text: Production planning & plant / machine optimization</summary>

1. **Trigger** (loop step 2): Planner asks in chat, or the monthly/weekly schedule fires → planning request
2. **System** (loop step 3): Exports from ERP, validated-batch-size system, quality-event system and validation planner load as-is into linked objects → reconciled data
3. **Skill** (loop step 4): Readiness skill checks master documents, MES recipe, open quality items, equipment requalification and materials per line → Ready / At risk / Blocked with blocker and owner
4. **Skill** (loop step 4): Batch-and-machine skill applies R1-R3 to demand and rounds to whole batches → batch sizes
5. **Guardrail** (loop step 5): Only equipment validated for the batch size and in date on requalification is used; others flagged with reason → compliant assignment
6. **Skill** (loop step 4): Groups batches sharing a blend to reduce non-serial changeovers → sequence and changeover saving
7. **Decision** (loop step 4): Any line blocked or equipment lapsed? yes → flag with source record for the owner / no → include in draft plan
8. **Agent** (loop step 4): Produces the machine-level draft plan with rationale per batch → plan pack
9. **Human** (loop step 5): Planner and quality SME review and approve; no write-back to source systems → approved plan
10. **Outcome** (loop step 7): Draft in about one hour and plan ready earlier, with zero violations (targets) → planner capacity released

</details>

**Production planning & plant / machine optimization** · M2 · L2 · Plan in about 1 hour, 80%+ effort cut, fewer batches and changeovers (targets)

- Problem: 16–17 planners took 10 days on monthly batch and machine plans in spreadsheets
- AI did: Applied batch rules, checked readiness and equipment qualification, grouped batches, drafted machine-level plan
- Solution did: Linked custom objects, shadow run, zero-violation guardrail, accuracy and ROI measurement
- Architecture: ERP + quality exports → 11 linked custom objects → Planning agent: readiness + batch skills → Plan pack → Planner + QA approve

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/uc-pharma-2-dark.svg">
  <img alt="Pharma use case: Conversational analytics (sales & market data). Problem: Business users queue behind central analysts for sales and market answers. AI did: Answered multi-domain questions in natural language. Solution did: Semantic layer, annotations, persona access control, synthetic data, cost logging. Business outcome: Self-serve answers, 99%+ consistency, transparent cost (targets). Maturity M1–M2 · L2; KPI: time. Architecture: Sample data → Synthetic generator → Semantic layer + annotations → Analytics assistant → Persona-scoped answers + cost log." src="../assets/uc-pharma-2-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/wf-pharma-2-dark.svg">
  <img alt="Solution workflow (conversational) for Conversational analytics (sales & market data): 1 trigger: Business user asks a question in natural language → request with persona; 2 guardrail: Persona access control and region/brand scope applied before any query → scoped request; 3 agent: Reads guidance, synonym map and field annotations; resolves metric and entities → query plan; 4 decision: Native text-to-SQL can see the custom fields? yes → step 5 / no → step 6; 5 skill: Generates and runs SQL over annotated objects → result set; 6 skill: Calls the domain query skill or cross-domain join skill → result set; 7 agent: Answers with table, period and scope using business labels, refusing schema enumeration and out-of-scope data → answer; 8 system: Logs tokens, cost and response time per query → cost and latency record; 9 human: QA reviewers score the harness run against ground truths computed outside the platform → pass rate; 10 outcome: Self-serve answers with consistency to certified reports and transparent cost (targets) → fewer analyst tickets" src="../assets/wf-pharma-2-light.svg" width="100%">
</picture>

<details>
<summary>Workflow steps as text: Conversational analytics (sales & market data)</summary>

1. **Trigger** (loop step 2): Business user asks a question in natural language → request with persona
2. **Guardrail** (loop step 5): Persona access control and region/brand scope applied before any query → scoped request
3. **Agent** (loop step 4): Reads guidance, synonym map and field annotations; resolves metric and entities → query plan
4. **Decision** (loop step 4): Native text-to-SQL can see the custom fields? yes → step 5 / no → step 6
5. **Skill** (loop step 4): Generates and runs SQL over annotated objects → result set
6. **Skill** (loop step 4): Calls the domain query skill or cross-domain join skill → result set
7. **Agent** (loop step 4): Answers with table, period and scope using business labels, refusing schema enumeration and out-of-scope data → answer
8. **System** (loop step 3): Logs tokens, cost and response time per query → cost and latency record
9. **Human** (loop step 6): QA reviewers score the harness run against ground truths computed outside the platform → pass rate
10. **Outcome** (loop step 7): Self-serve answers with consistency to certified reports and transparent cost (targets) → fewer analyst tickets

</details>

**Conversational analytics (sales & market data)** · M1–M2 · L2 · Self-serve answers, 99%+ consistency, transparent cost (targets)

- Problem: Business users queue behind central analysts for sales and market answers
- AI did: Answered multi-domain questions in natural language
- Solution did: Semantic layer, annotations, persona access control, synthetic data, cost logging
- Architecture: Sample data → Synthetic generator → Semantic layer + annotations → Analytics assistant → Persona-scoped answers + cost log

<sub>Anonymized: industries and generic system types only. Outcomes are labelled target, achieved, proposal or pilot exactly as the source work states them.</sub>
