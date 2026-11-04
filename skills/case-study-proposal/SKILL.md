---
name: case-study-proposal
description: Turns what a CSM or seller at Example Feedback (a fictional customer feedback platform) knows about a customer or prospect into a customer-facing Google Doc, either a full case study proposal (case study guidelines) or quick LinkedIn post guidelines for a customer quote, backed by a research pass across Hex, Custify and HubSpot when the requester has no angle, and logs it as a To Do issue in the Linear "Customer Stories" project for the marketing owners to approve before it goes to the customer. Use whenever someone wants a case study proposal, case study guidelines, a customer story pitch, LinkedIn post guidelines for a customer, a customer quote or testimonial post, or to propose, prep or pitch a case study or testimonial for a customer or lead, even if they only name the company ("can we do a case study with X?", "X could post about us", "prep a case study for X"). Also use for batches of logos marketing wants testimonials from.
---

# Case Study Proposal

The examples use Example Feedback, a fictional customer feedback platform. Replace the product name, links, people and Linear values in "Fixed assets" and Step 4 with your own.

Three templates, all end in a customer-facing Google Doc + a Linear issue. The skill picks the route itself after research (see "Pick the route" in Step 2):
- **Full case study, existing customer** → action-first doc: to-do list, results to confirm, questions to answer (references/case-study-customer.md)
- **Full case study, prospect** → plan-forward doc: metrics to track from day one (references/case-study-prospect.md)
- **Quick LinkedIn post** → "LinkedIn post guidelines for [first name]" (references/linkedin-post-route.md)

This skill replaces the conversation marketing would usually have with the requester. Act like it: before each step, tell the requester in one plain sentence what you're about to do and why (see "Narrate the why" below).

## Most important rule: context before buttons

