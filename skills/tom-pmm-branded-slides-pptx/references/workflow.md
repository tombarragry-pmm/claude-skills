# Branded Slides: Workflow

How to actually get pixels that match the design. Most quality and reliability problems live here, not in the design rules.

## Non-negotiables

1. **Render every slide and look at it before delivering.** Build the PNGs, view them (a montage is fine), and check for overflow, crowding, clipping, and fallback fonts. Never hand over a deck you have not seen.
2. **Type must be real Inter.** Inter is bundled in `assets/fonts` and loaded via `@font-face` at render time, so it renders correctly regardless of what is installed on any machine. Do not swap the font or rely on a system font.
3. **Always ship a PDF alongside the PPTX.** This deck format is image-based and image-heavy PPTX files often will not preview in chat or some clients. The PDF guarantees the work can be seen. Export both, every time.

## Dependencies

The engine needs:
- `playwright` plus its Chromium browser: `pip install playwright && playwright install chromium`
- `python-pptx`: `pip install python-pptx`
- `Pillow`: `pip install Pillow`

Fonts are bundled, so `fonttools` is only needed if you ever regenerate weights.

## How it runs

```python
from slide_kit import *          # from inside scripts/, or add scripts/ to sys.path
set_footer("Example Feedback")   # or "Example Feedback x Contoso" etc.
slides = [ cover(...), statement(...), ... , close(...) ]
render(slides, "png")                          # HTML -> Chromium screenshots at 2x (2560x1440)
export_pptx("png", "outputs/Deck.pptx")        # full-bleed image per slide
export_pdf("png",  "outputs/Deck.pdf")         # viewable companion
```

`render` drives a headless browser, so every slide is exactly what the CSS describes. Output is 1280 x 720 at 2x for crispness.

## Two pipelines, and the trade-off

This skill uses the **design pipeline**: HTML/CSS rendered to one image per slide, assembled into the PPTX. It gives full creative control and pixel-identical output on any machine. The cost is that **text is not editable in PowerPoint**; copy changes mean editing the slide definition and re-rendering (fast, a minute or two).

The alternative is an **editable pipeline** (pptxgenjs or python-pptx with live text boxes). Text stays editable, but the design ceiling is much lower and fonts must be embedded manually or they fall back. Reserve it for internal working decks where live editing matters more than polish.

Recommendation: design final, client-facing decks with this pipeline. Handle copy edits by regeneration. If someone needs to edit text themselves, give them the PDF for review and make the edits here.

## Definition of done

- [ ] Every slide rendered and visually reviewed
- [ ] Type is real Inter, no fallback
- [ ] Dark/light rhythm present, not all white
- [ ] At least one inline-highlight headline and 2 to 3 "moment" slides
- [ ] Brand mark used as a graphic device, plus a teal spot accent
- [ ] Deep accent `#2f6feb` on impact surfaces, teal used deliberately
- [ ] No em or en dashes, US English, curly quotes, correct product naming
- [ ] Delivered as both PPTX and a viewable PDF, to the outputs folder
