"""Hero (animated context constellation + acting agent) and the big-numbers strip."""
import math

from svgkit import (anim, arrowhead, card, chip, chip_row, circle, cubic, dashed, dotted, el, eyebrow, glow,
                    mono_label, para, paper, particle, path, ping, rect, rich, text)
from textfit import tw

W = 1000
SUN_INK = "#151515"  # text on the yellow core, both themes


# ------------------------------------------------------------------ hero
ORBIT = [(160, "Knowledge", "lime"), (205, "ERP", "lilac"), (250, "CRM", "sky"), (290, "Ticketing", "yellow"),
         (335, "HR", "peach"), (20, "Commerce", "mint"), (60, "Logistics", "lilac"), (120, "Voice", "pink")]
ACTIONS = ["deflect", "resolve", "automate"]


def _hero_left(T):
    o = [eyebrow(56, 92, "Shivaji M D · Enterprise AI Solutions Advisor · Bengaluru", T["purple"], 11, 2.0)]
    P = T["purple"]
    o.append(rich(54, 168, [[("I turn enterprise", None)], [("context", P), (" into AI", None)],
                            [("that ", None), ("acts.", P)]], T["ink"], 54, 60))
    s, _ = para(56, 338, "13+ years in SaaS. I take enterprise use cases from CXO discovery to production "
                "AI agents: the context layer first, then guarded multi-agent workflows on top.",
                T["ink2"], 16.5, 470, 25)
    o.append(s)
    b = T["bubbles"]
    row, _ = chip_row(56, 430, [("Context engineering", *b["lilac"]), ("Multi-agent workflows", *b["lime"]),
                                ("16+ production connectors", *b["yellow"])], gap=8, size=12.5, h=32)
    o.append(row)
    return "".join(o)


def _hero_core(T, cx, cy):
    o = [glow(cx, cy, 118, T["yellow"], 0.55 if T["name"] == "light" else 0.35, 16)]
    for i in range(16):  # sun spokes, deck "Shared Memory" style
        a = math.radians(i * 22.5 + 11)
        x1, y1 = cx + 60 * math.cos(a), cy + 60 * math.sin(a)
        x2, y2 = cx + (76 if i % 2 else 70) * math.cos(a), cy + (76 if i % 2 else 70) * math.sin(a)
        o.append(path(f"M{x1:.1f},{y1:.1f}L{x2:.1f},{y2:.1f}", T["gold"], 1.2, opacity=0.7))
        if i % 2:
            o.append(circle(x2, y2, 2.2, T["card"], T["gold"], 1))
    o += [ping(cx, cy, 52, 92, T["gold"], 3.2, "0s"), ping(cx, cy, 52, 92, T["gold"], 3.2, "1.6s"),
          circle(cx, cy, 52, T["yellow"], "#E2D21F", 1.5),
          text(cx, cy - 2, "enterprise", SUN_INK, 14.5, 800, "middle", "display", spacing=-0.3),
          text(cx, cy + 15, "context", SUN_INK, 14.5, 800, "middle", "display", spacing=-0.3),
          mono_label(cx, cy + 31, "shared memory", SUN_INK, 7, "middle", 1.2, 600)]
    return "".join(o)


def _hero_orbit(T, cx, cy, rx=140, ry=122):
    ring = [(cx + rx * math.cos(math.radians(a)), cy + ry * math.sin(math.radians(a))) for a in range(0, 361, 3)]
    o, kids = [dotted(ring, T["lav"], 1.2, 8, 0.9)], []
    for i, (ang, label, tone) in enumerate(ORBIT):
        a = math.radians(ang)
        bx, by = cx + rx * math.cos(a), cy + ry * math.sin(a)
        sx, sy = cx + 64 * math.cos(a), cy + 64 * math.sin(a)
        ex, ey = bx - 22 * math.cos(a), by - 16 * math.sin(a)
        o.append(dotted([(ex, ey), (sx, sy)], T["purple"], 1.3, 7, 0.55))
        o.append(particle(f"M{ex:.1f},{ey:.1f} L{sx:.1f},{sy:.1f}", 2.4, round(i * 0.37, 2), 2.8, T["purple"]))
        fill, ink = T["bubbles"][tone]
        s, _ = chip(bx, by - 16, label, fill, ink, 13, 32, weight=600, anchor="middle")
        float_ = el("animateTransform", attributeName="transform", type="translate",
                    values=f"0 0;0 {-3 if i % 2 else 3};0 0", dur=f"{4 + i % 3}s", repeatCount="indefinite")
        kids.append(el("g", s + float_))
    return "".join(o + kids)


