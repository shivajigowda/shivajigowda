"""'The AI maturity journey': two generic dotted curves. The employee journey runs ahead of the company journey,
because AI-centric employees create AI-centric companies."""
from panels_curve import _smooth
from svgkit import circle, dotted, el, eyebrow, glow, mono_label, paper, particle, ping, rect, rich, text

W = 1000

EMPLOYEE = [("AI blind", "unaware, or wary of AI"), ("AI curious", "experiments at work and home"),
            ("Daily AI", "uses AI daily for set tasks"), ("Expanding AI", "brings AI into more workflows"),
            ("AI first", "starts most tasks with AI"), ("AI evangelist", "lifts the whole team")]
COMPANY = [("AI desert", "absent, or blocked by policy"), ("AI tools", "secure tools made available"),
           ("AI initiatives", "sponsors high-value projects"), ("AI champions", "leaders spread the wins"),
           ("AI platform", "one standard to build and adopt"), ("AI-centric business", "doubles down on outcomes")]
XS = [120, 270, 420, 570, 720, 870]


def _journey(T, title, stages, base, rise, colour, label_above):
    ys = [base - rise * (i / 5) ** 1.35 for i in range(6)]
    o = []
    poly, d = _smooth(list(zip(XS, ys)), (60, ys[0] + 10), (950, ys[-1] - 18))
    o += [dotted(poly, colour, 1.9, 10, 0.75), particle(d, 7, 0, 3.4, colour)]
    for i, ((name, desc), x, y) in enumerate(zip(stages, XS, ys)):
        last = i == 5
        ty = y - 40 if label_above else y + 34
        o += [text(x, ty, name, T["ink"], 14, 800, "middle", "display", spacing=-0.2),
              text(x, ty + 16, desc, T["muted"], 11, 400, "middle")]
        if last:
            o += [glow(x, y, 30, colour, 0.28, 12), ping(x, y, 11, 24, colour, 2.6), circle(x, y, 11, colour)]
        else:
            o += [circle(x, y, 10, T["ms_ring"], T["card_line"], 1), circle(x, y, 7, colour)]
    ly = ys[0] + 34 if label_above else ys[0] - 26
    o.append(mono_label(64, ly, title, colour, 9.5, "start", 1.8, 700))
    return "".join(o)


def maturity(T):
    H = 720
    emp, comp = T["purple"], T["grn2"]
    o = [paper(W, H, T, ((1.02, -0.04, 0.4), (-0.04, 1.03, 0.42))),
         eyebrow(56, 64, "The AI maturity journey", T["purple"]),
         rich(54, 116, [[("AI-centric employees create ", None)], [("AI-centric companies.", T["purple"])]],
              T["ink"], 40, 46)]
    o.append(_journey(T, "the ai employee journey", EMPLOYEE, 410, 160, emp, True))
    o.append(_journey(T, "the ai company journey", COMPANY, 600, 170, comp, False))
    # axis
    for i in range(40):
        a = i / 39
        o.append(rect(56 + a * 870, 676, 22.5, 6, emp if a < 0.5 else comp, opacity=round(0.18 + 0.5 * a, 2)))
    o += [el("path", d="M930,672 L946,679 L930,686 Z", fill=comp),
          mono_label(500, 700, "ai maturity → value", T["muted"], 9.5, "middle", 2.2, 600)]
    return W, H, "".join(o)