After research, you MUST write the angles out in full as normal message text (the blocks in Step 2: What we found, Evidence, What we'd ask for, Trade-off, Route) BEFORE calling the button tool. The button tool ends your turn, so if you call it right after the research tool calls, the requester sees only button labels and can't choose. Check before every button call: "Have I written the full context for every option in this message?" If not, write it first. For prospects with no strong story, also write the "No strong story yet" line and the "What Sales can gather" section first.

Take this slowly. Gather everything, research, then think through which story is strongest before writing. A weak or vague use case is the main way this fails.

## Fixed assets (never leave these out or empty)

Images (public URLs, insert with `<img src="URL">`):
- SPONSORED_POST_IMG = `<YOUR_PUBLIC_IMAGE_URL>` (a mock personal LinkedIn post with a "Promoted by Example Feedback" label)

Links (always hyperlink these words, never leave a bare "(example)"):
- Customer stories → https://example.com/customer-stories/
- Reference stories (pick the closest to the topic): Contoso → https://example.com/customer-stories/contoso/ , Northwind Traders → https://example.com/customer-stories/northwind-traders/
- Fabrikam (5-star review example, use for G2/review topics) → https://example.com/customer-stories/fabrikam/
- "example" (personal post we drafted for a customer) → `<YOUR_EXAMPLE_PERSONAL_POST_URL>`
- Example Feedback LinkedIn page → `<YOUR_COMPANY_LINKEDIN_URL>`
- Example of a promoted customer post → `<YOUR_PROMOTED_POST_URL>`

People (link names as mailto):
- Case study owner (full case studies) → [Case study owner name](mailto:case-study-owner@example.com)
- Social owner (LinkedIn posts and post images) → [Social owner name](mailto:social-owner@example.com)

## Narrate the why

Keep each line to one sentence, friendly, no jargon. Examples:
- Start: "I'll ask a few quick questions, the same ones marketing would ask you, then turn your answers into a doc you can send."
- Existing customer, has an angle: "I'll check Hex, Custify and HubSpot to back up your angle with data, so you don't have to dig it up."
- Existing customer, no angle: "No angle yet, no problem. I'll check Hex (how they use Example Feedback), Custify (what they've told their CSM) and HubSpot (why they bought) and come back with a story idea."
- Prospect, no angle: "They're not a customer yet, so there's nothing in Hex or Custify. I'll check HubSpot for the deal context and come back with a story idea."
- Prospect, before the doc: "Since they're not a customer yet, I'll frame this as a starting idea and questions we'll check in on later, not a finished story."
- Before the doc: "Now I'll write the doc in Google Docs. [For customers: it opens with a short to-do list so they know exactly what to fill in.]"
- Before Linear: "Last step: I'm logging this in Linear (Customer Stories) so marketing can approve it before it goes out."

## Step 1: Ask the requester (interactive)

Use the interactive question tool (tappable buttons, e.g. ask_user_input) for anything with fixed options. Plain questions only if the tool isn't available. One round at a time.

Round 1 (buttons), in one call:
- "Is this a customer or a prospect?" → Existing customer / Prospect
- "Do you already have an angle for the story?" → Yes, I have an angle / Not really

Round 2 (plain text, short): your name and team, company name and website, contact person (name and role, if known), and if they have an angle:
- Prospect: what they want to use Example Feedback for, why they're choosing us, what they're switching from, expected results, pain points, anything specific they asked for.
- Existing customer (ask more here, Hex only covers product usage): what they use Example Feedback for, results they've mentioned (even rough), things they've said or written about us (quotes, talks, posts, events), which teams use the insights, changes they made because of feedback, other people who should be in the story, anything they promised to share.

Don't ask the requester which route they want. They usually don't know, and it depends on the data. You pick it in Step 2.

If they picked "Not really", don't ask about topics. Go straight to Step 2 and propose the angle yourself.

### Case study topics (the stories we need)
- We switched from [competitor] to Example Feedback
- We use multichannel surveys to collect feedback
- Example Feedback has the best SDK (or other technology)
- Example Feedback has the best advanced targeting
- Feedback analytics helped change our business strategy
- Example Feedback made acting on feedback possible (integrations)
- We run surveys at big scale (e.g. millions of responses yearly)
- Multiple teams use the data we collect in Example Feedback, and this is what they do with it
- (LinkedIn route also) How I use the Example Feedback AI connector with Claude/ChatGPT to work with customer feedback

Replace this list with the story topics your own marketing team needs.

## Step 2: Research

Which sources to check depends on two things: customer or prospect, and angle or no angle.

| | Has an angle | No angle |
|---|---|---|
| Existing customer | Hex + Custify + HubSpot | Hex + Custify + HubSpot |
| Prospect | None (HubSpot only to fill gaps) | HubSpot |

What to look for in each source:
- **Hex** (product usage): integrations connected, survey channels (web, in-product, mobile SDK, email, link), response volume and survey count yearly, targeting and triggers, seats/teams, customer since, plan, AI analysis / Feedback Library / AI connector usage, NPS/CSAT/CES surveys.
- **Custify** (CS view): if there's no Custify connector, check whether your warehouse (via Hex) mirrors some CS platform data such as plan, users and integrations. CSM notes usually aren't there. Look for: CSM notes, meeting notes, success plans and goals, health score history, renewal/expansion notes, feedback or praise they've shared, contacts and champions.
- **HubSpot** (sales view): deal notes and properties, closed-won reason, competitor or tool they switched from, pain points from discovery calls, emails and call notes, associated contacts.

**Likely contacts:** if the requester didn't name a contact, pick the single most likely one from HubSpot and Custify (job title closest to the chosen topic, e.g. Client Success or Support for a help desk CSAT story). Put them in the doc's Key people line marked `[to confirm]` and mention them to the requester.

Many "why we moved" and boilerplate-topic answers live in Custify and HubSpot, not Hex.

**Integration fit:** if one integration carries most of the customer's volume (e.g. most responses come through their help desk integration), say so to the requester in one line and add it to the Linear description as "Fits [integration] integration content". Marketing may use the customer in an integration page or data story.

**Has an angle:** use the data to back it up. If the data points to a stronger story, explain it with the full angle block below (not one line), then ask which to go with. Otherwise go to Step 3.

**No angle:** present 1 to 2 story ideas before writing the doc.

**Hard rule: explain every angle in the message text BEFORE showing any buttons.** The button tool ends the turn, so anything not written first never reaches the requester. Never show angles only as buttons, and never as a one-line list. The requester has to be able to choose without asking anything else.

For each idea, write a short block in this exact shape:

**[Number]. [Topic from the list]: [the story in one sentence]**
- **What we found:** 2 or 3 sentences of context. What the customer does with Example Feedback, how long, which team, what changed. Plain language, no internal jargon.
- **Evidence:** the 2 or 3 strongest facts, with numbers and source (Hex / Custify / HubSpot). Mark anything unsure `[to confirm]`.
- **What we'd ask the customer for:** the quote or result the post or case study would hinge on.
- **Why it works / trade-off:** one line, e.g. "strongest numbers, but needs a Product voice to land".
- **Route:** full case study or LinkedIn post, with the reason in a few words.

Mark the recommended idea with "(recommended)" in its heading.

Example of one block (fictional):

**1. Scale: Contoso runs 135k survey responses a year across web and mobile (recommended)**
- **What we found:** Contoso's product team has used Example Feedback since 2023, mostly for in-app NPS and feature feedback. Volume jumped after they added the mobile SDK last spring, and their CSM notes they now review feedback weekly with product leads.
- **Evidence:** 135k responses this year, 70% via Customer.io + SDK (Hex); weekly feedback reviews with product (Custify); bought to replace manual spreadsheet exports (HubSpot).
- **What we'd ask the customer for:** a quote on how feedback volume changed their roadmap decisions.
- **Why it works / trade-off:** strongest numbers we have, but needs a Product voice to land.
- **Route:** full case study, enough numbers for a before and after.

Only after all blocks are written, ask with buttons. The button question itself stays short ("Which story should I go with?"); the context lives in the text above it, never only in the labels. Each button repeats the topic plus its key proof point, never the topic alone. Good: "Scale: 135k responses a year via Customer.io + SDK". Bad: "1. Big scale, mobile channels". If they pick "Switched from a competitor" and the competitor isn't in the data, ask which one.

The same rule applies whenever you surface an angle the requester didn't bring: a "stronger story" flag on their own angle, a topic-list mismatch, or a second topic. Give it the same block (What we found, Evidence, What we'd ask for, Trade-off) instead of a one-line mention.

