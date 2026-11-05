"""Use-case tabs: tab bar (one per active tab), use-case card, and swimlane workflow per use case."""
import re

from panels_solution import kpi_icon
from svgkit import (arrowhead, card, chip, circle, dashed, el, mono_label, paper, para, particle, path, rect, rich,
                    text)
from textfit import tw, wrap
from usecases import TABS

W = 1000
KPI_LABEL = {"time": "time saved", "cost": "cost down", "risk": "risk down", "revenue": "revenue up",
             "quality": "quality up"}


# ------------------------------------------------------------------ tab bar
def tabbtn(T, label, on):
    """One clickable tab button (each is its own image so it can sit inside a link)."""
    h, size = 40, 14
    w = round(tw(label, size, 700) + 40)
    fill, ink, stroke = (T["purple_fill"], "#FFFFFF", T["purple_fill"]) if on else (T["card"], T["ink2"], T["card_line"])
    body = rect(1, 1, w - 2, h - 2, fill, stroke, 1.2, (h - 2) / 2) + text(w / 2, h / 2 + 5, label, ink, size,
                                                                            700, "middle", "display")
    return w, h, body


def accbtn(T, label, count):
    """Accordion summary drawn as a full-width button: industry, count, and a 'click to open' cue."""
    W_, h = 880, 56
    body = [rect(1, 1, W_ - 2, h - 2, T["card"], T["card_line"], 1.2, 16),
            rect(14, 14, 28, 28, T["lav_soft"], None, 1, 8),
            text(28, 33, "+", T["purple"], 18, 800, "middle", "display"),
            text(56, 34, label, T["ink"], 16, 800, font="display", spacing=-0.2)]
    sub = f"{count} use case{'s' if count > 1 else ''}"
    body.append(text(56 + tw(label, 16, 800) + 14, 34, sub, T["muted"], 13, 500))
    body.append(text(W_ - 24, 34, "CLICK TO OPEN", T["purple"], 10, 700, "end", "mono", spacing=1.6))
    return W_, h, "".join(body)


def tabbar(T, active):
    H, gap, h = 72, 8, 38
    widths = [tw(lab, 13.5, 700) + 34 for _, lab in TABS]
    x = (W - sum(widths) - gap * (len(TABS) - 1)) / 2
    o = [rect(0, 0, W, H, T["paper"], rx=22), rect(x - 8, 17, W - 2 * (x - 8), h + 0, T["card"], T["card_line"], 1, (h + 0) / 2)]
    for (slug, lab), w in zip(TABS, widths):
        on = slug == active
        o.append(rect(x, 17 + 4, w, h - 8, T["purple_fill"] if on else "none", None if on else None, 1, (h - 8) / 2))
        o.append(text(x + w / 2, 17 + h / 2 + 4.8, lab, "#FFFFFF" if on else T["ink2"], 13.5, 700 if on else 600,
                      "middle", "display"))
        x += w + gap
    return W, H, "".join(o)


# ------------------------------------------------------------------ use-case card
COLS = [("problem", 196), ("ai did", 196), ("solution did", 214), ("business outcome", 194)]


def _status(outcome):
    o = outcome.lower()
    if "achieved" in o:
        return "achieved"
    if "proposal" in o or "proposed" in o:
        return "proposal"
    if "target" in o:
        return "target"
    return "pilot"


