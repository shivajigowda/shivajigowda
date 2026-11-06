"""'How agents actually work': the sync panel's twin, in the deck's warm accents (orange, crimson, gold)."""
from panels_concepts import grid
from svgkit import circle, path, rect, text

# (eyebrow, title, plain-English explanation, used in, tone, glyph)
AGENTS = [
    ("prompting", "Prompt architecture",
     "Role, scope, rules and output contract as layered sections, not a wall of text. Red-teaming finds the gaps.",
     "Airline payments-desk agent", "peach", "sheets",
     "predictable behavior, faster review and sign-off"),
    ("state", "State outside the model",
     "The context window is not a database. Each turn reads a typed state record, decides one step, validates it "
     "and writes it back, so long chats don't drift.",
     "Airline payments desk · 15–30 → <5 min", "yellow", "loop",
     "long cases finish correctly, in minutes"),
    ("retrieval", "Retrieval, not stuffing",
     "An agent needs thousands of tokens, not trillions. Route each question: Text-to-SQL for numbers, semantic "
     "search for meaning, a keyword index for exact ids.",
     "Enterprise search & analytics agents", "pink", "pipes",
     "10–100× fewer tokens, lower cost, fewer hallucinations"),
    ("skills", "Skills and tools",
     "Each skill has one job, typed inputs and a narrow permission. The agent picks skills; it never improvises API calls.",
     "Planning & analytics skills", "yellow", "socket",
     "safe automation within permissions, easy audits"),
    ("grounding", "Grounded answers (RAG)",
     "Retrieve from the knowledge base or graph first, answer only from what came back, and cite it.",
     "Support agent assist", "pink", "cite",
     "answers customers can trust, with sources"),
    ("numbers", "Numbers by rules",
     "Figures come from versioned rules and queries. The model explains them and never invents a number.",
     "Finance / P&L copilot", "yellow", "calc",
     "no invented figures in finance reports"),
    ("workflows", "Workflows first",
     "Deterministic steps and approvals, with the model used inside a step only where judgment is needed.",
     "Ticket triage & enrichment", "peach", "ladder",
     "consistent outcomes with auditable steps"),
    ("guardrails", "Guardrails",
     "Check every output against facts and policy (amounts, ids, PII) before it ships; block or redraft on failure.",
     "Customer-facing replies", "pink", "shield",
     "wrong amounts, ids or PII never reach customers"),
    ("approval", "Human in the loop",
     "Consequential actions such as refunds and write-backs need approval. Maker-checker by default.",
     "Refunds & write-back", "peach", "switch",
     "risky actions stay controlled; lower financial risk"),
    ("evals", "Evals before go-live",
     "A golden set of real cases, a pass threshold as the gate, re-run on every prompt or model change.",
     "Every agent", "yellow", "score",
     "fewer production incidents, faster risk sign-off"),
    ("identity", "Identity and context",
     "The agent acts as the user, with that user's own permissions, over governed enterprise memory.",
     "Help-desk copilot (act-as)", "pink", "badge",
     "no permission leaks; security signs off sooner"),
    ("voice", "Voice agents",
     "Language, voice and greeting must all match, and latency is a feature, not an afterthought.",
     "Insurance voice agent", "yellow", "voice",
     "callers stay on the line; fewer drop-offs"),
]