**Rules:**
- **Never stall on missing info.** Don't send the requester off to ask someone (e.g. "ask the AE these 4 points", "wait until after the demo") before proposing angles. Work with what the data has: present the angles with the full blocks, mark weak spots `[to confirm]`, recommend one, and continue. Gaps go into the doc as questions for the customer or prospect, and into the Linear description under open questions. For prospects this is the expected case, since the doc is a starting idea anyway.
- An angle based on a signal (e.g. email clicks) rather than something the contact said is fine to propose. Say it's a signal in the Evidence line and keep going.
- If a source has no data or the connector isn't available, say which one in one line and continue with the rest.
- Never present guessed numbers as facts. Mark anything you're not 100% sure about `[to confirm]`, in the doc and in replies. The doc is reviewed by marketing before it goes out, so flagged guesses are fine.
- Pick 1 main topic (max 2) with the strongest evidence. If the requester's idea and the data disagree, explain the data's angle with the full angle block and ask which to go with.
- Contact names and facts from Custify and HubSpot can go in the doc, marked `[to confirm]` where you're not sure. Don't paste raw internal notes (deal notes, CSM notes, pricing) into it.

**Check against the topic list.** Before picking the final story, map it to the closest topic in "Case study topics (the stories we need)". This applies to the requester's own angle too.
- Fits a topic → frame the story around it and pull the proof that topic needs (e.g. Scale → response volume; Switched → previous tool and why they moved).
- Fits none → say so in one line and suggest the closest topic it could lean into.
- Fits two → pick the one with stronger evidence, mention the other in one line.

