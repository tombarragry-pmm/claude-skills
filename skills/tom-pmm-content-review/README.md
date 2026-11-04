# tom-pmm-content-review

Reviews any copy written about or for a company against one combined guide covering tone of voice, grammar, a product content framework, a style guide and AI-sounding language, then returns a fully revised version.

Originally built: November 2026

## What it does

1. Triggers whenever someone shares content about the company, on any channel, and always asks first whether to run the review.
2. Checks the content against the Collect → Analyze → Act framework, brand voice attributes and persona targeting.
3. Applies content type guidelines, technical accuracy checks, formatting rules and grammar and style rules.
4. Strips AI-style writing: banned phrases, word replacements and patterns to watch.
5. Returns specific review notes, then the full revised content in a code block, and saves the revised version as a Google Doc.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

- The Google Drive connector, to save the revised version as a Google Doc (the skill skips this step if the connector is unavailable).
- Optionally, a Feature & Capability Knowledge Base for your product, to verify technical claims against.

## Make it yours

The examples use Example Feedback, a fictional customer feedback platform, with fictional product areas (Research Projects, Ask AI), feature names, plan tiers and internal persona code names. Replace these with your own product name, product areas, plan tiers, personas, key integrations and retired names, and adjust the voice attributes and word lists to your style guide.
