# feature-brief-skill

Walks a product manager or product marketer through writing a feature brief, section by section, entirely in chat. The brief only goes to Notion once it's finished and confirmed.

Originally built: November 2026

## What it does

1. Checks the person is in the Claude project that holds your company context.
2. Asks whether they're a PM or a PMM, and splits the work accordingly: PMs own product truth, PMMs own positioning.
3. Checks for an existing brief before starting a new one.
4. Places the feature in the product architecture, then drafts every section of a fixed template in chat, with an approval at each step.
5. Pushes the finished brief to Notion in one pass.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

- The Notion connector.
- Web search, for verifying competitive claims.

## Make it yours

Replace Example Feedback, the product architecture table, the messaging framework pillars, the Claude project name, the Notion page URLs and IDs, and the banned-terms list with your own.
