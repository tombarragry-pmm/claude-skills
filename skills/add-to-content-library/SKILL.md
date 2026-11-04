---
name: add-to-content-library
description: 'Add a new article, benchmark report, competitor page, guide, product news post or interactive demo to the Content Enablement Library for Example Feedback (a fictional customer feedback platform), the persona-tabbed Google Sheet that sales and CX use to find content for outbound and follow-ups. Use this skill whenever anyone on the team wants to add, log, register or update a piece of content in "the library", "the enablement library", "the enablement sheet", "the content library" or "the sales enablement sheet", or shares a link to a published company page and asks to get it in front of sales or CX, even if they don''t name the sheet. Always use it for that job: it asks for the link and context first, checks for duplicates, enforces the row format and placement rules, writes the rows to the sheet after approval, and ends with the handoff reminders. Do not use it to write new marketing content, changelogs or customer quotes.'
---

# Add to the Content Enablement Library

The library is a Google Sheet where the sales and CX teams look up a piece of content to use in outbound or a follow-up. It works because every row is short enough to scan in five seconds and is written for one persona. Your job is to keep it that way while adding the new piece.

The examples use Example Feedback, a fictional customer feedback platform, and fictional competitors (Contoso Surveys, Fabrikam Research, Northwind Insights). Replace them with your own.

Sheet: `<YOUR_SPREADSHEET_URL>` (spreadsheetId `<YOUR_SPREADSHEET_ID>`)

Owner: the library owner in Product Marketing. Content decisions about swaps and overlap: the content reviewers (for example the library owner plus Jordan Lee and Sam Rivera; replace with your own reviewers).

## How the sheet is built

Four tabs, one per persona. The persona is the tab, so there is no persona column.

| Tab | Who the rows are written for |
|---|---|
| Product | Product Manager, Product Owner, Product Designer |
| Research | User Researcher, Customer Insights Manager, Research Lead |
| Marketing | Product Marketing Manager, Growth Marketer, CRM Manager |
| CX | CX Manager (Customer Success is bundled in here), Support Lead |

Seven columns, A to G, same on every tab:

| Column | What goes in it |
|---|---|
| Topic | Plain-language name of the piece, hyperlinked to it. "Top 3 Northwind Insights alternatives", "NPS benchmarks by industry", "Fabrikam Research pricing". Not the H1, not the meta title. Landing pages get "(landing page)" after the name. |
| Actual URL | The final link as plain text, exactly as fetched. This column exists because the Topic hyperlink didn't always render for the team, so every row carries the URL in the open. Never leave it blank. |
| Type | One of exactly: `Benchmark`, `Competitor`, `Guide`, `Product news`, `Interactive demo` |
| Lead with | The one stat or line a rep opens with. One sentence, no period needed. |
| Biggest takeaways | Three numbered lines in one cell, separated by line breaks. One number per line where the piece has numbers. Each line under 15 words. |
| Sales angle | One or two sentences: how to use the piece with a prospect. |
| CS angle | One or two sentences: how to use the piece with an existing customer. "CS" here means your own success team, not the persona. |

Rows inside a tab are grouped by Type in this order: Benchmark, Competitor, Guide, Product news, Interactive demo. A new row goes at the end of its type block, not at the bottom of the tab.

Read `references/row-examples.md` before drafting. It shows example rows, one per type, and the before/after that explains why the format is strict.

## The workflow

Follow these steps in order. Each one that says "wait" means the turn ends there; do not run ahead.

### Step 0. Ask before doing anything

Before fetching, reading the sheet or drafting, ask the person in one plain-text message (no buttons, no tool-rendered option lists) for three things:

1. What they are adding, in a sentence. Article, benchmark report, competitor page, guide, product news, or interactive demo.
2. The final link. The published URL, not a draft doc. For an interactive demo, the demo link.
3. Any FYIs. Who it's for, what it should be used for, claims to avoid, a persona it should or shouldn't reach, anything the content reviewers already said about it.

If they gave some of this already in the message that triggered the skill, don't ask for it again. Ask only for what's missing, then wait.

### Step 1. Check you can write to the sheet

This skill writes rows to the sheet itself. You need the Google Sheets connector (tools for reading values, updating values, inserting rows). If they aren't in your tool list, stop and say so in one or two sentences: the person needs to connect the Google Sheets connector in this chat, then you'll continue. Don't offer to produce copy-paste rows as a substitute unless they ask; the whole point is that the sheet stays the single source.

If a Google Workspace skill is available to you, read its Sheets reference before your first write. Sheets tools parse input like the UI, so a value that looks like a number or date can change type; everything in this sheet is text or a `HYPERLINK` formula.

### Step 2. Read the source, don't remember it

Fetch the final link and read the whole piece. Every number, date, price and claim in the row must come from the page as it is today. The content team's own summaries are a useful starting point, but the page wins when they differ.

For an interactive demo: approved demos come only from the "Demo Center" table on your Notion page of approved demos (page id `<YOUR_NOTION_APPROVED_DEMOS_PAGE_ID>`). Use its step-by-step breakdown section for each demo as the source for the three takeaways. If the demo isn't on that page, say so and stop; it isn't approved for the library yet.

### Step 3. Check for overlap before you write a word

The library gets bloated fast, and two rows that make the same argument are worse than one. Read columns A to D (Topic, Actual URL, Type, Lead with) of all four tabs with one read per tab (for example `Product!A:D`). Then compare the new piece against what's there on four things:

