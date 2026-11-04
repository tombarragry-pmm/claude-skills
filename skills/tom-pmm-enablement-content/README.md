# tom-pmm-enablement-content

Picks the single best piece of marketing content for a sales rep or CSM to send, pulled live from a curated, persona-tabbed Google Sheet library, and hands it over as a ready-to-paste card.

Originally built: November 2026

## What it does

1. Reads every tab of the Content Enablement Library sheet through the Google Sheets connector (and refuses to work from memory if the connector is missing).
2. Works out whether the asker is in sales or CS, who the content is going to (the persona tab), and what the job is (topic, competitor, objection or moment).
3. Chooses one piece, including the right call between a landing page, an article and an interactive demo.
4. Presents it as one card: linked topic, lead-with hook, three verbatim takeaways and the matching sales or CS angle.
5. Handles re-rolls and, on request, drafts a short send in the rep's own voice.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

- The Google Sheets connector, with read access to your library spreadsheet.
- A library sheet with one tab per persona and seven columns: Topic, Actual URL, Type, Lead with, Biggest takeaways, Sales angle, CS angle. The companion `add-to-content-library` skill maintains it.

## Make it yours

The examples use Example Feedback, a fictional customer feedback platform, and fictional competitors (Contoso Surveys, Fabrikam Research). Replace `<YOUR_SPREADSHEET_ID>` with your sheet's ID, rename the persona tabs if yours differ, and swap in your own product area names and competitors in the trigger examples.
