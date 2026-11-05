"""'What I build': three relay lanes of dashed hand-offs, each ending in a result chip."""
from textfit import tw
from svgkit import (arrowhead, card, chip, circle, dashed, el, eyebrow, mono_label, paper, particle, path, rect,
                    rich, text)

W = 1000

LANES = [
    ("01", "Enterprise context layer",
     "ERP, CRM, ticketing, HR and commerce unified so agents answer from governed context.",
     [("Source systems", "erp · crm · hr", "db"), ("MCP + REST", "+ webhooks", "plug"),
      ("Connectors", "etl · deltas", "bolt"), ("Knowledge graph", "permissioned", "graph")],
     ["read", "map", "link"], "governed graph", "lime"),
    ("02", "Agent orchestration, guarded",
     "Airline re-booking across CRM, payments, reservations and internal APIs.",
     [("Request", "customer · staff", "chat"), ("Planner", "multi-agent", "nodes"),
      ("Allowlist", "guardrails · human", "shield"), ("Tool calls", "crm · payments", "bolt")],
     ["intent", "plan", "act"], "15–30 → <5 min (target)", "violet"),
    ("03", "Connector delta engine",
     "16+ production TypeScript connectors that never re-send what the platform already has.",
     [("Scan window", "cursor · time", "scan"), ("Skip settled", "terminal states", "check"),
      ("Content hash", "id → hash", "hash"), ("Push changed", "429-safe saves", "push")],
     ["sweep", "diff", "send"], "sent = landed", "yellow"),
]


def _glyph(kind, x, y, c):
    """Tiny line glyphs inside a 26px dark tile at (x, y)."""
    cx, cy = x + 13, y + 13
    g = {
        "db": path(f"M{cx - 6},{cy - 5} a6,2.5 0 1,0 12,0 a6,2.5 0 1,0 -12,0 v10 a6,2.5 0 0,0 12,0 v-10", c, 1.4),
        "plug": path(f"M{cx - 3},{cy - 7}v4M{cx + 3},{cy - 7}v4M{cx - 6},{cy - 3}h12v3a6,6 0 0,1 -12,0zM{cx},{cy + 6}v3",
                     c, 1.4),
        "bolt": path(f"M{cx + 2},{cy - 8}L{cx - 5},{cy + 1}H{cx}L{cx - 2},{cy + 8}L{cx + 5},{cy - 1}H{cx}Z", c, 1.4),
        "graph": (path(f"M{cx - 6},{cy + 4}L{cx},{cy - 5}L{cx + 6},{cy + 4}Z", c, 1.2)
                  + circle(cx - 6, cy + 4, 2.2, c) + circle(cx, cy - 5, 2.2, c) + circle(cx + 6, cy + 4, 2.2, c)),
        "chat": path(f"M{cx - 7},{cy - 6}h14v9h-8l-4,4v-4h-2z", c, 1.4),
        "nodes": (path(f"M{cx - 6},{cy}H{cx + 6}M{cx},{cy - 6}V{cy + 6}", c, 1.2) + circle(cx, cy, 2.6, c)
                  + circle(cx - 6, cy, 1.8, c) + circle(cx + 6, cy, 1.8, c) + circle(cx, cy - 6, 1.8, c)
                  + circle(cx, cy + 6, 1.8, c)),
        "shield": path(f"M{cx},{cy - 8}l6,2.5v4.5c0,4 -3,6.5 -6,7.5c-3,-1 -6,-3.5 -6,-7.5v-4.5zM{cx - 2.5},{cy}l2,2l3.5,-4",
                       c, 1.4),
        "scan": path(f"M{cx - 7},{cy - 3}v-4h4M{cx + 3},{cy - 7}h4v4M{cx + 7},{cy + 3}v4h-4M{cx - 3},{cy + 7}h-4v-4"
                     f"M{cx - 5},{cy}h10", c, 1.4),
        "check": path(f"M{cx - 6},{cy}l4,4l8,-8", c, 1.8),
        "hash": path(f"M{cx - 3},{cy - 7}l-1.5,14M{cx + 3.5},{cy - 7}l-1.5,14M{cx - 6.5},{cy - 2.5}h13M{cx - 7},{cy + 3}h13",
                     c, 1.4),
        "push": path(f"M{cx},{cy + 7}V{cy - 6}M{cx - 5},{cy - 1}l5,-5l5,5M{cx - 7},{cy + 7}h14", c, 1.4),
    }
    return g[kind]


def _node(T, x, y, w, h, title, sub, kind, i):
    accent = T["grn"] if i % 2 == 0 else T["ink"]
    return (card(x, y, w, h, T, 12)
            + rect(x + 14, y - 1, w - 28, 3, accent, rx=1.5)
            + rect(x + 12, y + 12, 26, 26, T["ms_fill"] if T["name"] == "light" else "#2E2A42", rx=7)
            + _glyph(kind, x + 12, y + 12, T["lime"])
            + mono_label(x + w - 12, y + 24, f"0{i + 1}", T["faint"], 8.5, "end", 1)
            + text(x + 12, y + 58, title, T["ink"], 13.5, 700, font="display", spacing=-0.2)
            + mono_label(x + 12, y + 72, sub, T["muted"], 8, "start", 1.1))


def _lane(T, y, num, title, desc, nodes, hand, result, tone):
    o = [card(48, y, 904, 150, T, 18),
         text(72, y + 34, num, T["purple"], 12, 700, font="mono"),
         text(98, y + 34, title, T["ink"], 18, 800, font="display", spacing=-0.4)]
    tx = 98 + tw(title, 18, 800) + 18
    o.append(text(tx, y + 34, desc, T["muted"], 12.5))
    nw, nh, gap, ny = 132, 82, 46, y + 52
    for i, (t, s, k) in enumerate(nodes):
        x = 72 + i * (nw + gap)
        o.append(_node(T, x, ny, nw, nh, t, s, k, i))
        x1, x2, cy = x + nw + 6, x + nw + gap - 6, ny + nh / 2
        if i < len(nodes) - 1:
            lab = hand[i]
        else:
            lab = "result"
        o += [dashed([(x1, cy), (x2 - 2, cy)], T["faint"], 1.6, 4, 3.5), arrowhead(x2, cy, 0, T["faint"], 4.5),
              mono_label((x1 + x2) / 2, cy - 8, lab, T["muted"], 7.5, "middle", 0.6),
              particle(f"M{x1},{cy} L{x2},{cy}", 1.4, round(i * 0.7, 2), 2.6, T["purple_fill"])]
    fill, ink = T["bubbles"][tone]
    rx0 = 72 + 4 * (nw + gap)
    rw = 928 - rx0
    o += [rect(rx0, ny + 12, rw, nh - 24, fill, rx=(nh - 24) / 2),
          text(rx0 + rw / 2, ny + nh / 2 + 5.5, result, ink, 13.5 if len(result) > 15 else 15, 800, "middle", "display", spacing=-0.3)]
    return "".join(o)


def relay(T):
    H = 680
    o = [paper(W, H, T, ((1.0, -0.08, 0.38), (-0.04, 1.06, 0.4))),
         eyebrow(56, 64, "What I build", T["purple"]),
         rich(54, 112, [[("Three relays. ", None), ("One governed context.", T["purple"])]], T["ink"], 38, 40)]
    for i, lane in enumerate(LANES):
        o.append(_lane(T, 150 + i * 172, *lane))
    return W, H, "".join(o)
