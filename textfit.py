"""Text measuring for layout. Helvetica / Helvetica-Bold advance widths (per 1000 em),
which track SF Pro / Segoe / Inter closely enough for wrapping. Mono is 0.6 em."""

_CHARS = "".join(chr(c) for c in range(32, 127))
_REG = [278, 278, 355, 556, 556, 889, 667, 191, 333, 333, 389, 584, 278, 333, 278, 278, 556, 556, 556, 556, 556, 556,
        556, 556, 556, 556, 278, 278, 584, 584, 584, 556, 1015, 667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667,
        556, 833, 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 278, 278, 278, 469, 556, 333, 556,
        556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222, 833, 556, 556, 556, 556, 333, 500, 278, 556, 500, 722,
        500, 500, 500, 334, 260, 334, 584]
_BOLD = [278, 333, 474, 556, 556, 889, 722, 238, 333, 333, 389, 584, 278, 333, 278, 278, 556, 556, 556, 556, 556, 556,
         556, 556, 556, 556, 333, 333, 584, 584, 584, 611, 975, 722, 722, 722, 722, 667, 611, 778, 722, 278, 556, 722,
         611, 833, 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 333, 278, 333, 584, 556, 333, 556,
         611, 556, 611, 556, 333, 611, 611, 278, 278, 556, 278, 889, 611, 611, 611, 611, 389, 556, 333, 611, 556, 778,
         556, 556, 500, 389, 280, 389, 584]
_EXTRA = {"–": 556, "—": 1000, "→": 1000, "·": 278, "’": 278, "×": 584, "≈": 584, "~": 584}
REG = dict(zip(_CHARS, _REG), **_EXTRA)
BOLD = dict(zip(_CHARS, _BOLD), **_EXTRA)


def tw(s, size, weight=400, mono=False, spacing=0.0):
    """Width in px of string s. Heavy weights get a small safety margin."""
    if mono:
        return len(s) * (size * 0.6 + spacing)
    table = BOLD if weight >= 600 else REG
    k = 1.04 if weight >= 800 else 1.06
    return sum(table.get(c, 600) for c in s) * size / 1000 * k + spacing * len(s)


def wrap(s, maxw, size, weight=400, mono=False):
    out, cur = [], ""
    for word in s.split():
        trial = f"{cur} {word}".strip()
        if cur and tw(trial, size, weight, mono) > maxw:
            out.append(cur)
            cur = word
        else:
            cur = trial
    return out + ([cur] if cur else [])
