---
name: tom-pmm-branded-slides
description: Create branded Google Slides presentations for Example Feedback (a fictional customer feedback platform). Use this skill any time someone asks to create a presentation, deck, slides, or pitch for the company, even if they don't say "branded" explicitly. Triggers include: "make a deck", "create slides", "build a presentation", "put together a pitch", "I need slides for X". Also use when converting an existing outline or document into a company presentation. This skill handles both content generation from a brief AND brand-consistent styling. Always use this skill for any company presentation task. Do not build slides without it.
---

# Branded Slides Skill

Produces on-brand presentations for Example Feedback using pptxgenjs (Node.js). The output opens in Google Slides or PowerPoint. Always read this skill fully before writing any code.

The examples use Example Feedback, a fictional customer feedback platform, and a placeholder palette. Replace the product name, colors, logos and background images with your own (see "Brand assets" below).

The design language is **clean, airy, and minimal**: bold titles, generous margins, lots of breathing room. Study the images in `assets/reference/` before building, if you have added them.

---

## Brand assets

The skill expects these files. The repo ships simple placeholder SVGs so the code runs. Replace them with your own artwork.

| File | What to put there |
|------|-------------------|
| `assets/logo-black.svg` | Full logo (mark + wordmark), dark version for light backgrounds |
| `assets/logo-white.svg` | Full logo, white version for dark or accent backgrounds |
| `assets/icon-black.svg` | Brand mark only, dark, used as the small watermark on content slides |
| `assets/icon-white.svg` | Brand mark only, white, for dark slides |
| `assets/cover-bg.svg` | Full-slide cover background (16:9): white on the left half, your brand shape cluster on the right half |
| `assets/slide-bg.svg` | Full-slide accent background (16:9): white slide with an accent organic shape bleeding from the right edge |

If your version of PowerPoint or Google Slides import does not render SVG images, export the two backgrounds as 2560x1440 PNGs and point `COVER_BG` and `SLIDE_BG` at the PNG files instead.

### Reference images (add your own)

`assets/reference/` is empty in this repo. Add screenshots of 10 to 15 slides from decks that already look the way you want, one JPG per layout, so Claude can anchor on the target look. Suggested set and file names:

- `slide-cover.jpg`: the standard cover (white left half, shape cluster right)
- `slide-light-bullets.jpg`: a light content slide with pill label, title and bullets
- `slide-light-twocol.jpg`: a two-column slide with the tinted right column
- `slide-light-table.jpg`: a table slide
- `slide-light-flow.jpg`: a simple left-to-right flow or process diagram
- `slide-light-contrast.jpg`: a contrast or before/after slide, often on the accent background
- `slide-dark-statement.jpg`: a single bold statement on the accent color
- `slide-dark-quote.jpg`: a customer quote on a dark background
- `slide-dark-closing.jpg`: the minimal closing slide
- `partner-cover.jpg`, `partner-two-col-bullets.jpg`, `partner-two-col-diagram.jpg`, `partner-stats-quote.jpg`, `partner-closing-logos.jpg`: slides from a co-marketing or partner deck, for the patterns in "Additional patterns from the partner deck" below

Use screenshots of your own decks only. Don't commit slides that show customer names, logos or data you don't have permission to publish.

---

## Brand Colors

Placeholder palette, replace with your brand.

| Role | Hex |
|------|-----|
| Accent primary (titles, bullets, borders) | `#2F6FEB` |
| Light accent (right-col bg, subtle fills) | `#E8F0FD` |
| Pale accent (cover icon decor circle) | `#CFE0FB` |
| Accent shape mid (cover decor) | `#7FA6F2` |
| Accent shape back (cover decor) | `#B7CDF7` |
| Teal (pill bg, table header, table border) | `#5CCFC0` |
| White (light slide bg, table rows) | `#FFFFFF` |
| Near-black (body text) | `#1A1A2E` |

---

