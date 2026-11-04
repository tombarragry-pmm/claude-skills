# Chart recipes

Coordinates assume the Example Feedback preset; for Editorial research swap type and colors from
`editorial.md`. `Y0` = top of the chart block (from the header formula), `X0..X1` = the
plot area's horizontal extent.

## Contents
- Choosing a chart type
- Range / dot plot (house signature)
- Horizontal bar
- Bar + metrics table
- Vertical bar (single, grouped, stacked)
- Line / multi-line / area
- Scatter
- Pie / donut
- NPS breakdown
- Stat cards and stat blocks
- Waffle

---

## Choosing a chart type

| Data / question | Use |
|-----------------|-----|
| Compare categories, labels longer than ~8 chars or > 6 items | Horizontal bar |
| Compare few categories with short labels; or a time series with ≤ 12 periods | Vertical bar |
| Trend over time, many periods or several series | Line (area only for a single series' volume) |
| Distribution per group (median, P25 to P75, min to max) | Range / dot plot |
| Relationship between two numeric variables | Scatter |
| Parts of a whole, ≤ 5 parts | Donut (≥ 6 parts → horizontal bar sorted descending) |
| One headline share ("64 of 100") | Waffle or stat block |
| 2 to 4 headline numbers | Stat cards |
| Promoters / passives / detractors | NPS breakdown |

Sort categorical bars descending unless the categories have a natural order (time, scale,
funnel steps). Start value axes at zero for bars, always.

---

## Range / dot plot (house signature)

1. Label column: names `text-anchor="end"` at x = 20 + longest label width (typically 166; 208 for long names). Plot area X0 = label column + 24, X1 = 700
2. Tick row: 3 to 6 ticks, 14px `#6B6E7B` at baseline Y0; scale eyebrow (14px 700 ls 1 `#1A1A2E`, e.g. "LOG SCALE") at x=20 on the same baseline. First tick may anchor start, last anchors end at 700
3. Vertical grid `#F1F2F5` from Y0 + 12 to the bottom of the last row
4. Per row (pitch 60 to 78; 44 for dense 12+ row lists): optional full-scale line with end dots, flat `#CFE0FB` band P25→P75 rx=6, median pill 74×34 (or tick + 22px 800 value). Label only the median; P25/P75 values only on the row the takeaway is about
5. Row name 16px 600 vertically centered on the band (baseline = band center + 6). No per-row sub-labels. The total n goes in the footer
6. "All/total" row last, preceded by a `#E2E3E9` divider, pill in `#1A1A2E`
7. Log scales: say so in the scale eyebrow ("LOG SCALE · SECONDS")

## Horizontal bar

1. Label column: right-aligned at x = 20 + longest label width; X0 = that + 16
2. Row pitch 40 (h=24 bar) or 34 (h=20); bar y centered in the pitch
3. Scale: with tracks, percentages use a fixed 0 to 100% scale (the track = 100%), so a 50% bar must look half-full. Absolute values (counts, seconds) scale to the max, so the longest bar fills its area; shared scales across related charts
4. **With tracks** (default): track spans X0..644 (`#E8F0FD` for accent bars, `#F1F2F5` otherwise); values sit in a right column, 16px 700, `text-anchor="end"` at x=700. Never let a value sit on top of a track
5. **Without tracks** (dense or mixed-sign data): values at bar end + 8; bar area X0..700 minus widest value minus 8. Values inside bars: centered in the bar (see Element conventions)
6. Bars `rx = h/2`; value baseline = bar center + 5; optional vertical grid `#F1F2F5` only when no value labels
7. Ranked lists: 2-digit 16px 800 accent rank at x=20, labels start-anchored at x=52, X0 = 52 + longest label + 16
8. Key row: accent bar, accent name and value; other rows `#1A1A2E` bars, names and values

## Bar + metrics table

For rows that carry a bar *and* several metrics (overlap %, responses, teams…). Keep
every column the user provides.

1. **Optional hero block** above the table for the key metric: eyebrow 14px 700 ls 1
   `#1A1A2E` → 56px 900 `#2F6FEB` value; the defining sentence (16px 400 `#1A1A2E`, up to
   3 lines, key numbers 800) sits to its right, top-aligned with the value
2. **Column header row** (14px 700 ls 1 `#1A1A2E`, UPPERCASE): scope/name header at x=20;
   metric headers right-aligned to their column's right edge. Column width = max(header,
   widest value) + 24; the last column ends at 700
3. **Rows, stacked** (pitch 64, `#F1F2F5` 1px divider under each): name 16px 600 at
   baseline `top + 22`; bar h=12 rx=6 on a full-width track from x=20 to the first metric
   column minus 24, at `top + 32`; per metric column a primary value 16px 800 (baseline
   `top + 24`) with an optional secondary value 14px 400 below (baseline `top + 44`),
   both `#1A1A2E`, right-aligned
4. Key row: name 800, bar and its metric (primary + secondary) in `#2F6FEB`; other columns stay `#1A1A2E`
5. Reference / non-comparable rows go last after a `#E2E3E9` divider: reference row with a
   full `#D0D2DA` bar (visibly distinct from an empty `#F1F2F5` track) and the word "Reference" (14px 400) in the metric column;
   non-comparable rows with an empty track and "Not comparable". Their other columns still show
6. Sort by the bar metric unless the source order carries meaning
7. **Short names (≤ 120px, e.g. "5 points")**: keep them inline instead of stacked: name
   16px 600 at x=20 vertically centered on a h=24 bar; bar from `20 + widest name + 16` to
   the first metric column minus 24; primary/secondary values stacked in each column as above
8. Label the bar metric in a column, not on the bar, when the table already has value
   columns; add a bar header ("SHARE OF RESPONSES") at the bar's x so the bar's meaning is
   explicit without a description
