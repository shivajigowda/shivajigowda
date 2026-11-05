# Retail & D2C: AI use cases I've solutioned

[← back to profile](../README.md)

<p align="center">
<a href="airlines.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-airlines-off-dark.svg?v=29b7f121"><img alt="Airlines" src="../assets/tab-airlines-off-light.svg?v=a5de0822" height="40"></picture></a>
<a href="bfsi-fintech.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-bfsi-fintech-off-dark.svg?v=8ee70b76"><img alt="BFSI & Fintech" src="../assets/tab-bfsi-fintech-off-light.svg?v=26bd3e6a" height="40"></picture></a>
<a href="retail-d2c.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-retail-d2c-on-dark.svg?v=ebe1f47b"><img alt="Retail & D2C" src="../assets/tab-retail-d2c-on-light.svg?v=3d77027a" height="40"></picture></a>
<a href="automotive.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-automotive-off-dark.svg?v=e1da197d"><img alt="Automotive" src="../assets/tab-automotive-off-light.svg?v=d8efb5fd" height="40"></picture></a>
<a href="pharma.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-pharma-off-dark.svg?v=a1e6ad0c"><img alt="Pharma" src="../assets/tab-pharma-off-light.svg?v=094b707d" height="40"></picture></a>
<a href="it-services.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-it-services-off-dark.svg?v=feae9385"><img alt="IT services" src="../assets/tab-it-services-off-light.svg?v=66745c5f" height="40"></picture></a>
<a href="marketing.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-marketing-off-dark.svg?v=35e037b3"><img alt="Marketing" src="../assets/tab-marketing-off-light.svg?v=f13446de" height="40"></picture></a>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/uc-retail-d2c-1-dark.svg?v=3aaee1f4">
  <img alt="Retail & D2C use case: Apparel retail AI transformation. Problem: Two weeks a month of Excel to derive COGS and P&L. AI did: Explained variances, drafted outputs, flagged availability exceptions (proposed). Solution did: Unified sources, quality gates, versioned finance rules, lineage, shadow runs. Business outcome: Automated explainable close; availability above 98%. KPI: time. Architecture: ERP · DMS · POS · e-commerce → Sync connectors + quality gates → Knowledge graph → Area agents + workflow engine → App · chat · export." src="../assets/uc-retail-d2c-1-light.svg?v=498f6689" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/wf-retail-d2c-1-dark.svg?v=1b4f4df4">
  <img alt="Solution workflow (scheduled/batch) for Apparel retail AI transformation: 1 trigger: Scheduled sync (daily by default, intraday where needed, monthly for close packs) → source pulls; 2 system: Connectors pull read-only from ERP exports, DMS, POS, e-commerce, planning tool, HRMS and file drops, deltas only → staged data; 3 guardrail: Quality gate checks freshness, duplicates, missing keys and control totals → pass or block insights; 4 decision: Gate passed? yes → step 5 / no → insights blocked and data owner alerted; 5 system: Maps to the common grain (SKU, pack size, channel, month) in the knowledge graph with lineage and permissions → trusted base; 6 agent: Finance and planning agents run versioned rules for price bridge, COGS, forecast and plan vs actual; model explains, drafts → draft outputs; 7 human: Finance and planners approve key outputs at each gate → approved figures; 8 skill: Availability control tower raises debounced alerts with causes and next actions → exceptions; 9 system: Delivers via app, email, team chat, spreadsheet or PDF with data-as-of time; audit log and value ledger → governed delivery; 10 outcome: Automated explainable monthly close and earlier stock-out flags → time and working-capital gains" src="../assets/wf-retail-d2c-1-light.svg?v=7d40726e" width="100%">
</picture>

<details>
<summary>Workflow steps as text: Apparel retail AI transformation</summary>

1. **Trigger** (loop step 2): Scheduled sync (daily by default, intraday where needed, monthly for close packs) → source pulls
2. **System** (loop step 3): Connectors pull read-only from ERP exports, DMS, POS, e-commerce, planning tool, HRMS and file drops, deltas only → staged data
3. **Guardrail** (loop step 5): Quality gate checks freshness, duplicates, missing keys and control totals → pass or block insights
4. **Decision** (loop step 4): Gate passed? yes → step 5 / no → insights blocked and data owner alerted
5. **System** (loop step 3): Maps to the common grain (SKU, pack size, channel, month) in the knowledge graph with lineage and permissions → trusted base
6. **Agent** (loop step 4): Finance and planning agents run versioned rules for price bridge, COGS, forecast and plan vs actual; model explains, drafts → draft outputs
7. **Human** (loop step 5): Finance and planners approve key outputs at each gate → approved figures
8. **Skill** (loop step 4): Availability control tower raises debounced alerts with causes and next actions → exceptions
9. **System** (loop step 3): Delivers via app, email, team chat, spreadsheet or PDF with data-as-of time; audit log and value ledger → governed delivery
10. **Outcome** (loop step 7): Automated explainable monthly close and earlier stock-out flags → time and working-capital gains

