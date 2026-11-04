---
name: tom-pmm-customer-quote-finder
description: Find a real, verbatim customer quote from the Customer Quotes library in Notion for Example Feedback (a fictional customer feedback platform), matched to a topic, persona, product area, or use case, and return it with full attribution. Use this skill whenever anyone on the team asks for a customer quote, testimonial, review, or customer story, including phrasings like "find me a quote about how easy the tool is", "do we have a testimonial from a researcher", "I need a customer quote about integrations for a landing page", "pull a Feedback Library quote", "grab a review that mentions ROI", or "any quotes from a Product persona". Also trigger when someone is drafting a deck, landing page, email, social post, ad, or sales asset and needs a customer voice to drop in. Always use this skill for surfacing customer quotes. Never recite or invent a quote from memory, because quotes must come from the live library and be reproduced word for word. When no strong match exists, this skill logs the gap in Linear so it can be sourced from a real customer.
---

# Customer Quote Finder

Help anyone on the team find a genuine customer quote for whatever they're working on: a landing page, deck, email, social post, sales call, ad. Every quote you return comes from the live Customer Quotes library in Notion and is reproduced exactly. When the library doesn't have what they need, you capture the gap in Linear so the library owner can go source it from a real customer.

The examples use Example Feedback, a fictional customer feedback platform. Replace the product areas, personas, IDs and links with your own.

## The one rule that matters most

**Never invent, alter, embellish, paraphrase, "clean up", or combine quotes.** Only ever surface quotes that actually exist in the library, reproduced word for word.

This isn't a stylistic preference. A fabricated or doctored customer quote can end up on a public landing page, in an ad, or in a sales deck, which is a serious trust and legal problem and misrepresents a real person. If you're tempted to tidy a quote's grammar or trim it to fit, don't do it silently. Show it as stored. The person can decide how to edit it for their own use; if they ask you to trim a long quote, keep the wording identical and mark any cut with an ellipsis so it's obvious it's an excerpt.

If you can't reach the library, say so and stop. Do **not** fall back on a quote you "remember." There is no acceptable substitute for the real data.

## The library

**Customer Quotes** lives in Notion, in the Product Marketing space. It updates constantly (new reviews and customer stories get added all the time), so **always pull the current list at the start of every request.** Never answer from a list you saw earlier in the conversation or from memory; a quote you're confident exists may have been edited or removed, and great new ones appear regularly.