**Prospects: flag when there's no strong story yet.** A story is strong when it maps clearly to a topic in "Case study topics (the stories we need)" and has at least one confirmed fact behind it (something the prospect said or a deal property, not only a signal like email clicks). If no angle meets that bar:
- Say so plainly at the top of the reply, before the angle blocks, e.g. "No strong story yet for Northwind Traders. Here's the best we have, and what Sales can find out to get one."
- Still show the best 1 to 2 angles with the full blocks (this doesn't override "Never stall on missing info").
- Then add a **What Sales can gather** section: for each topic from the list that the prospect could plausibly fit, one line with the topic and the specific question Sales can ask on the next call to confirm it. Example: "Switched from a competitor → What are you using now, and what's not working?" / "Multiple teams use the data → Which teams would use feedback from all 7 brands?" Order by how likely the topic is for this prospect, max 5. Skip topics with no plausible fit.
- Put the same list in the Linear description under open questions, so marketing can follow up after the next call.

**Pick the route.** Decide between full case study and LinkedIn post based on what the research found:
- Full case study → enough data for a before and after (at least 2 or 3 solid numbers or results), or a prospect with a clear use case we can track from day one.
- LinkedIn post → thin data, one strong result or quote, or a story that works best in one person's voice.

Tell the requester the route in one line with the reason, e.g. "Going with a LinkedIn post: strong quote, but not enough numbers for a full case study yet." Add it to the Linear description so marketing can switch it on review.

If the route is LinkedIn post, ask then (buttons): "Will [contact] write the post themselves?" → Yes, they'll write it / No, we should write it / Not sure

## Step 3: Write the doc

Pick the template: existing customer + full case study → case-study-customer.md; prospect + full case study → case-study-prospect.md; LinkedIn post → linkedin-post-route.md. Read it and follow it exactly.

How to create the Google Doc: build the whole doc as one HTML file and upload it with the Google Drive create file tool (`textContent` = the HTML, `contentMimeType` = `text/html`), which converts it to a Google Doc. Insert images with `<img src="[public URL from Fixed assets]" width="500">`. Google fetches the image from the URL during conversion, so the image lands in the doc with no base64 and no later editing. Never embed base64. Never leave an image out or swap it for a placeholder. SPONSORED_POST_IMG is always set and always included.

**Spacing.** Google Docs drops most default HTML spacing, so set it inline on every element:
- `<h1 style="margin-bottom:12pt">`
- `<h2 style="margin-top:24pt;margin-bottom:8pt">`
- `<p style="margin-top:0;margin-bottom:10pt;line-height:1.4">`
- `<ul style="margin-top:0;margin-bottom:10pt">` and `<li style="margin-bottom:6pt;line-height:1.4">`
- Tables: `<table style="border-collapse:collapse;margin-bottom:12pt">` and `<td style="padding:6pt;border:1px solid #cccccc">` (same for `<th>`)
- "Your answer:" goes in its own `<p>` after the question, never after a `<br>`.

**Answer fields.** Every place the customer or prospect writes something must stand out at a glance:
- After every question (and the quote prompt), add a yellow answer box: a one-cell, full-width table:
  `<table style="border-collapse:collapse;width:100%;margin-bottom:14pt"><tr><td style="background-color:#FFF4CC;border:1px solid #F2C94C;padding:10pt;height:40pt"><b>✍️ Your answer:</b></td></tr></table>`
- In tables they fill in (e.g. Before / Now, or the "Your input" column in prospect metrics tables), give every empty cell `background-color:#FFF4CC` and put "✍️" in it. Cells we pre-filled stay white.
- Put the question itself in bold above the box, in its own `<p>`.
- Never use a plain "Your answer:" line. It gets lost in the doc.
- Put the image in its own `<p style="margin-top:12pt">`, directly after the "What will the promoted by Example Feedback post look like? 👇" line. The line always comes first, the image second, in every route.

**Check the doc before Step 4.** Export the new doc as HTML with the Google Drive download tool and check: the image landed (an `<img>` is there), the 👇 line sits right above it, and no "{{" or "<YOUR_" placeholder or bare "(example)" is left where a Fixed asset belongs. If anything is off, fix the HTML and create the doc again, then trash the broken one. Don't tell the requester the doc is ready until this passes.

Use real `<a href>` links for everything in Fixed assets, `<h1>`/`<h2>` for headings, `<table>` with a header row for tables, `<ul><li>` for bullets. Never start `<li>` text with "- ", "→" or "•": `<ul>` already adds the bullet. Key people line: exactly three people, in this order, never more:
- One key person from the customer, `[to confirm]` if it came from HubSpot or Custify rather than the requester
- The requester (the Sales or CS person who started this), with their role. Don't add other AEs, CSMs or deal owners.
- Marketing owner: the case study owner (from Fixed assets) for full case studies, the social owner for LinkedIn posts

Never `[FILL]` a name you were told. Only use `[FILL]` when no source has the name.

**Be as specific as possible.** Every ask in the doc names the exact topic, integration, metric or screen it's about. Include at least one targeted quote prompt tied to the chosen topic and the data, e.g. "How does the Example Feedback and Slack integration help your team follow up on CSAT and NPS responses from your help desk?" Cover every survey type and integration the data shows for that flow (e.g. CSAT and NPS, not CSAT only). A customer should be able to answer any question in a sentence or two without guessing what we mean.

"👉 Your input needed" markers: put them at the start of every heading or line where the customer has to act. Keep everything else short, customers scan.

## Step 4: Create the Linear issue

Linear tools to use (load them via tool search if deferred): `list_users`, `list_issues`, `save_issue`.

Fixed values:
- Team: `<YOUR_LINEAR_TEAM>` (e.g. Marketing)
- Project: Customer Stories (`<YOUR_LINEAR_PROJECT_URL>`)
- Status: Todo
- Mentions: `@<case-study-owner>` and `@<social-owner>`

Steps:
1. `list_issues` in Customer Stories for the customer name, to avoid a duplicate. If one exists, tell the requester and ask whether to update it instead.
2. `list_users` filtered to the marketing team, to get the IDs for the case study owner and the social owner (needed for the assignee in the LinkedIn route). Never guess IDs.
3. `save_issue` with your team, project Customer Stories, status Todo, and:
   - Title: `Case study proposal: [Customer]` or `LinkedIn post: [Customer]`
   - Description: requester name and team, customer or prospect, route and why it was picked, chosen topic, one-line story, key findings with source (Hex / Custify / HubSpot), integration fit if any, open questions, link to the Google Doc, then "`@<case-study-owner>` `@<social-owner>` please review before this goes to the customer."
   - LinkedIn route: always add "`@<social-owner>` to prepare the post image" to the description.
   - LinkedIn route where the contact won't write it ("No" or "Not sure"): assignee = the social owner, to draft the post; say so in the description.

If the Linear call is declined or fails, say which (declined by the user vs error) and offer to retry.

## Step 5: Reply to the requester

Short: Google Doc link, Linear issue link, chosen topic in one line, anything `[to confirm]`. Remind them not to send it to the customer until marketing approves, and to check links in Google Docs, not the Claude preview: LinkedIn links won't open in the preview.

For prospects: remind the requester the doc is a starting idea. They shouldn't ask the prospect to confirm the story, since there's nothing to confirm yet.

## No screenshots from customers

Never ask the customer or prospect for screenshots of their Example Feedback account or any other real screenshots, in any route. Logo and a team photo are fine for full case studies. Marketing prepares all product visuals. For LinkedIn posts, the social owner prepares the post image every time, so the doc says we'll prepare it.

## Writing rules
- Customer-facing: plain, friendly, direct, written to "you" / "your team".
- No em dashes. No AI-isms. Avoid "It didn't X, it Y" constructions.
- Bullets use hyphens or arrows in plain-text output (Linear, chat replies). In the HTML doc, use `<ul><li>` only.
- Never invent names, surnames, job titles or numbers. Use known names or `[FILL]`.

## Batch mode
For a list of companies (e.g. logos marketing wants testimonials from): run Steps 2 to 4 for each (existing customers with no angle, so check Hex, Custify and HubSpot per Step 2, and pick the strongest idea yourself instead of asking), skip Step 1 questions you can't get answers to, mark the requester as marketing, default to the LinkedIn post route unless told otherwise. Flag thin-data companies in the final summary.
