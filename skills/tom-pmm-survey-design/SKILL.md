---
name: tom-pmm-survey-design
description: Source of truth for how the Example Feedback survey widget (Example Feedback is a fictional customer feedback platform) is designed, covering Web Surveys (websites, web apps and link surveys) and In-App Surveys (native iOS and Android apps). ALWAYS use this skill, without asking, whenever anyone designs, mocks up, recreates, codes or reviews a survey screen or survey UI element, for example "mock up an NPS survey", "single choice with a follow-up", "build the thank-you screen in HTML", "is this survey screen correct?", "design a new question type", "in-app survey in landscape". Also use for survey microcopy that must fit the widget, widget sizes, mobile layouts, or survey themes. When a marketing visual contains a survey widget, use this for the widget and the brand visuals skill for the rest.
---

# Survey widget design system

This skill describes how a survey widget is put together, so that anything you design, build or review looks like it came out of the real component library rather than a generic form. The examples use Example Feedback, a fictional customer feedback platform. Fill in the placeholders (in angle brackets) with values from your own design system. Your Figma file is the truth: if it's reachable and something here looks outdated, check the file.

## Two products, one system

| Product | What it is |
|---|---|
| **Web Surveys** | Surveys on websites and web apps, plus link surveys. A bottom sheet on mobile web, and a floating card on desktop |
| **In-App Surveys** | Surveys inside native mobile apps, shown as a dialog or full screen, in portrait or landscape |

The two usually share components, question types, spacing, radius, type and themes, with a few differences. Work out which product the request is about first. If it mentions an app, SDK, in-app, iOS or Android, full screen or landscape, it's In-App Surveys. If it mentions a website, web, desktop, link survey or a widget width, it's Web Surveys. If it's unclear and the answer would differ, ask.

## The mental model

Every survey screen is one **widget** made of up to five stacked blocks, always in this order:

```
┌─ header ───────────── logo · progress bar · minimize / close ─┐
├─ [image block]  (optional, above OR below the text block)     │
├─ text block ───────── introduction (small) + question (bold)  │
├─ answer area ──────── "selection information" label + answers │
│                        + description labels (scales only)     │
├─ [disclaimer]  (optional, divider + legal text [+ checkbox])  │
└─ navigation ───────── divider · CTA(s) · branding             ┘
```

Only the answer area changes between question types. The header, text block, disclaimer and navigation are shared chrome. Get the chrome right and pick the correct answer component, and the screen will look right.

The widget sits on the host page. On mobile it's a bottom sheet over a dimmer. On desktop it's a floating card in a corner, or centered for larger sizes.

## How to work

1. **Identify the question type.** Pick the matching widget variant as your starting skeleton: for example NPS, single choice, multiple choice, text answer, contact form, date picker, dropdown, smiley scale, rating, matrix, welcome message, follow-up question, or thank-you screen.
2. **Pick the breakpoint or mode.** Mobile (375px wide, with fixed side padding), tablet, or one of the desktop widget sizes: `<YOUR_WIDGET_WIDTHS>`. For In-App Surveys, pick the presentation mode.
3. **Compose from components**, using your design tokens and component anatomy. Use the exact component, variant and state names when you describe or annotate a design, for example `survey button / Variant=single choice answer, State=active`, so developers and designers can find the component.
4. **Respect content limits**, such as the maximum introduction length and question length per widget size. If copy is too long, flag it or pick a bigger size. Don't squeeze the type.
5. **If the survey is themed**, swap only the themeable colors. Structure, spacing, radius and type never change with a theme.

When building in Figma with the Figma connector, **use instances of the real components** instead of drawing new shapes. Set component properties and variants rather than detaching.

When building in HTML, CSS or React, mirror the component names in class names (for example `.survey-button--active`), use the tokens as CSS variables, and use the system font.

## Non-negotiables (the things that make it look "right")

Write your own values into each line. These are the categories that most often go wrong:

- **One typeface, fixed sizes per breakpoint.** Introduction, question, answers and labels each have one size and weight on mobile and one on web: `<YOUR_TYPE_SCALE>`. A selected answer switches its label to a heavier weight.
- **One spacing grid.** Spacing only comes from the spacing scale (for example an 8px grid), with fixed values between answers, between an icon and its label, and around sections.
- **One radius for interactive elements:** answer buttons, inputs, text areas, CTAs and slots share it. The widget card has its own corner radius, and the progress bar is fully rounded.
- **How answer states work.** For example: answers are tinted, not outlined, and the selected state adds a border while the fill stays the same. Error adds a red tint and a red border.
- **The primary CTA.** Its width on mobile, height, color, label style, and its hover, pressed, disabled and focus states.
- **The "selection information" label** ("Select one", "Answer required"): its style and its distance above the answer list.
- **The widget shadow.**
- **Which questions auto-advance.** For example, single-select questions (NPS, single choice) move on when an answer is chosen and have no Next button, while questions that need confirmation (multiple choice, text, contact form, dropdown) keep the CTA. Old design frames often contradict this, so don't copy them.
- **Minimum tap targets** for answers, CTAs and scale items on mobile.

## Reviewing a design against the system

When asked "is this right?" or to audit a survey screen, check in this order, and report findings grouped by severity (breaks the system, then inconsistent, then nitpick):

1. Block order and presence (header, [image], text block, answers, [disclaimer], navigation)
2. Correct component and variant for the question type
3. States: does the selected answer show its selected style? Is there exactly one active CTA?
4. Tokens: colors and spacing on the scale, the right radius, the right type sizes and weights for the breakpoint
5. Content limits and truncation behavior
6. Theme applied only to themeable slots

Name the exact component or token that should be used instead, for example "gap is 10px, should be `spacing-8`". A vague "spacing looks off" isn't enough.

## Make it yours: reference files to add

Keep the details in reference files next to this one, and read only what the task needs:

| File | What it holds |
|---|---|
| `references/tokens.md` | Colors, spacing, radius, type scale, layer states |
| `references/components.md` | Anatomy, padding, states and properties for each component |
| `references/question-types.md` | How a full screen is composed for each question type |
| `references/layout-and-sizing.md` | Breakpoints, widget sizes, positions, character limits, scroll behavior |
| `references/in-app-surveys.md` | Presentation modes and anything that differs in the native app version |
| `references/themes.md` | Theme palette and which slots are themeable |
| `references/figma-map.md` | File keys, page map and component node IDs, plus known quirks not to copy |