def _glyph(kind, x, y, T, ink):
    """Mini diagram inside an 84 x 36 box at (x, y), warm accents."""
    O, C, Gd = T["orange"], T["crimson"], T["gold"]
    m = y + 18
    if kind == "sheets":
        o = [rect(x + 4 + i * 9, y + 2 + i * 4, 40, 26, T["card"], [ink, O, C][i], 1.2, 4) for i in range(3)]
        o += [path(f"M{x + 28},{y + 16 + k * 5}h{18 - k * 5}", C, 1.4) for k in range(3)]
        return "".join(o) + path(f"M{x + 72},{y + 6}l8,8l-8,8", C, 1.6)
    if kind == "socket":
        return (rect(x + 2, y + 8, 30, 20, O, rx=6) + path(f"M{x + 32},{m - 5}h10M{x + 32},{m + 5}h10", O, 2.2)
                + rect(x + 46, y + 4, 34, 28, "none", ink, 1.4, 7)
                + circle(x + 57, m - 5, 2.2, ink) + circle(x + 57, m + 5, 2.2, ink) + circle(x + 70, m, 2.2, C))
    if kind == "cite":
        return (rect(x + 2, y + 2, 28, 32, T["card"], ink, 1.2, 4) + path(f"M{x + 8},{y + 11}h16M{x + 8},{y + 18}h16M{x + 8},{y + 25}h10", ink, 1.1)
                + path(f"M{x + 46},{y + 30}c-8,-10 -10,-13 -10,-17a10,10 0 0,1 20,0c0,4 -2,7 -10,17z", C, 1.4, fill=C)
                + circle(x + 46, y + 13, 3.5, T["card"]) + rect(x + 60, y + 8, 22, 16, O, rx=6)
                + path(f"M{x + 64},{y + 24}l-2,6l7,-6", O, 1.2, fill=O))
    if kind == "calc":
        o = [rect(x + 2, y + 2, 28, 32, "none", ink, 1.3, 5), rect(x + 6, y + 6, 20, 7, Gd, rx=2)]
        o += [rect(x + 6 + c * 7, y + 17 + r * 7, 5, 5, ink, rx=1, opacity=0.7) for r in range(2) for c in range(3)]
        o += [path(f"M{x + 40},{y + 6}h40v18h-24l-8,7v-7h-8z", O, 1.4), path(f"M{x + 47},{y + 13}h26M{x + 47},{y + 18}h16", O, 1.2)]
        return "".join(o)
    if kind == "ladder":
        o = [rect(x + 2 + i * 15, y + 26 - i * 9, 13, 8 + i * 9, [ink, O, O][i], rx=2, opacity=[0.5, 0.75, 1][i])
             for i in range(3)]
        o += [path(f"M{x + 56},{m}l7,-7l7,7l-7,7z", C, 1.5, fill=C), path(f"M{x + 72},{m}h10", C, 1.4)]
        return "".join(o)
    if kind == "shield":
        return (path(f"M{x + 26},{y + 2}l14,5v10c0,9 -7,15 -14,17c-7,-2 -14,-8 -14,-17v-10z", O, 1.6, fill=T["card"])
                + path(f"M{x + 20},{m}l5,5l8,-9", C, 2) + text(x + 50, m - 3, "$ id", ink, 8.5, 700, font="mono")
                + text(x + 50, m + 10, "PII", C, 8.5, 700, font="mono"))
    if kind == "switch":
        return (rect(x + 2, y + 9, 40, 18, O, rx=9) + circle(x + 33, m, 7, T["card"])
                + circle(x + 62, y + 9, 5.5, "none", ink, 1.4)
                + path(f"M{x + 52},{y + 32}c0,-8 4,-12 10,-12s10,4 10,12", ink, 1.4) + path(f"M{x + 74},{y + 8}l3,3l6,-6", C, 1.8))
    if kind == "score":
        o = [path(f"M{x},{y + 33}H{x + 84}", ink, 1.2, opacity=0.5)]
        for i, h in enumerate([16, 24, 20, 28, 26]):
            o.append(rect(x + 4 + i * 16, y + 33 - h, 10, h, C if h >= 20 else ink, rx=2, opacity=None if h >= 20 else 0.4))
        o += [path(f"M{x + 1 + k * 8},{y + 13}h4", Gd, 1.6) for k in range(11)]
        return "".join(o)
    if kind == "loop":
        o = [rect(x + 30, y + 9, 24, 18, T["card"], ink, 1.3, 4), path(f"M{x + 35},{y + 15}h14M{x + 35},{y + 21}h9", ink, 1.1)]
        o += [circle(x + 42 + 30 * cx, m + 15 * cy, 3.6, c) for (cx, cy), c in
              zip([(0, -1), (1, 0), (0, 1), (-1, 0)], [O, C, Gd, O])]
        o.append(path(f"M{x + 46},{y + 2}c12,0 22,6 24,12M{x + 38},{y + 34}c-12,0 -22,-6 -24,-12", ink, 1, opacity=0.5))
        return "".join(o)
    if kind == "pipes":
        o = [rect(x + 2, y + 1, 14, 10, "none", O, 1.2, 2), path(f"M{x + 2},{y + 6}h14M{x + 9},{y + 1}v10", O, 1),
             circle(x + 8, m, 4, "none", C, 1.4), path(f"M{x + 11},{m + 3}l3,3", C, 1.4),
             path(f"M{x + 2},{y + 27}h9l4,4l-4,4h-9z", Gd, 1.3)]
        o += [path(f"M{x + 20},{yy}C{x + 40},{yy} {x + 40},{m} {x + 58},{m}", c, 1.3)
              for yy, c in [(y + 6, O), (m, C), (y + 31, Gd)]]
        return "".join(o) + path(f"M{x + 58},{m}H{x + 82}", ink, 1.2) + path(f"M{x + 77},{m - 4}l5,4l-5,4", ink, 1.4)
    if kind == "voice":
        o = [rect(x + 3 + i * 7, m - h / 2, 4, h, O if i % 2 else C, rx=2) for i, h in enumerate([8, 18, 28, 14, 22, 10, 6])]
        return "".join(o) + path(f"M{x + 56},{y + 6}h26v16h-16l-6,6v-6h-4z", ink, 1.3) + text(x + 69, y + 18, "hi", ink, 9, 700, "middle", "mono")
    # badge + key
    return (rect(x + 2, y + 2, 34, 32, "none", ink, 1.3, 6) + circle(x + 19, y + 13, 5, O)
            + path(f"M{x + 9},{y + 29}c0,-6 4,-9 10,-9s10,3 10,9", O, 1.5)
            + circle(x + 54, m, 7, "none", Gd, 2) + path(f"M{x + 61},{m}h20M{x + 75},{m}v5M{x + 80},{m}v4", Gd, 2))


def agents(T):
    return grid(T, "How agents actually work", ("The concepts behind ", "every agent I design."), T["crimson"],
                AGENTS, _glyph, (T["warm_a"], T["warm_b"]))
