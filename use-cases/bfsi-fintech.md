# BFSI & Fintech: AI use cases I've solutioned

[← back to profile](../README.md)

<p align="center">
<a href="airlines.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-airlines-off-dark.svg"><img alt="Airlines" src="../assets/tab-airlines-off-light.svg" height="40"></picture></a>
<a href="bfsi-fintech.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-bfsi-fintech-on-dark.svg"><img alt="BFSI & Fintech" src="../assets/tab-bfsi-fintech-on-light.svg" height="40"></picture></a>
<a href="retail-d2c.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-retail-d2c-off-dark.svg"><img alt="Retail & D2C" src="../assets/tab-retail-d2c-off-light.svg" height="40"></picture></a>
<a href="automotive.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-automotive-off-dark.svg"><img alt="Automotive" src="../assets/tab-automotive-off-light.svg" height="40"></picture></a>
<a href="pharma.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-pharma-off-dark.svg"><img alt="Pharma" src="../assets/tab-pharma-off-light.svg" height="40"></picture></a>
<a href="it-services.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-it-services-off-dark.svg"><img alt="IT services" src="../assets/tab-it-services-off-light.svg" height="40"></picture></a>
<a href="marketing.md"><picture><source media="(prefers-color-scheme: dark)" srcset="../assets/tab-marketing-off-dark.svg"><img alt="Marketing" src="../assets/tab-marketing-off-light.svg" height="40"></picture></a>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/uc-bfsi-fintech-1-dark.svg">
  <img alt="BFSI & Fintech use case: Order-to-cash SaaS support PoC. Problem: Rising in-app tickets for questions articles or data could resolve. AI did: Answered how-tos, diagnosed tenant issues, categorized tickets. Solution did: Identity-bound tenant isolation, read-only queries, tiered automation, taxonomy. Business outcome: Fewer avoidable tickets (pilot will measure). KPI: cost. Architecture: In-app chat, verified identity → Support agent + KB → Read-only diagnosis API → Confirm summary → Tiered automation." src="../assets/uc-bfsi-fintech-1-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/wf-bfsi-fintech-1-dark.svg">
  <img alt="Solution workflow (conversational) for Order-to-cash SaaS support PoC: 1 trigger: User opens the embedded chat widget with a verified identity (user and tenant) → session; 2 user: Asks a product, how-to or account question → request; 3 agent: Answers from help articles, approved Q&A and SOPs, giving name, path and button label → answer; 4 decision: Account-specific issue? yes → step 5 / no → step 8; 5 guardrail: Tenant taken from verified identity only; any user-supplied tenant or customer ID is ignored → isolated scope; 6 skill: Runs read-only diagnosis queries (customer lookup, pool status, collectible status, ranking filter) → reasons; 7 agent: Explains each reason then the fix → explained answer; 8 decision: User confirms it helped? yes → close without ticket / no → step 9; 9 human: User confirms an agent-drafted, categorized summary; ticket is created and linked to the conversation; support reviews per tier → categorized ticket; 10 outcome: Fewer avoidable tickets and cleaner handoffs (pilot to measure) → lower support load" src="../assets/wf-bfsi-fintech-1-light.svg" width="100%">
</picture>

<details>
<summary>Workflow steps as text: Order-to-cash SaaS support PoC</summary>

1. **Trigger** (loop step 2): User opens the embedded chat widget with a verified identity (user and tenant) → session
2. **User** (loop step 2): Asks a product, how-to or account question → request
3. **Agent** (loop step 4): Answers from help articles, approved Q&A and SOPs, giving name, path and button label → answer
4. **Decision** (loop step 4): Account-specific issue? yes → step 5 / no → step 8
5. **Guardrail** (loop step 5): Tenant taken from verified identity only; any user-supplied tenant or customer ID is ignored → isolated scope
6. **Skill** (loop step 4): Runs read-only diagnosis queries (customer lookup, pool status, collectible status, ranking filter) → reasons
7. **Agent** (loop step 4): Explains each reason then the fix → explained answer
8. **Decision** (loop step 4): User confirms it helped? yes → close without ticket / no → step 9
9. **Human** (loop step 5): User confirms an agent-drafted, categorized summary; ticket is created and linked to the conversation; support reviews per tier → categorized ticket
10. **Outcome** (loop step 7): Fewer avoidable tickets and cleaner handoffs (pilot to measure) → lower support load

