# tom-pmm-survey-design

A framework for keeping survey widget designs true to the real component library, whether Claude is mocking up a screen, building it in HTML or Figma, or reviewing someone else's design.

Originally built: November 2026

## What it does

1. Works out whether the request is about web or in-app surveys.
2. Builds every screen from one mental model: five stacked blocks, where only the answer area changes between question types.
3. Picks the question type, breakpoint and components, respects content limits, and only lets themes change themeable colors.
4. Uses real Figma component instances instead of drawn shapes.
5. Reviews designs in a fixed order and names the exact component or token to fix, grouped by severity.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

- Optional: the Figma connector, to build with your real components.

## Make it yours

The examples use Example Feedback, a fictional customer feedback platform. Fill in the placeholders (widget widths, type scale) and add the reference files listed at the end of `SKILL.md` with your own design system's values.
