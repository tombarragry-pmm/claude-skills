# -*- coding: utf-8 -*-
"""
slide_kit.py  -  Example Feedback branded slides engine.

Build decks by composing archetype functions into a list of slide HTML strings,
then render to crisp PNGs and export a PPTX + a viewable PDF.

    from slide_kit import *
    slides = [
        cover("Example Feedback x Contoso", "The feedback layer<br>for your <hl>journeys</hl>", "A technical session", "Jordan Lee"),
        statement("The premise", "Your journeys are only as smart as the <hlt>feedback</hlt> behind them.", 2),
        divider("01", "How it works.", 3),
        ...
        close("Feedback in.<br><hlt>Journeys out.</hlt>", "example.com"),
    ]
    render(slides, "png")
    export_pptx("png", "outputs/Deck.pptx")
    export_pdf("png",  "outputs/Deck.pdf")

Inline tags you can use inside any *_html argument:
    <hl>word</hl>   -> brand accent highlight
    <hlt>word</hlt> -> teal highlight
    <b>word</b>     -> ink bold lead-in
Curly quotes: write &#8220; &#8221; &#8216; &#8217;  (never straight quotes in copy).
Never use em or en dashes anywhere. Use colons or periods.

All colors below are a placeholder palette. Replace them with your brand.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.abspath(os.path.join(HERE, "..", "assets", "fonts"))
BRAND_DIR = os.path.abspath(os.path.join(HERE, "..", "assets", "brand"))

# The brand mark is used as a large graphic device (see mark()). It is read from
# assets/brand/icon-black.svg (viewBox 0 0 147 147, single fill #1A1A2E). If the
# file is missing, a simple built-in placeholder shape is used instead.
_FALLBACK_MARK = ("<path d='M36 0H111C130.9 0 147 16.1 147 36V111C147 130.9 130.9 147 111 147H36"
                  "C16.1 147 0 130.9 0 111V36C0 16.1 16.1 0 36 0ZM73.5 38C53.9 38 38 53.9 38 73.5"
                  "C38 93.1 53.9 109 73.5 109C93.1 109 109 93.1 109 73.5C109 53.9 93.1 38 73.5 38Z' "
                  "fill='#1A1A2E'/>")

def _load_mark():
    path = os.path.join(BRAND_DIR, "icon-black.svg")
    try:
        with open(path, encoding="utf-8") as f:
            svg = f.read()
        return svg.split(">", 1)[1].rsplit("</svg>", 1)[0]
    except (OSError, IndexError):
        return _FALLBACK_MARK

ICON_INNER = _load_mark()

# ---- brand tokens (placeholder palette, replace with your brand) -----------
INK, INK2, MUT, LINE = "#1a1a2e", "#44475a", "#9b9da8", "#e2e3e9"
ACC, ACC2, ACCL = "#2f6feb", "#4a80ee", "#7fa6f2"
ACCLL, ACCLL2, ACCD, ACCDD = "#e8f0fd", "#f3f7fe", "#163d8f", "#0f2a63"
TEAL, TEALD, TEALL = "#5ccfc0", "#2f9e90", "#c9efea"

# Hero gradient stops (cover and close only).
GRAD_HI, GRAD_MID, GRAD_LO = "#5b8ef5", "#2a62d9", "#12357f"

# Footer label shown bottom-left on content slides. Set per deck with set_footer().
FOOTER = "Example Feedback"
def set_footer(label):
    global FOOTER
    FOOTER = label

_FONTS = "".join(
    f"@font-face{{font-family:Inter;font-weight:{w};font-style:normal;"
    f"src:url('file://{FONT_DIR}/Inter-{w}.ttf')}}"
    for w in [400, 500, 600, 700, 800, 900]
) + (
    f"@font-face{{font-family:Inter;font-weight:400;font-style:italic;src:url('file://{FONT_DIR}/Inter-i400.ttf')}}"
    f"@font-face{{font-family:Inter;font-weight:700;font-style:italic;src:url('file://{FONT_DIR}/Inter-i700.ttf')}}"
)

CSS = _FONTS + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--ink:{INK};--ink2:{INK2};--mut:{MUT};--line:{LINE};
--acc:{ACC};--acc2:{ACC2};--accL:{ACCL};--accLL:{ACCLL};--accLL2:{ACCLL2};--accD:{ACCD};--accDD:{ACCDD};
--teal:{TEAL};--tealD:{TEALD};--tealL:{TEALL}}}
html,body{{width:1280px;height:720px}}
.stage{{position:relative;width:1280px;height:720px;overflow:hidden;font-family:Inter;background:#fff;color:var(--ink)}}
.pad{{position:absolute;inset:0;padding:70px 76px}}
.eyebrow{{font-size:13px;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:var(--acc)}}
.dark .eyebrow{{color:var(--teal)}}
.foot{{position:absolute;left:76px;bottom:34px;font-size:10.5px;font-weight:600;letter-spacing:1.6px;text-transform:uppercase;color:var(--mut);z-index:5}}
.pageno{{position:absolute;right:76px;bottom:32px;font-size:11px;font-weight:600;color:var(--mut);z-index:5}}
.dark .foot,.dark .pageno{{color:rgba(255,255,255,.55)}}
h1.t{{font-size:46px;font-weight:800;line-height:1.04;letter-spacing:-.6px;color:var(--ink)}}
hl{{color:var(--acc)}}
hlt{{color:var(--tealD)}}
.dark hl{{color:#b3cbf8}} .dark hlt{{color:{TEAL}}}
b{{font-weight:700;color:var(--ink)}}
.dark b{{color:#fff}}
.dot{{display:inline-block;width:9px;height:9px;border-radius:2px;background:var(--teal);transform:rotate(45deg);margin-right:16px;flex:0 0 auto;margin-top:9px}}
.li{{display:flex;align-items:flex-start;font-size:20px;font-weight:400;color:var(--ink2);line-height:1.38;margin-bottom:19px}}
.card{{position:relative;border-radius:18px;background:#fff;border:1.5px solid var(--line)}}
"""

