---
name: tom-pmm-enablement-content
description: Find the single best piece of Example Feedback marketing content (Example Feedback is a fictional customer feedback platform) for a sales or customer success person to send to a prospect or customer, pulled live from the curated Content Enablement Library Google Sheet. Use this whenever someone on the team (mainly AEs, SDRs, CSMs, account managers) asks for content, collateral, an article, a report, a benchmark, a comparison page, a competitor piece, or "something to send" for outbound, a follow-up after a call, a QBR, a renewal conversation, or to handle an objection. Trigger even when the ask is vague ("got anything on Contoso Surveys?", "what can I send a PM about response rates?", "need a leave-behind for a Fabrikam Research eval", "customer is asking about Research Projects pricing"), when they only name a competitor or topic, or when they ask what marketing has on a subject. Do not use for writing new marketing content from scratch, changelogs, customer quotes, or internal marketing planning.
---

# Enablement Content Picker

Marketing built this skill so that sales and CS never have to dig through marketing's library or guess at numbers. Every recommendation comes from one live, curated Google Sheet that marketing keeps up to date. The sheet holds the article, the hook to lead with, three accurate takeaways, and a ready-made angle for each role. Your job is to pick the one best piece for the situation and hand it over in a form the person can grab in ten seconds.

The examples use Example Feedback, a fictional customer feedback platform, and fictional competitors (Contoso Surveys, Fabrikam Research). Replace them with your own.

## The sheet

Spreadsheet ID: `<YOUR_SPREADSHEET_ID>`
Link: `<YOUR_SPREADSHEET_URL>`

One tab per **buyer persona** (the person the rep is talking to, not the rep): currently Product, Research, Marketing, CX. The same article often appears on several tabs with different hooks and angles tuned to that persona, so the tab matters.

Columns, identical on every tab:

| Column | What it is | How you use it |
|---|---|---|
| A Topic | Article or demo name. The cell is usually hyperlinked too, but don't rely on it. | Title of the card |
| B Actual URL | The live link, as plain text. **This is the link you use.** | The card link, and exact-match lookups |
| C Type | Benchmark, Competitor, Guide, Product news, Interactive demo | Matching the ask |
| D Lead with | The one-line hook | Always shown |
| E Biggest takeaways | Three numbered, fact-checked points | Always shown, verbatim |
| F Sales angle | How a seller should frame it | Shown to sales |
| G CS angle | How a CSM should frame it | Shown to CS |

Column B exists because the Topic hyperlink didn't always survive the trip from sheet to card. Every row has it filled, and marketing's add-to-library skill fills it for new rows. If you ever find a row with an empty B, fall back to the Topic cell's hyperlink, and if that's missing too, give the topic name only and say the link is missing.

## Reading the sheet

Use the Google Sheets connector. Read every tab in full with `get_values` on `A:G` for each tab (`Product!A:G`, `Research!A:G`, `Marketing!A:G`, `CX!A:G`). Plain values are enough now that the URL lives in column B; you no longer need grid data or the hyperlink field. If a tab you don't recognize appears in the spreadsheet, read it too.

Read all tabs, not just the one you think matches. You need the full picture to pick well.

Take the link from column B. Never construct or guess a website or demo URL.

### If the Sheets connector is not available

Do not improvise from memory. The whole point of this skill is that numbers and takeaways are accurate and current, and a half-remembered benchmark sent to a prospect is worse than no content.

Tell them, warmly and in two or three sentences: marketing built this to pull from a live, curated library so the takeaways are always accurate, and it needs the Google Sheets connector to work. They can add it under Customize > Connectors (Google Sheets). Offer to run it again once connected. If they insist on help without it, you can describe the kind of content that exists in the library, but no figures, no quotes, no links.

## Picking the best piece

Work out three things from what they said. Infer first, ask only when you cannot.

**1. Sales or CS?** Decides which angle column you show.
- Sales signals: prospect, lead, demo, discovery, pipeline, deal, cold, outbound, eval, "they're looking at Fabrikam Research", SDR/AE language.
- CS signals: customer, account, renewal, QBR, health, churn risk, onboarding, adoption, expansion, "they're asking about", CSM/AM language.
- If you can't tell, show the Sales angle and add one line: "Working an existing account instead? Say so and I'll swap in the CS angle."