def case_card(T, industry, case, index):
    from panels_solution import _styles
    cells = [case["problem"], case["ai"], case["solution"], case["outcome"]]
    lines = [wrap(c, w - 26, 12.5, 800 if k == 3 else 600) for k, (c, (_, w)) in enumerate(zip(cells, COLS))]
    bh = max(len(l) for l in lines) * 17 + 30
    top = 120
    arch_y = top + 30 + bh + 40
    H = arch_y + 92
    o = [paper(W, H, T, ((1.02, -0.2, 0.3), (-0.04, 1.2, 0.3))),
         mono_label(56, 46, f"— {industry} · use case {index:02d}", T["purple"], 10, "start", 2, 600),
         rich(54, 86, [[(case["use"], None)]], T["ink"], 28, 0, track=-0.025)]
    st = _status(case["outcome"])
    sfill = {"achieved": T["grn"], "target": T["yellow"], "proposal": T["bubbles"]["peach"][0],
             "pilot": T["bubbles"]["sky"][0]}[st]
    sink = {"achieved": "#0F4C00", "target": "#151515", "proposal": T["bubbles"]["peach"][1],
            "pilot": T["bubbles"]["sky"][1]}[st]
    a, aw = chip(944, 30, st, sfill, sink, 9.5, 26, weight=700, anchor="end", font="mono")
    b, bw = "", -8  # maturity tags retired with the generic journey curve
    kx = 944 - aw - bw - 16
    lab = KPI_LABEL[case["kpi"]]
    lw = tw(lab, 12, 600)
    o += [a, b, kpi_icon(T, kx - lw - 22, 43, case["kpi"]), text(kx - lw - 8, 47.5, lab, T["ink2"], 12, 600)]
    x = 48
    for k, ((name, w), rows, (fill, stroke, ink, wt)) in enumerate(zip(COLS, lines, _styles(T))):
        o.append(mono_label(x + 2, top + 18, name, [T["muted"], T["purple"], T["grn2"], T["yellow_ink"] if
                                                  T["name"] == "light" else T["gold"]][k], 9, "start", 1.6, 700))
        o.append(rect(x, top + 30, w, bh, fill, stroke, 1.1, 14))
        ty = top + 30 + bh / 2 - (len(rows) - 1) * 8.5 + 4.5
        o += [text(x + 13, ty + j * 17, r, ink, 12.5 + (0.5 if k == 3 else 0), wt,
                   font="display" if k == 3 else "sans") for j, r in enumerate(rows)]
        if k < 3:
            cy = top + 30 + bh / 2
            o += [dashed([(x + w + 2, cy), (x + w + 10, cy)], T["faint"], 1.5, 3, 2.5),
                  arrowhead(x + w + 12, cy, 0, T["faint"], 4)]
        x += w + 16
    o.append(_arch(T, arch_y, case["arch"]))
    return W, H, "".join(o)


def _arch(T, y, nodes):
    o = [mono_label(56, y - 12, "architecture", T["muted"], 9, "start", 1.6, 700)]
    n, gap = len(nodes), 26
    nw = (904 - gap * (n - 1)) / n
    for i, lab in enumerate(nodes):
        x = 48 + i * (nw + gap)
        rows = wrap(lab, nw - 20, 11.5, 600)[:3]
        o += [card(x, y, nw, 58, T, 12), rect(x + 12, y - 1, nw - 24, 3, T["grn"] if i % 2 == 0 else T["ink"], rx=1.5)]
        ty = y + 29 - (len(rows) - 1) * 7.5 + 4
        o += [text(x + nw / 2, ty + j * 15, r, T["ink"], 11.5, 600, "middle") for j, r in enumerate(rows)]
        if i < n - 1:
            cy = y + 29
            o += [dashed([(x + nw + 4, cy), (x + nw + gap - 8, cy)], T["faint"], 1.5, 3, 3),
                  arrowhead(x + nw + gap - 5, cy, 0, T["faint"], 4),
                  particle(f"M{x + nw + 4:.1f},{cy} L{x + nw + gap - 5:.1f},{cy}", 1.3, round(i * 0.5, 2), 2.4,
                           T["purple_fill"])]
    return "".join(o)


# ------------------------------------------------------------------ workflow swimlanes
LANES = ["User", "Agent / skills", "Systems", "Human"]
LANE_OF = {"TRIGGER": 0, "USER": 0, "AGENT": 1, "SKILL": 1, "GUARDRAIL": 1, "WORKFLOW": 2, "SYSTEM": 2,
           "HUMAN": 3}


def actor_colours(T):
    teal = "#0F766E" if T["name"] == "light" else "#2DD4BF"
    return {"User": T["ink2"], "Agent / skills": T["purple_fill"], "Systems": teal, "Human": T["orange"],
            "GUARDRAIL": T["crimson"], "OUTCOME": T["yellow"]}


