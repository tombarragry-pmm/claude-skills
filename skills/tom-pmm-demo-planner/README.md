# tom-pmm-demo-planner

Plans solution-led interactive product demos (title, subtext and a short step table with callout labels), then logs each recorded demo to a Notion demo center and updates its Linear ticket.

Originally built: November 2026

## What it does

1. Checks that the product map (the list of every app screen) and the Notion connector are available.
2. Plans one demo at a time around a specific ICP's pain point, not a feature.
3. Proposes an opening card (title and one-line subtext) and a step table of at most 5 steps, using exact screen codes from the product map.
4. Writes and iterates callout labels against fixed length, tone and copy rules.
5. After recording, adds the demo link as a row in the Notion Demo Center table.
6. Updates the matching Linear issue with the link and moves it to In Review, then moves on to the next demo.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

- The Notion connector (for logging demos).
- The Linear connector (for updating demo tickets).
- A product map of your app's screens, available in the Claude project.
- An interactive demo tool (e.g. Arcade) for the recording itself.

## Make it yours

The examples use Example Feedback, a fictional customer feedback platform with fictional product areas (Surveys, Research Projects) and screens. Replace the screen list with your own product map, set `<YOUR_NOTION_DEMO_CENTER_PAGE_ID>`, `<YOUR_LINEAR_PROJECT_ID>` and `<TEAM_KEY>`, adjust the ICP list, and update the product naming and retired-feature rules.
