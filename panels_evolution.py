"""Signature panel 'How I evolved': the latest two eras, latest first, on a vertical timeline that points
ahead to what's next. Each era: role, AI wave, maturity reached, a technical -> business mini relay, chips."""
from svgkit import (anim, arrowhead, card, chip, chip_row, circle, dashed, dotted, el, eyebrow, glow, mono_label,
                    para, paper, particle, path, ping, rect, rich, text)
from textfit import tw, wrap

W = 1000
CX, X0, X1 = 80, 116, 952  # timeline x, card left, card right

# years, role, company, wave (tone), maturity, relay nodes [(title, sub)], outcome, chip rows [(label, chips)], learned
ERAS = [
    ("2024–now", "AI Solutions Engineer", "DevRev → architect", ("Generative & agentic AI", "violet"),
     "journey: ai evangelist",
     [("16+ connectors", "delta sync"), ("Governed context", "graph · permissions"),
      ("Multi-agent", "tools · approvals"), ("Evals + guardrails", "before go-live")],
     [("↑", "Hours saved"), ("↓", "Cost to serve"), ("↑", "Revenue"), ("↑", "CSAT")],
     [("concepts", ["Context layer", "Multi-agent orchestration", "Evals", "Guardrails", "Act-as identity",
                    "Retrieval, not stuffing"])],
     "The model is a component; the solution is the product."),
    ("2021–2024", "Presales Manager → Lead Solutions Consulting", "MoEngage · promoted Feb 2023",
     ("Predictive ML", "lilac"), "journey: expanding ai",
     [("SDKs + Data API", "app · web · server"), ("Warehouse sync", "s3 · sftp · cdp"),
      ("RFM segments", "flows (journeys)"), ("Sherpa models", "bts · mpc · predictions")],
     [("↑", "MAU / DAU"), ("↑", "Retention"), ("↑", "CTR"), ("↑", "CVR")],
     [("data in", ["Android/iOS/Web SDKs", "Data API (server events)", "S3/SFTP imports",
                   "Warehouse (BigQuery/Snowflake/Redshift)", "CDP sources"]),
      ("sherpa (now merlin ai)", ["Best Time to Send", "Most Preferred Channel", "Predictions (churn & conversion)",
                                  "Dynamic A/B (bandit-style)", "RFM segments (1–3 per axis)", "Flows (journeys)"])],
     "AI is only as good as the event data feeding it."),
]


def _fit(s, maxw, size, weight, mono=False, spacing=0.0):
    """Largest size <= size (down to 70%) at which s fits in maxw."""
    while size > 0 and tw(s, size, weight, mono, spacing) > maxw and size > 5:
        size = round(size - 0.25, 2)
    return size