- Same URL already in column B of any tab (compare without trailing slashes or tracking parameters)
- Same subject: same competitor, same metric, same benchmark report family, same feature
- Same argument: a Lead with line that makes the same point the new piece would make
- Same job: a row a rep would reach for in the same situation (for example two "Fabrikam Research is expensive" pieces)

If you find any of these, flag it to the person before drafting, in plain text:

> Overlap check: this looks close to [existing Topic] on the [tab] tab, which already argues [its Lead with]. The library is meant to stay short, so this is worth raising with the content reviewers: swap the old row for this one, keep both with different jobs, or skip. Which way do you want to go for now?

Then wait. Never delete or overwrite an existing row on your own; a swap is a decision for the content reviewers. If the person says continue, continue, and repeat the flag in your closing summary so it gets passed on.

If nothing overlaps, say so in one line and move on.

### Step 4. Pick the tabs

One tab by default. Be picky. Ask "which persona would actually send this?" and put it there. A piece earns a second tab only when the argument is different for that persona, not just relevant to them.

All four tabs are reserved for platform-wide pieces: the platform overview demo, the AI assistant connector demo, and platform-level product news. Everything else lives in one or two tabs.

Say which tab(s) you're proposing and why, in one line each, before you draft. If the person's FYIs already named the tab, use it.

### Step 5. Draft the rows in chat

One block per tab, written for that persona. When a piece goes in two tabs, rewrite the takeaways and angles for each; don't copy the row across.

Show each row as labeled lines, like this:

```
Tab: CX
Topic: Fabrikam Research pricing
Actual URL: https://example.com/blog/fabrikam-research-pricing/
Type: Competitor
Lead with: Quote-only enterprise contracts vs published monthly pricing
Biggest takeaways:
1. Fabrikam Research is quote-only, with renewal uplifts and overage fees.
2. The premium buys advanced statistical modules most CX programs never run.
3. Example Feedback publishes its pricing, starting at $XX/month.
Sales angle: Ask one question: do you actually use the advanced statistics modules? If not, they're paying for rigor they don't touch.
CS angle: Customers eyeing Fabrikam Research: remind them of seats, services, overages and the dedicated admin it needs.
```

Rules for the content of a row. These exist because the first version of this library was unusable: 60-word takeaways stuffed with six numbers each.

- Three takeaways, each under 15 words, one number per line where the piece has numbers. If you can't say it in 15 words, you've picked the wrong fact.
- Lead with is the single thing a rep says first. If the piece is a benchmark, it's the headline number. If it's a competitor page, it's the contrast.
- Sales angle and CS angle always argue for picking Example Feedback. They never point a rep toward a competitor, lead with an Example Feedback gap, or tell the rep to qualify out. Honest competitor facts and our own gaps belong in Biggest takeaways only, where reps need them to stay credible.
- Facts only from the page you fetched. No numbers from memory, no invented customer quotes, no claims about plans, limits or certifications you didn't see on the page.
- US English. No em dashes or en dashes anywhere; use a comma, colon, period or hyphen. No "best-in-class", "powerful", "robust", "next-gen", "seamless". Contractions are fine.
- Product names: use the current official names (in the examples: "Research Projects" for the research product area and "Example Feedback Connector" for the AI assistant connector), never retired or internal names. Real job titles, never internal persona code names.
- Interactive demo rows: Lead with describes what the walkthrough proves; Sales angle says who to send it to and when; CS angle says which customers to send it to and what it nudges them toward.

End the draft with: "Approve as-is, or tell me what to change." Then wait. Iterate in chat until they approve. If they want to go element by element (Lead with first, then takeaways, then angles), do that.

### Step 6. Write to the sheet

Only after approval.

1. Read the target tab's columns A to G in full (for example `CX!A:G`) to find where the Type block ends. Rows are grouped Benchmark, Competitor, Guide, Product news, Interactive demo. The new row goes directly after the last row of its type. If a tab has no row of that type yet, place it where the block would sit in that order.
2. Insert one row at that position with the insert-rows tool, inheriting formatting from the row above, so wrapping, font and banding carry over.
3. Write the seven cells with the update-values tool as a single row: Topic as `=HYPERLINK("<url>","<Topic text>")`, Actual URL as the plain URL string (the same one used in the formula), the rest as plain text. Keep the three takeaways in one cell with real line breaks between them.
4. Read the row back and check it landed in the right block with the right values. A write the tool accepted is not the same as a correct row.
5. Repeat for each approved tab.

Never reorder, edit or delete existing rows. If something existing looks wrong, say so in the closing summary instead.

### Step 7. Close out

Finish with a short summary, plain text:

- What was added, which tab(s), and the row position.
- Any overlap flagged in Step 3, restated so it can be passed to the content reviewers.
- This reminder, every time, in roughly these words: "Last thing: tell the library owner about this addition so any tools that read the library (for example an internal sales assistant) get updated with it."

No long recap of the process. The person can open the sheet.

## Things that go wrong

- **Skipping Step 0.** The link in the trigger message is often a draft doc or a Notion page, not the final URL. Ask.
- **Writing from the content team's summary instead of the page.** Their takeaways are detailed and sometimes stale. Fetch the live page.
- **Putting a piece in every tab because it's "relevant to everyone".** That's how the library bloats. One tab unless the argument changes per persona.
- **Angles that hedge.** "Be upfront that we lack X" is a takeaway, not an angle. Angles argue for Example Feedback.
- **Appending at the bottom of the tab.** Rows live in type blocks. Insert inside the block.
- **Resolving an overlap yourself.** Flag it, ask, and never delete.
- **Leaving Actual URL empty because the Topic is already linked.** Both are filled, every row. The URL column is what the enablement picker skill and other downstream tools read.
