"""The maturity curve of my career: dotted ascending curve, M1-M5 milestones, proof under each."""
from svgkit import (anim, card, chip, circle, cubic, dotted, el, eyebrow, glow, mono_label, para, paper, particle,
                    ping, rich, text)
from textfit import tw

W = 1000

# (x, y, year, stage, role, proof)
MILESTONES = [
    (150, 372, "2013–2017", "Model the data", "Software engineer",
     "HRMS data model, 200+ tables; QA with 700+ defects found"),
    (330, 330, "2017–2019", "Keep it adopted", "AVP Customer Success, Mobisy / Bizom",
     "50+ enterprise FMCG accounts"),
    (510, 278, "2020–2021", "Shape the solution", "Manager Presales, LeadSquared",
     "100+ lending, eKYC and recovery projects in 12 months"),
    (690, 218, "2021–2024", "Design the deal", "Lead Solutions Consulting, MoEngage",
     "+50% conversion to proposal stage"),
    (866, 172, "2024–now", "Make it act", "AI Solutions Engineer, DevRev",
     "Production agents: case resolution 15–30 → <5 min (target)"),
]
CARRIED = ["Data models", "Account empathy", "Solution design", "Deal architecture", "Context engineering"]


def _smooth(points, start, end):
    """Catmull-Rom through points (with lead-in/out), sampled to a polyline and as an SVG path."""
    pts = [start] + points + [end]
    poly, d = [], f"M{pts[0][0]},{pts[0][1]}"
    for i in range(len(pts) - 1):
        p0 = pts[max(i - 1, 0)]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[min(i + 2, len(pts) - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        poly += cubic(p1, c1, c2, p2, 30)
        d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]},{p2[1]}"
    return poly, d


def _label(T, x, y, year, stage, role, proof, last):
    o = [mono_label(x, y + 40, year, T["purple"], 10, "middle", 1.4, 600),
         text(x, y + 62, stage, T["ink"], 16.5, 800, "middle", "display", spacing=-0.4)]
    s, yy = para(x, y + 81, role, T["muted"], 12, 164, 16, anchor="middle")
    o.append(s)
    s, _ = para(x, yy + 20, proof, T["ink2"] if not last else T["purple"], 12.5, 166, 17, 600 if last else 400,
                "middle")
    o.append(s)
    return "".join(o)


def curve(T):
    H = 620
    o = [paper(W, H, T, ((1.02, -0.1, 0.36), (-0.05, 1.1, 0.34))),
         eyebrow(56, 64, "The maturity curve of my career", T["purple"]),
         rich(54, 112, [[("Every role added a layer. ", None), ("Now it acts.", T["purple"])]], T["ink"], 38, 40)]
    # axes, deck style
    o += [el("path", d="M56,150 L56,520 L944,520", stroke=T["line"], stroke_width=1.2, fill="none"),
          mono_label(66, 160, "maturity → value", T["muted"], 9, "start", 1.6),
          mono_label(944, 540, "scope of work I own →", T["muted"], 9, "end", 1.6)]
    pts = [(x, y) for x, y, *_ in MILESTONES]
    poly, d = _smooth(pts, (62, 392), (950, 146))
    o.append(dotted(poly, T["purple"], 1.9, 10, 0.75))
    o.append(particle(d, 6, 0, 4, T["purple"]))
    # milestones
    for i, (x, y, year, stage, role, proof) in enumerate(MILESTONES):
        last = i == len(MILESTONES) - 1
        o.append(_label(T, x, y, year, stage, role, proof, last))
        if last:
            o += [glow(x, y, 44, T["purple_fill"], 0.35, 12), ping(x, y, 22, 40, T["purple"], 2.4),
                  circle(x, y, 25, T["lav_soft"], T["lav"], 2),
                  circle(x, y, 18, T["purple_fill"], kids=anim("r", "18;19.5;18", 2.4)),
                  text(x, y + 4, f"M{i + 1}", "#FFFFFF", 11.5, 700, "middle", "mono")]
        else:
            o += [circle(x, y, 21, T["ms_ring"], T["card_line"], 1),
                  circle(x, y, 17, T["ms_fill"]),
                  text(x, y + 4, f"M{i + 1}", T["ms_text"], 11, 700, "middle", "mono")]
    # what carried over
    o.append(card(48, 556, 904, 44, T, 22))
    s, w = chip(58, 564, "what carried over", T["purple_fill"], "#FFFFFF", 9.5, 28, weight=600, font="mono")
    o.append(s)
    x = 58 + w + 12
    for lab in CARRIED:
        s, cw = chip(x, 564, lab, T["lav_soft"], T["lav_ink"], 12.5, 28, weight=600)
        o.append(s)
        x += cw + 8
    return W, H, "".join(o)
