# Editorial research preset

Editorial research-report style: left-aligned, compact, whitespace instead of rules. Same
shared canvas rules as SKILL.md (720 wide, white, content x=20..700, top margin 40).
Series colors are placeholders; swap in your own.

## Header

| Element | Spec | Position |
|---------|------|----------|
| Title | 24px 900 `#111111`, Title Case (same rules as the Example Feedback preset), max 2 lines, line height 30 | x=20, first baseline y=62 |
| Subtitle / methodology | 14px 400 `#6B7280`, 1 line preferred, line height 20 | first baseline = last title baseline + 26 |
| First chart element | n/a | baseline ≥ last subtitle baseline + 32 |

## Footer

No logo. Source footnote: 14px 400 italic `#6B7280`, x=20, baseline `H − 40`;
place it ≥24px below the last chart content: `H = C + 24 + 40`. Never use dividers.

## Typography (all Inter)

| Element | Size | Weight | Fill |
|---------|------|--------|------|
| Title | 24 | 900 | `#111111` |
| Subtitle | 14 | 400 | `#6B7280` |
| Category label | 14 | 600 | `#374151` |
| Rank number (`01`, `02`) | 14 | 800 | series color |
| Value label | 14 | 700 | `#111111`, or `#FFFFFF` inside accent bars |
| Axis ticks | 14 | 400 | `#6B7280` |
| Stat value | 32 | 900 | series color |
| Stat label | 14 | 400 | `#6B7280` |
| Source footnote | 14 | 400 italic | `#6B7280` |

## Palette (checker-enforced)

Series 1 to 6: `#2F6FEB`, `#F2643D`, `#F5C243`, `#5CCFC0`, `#1F5AD6`, `#F58A6A`.
Text: `#111111`, `#374151`, `#6B7280`, `#9CA3AF`. Neutral series `#9B9DA8`, track `#F1F2F5`,
grid `#F1F2F5`. White text only on `#2F6FEB` / `#1F5AD6`; `#111111` on every other series color.
Likert / diverging scales: `#F2643D` → `#F58A6A` → `#9B9DA8` (neutral) → `#5CCFC0` → `#3B8C82`.

## Styles

- **Horizontal bars:** label column right-aligned, width = longest label + 12 (max 200);
  chart from label column + 32. Track `#F1F2F5` rx=4 h=24; bar series color rx=4 h=24;
  row pitch 36. Ranked lists: 2-digit colored rank before the label
- **Stat cards:** 2 to 4 equal cards filling x=20..700 with 12px gutters, rx=12, fill = series
  color with `fill-opacity="0.08"`, padding 16×20; value then label
- **Separation:** whitespace only (≥16px between groups); no dividers, no borders
- Otherwise follow `recipes.md`, swapping in this preset's type and colors
