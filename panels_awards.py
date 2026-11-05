"""'Recognition': awards as three trophy cards, latest first, with laurel glyphs."""
import math

from svgkit import card, chip, el, eyebrow, mono_label, rect, rich, text

W = 1000

# year, award, company, event, chip, highlight
AWARDS = [
    ("2026", "APJ SE of the Year", "DevRev", "Sales Kickoff 2026", "Asia-Pacific & Japan", True),
    ("2024", "Deal Maker", "MoEngage", "Annual Sales Kickoff 2024", "Adapt, Innovate & Win", False),
    ("2022", "Rainmaker", "MoEngage", "Q2 2022", "Quarterly award", False),
]


def laurel(cx, cy, r, colour):
    """Two mirrored leaf branches rising from below the centre up both sides, like a wreath."""
    leaves = []
    for side in (-1, 1):
        for i in range(6):
            deg = 240 - i * 22 if side < 0 else -60 + i * 22
            a = math.radians(deg)
            x, y = cx + r * math.cos(a), cy - r * math.sin(a)
            tangent = deg + (90 if side > 0 else -90)
            leaves.append(el("ellipse", cx=round(x, 1), cy=round(y, 1), rx=3.4, ry=8, fill=colour,
                             transform=f"rotate({-tangent + 90:.0f} {x:.1f} {y:.1f})",
                             opacity=round(0.5 + i * 0.09, 2)))
    return "".join(leaves)


def award_card(x, y, w, h, award, T):
    year, name, company, event, tag, hi = award
    o = [card(x, y, w, h, T, rx=18, fill=T["yellow_soft"] if hi else None,
              stroke=T["gold"] if hi else None)]
    if hi:
        o.append(rect(x + 0.5, y + 0.5, w - 1, h - 1, "none", T["gold"], 2, 18))
    cx = x + w / 2
    o.append(laurel(cx, y + 70, 42, T["gold"] if hi else T["purple"]))
    o.append(text(cx, y + 78, year, T["ink"], 22, 800, anchor="middle", font="display"))
    o.append(text(cx, y + 150, name, T["ink"], 20, 800, anchor="middle", font="display"))
    o.append(mono_label(cx, y + 174, f"{company} · {event}", T["muted"], 9.5, anchor="middle"))
    s, _ = chip(cx, y + 192, tag, T["lav_soft"] if not hi else T["yellow"], T["lav_ink"] if not hi else "#151515",
                size=11.5, h=26, anchor="middle")
    o.append(s)
    return "".join(o)


def awards(T):
    H = 400
    o = [rect(0, 0, W, H, T["paper"], rx=22), eyebrow(56, 64, "Recognition", T["purple"])]
    o.append(rich(54, 114, [[("Recognised for ", None), ("winning in the field.", T["purple"])]], T["ink"], 36, 40))
    cw, gap, top = 280, 24, 140
    x = (W - (cw * 3 + gap * 2)) / 2
    for a in AWARDS:
        o.append(award_card(x, top, cw, 228, a, T))
        x += cw + gap
    return W, H, "".join(o)