def _hl(s):  # allow <hl>/<hlt> shorthand as-is (they are real tags via CSS)
    return s

def doc(stage):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{stage}</body></html>"

def mark(color, size, style="", op=1.0):
    """The brand mark, recolored and positioned absolutely, used as a graphic device."""
    inner = ICON_INNER.replace("#1A1A2E", color).replace("#1a1a2e", color)
    return (f"<svg viewBox='0 0 147 147' fill='none' "
            f"style='position:absolute;width:{size};height:{size};opacity:{op};{style}'>{inner}</svg>")

def foot(n, dark=False):
    return f"<div class='foot'>{FOOTER}</div><div class='pageno'>{n:02d}</div>"

# ---- archetypes -------------------------------------------------------------

def cover(eyebrow, title_html, subtitle="", presenter="", org="Example Feedback"):
    return doc(f"""
<div class='stage dark' style="background:radial-gradient(130% 130% at 82% 18%, {GRAD_HI} 0%, {GRAD_MID} 42%, {GRAD_LO} 100%)">
  {mark('#ffffff','760px','right:-230px;top:-150px;',0.10)}
  {mark(TEAL,'150px','right:250px;top:250px;',0.9)}
  {mark('#ffffff','300px','right:-40px;bottom:-90px;',0.07)}
  <div class='pad'>
    <div class='eyebrow' style='color:{TEALL}'>{eyebrow}</div>
    <div style='position:absolute;left:76px;top:210px;width:780px'>
      <div style='font-size:70px;font-weight:800;line-height:1.02;letter-spacing:-1.5px;color:#fff'>{title_html}</div>
      <div style='margin-top:26px;font-size:20px;font-weight:400;color:#dbe6fc'>{subtitle}</div>
    </div>
    <div style='position:absolute;left:76px;bottom:62px'>
      <div style='font-size:20px;font-weight:700;color:#fff'>{presenter}</div>
      <div style='font-size:15px;font-weight:400;color:#bcd0f8;margin-top:2px'>{org}</div>
    </div>
  </div>
</div>""")

def statement(eyebrow, body_html, page, theme="ink"):
    bg = INK if theme == "ink" else ACCDD
    pc = ACC if theme == "ink" else ACCL
    return doc(f"""
<div class='stage dark' style='background:{bg}'>
  {mark(pc,'620px','right:-170px;bottom:-210px;',0.5)}
  {mark(TEAL,'120px','right:150px;top:110px;',0.85)}
  <div class='pad'>
    <div class='eyebrow'>{eyebrow}</div>
    <div style='position:absolute;left:76px;top:250px;width:820px;font-size:60px;font-weight:800;line-height:1.08;letter-spacing:-1px;color:#fff'>{body_html}</div>
  </div>
  {foot(page)}
</div>""")

