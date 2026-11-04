---
name: screenshot-to-mockup
description: >
  Use this skill whenever the user uploads a screenshot and wants it converted into a marketing-ready UI mockup image. Triggers include any mention of mockup, clean up this screenshot, make this look like a marketing image, ghost out the background, UI illustration, or when a screenshot is uploaded alongside intent to use it in a campaign, landing page, social post, or sales asset. Also trigger when the user shares a product screenshot and asks for it to look more polished or less raw. This skill governs the full workflow: analyzing the image, proposing what to keep sharp vs. ghost, confirming with the user, then generating the HTML mockup and exporting a PNG.
---

# Screenshot to Mockup Skill

Transforms raw product screenshots (for example, from Example Feedback, a fictional customer feedback platform) into clean, marketing-ready UI mockup images. The style sits between a real screenshot and a wireframe: the focal UI content stays sharp and real, and everything surrounding it is abstracted into ghost placeholder elements.

**Golden rule: when in doubt, cut it out.** Be brutal. Fewer elements with more breathing room always beats a busy layout.

---

## Visual Style

**Canvas and card:**
- Background: `#F0F0F3`
- White card, `border-radius: 20px`, `box-shadow: 0 8px 40px rgba(0,0,0,0.07)`
- Card width: about 700 to 800px depending on content
- Canvas: 1200x800px default (ask if a different size is needed)
- Generous padding inside card: `52px 56px`

**Ghost elements:**
- Color: `#E8E8E8`, `border-radius: 6px`
- Ghost text lines: `height: 16px`, vary widths (e.g. 88% and 64%)
- Gap between ghost text lines: `margin-bottom: 20px` minimum between each line
- Single ghost line per chart bar row, never two stacked lines per row
- Nav tabs: `height: 11px`, varied widths, well spaced

**Spacing:**
- Always use `margin-right` for spacing between inline elements, never `gap` (wkhtmltoimage does not render `gap` reliably)
- Be generous: if elements look close, double the spacing
- Every section needs breathing room. Margin between sections should feel almost too big

---

## What to Keep Sharp vs. Ghost

**Keep sharp (render as real UI):**
- The focal product element: the key insight, survey question, chart, or interaction
- Any text that communicates the feature's value
- Brand-colored interactive elements where they aid clarity

**Ghost out (replace with placeholder blocks):**
- Nav bars, toolbars, sidebars: render as rounded gray pill or bar shapes
- Body text that isn't the focal point: replace with ghost lines
- Secondary panels, list items, irrelevant UI chrome
- Cut elements entirely if the layout feels crowded. Less is more

---

## Focal Element: Pill + Badge

The highlighted insight or key phrase goes in a tinted pill. The count badge sits **outside and after** the pill, never inside.

```html
<div style="display:inline-flex;align-items:center;background:#E8F0FD;border-radius:100px;padding:12px 22px;">
  <span style="font-size:15px;font-weight:600;color:#1E4FB8;white-space:nowrap;">"Focal phrase here"</span>
</div>
<div style="width:30px;height:30px;background:#2F6FEB;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;color:#fff;font-size:12px;font-weight:700;margin-left:12px;">18</div>
```

---

## Chart Pattern

No text anywhere in charts. Ghost label block on the left, colored bar on the right. Single ghost line per row. Bars fade from the full accent color to a light tint.

```
Accent scale (bar 1 to bar 5):
#2F6FEB, #5A8DF0, #8AAEF4, #B7CDF8, #DDE8FC
```

**Structure:**
```html
<div style="display:flex;flex-direction:column;">

  <!-- Row -->
  <div style="display:flex;align-items:center;margin-bottom:20px;">
    <div style="width:140px;flex-shrink:0;display:flex;justify-content:flex-end;padding-right:16px;">
      <div style="height:11px;width:110px;background:#E8E8E8;border-radius:6px;"></div>
    </div>
    <div style="flex:1;">
      <div style="height:24px;width:100%;background:#2F6FEB;border-radius:4px;"></div>
    </div>
  </div>

  <!-- Repeat with decreasing bar widths and lighter tints -->

</div>
```

Use `margin-bottom` on each row instead of `gap` on the container.

---

