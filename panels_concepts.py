"""'How sync actually works': nine concept cards, each with a tiny inline diagram."""
from svgkit import arrowhead, card, chip, circle, el, eyebrow, mono_label, para, paper, path, rect, rich, text

W = 1000

# (eyebrow, title, plain-English explanation, used in, tone, diagram)
CONCEPTS = [
    ("watermark", "Modified-date watermark",
     "Read only records with updated_at after the last one seen, minus a small overlap for clock skew.",
     "ReturnPrime · Xray", "lilac", "watermark",
     "smaller syncs, fresher data, lower API cost"),
    ("hashing", "Content hashing",
     "No reliable timestamp? Hash the mapped fields; send only on change. Cut ~1.3k unchanged re-sends per sync.",
     "Shopify", "lime", "hash",
     "fewer re-sends, no duplicates, lower load cost"),
    ("skip", "Settled-record skip",
     "Stop re-fetching records already in a terminal state, such as delivered shipments.",
     "Shiprocket", "mint", "settled",
     "shorter syncs and fewer API calls"),
    ("transport", "Polling vs webhooks",
     "Polling: I ask on a schedule, self-healing. Webhooks: they tell me now, at-least-once, so verify the HMAC.",
     "Hybrid: webhooks + polling", "sky", "poll",
     "near-real-time updates without missed events"),
    ("paging", "Pagination that can't lie",
     "Cursor or keyset beats offset; time windows split when a page cap hits. A page-100 cap once gave 5k of 88k orders.",
     "Shiprocket", "yellow", "paging",
     "complete data: no silently missing records"),
    ("api shape", "REST vs GraphQL",
     "REST: many endpoints, fixed shapes, N+1 calls. GraphQL: one exact nested query, cost-based limits, "
     "errors that arrive with HTTP 200.",
     "Shopify GraphQL · Xray", "pink", "graphql",
     "fewer calls, faster syncs, predictable limits"),
    ("identity", "Idempotent typed IDs",
     "Stable ids prefixed by type, so retries never duplicate and order-123 never collides with return-123.",
     "Every connector", "peach", "ids",
     "no duplicates or collisions, so reports stay trusted"),
    ("retries", "Backoff with jitter",
     "Retry 429s and 5xx with exponential backoff plus jitter. Never retry a 4xx: that is a bug.",
     "Every connector", "lilac", "backoff",
     "syncs survive rate limits without manual reruns"),
    ("state", "Checkpoint after verified writes",
     "Save state only after the upload is verified; move large state out of the run into durable storage.",
     "Sync state + artifacts", "lime", "checkpoint",
     "no lost or duplicated data after a crash"),
]


