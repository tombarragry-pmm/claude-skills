# tom-pmm-panel-ui

Mocks up screens of your own app as downloadable PNG images that match the real product, using your tokens and components instead of generic UI. Each mockup is linted for off-token colors, rendered offline with Playwright, and delivered as an HTML preview with a background picker, annotation tools and Download PNG (1x and 2x) buttons.

Originally built: November 2026

## What it does

1. Starts every screen from a base template with the app shell and every token as a CSS variable.
2. Lints the HTML: any color not in `references/tokens.md`, raw Tailwind greys or text under 10px is an error.
3. Renders the screen to a PNG that is always 1600px wide at 1x and 3200px at 2x.
4. Optionally places it on a gradient at a fixed ratio (for example 1.91:1 for link previews).
5. Wraps it in a preview where you can pick a background, draw arrows and boxes, and download.

## Files

- `SKILL.md`: the instructions Claude follows.
- `references/tokens.md`: placeholder tokens. The render script reads this file.
- `assets/app-mockup-base.html`: the starting template.
- `assets/preview-template.html`: the preview page.
- `assets/backgrounds/`: four placeholder gradients.
- `assets/illustrations/`: empty. Add your own artwork.
- `scripts/`: `render_screen.py`, `add_background.py`, `build_preview.py`.
- `assets/vendor/`: Inter (SIL Open Font License, see `fonts/OFL-LICENSE.txt`) and lucide (ISC License, see `LUCIDE-LICENSE.txt`).

## Requirements

- Python 3 with Pillow, numpy and Playwright (`pip install pillow numpy playwright && playwright install chromium`).

## Make it yours

The examples use Example Feedback, a fictional customer feedback platform, with a placeholder palette. Replace the tokens, the shell and navigation in the base template, the gradients and the illustrations with your own product's.
