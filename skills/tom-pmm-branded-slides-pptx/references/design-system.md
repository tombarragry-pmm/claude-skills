# Branded Slides: Design System

The visual rules that make a deck feel designed rather than templated. All values are already wired into `scripts/slide_kit.py`; this doc explains the intent so you make good choices when composing.

All hex values below are a placeholder palette for Example Feedback, a fictional brand. Replace them with your brand, here and in the token block at the top of `slide_kit.py`.

## Color tokens

Accent (lead with the deeper primary, not a pale tint):
- `#2f6feb` primary. Impact surfaces, hot cards, key accents.
- `#4a80ee`, `#7fa6f2` lighter accents, ghosted numerals live around `#e8f0fd`.
- `#163d8f`, `#0f2a63` deep accent for dark slides and section dividers.
- `#e8f0fd`, `#f3f7fe` light accent tints.

Teal (the accent that makes it pop, used deliberately):
- `#5ccfc0` spot marks, diamond bullets, highlight words on dark.
- `#2f9e90` teal highlight on light, teal divider background.
- `#c9efea` teal tint for cards and callout bars.

Neutral:
- `#1a1a2e` text and near-black slides, `#44475a` body, `#9b9da8` muted, `#e2e3e9` lines, `#ffffff`.

Gradients are allowed on hero surfaces only (cover, close, and where you want drama). Cover uses `radial-gradient(130% 130% at 82% 18%, #5b8ef5, #2a62d9 42%, #12357f)`. Do not gradient-fill content slides.

## Type

Font is Inter, bundled in `assets/fonts` (weights 400 to 900 plus italics). Never substitute.
- Hero: 70 to 88px, weight 800 to 900, letter-spacing -1.5 to -2px.
- Section title (content slides): 46px, weight 800, tighten to -0.6px.
- Divider numeral 150px / 800, divider title 64px / 800.
- Eyebrow: 13px, weight 700, letter-spacing 2.5px, uppercase.
- Body: 19 to 20px, weight 400. Bold lead-ins at 700.

Signature move: **inline-highlight headlines**. Near-black title with exactly one word wrapped in `<hl>` (accent) or `<hlt>` (teal). Do not make the whole title accent-colored, and do not do it on every slide.

## The brand mark motif

Use the brand mark as a graphic device, not just a corner logo:
- Large, 300 to 760px, bleeding off an edge, low opacity (0.07 to 0.14 on color fills, 0.20 to 0.30 as a ghost on light).
- One solid teal mark, 120 to 150px, as a spot accent on hero and divider slides.

The `mark(color, size, style, opacity)` helper recolors and positions it. It reads `assets/brand/icon-black.svg`, which must use a `viewBox="0 0 147 147"` and a single fill of `#1A1A2E` so it can be recolored. The repo ships a placeholder shape: replace it with your own mark. Logos live in `assets/brand` (use white on dark, black on light).

## Rhythm

Do not ship a deck of all-white slides. Introduce a dark or colored slide roughly every 3 to 4 slides: a near-black or deep-accent statement early, deep-accent section dividers with one teal divider for contrast, accent side panels on the agenda and intro. The archetypes below already carry this.

## Archetype catalog

Each maps to a proven layout. Reference images live in `assets/reference`. That folder is not included in this repo: add one screenshot per archetype from decks that already look the way you want, using the file names below.

| Function | Use for | Reference image |
|---|---|---|
| `cover(...)` | Title slide | slide-cover.jpg, partner-cover.jpg |
| `statement(...)` | A single bold point, dark | slide-dark-statement.jpg |
| `divider(num, title, page, theme)` | Section breaks, `theme='deep'` or `'teal'` | slide-dark-statement.jpg |
| `agenda(title, items, page)` | Contents, accent side panel + numerals | slide-light-twocol.jpg |
| `split(...)` | Left color panel + right labeled rows | slide-light-twocol.jpg |
| `bullets(..., aside_html)` | Points, optional right-side visual | slide-light-bullets.jpg |
| `cards(...)` | 2 to 4 tiles, first can be `hot` (solid accent) | slide-light-contrast.jpg |
| `close(title, url)` | Closing, mirrors the cover | slide-dark-closing.jpg, partner-closing-logos.jpg |

For a flow diagram or anything bespoke, compose custom HTML with the shared CSS classes plus `mark()`, `doc()`, `foot()`. `scripts/example_deck.py` includes a `flow_three` custom slide as a pattern. Reference: slide-light-flow.jpg, partner-two-col-diagram.jpg.

The `partner-*.jpg` files are slides from a co-marketing deck (for example "Example Feedback x Contoso"). Only commit screenshots you have permission to publish, with no customer names, logos or data.

Aim for 2 to 3 real "moments" per deck: a statement hook, a signature diagram or pull-quote, and a bookended cover/close.

## Copy rules

- No em dashes or en dashes anywhere. Use colons or periods. (Hyphens in compound words are fine.)
- US English. Curly quotes and apostrophes (`&#8220; &#8221; &#8216; &#8217;`), never straight quotes.
- Active voice, contractions, lead with the outcome or pain, not the feature name.
- Product naming: in the examples, Example Feedback is a customer feedback platform with two products, Surveys and Feedback Lab. Replace with your own product names and list any retired names here so they never appear (for example, "Never 'Old Product Name'").
- Avoid: focused, excited to announce, agentic, seamless, best-in-class, next-gen, powerful, robust, revolutionary. Never reference retired features by name.

## Do / Don't

Do: bold large type, one clear idea per slide, generous whitespace with a strong focal point, teal used sparingly, rounded corners (16 to 18px), the deep accent on impact surfaces.

Don't: pale accent titles on every slide, everything centered and evenly spaced, multiple accent colors competing in one composition, thin font weights, drop shadows on text, the logo on a busy background without a clear zone.