9. Any non-zero value gets a visible bar: minimum width 4px (rx 2); zero stays empty

## Vertical bar (single, grouped, stacked)

1. Y axis: 3 tick labels (0, mid, max) 14px `#6B6E7B` end-anchored at X0 minus 8, X0 = 20 + widest tick label + 8; horizontal grid `#F1F2F5`; baseline `#D0D2DA`
2. Plot height 220 to 300; 15% headroom above the max, rounded up to a nice tick (1, 2, 2.5, 5 × 10ⁿ)
3. Slot = (700 − X0) / n; bar width = slot × 0.6 (max 64); grouped: group width = slot × 0.72, bars touch with 4px gaps
4. Top-rounded bars: `<path>` with 4px radius on the top corners only; square at the baseline
5. Label values *or* show a y axis, not both. Value 16px 800 `#1A1A2E` 8px above the bar; category 16px 600 `#1A1A2E` centered, baseline = plot bottom + 22
6. Stacked: segments in series order bottom→top, 2px white gaps (stroke `#FFFFFF` 2); label segments ≥ 20px tall centered inside (both axes), `#1A1A2E` or white per contrast rules
7. Long category labels: switch to horizontal bars. Don't rotate text

## Line / multi-line / area

1. Axes and grid as vertical bar; x ticks at each period (or every 2nd/3rd if > 12)
2. Lines 3px, `stroke-linejoin="round" stroke-linecap="round"`, `fill="none"`. Points only at the last value (r=5, 2px white stroke) and at a callout target, not on every period
3. Multi-line: key series accent 3px with an accent 16px 800 end label; other series `#1A1A2E` 2px with 16px 600 `#1A1A2E` end labels. Label each series directly at the right end (8px right of the last point); reserve that label width when computing X1. Separate end labels vertically by ≥ 16px
4. Dashed series (forecast/benchmark): `stroke-dasharray="6 4"`
5. Area: single series only, fill series color `fill-opacity="0.1"` down to the baseline, drawn before the line
6. Up to 2 callouts at notable points (peak, inflection). A callout must not cover any line or point. Slide the box along its arrow edge (arrow stays on target) until it sits in clear space
7. Grid lines stop at X1; the end-label column stays clean
8. More than 8 periods: label the x axis at the coarser unit only (years for quarterly data, 14px `#6B6E7B`, centered on each year's span) with 4px tick marks `#D0D2DA` per period
9. End labels for yellow or teal-light series use `#1A1A2E` (contrast); the adjacent point carries the color

## Scatter

1. Both axes with round ticks; grid both directions `#F1F2F5`
2. Points r=5 `#2F6FEB` `fill-opacity="0.7"`, no stroke; highlight group in the accent color, others `#9B9DA8` at 0.5
3. Axis titles are required here: 14px 700 `#1A1A2E`, x-title centered below ticks, y-title as an eyebrow at x=20 above the plot
4. Label ≤ 3 notable points (14px 600, 6px offset); optional trend line `#1A1A2E` 1.5px dashed `4 4`

## Pie / donut

Prefer donut. Outer r = 110 to 130, inner r = outer × 0.55. Center: total or key share
(40px 800 `#1A1A2E`) + 14px caption.
1. Slices as arc paths from 12 o'clock clockwise, largest first; 2px white separators (stroke `#FFFFFF` 2)
2. **Direct labels, no legend:** place the donut left (center x = 20 + r + 10); label list on the right, one row per slice aligned to its order: 12×12 rx=3 swatch, name 14px 600, value 14px 700 end-anchored at 700
3. Slices < 3% merge into "Other" `#9B9DA8`

## NPS breakdown

1. 100% stacked horizontal bar per group, h=32 rx=6 (outer ends only), segments: detractors `#C8414F` (left), passives `#F0C04F`, promoters `#5DC98A`
2. No segment percentages by default. The score column carries the message. Add them (14px 700, white on detractors, `#1A1A2E` on others, segment ≥ 44px, centered in the segment) only when the takeaway is about the split itself
3. NPS score end-anchored at 700: 22px 800 `#1A1A2E`, column eyebrow "NPS" 14px 700; negative scores use a real minus `−`
4. Legend: stat blocks above the bars with segment-colored rules (see Stat blocks). Only if there are no stat blocks, one description line naming the colors

## Stat cards and stat blocks

Only for figures the takeaway is about. Sample sizes, company counts and derived context
(spreads, averages of the sample) never get cards: they go in the footer meta line.


- **Cards:** 3 (or 2/4) equal cards across x=20..700, 16px gutters, rx=12, `#F8F8FA`, padding 20. Eyebrow 14px 700 ls 1 `#1A1A2E` → value 36px 800 (`#1A1A2E` neutral, series color if meaningful). Support copy only if the eyebrow can't say it
- **Stat blocks** (no card): eyebrow 14px 700 ls 1 `#1A1A2E` at baseline `y`, value 56px 900 `#2F6FEB` at `y + 60`. No support copy. Put the context in the eyebrow ("PROMOTERS"). **Stat blocks can be the legend:** when they report segments shown below (detractors / passives / promoters), color each left rule in its segment color (4px wide), set the values in `#1A1A2E`, and drop the description. Otherwise optional 3px `#CFE0FB` left rule from `y − 11`, height 86, text at rule + 16. Blocks share x=20..700 with 24px gutters; check the widest value leaves ≥ 24px before the next rule. Next section starts ≥ 64px below the value baseline

## Waffle

10×10 circles r=11, 30px pitch (grid 291px square), filled `#2F6FEB` row by row from top-left,
remainder `#E2E3E9`. Place left; caption on the right or below: 20px 700 `#1A1A2E` sentence
in 22px 800 with the number in the accent color (e.g. "~64 responses mention onboarding").
