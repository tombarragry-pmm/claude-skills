#!/usr/bin/env python3
"""Place a rendered screen PNG on a background (a gradient from assets/backgrounds, or a flat color).

Usage:
  add_background.py in.png out.png --background gradient-3 [--padding 64] [--radius 16]
                    [--aspect 1.91:1] [--no-shadow] [--scale 2]

--background  gradient-N (any file in assets/backgrounds), a hex color like "#F8F8FA", or "none"
              to copy the input as is.
--padding     space around the screen in 1x px (default 64; it scales with --scale).
--radius      corner radius of the screen in 1x px (default 16; 0 = square corners).
--aspect      optional canvas ratio (e.g. 16:9, 1.91:1 for OG/LinkedIn, 1:1, 4:5). The screen is
              fitted inside with at least --padding on every side and centered.
--scale       pixel ratio of the input render; read from the PNG written by render_screen.py.
The gradients are stored smoothed at about 900 px; they are scaled to cover the canvas and fresh fine grain is added
so they don't look soft at 2x/3x.
"""
import argparse, pathlib, random
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
BG_DIR = HERE.parent / "assets" / "backgrounds"


def cover(img, w, h):
    s = max(w / img.width, h / img.height)
    img = img.resize((round(img.width * s), round(img.height * s)), Image.LANCZOS)
    x, y = (img.width - w) // 2, (img.height - h) // 2
    return img.crop((x, y, x + w, y + h))


def grain(img, sigma=3.5):
    a = np.asarray(img, dtype=np.float32)
    rng = np.random.default_rng(7)
    n = rng.normal(0, sigma, a.shape[:2])[..., None]
    return Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))


def parse_aspect(s):
    a, b = s.split(":")
    return float(a) / float(b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("png"); ap.add_argument("out")
    ap.add_argument("--background", default="gradient-1")
    ap.add_argument("--padding", type=float, default=64)
    ap.add_argument("--radius", type=float, default=16)
    ap.add_argument("--aspect")
    ap.add_argument("--no-shadow", action="store_true")
    ap.add_argument("--scale", type=float, help="render pixel ratio; read from the PNG if omitted")
    a = ap.parse_args()

    raw = Image.open(a.png)
    if a.scale is None:
        a.scale = float(raw.info.get("mockup-scale", 2))
    src = raw.convert("RGBA")
    if a.background == "none":
        src.save(a.out); print(f"Copied {a.png} -> {a.out} (no background)"); return

    pad, rad = round(a.padding * a.scale), round(a.radius * a.scale)
    W, H = src.width + 2 * pad, src.height + 2 * pad
    if a.aspect:
        r = parse_aspect(a.aspect)
        if W / H < r: W = round(H * r)
        else: H = round(W / r)

    if a.background.startswith("#"):
        canvas = Image.new("RGB", (W, H), a.background)
    else:
        f = BG_DIR / f"{a.background}.jpg"
        if not f.exists():
            raise SystemExit(f"Unknown background '{a.background}'. Use gradient-N from assets/backgrounds, a #hex color or none.")
        canvas = grain(cover(Image.open(f).convert("RGB"), W, H))
    canvas = canvas.convert("RGBA")

    x, y = (W - src.width) // 2, (H - src.height) // 2
    mask = Image.new("L", src.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, src.width - 1, src.height - 1), radius=rad, fill=255)

    if not a.no_shadow:
        sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        m = Image.new("L", (W, H), 0)
        off = round(8 * a.scale)
        m.paste(mask, (x, y + off))
        m = m.filter(ImageFilter.GaussianBlur(round(24 * a.scale)))
        sh.putalpha(m.point(lambda v: int(v * 0.14)))
        canvas = Image.alpha_composite(canvas, sh)

    canvas.paste(src, (x, y), Image.composite(src.getchannel("A"), Image.new("L", src.size, 0), mask))
    from PIL.PngImagePlugin import PngInfo
    info = PngInfo(); info.add_text("mockup-scale", f"{a.scale:.6f}")
    canvas.convert("RGB").save(a.out, optimize=True, pnginfo=info)
    print(f"Wrote {a.out} ({W}x{H}, background {a.background}, padding {a.padding:g}px, radius {a.radius:g}px)")


if __name__ == "__main__":
    main()
