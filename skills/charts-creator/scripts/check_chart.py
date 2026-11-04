#!/usr/bin/env python3
"""Lint a charts-creator SVG and render a PNG for visual review.

Usage: check_chart.py chart.svg [--preset example-feedback|editorial] [--no-render]

ERRORs must be fixed before delivery. WARNINGs need a human-eye judgment.
Text boxes are measured with the real Inter metrics (downloaded on first run if missing),
so overflow/collision reports are close to what the browser renders.
"""
import argparse, io, os, pathlib, re, subprocess, sys, urllib.request, zipfile
from lxml import etree

NS = "{http://www.w3.org/2000/svg}"
FONT_DIR = pathlib.Path.home() / ".fonts" / "inter"
INTER_ZIP = "https://github.com/rsms/inter/releases/download/v4.0/Inter-4.0.zip"
WEIGHT_FILES = {400: "Inter-Regular.ttf", 600: "Inter-SemiBold.ttf", 700: "Inter-Bold.ttf", 800: "Inter-ExtraBold.ttf", 900: "Inter-Black.ttf"}
MIN_SIZE = 14
MAX_TEXT_RUNS = 35

PALETTES = {
    "example-feedback": """#FFFFFF #2F6FEB #1F5AD6 #1A48A8 #CFE0FB #E8F0FD #F2643D #F58A6A #FAC3B1
        #D4602F #F5C243 #C9EFEA #5CCFC0 #3B8C82 #1A1A2E #44475A #6B6E7B #9B9DA8 #D0D2DA
        #E2E3E9 #F1F2F5 #F8F8FA #5DC98A #F0C04F #C8414F""",
    "editorial": """#FFFFFF #2F6FEB #F2643D #F5C243 #5CCFC0 #1F5AD6 #F58A6A #3B8C82 #9B9DA8
        #F1F2F5 #E2E3E9 #111111 #374151 #6B7280 #9CA3AF""",
}
# Your product UI grays (brand tokens). Charts use the chart grays instead, so list the
# UI grays here and the checker will flag them. Empty by default.
BRAND_TOKEN_GRAYS = set()

issues = []
MARKS, CALLOUTS = [], []  # data polylines/points and dark callout boxes
SHAPES = []  # filled rects (bars, pills, segments) for inside-label centering

MINOR = {"a", "an", "the", "and", "but", "or", "nor", "for", "so", "yet",
         "at", "by", "in", "of", "on", "to", "up", "per", "via", "vs", "vs."}

def title_case_problems(title):
    probs = []
    words = title.split()
    for i, w in enumerate(words):
        core = w.strip(".,:;!?()\"'")
        for part in core.split("-"):
            if not part or not part[0].isalpha():
                continue
            edge = i == 0 or i == len(words) - 1
            if part.lower() in MINOR and not edge and "-" not in core:
                if part[0].isupper():
                    probs.append(f"'{part}' should be lowercase")
            elif part[0].islower():
                probs.append(f"'{part}' should be capitalized")
    return probs
def err(m): issues.append(("ERROR", m))
def warn(m): issues.append(("WARN", m))


def ensure_inter():
    if all((FONT_DIR / f).exists() for f in WEIGHT_FILES.values()):
        return True
    try:
        data = urllib.request.urlopen(INTER_ZIP, timeout=60).read()
        FONT_DIR.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            for f in WEIGHT_FILES.values():
                (FONT_DIR / f).write_bytes(z.read(f"extras/ttf/{f}"))
        subprocess.run(["fc-cache", "-f", str(FONT_DIR)], capture_output=True)
        return True
    except Exception as e:  # network blocked etc.
        print(f"note: could not fetch Inter ({e}); measurements approximate", file=sys.stderr)
        return False


_fonts = {}
def measure(text, size, weight, spacing, have_inter):
    try:
        from PIL import ImageFont
        w = 900 if weight >= 850 else 800 if weight >= 750 else 700 if weight >= 650 else 600 if weight >= 550 else 400
        key = (w, size)
        if key not in _fonts:
            path = FONT_DIR / WEIGHT_FILES[w] if have_inter else None
            _fonts[key] = ImageFont.truetype(str(path), size) if path else ImageFont.load_default(size)
        width = _fonts[key].getlength(text)
    except Exception:
        width = len(text) * size * 0.56
    return width + spacing * max(len(text) - 1, 0)


