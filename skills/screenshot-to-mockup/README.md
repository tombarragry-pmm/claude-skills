# screenshot-to-mockup

Turns a raw product screenshot into a clean, marketing-ready UI mockup PNG. The focal UI element stays sharp and real, and everything around it becomes soft gray "ghost" placeholders.

Originally built: November 2026

## What it does

1. Analyzes the screenshot and proposes what to keep sharp, what to ghost, the frame and the canvas size.
2. Waits for your confirmation.
3. Rebuilds the mockup as a single self-contained HTML file.
4. Exports it as a PNG with `wkhtmltoimage`, then iterates on your feedback.

## Files

- `SKILL.md`: the instructions Claude follows.
- `output.html`: an example mockup built with the skill, using a fictional product and placeholder colors.

## Requirements

- [wkhtmltoimage](https://wkhtmltopdf.org/) for the PNG export.

## Make it yours

Replace the placeholder colors in the "Brand Colors" table in `SKILL.md` with your own palette.
