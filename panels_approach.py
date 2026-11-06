"""'My approach': the 7-step problem-solving loop as a relay loop."""
from svgkit import (arrowhead, card, chip, circle, cubic, dashed, eyebrow, mono_label, para, paper, particle, path,
                    rect, rich, text)
from textfit import tw

W = 1000

STEPS = [
    ("Find the pain and baseline it", "minutes, cost, risk", "target"),
    ("Map the process and systems", "who, what, where the data lives", "map"),
    ("Unify the context", "connectors, governed objects, annotations", "stack"),
    ("Design the agent", "skills, tools, prompt contract, state outside the model", "agent"),
    ("Guardrails and humans at the right gates", "approvals, hard blocks, escalation", "gate"),
    ("Prove it before go-live", "shadow run, evals, targets", "check"),
    ("Measure the outcome, then expand", "time, cost, revenue, risk", "chart"),
]
INSTANCES = [("Airlines", "3 systems, human confirm gates"), ("BFSI & Fintech", "authority block, tenant isolation"),
             ("Retail & D2C", "4 systems unified, ~76% deflection"), ("Automotive", "≤3 taps, no re-asking"),
             ("Pharma", "shadow run, zero-violation guardrail"), ("IT services", "P1/P2 hard block, confirm gates"),
             ("Marketing", "event data → segments → journeys")]


def _glyph(kind, x, y, c, bg):
    cx, cy = x + 15, y + 15
    g = {
        "target": circle(cx, cy, 9, "none", c, 1.6) + circle(cx, cy, 4.5, "none", c, 1.6) + circle(cx, cy, 1.6, c),
        "map": path(f"M{cx - 9},{cy - 6}l6,-2l6,2l6,-2v12l-6,2l-6,-2l-6,2zM{cx - 3},{cy - 8}v12M{cx + 3},{cy - 6}v12", c, 1.4),
        "stack": path(f"M{cx},{cy - 9}l9,4.5l-9,4.5l-9,-4.5zM{cx - 9},{cy + 1}l9,4.5l9,-4.5M{cx - 9},{cy + 5.5}l9,4.5l9,-4.5", c, 1.4),
        "agent": rect(cx - 9, cy - 7, 18, 14, "none", c, 1.6, 4) + circle(cx - 3.5, cy, 1.8, c) + circle(cx + 3.5, cy, 1.8, c)
        + path(f"M{cx},{cy - 7}v-3", c, 1.6),
        "gate": path(f"M{cx - 8},{cy + 9}V{cy - 7}M{cx + 8},{cy + 9}V{cy - 7}M{cx - 10},{cy - 3}H{cx + 10}M{cx - 10},{cy + 3}H{cx + 10}", c, 1.6),
        "check": path(f"M{cx},{cy - 9}l8,3v5c0,5 -3.5,8 -8,9.5c-4.5,-1.5 -8,-4.5 -8,-9.5v-5zM{cx - 4},{cy}l3,3l5,-6", c, 1.5),
        "chart": path(f"M{cx - 9},{cy + 8}H{cx + 9}M{cx - 6},{cy + 8}V{cy + 2}M{cx},{cy + 8}V{cy - 3}M{cx + 6},{cy + 8}V{cy - 8}", c, 2),
    }
    return rect(x, y, 30, 30, bg, rx=8) + g[kind]


def _step(T, x, y, w, h, i, title, desc, kind):
    last = i == len(STEPS) - 1
    o = [card(x, y, w, h, T, 16, T["lav_soft"] if last else None, T["purple_fill"] if last else None),
         text(x + 18, y + 44, f"{i + 1}", T["purple"], 34, 800, font="display", spacing=-1),
         _glyph(kind, x + w - 48, y + 18, T["lime"], T["ms_fill"] if T["name"] == "light" else "#2E2A42")]
    s, yy = para(x + 18, y + 76, title, T["ink"], 15, w - 36, 18.5, 800, font="display")
    o.append(s)
    s, _ = para(x + 18, yy + 21, desc, T["muted"], 12, w - 36, 16)
    o.append(s)
    return "".join(o)


def approach(T):
    w, h, g = 208, 166, 24
    top1, top2 = 168, 168 + h + 46
    xs1 = [48 + k * (w + g) for k in range(4)]
    xs2 = [xs1[3] - k * (w + g) for k in range(3)]  # 5, 6, 7 run right to left under 4, 3, 2
    o = [paper(W, 760, T, ((1.02, -0.04, 0.4), (-0.04, 1.03, 0.42))),
         eyebrow(56, 64, "My approach", T["purple"]),
         rich(54, 116, [[("Every build follows the same ", None), ("problem-solving loop.", T["purple"])]], T["ink"],
              38, 44)]
    pos = [(x, top1) for x in xs1] + [(x, top2) for x in xs2]
    # connectors first, so cards sit on top
    for i in range(len(pos) - 1):
        (x1, y1), (x2, y2) = pos[i], pos[i + 1]
        if y1 == y2:
            a, b = (x1 + w + 4, y1 + h / 2), (x2 - 4, y2 + h / 2)
            if x2 < x1:
                a, b = (x1 - 4, y1 + h / 2), (x2 + w + 4, y2 + h / 2)
            o += [dashed([a, b], T["purple"], 1.6, 4, 3.5, 0.7), arrowhead(b[0], b[1], 0 if x2 > x1 else 180, T["purple"], 5)]
            o.append(particle(f"M{a[0]:.0f},{a[1]:.0f} L{b[0]:.0f},{b[1]:.0f}", 1.2, round(i * 0.5, 1), 3, T["purple_fill"]))
        else:
            a, b = (x1 + w / 2, y1 + h + 4), (x2 + w / 2, y2 - 4)
            o += [dashed([a, b], T["purple"], 1.6, 4, 3.5, 0.7), arrowhead(b[0], b[1], 90, T["purple"], 5)]
    # loop back: 7 -> 1, around the left
    (x7, y7), (x1_, y1_) = pos[6], pos[0]
    pts = cubic((x7 - 4, y7 + h / 2), (x7 - 60, y7 + h / 2), (x1_ + w / 2 - 40, y1_ + h + 60), (x1_ + w / 2, y1_ + h + 4), 50)
    o += [dashed(pts, T["purple"], 1.6, 4, 3.5, 0.7), arrowhead(x1_ + w / 2, y1_ + h + 4, -90, T["purple"], 5),
          mono_label(x1_ + 24, y7 + h / 2 + 4, "run again →", T["purple"], 8.5, "start", 1.2, 700)]
    for i, ((x, y), (title, desc, kind)) in enumerate(zip(pos, STEPS)):
        o.append(_step(T, x, y, w, h, i, title, desc, kind))
    H = top2 + h + 46
    o[0] = paper(W, H, T, ((1.02, -0.04, 0.4), (-0.04, 1.03, 0.42)))
    return W, H, "".join(o)
