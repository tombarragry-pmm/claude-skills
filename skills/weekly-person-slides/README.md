# weekly-person-slides

Pulls one team member's tasks from Linear and turns them into two branded weekly meeting slides (.pptx): "Done this week" and "Next week".

Originally built: November 2026

## What it does

1. Identifies the team member and maps them to their Linear assignee value.
2. Works out the week range (current Monday to Friday, or the dates you give).
3. Pulls their Linear issues and filters them with strict rules: only Done items count as done, blocked items get their own section, and next week is limited to in-progress or due-soon work, curated to 3 to 5 bullets each.
4. Fills a Node.js (pptxgenjs) generator with the data and builds the two slides, with screenshot placeholders and an FYI panel.
5. Hands you the .pptx file and offers to run it for someone else.

## Files

- `SKILL.md`: the instructions Claude follows, including the single-person generator template.
- `generator-template.js`: a full-team version that builds a cover slide, two slides per person and a closing slide (filled with fictional example data).
- `assets/icon-black.svg`: placeholder for your small brand icon (bottom-right of each slide).
- `assets/logo-black.svg`: placeholder for your wordmark logo (cover and closing slides).
- `assets/cover-bg.svg`: placeholder background for the cover and closing slides.

## Requirements

- The Linear connector (MCP).
- A code execution environment with Node.js and npm, to install `pptxgenjs` and `lucide-static`.
- The Inter font installed where the slides are opened (or change `fontFace`).

## Make it yours

The examples use Example Feedback, a fictional company, and fictional team members. Replace the team table in `SKILL.md` (names, Linear assignee values, and who counts In Review as done), the `TEAM` data in `generator-template.js`, the placeholder color palette at the top of both generators, the three SVGs in `assets/` with your own icon, logo and cover background, and the "Example Feedback Marketing Team" label on the cover.