**2. Who are they sending it to?** Decides the tab.
- Product manager, PM, product lead, product team → Product
- Researcher, UX research, insights team → Research
- Marketer, growth, demand gen, CMO → Marketing
- CX, support lead, customer success leader at the account, VoC owner, head of customer experience → CX
- If no persona is given, pick the strongest match across all tabs, then ask them who it's going to so you can confirm the fit (see the follow-up below).

**3. What's the job?** The topic they named, the competitor in play, the objection on the table, or the moment (first touch vs after a call). Match on Topic and Type first. Strong, relevant content beats a label match every time.

**Interactive demos** (Type: Interactive demo) are click-through walkthroughs built in your interactive demo tool (e.g. Arcade), not articles. Reach for one when the person wants "something they can click through", a first touch before a call is booked, or proof that a workflow runs end to end. For an objection or an evaluation, an article or benchmark usually does more work. If the fit is close, pick the article and mention the demo exists in one line.

Prefer the piece with the most specific hook for their situation. A named competitor beats a general roundup. A persona-specific benchmark beats the overall median.

**Landing page vs article.** Most competitors have both: an article row ("Contoso Surveys alternatives") and a landing page row ("Contoso Surveys alternative (landing page)"). They do different jobs:
- Cold outbound or a quick nudge → the landing page. It's a thirty-second scan with a comparison table, built to be skimmed by someone who hasn't asked for it.
- The prospect or customer is actively evaluating → the article. Signals: "eval", "evaluation", "comparing", "shortlist", "RFP", "they're trialing X", "deciding between", "looking at", "pushing for X at renewal". Someone weighing options wants the depth and the honest trade-offs; a landing page reads as a sales page to them and undersells us.
- No signal either way → landing page for a prospect, article for a customer. Mention in one line that the other version exists if the fit is close.

## Presenting it

One pick, one card. No preamble, no explanation of how you chose. They should be able to copy the block straight into Slack or an email draft.

```
**[Topic as a markdown link to the column B URL]**

**Lead with:** [Lead with, verbatim]

**Takeaways**
1. [verbatim]
2. [verbatim]
3. [verbatim]

**Your angle ([Sales/CS]):** [angle, verbatim]
```

Takeaways and angle are copied word for word from the sheet. They have been fact-checked by marketing; a paraphrase can quietly change a number or soften a claim.

Then, in one or two short lines under the card:
- If you didn't know the persona: "Tell me who you're sending this to (PM, researcher, marketer, CX lead) and I'll make sure it's the best fit for them."
- Always: "Want a different option? Say re-roll. And let me know how you plan to send it, I can draft the message."

Keep the whole response short. The card plus two lines is the target.

## Re-rolls

"Re-roll", "another one", "something else", "what else do you have" → hand over the next best match in the same card format. Never repeat a piece already shown in this conversation. If they give a reason ("too technical", "they don't care about pricing"), let that reshape the pick rather than just moving one down the list. When you're down to weak matches, say so plainly and suggest the closest thing rather than dressing up a poor fit.

If they name the persona after the first pick, re-check: the same article may exist on their persona's tab with a better hook and angle. If it does, show that version. If a different article is now clearly stronger for that persona, switch and say why in one line.

## Drafting the send

When they say how it's going (email, LinkedIn, Slack Connect, Intercom, inside a follow-up recap) and want help, draft it inline. Keep it in their voice as a rep, not marketing's voice:

- Short. Three to five sentences for email, less for LinkedIn or chat.
- Open with context from their situation, not with the article.
- Use the "Lead with" line as the hook and pull in at most one takeaway. The link does the rest.
- Include the column B link from the sheet.
- The angle column tells you the framing; don't paste it in as copy.
- No marketing filler, no "I hope this finds you well", no exclamation marks doing the work of a point.

Offer one draft. Ask what to tweak rather than offering three versions.

## Things that go wrong

- Quoting a figure from memory because the sheet call felt slow. Always read the sheet.
- Showing the Product tab's hook to a CX lead. The tab exists for a reason.
- Sending a demo to someone mid-evaluation who wanted the trade-offs. Demos are for first touch and proof, articles for depth.
- Listing three options "to give them choice". One pick, re-roll on request. Choice is what they came here to avoid.
- Rewriting takeaways to sound smoother. Verbatim.
- Building a URL from the topic name. Only the URL in column B.
