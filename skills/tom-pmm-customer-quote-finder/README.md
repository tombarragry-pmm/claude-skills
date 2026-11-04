# tom-pmm-customer-quote-finder

Finds a real, verbatim customer quote in a Notion quote library that matches a theme, persona or product area, and logs a Linear issue when the library has nothing that fits.

Originally built: November 2026

## What it does

1. Pulls the full, current Customer Quotes database from Notion on every request.
2. Reads the request for theme, persona, product area, quote type and where the quote will be used.
3. Matches and ranks quotes against the request, trusting quote text over tags.
4. Returns one best match plus up to three alternates, word for word, with attribution and links.
5. When nothing fits, says so plainly and offers to log the gap in a Linear backlog project, drafting the issue in chat for approval first.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

- The Notion connector, with access to your quote library database.
- The Linear connector, for logging quote gaps (optional).

## Make it yours

The examples use Example Feedback, a fictional customer feedback platform. Replace the Notion view URL, data source ID and page URL, the Linear team, project ID, project URL and assignee, and the Persona and Product field values with the ones in your own library.