## Accent Background (slide-bg)

`assets/slide-bg.svg`: white slide with an accent organic shape bleeding from the right edge. Use **sparingly**: 1 to 2 slides per deck maximum, most slides stay plain white.

```javascript
const ASSETS = 'assets';
const SLIDE_BG = `${ASSETS}/slide-bg.svg`;

function addSlideBg(slide) {
  slide.addImage({ path: SLIDE_BG, x: 0, y: 0, w: 13.33, h: 7.5 });
}
```

**When to use**: Statement slides, contrast/transition slides, key takeaway slides.
**Opt-in only**: Do not apply by default. It must be explicitly chosen for a specific slide.
**Important**: Keep text width to ~9.8" max, since the organic shape occupies the far right edge (~x > 11"). Use near-black text (not accent) since the bg is light.
**Do NOT combine** with `rightColBg()`: the shapes conflict. Choose one or the other.

---

## Typography

**Font**: Inter (all weights)

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| Cover title | 50pt | **Bold** | `#1A1A2E` |
| Light slide title | 38pt | **Bold** | `#2F6FEB` |
| Pill label | 12pt | Bold | `#1A1A2E` (UPPERCASE) |
| Body / bullets | 20pt | Regular | `#1A1A2E` |
| Bullet marker (✦) | 20pt | Regular | `#2F6FEB` |
| Dark slide text | 40pt | **Bold** | `#FFFFFF` |
| Closing word | 72pt | Regular | `#FFFFFF` |
| Speaker name | 20pt | Regular | `#2F6FEB` |

**Note**: All slide titles are bold. Pill labels are UPPERCASE + bold.

---

## Margins & Spacing Constants

```javascript
const M       = 0.55;   // left/right margin (tighter)
const MT      = 0.55;   // top margin for pill (increased)
const MB      = 0.55;   // bottom safe-zone
const PILL_H = 0.40;
const TITLE_Y = MT + PILL_H + 0.32;        // ~1.27"
const TITLE_H = 1.35;
const BODY_Y  = TITLE_Y + TITLE_H + 0.40;  // ~3.02"
const ICON_Y  = 7.5 - MB - 0.28;           // icon pinned above bottom margin
const CONTENT_W = 13.33 - M * 2;           // 11.73"
const COL_L_W   = 5.6;
const COL_R_X   = 6.93;
const COL_R_W   = 13.33 - COL_R_X - M;    // ~5.6"
```

These are mandatory. Do not reduce them. The generous gap below the title is key to the airy feel.

---

## Slide Layout: LAYOUT_WIDE (13.33" x 7.5")

### 1. Cover Slide
Reference: `assets/reference/slide-cover.jpg`, `assets/cover-bg.svg`

- **ALWAYS use `cover-bg.svg` as a full-slide background image**. Do not recreate the shapes manually.
  ```javascript
  s.addImage({ path: `${ASSETS}/cover-bg.svg`, x: 0, y: 0, w: 13.33, h: 7.5 });
  ```
- The image is white on the left half, with the brand shape cluster (your brand mark motif + accent gradient) on the right half
- **Title**: 52pt **Bold**, `#1A1A2E`, x=M, y=0.85, w=7.2, h=3.8
- **Speaker name**: 22pt Regular, `#2F6FEB`, x=M, y=5.0
- **Speaker title**: 17pt Regular, `#2F6FEB`, x=M, y=5.55
- **Logo**: `logo-black.svg`, x=M, y=6.9, **w=1.4, h=0.26** (smaller than content slides)
- **No icon watermark** on cover

### 6. Closing Slide
- **ALWAYS use `cover-bg.svg` as background**, same as cover
- Text: 72pt **Bold**, `#1A1A2E`, x=M, y=2.5, always bold
- Same small logo (w=1.4, h=0.26) bottom-left, no icon

### 2. Light Content Slide
Reference: `assets/reference/slide-light-bullets.jpg`