def _relay(T, x, y, nodes, outcome, accent):
    nw, gap, nh = 124, 28, 72
    o = []
    for i, (t, s) in enumerate(nodes):
        nx = x + i * (nw + gap)
        o += [card(nx, y, nw, nh, T, 12), rect(nx + 12, y - 1, nw - 24, 3, accent if i % 2 else T["grn"], rx=1.5),
              text(nx + 12, y + 32, t, T["ink"], _fit(t, nw - 22, 13, 700), 700, font="display", spacing=-0.2),
              mono_label(nx + 12, y + 50, s, T["muted"], _fit(s.upper(), nw - 22, 7.5, 500, True, 0.8), "start", 0.8)]
        ax, cy = nx + nw + 4, y + nh / 2
        o += [dashed([(ax, cy), (ax + gap - 10, cy)], T["faint"], 1.5, 4, 3), arrowhead(ax + gap - 7, cy, 0, T["faint"], 4.5),
              particle(f"M{ax},{cy} L{ax + gap - 7},{cy}", 1.3, round(i * 0.6, 2), 2.6, T["purple_fill"])]
    ox = x + 4 * (nw + gap)
    ow = X1 - 24 - ox
    o += [rect(ox, y, ow, nh, T["yellow"], rx=14),
          mono_label(ox + 12, y + 16, "business outcomes", "#5C5200", 7.5, "start", 1.2, 700)]
    for j, (arrow, item) in enumerate(outcome):
        cx_, cy_ = ox + 12 + (j % 2) * ((ow - 20) / 2), y + 36 + (j // 2) * 18
        o += [text(cx_, cy_, arrow, "#3F8F0A" if arrow == "↑" else "#B0123F", 11.5, 800, font="display"),
              text(cx_ + 12, cy_, item, "#151515", _fit(item, (ow - 20) / 2 - 16, 11.5, 700), 700, font="display")]
    return "".join(o)


def _era(T, y, era, latest):
    years, role, company, (wave, tone), level, nodes, outcome, chip_rows, learned = era
    x = X0 + 24
    o = [mono_label(x, y + 32, years, T["purple"], 10.5, "start", 1.6, 700)]
    s, yy = para(x, y + 62, role, T["ink"], 25, 520, 29, 800, font="display")
    o += [s, text(x, yy + 22, company, T["muted"], 13.5)]
    fill, ink = T["bubbles"][tone]
    a, aw = chip(X1 - 24, y + 18, level, T["ink"] if T["name"] == "light" else "#2E2A42", "#FFFFFF", 9.5, 28,
                 weight=700, anchor="end", font="mono")
    b, _ = chip(X1 - 24 - aw - 8, y + 18, wave, fill, ink, 12.5, 28, weight=700, anchor="end")
    o += [a, b]
    ry = yy + 62
    o.append(mono_label(x, ry - 10, "technical → business", T["faint"], 8.5, "start", 1.4, 700))
    o.append(_relay(T, x, ry, nodes, outcome, T["ink"]))
    cy = ry + 72 + 28
    for label, chips in chip_rows:
        o.append(mono_label(x, cy + 16, label, T["faint"], 8.5, "start", 1.4, 700))
        cx, lx = x + 150, x + 150
        for lab in chips:
            w = tw(lab, 11.5, 600) + 24
            if cx + w > X1 - 24 and cx > lx:
                cx, cy = lx, cy + 32
            s, w = chip(cx, cy, lab, T["card"] if latest else T["lav_soft"], T["lav_ink"], 11.5, 24,
                        T["lav"] if latest else None, 600)
            o.append(s)
            cx += w + 8
        cy += 36
    o += [mono_label(x, cy + 18, "learned", T["faint"], 8.5, "start", 1.4, 700),
          text(x + 150, cy + 18, learned, T["purple"], 15, 800, font="display", spacing=-0.3)]
    return "".join(o), cy + 44 - y


def evolution(T):
    top = 250
    # measure each era, then lay out
    bodies, y = [], top
    for i, era in enumerate(ERAS):
        s, h = _era(T, y, era, i == 0)
        bodies.append((y, h, s))
        y += h + 26
    H = y + 30
    o = [paper(W, H, T, ((1.02, -0.03, 0.42), (-0.04, 1.02, 0.44))),
         eyebrow(56, 64, "How I evolved", T["purple"]),
         rich(54, 118, [[("From predictive marketing AI", None)], [("to agentic enterprise AI.", T["purple"])]],
              T["ink"], 42, 48)]
    # next: dotted, ahead of the latest era
    o += [dotted([(CX, top - 6), (CX, 196)], T["purple"], 1.6, 8, 0.45), arrowhead(CX, 192, -90, T["purple"], 6),
          rect(X0, 200, 420, 32, "none", T["purple"], 1, 16, opacity=0.6),
          mono_label(X0 + 16, 220, "next →", T["purple"], 9, "start", 1.4, 700),
          text(X0 + 72, 220.5, "Solutions Architect, governed enterprise AI", T["purple"], 13, 600)]
    (y1, h1, _), (y2, h2, _) = bodies
    o.append(dotted([(CX, y1 + 40), (CX, y2 + 40), (CX, y2 + h2 - 10)], T["purple"], 2, 9, 0.75))
    for i, (yy, h, s) in enumerate(bodies):
        latest = i == 0
        if latest:
            o += [glow(CX, yy + 40, 46, T["purple_fill"], 0.4, 14), ping(CX, yy + 40, 16, 36, T["purple"], 2.4),
                  ping(CX, yy + 40, 16, 36, T["purple"], 2.4, "1.2s"), circle(CX, yy + 40, 20, T["lav_soft"], T["lav"], 2),
                  circle(CX, yy + 40, 14, T["purple_fill"]), text(CX, yy + 43.5, "NOW", "#FFFFFF", 8.5, 700, "middle", "mono"),
                  card(X0, yy, X1 - X0, h, T, 20, T["lav_soft"], T["purple_fill"])]
        else:
            o += [circle(CX, yy + 40, 16, T["ms_ring"], T["card_line"], 1), circle(CX, yy + 40, 12, T["ms_fill"]),
                  text(CX, yy + 43.5, "21", T["ms_text"], 9, 700, "middle", "mono"), card(X0, yy, X1 - X0, h, T, 20)]
        o += [path(f"M{CX + 20},{yy + 40}H{X0}", T["lav"] if latest else T["line"], 1.4), s]
    return W, H, "".join(o)
