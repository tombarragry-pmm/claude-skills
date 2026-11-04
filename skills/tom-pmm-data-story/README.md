# tom-pmm-data-story

Builds a "data story": a customer-story-style piece about one feature or integration, written from aggregated product usage data in Hex instead of a named customer, with vertical breakdowns and numbers that prove the workflow runs at scale.

Originally built: November 2026

## What it does

1. Locks the topic (one feature or integration) and checks in the help center that the workflow is real.
2. Runs a Hex Thread with fixed cohort, window and vertical definitions to get the hero total, breakdowns, dimensions and concentration.
3. Picks the hero stat, supporting stats and vertical callouts, and records every number considered and cut.
4. Chooses the lead persona and use cases from the topic.
5. Drafts the story in chat from a fixed template (internal notes plus the public story), then creates a Google Doc or Claude Doc and replies with the key numbers and open items.

## Files

- `SKILL.md`: the instructions Claude follows.
- `references/hex-thread-prompts.md`: the main Hex Thread prompt and follow-ups, with fixed definitions.
- `references/doc-template.md`: the doc structure (internal notes block plus the story).
- `references/vertical-map.md`: how warehouse industry labels map to published cohort labels.
- `references/example-story.md`: a fully fictional finished data story to match the shape of.

## Requirements

- Hex connector (Hex Threads) on top of your product data warehouse.
- Google Drive connector or Claude Docs, for the draft doc.
- Optional: Notion connector plus the `tom-pmm-customer-quote-finder` skill for quotes, and a product analytics connector (e.g. Mixpanel) for UI adoption questions.

## Make it yours

The examples use Example Feedback, a fictional customer feedback platform, and a fictional help desk tool, Fabrikam Desk. Replace the product and product area names, the help center and signup URLs, the `<companies_table>` and column placeholders with your own warehouse names, the vertical labels with the ones your enrichment produces, and the persona and use case sources with your own ICP references.