- Background: White `#FFFFFF`
- Teal pill → Bold title → ✦ bullets, all using margin constants
- **Icon**: `icon-black.svg`, x=12.63, y=6.82, w=0.42, h=0.42

### 3. Light Two-Column Slide
Reference: `assets/reference/slide-light-twocol.jpg`

- Right bg rect: x=`COL_R_X - 0.3`, y=0, w=`13.33-(COL_R_X-0.3)`, h=7.5, fill `#E8F0FD`, no border
- Left col: x=M, w=`COL_L_W`
- Right col: x=`COL_R_X`, w=`COL_R_W`

### 4. Table Slide
Reference: `assets/reference/slide-light-table.jpg`

- Header row: teal `#5CCFC0` fill, teal border `#5CCFC0` 1.5pt, bold text
- Body rows: white fill, teal border `#5CCFC0` 1.5pt
- All cells: same teal border color
- Start at `BODY_Y`, two equal columns with 0.15" gap

### 5. Dark Statement Slide
Reference: `assets/reference/slide-dark-statement.jpg`

- Background: `#2F6FEB`
- Text: Bold white, 40pt
- No pill

### 6. Closing Slide
Reference: `assets/reference/slide-dark-closing.jpg`

- Background: `#2F6FEB`
- Single phrase, 72pt Regular white, x=M, y=2.6
- Nothing else (no logo)

---

## Reusable Helper Functions

```javascript
const ICON_BLACK = `${ASSETS}/icon-black.svg`;
const ICON_WHITE = `${ASSETS}/icon-white.svg`;

function addIcon(slide, dark = false) {
  const sz = 0.28;
  slide.addImage({ path: dark ? ICON_WHITE : ICON_BLACK, x: 13.33 - M - sz, y: ICON_Y, w: sz, h: sz });
}

function addPill(slide, label) {
  const text = label.toUpperCase();
  const w = Math.max(1.5, text.length * 0.105 + 0.6);
  slide.addShape(pptx.ShapeType.roundRect, {
    x: M, y: MT, w, h: PILL_H,
    fill: { color: '5CCFC0' }, line: { type: 'none' }, rectRadius: 0.2,
  });
  slide.addText(text, {
    x: M, y: MT, w, h: PILL_H,
    fontFace: 'Inter', fontSize: 12, bold: true, color: '1A1A2E',
    align: 'center', valign: 'middle', charSpacing: 0.5,
  });
}

function addTitle(slide, text, opts = {}) {
  slide.addText(text, {
    x: M, y: TITLE_Y, w: CONTENT_W, h: TITLE_H,
    fontFace: 'Inter', fontSize: 38, bold: true, color: '2F6FEB',
    valign: 'top', ...opts,
  });
}

function bullets(slide, items, y, x = M, w = CONTENT_W, h = 3.8) {
  const rows = items.flatMap((item, i) => [
    { text: '✦  ', options: { color: '2F6FEB', fontSize: 20, fontFace: 'Inter', bold: false } },
    { text: item + (i < items.length - 1 ? '\n\n' : ''), options: { color: '1A1A2E', fontSize: 20, fontFace: 'Inter' } },
  ]);
  slide.addText(rows, { x, y, w, h, valign: 'top' });
}

function rightColBg(slide) {
  slide.addShape(pptx.ShapeType.rect, {
    x: COL_R_X - 0.3, y: 0, w: 13.33 - (COL_R_X - 0.3), h: 7.5,
    fill: { color: 'E8F0FD' }, line: { type: 'none' },
  });
}
```

---

## Table Helper

