# tom-pmm-branded-slides-pptx

Builds editorial-quality branded decks by rendering HTML/CSS slides in a headless browser, then exporting them as a full-bleed PPTX plus a viewable PDF. Every slide is rendered and visually checked before delivery.

Originally built: November 2026

## What it does

1. Reads the design system (tokens, type, brand mark motif, archetype catalog, copy rules) and any reference images.
2. Plans the slide order with dark/light rhythm and 2 to 3 "moment" slides.
3. Composes slides from ready-made archetypes in `scripts/slide_kit.py` (cover, statement, divider, agenda, split, bullets, cards, close), or custom HTML for bespoke layouts.
4. Renders each slide to a 2x PNG with Playwright and Chromium, then reviews every slide for overflow, crowding and fallback fonts.
5. Exports a PPTX (one image per slide) and a PDF, and delivers both.

## Files

- `SKILL.md`: the instructions Claude follows.
- `references/design-system.md`: color tokens, type scale, brand mark motif, archetype catalog, copy rules.
- `references/workflow.md`: production rules, dependencies, the two pipelines and the definition of done.
- `scripts/slide_kit.py`: the engine (tokens, archetypes, `render()`, `export_pptx()`, `export_pdf()`).
- `scripts/example_deck.py`: a worked example deck with fictional content, also a smoke test.
- `assets/brand/`: placeholder logos and brand mark. `icon-black.svg` is recolored and used as the large graphic motif.
- `assets/fonts/`: bundled Inter weights and their license (`OFL.txt`).
- `assets/reference/`: not included. Add your own reference slide screenshots here (file names are listed in `references/design-system.md`).

## Requirements

- Python 3 with `playwright` (plus `playwright install chromium`), `python-pptx` and `Pillow`.

## Make it yours

The examples use Example Feedback, a fictional customer feedback platform, with a placeholder blue and teal palette.

1. Replace the hex values in the token block at the top of `scripts/slide_kit.py` and in `references/design-system.md`.
2. Replace `assets/brand/icon-black.svg` with your brand mark (keep `viewBox="0 0 147 147"` and a single `#1A1A2E` fill so it can be recolored), and swap the other logo files.
3. Update the product naming and the retired-names list in the copy rules.
4. Add screenshots of your best existing slides to `assets/reference/`.
5. Change the default footer and organization label ("Example Feedback") in `slide_kit.py`.
