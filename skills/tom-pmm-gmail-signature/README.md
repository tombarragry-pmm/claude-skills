# tom-pmm-gmail-signature

Generates a paste-ready branded Gmail signature for a team member as a single self-contained HTML file, then walks them through installing it. Brand graphics are PNGs (embedded or hosted) because Gmail strips SVG on paste.

Originally built: November 2026

## What it does

1. Collects or confirms the person's full name and role in a labeled layout, and asks whether they want an optional "Book a call with me" button (and its link).
2. Runs `scripts/build_signature.py` to stamp the details into the fixed brand template: logo, category line, social icons and three feature pills.
3. Restyles automatically when the booking button is on (footer-nav links instead of filled pills, light pill-style social icons).
4. Hands over the HTML file and click-by-click Gmail install steps, including the expected quirks (Arial fallback, square pill corners).

## Files

- `SKILL.md`: the instructions Claude follows.
- `scripts/build_signature.py`: builds the signature HTML (Python standard library only).
- `references/gmail-paste-instructions.md`: the install steps and quirks to give the person.
- `assets/images/`: not included. Add your own brand PNGs here (the file list is in `SKILL.md`), or host them and set `IMAGE_BASE_URL`.

## Requirements

- Python 3 (standard library only).

## Make it yours

The template uses Example Feedback, a fictional customer feedback platform. In `scripts/build_signature.py`, replace `BRAND_NAME`, `BRAND_URL`, `CATEGORY_LINE`, `SOCIAL_LINKS`, the three `PILLS` (labels and URLs), the placeholder color constants, and `IMAGE_BASE_URL`. Then add your logo, social icons and pill icons as PNGs in `assets/images/`.
