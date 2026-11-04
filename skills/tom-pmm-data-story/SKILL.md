---
name: tom-pmm-data-story
description: Build a "data story" for Example Feedback (a fictional customer feedback platform), a case-study-style piece written from aggregated product usage data in Hex instead of a named customer. No quotes as the subject, no logos, no single customer. One story per feature or integration, with vertical breakdowns ("marketplace apps", "retail and loyalty apps") and numbers that prove the thing is possible at scale. Output is a Google Doc (or Claude Doc) draft for the customer stories hub. Use this skill whenever anyone on the marketing team asks to create, draft, research, scaffold or "pull the numbers for" a data story, a usage story, a by-the-numbers story, a proof-at-scale piece, a feature or integration story with no customer attached, or asks "what do marketplaces / retail apps / fintechs actually do with [feature]" for marketing. Trigger even on casual phrasing like "data story for our help desk integration", "let's do one for the SDK", "can we show scale on the marketing automation integration", or "backup for the [customer] case study". Always use this skill for data stories; never freestyle one from memory or from a single Hex question.
---

# Data story

A data story is proof backed by our data, not by a customer. It takes one feature or integration, pulls the real usage totals from the warehouse via Hex, groups them by vertical, and inspires readers in those verticals to do the same thing. It looks like a customer story (same hub, same narrative arc as your strongest customer story) without a protagonist or a logo. Customer quotes are allowed as social proof when they come from the Notion quote library via the `tom-pmm-customer-quote-finder` skill, never as the subject of the piece.

The examples use Example Feedback, a fictional customer feedback platform, and a fictional help desk tool called Fabrikam Desk. Replace them with your own product, partners and data model.

The format to aspire to is `references/example-story.md` (a fully fictional example). Read it before drafting any data story and match its shape.

Two jobs for the numbers: show it's possible, and show it works at the scale a B2C reader needs. They do not have to show business outcomes. "1,264,530 tickets synced from Fabrikam Desk" is a result here.

Take it in order. Lock the topic, verify the workflow is real, research in Hex, pick the numbers, write, then create the doc. Draft and iterate in chat before touching Drive.

## Inputs

The topic is required: one feature or integration ("help desk integration", "mobile SDK", "AI follow-up questions", "marketing automation integration", "Feedback Library continuous projects"). If it's missing or it's a vertical or a persona instead of a feature, ask for the feature before anything else. Verticals are breakdowns inside a story, never the subject.

Optional, with defaults if not given:
- Data window: last 12 full months
- Lead persona: inferred from the topic (see "Persona and use cases")
- Verticals to prioritize: B2C first, see the vertical map

## The rules (locked, do not relitigate)

1. One story, one feature or integration. Verticals are breakdowns inside it.
2. The subject is always a plural cohort. Never a customer, named or describable. n doesn't matter; one account can carry a vertical and the copy still says "B2C software and apps". Vertical blocks are judged by the volume of the end product (responses, tickets), not by how many accounts sit behind them.
3. Every number traces to a Hex thread. Save the thread link in the doc. Never present a guessed or remembered number.
4. Inferred workflows are fine, invented ones aren't. Describe what the usage data shows ("marketplace apps route negative CSAT responses into the help desk as tickets") and only describe workflows the product supports today, confirmed in your help center.
5. Totals over averages. A total is true at n=1 or n=100. "Typically" and "on average" need a crowd we may not have, so avoid them.
6. Every number gets a dimension: a window, markets, languages, channels or accounts. "1M responses" is a number. "1M responses across 9 markets in 12 months" is scale.
7. Exact and rounded, both on the page. Exact in the body with thousands separators (1,264,530). Rounded floor in the title and the stat strip (1.2M+). Round down to a clean figure that stays true as the number grows.
8. Cut anything unflattering. A weak vertical, a flat trend, a small channel: leave it out rather than explain it. Keep totals consistent across stories. Never highlight survey counts; they're not exciting.
9. With and without, not before and after. The problem section shows life without the workflow, the shift and mechanics show life with it. No timeline, no "day 1, day 2". A with-and-without table is optional; the example doesn't use one.
10. Use cases come from your ICP persona needs or your product's use case library. Never invent one.
11. One easy-reading cohort label for the headline, granular callouts underneath. Bundle everything B2C-facing under "B2C software and apps" (e-learning, media, marketplaces, retail and loyalty, consumer software, healthcare apps, fintech apps). Never split out a narrow vertical such as "e-learning apps" as its own block. Call out a sub-vertical only where the data shows a distinct pattern, and express it as a percentage of the parent block, not a raw number.
12. Address CX teams, not support teams, when CX teams are the buyer. Use the CX vocabulary analysts like Gartner use: Voice of Customer, inner loop (fix it for this customer), outer loop (fix it for everyone), transactional CSAT, direct and indirect feedback. The angle is understanding users better and making changes that scale across a similar segment. Never position Example Feedback or a partner as a "segment tool" or as a place to "centralize" feedback; use action language (close the loop, fix, act).
13. It must read like a story worth telling, not a stat sheet. Borrow the classic customer story arc: a problem the reader recognizes, the shift, the mechanics with screenshots, the result. Lead with the Voice of Customer framing and the two loops, and end with how other personas win (lifecycle teams via customer attributes in marketing automation, product and research teams via Feedback Library).
14. House rules: US English, active voice, contractions, no em dashes or en dashes (hyphens, colons and periods only), no superlatives ("best-in-class", "powerful", "robust"), no "focused" as an adjective, real job titles only (never "Research Ranger" or "Product Architect"), use the current product area names (never a retired name), Collect, Analyze, Act where it fits.

