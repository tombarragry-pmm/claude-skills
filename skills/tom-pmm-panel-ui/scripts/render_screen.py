#!/usr/bin/env python3
"""Check an app screen mockup HTML file against the token rules, then render it to PNG.

Usage:
  render_screen.py screen.html out.png [--width 1440] [--height 900] [--scale auto]
                   [--selector CSS] [--full-page]

- Output size: every deliverable is 1600px wide at 1x and 3200px at 2x. With --scale auto
  (default) the pixel ratio is chosen so the captured screen or element is 3200px wide; the
  preview then exports exactly 3200 / 1600 wide, with or without a background. The ratio and
  the CSS width are stored in the PNG (tEXt "mockup-scale", "mockup-css-width").

- Rendering is offline: Google Fonts and the lucide CDN script are swapped for the
  copies bundled in assets/vendor, and every other network request is blocked.
- --selector crops the screenshot to one element (e.g. a dialog or a card).
- --full-page captures the whole scroll height (only for pages without the fixed shell).
- Lint: ERROR for hex colors that are not tokens (every hex in references/tokens.md counts as one),
  raw Tailwind gray/neutral classes and text under 10px; WARNING for hex values written outside
  the :root block.
"""
import argparse, pathlib, re, sys, tempfile, shutil

HERE = pathlib.Path(__file__).resolve().parent
VENDOR = HERE.parent / "assets" / "vendor"
ILLUSTRATIONS = HERE.parent / "assets" / "illustrations"

TOKENS_FILE = HERE.parent / "references" / "tokens.md"
TOKENS = {"fff", "ffffff", "000", "000000"} | {
    h.lower() for h in re.findall(r"#([0-9a-fA-F]{3,8})\b", TOKENS_FILE.read_text(encoding="utf-8"))
}

FONT_FACES = "\n".join(
    f"@font-face{{font-family:'Inter';font-style:normal;font-weight:{w};font-display:block;"
    f"src:url('{(VENDOR / 'fonts' / f'inter-{sub}-{w}-normal.woff2').as_uri()}') format('woff2');"
    f"unicode-range:{rng};}}"
    for w in (400, 500, 600, 700)
    for sub, rng in (
        ("latin", "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"),
        ("latin-ext", "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF"),
    )
)


def lint(html: str):
    errors, warnings = [], []
    root = re.search(r":root\s*\{.*?\}", html, re.S)
    root_txt = root.group(0) if root else ""
    rest = html.replace(root_txt, "") if root_txt else html
    for h in sorted(set(m.lower() for m in re.findall(r"#([0-9a-fA-F]{3,8})\b", html))):
        if h not in TOKENS:
            errors.append(f"#{h} is not a token (see references/tokens.md)")
    outside = sorted(set(m.lower() for m in re.findall(r"#([0-9a-fA-F]{3,8})\b", rest)))
    outside = [h for h in outside if h in TOKENS and h not in {"fff", "ffffff", "000", "000000"}]
    if outside:
        warnings.append("hex written outside :root, use var(--token) instead: " + ", ".join("#" + h for h in outside))
    for c in sorted(set(re.findall(r"\b(?:text|bg|border|ring)-(?:gray|neutral|slate|zinc)-\d{2,3}\b", html))):
        errors.append(f"raw Tailwind palette class {c}; use a semantic token")
    for px in re.findall(r"font-size\s*:\s*(\d+(?:\.\d+)?)px", html):
        if float(px) < 10:
            errors.append(f"font-size {px}px is below the 10px minimum (text-2xs)")
    return errors, warnings


def inline_illustrations(html: str):
    """Replace <div class="illustration" data-illustration="dashboards/empty-state" ...></div>
    with the SVG of the same name from assets/illustrations."""
    missing = []
    def rep(m):
        tag, ident = m.group(0), m.group(2)
        f = ILLUSTRATIONS / f"{ident}.svg"
        if not f.exists():
            missing.append(ident); return tag
        svg = f.read_text(encoding="utf-8")
        svg = re.sub(r"<\?xml[^>]*>", "", svg)
        svg = re.sub(r"<svg\b", '<svg width="100%" height="100%" preserveAspectRatio="xMidYMid meet"', svg, count=1)
        return m.group(1).replace('class="illustration"', 'class="illustration has-art"') + svg + "</div>"
    html = re.sub(r'(<div[^>]*class="illustration"[^>]*data-illustration="([^"]+)"[^>]*>)[^<]*</div>', rep, html)
    return html, missing