def divider(num, title_html, page, theme="deep"):
    if theme == "deep":
        style, pc, op, numc = f"background:{ACCDD};color:#fff", ACCL, 0.28, TEALL
        spot = mark(TEAL, "120px", "left:78px;top:150px;", 0.9)
    else:
        style, pc, op, numc = f"background:{TEALD};color:#fff", "#ffffff", 0.16, "#ebfaf8"
        spot = mark("#ffffff", "120px", "left:78px;top:150px;", 0.5)
    return doc(f"""
<div class='stage dark' style='{style}'>
  {mark(pc,'720px','right:-190px;bottom:-230px;',op)}
  {spot}
  <div class='pad'>
    <div style='position:absolute;left:76px;top:300px;font-size:150px;font-weight:800;color:{numc};line-height:.8;letter-spacing:-4px;opacity:.9'>{num}</div>
    <div style='position:absolute;left:280px;top:322px;font-size:64px;font-weight:800;line-height:1.05;letter-spacing:-1px'>{title_html}</div>
  </div>
  {foot(page)}
</div>""")

def agenda(title, items, page):
    rows = ""
    for i, (n, t) in enumerate(items):
        top = 150 + i * 98
        line = "" if i == 0 else "border-top:1.5px solid var(--line);"
        rows += (f"<div style='position:absolute;left:470px;right:76px;top:{top}px;height:98px;display:flex;align-items:center;{line}'>"
                 f"<div style='font-size:40px;font-weight:800;color:var(--accL);width:92px;letter-spacing:-1px'>{n}</div>"
                 f"<div style='font-size:24px;font-weight:600;color:var(--ink)'>{t}</div></div>")
    return doc(f"""
<div class='stage'>
  <div style='position:absolute;left:0;top:0;width:392px;height:720px;background:var(--acc);color:#fff;overflow:hidden'>
    {mark('#ffffff','300px','left:-70px;bottom:-90px;',0.12)}
    <div style='padding:70px 46px'>
      <div class='eyebrow' style='color:#b7cdf7'>Agenda</div>
      <div style='margin-top:210px;font-size:48px;font-weight:800;line-height:1.05;letter-spacing:-.5px'>{title}</div>
    </div>
  </div>
  {rows}
  <div class='pageno'>{page:02d}</div>
</div>""")

def split(panel_eyebrow, panel_title_html, panel_sub, rows, page, panel="deep"):
    bg = ACCDD if panel == "deep" else ACC
    body = ""
    for k, v in rows:
        body += (f"<div style='margin-bottom:34px'>"
                 f"<div style='font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--tealD)'>{k}</div>"
                 f"<div style='margin-top:8px;font-size:23px;font-weight:700;color:var(--ink)'>{v}</div></div>")
    return doc(f"""
<div class='stage'>
  <div style='position:absolute;left:0;top:0;width:520px;height:720px;background:{bg};color:#fff;overflow:hidden'>
    {mark(ACCL,'360px','left:-110px;top:-80px;',0.30)}
    {mark(TEAL,'120px','left:300px;bottom:150px;',0.9)}
    <div style='padding:78px 54px'>
      <div class='eyebrow' style='color:{TEALL}'>{panel_eyebrow}</div>
      <div style='margin-top:150px;font-size:40px;font-weight:800;line-height:1.12;letter-spacing:-.5px'>{panel_title_html}</div>
      <div style='margin-top:22px;font-size:17px;color:#b7cdf7;font-weight:500'>{panel_sub}</div>
    </div>
  </div>
  <div style='position:absolute;left:520px;right:0;top:0;height:720px;padding:88px 60px'>{body}</div>
  {foot(page)}
</div>""")

def bullets(eyebrow, title_html, items, page, aside_html="", title_width=620):
    lis = "".join(f"<div class='li'><span class='dot'></span><div>{t}</div></div>" for t in items)
    left_w = 560 if aside_html else 1000
    return doc(f"""
<div class='stage'>
  <div class='pad'>
    <div class='eyebrow'>{eyebrow}</div>
    <h1 class='t' style='margin-top:16px;width:{title_width}px'>{title_html}</h1>
    <div style='position:absolute;left:76px;top:270px;width:{left_w}px'>{lis}</div>
  </div>
  {aside_html}
  {foot(page)}
</div>""")

