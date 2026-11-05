"""Small SVG toolkit. Presentation attributes only (no CSS, no web fonts, no filters) so files
render the same in GitHub's <img>, browsers and MuPDF. Dashes and glows are drawn as real
geometry (segment paths, stacked translucent discs) because MuPDF ignores dasharray and gradients."""
import math
from xml.sax.saxutils import escape

from textfit import tw, wrap

DISPLAY = "Inter,'SF Pro Display',-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
SANS = "Inter,'SF Pro Text',-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,'SF Mono',SFMono-Regular,Menlo,Consolas,monospace"
FONTS = {"display": DISPLAY, "sans": SANS, "mono": MONO}


def esc(v):
    return escape(str(v), {'"': "&quot;"})


def f1(v):
    return f"{v:.1f}".rstrip("0").rstrip(".") if isinstance(v, float) else str(v)


def el(tag, kids="", **a):
    at = "".join(f' {k.rstrip("_").replace("_", "-")}="{esc(f1(v))}"' for k, v in a.items() if v is not None)
    return f"<{tag}{at}>{kids}</{tag}>" if kids else f"<{tag}{at}/>"


# ------------------------------------------------------------------ text
def text(x, y, s, fill, size=13, weight=400, anchor="start", font="sans", opacity=None, spacing=None):
    return el("text", esc(s), x=round(x, 1), y=round(y, 1), fill=fill, font_size=size, font_weight=weight,
              text_anchor=anchor, font_family=FONTS[font], opacity=opacity, letter_spacing=spacing)


def rich(x, y, lines, base, size, lh, weight=800, anchor="start", font="display", track=-0.03):
    """Multi-line text with coloured spans. lines = [[(str, colour|None), ...], ...]."""
    out = []
    for i, segs in enumerate(lines):
        spans = "".join(el("tspan", esc(s), fill=c) if c else esc(s) for s, c in segs)
        out.append(el("text", spans, x=x, y=round(y + i * lh, 1), fill=base, font_size=size, font_weight=weight,
                      text_anchor=anchor, font_family=FONTS[font], letter_spacing=round(size * track, 2)))
    return "".join(out)


def para(x, y, s, fill, size, maxw, lh, weight=400, anchor="start", font="sans"):
    """Wrapped paragraph; returns (svg, y_after_last_baseline)."""
    rows = wrap(s, maxw, size, weight, font == "mono")
    svg = "".join(text(x, y + i * lh, r, fill, size, weight, anchor, font) for i, r in enumerate(rows))
    return svg, y + (len(rows) - 1) * lh


def eyebrow(x, y, s, colour, size=11, spacing=2.2):
    return (el("line", x1=x, y1=y - size * 0.35, x2=x + 22, y2=y - size * 0.35, stroke=colour, stroke_width=1.6)
            + text(x + 32, y, s.upper(), colour, size, 500, font="mono", spacing=spacing))


def mono_label(x, y, s, fill, size=9.5, anchor="start", spacing=1.6, weight=500):
    return text(x, y, s.upper(), fill, size, weight, anchor, "mono", spacing=spacing)


# ------------------------------------------------------------------ shapes
def rect(x, y, w, h, fill="none", stroke=None, sw=1, rx=0, opacity=None, kids=""):
    return el("rect", kids, x=round(x, 1), y=round(y, 1), width=round(w, 1), height=round(h, 1), rx=rx, fill=fill,
              stroke=stroke, stroke_width=sw if stroke else None, opacity=opacity)


def circle(cx, cy, r, fill="none", stroke=None, sw=1.2, opacity=None, kids=""):
    return el("circle", kids, cx=round(cx, 1), cy=round(cy, 1), r=round(r, 1), fill=fill, stroke=stroke,
              stroke_width=sw if stroke else None, opacity=opacity)


def path(d, stroke, sw=1.4, fill="none", opacity=None, kids=""):
    return el("path", kids, d=d, fill=fill, stroke=stroke, stroke_width=sw, opacity=opacity,
              stroke_linecap="round", stroke_linejoin="round")


def card(x, y, w, h, T, rx=16, fill=None, stroke=None):
    """White card with a faint drop shadow, like the deck's tiles."""
    return (rect(x, y + 3, w, h, T["shadow"], rx=rx, opacity=0.05 if T["name"] == "light" else 0.35)
            + rect(x, y, w, h, fill or T["card"], stroke or T["card_line"], 1, rx))


def glow(cx, cy, r, colour, peak=0.5, steps=30):
    """Soft radial glow from stacked discs (no gradient needed)."""
    a = 1 - (1 - peak) ** (1 / steps)
    return "".join(circle(cx, cy, r * (1 - i / steps) ** 0.8, colour, opacity=round(a, 4)) for i in range(steps))


def paper(W, H, T, glows=((1.0, -0.05, 0.42), (-0.02, 1.05, 0.45)), colours=None):
    """Off-white (or ink) paper with a lime glow top-right, lilac bottom-left and a faint light band."""
    o = [rect(0, 0, W, H, T["paper"], rx=22)]
    (ax, ay, ar), (bx, by, br) = glows
    ca, cb = colours or (T["glow_a"], T["glow_b"])
    o.append(el("g", glow(W * ax, H * ay, W * ar, ca, T["glow_op"])
                + glow(W * bx, H * by, W * br, cb, T["glow_op"]), clip_path="url(#clip)"))
    band = f"M{W * 0.62:.0f},{H} L{W * 0.98:.0f},0 L{W * 1.12:.0f},0 L{W * 0.80:.0f},{H} Z"
    o.append(el("path", d=band, fill=T["band"], opacity=T["band_op"], clip_path="url(#clip)"))
    return "".join(o)