</details>

**Apparel retail AI transformation** · Automated explainable close; availability above 98%

- Problem: Two weeks a month of Excel to derive COGS and P&L
- AI did: Explained variances, drafted outputs, flagged availability exceptions (proposed)
- Solution did: Unified sources, quality gates, versioned finance rules, lineage, shadow runs
- Architecture: ERP · DMS · POS · e-commerce → Sync connectors + quality gates → Knowledge graph → Area agents + workflow engine → App · chat · export

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/uc-retail-d2c-2-dark.svg?v=baad80d7">
  <img alt="Retail & D2C use case: Customer-experience agent. Problem: Brittle 95-node bot could not absorb launch-surge support. AI did: Chose skills; answered orders, returns, refunds in natural language. Solution did: Unified four systems; one re-skinnable agent; human escalation wired. Business outcome: ~76% deflection through ~14x surge. KPI: cost. Architecture: Storefront · shipping · returns · tracking → Sync layer: one customer record → Identity + cross-channel memory → CX agent, 8 skills → WhatsApp + email; human team." src="../assets/uc-retail-d2c-2-light.svg?v=11a096ec" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/wf-retail-d2c-2-dark.svg?v=b4b92d44">
  <img alt="Solution workflow (hybrid) for Customer-experience agent: 1 trigger: Shopper sends a message on messaging or email → conversation opened with unified identity and cross-channel memory; 2 agent: Understands the request in natural language and picks a skill → skill call; 3 skill: Reads live order, tracking, refund or catalogue data from the source systems → verified facts; 4 decision: Is the request an action (return, exchange, cancel)? yes → step 5 / no → step 8; 5 skill: Checks per-item eligibility against window and policy → verdict; 6 decision: Eligible? yes → step 7 / no → step 9; 7 skill: Files the return/exchange or cancels the unshipped order and triggers the refund → record in order and returns systems; 8 agent: Replies with status, answer or product results → resolved conversation (deflected); 9 human: Receives handover with sentiment and severity classification, works the chat or ticket with SLA and CSAT → human resolution; 10 outcome: Self-served conversation or escalated case with full context → deflection and zero broken journeys" src="../assets/wf-retail-d2c-2-light.svg?v=ce86a585" width="100%">
</picture>

<details>
<summary>Workflow steps as text: Customer-experience agent</summary>

1. **Trigger** (loop step 2): Shopper sends a message on messaging or email → conversation opened with unified identity and cross-channel memory
2. **Agent** (loop step 4): Understands the request in natural language and picks a skill → skill call
3. **Skill** (loop step 4): Reads live order, tracking, refund or catalogue data from the source systems → verified facts
4. **Decision** (loop step 4): Is the request an action (return, exchange, cancel)? yes → step 5 / no → step 8
5. **Skill** (loop step 4): Checks per-item eligibility against window and policy → verdict
6. **Decision** (loop step 4): Eligible? yes → step 7 / no → step 9
7. **Skill** (loop step 4): Files the return/exchange or cancels the unshipped order and triggers the refund → record in order and returns systems
8. **Agent** (loop step 4): Replies with status, answer or product results → resolved conversation (deflected)
9. **Human** (loop step 5): Receives handover with sentiment and severity classification, works the chat or ticket with SLA and CSAT → human resolution
10. **Outcome** (loop step 7): Self-served conversation or escalated case with full context → deflection and zero broken journeys

</details>

**Customer-experience agent** · ~76% deflection through ~14x surge

- Problem: Brittle 95-node bot could not absorb launch-surge support
- AI did: Chose skills; answered orders, returns, refunds in natural language
- Solution did: Unified four systems; one re-skinnable agent; human escalation wired
- Architecture: Storefront · shipping · returns · tracking → Sync layer: one customer record → Identity + cross-channel memory → CX agent, 8 skills → WhatsApp + email; human team

<sub>Anonymized: industries and generic system types only.</sub>