def num(v, default=None):
    if v is None:
        return default
    m = re.match(r"\s*(-?[\d.]+)", str(v))
    return float(m.group(1)) if m else default


def parse_transform(t):
    """Return (dx, dy, scaled) for translate/scale-only transforms."""
    dx = dy = 0.0; scaled = False
    for fn, args in re.findall(r"(\w+)\s*\(([^)]*)\)", t or ""):
        vals = [float(x) for x in re.split(r"[\s,]+", args.strip()) if x]
        if fn == "translate":
            dx += vals[0]; dy += vals[1] if len(vals) > 1 else 0
        elif fn == "scale":
            scaled = True
        else:
            scaled = True  # rotate/matrix: skip geometry checks
    return dx, dy, scaled


def in_clip(el):
    p = el.getparent()
    while p is not None:
        if etree.QName(p).localname in ("clipPath", "defs", "mask"):
            return True
        p = p.getparent()
    return False


INHERIT = ("font-size", "font-weight", "font-family", "text-anchor", "letter-spacing", "fill")


def walk(el, ctx, dx, dy, scaled, texts, colors, fams):
    tag = etree.QName(el).localname if isinstance(el.tag, str) else None
    if tag is None:
        return
    ctx = dict(ctx)
    for k in INHERIT:
        if el.get(k) is not None:
            ctx[k] = el.get(k)
    style = el.get("style") or ""
    for k, v in re.findall(r"([\w-]+)\s*:\s*([^;]+)", style):
        if k in INHERIT:
            ctx[k] = v.strip()
    if el.get("class"):
        warn(f"<{tag} class=\"{el.get('class')}\">: use presentation attributes, not CSS classes")
    tdx, tdy, ts = parse_transform(el.get("transform"))
    dx, dy, scaled = dx + tdx, dy + tdy, scaled or ts
    for attr in ("fill", "stroke", "stop-color"):
        v = el.get(attr)
        if v:
            colors.append((v, tag))
    for v in re.findall(r"(?:fill|stroke)\s*:\s*(#[0-9a-fA-F]{3,6})", style):
        colors.append((v, tag))
    if el.get("font-family"):
        fams.add(el.get("font-family"))
    if tag == "text":
        collect_text(el, ctx, dx, dy, scaled, texts)
        return
    if not scaled and tag == "polyline":
        pts = [float(v) for v in re.split(r"[\s,]+", (el.get("points") or "").strip()) if v]
        pts = [(pts[i] + dx, pts[i + 1] + dy) for i in range(0, len(pts) - 1, 2)]
        MARKS.append(("line", pts, float(num(el.get("stroke-width"), 1))))
    if not scaled and tag == "circle":
        MARKS.append(("dot", (num(el.get("cx"), 0) + dx, num(el.get("cy"), 0) + dy), num(el.get("r"), 0)))
    if not scaled and tag == "rect" and not in_clip(el) and (el.get("fill") or "none").lower() not in ("none", "#ffffff", "white"):
        x, y = num(el.get("x"), 0) + dx, num(el.get("y"), 0) + dy
        SHAPES.append((x, y, x + num(el.get("width"), 0), y + num(el.get("height"), 0), (el.get("fill") or "").upper()))
    if not scaled and tag == "rect" and (el.get("fill") or "").upper() in ("#1A1A2E", "#2F6FEB") and num(el.get("rx"), 0) == 6:
        x, y = num(el.get("x"), 0) + dx, num(el.get("y"), 0) + dy
        CALLOUTS.append((x, y, x + num(el.get("width"), 0), y + num(el.get("height"), 0)))
    if tag == "style":
        return
    for ch in el:
        walk(ch, ctx, dx, dy, scaled, texts, colors, fams)


