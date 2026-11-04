---
name: tom-pmm-branded-slides-pptx
description: Create branded, editorial-quality slide decks for Example Feedback (a fictional customer feedback platform), delivered as PPTX and PDF. Use this skill any time someone asks to create a presentation, deck, slides, pitch, or to turn an outline or document into slides for the company, even if they do not say "branded". Triggers include "make a deck", "create slides", "build a presentation", "put together a pitch", "I need slides for X", "turn this into a deck". Always use this skill for any company presentation, and always render and visually check the slides and deliver a PDF as well as a PPTX. Do not hand-build company slides without it.
---

# Branded Slides (PPTX + PDF)

Produces decks that look designed, not templated: real Inter type, a deep brand accent color, the brand mark used as a graphic device, dark/light rhythm, editorial headlines, and full-bleed output that renders identically on any machine.

The examples use Example Feedback, a fictional customer feedback platform, with a placeholder palette and a placeholder brand mark. Replace them with your own (see "Make it yours" in the README).

The engine renders HTML/CSS slides to one image per slide, then assembles a PPTX plus a viewable PDF. This is why the quality ceiling is high. The trade-off is that text is not editable in PowerPoint; copy edits are made in the slide definition and re-rendered. See `references/workflow.md`.

## Setup

Install once in the environment:
```
pip install playwright python-pptx Pillow && playwright install chromium
```
Inter is bundled in `assets/fonts`, so type renders correctly without any system font.

## How to build a deck

1. Read `references/design-system.md` (tokens, type, motif, archetype catalog, copy rules) and, if you have added any, open a few images in `assets/reference` to anchor on the target look.
2. Plan the slide order. Aim for dark/light rhythm and 2 to 3 "moment" slides (a statement hook, a signature diagram or pull-quote, a bookended cover and close).
3. Compose slides by importing the archetypes from `scripts/slide_kit.py`. Copy the structure in `scripts/example_deck.py`.
4. Render, then **look at every slide** (montage the PNGs) and fix overflow or crowding before exporting.
5. Export a PPTX and a PDF to `outputs/` (or wherever your environment delivers files), then present both. The PDF is mandatory because image-based PPTX often will not preview.

Minimal shape:
```python
import sys; sys.path.insert(0, "scripts")
from slide_kit import *
set_footer("Example Feedback")
slides = [
    cover("Example Feedback", "Turn feedback into<br><hl>product direction</hl>", "A short overview", "Jordan Lee"),
    statement("The premise", "Most feedback never becomes a <hlt>decision</hlt>.", 2),
    divider("01", "How it works.", 3),
    cards("Use cases", "Turn scores into <hl>action</hl>.", [
        ("01", "Rescue detractors", "A low score triggers a save play.", True),
        ("02", "Grow promoters", "Happy customers flow into referral asks.", False),
        ("03", "Act post-purchase", "A dip routes to support, a high score to upsell.", False)], 4),
    close("Feedback in.<br><hlt>Decisions out.</hlt>", "example.com"),
]
render(slides, "png")
export_pptx("png", "outputs/Deck.pptx")
export_pdf("png",  "outputs/Deck.pdf")
```

Archetypes available: `cover`, `statement`, `divider`, `agenda`, `split`, `bullets`, `cards`, `close`. For a flow diagram or anything bespoke, compose custom HTML with the shared CSS classes plus `mark()`, `doc()`, `foot()`. `example_deck.py` shows a custom `flow_three` slide as a pattern.

Inline tags inside any `*_html` argument: `<hl>word</hl>` accent highlight, `<hlt>word</hlt>` teal highlight, `<b>word</b>` bold lead-in.

## The rules that matter most

Design (full detail in `references/design-system.md`):
- Lead with the deep accent `#2f6feb`, not a pale tint. Teal (`#5ccfc0`) is a deliberate accent, not a base color.
- Inline-highlight headlines: one highlighted word, not an all-accent title on every slide.
- Brand mark as a large graphic device plus a teal spot accent. Gradients only on cover and close.
- Dark/light rhythm, never all-white.

Copy:
- No em or en dashes anywhere. Colons or periods. US English. Curly quotes.
- Use the current product naming from your messaging doc. In the examples, Example Feedback is a customer feedback platform with two products, Surveys and Feedback Lab. Never use retired product or feature names (list yours in `references/design-system.md`).
- Avoid: focused, excited to announce, agentic, seamless, best-in-class, powerful.

Workflow (full detail in `references/workflow.md`):
- Render and visually review every slide before delivering.
- Type must be real Inter (bundled), never a fallback.
- Always deliver both a PPTX and a PDF.

## Files

- `scripts/slide_kit.py` engine: tokens, `mark()`, archetypes, `render()`, `export_pptx()`, `export_pdf()`.
- `scripts/example_deck.py` worked example and smoke test (`python3 example_deck.py`).
- `references/design-system.md` design tokens, archetype catalog, copy rules.
- `references/workflow.md` production discipline, dependencies, pipelines, definition of done.
- `assets/brand` placeholder logos and brand mark (`icon-black.svg` drives `mark()`; if it is missing, a built-in placeholder shape is used). `assets/fonts` bundled Inter with its license (`OFL.txt`). `assets/reference` target-look images: not included, add your own (see `references/design-system.md`).
