---
name: tom-pmm-panel-ui
description: Mocks up screens of the Example Feedback app (a fictional customer feedback platform) as downloadable PNG images, built from the app's own tokens and components so they look like the real product. ALWAYS use this skill, without asking, whenever anyone mocks up, sketches, designs, recreates or reviews a screen, flow, modal, settings page, table or empty state of the app, or asks which button, tab or dialog size to use. Output is an HTML preview with Download PNG buttons, rendered by this skill's scripts. Not for marketing visuals or standalone charts.
---

# App screen mockups

This skill produces product screens as images that match the live app: same tokens, same components, same layout rules. The examples use Example Feedback, a fictional customer feedback platform, with placeholder tokens. Replace `references/tokens.md` and `assets/app-mockup-base.html` with your own product's values, measured from the live app.

The live app usually contains drift: hardcoded hex values, one-off greys, duplicate components. **Never copy drift into a mockup.** When a screenshot disagrees with this skill, this skill wins.

## Core rules

These are the decisions most likely to be gotten wrong. Read them before producing anything.

1. **Tokens only.** Every color is a token from `references/tokens.md`. Never a raw hex value, never a Tailwind `gray-*` or `neutral-*` class. If a needed color doesn't exist, say so instead of inventing one.
2. **Three surfaces.** Canvas behind the floating shell cards, surface inside them, white cards for blocks on top. Don't collapse them.
3. **One primary button per view.** The primary fill is for the single main action. Secondary actions use the outline or grey button.
4. **Hover is a solid shade.** Use the hover token, never an opacity of the primary.
5. **Flat by default.** Content boxes have a border and no shadow. Shadows mean elevation: shell cards, menus, popovers, dialogs, toasts.
6. **Status tags are pills.** 20px high, fully rounded, 12px semibold.
7. **Empty states always have an illustration.** No icon-only or text-only empty states. Use your design team's artwork from `assets/illustrations/`.
8. **Light mode and desktop only**, unless someone asks otherwise.

## How to produce a screen

**The deliverable is a downloadable image:** one HTML preview file with **Download PNG (1x)** and **Download PNG (2x)** buttons. Treat every visual request ("mock up", "design", "show me", "sketch") as a request for that file.

`$S` below is this skill's folder.

1. **Identify the page type** (list, table, settings, editor, dashboard, chat, public page). Most new screens are a variation of an existing type, so say which one you're starting from.
2. **Pick components.** Prefer an existing component over a new one. If nothing fits, propose the new component explicitly instead of quietly hand-rolling it.
3. **Write the screen HTML.** Copy `$S/assets/app-mockup-base.html` and fill it. It has every token as a CSS variable, Inter, lucide icons, the shell and base classes for common components. Use `var(--token)` for every color and write no hex outside `:root`. Use realistic content (survey names, response counts, teammates), never lorem ipsum. One screen per file, and one file per extra state (empty, loading, error).
   - **Full screen** (default): keep the shell. The frame is 1440 × 900.
   - **Export size is fixed:** every image is 1600px wide at 1x and 3200px at 2x, whatever is captured.
   - **A single element** (a modal, a card, a menu): build it inside the shell when context matters, otherwise place it alone on the surface background and crop with `--selector`.
4. **Render and check. This step is mandatory.**
   ```bash
   python3 "$S/scripts/render_screen.py" screen.html screen.png
   ```
   Options: `--width/--height` for another frame, `--selector ".dialog"` to crop to one element, `--full-page` for long pages without the fixed shell. Rendering is offline with the bundled Inter and lucide. The script reports ERRORs (off-token hex, raw `gray-*` classes, text under 10px) and WARNINGs (hex outside `:root`, missing illustrations). **Fix every ERROR, then look at the PNG** and judge it like a designer against the pre-flight checklist: alignment, spacing rhythm, one primary button, truncated text, empty gaps. Re-render until clean.
5. **Background (optional).** The preview has a **Background** picker: None (default) plus every `gradient-N.jpg` in `assets/backgrounds`. Choosing one places the screen on it with 64px padding, 16px rounded corners and a soft shadow, and both downloads include it. For a fixed canvas ratio (`1.91:1` for link previews, `16:9`, `1:1`, `4:5`), bake it in first:
   ```bash
   python3 "$S/scripts/add_background.py" in.png out.png --background gradient-3 --aspect 1.91:1
   ```
   Gradients are for presenting screens only. Never put them inside the app UI.
6. **Annotate (optional).** The preview has an **Annotate** toolbar: Arrow, Rectangle, Ellipse and Line, a Solid or Hand-drawn style, three colors, Undo and Clear. Marks are included in both downloads. When someone asks Claude to point at something ("add an arrow to the Export button"), draw it into the screen HTML instead, as an absolutely positioned SVG, so it's there when the preview opens.
7. **Build and deliver the preview.**
   ```bash
   python3 "$S/scripts/build_preview.py" screen.png screen-preview.html [--background gradient-N]
   ```
   Deliver the preview file. Add one or two sentences: which page type it's based on, and anything that isn't in the system yet (a new component, a missing illustration). Never paste the HTML in chat.

If Playwright isn't available, install it (`pip install playwright && playwright install chromium`). If that fails too, deliver the screen HTML file itself and say the PNG couldn't be rendered.

When describing a design in words instead of drawing it, name the actual components and tokens (`SectionHeader` with a primary button, `--surface` body) so developers can build it directly.

## Icons and copy

- Icons: lucide only, stroke 2. 16px by default, 20px in the main navigation rail. In mockups, write `<i data-lucide="name"></i>`.
- Buttons, titles, tabs and menu items use sentence case ("New survey", "Add widget"). Buttons start with a verb. Flag anything beyond basic labels for UX copy review.

## Pre-flight checklist

- [ ] No raw hex or Tailwind palette colors outside `references/tokens.md`
- [ ] Canvas, surface and card used in the right places
- [ ] At most one primary button visible
- [ ] Controls are 40px; 30px only for pills and compact tiles
- [ ] Status tags are 20px pills
- [ ] Shell cards float with a soft shadow; content boxes are flat with a border
- [ ] Tables sit directly on the surface, headers in ink
- [ ] Muted text only on white or the surface
- [ ] Empty states use an illustration
- [ ] No third-party overlays (chat launchers, feedback tabs)
- [ ] `render_screen.py` passes with no ERRORs, and the PNG was checked
- [ ] Delivered as the HTML preview with Download PNG buttons

## Files

| File | Use |
|---|---|
| `references/tokens.md` | Always, before choosing any color, size, radius, shadow or type style. The render script reads it to lint colors. |
| `assets/app-mockup-base.html` | Start of every screen mockup |
| `assets/illustrations/` | Your design team's empty-state artwork (ships empty) |
| `assets/backgrounds/` | Gradients for presenting screens |
| `scripts/render_screen.py` | Lint and render the PNG |
| `scripts/add_background.py` | Place a PNG on a background at a fixed ratio |
| `scripts/build_preview.py` | Wrap the PNG into the downloadable preview |
| `assets/preview-template.html`, `assets/vendor/` | Used by the scripts |
