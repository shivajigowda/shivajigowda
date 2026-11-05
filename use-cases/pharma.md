# Pharma: AI use cases I've solutioned

[← back to profile](../README.md)

<p align="center">
<a href="airlines.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-airlines-off-dark.svg?v=29b7f121"><img alt="Airlines" src="../assets/tab-airlines-off-light.svg?v=a5de0822" height="40"></picture></a>
<a href="bfsi-fintech.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-bfsi-fintech-off-dark.svg?v=8ee70b76"><img alt="BFSI & Fintech" src="../assets/tab-bfsi-fintech-off-light.svg?v=26bd3e6a" height="40"></picture></a>
<a href="retail-d2c.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-retail-d2c-off-dark.svg?v=de14334d"><img alt="Retail & D2C" src="../assets/tab-retail-d2c-off-light.svg?v=1cb9dfde" height="40"></picture></a>
<a href="automotive.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-automotive-off-dark.svg?v=e1da197d"><img alt="Automotive" src="../assets/tab-automotive-off-light.svg?v=d8efb5fd" height="40"></picture></a>
<a href="pharma.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-pharma-on-dark.svg?v=9d476008"><img alt="Pharma" src="../assets/tab-pharma-on-light.svg?v=711bcab6" height="40"></picture></a>
<a href="it-services.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-it-services-off-dark.svg?v=feae9385"><img alt="IT services" src="../assets/tab-it-services-off-light.svg?v=66745c5f" height="40"></picture></a>
<a href="marketing.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-marketing-off-dark.svg?v=35e037b3"><img alt="Marketing" src="../assets/tab-marketing-off-light.svg?v=f13446de" height="40"></picture></a>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/uc-pharma-1-dark.svg?v=ec539aff">
  <img alt="Pharma use case: Production planning & plant / machine optimization. Problem: 16–17 planners took 10 days on monthly batch and machine plans in spreadsheets. AI did: Applied batch rules, checked readiness and equipment qualification, grouped batches, drafted machine-level plan. Solution did: Linked custom objects, shadow run, zero-violation guardrail, accuracy and ROI measurement. Business outcome: Plan in about 1 hour, 80%+ effort cut, fewer batches and changeovers. KPI: time. Architecture: ERP + quality exports → 11 linked custom objects → Planning agent: readiness + batch skills → Plan pack → Planner + QA approve." src="../assets/uc-pharma-1-light.svg?v=e35b1daf" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/wf-pharma-1-dark.svg?v=411e7538">
  <img alt="Solution workflow (hybrid) for Production planning & plant / machine optimization: 1 trigger: Planner asks in chat, or the monthly/weekly schedule fires → planning request; 2 system: Exports from ERP, validated-batch-size system, quality-event system and validation planner load as-is into linked objects → reconciled data; 3 skill: Readiness skill checks master documents, MES recipe, open quality items, equipment requalification and materials per line → Ready / At risk / Blocked with blocker and owner; 4 skill: Batch-and-machine skill applies R1-R3 to demand and rounds to whole batches → batch sizes; 5 guardrail: Only equipment validated for the batch size and in date on requalification is used; others flagged with reason → compliant assignment; 6 skill: Groups batches sharing a blend to reduce non-serial changeovers → sequence and changeover saving; 7 decision: Any line blocked or equipment lapsed? yes → flag with source record for the owner / no → include in draft plan; 8 agent: Produces the machine-level draft plan with rationale per batch → plan pack; 9 human: Planner and quality SME review and approve; no write-back to source systems → approved plan; 10 outcome: Draft in about one hour and plan ready earlier, with zero violations → planner capacity released" src="../assets/wf-pharma-1-light.svg?v=4424e5e6" width="100%">
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
10. **Outcome** (loop step 7): Draft in about one hour and plan ready earlier, with zero violations → planner capacity released

</details>

**Production planning & plant / machine optimization** · Plan in about 1 hour, 80%+ effort cut, fewer batches and changeovers

