"""Preview renderers (dev only, not stdlib): PyMuPDF per-panel PNGs + stitched README-order pages, and,
when Google Chrome is installed, browser-faithful screenshots (gradients, dashes, letter-spacing, SMIL frame).
MuPDF ignores dasharray/letter-spacing, so the chrome-* files are the ones to judge design by."""
import shutil
import subprocess
import tempfile
from pathlib import Path

from theme import THEMES

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
GAP, PAD, SCALE = 18, 28, 1.5
BG = {"light": "#FFFFFF", "dark": "#0D1117"}  # GitHub page colours


def _mupdf(files, names, order, out):
    import fitz
    for theme in THEMES:
        for n in names:
            src = fitz.open(stream=files[(n, theme)][0].encode(), filetype="svg")
            src[0].get_pixmap(matrix=fitz.Matrix(SCALE, SCALE)).save(out / f"{n}-{theme}.png")
        W = max(files[(n, theme)][1] for n in order) + PAD * 2
        H = PAD * 2 + sum(files[(n, theme)][2] for n in order) + GAP * (len(order) - 1)
        pdf = fitz.open()
        page = pdf.new_page(width=W, height=H)
        page.draw_rect(page.rect, color=None, fill=tuple(int(BG[theme][i:i + 2], 16) / 255 for i in (1, 3, 5)))
        y = PAD
        for n in order:
            svg, w, h = files[(n, theme)]
            sp = fitz.open("pdf", fitz.open(stream=svg.encode(), filetype="svg").convert_to_pdf())
            page.show_pdf_page(fitz.Rect(PAD, y, PAD + w, y + h), sp, 0)
            y += h + GAP
        page.get_pixmap(matrix=fitz.Matrix(1, 1)).save(out / f"full-{theme}.png")


def _shot(dest, w, h, url):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--screenshot={dest}",
                    f"--window-size={w},{h}", "--virtual-time-budget=1500", url],
                   check=True, capture_output=True, timeout=90)


def _chrome(files, names, order, out):
    if not Path(CHROME).exists():
        print("chrome not found; skipping browser previews")
        return
    tmp = Path(tempfile.mkdtemp(prefix="ghprof-"))
    try:
        for theme in THEMES:
            for n in names:
                (tmp / f"{n}-{theme}.svg").write_text(files[(n, theme)][0])
            imgs = "".join(f'<img src="{n}-{theme}.svg" style="display:block;width:880px;margin:0 0 {GAP}px">'
                           for n in order)
            (tmp / f"page-{theme}.html").write_text(
                f'<!doctype html><html><body style="margin:0;padding:{PAD}px;background:{BG[theme]}">{imgs}</body></html>')
            H = PAD * 2 + sum(round(files[(n, theme)][2] * 0.88) + GAP for n in order)
            _shot(out / f"chrome-full-{theme}.png", 880 + PAD * 2, H, f"file://{tmp}/page-{theme}.html")
            for n in names:
                _, w, h = files[(n, theme)]
                _shot(out / f"chrome-{n}-{theme}.png", w, h, f"file://{tmp}/{n}-{theme}.svg")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def render_all(files, names, order, out):
    out.mkdir(exist_ok=True)
    _mupdf(files, names, order, out)
    _chrome(files, names, order, out)
    print(f"previews -> {out}")