def prepare(src: pathlib.Path, tmp: pathlib.Path) -> pathlib.Path:
    html = src.read_text(encoding="utf-8")
    html, missing = inline_illustrations(html)
    for ident in missing:
        print(f"WARNING: no illustration '{ident}' in assets/illustrations (see assets/illustrations/README.md)")
    html = re.sub(r"<link[^>]+fonts\.googleapis\.com[^>]*>", "", html)
    html = re.sub(r"<link[^>]+fonts\.gstatic\.com[^>]*>", "", html)
    html = re.sub(r"@import\s+url\([^)]*fonts\.googleapis[^)]*\);?", "", html)
    html = html.replace("<head>", "<head>\n<style>" + FONT_FACES + "</style>", 1)
    html = re.sub(r'src="https://[^"]*lucide[^"]*"', f'src="{(VENDOR / "lucide.min.js").as_uri()}"', html)
    out = tmp / src.name
    for p in src.parent.iterdir():
        if p.is_file() and p != src and p.suffix.lower() in {".svg", ".png", ".jpg", ".jpeg", ".webp"}:
            shutil.copy(p, tmp / p.name)
    out.write_text(html, encoding="utf-8")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html"); ap.add_argument("png")
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--height", type=int, default=900)
    ap.add_argument("--scale", default="auto", help="pixel ratio, or auto = make the capture 3200px wide")
    ap.add_argument("--selector")
    ap.add_argument("--full-page", action="store_true")
    a = ap.parse_args()

    src = pathlib.Path(a.html)
    errors, warnings = lint(src.read_text(encoding="utf-8"))
    for w in warnings: print("WARNING:", w)
    for e in errors: print("ERROR:", e)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("Playwright is not available: pip install playwright --break-system-packages && playwright install chromium")

    with tempfile.TemporaryDirectory() as t:
        page_file = prepare(src, pathlib.Path(t))
        with sync_playwright() as p:
            b = p.chromium.launch()
            def load(dsf):
                pg = b.new_page(viewport={"width": a.width, "height": a.height}, device_scale_factor=dsf)
                pg.route("http*://**/*", lambda r: r.abort())
                pg.goto(page_file.as_uri())
                pg.evaluate("document.fonts.ready")
                pg.wait_for_timeout(300)
                return pg
            if a.scale == "auto":
                probe = load(1)
                if a.selector and probe.locator(a.selector).count():
                    css_w = probe.locator(a.selector).first.bounding_box()["width"]
                else:
                    css_w = a.width
                probe.close()
                scale = 3200 / css_w
            else:
                scale = float(a.scale)
                css_w = None
            pg = b.new_page(viewport={"width": a.width, "height": a.height}, device_scale_factor=scale)
            pg.route("http*://**/*", lambda r: r.abort())
            pg.goto(page_file.as_uri())
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(400)
            # Freeze any animated (SMIL) SVG at 2.5s so the capture is stable
            pg.evaluate("document.querySelectorAll('svg').forEach(s=>{if(s.pauseAnimations){s.pauseAnimations();s.setCurrentTime(2.5)}})")
            pg.wait_for_timeout(100)
            if pg.evaluate("typeof lucide") == "undefined" and "lucide" in page_file.read_text():
                print("WARNING: lucide did not load; icons are missing")
            ok_font = pg.evaluate("document.fonts.check('400 14px Inter')")
            if not ok_font:
                print("WARNING: Inter did not load; the render uses a fallback font")
            if a.selector and pg.locator(a.selector).count() == 0:
                b.close()
                sys.exit(f"ERROR: selector {a.selector!r} matches nothing in the page")
            target = pg.locator(a.selector).first if a.selector else pg
            kwargs = {"path": a.png}
            if not a.selector and a.full_page:
                kwargs["full_page"] = True
            target.screenshot(**kwargs)
            b.close()
    from PIL import Image
    from PIL.PngImagePlugin import PngInfo
    im = Image.open(a.png); info = PngInfo()
    if css_w is None: css_w = im.width / scale
    info.add_text("mockup-scale", f"{scale:.6f}"); info.add_text("mockup-css-width", f"{css_w:.2f}")
    im.save(a.png, pnginfo=info)
    a.scale = round(scale, 3)
    print(f"Rendered {a.png} ({'element ' + a.selector if a.selector else f'{a.width}x{a.height}'} @{a.scale}x, {im.width}px wide)"
          + (f" with {len(errors)} ERROR(s)" if errors else ""))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