- **Pull all rows** by querying this database view (it returns the whole table in one call at today's size):
  `<YOUR_NOTION_QUOTES_VIEW_URL>`
  If that query ever fails, fetch the database page to get a live view URL, or query the data source directly: `collection://<YOUR_NOTION_DATA_SOURCE_ID>`. If the response is paginated (`has_more: true`), keep fetching with the next cursor until you have every row. A missed page means a missed quote.
- **Human-facing page** (for pointing someone to browse it themselves): `<YOUR_NOTION_QUOTES_PAGE_URL>`

Each quote has these fields:

- **Quote:** the quote text itself. Reproduce this exactly.
- **Person who said it:** sometimes a named person with title and company (e.g. "Jordan Lee, Head of Research, Contoso"), sometimes an anonymized role (e.g. "Marketing Manager, IT Services"), sometimes a company name. Present whatever is stored; never invent a name, title, or company.
- **Persona:** one or more of Researcher, Product, CX, Marketing.
- **Product:** one or more of Feedback Library, AI, Survey, Customer Support, Dashboards, Ask AI, Integrations, Security.
- **Review or Customer Story:** whether it came from a review site or a full customer story.
- **Link if applicable:** a customer-story URL, review-site link (e.g. G2), or source doc. Often present, sometimes empty.

## Workflow

### 1. Pull the current list
Query the view above and load every quote. This is step one on every request, no exceptions.

If the Notion connector isn't available, follow "When you can't reach the library" below.

### 2. Understand what they actually need
Read their request for:
- **Theme:** what the quote should be *about* (ease of use, fast setup, integrations, ROI/revenue, customer support/CSM, AI, dashboards/reporting, switching from a competitor, research workflows, etc.).
- **Persona:** did they ask for a specific voice (a researcher, a PM, a marketer, a CX leader)?
- **Product area:** did they name a product (Feedback Library, integrations, surveys, dashboards)?
- **Type:** do they want a named customer story or is a review fine?
- **Where it's going:** landing page, deck, social, ad, sales, internal. You usually don't need to ask; infer it from the conversation. It matters for two reasons: it helps you judge fit (a named, linked customer-story quote is safest for anything public; anonymized reviews are better for internal or aggregate use), and you'll need it if you end up logging a gap in Linear.

Don't interrogate them. If the ask is clear enough to search, search. Only ask a clarifying question if the request is too vague to match on at all (e.g. just "get me a quote" with no theme).

### 3. Match and rank
Reason over the full list: read each quote's text *and* its fields. Judge relevance on what they asked:
- A **strong match** genuinely speaks to the theme and satisfies any explicit constraint they gave. If they asked for "a researcher's quote about Feedback Library," a strong match has Persona = Researcher, Product including Feedback Library, and text that's actually about the research/reporting experience, not just any researcher quote.
- Rank the alternates by how closely they fit. When quality is otherwise close, prefer named customer-story quotes and quotes that have a link, since they're more usable, but relevance to the theme always comes first.
- Trust the **text over the tags** if they ever disagree (the odd row is mistagged). Don't try to fix the database; just pick sensibly.

### 4. Present one strong match + up to three alternates
Use this shape. Reproduce each quote's wording exactly; a blockquote is fine for readability, but don't change the words, spelling, or punctuation.

```
**Best match**

> [quote, verbatim]

[Person who said it] · [Persona] · [Review or Customer Story]
[Link if present]

**Other options**

1. > [quote, verbatim]
   [person] · [persona]
   [link if present]

2. > [quote, verbatim]
   [person] · [persona]
   [link if present]

3. > [quote, verbatim]
   [person] · [persona]
   [link if present]
```

If only one or two quotes genuinely fit, show only those. Don't pad to four with weak matches: a padded list makes the person trust the strong match less and wastes their time. A quick line like "those are the only two that really fit the theme" is better than filler.

Keep any framing short. The quotes are the point.

### 5. When there's no strong match
Be straight about it. Say there's nothing in the library that's a strong fit for the theme, and show the one or two closest things if there's anything even loosely relevant, clearly labeled as "closest I found, but not a strong match."

Only if there's genuinely nothing worth showing, point them to the library to check for themselves: `<YOUR_NOTION_QUOTES_PAGE_URL>`, and note this is only worth doing because you already searched the whole thing and came up empty.

Then offer to log the gap in Linear (next step).

### 6. Log the gap in Linear
When there's no strong match, or the person says none of the options work, offer to record it in the **"Customer Quotes we didn't have"** project. This project is a permanent backlog: every issue is a real request for a quote we didn't have. Logging it is genuinely useful, so explain why in a sentence: it tells the library owner exactly which quotes are missing, so they can prioritize the right customers when they reach out for stories and reviews. The next person who needs this quote might actually have it.

**Draft the issue in chat first and create it only after they confirm.** Don't auto-file: the person may want to reword it, and unconfirmed issues clutter the backlog. Show them the title and description, get a yes, then create it.

If you don't already know where they were going to use the quote, ask once before drafting (it's the most useful part of the context for the library owner).

Create the issue with:
- **Team:** `<YOUR_LINEAR_TEAM>` (required).
- **Project:** `<YOUR_LINEAR_PROJECT_ID>` (name: "Customer Quotes we didn't have").
- **Assignee:** `<LIBRARY_OWNER_EMAIL>` (the person who owns the quote library, e.g. you@example.com).
- **Title:** short and specific: `Quote needed: [theme] [(persona/product if relevant)]`, e.g. `Quote needed: measurable ROI (Marketing persona)`.
- **Description:** in Markdown, covering:
  - **What they were looking for:** the theme and any persona / product / type constraints.
  - **Where it was going to be used:** landing page, deck, email, ad, sales, etc.
  - **Requested by:** the person, if known, and the date.
  - A pointer back to the library: `<YOUR_NOTION_QUOTES_PAGE_URL>`
  - A note that it was logged via the customer quote finder.

After creating it, give them the issue link and a one-line confirmation of what it'll help with.

## When you can't reach the library
If the Notion connector isn't connected, don't guess at quotes. Tell the person plainly that you couldn't reach the Customer Quotes library because the Notion connector isn't set up, and encourage them to connect it (Settings → Connectors) so you can pull real quotes. If they'd rather not connect it, point them at the library so they can search it themselves:
`<YOUR_NOTION_QUOTES_PAGE_URL>`

Same principle if Linear isn't connected and they want to log a gap: let them know, and either suggest connecting it or share the project link so they can add it manually:
`<YOUR_LINEAR_PROJECT_URL>`

## A few things to keep in mind
- The library is small enough today to read in full. Do that rather than relying on fuzzy search, so you never miss a good quote. If it ever grows to many hundreds of rows, switch to filtered or semantic queries scoped to the theme.
- Some quotes are long. It's fine to point out which sentence is the most relevant, but show the real wording and don't rewrite it.
- Some rows carry notes like "(APPROVED with Logo)" or "(name not given)" in the person field. That's internal context about usage rights. Surface it if it's relevant to how they'll use the quote (especially anything public-facing), but you don't need to make a fuss about it.
- If someone asks you to write a testimonial or make up a quote "in the style of" a customer, don't. Offer to find a real one instead. That's the whole point of this library.
