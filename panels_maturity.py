"""'Two maturity curves': business M1-M4 and individual L1-L5, with my builds plotted as markers."""
from panels_curve import _smooth
from svgkit import (anim, card, chip, circle, dotted, el, eyebrow, glow, mono_label, paper, particle, path, ping,
                    rich, text)
from textfit import tw

W = 1000

BUSINESS = [("M1", "Unify & see", "connect systems, one governed memory"),
            ("M2", "Agentic bridges", "agents act across 2–3 systems"),
            ("M3", "End-to-end chains", "multi-step journeys with approvals"),
            ("M4", "Governed enterprise", "evals, policy and audit at scale")]
PEOPLE = [("L1", "AI answers", "search, Q&A"), ("L2", "AI assists", "drafts, summaries, copilots"),
          ("L3", "AI acts", "agents with tools"), ("L4", "AI orchestrates", "multi-agent workflows"),
          ("L5", "AI governs", "evals, guardrails, policy")]
# (label, era) per milestone index, from the use-case rows; "now" = DevRev era, "prev" = MoEngage 2021-24
B_MARKS = {0: [("Pharma analytics (M1–M2)", "now"), ("Marketing (M1–M2)", "prev")],
           1: [("BFSI ×2", "now"), ("Pharma planning", "now"), ("Automotive", "now")],
           2: [("Airlines", "now"), ("Retail & D2C ×2", "now")],
           3: [("IT services (M3–M4)", "now")]}
P_MARKS = {1: [("Marketing", "prev"), ("Pharma ×2", "now"), ("Automotive", "now")],
           2: [("Airlines", "now"), ("BFSI ×2", "now"), ("Retail & D2C ×2", "now")],
           3: [("IT services", "now")]}


def _marker(T, cx, y, label, era):
    fill, ink = (T["purple_fill"], "#FFFFFF") if era == "now" else T["bubbles"]["peach"]
    w = tw(label, 11, 600) + 22
    x = min(max(cx - w / 2, 56), 944 - w)
    s, _ = chip(x, y, label, fill, ink, 11, 24, weight=600)
    return s


def _curve(T, top, title, levels, marks, xs, rise):
    """One curve block: header, axis, dotted path, milestone dots, labels above, markers below."""
    n = len(levels)
    base = top + 70 + rise
    ys = [base - rise * i / (n - 1) for i in range(n)]
    o = [mono_label(56, top + 8, title, T["purple"], 10, "start", 2, 700),
         el("line", x1=56, y1=top + 18, x2=944, y2=top + 18, stroke=T["line"], stroke_width=1)]
    poly, d = _smooth(list(zip(xs, ys)), (60, ys[0] + 22), (950, ys[-1] - 20))
    o += [dotted(poly, T["purple"], 1.9, 10, 0.7), particle(d, 6, 0, 3.6, T["purple"])]
    for i, ((code, name, desc), x, y) in enumerate(zip(levels, xs, ys)):
        last = i == n - 1
        o += [text(x, y - 44, name, T["ink"], 15, 800, "middle", "display", spacing=-0.3),
              text(x, y - 27, desc, T["muted"], 11.5, 400, "middle")]
        if last:
            o += [glow(x, y, 34, T["purple_fill"], 0.3, 12), ping(x, y, 15, 30, T["purple"], 2.6),
                  circle(x, y, 15, T["purple_fill"])]
        else:
            o += [circle(x, y, 17, T["ms_ring"], T["card_line"], 1), circle(x, y, 14, T["ms_fill"])]
        o.append(text(x, y + 4, code, "#FFFFFF" if last else T["ms_text"], 10, 700, "middle", "mono"))
        for k, (lab, era) in enumerate(marks.get(i, [])):
            my = y + 26 + k * 30
            o += [path(f"M{x},{y + 15}V{my}", T["faint"], 1, opacity=0.7) if k == 0 else "",
                  _marker(T, x, my, lab, era)]
    return "".join(o)


def maturity(T):
    H = 920
    o = [paper(W, H, T, ((1.02, -0.04, 0.4), (-0.04, 1.03, 0.42))),
         eyebrow(56, 64, "The AI maturity curve", T["purple"]),
         rich(54, 116, [[("AI that answers → AI that acts,", None)], [("for businesses and for people.", T["purple"])]],
              T["ink"], 40, 46)]
    o.append(_curve(T, 196, "for businesses · m1 → m4", BUSINESS, B_MARKS, [150, 400, 650, 860], 110))
    o.append(_curve(T, 530, "for people · l1 → l5", PEOPLE, P_MARKS, [140, 330, 520, 710, 870], 120))
    # caption + legend
    o.append(card(48, 856, 904, 44, T, 22))
    s, w = chip(58, 864, "where each build sits", T["purple_fill"], "#FFFFFF", 9.5, 28, weight=600, font="mono")
    o += [s, text(58 + w + 14, 883, "and how I climbed.", T["ink2"], 13, 600)]
    a, aw = chip(944 - 8, 864, "MoEngage 2021–24", *T["bubbles"]["peach"], 11.5, 28, weight=600, anchor="end")
    b, _ = chip(944 - 8 - aw - 8, 864, "DevRev 2024–now", T["purple_fill"], "#FFFFFF", 11.5, 28, weight=600,
                anchor="end")
    o += [a, b]
    return W, H, "".join(o)