```javascript
function addTable(slide, rows, startY = BODY_Y) {
  // rows[0] = header row, rows[1..] = body rows
  const colW = (CONTENT_W - 0.15) / rows[0].length;
  const rowH = 0.82;
  const gap = 0.15;
  rows.forEach((row, ri) => {
    row.forEach((cell, ci) => {
      const x = M + ci * (colW + gap);
      const y = startY + ri * rowH;
      const isHeader = ri === 0;
      slide.addShape(pptx.ShapeType.rect, {
        x, y, w: colW, h: rowH,
        fill: { color: isHeader ? '5CCFC0' : 'FFFFFF' },
        line: { color: '5CCFC0', pt: 1.5 },
      });
      slide.addText(cell, {
        x: x + 0.22, y, w: colW - 0.22, h: rowH,
        fontFace: 'Inter', fontSize: isHeader ? 15 : 17,
        bold: isHeader, color: '1A1A2E', valign: 'middle',
      });
    });
  });
}
```

---

## Deck Structure

```
1.  Cover (white + shape cluster + icon decor)
2 to N. Light slides (bullets or two-col)
    1 dark statement per ~5 light slides
N.  Closing (dark accent, minimal)
```

---

## QA Checklist

- [ ] Cover: logo (not watermark icon), shape cluster, pale circle + white icon decor, bold title
- [ ] All light slide titles: bold, accent `#2F6FEB`
- [ ] All pill labels: UPPERCASE, teal bg, bold text
- [ ] Body text at `BODY_Y`: generous gap below title
- [ ] Tables: teal header row, white body rows, teal borders on all cells
- [ ] Two-col right half fills full slide height, no border
- [ ] Icon watermark bottom-right on every non-cover slide
- [ ] Dark slides: white bold text on `#2F6FEB`
- [ ] Font is Inter throughout

---

## What NOT to Do

- **Don't make titles Regular weight**: all titles are bold
- **Don't use lowercase pill labels**: always UPPERCASE
- **Don't use gray table borders**: tables use teal borders `#5CCFC0`
- **Don't reduce margins below M=0.8"**: keep the airy feel
- **Don't reduce BODY_Y spacing**: the gap below titles is intentional
- **Don't put logo on content slides**: icon watermark only
- **Don't add decorative lines**: the style has none

---

## Additional Patterns from the Partner Deck

Reference images: `assets/reference/partner-*.jpg` (add your own, see "Reference images" above). These patterns come from a co-marketing deck built for a partner. The examples below use Contoso, a fictional partner.

### Cover Variant B: Large Statement + Logo Bar
Reference: `assets/reference/partner-cover.jpg`

An alternative to the shape-cluster cover. Use for sales/outreach decks:
- **Background**: White `#FFFFFF`
- **Top-left label**: small gray text, 11pt, "Context label" (e.g. "Example Feedback for Contoso")
- **Top-right**: `logo-black.svg` (full logo with wordmark), right-aligned, ~1.8" wide
- **Title**: Very large (60 to 72pt), Regular weight, near-black `#1A1A2E`, left-aligned. Key word or phrase highlighted in accent `#2F6FEB` inline
- **Subtitle**: 18 to 20pt Regular, near-black, below title
- **Accent footer bar**: Full-width accent `#2F6FEB` rectangle, h=1.3", bottom of slide. Contains:
  - Client logos in white (centered), 18pt
  - One-liner descriptor in white below logos, ~14pt

### Two-Column: Left Bullets + Right Diagram/Screenshot
Reference: `assets/reference/partner-two-col-bullets.jpg`

