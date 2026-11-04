# add-to-content-library

Adds a new content piece (article, benchmark, competitor page, guide, product news or interactive demo) to a persona-tabbed Google Sheet library that sales and CX use, with duplicate checks, strict row formatting and correct placement.

Originally built: November 2026

## What it does

1. Asks for what is being added, the final published link and any FYIs before touching anything.
2. Confirms the Google Sheets connector is available for writing.
3. Fetches and reads the live page (or, for demos, the approved demo list in Notion) so every fact comes from the source.
4. Checks all tabs for overlap by URL, subject, argument and job, and flags any overlap for the content reviewers to decide.
5. Proposes which persona tab(s) the piece belongs on.
6. Drafts one row per tab in chat (lead with, three short takeaways, sales angle, CS angle) and waits for approval.
7. Inserts each approved row at the end of its type block, writes the cells and reads them back to verify.
8. Closes with a short summary, any overlap flags and a handoff reminder.

## Files

- `SKILL.md`: the instructions Claude follows.
- `references/row-examples.md`: one fictional example row per content type, plus a before/after showing why the format is strict.

## Requirements

- The Google Sheets connector, with write access to the library spreadsheet.
- A way to fetch web pages, to read the published piece.
- The Notion connector, if you add interactive demos from a Notion list of approved demos.

## Make it yours

The examples use Example Feedback, a fictional customer feedback platform, and fictional competitors. Replace `<YOUR_SPREADSHEET_URL>`, `<YOUR_SPREADSHEET_ID>` and `<YOUR_NOTION_APPROVED_DEMOS_PAGE_ID>` with your own, set the library owner and content reviewers, adjust the persona tabs and job titles, and update the product naming rules and handoff reminder to match your team.