def _diagram(kind, x, y, T, ink):
    """Mini diagram inside an 84 x 36 box at (x, y)."""
    P, F, G = T["purple_fill"], T["faint"], T["grn2"]
    m = y + 18
    if kind == "watermark":
        o = [path(f"M{x},{m}H{x + 84}", ink, 1.2, opacity=0.5), rect(x + 40, y + 4, 12, 28, P, rx=3, opacity=0.18),
             path(f"M{x + 52},{y + 2}V{y + 34}", P, 2)]
        o += [circle(x + 6 + i * 13, m, 3.2, F if i < 4 else P) for i in range(7)]
        return "".join(o)
    if kind == "hash":
        o = []
        for i, (lab, hot) in enumerate([("#a1", False), ("#a1", False), ("#9f", True)]):
            o += [rect(x + i * 29, y + 6, 25, 24, P if hot else "none", ink if not hot else None, 1.2, 6,
                       opacity=None if hot else 0.6),
                  text(x + i * 29 + 12.5, y + 21.5, lab, "#FFFFFF" if hot else ink, 9, 700, "middle", "mono")]
        return "".join(o)
    if kind == "settled":
        o = []
        for i in range(5):
            cx = x + 7 + i * 16
            if i < 3:
                o += [circle(cx, m, 7, G, opacity=0.25), path(f"M{cx - 3},{m}l2,2.5l4,-4.5", G, 1.6)]
            else:
                o.append(circle(cx, m, 6.5, "none", P, 1.6))
        return "".join(o) + arrowhead(x + 86, m, 0, P, 4)
    if kind == "poll":
        return (circle(x + 16, m, 12, "none", ink, 1.4, opacity=0.7) + path(f"M{x + 16},{m}V{m - 7}M{x + 16},{m}H{x + 22}", ink, 1.4)
                + path(f"M{x + 46},{y + 4}L{x + 38},{m + 2}H{x + 46}L{x + 42},{y + 32}L{x + 54},{m - 2}H{x + 46}Z", P, 1.4,
                       fill=P) + path(f"M{x + 60},{m}H{x + 82}", P, 1.4) + arrowhead(x + 84, m, 0, P, 5))
    if kind == "paging":
        o = [rect(x + 2 + i * 5, y + 3 + i * 4, 30, 22, T["card"], ink, 1.1, 4, opacity=0.9) for i in range(3)]
        o += [path(f"M{x + 50},{m}H{x + 84}", ink, 1.2, opacity=0.5), rect(x + 50, y + 10, 16, 16, P, rx=4),
              rect(x + 68, y + 10, 16, 16, "none", P, 1.4, 4)]
        return "".join(o)
    if kind == "graphql":
        o = [circle(x + 6, m, 4, ink, opacity=0.7)]
        o += [path(f"M{x + 10},{m}L{x + 30},{y + 6 + i * 12}", ink, 1, opacity=0.6) for i in range(3)]
        o += [circle(x + 32, y + 6 + i * 12, 3, ink, opacity=0.7) for i in range(3)]
        o += [circle(x + 52, m, 4, P), path(f"M{x + 56},{m}H{x + 66}M{x + 66},{y + 8}V{y + 28}M{x + 66},{y + 8}H{x + 76}"
                                             f"M{x + 66},{m}H{x + 80}M{x + 66},{y + 28}H{x + 76}", P, 1.4)]
        return "".join(o)
    if kind == "ids":
        o = []
        for i, lab in enumerate(["ord:123", "ret:123"]):
            o += [rect(x + 2, y + 2 + i * 17, 78, 15, "none", P if i else ink, 1.2, 7.5, opacity=None if i else 0.6),
                  text(x + 41, y + 13 + i * 17, lab, P if i else ink, 9, 700, "middle", "mono")]
        return "".join(o)
    if kind == "backoff":
        o, cx = [path(f"M{x},{y + 32}H{x + 84}", ink, 1.2, opacity=0.5)], x + 2
        for i, h in enumerate([8, 12, 17, 23, 30]):
            o.append(rect(cx, y + 32 - h, 6, h, P, rx=2, opacity=0.35 + i * 0.15))
            cx += 6 + 3 * (2 ** i) / 2 + 2
        return "".join(o)
    # checkpoint
    return (path(f"M{x + 10},{y + 30}V{y + 8}M{x + 3},{y + 15}l7,-7l7,7", ink, 1.6) + path(f"M{x + 26},{m}H{x + 40}", F, 1.4)
            + circle(x + 50, m, 9, G, opacity=0.25) + path(f"M{x + 45},{m}l3.5,3.5l6,-6.5", G, 1.8)
            + path(f"M{x + 62},{m}H{x + 70}", F, 1.4) + path(f"M{x + 74},{y + 32}V{y + 6}h9l-3,4l3,4h-9", P, 1.6))


def _card(T, x, y, w, h, i, c, diagram):
    eb, title, body, used, tone, kind, biz = c
    fill, ink = T["bubbles"][tone]
    o = [card(x, y, w, h, T, 16), rect(x + 1, y + 1, w - 2, 58, fill, rx=15),
         rect(x + 1, y + 44, w - 2, 15, fill), rect(x, y, w, h, "none", T["card_line"], 1, 16),
         mono_label(x + 18, y + 26, f"{i + 1:02d} · {eb}", ink, 9.5, "start", 1.6, 700),
         diagram(kind, x + w - 102, y + 11, T, ink),
         text(x + 18, y + 88, title, T["ink"], 16.5, 800, font="display", spacing=-0.4)]
    s, _ = para(x + 18, y + 111, body, T["ink2"], 12.5, w - 34, 17.5)
    o.append(s)
    o.append(mono_label(x + 18, y + 184, "→ business", T["muted"], 8.5, "start", 1.4, 700))
    s, _ = para(x + 18, y + 201, biz, T["ink"], 12.5, w - 34, 16, 700)
    o.append(s)
    return "".join(o)


def grid(T, eyebrow_text, head, accent, items, diagram, glow_colours=None):
    """3-column concept-card panel shared by the sync and agent panels."""
    cw, ch, g, top = 290, 246, 17, 150
    rows = -(-len(items) // 3)
    H = top + rows * ch + (rows - 1) * g + 40
    o = [paper(W, H, T, ((1.02, -0.05, 0.36), (-0.04, 1.04, 0.4)), glow_colours),
         eyebrow(56, 64, eyebrow_text, accent),
         rich(54, 112, [[(head[0], None), (head[1], accent)]], T["ink"], 38, 40)]
    for i, c in enumerate(items):
        r, k = divmod(i, 3)
        o.append(_card(T, 48 + k * (cw + g), top + r * (ch + g), cw, ch, i, c, diagram))
    return W, H, "".join(o)


def concepts(T):
    return grid(T, "How sync actually works", ("The concepts behind ", "every connector I ship."), T["purple"],
                CONCEPTS, _diagram)