def collect_text(el, ctx, dx, dy, scaled, texts):
    lines = []  # (x, y, string, ctx)
    x, y = num(el.get("x"), 0), num(el.get("y"), 0)
    cur = {"x": x, "y": y, "s": (el.text or ""), "ctx": ctx}
    for ts in el:
        tctx = dict(ctx)
        for k in INHERIT:
            if ts.get(k) is not None:
                tctx[k] = ts.get(k)
        if ts.get("x") is not None or ts.get("y") is not None:
            if cur["s"].strip():
                lines.append(cur)
            cur = {"x": num(ts.get("x"), cur["x"]),
                   "y": num(ts.get("y"), cur["y"]) + num(ts.get("dy"), 0),
                   "s": ts.text or "", "ctx": tctx}
        else:
            cur["s"] += ts.text or ""
        cur["s"] += ts.tail or ""
    if cur["s"].strip():
        lines.append(cur)
    for ln in lines:
        texts.append((ln["x"] + dx, ln["y"] + dy, ln["s"].strip(), ln["ctx"], scaled))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("svg")
    ap.add_argument("--preset", default="example-feedback", choices=PALETTES)
    ap.add_argument("--no-render", action="store_true")
    a = ap.parse_args()

    raw = pathlib.Path(a.svg).read_text(encoding="utf-8")
    try:
        root = etree.fromstring(raw.encode("utf-8"))
    except etree.XMLSyntaxError as e:
        print(f"ERROR: invalid XML: {e}"); sys.exit(1)

    W, H = num(root.get("width")), num(root.get("height"))
    vb = (root.get("viewBox") or "").split()
    if W != 720: err(f"width is {W}, must be 720")
    if H is None: err("root <svg> needs a numeric height"); H = 0
    if len(vb) != 4 or float(vb[2]) != W or float(vb[3]) != H:
        err(f"viewBox '{root.get('viewBox')}' must be '0 0 {W:g} {H:g}'")
    if H % 1: warn(f"height {H} is fractional: round it")

    if re.search(r"<script|<image|<foreignObject|<filter", raw):
        err("no <script>, <image>, <foreignObject> or <filter> allowed")
    if "fonts.googleapis.com/css2?family=Inter" not in raw:
        err("missing Inter @import in <defs><style>")
    for fam in re.findall(r"font-family\s*[:=]\s*[\"']?([^;\"'>]+)", raw):
        if fam.split(",")[0].strip().strip("'\"") != "Inter":
            err(f"font-family '{fam}': only Inter is allowed")

    # background rect
    first_shape = next((e for e in root.iter() if isinstance(e.tag, str)
                        and etree.QName(e).localname in ("rect", "path", "circle", "g", "line", "text")
                        and etree.QName(e).localname != "g"), None)
    if first_shape is None or etree.QName(first_shape).localname != "rect" \
            or (first_shape.get("fill") or "").upper() not in ("#FFFFFF", "#FFF", "WHITE") \
            or num(first_shape.get("width")) != W or num(first_shape.get("height")) != H:
        err("first drawn element must be a #FFFFFF rect covering the full canvas")

    texts, colors, fams = [], [], set()
    walk(root, {}, 0, 0, False, texts, colors, fams)

    # palette
    allowed = set(PALETTES[a.preset].split())
    for c, tag in colors:
        cu = c.strip().upper()
        if cu in ("NONE", "TRANSPARENT", "CURRENTCOLOR") or cu.startswith("URL("):
            continue
        if cu in ("WHITE",): cu = "#FFFFFF"
        if len(cu) == 4 and cu.startswith("#"):
            cu = "#" + "".join(ch * 2 for ch in cu[1:])
        if cu in BRAND_TOKEN_GRAYS:
            err(f"{c} on <{tag}> is a brand-token gray: charts use the chart grays")
        elif cu not in allowed:
            err(f"{c} on <{tag}> is not in the {a.preset} chart palette")
    for ln in root.iter("{http://www.w3.org/2000/svg}line"):
        if (ln.get("stroke") or "").upper() == "#E2E3E9" and num(ln.get("x1")) == 20 and num(ln.get("x2")) == 700 \
                and num(ln.get("y1"), 0) > H - 120 and num(ln.get("y1")) != H - 68 and a.preset == "example-feedback":
            err(f"footer divider at y={num(ln.get('y1')):g}: must be at H-68 ({H - 68:g})")
    if a.preset == "example-feedback" and "scale(0.135)" not in raw:
        err("Example Feedback logo missing (expected translate(20, H-40) scale(0.135))")
    elif a.preset == "example-feedback":
        m = re.search(r"translate\(\s*([\d.]+)[ ,]+([\d.]+)\s*\)\s*scale\(0\.135\)", raw)
        if not m or float(m.group(1)) != 20 or float(m.group(2)) != H - 40:
            err(f"logo must be at translate(20, {H - 40:g}) scale(0.135)")

    have_inter = ensure_inter()
    boxes = []
    for x, y, s, ctx, scaled in texts:
        size = num(ctx.get("font-size"), 16)
        weight = {"bold": 700, "normal": 400}.get(str(ctx.get("font-weight")), num(ctx.get("font-weight"), 400))
        if size < MIN_SIZE:
            err(f"'{s[:40]}' is {size:g}px: minimum is {MIN_SIZE}px")
        if weight < 900 and (size >= 40 or (size >= 28 and y <= 160)):
            warn(f"'{s[:40]}' is {size:g}px at weight {weight:g}: titles and hero numbers use 900")
        if weight not in (400, 600, 700, 800, 900):
            warn(f"'{s[:40]}' uses weight {weight:g}: use 400/600/700/800/900")
        if a.preset == "example-feedback" and str(ctx.get("fill", "")).upper() == "#44475A":
            warn(f"'{s[:40]}' uses #44475A: that gray is non-text only; use #1A1A2E")
        if a.preset == "example-feedback" and str(ctx.get("fill", "")).upper() in ("#6B6E7B", "#44475A") and weight >= 600:
            warn(f"'{s[:40]}' is gray at weight {weight:g}: gray text is only for footer meta and axis ticks (400)")
        if a.preset == "example-feedback" and str(ctx.get("fill", "")).upper() == "#9B9DA8":
            err(f"'{s[:40]}' uses #9B9DA8 text (2.7:1 contrast): use #6B6E7B")
        if scaled:
            continue
        w = measure(s, size, weight, num(ctx.get("letter-spacing"), 0), have_inter)
        anchor = ctx.get("text-anchor", "start")
        x0 = x - w if anchor == "end" else x - w / 2 if anchor == "middle" else x
        box = (x0, y - size * 0.73, x0 + w, y + size * 0.22, s)
        boxes.append(box)
        if box[0] < 19.5 or box[2] > 700.5:
            err(f"'{s[:40]}' spans x {box[0]:.0f}..{box[2]:.0f}: must stay within 20..700")
        if box[1] < 30:
            warn(f"'{s[:40]}' top at y {box[1]:.0f}: header starts at the 40px margin")
        if box[3] > H - 16:
            err(f"'{s[:40]}' bottom at y {box[3]:.0f} runs into the bottom margin (H={H:g})")

    # title vs eyebrow: needs 24px clearance
    titles = [b for b, (_, _, _, c, _) in zip(boxes, [t for t in texts if not t[4]])
              if num(c.get("font-size"), 0) >= 30]
    eyebrows = [b for b in boxes if b[2] >= 699 and b[1] < 70]
    for b in eyebrows:
        if b not in titles:
            err(f"'{b[4]}' sits right of the title: report labels go in the pill above the title")
    for t in titles:
        for e in eyebrows:
            if e is not t and e[1] < t[3] and t[1] < e[3] and e[0] - t[2] < 24:
                err(f"title '{t[4][:30]}' is {e[0] - t[2]:.0f}px from eyebrow '{e[4]}': "
                    "needs 24px; wrap the title to two lines")

    # headline rules
    title_runs = sorted((t[1], t[2]) for t in texts if num(t[3].get("font-size"), 0) >= 28 and t[1] <= 160)
    if title_runs:
        title = " ".join(s for _, s in title_runs)
        for p_ in title_case_problems(title):
            err(f"title case: {p_} in '{title}'")
        if title.rstrip().endswith("."):
            err("title ends with a period: headlines have none")
    for t in texts:
        if "\u2013" in t[2] or "\u2014" in t[2]:
            err(f"'{t[2][:40]}' uses an en/em dash: use a hyphen or rephrase (house style)")

    # labels inside bars/pills/segments must be centered
    for b in boxes:
        inside = [r for r in SHAPES if r[0] - 0.5 <= b[0] and b[2] <= r[2] + 0.5 and r[1] - 0.5 <= b[1] and b[3] <= r[3] + 0.5
                  and (r[2] - r[0]) < W - 1 and not any(abs(r[0] - c[0]) < .6 and abs(r[1] - c[1]) < .6 for c in CALLOUTS)]
        if not inside:
            continue
        r = inside[-1]  # topmost shape under the label (document order)
        stacked = sum(1 for o in boxes if r[0] - 0.5 <= o[0] and o[2] <= r[2] + 0.5 and r[1] - 0.5 <= o[1] and o[3] <= r[3] + 0.5) > 1
        size = (b[3] - b[1]) / 0.95
        tcx, tcy = (b[0] + b[2]) / 2, b[3] - 0.22 * size - 0.36 * size
        rcx, rcy = (r[0] + r[2]) / 2, (r[1] + r[3]) / 2
        if abs(tcx - rcx) > 1.5 or (not stacked and abs(tcy - rcy) > 2.5):
            err(f"'{b[4][:30]}' sits inside a bar but isn't centered (off by {tcx - rcx:+.0f}px x, {tcy - rcy:+.0f}px y)")

    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            a1, b1 = boxes[i], boxes[j]
            gx = max(a1[0], b1[0]) - min(a1[2], b1[2])
            gy = max(a1[1], b1[1]) - min(a1[3], b1[3])
            if gx < 0 and gy < 0:
                err(f"text collision: '{a1[4][:30]}' overlaps '{b1[4][:30]}'")
            elif gx < 4 and gy < 0:
                warn(f"tight: '{a1[4][:30]}' and '{b1[4][:30]}' are {gx:.1f}px apart (min 4)")

    # labels and callouts must not sit on data lines or points
    def seg_hits_box(p, q, b, pad):
        x0, y0, x1, y1 = b[0] - pad, b[1] - pad, b[2] + pad, b[3] + pad
        for t in [i / 40 for i in range(41)]:
            x, y = p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t
            if x0 <= x <= x1 and y0 <= y <= y1:
                return True
        return False
    def box_in(b, c):  # text fully inside a callout box
        return c[0] <= b[0] and b[2] <= c[2] and c[1] <= b[1] and b[3] <= c[3]
    targets = [("callout", c) for c in CALLOUTS] + \
              [("label '" + b[4][:30] + "'", b) for b in boxes if not any(box_in(b, c) for c in CALLOUTS)]
    for name, b in targets:
        for kind, geo, w in MARKS:
            if kind == "line":
                if any(seg_hits_box(geo[i], geo[i + 1], b, w / 2) for i in range(len(geo) - 1)):
                    err(f"{name} covers a data line: move it into clear space"); break
            else:
                (cx, cy), r = geo, w
                if b[0] - r < cx < b[2] + r and b[1] - r < cy < b[3] + r:
                    err(f"{name} covers a data point at ({cx:.0f},{cy:.0f})"); break

    prose = [t for t in texts if len(t[2].split()) >= 6]
    if len(prose) > 6:
        warn(f"{len(prose)} prose lines: trim explanatory text (keep all data values)")

    for level, m in issues:
        print(f"{level}: {m}")
    n_err = sum(1 for l, _ in issues if l == "ERROR")
    print(f"\n{n_err} error(s), {len(issues) - n_err} warning(s); {len(boxes)} text runs measured"
          + ("" if have_inter else " (approximate: Inter unavailable)"))

    if not a.no_render:
        try:
            import cairosvg
        except ImportError:
            subprocess.run([sys.executable, "-m", "pip", "install", "-q", "cairosvg",
                            "--break-system-packages"], capture_output=True)
            try:
                import cairosvg
            except ImportError:
                cairosvg = None
        if cairosvg:
            out = str(pathlib.Path(a.svg).with_suffix(".check.png"))
            offline = re.sub(r"@import url\([^)]*\);", "", raw)
            cairosvg.svg2png(bytestring=offline.encode(), write_to=out, output_width=1440)
            print(f"Rendered {out}: view it and review the composition before delivering.")
        else:
            print("note: cairosvg unavailable; skipped render: review the SVG by hand.")
    sys.exit(1 if n_err else 0)


if __name__ == "__main__":
    main()