- Problem: 16–17 planners took 10 days on monthly batch and machine plans in spreadsheets
- AI did: Applied batch rules, checked readiness and equipment qualification, grouped batches, drafted machine-level plan
- Solution did: Linked custom objects, shadow run, zero-violation guardrail, accuracy and ROI measurement
- Architecture: ERP + quality exports → 11 linked custom objects → Planning agent: readiness + batch skills → Plan pack → Planner + QA approve

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/uc-pharma-2-dark.svg?v=25b95415">
  <img alt="Pharma use case: Conversational analytics (sales & market data). Problem: Business users queue behind central analysts for sales and market answers. AI did: Answered multi-domain questions in natural language. Solution did: Catalog sync of BigQuery metadata, semantic layer + annotations, runtime query generation, persona access, cost logging. Business outcome: Self-serve answers, 99%+ consistency, transparent cost. KPI: time. Architecture: Google BigQuery → Metadata catalog sync → Semantic layer + annotations → Runtime query generation → Analytics answers + cost log." src="../assets/uc-pharma-2-light.svg?v=d6dda988" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/wf-pharma-2-dark.svg?v=47e25ad0">
  <img alt="Solution workflow (conversational) for Conversational analytics (sales & market data): 1 trigger: Business user asks a question in natural language → request with persona; 2 guardrail: Persona access control and region/brand scope applied before any query → scoped request; 3 system: Catalog sync pulls table and column metadata from Google BigQuery → governed metadata catalog; 4 agent: Reads guidance, synonym map and field annotations; resolves metric and entities → query plan; 5 decision: Native text-to-SQL can see the custom fields? yes → step 6 / no → step 7; 6 skill: Generates SQL at runtime from the catalog and runs it on BigQuery → result set; 7 skill: Calls the domain query skill or cross-domain join skill → result set; 8 agent: Answers with table, period and scope using business labels, refusing schema enumeration and out-of-scope data → answer; 9 system: Logs tokens, cost and response time per query → cost and latency record; 10 human: QA reviewers score the harness run against ground truths computed outside the platform → pass rate; 11 outcome: Self-serve answers with consistency to certified reports and transparent cost → fewer analyst tickets" src="../assets/wf-pharma-2-light.svg?v=34306a97" width="100%">
</picture>

<details>
<summary>Workflow steps as text: Conversational analytics (sales & market data)</summary>

1. **Trigger** (loop step 2): Business user asks a question in natural language → request with persona
2. **Guardrail** (loop step 5): Persona access control and region/brand scope applied before any query → scoped request
3. **System** (loop step 3): Catalog sync pulls table and column metadata from Google BigQuery → governed metadata catalog
4. **Agent** (loop step 4): Reads guidance, synonym map and field annotations; resolves metric and entities → query plan
5. **Decision** (loop step 4): Native text-to-SQL can see the custom fields? yes → step 6 / no → step 7
6. **Skill** (loop step 4): Generates SQL at runtime from the catalog and runs it on BigQuery → result set
7. **Skill** (loop step 4): Calls the domain query skill or cross-domain join skill → result set
8. **Agent** (loop step 4): Answers with table, period and scope using business labels, refusing schema enumeration and out-of-scope data → answer
9. **System** (loop step 3): Logs tokens, cost and response time per query → cost and latency record
10. **Human** (loop step 6): QA reviewers score the harness run against ground truths computed outside the platform → pass rate
11. **Outcome** (loop step 7): Self-serve answers with consistency to certified reports and transparent cost → fewer analyst tickets

</details>

**Conversational analytics (sales & market data)** · Self-serve answers, 99%+ consistency, transparent cost

- Problem: Business users queue behind central analysts for sales and market answers
- AI did: Answered multi-domain questions in natural language
- Solution did: Catalog sync of BigQuery metadata, semantic layer + annotations, runtime query generation, persona access, cost logging
- Architecture: Google BigQuery → Metadata catalog sync → Semantic layer + annotations → Runtime query generation → Analytics answers + cost log

<sub>Anonymized: industries and generic system types only.</sub>