## Step 1: Verify the workflow is real

Before Hex, search your help center (e.g. `https://help.example.com`) for the feature or integration and read what it actually does. Note the exact capability and the article URL; both go into the "How to set it up" section later. If the help center doesn't support a claim you planned to make, drop the claim. Do not assume standard SaaS behavior applies.

If the topic touches a product area with its own messaging guide (for example Feedback Library, or the AI connector and AI assistants), read that messaging skill or doc first. Those guides hold claims that aren't cleared externally.

## Step 2: Research in Hex

Hex is the only data connector for data stories. If your data team only exposes Hex Threads (no direct SQL), ask in plain language, poll `get_thread` until IDLE, and use `continue_thread` for follow-ups. Warn the user that a thread takes a few minutes.

Read `references/hex-thread-prompts.md` and use its prompt template. The important fixed definitions, so stories stay consistent:

- Cohort: active paying accounts today (Hex's own status definition, deleted and internal accounts excluded) that actually use the topic feature or integration in the window. Ask for the net counting method (daily response deltas including days where counts go down). Widening the cohort to churned, free, trial and deleted accounts usually moves the total very little, so paying-today is the default; run the sensitivity check only if the user asks, and record the difference in the internal notes. Exact figures drift as the warehouse takes in late responses, so re-run once on publish day and refresh every exact number from that single run. Prefer event-level evidence (responses sent, surveys triggered, tickets created) over "configured" flags. A configured-integrations list (for example one synced from a CS platform such as Custify) shows what was set up, not what's running, so use it only as a fallback and say so.
- Vertical label: the industry label column on your companies table (`<companies_table>.<industry_shortlist_column>`), an enrichment label from a tool such as Clay. Check its coverage on paying accounts before relying on it. For sub-verticals (food delivery, mobility, travel, gaming, loyalty) ask Hex to keyword-group the free-text industry column (`<industry_free_text_column>`). Avoid low-coverage or generic industry fields (for example a CRM's default industry property or a deprecated signup field). Reading a stored enrichment column costs nothing and does not call the enrichment tool.
- Always ask for: the hero total, the cohort size, the per-vertical breakdown, the dimension numbers (markets or countries, languages, channels, surveys, time span), the share of the total carried by the single biggest account (internal only, so you know what the story rests on), and the definitions and caveats Hex used.

Mixpanel (or your product analytics tool) is optional and off by default. Use it only when Hex can't answer a UI adoption question (which workspaces used an app feature) and the user says yes. It logs clicks and toggles, not volumes. Check the connector has the scopes it needs before relying on it.

Known warehouse gaps: keep a dated list here of what the warehouse can't answer yet (for example: no log of integration deliveries such as tickets created, updated or commented; no Feedback Library items by source; no project-to-source link). Until those are modeled, numbers for them come from someone's manual analysis; label them in the internal notes with who produced them and the date, and don't cross-check them.

## Step 3: Pick the numbers

- Hero stat: the biggest total that directly expresses the topic, not the cohort size. When a feature has several uses that overlap (an integration that both sends surveys and writes answers back), the hero is the deduplicated combined total, and each direction becomes its own exact number in the use-case table with the overlap stated once. Cohort size is internal.
- Two or three supporting stats: whatever the story has. No fixed set. Favor the ones that add a dimension (markets, languages, channels, surveys).
- Vertical breakdowns: one block per vertical with a real number and an inferable workflow. Map warehouse labels to story labels with `references/vertical-map.md`. B2C verticals lead. B2B SaaS, agencies, manufacturing, wholesale and education are allowed when their numbers earn a place, never as the lead.
- Cut what's weak. If a vertical has a thin number or the inferred workflow is a stretch, drop it.
- Internal note: list every number you considered and cut, with the reason, so the next story can reuse the work.

## Step 4: Persona and use cases

Pick the lead job title from the topic:
- Support and help desk integrations, CSAT, NPS, CES: CX Manager, Head of Customer Experience. Not Support Lead as the lead persona. Read your CX persona reference if it's available: CX thinks in segments, RFM, direct plus indirect feedback, inner and outer loop. Use that vocabulary, and name Voice of Customer explicitly.
- SDK, in-product and mobile surveys, event targeting, product analytics integrations: Product Manager, Product Owner, Product Designer.
- CRM and marketing automation (e.g. HubSpot, Customer.io), email and website surveys: CRM Manager, Growth Marketer, Product Marketing Manager.
- Feedback Library, Ask AI, transcripts, multi-source analysis: User Researcher, Customer Insights Manager, Research Lead, plus Product Manager.
- AI connector, Slack, Teams: whichever persona the workflow serves, with your AI messaging rules on top (for example: every survey an AI assistant creates is a draft; never imply a survey launches from Slack or an assistant).

Use cases: take them from your ICP reference persona "wants" and the vertical's own CX questions. For Feedback Library topics, use your product's own use case library only. Every use case card names the job title it serves and ties back to a number in the story.

## Step 5: Write the draft in chat

Use the template in `references/doc-template.md` exactly. It has two parts: an internal notes block at the top (never published) and the story. Draft it in chat first, lock it element by element if the user wants (title, then stat strip, then sections), and only create the doc once they say go.

Title shape: fact first, hook as the tail. Rounded numbers, the partner or feature, Example Feedback named, an action verb. The example: "How Fabrikam Desk customers turn 1.2M+ tickets and 300K+ survey responses into feedback that fixes itself, using Example Feedback." Rules learned while getting there:
- Never hook-first ("Feedback in, fixes out: how...").
- Never a storage verb (centralize, collect, gather). Action verbs only.
- Your product must be in the title, not just the partner.
- If the title leans on "loop", make the meaning plain ("fix it for one customer, then for everyone") or pair it with "closed-loop VoC".
- Keep it under about 110 characters. Offer options in batches of three to five, letter-labeled, with a pick.

Offer the title last, after the body is agreed; it takes the most rounds.

Copy checks before you show it: every number has a dimension, every workflow sentence has a help center article behind it, every use case has a job title, every quote is verbatim from the library with attribution, no survey counts, no dashes, no superlatives, no "centralize", no customer is identifiable.

## Step 6: Create the doc

Ask which the user wants: a Google Doc (read the `google-workspace` skill first; create it in their Drive root unless they name a folder, as HTML so the tables land as tables) or a Claude Doc (the `docs` skill; create the outline first, then fill section by section, and leave the Part A notes out unless they ask for them). Title: `Data story: [Topic] (draft)`. In a Google Doc the internal notes go first, then the story. Keep formatting exec-ready: headings, short paragraphs, the stat strip and the framework and use-case tables as real tables, brand accent color on headings, Inter.

## Step 7: Reply

Short. Doc link, the hero stat in one line, the cohort and callouts included, what you cut and why, and anything marked `[to confirm]`. Offer to run a content review skill on the draft (if you have one) before it goes to your CMS. If the session changed how data stories should be built, offer to update this skill.

## Writing rules

- Numbers: exact in the body with thousands separators, rounded floor in title and stat strip, both always present.
- Plural cohorts only. "Marketplace apps route", never "a marketplace app routes".
- Present tense for what cohorts do. Past tense only for totals over a window ("sent 327,905 responses between January and December 2025").
- Every workflow claim links to a help center article in "How to set it up".
- Internal notes stay internal: the Hex thread link, the label source, the single-account share and the cut list never reach the published page.
- No customer is identifiable from a description. "A Nordic food delivery app with 5M users" is a name. If a vertical has one account and the numbers would make it obvious who it is, say so in the internal notes and let the user decide.
