<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg?v=a59d5c7a">
  <img alt="I turn enterprise context into AI that acts. Animated: ERP, CRM, ticketing, HR, commerce, logistics, voice and knowledge bubbles feed a glowing enterprise-context core; an agent below it fires actions: deflect, resolve, automate." src="assets/hero-light.svg?v=4db9c928" width="100%">
</picture>


**AI Solutions Engineer** | Context layer first, agents on top | Agentic AI across complex enterprise systems | Guardrails, evals and human gates built in | 13+ yrs in SaaS · 5+ yrs enterprise AI | APJ SE of the Year

[![LinkedIn](https://img.shields.io/badge/LinkedIn-shivaji--md-6E22FE?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=151515)](https://www.linkedin.com/in/shivaji-m-d-ab983a65) [![Email](https://img.shields.io/badge/Email-shiv.shivaji090%40gmail.com-FDF049?style=for-the-badge&logo=gmail&logoColor=151515&labelColor=151515)](mailto:shiv.shivaji090@gmail.com)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/maturity-dark.svg?v=2dbf88a0">
  <img alt="AI-centric employees create AI-centric companies. Two dotted curves. The AI employee journey: AI blind, AI curious, daily AI, expanding AI, AI first, AI evangelist. The AI company journey, running behind it: AI desert, AI tools, AI initiatives, AI champions, AI platform, AI-centric business." src="assets/maturity-light.svg?v=1684abe9" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/evolution-dark.svg?v=29e5b156">
  <img alt="Latest first: 2024-now AI Solutions Engineer at DevRev (generative and agentic AI; airline payments desk 15-30 to under 5 min per case, target), then 2021-2024 Presales Manager to Lead Solutions Consulting at MoEngage (predictive ML, L2; +50% conversion to proposal). A dotted line points ahead to Solutions Architect, governed enterprise AI." src="assets/evolution-light.svg?v=6b7c2b64" width="100%">
</picture>

<details>
<summary><b>Text version: how I evolved</b></summary>

- **2024–now · AI Solutions Engineer, DevRev → architect** (Generative & agentic AI, journey: ai evangelist). Pipeline: 16+ connectors → Governed context → Multi-agent → Evals + guardrails → outcomes: Hours saved ↑, Cost to serve ↓, Revenue ↑, CSAT ↑. concepts: Context layer, Multi-agent orchestration, Evals, Guardrails, Per-user identity, Retrieval, not stuffing. Learned: The model is a component; the solution is the product.
- **2021–2024 · Presales Manager → Lead Solutions Consulting, MoEngage · promoted Feb 2023** (Predictive ML + GenAI, journey: expanding ai). Pipeline: SDKs + Data API → Warehouse sync → RFM segments → Sherpa models → outcomes: MAU / DAU ↑, Retention ↑, CTR ↑, CVR ↑. data in: Android/iOS/Web SDKs, Data API (server events), S3/SFTP imports, Warehouse (BigQuery/Snowflake/Redshift), CDP sources; sherpa (now merlin ai): Best Time to Send, Most Preferred Channel, Predictions (churn & conversion), Dynamic A/B (bandit-style), RFM segments (1–3 per axis), Flows (journeys). Learned: AI is only as good as the event data feeding it.

Explainers I used with customers (general techniques, not vendor claims): propensity models are typically gradient-boosted trees; behavioral clustering, e.g. k-means; a multi-armed bandit shifts traffic to the winning variant while still exploring; RFM scores recency, frequency and monetary value; aggregations turn event streams into features (counts, recency, rolling windows).

</details>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/awards-dark.svg?v=7672a538">
  <img alt="Awards, latest first: APJ SE of the Year, DevRev, Sales Kickoff 2026; Deal Maker, MoEngage, Annual Sales Kickoff 2024; Rainmaker, MoEngage, Q2 2022." src="assets/awards-light.svg?v=c6829ae1" width="100%">
</picture>


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/approach-dark.svg?v=70e96323">
  <img alt="A seven-step problem-solving loop: 1 Find the pain and baseline it; 2 Map the process and systems; 3 Unify the context; 4 Design the agent; 5 Guardrails and humans at the right gates; 6 Prove it before go-live; 7 Measure the outcome, then expand. Each industry tab is one run of the loop." src="assets/approach-light.svg?v=a1566cb4" width="100%">
</picture>

<details>
<summary><b>Text version: my approach</b></summary>

1. **Find the pain and baseline it**: minutes, cost, risk
2. **Map the process and systems**: who, what, where the data lives
3. **Unify the context**: connectors, governed objects, annotations
4. **Design the agent**: skills, tools, prompt contract, state outside the model
5. **Guardrails and humans at the right gates**: approvals, hard blocks, escalation
6. **Prove it before go-live**: shadow run, evals, targets
7. **Measure the outcome, then expand**: time, cost, revenue, risk

</details>

## Concepts

<details>
<summary><b>How sync actually works: 9 concepts</b></summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/concepts-dark.svg?v=09ecb61e">
  <img alt="Nine connector concepts, each with its business effect: Modified-date watermark; Content hashing; Settled-record skip; Polling vs webhooks; Pagination that can't lie; REST vs GraphQL; Idempotent typed IDs; Backoff with jitter; Checkpoint after verified writes." src="assets/concepts-light.svg?v=21be79ad" width="100%">
</picture>

1. **Modified-date watermark**: Read only records with updated_at after the last one seen, minus a small overlap for clock skew. *Business:* smaller syncs, fresher data, lower API cost.
2. **Content hashing**: No reliable timestamp? Hash the mapped fields; send only on change. Cut ~1.3k unchanged re-sends per sync. *Business:* fewer re-sends, no duplicates, lower load cost.
3. **Settled-record skip**: Stop re-fetching records already in a terminal state, such as delivered shipments. *Business:* shorter syncs and fewer API calls.
4. **Polling vs webhooks**: Polling: I ask on a schedule, self-healing. Webhooks: they tell me now, at-least-once, so verify the HMAC. *Business:* near-real-time updates without missed events.
5. **Pagination that can't lie**: Cursor or keyset beats offset; time windows split when a page cap hits. A page-100 cap once gave 5k of 88k orders. *Business:* complete data: no silently missing records.
6. **REST vs GraphQL**: REST: many endpoints, fixed shapes, N+1 calls. GraphQL: one exact nested query, cost-based limits, errors that arrive with HTTP 200. *Business:* fewer calls, faster syncs, predictable limits.
7. **Idempotent typed IDs**: Stable ids prefixed by type, so retries never duplicate and order-123 never collides with return-123. *Business:* no duplicates or collisions, so reports stay trusted.
8. **Backoff with jitter**: Retry 429s and 5xx with exponential backoff plus jitter. Never retry a 4xx: that is a bug. *Business:* syncs survive rate limits without manual reruns.
9. **Checkpoint after verified writes**: Save state only after the upload is verified; move large state out of the run into durable storage. *Business:* no lost or duplicated data after a crash.

</details>

<details>
<summary><b>How agents actually work: 12 concepts</b></summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/agents-dark.svg?v=6cbafa44">
  <img alt="Twelve agent-design concepts, each with its business effect: Prompt architecture; State outside the model; Retrieval, not stuffing; Skills and tools; Grounded answers (RAG); Numbers by rules; Workflows first; Guardrails; Human in the loop; Evals before go-live; Identity and context; Voice agents." src="assets/agents-light.svg?v=f97b0679" width="100%">
</picture>

1. **Prompt architecture**: Role, scope, rules and output contract as layered sections, not a wall of text. Red-teaming finds the gaps. *Business:* predictable behavior, faster review and sign-off.
2. **State outside the model**: The context window is not a database. Each turn reads a typed state record, decides one step, validates it and writes it back, so long chats don't drift. *Business:* long cases finish correctly, in minutes.
3. **Retrieval, not stuffing**: An agent needs thousands of tokens, not trillions. Route each question: Text-to-SQL for numbers, semantic search for meaning, a keyword index for exact ids. *Business:* 10–100× fewer tokens, lower cost, fewer hallucinations.
4. **Skills and tools**: Each skill has one job, typed inputs and a narrow permission. The agent picks skills; it never improvises API calls. *Business:* safe automation within permissions, easy audits.
5. **Grounded answers (RAG)**: Retrieve from the knowledge base or graph first, answer only from what came back, and cite it. *Business:* answers customers can trust, with sources.
6. **Numbers by rules**: Figures come from versioned rules and queries. The model explains them and never invents a number. *Business:* no invented figures in finance reports.
7. **Workflows first**: Deterministic steps and approvals, with the model used inside a step only where judgment is needed. *Business:* consistent outcomes with auditable steps.
8. **Guardrails**: Check every output against facts and policy (amounts, ids, PII) before it ships; block or redraft on failure. *Business:* wrong amounts, ids or PII never reach customers.
9. **Human in the loop**: Consequential actions such as refunds and write-backs need approval. Maker-checker by default. *Business:* risky actions stay controlled; lower financial risk.
10. **Evals before go-live**: A golden set of real cases, a pass threshold as the gate, re-run on every prompt or model change. *Business:* fewer production incidents, faster risk sign-off.
11. **Identity and context**: The agent acts as the user, with that user's own permissions, over governed enterprise memory. *Business:* no permission leaks; security signs off sooner.
12. **Voice agents**: Language, voice and greeting must all match, and latency is a feature, not an afterthought. *Business:* callers stay on the line; fewer drop-offs.

</details>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg?v=59ba16ba">
  <img alt="Agents and AI, context and integration, languages, and solution craft." src="assets/stack-light.svg?v=41e3844f" width="100%">
</picture>

<a href="https://www.linkedin.com/in/shivaji-m-d-ab983a65/recent-activity/articles/">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/writing-dark.svg?v=28718f7d">
  <img alt="LinkedIn article, April 2026: Your AI agent doesn't have a knowledge problem. It has a noise problem." src="assets/writing-light.svg?v=f41b779b" width="100%">
</picture>
</a>

<sub>Every visual is generated by [build_profile.py](build_profile.py) (stdlib Python; `python3 build_profile.py --preview`
renders previews). Client names are left out on purpose: industries and generic system types only.</sub>
