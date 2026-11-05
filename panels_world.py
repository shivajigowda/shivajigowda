"""Constellation of industries (bubbles sized by depth) and the purple 'Why work with me?' panel."""
import math

from svgkit import (anim, chip, circle, dashed, dotted, el, eyebrow, glow, mono_label, para, paper, particle, path,
                    rect, rich, text)
from textfit import tw

W = 1000

# name, cx, cy, r, tone, [(use case, angle deg, distance from edge)]
BUBBLES = [
    ("BFSI", 214, 352, 86, "lilac",
     [("Lending & eKYC", 225, 26), ("Debt recovery", 290, 24), ("CX & voice agents", 122, 30),
      ("QA-audit agents", 58, 22)]),
    ("Retail / D2C", 480, 246, 64, "lime",
     [("50+ FMCG accounts", 196, 20), ("Commerce data in one graph", 270, 16)]),
    ("Aviation", 752, 300, 76, "sky",
     [("Multi-agent re-booking", 292, 18), ("15–30 → <5 min", 0, 20)]),
    ("Logistics", 430, 470, 56, "peach",
     [("Shipment tracking", 150, 26), ("Returns connectors", 100, 30)]),
    ("IT services", 646, 478, 58, "mint",
     [("Self-service agent", 90, 22)]),
    ("Pharma", 878, 456, 50, "pink",
     [("ERP + QA → planning", 262, 20), ("20 products", 90, 22)]),
]
CORE = (560, 360)


def _usecase(T, cx, cy, r, label, ang, dist):
    a = math.radians(ang)
    ex, ey = cx + r * math.cos(a), cy + r * math.sin(a)
    px, py = cx + (r + dist) * math.cos(a), cy + (r + dist) * math.sin(a)
    c = math.cos(a)
    anchor = "middle" if abs(c) < 0.35 else ("start" if c > 0 else "end")
    h = 24
    y = py - h / 2 + (0 if abs(c) >= 0.35 else (-h / 2 if math.sin(a) < 0 else h / 2))
    s, w = chip(px, y, label, T["card"], T["ink2"], 11.5, h, T["card_line"], 500, anchor=anchor)
    return path(f"M{ex:.1f},{ey:.1f}L{px:.1f},{py:.1f}", T["faint"], 1, opacity=0.8) + s


def constellation(T):
    H = 640
    o = [paper(W, H, T, ((1.02, -0.06, 0.36), (-0.04, 1.08, 0.38))),
         eyebrow(56, 64, "Where I've applied it", T["purple"]),
         rich(54, 112, [[("Six industries. ", None), ("One context-first pattern.", T["purple"])]], T["ink"], 38, 40)]
    cx0, cy0 = CORE
    for i, (name, cx, cy, r, tone, _) in enumerate(BUBBLES):
        dx, dy = cx - cx0, cy - cy0
        dlen = math.hypot(dx, dy)
        sx, sy = cx0 + dx / dlen * 34, cy0 + dy / dlen * 34
        ex, ey = cx - dx / dlen * (r + 4), cy - dy / dlen * (r + 4)
        o.append(dashed([(sx, sy), (ex, ey)], T["purple"], 1.3, 4, 4, 0.55))
        o.append(particle(f"M{sx:.1f},{sy:.1f} L{ex:.1f},{ey:.1f}", 2.2, round(i * 0.45, 2), 2.6, T["purple"]))
    o += [glow(cx0, cy0, 64, T["yellow"], 0.5 if T["name"] == "light" else 0.3, 12),
          circle(cx0, cy0, 32, T["core_fill"]),
          text(cx0, cy0 - 1, "context", T["core_text"], 11.5, 800, "middle", "display"),
          text(cx0, cy0 + 12, "first", T["core_text"], 11.5, 800, "middle", "display")]
    for i, (name, cx, cy, r, tone, uses) in enumerate(BUBBLES):
        fill, ink = T["bubbles"][tone]
        for lab, ang, dist in uses:
            o.append(_usecase(T, cx, cy, r, lab, ang, dist))
        breathe = anim("r", f"{r};{r + 2.5};{r}", 4 + i % 3, f"{i * 0.4:.1f}s")
        size = max(14, min(22, r / 3.6))
        o += [circle(cx, cy, r, fill, kids=breathe),
              text(cx, cy + size * 0.36, name, ink, size, 800, "middle", "display", spacing=-0.3)]
    o.append(mono_label(944, 616, "bubble size = depth of work", T["muted"], 9, "end", 1.6))
    return W, H, "".join(o)


# ------------------------------------------------------------------ statement
PROOFS = ["16+ production connectors", "15–30 → <5 min per case (target)", "Shadow run first, gated go-live"]


def statement(T):
    H = 380
    base = "#4A16D6" if T["name"] == "light" else "#3B12AE"
    clip = el("g", glow(-60, H / 2, 620, "#24096E", 0.85, 18)
              + glow(W + 40, -40, 560, "#9B6EFF", 0.7, 18)
              + glow(80, H + 60, 340, "#E9FD70", 0.22, 14), clip_path="url(#clip)")
    arcs = "".join(el("circle", cx=W - 40, cy=H + 30, r=120 + k * 46, fill="none", stroke="#FFFFFF",
                      stroke_width=1, opacity=round(0.16 - k * 0.022, 3)) for k in range(7))
    o = [rect(0, 0, W, H, base, rx=22), clip, el("g", arcs, clip_path="url(#clip)"),
         eyebrow(64, 92, "Why work with me", "#E9FD70"),
         rich(62, 170, [[("Why work with me?", None)]], "#FFFFFF", 66, 0, track=-0.035)]
    o.append(rich(64, 226, [[("Because your AI is only as good as the context it can ", None), ("govern", "#E9FD70"),
                             (".", None)]], "#FFFFFF", 23, 0, 600, track=-0.015))
    o.append(rich(64, 258, [[("I build that context.", None)]], "#FFFFFF", 23, 0, 800, track=-0.015))
    x = 64
    for lab in PROOFS:
        w = tw(lab, 13, 600) + 52
        o += [rect(x, 298, w, 36, "#FFFFFF", "#FFFFFF", 1, 18, opacity=0.14),
              rect(x, 298, w, 36, "none", "#FFFFFF", 1, 18, opacity=0.35),
              circle(x + 19, 316, 4, "#E9FD70"),
              text(x + 32, 320.5, lab, "#FFFFFF", 13, 600)]
        x += w + 10
    # orbiting spark on the arcs
    o.append(particle(f"M{W - 40 - 212},{H + 30} A212,212 0 0,1 {W - 40},{H + 30 - 212}", 5, 0, 3.5, "#E9FD70"))
    return W, H, "".join(o)