## Reusable UI Elements

### Nav tabs (generic)
```html
<div style="display:flex;margin-bottom:64px;">
  <div style="height:11px;width:44px;background:#B7CDF8;border-radius:6px;margin-right:32px;"></div>
  <div style="height:11px;width:56px;background:#E8E8E8;border-radius:6px;margin-right:32px;"></div>
  <div style="height:11px;width:40px;background:#E8E8E8;border-radius:6px;margin-right:32px;"></div>
  <div style="height:11px;width:68px;background:#E8E8E8;border-radius:6px;"></div>
</div>
```

### Report toolbar (optional, right-aligned actions)
Use when the screenshot is from a report view with actions in the top right. Place in a `justify-content:space-between` row with the nav tabs.

```html
<!-- Action pill button -->
<div style="display:inline-flex;align-items:center;background:#F2F2F2;border-radius:8px;padding:8px 14px;margin-right:60px;">
  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" style="margin-right:6px;">
    <path d="M12 2l2.4 7.4H22l-6.2 4.5 2.4 7.4L12 17l-6.2 4.3 2.4-7.4L2 9.4h7.6z" fill="#555"/>
  </svg>
  <span style="font-size:12.5px;font-weight:500;color:#333;">Edit</span>
</div>

<!-- Green tick -->
<svg width="20" height="20" viewBox="0 0 24 24" fill="none">
  <circle cx="12" cy="12" r="10" stroke="#22A55B" stroke-width="2"/>
  <path d="M7.5 12l3 3 6-6" stroke="#22A55B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```

---

## Brand Colors (replace with your own)

The values below are neutral placeholders. Swap in your own brand palette, and use brand colors only when the user confirms they should be applied:

| Token | Placeholder value |
|---|---|
| Primary accent | `#2F6FEB` |
| Light accent tint | `#E8F0FD` |
| Accent text | `#1E4FB8` |
| Nav tab active | `#B7CDF8` |
| Dark text | `#1A1A2E` |
| Ghost | `#E8E8E8` |

---

## Workflow

### Step 1: Analyze the screenshot

When the user uploads a screenshot:

1. Identify the **focal element**: the key UI moment to highlight.
2. Identify everything that can be cut or ghosted.
3. Infer the frame from context (browser chrome, email chrome, or plain card).
4. Present a concise proposal:

> **Focus:** [what you'll keep sharp]
> **Focal copy:** [exact text you plan to use. Flag if remixing from the screenshot, and suggest a marketing-friendly alternative if the original is too specific]
> **Ghost/cut:** [what gets abstracted or removed]
> **Frame:** [inferred frame + reason]
> **Canvas:** 1200x800px. OK, or is a different size needed?
> **Brand colors:** [yes / no. Ask if not specified]
>
> Happy with this, or want to adjust the focus or copy before I build?

Wait for confirmation before building.

### Step 2: Build the HTML

- Single self-contained HTML file, inline CSS only
- Canvas: `<body>` set to `width:1200px; height:800px`
- Always use `margin-right` for spacing, never `gap`
- Rebuild the focal element in HTML/CSS. Do not embed the original screenshot
- Read actual text from the screenshot for the focal element
- Keep text to a minimum. Only the focal phrase needs real text

### Step 3: Export as PNG

```bash
wkhtmltoimage --width 1200 --height 800 --zoom 2 output.html mockup.png
```

Share the PNG with the user.

### Step 4: Iterate

After presenting, ask:
> How does this look? Anything to adjust: focus, spacing, copy, colors, size?

Rebuild and re-export after each round of feedback.

---

## Output Sizes

| Use case | Canvas |
|---|---|
| Email / landing page feature section | 1200x800px (default) |
| LinkedIn landscape | 1200x627px |
| Social square | 1080x1080px |

---

## Common Mistakes to Avoid

- **Too much text:** real text renders poorly at small sizes, so ghost it
- **Elements too close:** always add more spacing than feels necessary
- **Using `gap`:** use `margin-right` / `margin-bottom` instead
- **Two ghost lines per chart row:** one line only
- **Badge inside the pill:** the badge always goes outside and after
- **Keeping too much UI:** be brutal, and cut anything that isn't essential