def cards(eyebrow, title_html, card_list, page, note_html=""):
    n = len(card_list)
    gap = 28
    total_w = 1280 - 76 * 2
    cw = int((total_w - gap * (n - 1)) / n)
    blocks = ""
    for i, c in enumerate(card_list):
        kbd, title, body, hot = c
        left = 76 + i * (cw + gap)
        if hot:
            box = f"background:{ACC};color:#fff;overflow:hidden"; kc = "#b7cdf7"; tc = "#fff"; bc = "#dbe6fc"
            extra = mark("#ffffff", "160px", "right:-50px;bottom:-60px;", 0.12)
        else:
            box = f"background:#fff;border:1.5px solid {LINE}"; kc = ACCL; tc = INK; bc = INK2; extra = ""
        blocks += (f"<div style='position:absolute;left:{left}px;top:236px;width:{cw}px;height:280px;border-radius:18px;padding:30px;{box}'>"
                   f"{extra}"
                   f"<div style='font-size:40px;font-weight:800;color:{kc};letter-spacing:-1px;line-height:1'>{kbd}</div>"
                   f"<div style='margin-top:22px;font-size:24px;font-weight:800;color:{tc}'>{title}</div>"
                   f"<div style='margin-top:10px;font-size:17px;color:{bc};line-height:1.45'>{body}</div></div>")
    note = ""
    if note_html:
        note = (f"<div style='position:absolute;left:76px;right:76px;top:548px;background:{TEALL};border-radius:14px;"
                f"padding:18px 24px;display:flex;align-items:center;gap:14px'>{mark(TEALD,'20px','position:relative;')}"
                f"<div style='font-size:17px;color:{INK};font-weight:500'>{note_html}</div></div>")
    return doc(f"""
<div class='stage'>
  <div class='pad'><div class='eyebrow'>{eyebrow}</div><h1 class='t' style='margin-top:16px'>{title_html}</h1></div>
  {blocks}{note}
  {foot(page)}
</div>""")

def close(title_html, url):
    return doc(f"""
<div class='stage dark' style="background:radial-gradient(130% 130% at 18% 85%, {GRAD_HI} 0%, {GRAD_MID} 44%, {GRAD_LO} 100%)">
  {mark('#ffffff','700px','left:-210px;bottom:-230px;',0.10)}
  {mark(TEAL,'140px','right:230px;top:150px;',0.9)}
  {mark('#ffffff','280px','right:-60px;top:-90px;',0.07)}
  <div class='pad'>
    <div style='position:absolute;left:76px;top:250px;font-size:88px;font-weight:800;line-height:1.0;letter-spacing:-2px;color:#fff'>{title_html}</div>
    <div style='position:absolute;left:78px;bottom:90px;font-size:19px;font-weight:500;color:#dbe6fc'>{url}</div>
  </div>
</div>""")

# ---- render + export --------------------------------------------------------

def render(slides, out_dir, scale=2):
    """Screenshot each slide HTML to out_dir/slide_NN.png at 2x. Requires playwright + chromium."""
    from playwright.sync_api import sync_playwright
    os.makedirs(out_dir, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1280, "height": 720}, device_scale_factor=scale)
        for i, html in enumerate(slides, 1):
            pg.set_content(html)
            pg.wait_for_timeout(250)
            pg.screenshot(path=os.path.join(out_dir, f"slide_{i:02d}.png"),
                          clip={"x": 0, "y": 0, "width": 1280, "height": 720})
        b.close()
    return sorted(f for f in os.listdir(out_dir) if f.endswith(".png"))

def _pngs(png_dir):
    import glob
    return sorted(glob.glob(os.path.join(png_dir, "slide_*.png")))

def export_pptx(png_dir, out_path):
    """Assemble full-bleed image-per-slide PPTX. Requires python-pptx."""
    from pptx import Presentation
    from pptx.util import Inches
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]
    for f in _pngs(png_dir):
        s = prs.slides.add_slide(blank)
        s.shapes.add_picture(f, 0, 0, width=prs.slide_width, height=prs.slide_height)
    prs.save(out_path)
    return out_path

def export_pdf(png_dir, out_path):
    """Assemble a viewable PDF from the slide PNGs. Requires Pillow. Always ship this alongside the PPTX."""
    from PIL import Image
    imgs = [Image.open(f).convert("RGB") for f in _pngs(png_dir)]
    imgs[0].save(out_path, save_all=True, append_images=imgs[1:], resolution=144.0)
    return out_path
