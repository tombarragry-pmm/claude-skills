# tom-pmm-branded-slides

Builds on-brand slide decks with pptxgenjs, ready to open in Google Slides or PowerPoint, from a brief or an existing outline. It fixes the palette, type scale, margins, slide layouts and helper functions so every deck has the same clean, airy look.

Originally built: November 2026

## What it does

1. Reads the brand rules and the reference slide images before writing any code.
2. Plans the deck: cover, light content slides (bullets, two-column, table), an occasional dark statement slide, and a closing slide.
3. Writes a pptxgenjs script using fixed margin constants and reusable helpers (pill label, title, bullets, tinted right column, table, icon watermark).
4. Uses the full-slide cover and accent backgrounds where the rules allow, plus optional partner-deck patterns (statement cover with logo bar, stat and quote split, circle-step lists, inline accent highlights).
5. Runs the QA checklist (bold titles, uppercase pills, teal tables, icon watermark, Inter throughout) before handing over the file.

## Files

- `SKILL.md`: the instructions Claude follows.
- `assets/logo-black.svg`, `assets/logo-white.svg`: placeholder full logos (dark and white).
- `assets/icon-black.svg`, `assets/icon-white.svg`: placeholder brand marks, used as the slide watermark.
- `assets/cover-bg.svg`: placeholder cover background (white left half, shape cluster on the right).
- `assets/slide-bg.svg`: placeholder accent background (organic shape on the right edge).
- `assets/reference/`: not included. Add your own reference slide screenshots here (the file list is in `SKILL.md`).

## Requirements

- Node.js with `pptxgenjs`.
- The Inter font installed on the machine that opens the deck, or a fallback will be used.

## Make it yours

The examples use Example Feedback, a fictional customer feedback platform, and a placeholder blue, teal and navy palette.

1. Replace the four logo and icon SVGs and the two background SVGs with your own artwork (export the backgrounds as PNG if your tools don't render SVG).
2. Swap the hex values in the Brand Colors table and in the helper functions for your brand colors.
3. Add 10 to 15 screenshots of your best existing slides to `assets/reference/` so Claude can match the look.
4. Replace the partner deck examples (Contoso) with your own co-marketing patterns, or delete that section.
