#!/usr/bin/env python3
"""Wrap a chart SVG into the self-contained HTML preview with PNG + SVG download buttons.

Usage: build_preview.py chart.svg out.html [--name file-stem]
Reads the canvas height from the SVG, escapes the SVG for a JS template literal,
and fills assets/preview-template.html.
"""
import argparse, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "assets" / "preview-template.html"
FONT_CSS = HERE.parent / "assets" / "inter-embed.css"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("svg")
    ap.add_argument("out")
    ap.add_argument("--name", help="download file stem (default: output file stem)")
    a = ap.parse_args()

    svg = pathlib.Path(a.svg).read_text(encoding="utf-8").strip()
    svg = re.sub(r"^<\?xml[^>]*>\s*", "", svg)
    m = re.search(r"<svg\b[^>]*\bheight=\"([\d.]+)\"", svg)
    if not m:
        sys.exit("ERROR: root <svg> needs a numeric height attribute")
    h = m.group(1)
    w = re.search(r"<svg\b[^>]*\bwidth=\"([\d.]+)\"", svg)
    if not w or float(w.group(1)) != 720:
        sys.exit("ERROR: root <svg> width must be 720")

    escaped = svg.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
    name = a.name or pathlib.Path(a.out).stem
    html = (TEMPLATE.read_text(encoding="utf-8")
            .replace("{NAME}", name)
            .replace("{H}", h)
            .replace("{FONT_CSS}", FONT_CSS.read_text(encoding="utf-8"))
            .replace("{SVG_ESCAPED}", escaped))
    pathlib.Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(a.out).write_text(html, encoding="utf-8")
    print(f"Wrote {a.out} (720x{h}, downloads as {name}.png / {name}.svg)")


if __name__ == "__main__":
    main()