def _hero_agent(T, cx, top):
    P, G = T["purple_fill"], T["grn2"]
    ay = top + 92
    o = [path(f"M{cx},{top}L{cx},{ay - 20}", P, 2),
         particle(f"M{cx},{top} L{cx},{ay - 20}", 1.6, 0, 3, P),
         particle(f"M{cx},{top} L{cx},{ay - 20}", 1.6, 0.8, 3, P),
         mono_label(cx + 10, top + 42, "permission-aware", T["muted"], 8.5, "start", 1.4)]
    s, w = chip(cx, ay - 20, "agent", P, "#FFFFFF", 15, 40, weight=800, dot=T["lime"], anchor="middle",
                font="display")
    o.append(ping(cx, ay, 20, 44, T["purple"], 2.6, "0.4s", 2) + s)
    xs = [cx - 136, cx, cx + 128]
    for i, (x, lab) in enumerate(zip(xs, ACTIONS)):
        pts = cubic((cx, ay + 20), (cx, ay + 44), (x, ay + 30), (x, ay + 60), 40)
        d = f"M{cx},{ay + 20} C{cx},{ay + 44} {x},{ay + 30} {x},{ay + 60}"
        o += [dashed(pts, G, 1.5, 5, 4), arrowhead(x, ay + 61, 90, G),
              particle(d, 1.8, round(1.2 + i * 0.5, 2), 2.6, G)]
        c, cw = chip(x, ay + 64, lab, T["card"], T["ink"], 12.5, 30, T["card_line"], 600, dot=G, anchor="middle")
        o.append(el("g", c + anim("opacity", "1;1;0.55;1", 3.6, f"{1.4 + i * 0.5}s", "0;0.5;0.62;1")))
    return "".join(o)


def hero(T):
    H, cx, cy = 560, 792, 228
    body = paper(W, H, T) + _hero_left(T) + _hero_core(T, cx, cy) + _hero_orbit(T, cx, cy) + _hero_agent(T, cx, cy + 52 + 70)
    return W, H, body


# ------------------------------------------------------------------ metrics
METRICS = [("<5", " min", "per airline payments-desk case, down from 15–30 (target)"),
           ("16+", "", "systems unified into one governed context"),
           ("+50%", "", "conversion to proposal stage at MoEngage"),
           ("70+", "", "BFSI projects: banks, NBFCs, insurers, fintechs"),
           ("13+", " yrs", "in SaaS: engineering, customer success, presales, AI solutions")]


def metrics(T):
    H, size = 320, 50
    o = [paper(W, H, T, ((1.0, -0.2, 0.3), (-0.02, 1.2, 0.3))), eyebrow(56, 64, "By the numbers", T["purple"])]
    o.append(rich(54, 114, [[("Every build, projected to a ", None), ("business outcome.", T["purple"])]],
                  T["ink"], 36, 40))
    widths = [max((tw(n, size, 800) + tw(s, 26, 800)) * 1.12, 150) for n, s, _ in METRICS]
    gap = (888 - sum(widths)) / (len(METRICS) - 1)
    x = 56
    for i, ((num, suf, cap), w) in enumerate(zip(METRICS, widths)):
        o.append(rich(x - 2, 214, [[(num, None)]], T["purple"], size, 0, font="display", track=-0.04))
        if suf:
            o.append(text(x + tw(num, size, 800) * 0.97, 214, suf, T["purple"], 26, 800, font="display"))
        s, _ = para(x, 246, cap, T["muted"], 13.5, w, 19)
        o.append(s)
        if i:
            o.append(el("line", x1=round(x - gap / 2, 1), y1=158, x2=round(x - gap / 2, 1), y2=292,
                        stroke=T["line"], stroke_width=1))
        x += w + gap
    return W, H, "".join(o)