# ------------------------------------------------------------------ dashed geometry
def cubic(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        pts.append((u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
                    u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1]))
    return pts


def _walk(pts, step):
    """Yield evenly spaced points (distance `step`) along a polyline."""
    out, carry = [pts[0]], 0.0
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        seg = math.hypot(x2 - x1, y2 - y1)
        d = step - carry
        while d <= seg:
            t = d / seg
            out.append((x1 + (x2 - x1) * t, y1 + (y2 - y1) * t))
            d += step
        carry = seg - (d - step)
    return out


def dashed(pts, stroke, sw=1.4, dash=5, gap=4, opacity=None):
    """Dashed polyline drawn as real sub-paths."""
    dense = _walk(pts, 1.0)
    period, d = int(dash + gap), []
    for i in range(0, len(dense) - 1, period):
        a, b = dense[i], dense[min(i + int(dash), len(dense) - 1)]
        d.append(f"M{a[0]:.1f},{a[1]:.1f}L{b[0]:.1f},{b[1]:.1f}")
    return el("path", d="".join(d), stroke=stroke, stroke_width=sw, fill="none", stroke_linecap="round",
              opacity=opacity)


def dotted(pts, fill, r=1.6, step=9, opacity=None):
    """Dotted line as a single path of tiny circles."""
    d = "".join(f"M{x - r:.1f},{y:.1f}a{r},{r} 0 1,0 {2 * r},0a{r},{r} 0 1,0 {-2 * r},0" for x, y in _walk(pts, step))
    return el("path", d=d, fill=fill, opacity=opacity)


def arrowhead(x, y, ang, colour, s=5):
    a = math.radians(ang)
    p1 = (x - s * math.cos(a - 0.5), y - s * math.sin(a - 0.5))
    p2 = (x - s * math.cos(a + 0.5), y - s * math.sin(a + 0.5))
    return el("path", d=f"M{p1[0]:.1f},{p1[1]:.1f}L{x:.1f},{y:.1f}L{p2[0]:.1f},{p2[1]:.1f}", stroke=colour,
              stroke_width=1.5, fill="none", stroke_linecap="round", stroke_linejoin="round")


# ------------------------------------------------------------------ chips
def chip(x, y, label, fill, ink, size=12, h=28, stroke=None, weight=600, dot=None, anchor="start", font="sans"):
    """Pill chip; returns (svg, width). anchor='middle' centres it on x."""
    pad = h * 0.5
    w = tw(label, size, weight, font == "mono", 1.2 if font == "mono" else 0) + pad * 2 + (14 if dot else 0)
    x0 = x - w / 2 if anchor == "middle" else x - w if anchor == "end" else x
    o = [rect(x0, y, w, h, fill, stroke, 1, h / 2)]
    tx = x0 + pad
    if dot:
        o.append(circle(tx + 3.5, y + h / 2, 3.5, dot))
        tx += 14
    o.append(text(tx, y + h / 2 + size * 0.36, label if font != "mono" else label.upper(), ink, size, weight,
                  font=font, spacing=1.2 if font == "mono" else None))
    return "".join(o), w


def chip_row(x, y, items, gap=10, **kw):
    """items = [(label, fill, ink), ...] on one line; returns (svg, total_width)."""
    o, cx = [], x
    for label, fill, ink in items:
        s, w = chip(cx, y, label, fill, ink, **kw)
        o.append(s)
        cx += w + gap
    return "".join(o), cx - gap - x


def chip_flow(x, y, labels, maxw, fill, ink, stroke=None, size=12.5, h=30, gap=10):
    o, cx, cy = [], x, y
    for lab in labels:
        w = tw(lab, size, 600) + h
        if cx + w > x + maxw and cx > x:
            cx, cy = x, cy + h + gap
        s, w = chip(cx, cy, lab, fill, ink, size, h, stroke)
        o.append(s)
        cx += w + gap
    return "".join(o), cy + h - y


# ------------------------------------------------------------------ animation (SMIL; static frame stays complete)
def anim(attr, values, dur, begin="0s", times=None, spline=False):
    return el("animate", attributeName=attr, values=values, dur=f"{dur}s", begin=begin, repeatCount="indefinite",
              keyTimes=times, calcMode="spline" if spline else None,
              keySplines=";".join(["0.4 0 0.2 1"] * (len(values.split(";")) - 1)) if spline else None)


def particle(d, dur, begin, r, fill):
    """A dot travelling along path d. Base opacity 0, so static renderers never show it."""
    kids = (el("animateMotion", path=d, dur=f"{dur}s", begin=f"{begin}s", repeatCount="indefinite")
            + anim("opacity", "0;1;1;0", dur, f"{begin}s", "0;0.15;0.8;1"))
    return circle(0, 0, r, fill, opacity=0, kids=kids)


def ping(cx, cy, r0, r1, colour, dur=2.8, begin="0s", sw=1.6):
    """Expanding ring that fades out; invisible in a static frame."""
    return circle(cx, cy, r0, "none", colour, sw, opacity=0,
                  kids=anim("r", f"{r0};{r1}", dur, begin) + anim("opacity", "0.7;0", dur, begin))


# ------------------------------------------------------------------ document
def doc(W, H, body, title, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
            f'role="img" aria-labelledby="t d">'
            f'<title id="t">{esc(title)}</title><desc id="d">{esc(desc)}</desc>'
            f'<defs><clipPath id="clip"><rect width="{W}" height="{H}" rx="22"/></clipPath></defs>'
            + body + "</svg>\n")
