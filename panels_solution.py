"""'Where AI met the solution': relay rows, PROBLEM -> AI DID -> SOLUTION DID -> OUTCOME."""
from svgkit import (arrowhead, card, chip, circle, dashed, eyebrow, mono_label, paper, para, particle, path, rect,
                    rich, text)
from textfit import wrap

W = 1000

# name, problem, AI did, solution did, business outcome, maturity tag, KPI kind (latest first)
CASES = [
    ("Airline payments desk", "15–30 min manual cases across three systems",
     "Picks the next step and calls the right tool each turn",
     "State kept outside the model, workflow with approvals, integrations to 4 systems",
     "Under 5 min per case (target)", "M3 · L4", "time"),
    ("Enterprise answers", "Answers scattered across CRM, tickets and docs",
     "Text-to-SQL + semantic search + keyword index",
     "16+ connectors with delta sync, field annotations and permissions",
     "Trusted answers from small, permission-aware context", "M1 · L2", "quality"),
    ("Pharma planning", "Monthly production planning done by hand for 20 products",
     "Natural-language planning skills", "ERP and quality data modeled into governed objects",
     "Manual monthly process replaced", "M2 · L3", "time"),
    ("Support & CX agents", "High-volume, repetitive, multilingual queries (BFSI, fintech, mobility)",
     "CX, voice and QA-audit agents", "Knowledge indexing, skill design, evals and escalation",
     "Agents that answer, act and hand off, with QA audit", "M2 · L3", "risk"),
    ("Marketing, 2021–24", "Right message, right user, right time, right channel (BFSI and retail)",
     "Sherpa (now Merlin AI): Best Time to Send, Most Preferred Channel, Predictions, Dynamic A/B",
     "SDKs + Data API + warehouse imports, RFM segments, Flows (journeys)",
     "+50% conversion to proposal stage", "M1–2 · L2", "revenue"),
]
COLS = [("problem", 160), ("ai did", 160), ("solution did", 184), ("business outcome", 140)]
X0, GAP, SIZE, LH = 222, 22, 12, 16


def kpi_icon(T, cx, cy, kind):
    """Clock = time, coin = revenue/cost, shield = risk, check = quality. 18px, centred."""
    kind = "revenue" if kind == "cost" else kind
    c = {"time": T["orange"], "revenue": T["gold"], "risk": T["crimson"], "quality": T["grn2"]}[kind]
    base = circle(cx, cy, 9, "none", c, 1.5)
    if kind == "time":
        return base + path(f"M{cx},{cy - 5}V{cy}H{cx + 4}", c, 1.5)
    if kind == "revenue":
        return base + text(cx, cy + 3.5, "$", c, 10, 800, "middle", "display")
    if kind == "risk":
        return path(f"M{cx},{cy - 9}l7,3v5c0,5 -3,8 -7,10c-4,-2 -7,-5 -7,-10v-5z", c, 1.5)
    return base + path(f"M{cx - 4},{cy}l3,3l5,-6", c, 1.7)


def _styles(T):
    dark = T["name"] == "dark"
    return [(T["paper"], T["card_line"], T["ink2"], 400),
            (T["lav_soft"], T["lav"], T["lav_ink"], 600),
            (T["grn_soft"], T["grn2"] if not dark else "#3D5E1E", T["grn_ink"], 600),
            (T["yellow"], "#D9C92E", "#151515", 800)]


def _row(T, y, i, case):
    name, *cells, tag, kpi = case
    lines = [wrap(c, w - 24, SIZE, 800 if k == 3 else 600) for k, (c, (_, w)) in enumerate(zip(cells, COLS))]
    h = max(max(len(l) for l in lines) * LH + 24, 84)
    o = [card(48, y, 904, h + 20, T, 16),
         mono_label(70, y + 30, f"{i + 1:02d}", T["purple"], 10, "start", 1.2, 700)]
    s, ny = para(70, y + 50, name, T["ink"], 15, 132, 18, 800, font="display")
    c, cw = chip(70, ny + 10, tag, T["ink"] if T["name"] == "light" else "#2E2A42", "#FFFFFF", 9, 20, weight=700,
                 font="mono")
    o += [s, c, kpi_icon(T, 70 + cw + 16, ny + 20, kpi)]
    x, bt = X0, y + 10
    for k, ((_, w), rows, (fill, stroke, ink, wt)) in enumerate(zip(COLS, lines, _styles(T))):
        o.append(rect(x, bt, w, h, fill, stroke, 1.1, 12))
        ty = bt + h / 2 - (len(rows) - 1) * LH / 2 + SIZE * 0.36
        o += [text(x + 12, ty + j * LH, r, ink, SIZE + (0.5 if k == 3 else 0), wt,
                   font="display" if k == 3 else "sans") for j, r in enumerate(rows)]
        if k < 3:
            ax, cy = x + w + 3, bt + h / 2
            o += [dashed([(ax, cy), (ax + GAP - 8, cy)], T["faint"], 1.5, 3, 3), arrowhead(ax + GAP - 5, cy, 0, T["faint"], 4),
                  particle(f"M{ax},{cy} L{ax + GAP - 5},{cy}", 1.2, round(i * 0.3 + k * 0.6, 2), 2.4, T["purple_fill"])]
        x += w + GAP
    return "".join(o), h + 20


def solution(T):
    top, body = 206, []
    y = top
    for i, case in enumerate(CASES):
        s, h = _row(T, y, i, case)
        body.append(s)
        y += h + 12
    H = y + 28
    o = [paper(W, H, T, ((1.02, -0.04, 0.38), (-0.04, 1.03, 0.4))),
         eyebrow(56, 64, "Where AI met the solution", T["purple"]),
         rich(54, 112, [[("The model is a component.", None)], [("The solution is the product.", T["purple"])]],
              T["ink"], 38, 44)]
    x = X0
    tones = [T["muted"], T["purple"], T["grn2"], T["gold"] if T["name"] == "dark" else T["yellow_ink"]]
    for (lab, w), c in zip(COLS, tones):
        o.append(mono_label(x + 2, top - 12, lab, c, 9.5, "start", 1.8, 700))
        x += w + GAP
    return W, H, "".join(o + body)