</details>

**Order-to-cash SaaS support PoC** · Fewer avoidable tickets (pilot will measure)

- Problem: Rising in-app tickets for questions articles or data could resolve
- AI did: Answered how-tos, diagnosed tenant issues, categorized tickets
- Solution did: Identity-bound tenant isolation, read-only queries, tiered automation, taxonomy
- Architecture: In-app chat, verified identity → Support agent + KB → Read-only diagnosis API → Confirm summary → Tiered automation

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/uc-bfsi-fintech-2-dark.svg">
  <img alt="BFSI & Fintech use case: NBFC customer support transformation. Problem: Every lender support email triaged by hand, regulators included. AI did: Spotted authority senders, classified, wrote multilingual KB replies. Solution did: Dual-inbox rules, authority block, one-action cost cap, supervised go-live. Business outcome: Fewer manual touches, safe automation (targets). KPI: risk. Architecture: Service + complaints inboxes → Ticket-created trigger → Agent: authority scan, classify, mask PII → Category + reply → Human groups for complaints." src="../assets/uc-bfsi-fintech-2-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/wf-bfsi-fintech-2-dark.svg">
  <img alt="Solution workflow (event-triggered) for NBFC customer support transformation: 1 trigger: Email lands in the service or complaints inbox → email integration creates one ticket per thread; 2 workflow: Fires once on ticket creation and calls the support agent → one AI action; 3 guardrail: Agent scans title, body, sender and display name for authority signals → authority flag; 4 decision: Authority or regulatory sender? yes → classify as complaint, zero reply, human queue / no → step 5; 5 agent: Classifies category and sub-category, applies inbox and email-type rules, searches KB, masks PII → structured output; 6 workflow: Sets category, sub-category, group atomically → routed ticket; 7 decision: Reply allowed and KB content found? yes → step 8 / no → fallback template or silent routing to human; 8 agent: Posts the multilingual KB reply as an external comment → customer email, stage awaiting customer; 9 workflow: No reply within N days → resolved then closed; customer follow-ups go to humans → closed or human-owned ticket; 10 human: Complaints and regulator mail handled in the complaints group → human resolution; 11 outcome: Fewer manual touches with regulator-safe automation (targets) → lower triage load" src="../assets/wf-bfsi-fintech-2-light.svg" width="100%">
</picture>

<details>
<summary>Workflow steps as text: NBFC customer support transformation</summary>

1. **Trigger** (loop step 2): Email lands in the service or complaints inbox → email integration creates one ticket per thread
2. **Workflow** (loop step 4): Fires once on ticket creation and calls the support agent → one AI action
3. **Guardrail** (loop step 5): Agent scans title, body, sender and display name for authority signals → authority flag
4. **Decision** (loop step 4): Authority or regulatory sender? yes → classify as complaint, zero reply, human queue / no → step 5
5. **Agent** (loop step 4): Classifies category and sub-category, applies inbox and email-type rules, searches KB, masks PII → structured output
6. **Workflow** (loop step 4): Sets category, sub-category, group atomically → routed ticket
7. **Decision** (loop step 4): Reply allowed and KB content found? yes → step 8 / no → fallback template or silent routing to human
8. **Agent** (loop step 4): Posts the multilingual KB reply as an external comment → customer email, stage awaiting customer
9. **Workflow** (loop step 4): No reply within N days → resolved then closed; customer follow-ups go to humans → closed or human-owned ticket
10. **Human** (loop step 5): Complaints and regulator mail handled in the complaints group → human resolution
11. **Outcome** (loop step 7): Fewer manual touches with regulator-safe automation (targets) → lower triage load

</details>

**NBFC customer support transformation** · Fewer manual touches, safe automation (targets)

- Problem: Every lender support email triaged by hand, regulators included
- AI did: Spotted authority senders, classified, wrote multilingual KB replies
- Solution did: Dual-inbox rules, authority block, one-action cost cap, supervised go-live
- Architecture: Service + complaints inboxes → Ticket-created trigger → Agent: authority scan, classify, mask PII → Category + reply → Human groups for complaints

<sub>Anonymized: industries and generic system types only. Outcomes are labelled target, achieved, proposal or pilot exactly as the source work states them.</sub>
