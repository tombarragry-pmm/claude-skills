# charts-creator

Builds polished, on-brand charts as a single HTML preview with two download buttons: PNG (1920px wide) and SVG (720px wide). A built-in checker catches layout, color, contrast and typography mistakes before delivery.

Originally built: November 2026

## What it does

1. Gathers the data, title and preset, and picks a chart type if you didn't.
2. Plans the layout numerically, so every element has an exact position.
3. Writes the chart as a clean SVG.
4. Runs `scripts/check_chart.py` to lint the SVG and render a PNG for a visual review.
5. Wraps the chart into an HTML preview with download buttons using `scripts/build_preview.py`.

## Files

- `SKILL.md`: the instructions Claude follows.
- `references/example-feedback.md`: the default house-style preset (palette, type, header, footer).
- `references/editorial.md`: an editorial research-report preset.
- `references/recipes.md`: layout recipes for each chart type.
- `scripts/check_chart.py`: the linter and PNG renderer.
- `scripts/build_preview.py`: builds the HTML preview.
- `assets/`: the preview template, a placeholder logo, and the embedded Inter font with its license (`OFL.txt`).

## Requirements

- Python 3 with `lxml` and `Pillow`. `cairosvg` is installed on first run if missing, for the PNG check render.

## Make it yours

All colors and the logo are placeholders for a fictional brand. To use your own brand:

1. Replace the hex values in `references/example-feedback.md` and `references/editorial.md`.
2. Update the matching color lists in `PALETTES` in `scripts/check_chart.py`.
3. Replace the shapes in `assets/logo-snippet.svg` with your logo paths.
4. Optionally, list your product UI grays in `BRAND_TOKEN_GRAYS` so the checker flags them in charts.