def _gate(x, y, c):
    return path(f"M{x},{y + 10}V{y}M{x + 12},{y + 10}V{y}M{x - 2},{y + 3}H{x + 14}", c, 1.6)


def _shield(x, y, c):
    return path(f"M{x + 6},{y}l6,2.5v4c0,4 -3,6 -6,7c-3,-1 -6,-3 -6,-7v-4z", c, 1.4, fill="none")


LOOP = {"TRIGGER": 2, "USER": 2, "SYSTEM": 3, "WORKFLOW": 4, "AGENT": 4, "SKILL": 4, "DECISION": 4,
        "GUARDRAIL": 5, "HUMAN": 5, "OUTCOME": 7}


def loop_step(actor, txt):
    """Which step of 'my approach' (1-7) a workflow step instantiates."""
    if actor in ("HUMAN", "SYSTEM") and re.search(r"\bQA\b|harness|shadow|eval|score", txt):
        return 6
    return LOOP.get(actor, 4)


def split_step(actor, txt):
    """(headline, no-branch) for display; full text stays in alt/details."""
    if actor == "DECISION":
        q = txt.split("?")[0].strip() + "?"
        clean = lambda v: re.sub(r"\[(\w+)\]", lambda k: k.group(1).lower(), v.strip(" /"))
        yes = re.search(r"\byes\s*→\s*(.+?)(?:\s/\s*no\s*→|$)", txt)
        no = re.search(r"\bno\s*→\s*(.+)$", txt)
        return q, (clean(yes.group(1)) if yes else "", clean(no.group(1)) if no else "")
    return txt.split("→")[0].strip(), ("", "")


def _branches(branch, next_no):
    """(label on the forward connector, text for the side stub)."""
    yes, no = branch
    nxt = f"step {next_no}"
    if no.startswith(nxt) and not yes.startswith(nxt):
        return "no", ("yes → " + yes) if yes else ""
    return "yes", ("no → " + no) if no else ""


