"""Engagement staircase (9 blocks: Why / Build / Ship & prove) and the grouped stack chips."""
from svgkit import (anim, arrowhead, card, chip, chip_flow, circle, cubic, dashed, dotted, el, eyebrow, mono_label,
                    para, paper, path, rect, rich, text)

W = 1000

# group, tone, note under the column, [(block, question)] listed bottom-up
COLUMNS = [
    ("Why", "lilac", "outcomes with a baseline and an owner",
     [("Business value", "Which outcome, measured how?"), ("Use-case portfolio", "Value × feasibility × readiness")]),
    ("Build", "lime", "numbers by rules, words by model",
     [("Data foundation", "Connectors, grain, deltas, quality"), ("Knowledge & memory", "Graph, vectors, KB, annotations"),
      ("Agents", "Skills and tools that act")]),
    ("Ship & prove", "yellow", "measurement feeds the next use case",
     [("Governance", "RBAC, audit, evals, guardrails"), ("Delivery", "Shadow run, gated go-live"),
      ("Adoption", "Meet users in their channels"), ("Measurement", "Business, AI and data KPIs")]),
]


def method(T):
    H, base = 640, 576
    o = [paper(W, H, T, ((1.02, -0.08, 0.36), (-0.04, 1.08, 0.38))),
         eyebrow(56, 64, "How I run an engagement", T["purple"]),
         rich(54, 112, [[("Justify top-down. ", None), ("Build bottom-up.", T["purple"])]], T["ink"], 38, 40)]
    cw, ch, cg, colgap = 282, 54, 8, 29
    bottoms = [base - 16, base - 72, base - 128]
    tops, n = [], 0
    for ci, (group, tone, note, blocks) in enumerate(COLUMNS):
        x = 48 + ci * (cw + colgap)
        bottom = bottoms[ci]
        top = bottom - len(blocks) * (ch + cg) + cg
        fill, ink = T["bubbles"][tone]
        # pedestal: the stair riser under each column
        o.append(rect(x, bottom + 8, cw, base - bottom - 8 + 24, fill, rx=14, opacity=0.55))
        if base - bottom > 40:
            s, _ = para(x + cw / 2, bottom + 40, note, ink, 12, cw - 40, 16, 600, "middle")
            o.append(s)
        else:
            o.append(text(x + cw / 2, base + 12, note, ink, 12, 600, "middle"))
        o += [mono_label(x + 2, top - 16, f"0{ci + 1} · {group}", T["purple"], 10.5, "start", 2, 600)]
        tops.append((x + cw / 2, top - 34))
        for bi, (name, q) in enumerate(blocks):
            n += 1
            y = bottom - (bi + 1) * ch - bi * cg
            o += [card(x, y, cw, ch, T, 12),
                  circle(x + 26, y + ch / 2, 13, fill),
                  text(x + 26, y + ch / 2 + 4.5, str(n), ink, 12.5, 800, "middle", "display"),
                  circle(x + 26, y + ch / 2, 16, "none", T["purple"], 1.6, opacity=0,
                         kids=anim("opacity", "0;1;0;0", 9, f"{(n - 1)}s", "0;0.05;0.12;1")),
                  text(x + 50, y + 23, name, T["ink"], 14.5, 700, font="display", spacing=-0.2),
                  text(x + 50, y + 41, q, T["muted"], 12)]
    # dotted ascent over the column tops
    (_, y1), (_, y2), (_, y3) = tops
    xa, xb = 48 + cw + colgap / 2, 48 + 2 * cw + 1.5 * colgap
    stair = [(48, y1), (xa, y1), (xa, y2), (xb, y2), (xb, y3), (948, y3)]
    o.append(dotted(stair, T["purple"], 1.7, 9, 0.7))
    o.append(arrowhead(952, y3, 0, T["purple"], 6))
    return W, H, "".join(o)


# ------------------------------------------------------------------ stack
GROUPS = [("Agents & AI", "lilac", ["Multi-agent orchestration", "LLM agent design", "Voice agents",
                                    "Evals & guardrails", "Claude Code"]),
          ("Context & integration", "lime", ["MCP", "REST", "Webhooks", "Connectors / ETL", "Knowledge graphs",
                                             "DevRev AirSync"]),
          ("Languages", "yellow", ["Python", "SQL", "TypeScript", "JavaScript", "HTML / CSS"]),
          ("Solution craft", "peach", ["CXO discovery", "Solution architecture", "RFP responses", "Pricing & ROI models",
                                       "POC → production"])]


def stack(T):
    o, y = [], 150
    rows = []
    for label, tone, items in GROUPS:
        fill, ink = T["bubbles"][tone]
        s, h = chip_flow(270, y, items, 674, fill, ink, size=13, h=32, gap=10)
        rows.append((label, y, s))
        y += h + 26
    H = y + 18
    o = [paper(W, H, T, ((1.02, -0.2, 0.32), (-0.04, 1.2, 0.32))), eyebrow(56, 64, "Stack", T["purple"]),
         rich(54, 112, [[("Tools I reach for. ", None), ("Context first.", T["purple"])]], T["ink"], 38, 40)]
    for i, (label, yy, s) in enumerate(rows):
        o += [mono_label(56, yy + 20, label, T["muted"], 10, "start", 1.8, 600), s]
        if i:
            o.append(el("line", x1=56, y1=yy - 13, x2=944, y2=yy - 13, stroke=T["line"], stroke_width=1))
    return W, H, "".join(o)


# ------------------------------------------------------------------ writing strip
ARTICLE = ("Your AI agent doesn't have a knowledge problem. It has a noise problem.",
           "Why agents stumble on noisy context rather than missing knowledge, and how precise, "
           "permission-aware retrieval fixes it.", "LinkedIn article · Apr 2026")


def writing(T):
    H = 176
    title, summary, meta = ARTICLE
    o = [paper(W, H, T, ((1.02, -0.4, 0.26), (-0.04, 1.4, 0.26))),
         eyebrow(56, 46, "Writing", T["purple"]),
         rich(54, 86, [[(title, None)]], T["ink"], 22, 0, track=-0.02)]
    s, sy = para(56, 114, summary, T["muted"], 13.5, 640, 19)
    o.append(s)
    o.append(mono_label(56, sy + 26, meta, T["faint"], 9, "start", 1.4))
    c, w = chip(944, 96, "Read on LinkedIn →", T["purple_fill"], "#FFFFFF", 13, 34, weight=700, anchor="end")
    return W, H, "".join(o) + c
