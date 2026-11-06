#!/usr/bin/env python3
"""Wrap a rendered screen PNG into the HTML preview.

The preview has a Background picker (None plus every gradient-N.jpg in assets/backgrounds), an
Annotate toolbar, and Download PNG (2x) / (1x) buttons. Exports are always 1600px wide at 1x and
3200px at 2x, with or without a background.

Usage: build_preview.py screen.png out.html [--name file-stem] [--scale N] [--background none|gradient-N]
--scale       pixel ratio of the render; read from the PNG written by render_screen.py, so only
              needed for PNGs made some other way (default 2)
--background  which option is selected when the preview opens (default none)
The PNG and the gradients are embedded, so the preview is one self-contained file.
"""
import argparse, base64, json, pathlib, struct

HERE = pathlib.Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "assets" / "preview-template.html"
BG_DIR = HERE.parent / "assets" / "backgrounds"


def png_size(data: bytes):
    return struct.unpack(">II", data[16:24])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("png"); ap.add_argument("out")
    ap.add_argument("--name", help="download file stem (default: output file stem)")
    ap.add_argument("--scale", type=float)
    ap.add_argument("--background", default="none")
    a = ap.parse_args()
    data = pathlib.Path(a.png).read_bytes()
    w, h = png_size(data)
    if a.scale is None:
        from PIL import Image
        a.scale = float(Image.open(a.png).info.get("mockup-scale", 2))
    name = a.name or pathlib.Path(a.out).stem
    bgs, swatches = {}, []
    n_bg = len(list(BG_DIR.glob("gradient-*.jpg")))
    for i in range(1, n_bg + 1):
        key = f"gradient-{i}"
        uri = "data:image/jpeg;base64," + base64.b64encode((BG_DIR / f"{key}.jpg").read_bytes()).decode()
        bgs[key] = uri
        swatches.append(f'<button class="sw" type="button" data-bg="{key}" aria-pressed="false" '
                        f'title="Gradient {i}" style="background-image:url({uri})"><span>{i}</span></button>')
    if a.background not in ("none", *bgs):
        raise SystemExit(f"--background must be none or gradient-1 … gradient-{n_bg}")
    scale = round(a.scale, 6)
    html = (TEMPLATE.read_text(encoding="utf-8")
            .replace("<!--SWATCHES-->", "\n  ".join(swatches))
            .replace("{BG_JSON}", json.dumps(bgs))
            .replace("{INITIAL_BG}", a.background)
            .replace("{SCALE}", str(scale))
            .replace("{NAME}", name)
            .replace("{PNG_B64}", base64.b64encode(data).decode()))
    out = pathlib.Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"Wrote {a.out} (render {w}x{h} @{scale:g}x; exports 1600px wide at 1x / 3200px at 2x; "
          f"background picker opens on {a.background})")


if __name__ == "__main__":
    main()