def workflow(T, title, wf):
    steps = [(a.upper(), t) for a, t in wf["steps"]]
    cols = 6 if len(steps) > 6 else len(steps)
    nrows = -(-len(steps) // cols)
    lh, lab_w = 82, 92
    cw = (904 - lab_w) / cols
    top = 120
    lanes_of = []
    for r in range(nrows):
        used = set()
        prev = None
        for i, (actor, _) in enumerate(steps[r * cols:(r + 1) * cols]):
            ln = LANE_OF.get(actor, prev if prev is not None else 1)
            used.add(ln)
            prev = ln
        lanes_of.append(sorted(used))
    row_tops, y = [], top
    for used in lanes_of:
        row_tops.append(y)
        y += len(used) * lh + 34
    H = y + 36
    C = actor_colours(T)
    o = [paper(W, H, T, ((1.02, -0.2, 0.3), (-0.04, 1.2, 0.3))),
         mono_label(56, 44, f"— solution workflow · {wf.get('type', 'workflow')}", T["purple"], 10, "start", 2, 600),
         rich(54, 82, [[(title, None)]], T["ink"], 24, 0, track=-0.02)]
    legend_x = 944
    for lab, col in [("loop step", T["purple"]), ("guardrail", C["GUARDRAIL"]), ("outcome", C["OUTCOME"])][::-1]:
        lw = tw(lab, 10, 500, True, 1) + 18
        o += [circle(legend_x - lw, 78, 5, col), mono_label(legend_x - lw + 10, 81.5, lab, T["muted"], 8.5, "start", 1)]
        legend_x -= lw + 16
    pos = []
    for i, (actor, txt) in enumerate(steps):
        r, c = divmod(i, cols)
        lane = LANE_OF.get(actor, pos[-1][2] if pos else 1)
        if actor == "OUTCOME":
            lane = pos[-1][2] if pos else 3
        slot = lanes_of[r].index(lane)
        pos.append((48 + lab_w + c * cw + 8, row_tops[r] + slot * lh + 9, lane, r, actor, txt))
    for r in range(nrows):
        ry = row_tops[r]
        for k, li in enumerate(lanes_of[r]):
            lane = LANES[li]
            ly = ry + k * lh
            o += [rect(48, ly, 904, lh - 4, T["card"] if k % 2 == 0 else T["paper"], T["card_line"], 1, 10),
                  rect(48, ly, 5, lh - 4, C[lane], rx=2.5)]
            s, _ = para(62, ly + lh / 2 - 2, lane.upper(), C[lane] if lane != "User" else T["muted"], 8.5, 70, 11, 700,
                        font="mono")
            o.append(s)
    nw, nh = cw - 16, lh - 22
    for i, (x, y, lane, r, actor, txt) in enumerate(pos):
        colour = C["GUARDRAIL"] if actor == "GUARDRAIL" else C[LANES[lane]]
        head, branch = split_step(actor, txt)
        fwd, stub = _branches(branch, i + 2) if actor == "DECISION" else ("yes", "")
        if i < len(pos) - 1:
            nx, ny, *_ = pos[i + 1]
            if pos[i + 1][3] == r:
                x1, y1, x2, y2 = x + nw, y + nh / 2, nx, ny + nh / 2
                mid = x2 - 8
                o.append(dashed([(x1 + 2, y1), (mid, y1), (mid, y2), (x2 - 4, y2)], T["faint"], 1.4, 4, 3))
                o.append(arrowhead(x2 - 2, y2, 0, T["faint"], 4))
                if actor == "DECISION":
                    o.append(mono_label(x1 + 3, y1 - 5, fwd, T["grn2"], 8, "start", 0.5, 700))
            else:
                o.append(mono_label(x + nw, y + nh + 13, "continues below ↓", T["faint"], 7.5, "end", 0.6))
        tag = loop_step(actor, txt)
        if actor == "DECISION":
            cx, cy = x + nw / 2, y + nh / 2
            o.append(el("path", d=f"M{cx:.1f},{y - 6:.1f}L{x + nw:.1f},{cy:.1f}L{cx:.1f},{y + nh + 6:.1f}L{x:.1f},{cy:.1f}Z",
                        fill=T["card"], stroke=T["purple_fill"], stroke_width=1.6))
            rows = wrap(head, nw - 46, 10, 600)[:3]
            o += [text(cx, cy - (len(rows) - 1) * 6 + 3.5 + j * 12, rw, T["ink"], 10, 600, "middle")
                  for j, rw in enumerate(rows)]
            if stub:
                nrow = wrap(stub, nw + 6, 8.5, 600)[:2]
                o += [text(x - 2, y + nh + 18 + j * 10.5, rw, T["crimson"], 8.5, 600) for j, rw in enumerate(nrow)]
        else:
            out = actor == "OUTCOME"
            o += [rect(x, y, nw, nh, T["yellow"] if out else T["card"], None if out else colour, 1.4, 10),
                  "" if out else rect(x, y + 7, 3, nh - 14, colour, rx=1.5),
                  text(x + 10, y + 14, f"{i + 1:02d} · {actor.lower()}", "#5C5200" if out else colour, 7.5, 700,
                       font="mono", spacing=0.6)]
            fs, lh2, cap = (9.5, 10.5, 4) if out else (10.5, 12.5, 3)
            full = wrap(head, nw - 18, fs, 700 if out else 400)
            rows = full[:cap]
            if len(full) > cap:
                rows[-1] = rows[-1].rstrip(".,;:") + "…"
            o += [text(x + 10, y + (24 if out else 27) + j * lh2, rw, "#151515" if out else T["ink"], fs, 700 if out else 400)
                  for j, rw in enumerate(rows)]
            if actor == "GUARDRAIL":
                o.append(_shield(x + nw - 34, y + 4, C["GUARDRAIL"]))
            if actor == "HUMAN" and re.search(r"approv|confirm|review", txt, re.I):
                o.append(_gate(x + nw - 36, y + 4, C["Human"]))
        bx, by = x + nw - 9, y + 0 if actor != "DECISION" else y + 2
        o += [circle(bx, by + 9, 7.5, T["purple_fill"]), text(bx, by + 12.3, str(tag), "#FFFFFF", 9, 800, "middle", "display")]
    return W, H, "".join(o)
