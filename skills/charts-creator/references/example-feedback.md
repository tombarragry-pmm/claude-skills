# Example Feedback preset

White canvas, confident 32px title, the accent color as the single hero accent, generous whitespace.
Everything below is in px on the 720-wide canvas. All hex values are placeholders for a
fictional brand: swap in your own palette, and update the list in `scripts/check_chart.py` to match.

## Contents
1. Header layout
2. Footer layout
3. Typography
4. Chart palette (exception to brand tokens)
5. Element conventions
6. Callout boxes
7. Simplification rules

---

## 1. Header layout

Computed top-down. `T` = baseline of the last title line, `D` = baseline of the last description line.

| Element | Spec | Position |
|---------|------|----------|
| Label pill (optional, report/series name) | Pill: `#E8F0FD` rect, height 28, rx=14, width = text width + 24. Text: 14px 700, letter-spacing 1.2, `#2F6FEB`, UPPERCASE, centered in the pill (baseline y=59), e.g. `FEEDBACK TRENDS · 2026` | x=20, y=40 (above the title, left-aligned) |
| Title line 1 | 32px **900** `#1A1A2E`, **Title Case** (rules below) | x=20, baseline y=116 with a label pill (≈24px clear between pill and cap height), y=66 without |
| Title line 2 | same | first baseline + 38 |
| Description (optional) | 16px 400 `#1A1A2E`, **1 line preferred**, max 2, line height 24 | first baseline `T + 42` |
| First chart element | tick labels, column eyebrows, first row | baseline ≥ `D + 44` (no description: `T + 52`) |

- **Title width:** ≤ 680px. Never put a label to the right of the title; it always goes in the pill above.
  Wrap at a word boundary so line 2 carries at least two words (no orphan) and line 1 doesn't end on a short word (the, a, of, to, and, are…). If two lines
  aren't enough, shorten the title
- **Title capitalization (house style guide):** Title Case. Capitalize every word except
  articles (a, an, the), coordinating conjunctions (and, but, or, nor, for, so, yet) and
  prepositions of 3 letters or fewer (at, by, in, of, on, to, up, per, via, vs), which stay
  lowercase unless first or last. Capitalize both parts of hyphenated words (E-Commerce,
  Year-Over-Year). Keep acronyms as written (NPS, CSAT, SaaS). Numerals for numbers, no
  final period, no en or em dashes (write ranges as `2024-2026`). The checker enforces this
