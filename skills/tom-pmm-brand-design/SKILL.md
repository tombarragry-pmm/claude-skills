---
name: tom-pmm-brand-design
description: Use this skill whenever creating any visual or graphic output for Example Feedback (a fictional customer feedback platform). Triggers include any request to create graphics, illustrations, diagrams, mockups, social images, presentation slides, email graphics, video scenes, SVGs, HTML visuals, or any other visual asset. Also trigger when someone asks for on-brand design work, wants to produce a visual in the brand style, or references brand colors, typography, or logo. This skill is tool-agnostic. Apply it whether the output is HTML, SVG, React, Remotion, a slide, or any other format.
---

# Brand Design Skill

The examples use Example Feedback, a fictional customer feedback platform, with a placeholder palette. Replace the colors, the logo rules and the product names with your own brand's.

## How to Use This Skill

When producing any visual output:
1. Read the color tokens and use exact hex values. Never approximate.
2. Apply the type rules appropriate to the output medium.
3. Follow the logo rules if the logo appears.
4. Follow the copy rules for any text on screen.
5. Apply the do and don't design principles before finalizing.

The values here should be taken directly from your design system file. Do not override them with guesses.

---

## Colors

### Primary: Accent

The main brand color is the accent. The designated primary is `#2F6FEB`.

| Role | Hex | Use |
|---|---|---|
| Accent | `#2F6FEB` | **Main brand color. CTAs, key accents, logo background** |
| Accent light | `#4A82EE` | Highlights, hover states, secondary accent moments |
| Accent lighter | `#6B9BF2` | Lighter accent, decorative use |
| Accent dark | `#1F5AD6` | Darker accent, pressed states |
| Accent very dark | `#13306F` | Dark scene backgrounds |
| Accent deepest | `#0C2050` | Subtle dark background variation |
| Accent tint | `#CFE0FB` | Light tint, subtle backgrounds |
| Accent tint light | `#E8F0FD` | Very light tint |
| Accent near-white | `#F3F7FE` | Near-white with an accent cast |

### Grayscale

| Role | Hex | Use |
|---|---|---|
| Ink | `#1A1A2E` | Primary text, near-black |
| Dark gray | `#44475A` | Dark body text |
| Mid gray | `#6B6E7B` | Secondary text, captions |
| Light gray | `#9B9DA8` | Placeholder, disabled |
| Border | `#D0D2DA` | Borders, dividers |
| Light border | `#E2E3E9` | Light borders |
| Tint | `#F1F2F5` | Subtle background tint |
| Canvas | `#F8F8FA` | Page and canvas background |
| White | `#FFFFFF` | White |

### Secondary: Teal

| Role | Hex | Use |
|---|---|---|
| Teal | `#5CCFC0` | Main teal. Use sparingly alongside the accent |
| Teal light | `#9EE3DA` | Light teal accent |
| Teal dark | `#46AFA2` | Darker teal |
| Teal tint | `#C9EFEA` | Very light teal tint |

### Semantic

| Purpose | Hex |
|---|---|
| Success | `#5DC98A` |
| Error | `#C8414F` |
| Warning | `#F0C04F` |
| Info | `#4A90D9` |

### Approved Color Combinations

**Dark scene (most common for marketing):**
- Background: `#1A1A2E` (ink) or `#13306F` (accent very dark)
- Headline text: `#FFFFFF`
- Accent: `#2F6FEB`
- Secondary accent: `#5CCFC0` (teal, use sparingly)

**Light scene:**
- Background: `#FFFFFF` or `#F8F8FA`
- Headline text: `#1A1A2E`
- Accent: `#2F6FEB`
- CTA button: `#2F6FEB` background, `#FFFFFF` text

**Accent scene:**
- Background: `#2F6FEB`
- Text: `#FFFFFF`
- Secondary text: `#CFE0FB` (accent tint)

**Never combine:**
- Accent text on a dark accent background (insufficient contrast)
- Teal as a primary color. It's always secondary to the accent.
- Mid gray text on white for headlines (low contrast)

---

## Typography

**Font family: Inter**, the only approved font.

Take the exact type scale (sizes, weights, line heights) from your design system. Scale up proportionally, roughly 2x, for large formats such as video, presentations and posters.

### Typography Rules

- Headlines: SemiBold (600) for most headings. Black (900) for display sizes only.
- Body copy: Regular (400) or Medium (500). Never Bold in body paragraphs.
- Letter spacing: 0 on all styles.
- All caps: avoid. No uppercase transform unless it's a badge or tag.
- Underline: only for links, never for emphasis. Use SemiBold for emphasis instead.

---

## Logo

### Variants

| Variant | When to use |
|---|---|
| Primary (icon + wordmark) | Default. Use in most contexts. |
| Icon only | Small sizes, square formats, app icons |
| Wordmark only | Rare. Only when the icon context is already established |

### Color Rules

| Background | Use |
|---|---|
| Dark, accent or colored | White logo variant |
| Light or white | Black logo variant |
| Never | A colored logo on a similarly colored background |

Always keep the aspect ratio, and give the logo a clear zone. Never stretch it.

---

## Design Principles

### Do

- Lead with bold, large typography. The visual language is type-forward.
- Use dark backgrounds for hero moments. Light backgrounds for functional and UI contexts.
- Use white space generously. Don't crowd content.
- The accent is the primary color. Use it decisively for the one key element per scene.
- Teal (`#5CCFC0`) can support the accent but should never compete with it.
- Rounded corners on cards and buttons.
- Stagger or sequence content. Don't show everything at once in animated contexts.

### Don't

- Never use a color from a previous brand identity. List any retired brand colors here so nobody brings them back.
- Never use gradients unless explicitly directed.
- Never use multiple accent colors in the same composition. Pick one per scene.
- Never use decorative fonts or change from Inter.
- Never place the logo on a busy background without a clear zone.
- Never use drop shadows on text.
- Avoid thin font weights (100, 200, 300). They don't read well at scale.

---

## Copy Rules (for on-screen text)

- No em dashes or en dashes. Use a period or colon instead.
- US English spelling.
- Short sentences, ideally under 8 words per line in large-format contexts.
- Active voice and contractions are fine.
- Lead with pain or outcome, not feature name.
- Avoid: "powerful", "seamless", "next-gen", "best-in-class", "focused".
- Products: Surveys (Survey Software) and Feedback Library (Research Repository).
- Never use retired product names. Keep your list of them here.

---

## Design System Source

Point this section at your own design system file, with the page or node for each area (colors, typography in light and dark mode, logo, buttons). If you need to verify or extend any token, open those pages with the Figma connector.
