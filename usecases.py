"""Anonymized use cases by industry (industries and generic system types only; no client names).
Rows follow the case-study notes' 'Profile rows by industry', latest first within each industry.
Workflows are imported from the notes by import_workflows.py into workflows.json when available."""
import json
from pathlib import Path

TABS = [("airlines", "Airlines"), ("bfsi-fintech", "BFSI & Fintech"), ("retail-d2c", "Retail & D2C"),
        ("automotive", "Automotive"), ("pharma", "Pharma"), ("it-services", "IT services"),
        ("marketing", "Marketing")]

# slug -> [dict(use, problem, ai, solution, outcome, tag, kpi, arch)]
CASES = {
    "airlines": [dict(
        use="Payments desk transformation",
        problem="Paid-but-unbooked cases took 15–30 min across three systems",
        ai="Searched, reserved, enrolled, billed, retrieved booking, closed case",
        solution="Integrated three systems; human confirm gates; escalation matrix and audits",
        outcome="Under 5 min per case (target)", tag="M3 · L3", kpi="time",
        arch=["CRM case", "AI workspace chat", "Payment gateway + reservation system", "Human confirms",
              "Payment link → booking ref", "CRM auto-close"])],
    "bfsi-fintech": [
        dict(use="Order-to-cash SaaS support PoC",
             problem="Rising in-app tickets for questions articles or data could resolve",
             ai="Answered how-tos, diagnosed tenant issues, categorized tickets",
             solution="Identity-bound tenant isolation, read-only queries, tiered automation, taxonomy",
             outcome="Fewer avoidable tickets (pilot to measure; no target)", tag="M2 · L3", kpi="cost",
             arch=["In-app chat, verified identity", "Support agent + KB", "Read-only diagnosis API",
                   "Confirm summary", "Tiered automation"]),
        dict(use="NBFC customer support transformation",
             problem="Every lender support email triaged by hand, regulators included",
             ai="Spotted authority senders, classified, wrote multilingual KB replies",
             solution="Dual-inbox rules, authority block, one-action cost cap, supervised go-live",
             outcome="Fewer manual touches, safe automation (targets)", tag="M2 · L3", kpi="risk",
             arch=["Service + complaints inboxes", "Ticket-created trigger", "Agent: authority scan, classify, mask PII",
                   "Category + reply", "Human groups for complaints"]),
    ],
    "retail-d2c": [
        dict(use="Apparel retail AI transformation",
             problem="Two weeks a month of Excel to derive COGS and P&L",
             ai="Explained variances, drafted outputs, flagged availability exceptions (proposed)",
             solution="Unified sources, quality gates, versioned finance rules, lineage, shadow runs",
             outcome="Automated explainable close; availability above 98% (targets)", tag="M1–M3 · L3", kpi="time",
             arch=["ERP · DMS · POS · e-commerce", "Sync connectors + quality gates", "Knowledge graph",
                   "Area agents + workflow engine", "App · chat · export"]),
        dict(use="Customer-experience agent (live)",
             problem="Brittle 95-node bot could not absorb launch-surge support",
             ai="Chose skills; answered orders, returns, refunds in natural language",
             solution="Unified four systems; one re-skinnable agent; human escalation wired",
             outcome="~76% deflection through ~14x surge (achieved)", tag="M3 · L3", kpi="cost",
             arch=["Storefront · shipping · returns · tracking", "Sync layer: one customer record",
                   "Identity + cross-channel memory", "CX agent, 8 skills", "WhatsApp + email; human team"]),
    ],
    "automotive": [dict(
        use="Dealer assist & navigation", problem="Dealers hit repeat system errors with scripted fixes",
        ai="Ran the right procedure from a pre-set starting turn",
        solution="Button tree, 35 handoff contracts, no-re-ask context payloads",
        outcome="Faster dealer self-service (no KPI stated)", tag="M2 · L2 (inferred)", kpi="time",
        arch=["Dealer-system chat widget", "Greeting + 5 buttons", "Handoff context payload",
              "Agent runs procedure", "Outcome + rating"])],
    "pharma": [
        dict(use="Production planning & plant / machine optimization",
             problem="16–17 planners took 10 days on monthly batch and machine plans in spreadsheets",
             ai="Applied batch rules, checked readiness and equipment qualification, grouped batches, drafted machine-level plan",
             solution="Linked custom objects, shadow run, zero-violation guardrail, accuracy and ROI measurement",
             outcome="Plan in about 1 hour, 80%+ effort cut, fewer batches and changeovers (targets)", tag="M2 · L2",
             kpi="time",
             arch=["ERP + quality exports", "11 linked custom objects", "Planning agent: readiness + batch skills",
                   "Plan pack", "Planner + QA approve"]),
        dict(use="Conversational analytics (sales & market data)",
             problem="Business users queue behind central analysts for sales and market answers",
             ai="Answered multi-domain questions in natural language",
             solution="Catalog sync of BigQuery metadata, semantic layer + annotations, runtime query generation, persona access, cost logging",
             outcome="Self-serve answers, 99%+ consistency, transparent cost (targets)", tag="M1–M2 · L2",
             kpi="time",
             arch=["Google BigQuery", "Metadata catalog sync", "Semantic layer + annotations", "Runtime query generation",
                   "Analytics answers + cost log"]),
    ],
    "it-services": [dict(
        use="Cloud managed-services support transformation",
        problem="Tickets took 25–40 min of manual alert correlation and drafting",
        ai="Auto-tracked incidents from observability alerts, triaged and classified, drafted replies and SOP steps",
        solution="Observability platform → auto incident tracking and AI triage; one-action workflow, P1/P2 hard block, human confirm gates",
        outcome="Under 5 min, 2x customers per team (targets)", tag="M3–M4 · L4", kpi="time",
        arch=["Observability alerts · email · portal", "Auto incident tracking", "Correlation + dedupe",
              "AI triage: classify P1–P4, draft", "Humans confirm; P1/P2 human-only"])],
    "marketing": [dict(
        use="Predictive marketing at MoEngage (2021–24)",
        problem="Right message, right user, right time, right channel (BFSI and retail)",
        ai="Sherpa (now Merlin AI): Best Time to Send, Most Preferred Channel, Predictions, Dynamic A/B",
        solution="SDKs + Data API + warehouse imports, RFM segments, Flows (journeys)",
        outcome="+50% conversion to proposal stage (achieved)", tag="M1–M2 · L2", kpi="revenue",
        arch=["SDKs + Data API", "Warehouse + S3/SFTP imports", "RFM segments", "Sherpa: BTS · MPC · predictions",
              "Flows + Dynamic A/B"])],
}

WORKFLOW_FILE = Path(__file__).parent / "workflows.json"


def workflow_for(use):
    """{"type": str, "steps": [[ACTOR, text], ...]} for a use case, or None when not imported."""
    if not WORKFLOW_FILE.exists():
        return None
    data = {k.lower(): v for k, v in json.loads(WORKFLOW_FILE.read_text()).items()}
    return data.get(use.lower())