- Description, labels and legends use sentence case; category names keep their own casing
- **The title carries the takeaway** whenever it can ("Short Surveys Get 3× More
  Responses"); then the description is often unnecessary

## 2. Footer layout

`C` = the lowest pixel of chart content (text bottom, bar bottom, axis label bottom).

| Element | Spec | Position |
|---------|------|----------|
| Clear space | n/a | `H = C + 96`: divider 28px below content, logo 28px below the divider |
| Divider (optional, for closure) | `#E2E3E9` 1px | x=20..700, y=`H − 68` |
| Logo | `assets/logo-snippet.svg` (placeholder), fill `#1A1A2E` | `translate(20, H−40) scale(0.135)` → box x 20..127, y H−40..H−20 |
| Meta line (optional) | 14px 400 `#6B6E7B`, **one line**, e.g. `n = 2,400 responses` | `text-anchor="end"` x=700, baseline `H − 25` |

- Meta = sample size and other context figures (e.g. `n = 2,400 responses · 180 teams ·
  P25-P75 spread 18.2 pts`). Must fit x=151..700 on one line; if not, keep the sample size
  there and move the rest onto the source line
- **Source line** (URL or report name, whenever given): 14px 400 `#6B6E7B`, x=20, baseline
  `C + 32`; divider at `C + 56`; then `H = C + 124` so the logo and meta sit as usual
- Omit what you don't have; never invent a sample size or source

## 3. Typography (all Inter)

Minimum size is **14px** for every piece of text. Hierarchy comes from weight as much as
size: five weights, each with a job. Skip a step between neighbors (600 name next to an 800 value).

| Weight | Job |
|--------|-----|
| **900** Black | Title, hero stat values |
| **800** ExtraBold | Data values, pill and callout values, score columns, "total" row names |
| **700** Bold | Eyebrows, zone labels |
| **600** SemiBold | Category / row / series names |
| **400** Regular | Description, ticks, captions, footer |

| Element | Size | Weight | Fill |
|---------|------|--------|------|
| Title | 32 | 900 | `#1A1A2E` |
| Description | 16 | 400 | `#1A1A2E` |
| Label pill text (report name) | 14, ls 1.2 | 700 | `#2F6FEB` on `#E8F0FD` |
| Axis tick labels | 14 | 400 | `#6B6E7B` |
| Scale / column eyebrow ("LOG SCALE", "NPS") | 14, ls 1 | 700 | `#1A1A2E` |
| Category / row name | 16 | 600 | `#1A1A2E` |
| "All / total" row name | 16 | 800 | `#1A1A2E` |
| Data value labels | 16 | 800 | series color or `#1A1A2E` |
| Big stat below a marker | 22 | 800 | accent color |
| Headline score column (e.g. NPS) | 22 | 800 | `#1A1A2E` (key row `#2F6FEB`) |
| Hero stat value | 56 | 900 | `#2F6FEB` |
| Pill value text | 16 | 800 | `#FFFFFF` |
| Callout value (caption optional) | 16 / 14 | 800 / 400 | `#FFFFFF` / `#D0D2DA` |
| Footer meta | 14 | 400 | `#6B6E7B` |

Use one size per role within a chart. Row sub-labels are not part of the scale. If a
row genuinely needs one, it's 14px 400 `#1A1A2E`.

**Label color, two colors only:** the **key metric** (the row, series, bar or number the
title is about) is the accent `#2F6FEB`, both its mark and its label (name, value, callout).
Every other label is `#1A1A2E`. No text in coral, yellow, teal or any other hue, even when
the mark has that color. Marks follow the same logic: key mark accent, other marks `#1A1A2E`
(lines 2px, pills and bars solid), with light non-text supports (`#E2E3E9` bands,
`#F1F2F5` tracks and zones). Exceptions: marks with fixed meaning (NPS segments) keep their
colors; charts with no single key metric (every series equally important) use the series
palette for marks, with all labels `#1A1A2E`. Callouts on the key metric are accent boxes.

**Gray text is only for the least important information:** the footer meta line and axis
tick labels (`#6B6E7B`). Everything else (titles, descriptions, eyebrows, column and
legend labels, row names, values) is `#1A1A2E` or a brand color. Grays stay available for
non-text structure (grid, tracks, dividers).

## 4. Chart palette (exception to your brand tokens)

Deliberately kept separate from the product's brand-token palette. These are the only
colors allowed in Example Feedback charts (the checker enforces this list).

| Role | Hex |
|------|-----|
| Accent main: primary series, pills, markers | `#2F6FEB` |
| Accent dark / darker: emphasis, hover-like depth | `#1F5AD6` / `#1A48A8` |
| Accent 100: range bands | `#CFE0FB` |
| Accent 50: chips, bar tracks | `#E8F0FD` |
| Coral main: second series | `#F2643D` |
| Coral mid / light: tier ramps | `#F58A6A` / `#FAC3B1` |
| Coral dark: negative/alert (never pure red) | `#D4602F` |
| Yellow | `#F5C243` |
| Teal light / main / dark | `#C9EFEA` / `#5CCFC0` / `#3B8C82` |
| Gray 900: titles, callouts, "total" pills, logo | `#1A1A2E` |
| Gray 700: non-text only (e.g. neutral marks) | `#44475A` |
| Gray 500: footer meta and axis ticks only | `#6B6E7B` |
| Gray 300: muted series, non-text marks only | `#9B9DA8` |
| Gray 200: callout captions, axis baseline | `#D0D2DA` |
| Gray 100: dividers, waffle remainder | `#E2E3E9` |
| Gray 50: grid lines, neutral tracks | `#F1F2F5` |
| Gray 25: neutral card fill | `#F8F8FA` |
| NPS reserved (from brand tokens): promoters / passives / detractors | `#5DC98A` / `#F0C04F` / `#C8414F` |

**Series order:** accent → coral → yellow → teal (→ accent dark → coral mid).
More than 4 series is a smell. Group the tail into "Other" in `#9B9DA8` or split the chart.
**Highlight pattern:** one series/row in the accent color, everything else `#D0D2DA` or `#9B9DA8`.
**Tier ramps:** coral → yellow → teal light → teal.
**NPS colors** are used only for promoter/passive/detractor segments, nowhere else.

**Text on fills (WCAG checked):**
- White on `#2F6FEB` (4.6:1), `#1A1A2E`, `#C8414F` (4.9:1)
- `#1A1A2E` on coral, yellow, teal, NPS green/yellow, `#CFE0FB`, `#E8F0FD`
- `#D4602F` as text only at ≥19px 700+ (3.81:1 on white passes large text only).
  Smaller negative values: `#1A1A2E` with a real minus sign `−`
- `#9B9DA8` (2.7:1) is never used for text

## 5. Element conventions

- **Grid:** `#F1F2F5` 1px; horizontal for vertical bars/lines, vertical for horizontal bars/range plots. 4 to 6 lines at round values. Zero/baseline line `#D0D2DA` 1px
- **Range / box bands:** flat `#CFE0FB`, h≈26 (16 to 20 in dense lists), rx=6. Never translucent, outlined, or full-pill
- **Median markers:** 3px vertical tick `#2F6FEB` (second series `#3B8C82`), extending ~7px past the band top and bottom
- **Median value pills:** 74×34, rx=17, `#2F6FEB` (`#1A1A2E` for "all/total" rows), white 16px 800 centered; clamp inside the chart area near either end
- **Full-scale lines:** `#1A1A2E` stroke 2 with r=3.5 filled end dots
- **Labels inside bars, pills and segments are always centered:** `text-anchor="middle"` at the shape's horizontal center, baseline = vertical center + 0.35 × font size. If a label doesn't fit centered with 8px padding each side, move it outside. The checker enforces this
- **Horizontal bars:** pill bars (rx = h/2, h 20 to 24) on `#E8F0FD` or `#F1F2F5` tracks; value 16px 800 at bar end + 8, or centered inside the bar (white on accent/black) when the bar is long enough
- **Vertical bars:** rx=4 on top corners (use a path, or rx=4 with bottom masked by baseline); value 16px 700 centered 8px above the bar
- **Chips (P25/P75, language codes):** flat `#E8F0FD` pills, accent 14px 700, no outline
- **Brackets (IQR etc.):** `#2F6FEB` 1.5px, 6px rounded corners (Q curves)
- **Stat blocks:** eyebrow → 54px accent value → 15px support copy; exact offsets in `recipes.md`
- **Reference lines** (NPS zero, target, average): `#F2643D` 1.5px (dashed `6 4` for targets/averages); label 14px 700 `#1A1A2E` in clear space near the line, with the value
- **Highlight zones:** flat `#E8F0FD` rect behind the data, no stroke; label inside top-left 14px 700 ls 1 `#2F6FEB`
- **Row dividers:** `#F1F2F5` 1px; `#E2E3E9` before an "all/total" row
- **Data labels vs axis:** if every bar/point has a value label, drop the value axis and its grid entirely

## 6. Callout boxes

`#1A1A2E` rect, rx=6, padding 8×12 (`#2F6FEB` when it points at the key metric). Value line 16px 800 white; caption 14px 400 `#D0D2DA`
(never white). Value only: box height 36, baseline top + 24. With caption: height 50, baselines top + 22 / top + 40. Prefer value only. Always a filled triangular arrow ~10×6 flush to the edge facing the target,
never a line connector. The arrow tip sits 4px from the target mark.

```svg
<!-- rect spans x rx1..rx2, y ry1..ry2; arrow centered at cx or cy -->
<polygon points="{cx-5},{ry2} {cx+5},{ry2} {cx},{ry2+6}" fill="#1A1A2E"/>  <!-- box above target, points down -->
<polygon points="{cx-5},{ry1} {cx+5},{ry1} {cx},{ry1-6}" fill="#1A1A2E"/>  <!-- box below, points up -->
<polygon points="{rx2},{cy-5} {rx2},{cy+5} {rx2+6},{cy}" fill="#1A1A2E"/>  <!-- box left, points right -->
<polygon points="{rx1},{cy-5} {rx1},{cy+5} {rx1-6},{cy}" fill="#1A1A2E"/>  <!-- box right, points left -->
```

Pick the side that keeps the box inside x=20..700 and off every label; prefer above. Max 1
callout per chart (2 only on a chart with no description). The arrow may be shifted along its edge (≥8px from a corner) to stay aligned.

## 7. Simplification rules

- No HIGHEST / LOWEST / FASTEST badges. The takeaway lives in the description
- No legend rows. Explain encoding in the description, or label series directly at the line end / on the slice
- No axis titles when units fit in the scale eyebrow or tick labels ("0%", "10s")
- Shorten row sub-labels to the essential number ("320 RESPONSES")
- No hero panels, gradients, shadows, 3D, or icons as decoration
