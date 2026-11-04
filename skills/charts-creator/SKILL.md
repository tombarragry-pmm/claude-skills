---
name: "charts-creator"
description: "Use for ALL chart and infographic creation. Use it automatically, without asking, any time anyone requests a chart, graph, infographic, data visualization, or any visual representation of data. Covers bar, line, area, pie, donut, horizontal bar, multi-line, scatter, stat cards, KPI visuals, NPS breakdowns, comparison and trend visuals, range/dot plots, waffles, and infographics of any kind. Trigger on any phrasing whose deliverable is a data visual. Never produce charts by any other method. Supports two brand presets: Example Feedback (house style) and Editorial research. Output is a self-contained HTML preview with two download buttons: PNG (1920px wide, primary) and SVG (720px wide, secondary). Font is always Inter. Exception: charts inside product-screen mockups follow your product-mockup skill instead, if you have one."
---

# Charts Creator (house style)

> **Scope exception.** A chart that sits inside a mockup of your product's own UI (a dashboard widget, a report chart, a results screen) should be drawn with a separate product-mockup skill that records how the live product renders charts, if you have one. Don't apply this skill's palette, type sizes or chrome there.

Produce polished, branded charts as one HTML preview with **Download PNG** (1920px) and
**Download SVG** (720px) buttons. **Font is always `Inter`.** The download buttons are
required in every output medium, including a Claude Design canvas (see "Delivering on a
Design canvas" below).

Two presets: **Example Feedback** (default house style for a fictional customer feedback
platform) and **Editorial research** (a research-report style). Use Example Feedback unless
the request is clearly for an editorial research report; ask only if it's truly unclear.
Swap the preset values for your own brand before real use.

## Files in this skill

| File | Read when |
|------|-----------|
| `references/example-feedback.md` | Every Example Feedback chart: palette, type scale, header, footer, element conventions |
| `references/editorial.md` | Every Editorial research chart |
| `references/recipes.md` | Always. Read the section for the chart type you're drawing |
| `assets/logo-snippet.svg` | Example Feedback footer. Paste verbatim, replace `{LOGO_Y}` with `H-40`. It is a placeholder: swap in your own logo path |
| `assets/preview-template.html` | Reference for the download buttons' look and the PNG/SVG export logic |
| `assets/inter-embed.css` | Inter (400 to 900, Latin and Latin Extended subset) as embedded `@font-face` rules; used by the preview and the PNG export so they work offline. Licensed under the SIL Open Font License (see `assets/OFL.txt`) |
| `scripts/check_chart.py` | After writing the SVG: lint + render a PNG to look at |
| `scripts/build_preview.py` | Last step: wraps the SVG into the HTML preview |

---

## Workflow

### 1. Gather inputs
You need: chart type, exact data (values, labels, units), title, and preset. Optional, and
only when the user actually provides them: description/takeaway, label pill text (a real
report or series name, e.g. "FEEDBACK TRENDS · 2026"), sample size, source line, annotations or
reference lines. If the data is there, proceed. Don't interrogate. Pick the chart type
yourself if not given (see "Choosing a chart type" in `recipes.md`).

### 2. Read the references
Preset file + the recipe section. Don't draw from memory; the values are exact.

### 3. Plan the layout numerically, before writing any SVG
Write a short layout sheet (in your head or a scratch file) with every y-position:
header block → chart block → footer. Derive `H` from the stack; never guess a height.
Compute label column widths from the longest label, scales from the data, bar lengths as
`value / scaleMax × width`. Decide where every value label goes and check it can't collide.

### 4. Write the SVG
Save to `charts/{name}.svg`. Authoring rules (the checker depends on them):
- Presentation **attributes** only (`font-size="16" fill="#1A1A2E"`), no CSS classes. The only
  `<style>` is the Inter `@import` in `<defs>`
- `font-family="Inter"` on the root `<svg>`; nothing else anywhere
- Positioning via `x`/`y` and `translate()` only; `scale()` is reserved for the logo
- Integers or 1 decimal; one `<g>` + comment per logical block
- Escape `&` and `<` in text (`Research &amp; Development`)
- Rounded 100%-stacked bars: `<clipPath>` with an rx=6 rect in `<defs>`, segments inside
- Source order = paint order: background rect → grid → reference zones → data → labels → callouts → footer

### 5. Check and look (mandatory)
```bash
python3 scripts/check_chart.py charts/{name}.svg --preset example-feedback
```
It reports ERRORs (canvas, margins, off-palette colors, text under 14px, too many text runs, text overflow, text
collisions, long prose runs, title capitalization and dashes, off-center labels inside bars, the title running into the eyebrow, labels or callouts covering data lines/points)
and WARNINGs, and renders `{name}.check.png`. **Fix every ERROR, then `view` the
PNG** and judge it like a designer: uneven gaps, cramped labels, orphaned words in wrapped
titles, a lopsided composition, labels that read as belonging to the wrong bar. Fix and
re-run until clean (usually 1 to 3 passes). If the script can't run, do the checklist by hand.

### 6. Build and deliver the preview
```bash
python3 scripts/build_preview.py charts/{name}.svg charts/{name}.html
```
Deliver only the HTML file. One or two sentences of summary; never paste SVG code in chat.
When the chart goes on a Claude Design canvas instead, skip this script and follow
"Delivering on a Design canvas" below. The buttons are still required.

---

## Delivering on a Design canvas (Claude Design)

When the chart is built on a Design canvas artboard rather than as the HTML preview, the
artboard must still carry working **Download PNG** (1920px wide) and **Download SVG**
(720px wide) buttons. Never deliver a chart artboard without them.

**Layout**
- Artboard is 720 wide. The chart SVG (checked, unchanged, `id="chart-svg"`) sits at the top
  at 720 × `H`; directly below it a button row: padding 16px 20px, `display: flex; gap: 12px`
- Artboard height = `H + 76` (16 + 44 + 16); `$preview` and the `boards` entry use the same size
- Buttons match `assets/preview-template.html`: real `<button type="button">` elements,
  `flex: 1 1 0`, height 44, radius 8, no border, Inter 14px 600, a 16px stroke download icon
  (inline SVG, `stroke="currentColor"`) + label. PNG: `#2F6FEB` fill, white text (primary).
  SVG: `#1A1A2E` fill, white text (secondary). Labels exactly `Download PNG` / `Download SVG`
- The buttons are not part of the chart: never put them inside the SVG, and the exported
  files contain only the chart
- Mark the artboard `"is_interactive": true` in the canvas index so the buttons work in Play

**Wiring (artboard logic class, classic JS)**
- Bind `onClick="{{ downloadPng }}"` and `onClick="{{ downloadSvg }}"`; return both
  handlers from `renderVals()`
- Keep the full chart SVG text (including the `<defs>` Inter `@import`) as a string constant in
  the logic class, or read the live element with `document.getElementById('chart-svg')` and
  `XMLSerializer`, re-adding the `<defs><style>@import…</style></defs>` block if the inline copy
  dropped it. Either way the downloaded SVG equals the checked SVG
- SVG download: `Blob` (`image/svg+xml;charset=utf-8`) → object URL → temporary `<a download>`
  click → revoke. File name = the chart's kebab-case name + `.svg`
- PNG download: port `embedFonts()` and `downloadPNG()` from `assets/preview-template.html`
  and embed the Inter `@font-face` rules from `assets/inter-embed.css` in the artboard (never
  fetch fonts at click time). Load the font-embedded SVG into an `Image` through a
  `data:image/svg+xml` URL, never a `blob:` URL (sandboxed previews block both the font fetch
  and blob image loads, which makes the export fail silently), draw it onto a
  1920 × round(H × 1920 / 720) canvas over a white fill, `toBlob` → download, and show an
  error with `img.onerror` instead of failing silently
- The temporary `<a>` and `<canvas>` used for downloading are not UI and are allowed; no
  other script-built markup

The "Self-contained: no JS" rule below applies to the chart SVG itself, not to the
artboard's download logic.

---

## Label pill and footer meta: only from real, given information

These rules override anything in the preset or recipe files that describes the label pill
or the footer meta line as optional decoration.

**Label pill (above the title)**
- Add it **only** when the user gives (or the source material clearly states) a real report,
  series or campaign name, e.g. "Feedback Trends 2026" → `FEEDBACK TRENDS · 2026`
- **Never** invent or infer one: no generic placeholders like `BENCHMARK`, `REPORT`,
  `INSIGHTS`, `DATA` or a bare year, and no pill just to fill the header
- No pill → title line 1 baseline at y=66 (per the preset's header formula)

**Footer meta line (right of the logo) and source line**
- Add the meta line **only** for a real sample size or context figures the user provided
  (e.g. `n = 2,400 responses`). Add the source line only for a real source the user provided
- **Never** invent a sample size or source, and never fill the slot with descriptive filler
  such as `Sample data`, `Illustrative`, `4 channels · 12 months` or a restatement of the chart
- Sample or made-up data: leave the meta line out, and say in your reply (not on the chart)
  that the data is sample data
- No meta and no source → the footer is the divider (optional) and the logo only

---

## Shared rules (both presets)

- **Canvas:** 720px wide, `#FFFFFF` background rect covering the canvas. No transparency, no
  off-white, no colored hero panels
- **Margins:** content lives in x=20..700; top margin 40px; bottom margin per preset footer
- **Height:** computed from the layout stack
- **Fonts:** `<defs><style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&amp;display=swap');</style></defs>`. Weights 400 / 600 / 700 / 800 / 900 only
- **Spacing:** ≥4px between any two adjacent elements; ≥8px between stacked header rows;
  label-to-mark gap 8px (value after a bar end, category label before a track)
- **Fill the width:** distribute the chart across x=20..700; no dead zones on the right
- **Grid behind data** in source order
- **No text below 14px**, ever. Weight carries hierarchy: 900 titles and hero numbers,
  800 data values, 700 eyebrows, 600 names, 400 supporting text (see the preset's weight table)
- **Data completeness comes first.** Every relevant value the user gives must appear on the
  chart: all rows (including reference or "not comparable" rows, shown as such), all metric
  columns, secondary figures ("12 of 40", "7.5%", "2.3 / team"), sample size, and source.
  Match prominence to importance: context figures (sample sizes, counts of companies, derived
  spreads) go in the footer meta line, not in stat cards or hero blocks. Only drop data that is a true duplicate or clearly irrelevant, and say what you dropped
  in your reply. If it doesn't fit, change the layout (stack rows, add columns, grow the
  height); never delete data to make room
- **Then trim the prose, not the data:**
  - The title states the takeaway. A description only when it adds information the chart
    does not show anywhere (e.g. how a metric is defined). Never a description that explains
    an encoding the labels already make clear, or that repeats values shown in the chart
  - Drop prose that restates what the chart already shows (e.g. "X is the lowest, Y the highest")
  - Don't repeat the same figure in two places, except the key metric, which may also appear as a hero stat
  - Label values *or* draw a value axis, never both; value axes get 3 ticks (4 max)
  - Max 1 callout. When given, the report name goes in the label pill above the title and the sample size and source in the footer, never placeholders (see "Label pill and footer meta" above)
- **One message per chart:** the title states the takeaway in **Title Case**; the key metric is
  the accent color (mark + label), everything else `#1A1A2E`. Labels inside bars are centered
- **Gray text only for the least important information** (footer meta, axis ticks). See the preset
- **Neutral info cards:** `#F8F8FA` bg, `#1A1A2E` label and value; brand colors only
  for values that carry meaning
- **Numbers:** match source precision; thousands separators (`2,400`); units on values or in
  the scale eyebrow, not both
- **Self-contained:** the chart SVG has no JS, no external images, no `<image>` tags, no filters/drop shadows

## Palette policy

The chart palette in `references/example-feedback.md` is a **documented exception** to
your product's brand tokens: charts use their own tuned set (incl. coral series colors and chart
grays) because categorical data needs more distinguishable hues than a product palette usually offers.
- Use only the hexes listed in the preset file. The checker flags anything else
- Don't mix in your product UI grays; charts use chart grays. List them in `BRAND_TOKEN_GRAYS` in `scripts/check_chart.py` so the checker catches them
- The logo, Inter, white canvas, and NPS reserved colors still follow your brand tokens

---

## Final checklist

- [ ] `check_chart.py` passes with no ERRORs; PNG viewed and visually clean
- [ ] Canvas 720 wide, white, height derived from the stack
- [ ] Header, footer and logo placed per the preset's formulas
- [ ] Label pill only for a real, given report/series name; footer meta and source only for real, given figures, no placeholders
- [ ] Every data value plotted accurately (spot-check two by recomputing)
- [ ] Legend folded into the description, or replaced by direct labels
- [ ] Contrast: dark text on coral/yellow/teal; white only on the accent color or `#1A1A2E`
- [ ] Delivered with working PNG (1920px) + SVG (720px) download buttons, as the HTML preview or on a Design canvas artboard marked interactive
