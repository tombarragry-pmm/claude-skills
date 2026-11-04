# create-cms-feature-page

Takes a feature brief and a page template exported from a visual CMS (e.g. Builder.io), writes the copy section by section with you, then fills the template and hands back a page JSON that imports cleanly. A bundled script swaps only copy, never shared blocks, IDs or images, and checks for dashes.

Originally built: November 2026

## What it does

1. Reads the feature brief (fetching it from Notion if needed), then parses the uploaded template and maps it to the canonical 13-block page structure.
2. Sets the strategy: primary and secondary personas, and 2 to 3 hero angles to choose from.
3. Works each section in order (hero, opening grid, two showcases with their cards, how-it-works carousel, testimonial, FAQ), offering short options against per-slot character budgets and locking each before moving on.
4. Assembles the file with the bundled Python script: fills copy by component role, fixes button links, drafts SEO metadata, and validates that shared blocks are untouched, there are no dashes and the JSON is valid.
5. Hands over the end-state flags: images to swap, plan availability to confirm, SEO and slug drafts, a real testimonial quote, and any disputed facts.

## Files

- `SKILL.md`: the instructions Claude follows, including the component schema, character budgets, copy rules and the assembly script.

## Requirements

- Python 3 (standard library only) to run the assembly script.
- Optional: the Notion connector, if feature briefs live in Notion.
- Claude.ai tools `ask_user_input_v0` and `present_files` are referenced; in other environments, ask questions in chat and save the file to an outputs folder.

## Make it yours

The examples use Example Feedback, a fictional customer feedback platform, and its fictional product Feedback Lab.

1. Replace the component names and the 13-block table with the components your CMS templates actually use.
2. Set `SIGNUP`, `DEMO`, `BRAND_NAME` and `BRAND_URL` in the script.
3. Recalibrate the character budgets against your own live pages.
4. Fill in your retired product and feature names, internal persona codenames to avoid, and the integrations you lead with.