- **Background**: White `#FFFFFF` (no right-col color fill: both cols are white)
- **Top-left section label**: small bold accent text, 12pt (e.g. "**Real world examples:** Context"), no pill
- **Left col**: Large bold title (28 to 36pt, near-black), then 3 bullet-style steps:
  - Accent filled circle `#2F6FEB` (diameter ~0.3") as bullet marker (not ✦)
  - Bold keyword + Regular description text, 20pt
  - Vertical accent bar `#E8F0FD` connecting bullets on the left edge
- **Right col**: Screenshot, diagram or UI mockup (image or shapes), ~55% of slide width

### Mixed-Background: Half-and-Half Stat + Quote
Reference: `assets/reference/partner-stats-quote.jpg`

- **Left half**: Accent `#2F6FEB` background, ~48% width, full height
  - Small UPPERCASE section label text, white, 11pt, top-left
  - Two logos/partner names on same line (white)
  - Large stat numbers: 52 to 64pt, white, Regular weight
  - Descriptor text: 18pt, white, lighter accent tint
- **Right half**: White background
  - Large `"` open-quote mark in accent `#2F6FEB`, ~80pt
  - Quote text: italic, 22 to 26pt, near-black
  - Speaker photo: circular, ~1.0" diameter
  - Speaker name + title: bold, 16pt, near-black

Use only real, approved quotes and stats here. Never invent a customer quote or number for a deck that will be shown externally.

### Closing: Text Top + Full-Width Accent Logo Bar Bottom
Reference: `assets/reference/partner-closing-logos.jpg`

- **Background**: White top ~60%, accent `#2F6FEB` bottom ~40%
- **Top**: Single closing sentence, 32 to 38pt Regular, near-black, centered horizontally, positioned upper third
- **Accent bar**: `x=0, y=4.5" approx, w=13.33", h=3.0"`, fill accent `#2F6FEB`
- **Inside bar**:
  - "Trusted by [Partner] **customers** like" in teal text, 18pt, centered
  - 2 rows of client logos in white, centered

### Inline Accent Highlight in Titles
A key pattern from the partner deck: part of the title is accent, the rest is near-black, on the same line:
```javascript
slide.addText([
  { text: 'You\'re ', options: { color: '1A1A2E', fontFace: 'Inter', fontSize: 64, bold: false } },
  { text: 'Personalizing', options: { color: '2F6FEB', fontFace: 'Inter', fontSize: 64, bold: false } },
  { text: ' On Clicks.', options: { color: '1A1A2E', fontFace: 'Inter', fontSize: 64, bold: false } },
], { x: M, y: 1.5, w: CONTENT_W, h: 2.5 });
```

### Accent Bullet Dots (circle style)
Alternative to ✦ bullets. Use for "Ask / Send / Trigger" style step lists:
```javascript
// Vertical connector bar (light accent)
slide.addShape(pptx.ShapeType.rect, {
  x: M, y: BODY_Y + 0.25, w: 0.06, h: 3.5,
  fill: { color: 'E8F0FD' }, line: { type: 'none' },
});
// Circle bullets
[0, 1.4, 2.8].forEach(offset => {
  slide.addShape(pptx.ShapeType.ellipse, {
    x: M - 0.12, y: BODY_Y + offset + 0.1, w: 0.3, h: 0.3,
    fill: { color: '2F6FEB' }, line: { type: 'none' },
  });
});
// Text items
['Ask what the user needs', 'Send data to integration', 'Trigger the right action'].forEach((text, i) => {
  slide.addText(text, {
    x: M + 0.35, y: BODY_Y + i * 1.4, w: COL_L_W - 0.4, h: 0.9,
    fontFace: 'Inter', fontSize: 20, bold: false, color: '1A1A2E',
  });
});
```

---

## Updated Design Rules (from both reference decks)

- **Title color mix**: Titles can be fully accent OR near-black with an accent word/phrase inline. Choose based on context
- **Cover title weight**: Regular (not bold) for very large statement titles (60pt+); Bold for 38 to 50pt titles
- **Bullet styles**: Use ✦ for standard content bullets; use accent circles + connector bar for sequential step lists (Ask → Send → Trigger)
- **No-pill variant**: For sales/outreach slides, replace the pill with a small bold accent inline label at top-left (e.g. "**Real world examples:** Context text")
- **Footer bars**: Accent full-width bars at the bottom are used for logo strips and social proof, a strong brand pattern
- **White-on-white two-col**: Some two-col slides have NO background color on the right. Both halves are white, differentiated only by content (diagram vs text)
