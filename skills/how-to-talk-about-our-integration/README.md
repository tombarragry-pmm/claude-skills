# how-to-talk-about-our-integration

Checks customer-facing copy and campaign ideas against a live feature brief before anything about a fast-moving launch (here, an MCP integration) gets written. It flags unverified claims and off-brief framing instead of quietly fixing them.

Originally built: November 2026

## What it does

1. Decides whether the work is customer-facing. Internal product or research work is left alone.
2. Offers to check against the brief, once per conversation, as a button choice.
3. Fetches the live brief from Notion, or stops if it can't.
4. Answers a fixed set of questions from the brief: clearance, positioning, differentiation, limits and audience.
5. Flags every conflict between the request and the brief, then writes using the brief's own language.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

- The Notion connector, or an exported copy of the brief.

## Make it yours

Replace Example Feedback, the fictional launch names ("Assistant Layer", "Feedback Agent") and the brief URL and page ID placeholders with your own.
