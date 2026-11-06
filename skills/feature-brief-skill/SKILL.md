---
name: feature-brief-skill
description: 'Use this skill whenever someone (a product manager or product marketing manager) wants to create a new feature brief for Example Feedback, a fictional customer feedback platform. Triggers include any mention of feature brief, positioning brief, new feature doc, or requests to document a new or updated feature for marketing purposes. Also use when someone shares a Notion link and says a feature brief has already been started. This skill governs the full workflow of creating and completing feature briefs collaboratively: all drafting, iteration, and content approval happens in chat first. Notion is only touched once the brief is finalized and the person confirms it is ready to be published.'
---

# Feature Brief Skill

The examples use Example Feedback, a fictional customer feedback platform with two products: Surveys and Feedback Library. Replace the product names, the architecture table, the Notion locations and the banned-terms list with your own.

## Purpose

Feature briefs are the single source of truth for launching any feature, at any tier. They live in Notion under the Product Marketing section and are used by PMMs, PMs, sales, and CS to align on positioning, messaging, and go-to-market before any content is created.

Your best existing brief (`<YOUR_CANONICAL_BRIEF_PAGE_ID>`) is the canonical example. All new feature briefs follow the same section structure, regardless of feature tier or complexity.

---

## Step 0: Before You Start

### Project check (do this first, every time)

Before doing anything else, **confirm the person is working in the Claude project that holds your company context.** Ask directly:

> "Are you working in the **<YOUR_CLAUDE_PROJECT>** project right now?"

- **If yes:** proceed to Step 1.
- **If no (or unsure):** say the following and do not proceed until they confirm or choose to continue anyway:

> "Quick reminder: for the most accurate output, work in the **<YOUR_CLAUDE_PROJECT>** project in Claude. It's preloaded with our current positioning, ICP reference, and tone of voice. Without it, I'll be working with less context and may miss nuances. If you're not in that project yet, start a new chat there and come back."

Only continue once the person confirms they're in the right project, or has acknowledged the limitation and chosen to proceed anyway.

---

## Step 1: Identify Who You're Talking To

Ask this question before anything else:

> "Before we get started, are you a **product manager** or a **product marketing manager**?"

This determines the workflow:

### If they are a Product Manager (PM)

- Their job is to fill in the product truth: what the feature does, how it works, what's launching, what's not launching, known limitations, key use cases, and real-world workflows.
- They are NOT responsible for positioning, external copy, or messaging tone. Don't push them on those.
- Help them avoid overly technical language where it isn't needed (see "Avoiding Over-Technical Language" below).
- PMs often start the brief. PMMs come in later to complete the positioning and copy sections.
- Be encouraging if they want to attempt positioning. Just note clearly which sections are PMM territory.
- **Before creating a new brief, always ask the PM:** "Has anyone already started a brief for this feature? You can check the Launches section of the Product Marketing page here: `<YOUR_LAUNCHES_PAGE_URL>`. If one exists, share the Notion link and I'll pick up where it left off."

### If they are a Product Marketing Manager (PMM)

- They own the positioning, taglines, messaging, objection handling, and competitive framing.
- Before starting from scratch, always ask: "Has a PM already started a brief for this feature? You can check the Launches section of the Product Marketing page here: `<YOUR_LAUNCHES_PAGE_URL>`. If a brief exists, share the Notion link and I'll pull it up."
- If a brief already exists: fetch it via the Notion connector using the page ID from the URL, review what's been filled in, and pick up where the PM left off.
- If no brief exists yet: create a blank one and work through all sections together.

---

## Step 2: Company Positioning Check

Before writing a single word about the feature itself, anchor it in the platform structure. Ask:

1. **What product does this feature sit under?**
   - Surveys
   - Feedback Library
   - Platform-level (applies to both)
   - New product (rare, flag if so)

2. **Is this a new feature, or an improvement to an existing one?**
   - If improving an existing feature: identify which one from the knowledge base and note what changes.
   - If new: confirm it isn't already listed somewhere under a different name.

This check prevents misclassification and catches naming conflicts early. Flag any inconsistency directly in the conversation before moving on.

---

## Step 3: Draft the Feature Brief in Chat (NOT Notion yet)

**Do not create anything in Notion at this stage.** All drafting, iteration, and content approval happens here in the chat first. Notion is only touched once you and the person have agreed the brief is complete and ready (see Step 5).

This is intentional. Updating tables and structured content in Notion via Claude is fiddly and slow. It's much faster to get the content right in the conversation, then push it to Notion in one clean pass at the end.

Say this to the person before proceeding:

> "I'll draft everything here in chat first, and we'll go section by section until you're happy with the full brief. Once it's finalized, I'll create the Notion page and populate it all at once. That way we're not fighting with Notion tables mid-conversation."

Then present the blank template structure below to show the person what sections you'll be working through together.

### Brief Template (work through this in chat)

```
# 🏆 Company-level positioning

**Example Feedback**: Customer Feedback Platform

| | Surveys | Feedback Library |
|---|---|---|
| **Category** | Survey Software | Research Repository |
| **Features** | Multichannel distribution: email, website, in-product, mobile app, link/QR | Projects: scoped feedback analysis, run once or continuously |
| | Targeting: behavioral triggers, events, URL, attributes, exit intent | Insights: AI-assisted pattern discovery across feedback, plus tracking of known insights over time |
| | Template library: pre-built NPS, CSAT, CES and other surveys | Reports: AI-generated reports that teams can refine, backed by quotes and evidence |
| | Integrations: native connections to CRM, messaging and collaboration tools | Feedback sources: connect support, sales call and review sources alongside survey data |
| | AI survey creation: generate a survey from a one-line description | Company context: personas, products and positioning that make AI output specific to your business |
| | Branding: custom themes, logo, CSS, white labeling | Research assistant: ask follow-up questions grounded in your project's sources only |
| | Survey logic: skip logic, branching, piping, display logic | Dashboards: custom widgets for tracking scores and trends across surveys |

[Note: replace this table with your own product architecture. It should stay as-is by default. Only update it when a new feature being briefed explicitly adds to or changes the architecture.]

---

# 📌 [Feature Name]

## 📅 Estimated release date

- Early access:
- Live for all customers:

---

## 📣 Can we talk about it?

[Who can talk about this, when, and with what caveats?]

---

## ✨ Important pre-information

## 👥 Who is this for?

**Primary persona: [Job title]**

[One sentence describing why this persona is primary: what specific, recurring job do they have that this feature directly unblocks? Anchor to a real workflow moment, not a general category.]

*Note: [Supporting data point if available: lost deals, customer requests, sales calls, etc.]*

**Secondary personas:**

**[Persona]:** [One to two sentences on their use case and why it's secondary, not primary. Include any honest caveats about why they might prefer another tool or channel for this job.]

*Note: [Any positioning caveat relevant to sales or CS conversations.]*

[Repeat for each secondary persona.]

---

[Naming notes, migration notes, or anything the team needs to know before reading further.]

---

## 🤖 Key features

[Table: Feature name | What it does]

---

## 🔑 Example taglines (by persona)

[Table: Key persona | Tagline options]

## 🔑 Additional key messaging

[Voice of customer phrases. What language do customers use when describing this problem?]

---

## 💉 How this solves customer pain points

[Table: Persona | Pain Point | How this solves it]

---

## 🤝 Messaging framework mapping

[Table: one column per pillar of your messaging framework. How does this feature map to each?]

---

## 🤗 Why does our customer care?

[Key personas: primary and secondary. What do they get out of this? Tangible reasons only.]

---

## ✨ How is this different from what we had before?

[What changed? What does this replace or extend?]

---

## 🤔 Known limitations, myths debunked, and objections handled

[Table: Common question | Answer]

---

## 🤸 Real-world examples and workflows

[Scenario-based examples per persona. Specific, grounded, outcome-focused.]

---

## 🎯 How is this different from what competitors offer?

[Competitor | Comparison point]
```

### Post-template cross-check (do this every time, for both PMs and PMMs)

After presenting the template structure, summarize back to the person what was pre-filled based on the conversation so far, and what is still blank or flagged as TBD. Use this format:

> "Here's what I've captured so far from our conversation:
> - **Confirmed:** [list what's filled in with real content]
> - **Flagged as open questions:** [list TBDs and why they matter]
> - **Left for PMM:** [list sections that need positioning input]
>
> Does this match what you had in mind? Anything I got wrong or that needs updating before we continue?"

Do not proceed to Step 4 until the person has confirmed the cross-check. This is the moment to catch misunderstandings early before they propagate through the rest of the brief.

---

## Step 4: Go Section by Section, In Chat

Work through the brief section by section **entirely in the chat**. Do not touch Notion at this stage. Do not jump ahead or fill in sections speculatively.

For each section:
1. Tell the person which section you're on and what it needs.
2. Ask them targeted questions to extract the right information.
3. Draft the content based on their answers and your knowledge of the company's positioning.
4. Show them the draft and ask for feedback. Iterate until they're happy.
5. Once they've approved the section, note it as confirmed and **immediately move to the next section.**

Do not update Notion between sections. Keep everything in chat until all sections are done. The full push to Notion happens in Step 5.

The pace is async: you fill in what you can from what they tell you, flag what's missing, and move forward. Don't block on sections that need the other person (PM or PMM) to complete.

### Keeping the conversation going

Do not drop the thread after each section. After confirming a section is approved, immediately say something like:

> "That's [section name] confirmed. Moving on to [next section name]: [brief description of what it needs]."

Keep going until one of the following is true:
- All sections owned by the current person are complete and approved
- The person explicitly tells you to stop or come back to it later
- You hit a section that genuinely requires the other person (PM or PMM) and cannot proceed without them

### Handoff message at end of PM sections

When all PM-owned sections are complete and approved in chat, say:

> "Your sections are all confirmed. Before I create the Notion page, is there anything you'd like to change or add? Once you give the go-ahead, I'll push the full brief to Notion in one go.
>
> The sections still needed from your PMM are: [list remaining PMM sections]. Once it's in Notion, share the link with them so they can pick it up."

**Do not create the Notion page until the PM confirms they're happy.**

### Completion message at end of PMM sections

When all sections are complete and approved in chat, say:

> "That's everything confirmed. The brief looks complete. Ready for me to create the Notion page and populate it with everything we've agreed here? Just say the word and I'll push it across."

**Do not create the Notion page until the person explicitly confirms.**

---

## Step 5: Push to Notion (Final Draft Only)

Only reach this step once the person has confirmed the brief is finalized and ready. Do not push partial drafts or works in progress to Notion.

**Create the Notion page with the full content:**

**Parent page:** create the brief as a subpage under the "Coming Up" section of your Product Marketing Launches page:
`<YOUR_LAUNCHES_PAGE_URL>`

The parent page ID is: `<YOUR_LAUNCHES_PAGE_ID>`

Use the Notion connector's `notion-create-pages` tool with:
- `parent.page_id`: `<YOUR_LAUNCHES_PAGE_ID>`
- `properties.title`: `[Feature Name]: Feature Brief` (for example "AI Follow-Up Questions: Feature Brief")
- Content: the full approved brief from the chat

Once created, share the Notion URL and confirm:

> "Done! The brief is live in Notion: [Notion URL]
>
> It's ready to be used for campaign planning, sales enablement, and content creation. If anything changes before launch (feature name, dates, scope), come back and we can update the relevant sections directly."

---

## Section-by-section guidance

**Company-level positioning**
Ask: What product does this sit under? Is it a new capability or an improvement? Cross-check against the product architecture. Flag any naming or classification conflicts immediately.

**Feature name and release date**
Ask: What's the confirmed feature name? Is there an early access phase? What's the estimated general availability date? Note if dates are unknown. Never guess.

**Can we talk about it?**
Ask: Is this under NDA? Can sales reference it with prospects? Can marketing publish? Are there conditions (for example "only after X date" or "only in sales conversations")? This section sets the rules for all downstream usage.

**Important pre-information**
Ask: Any naming changes from previous versions? Any migration of existing data or features? Anything the team needs to know before reading the rest of the brief? Keep this short and factual.

**Key features**
Ask: What are the specific features launching? What does each one do in plain terms? Probe for completeness: ask "is there anything else launching with this?" Watch for technical jargon. Help the PM express features in outcome terms, not technical specs (see language guidance below).

**Example taglines**
This is PMM territory. If a PM is filling this in, note that it's a starting point only and will be refined. Use approved voice of customer language from the knowledge base.

Always organize taglines by persona in a table, following the canonical brief's format. Never organize by format (for example "headline vs email subject") at this stage. Each persona gets its own set of options.

When a persona splits meaningfully into two angles (for example users who already have a competing tool vs users who don't), draft for both angles separately within that persona's section.

**Tagline subject clarity rule:** every tagline must make the subject obvious. If you removed the company name from the line, would it still be clear what product or feature it's about? If not, rewrite it. Never let a tagline read as if it could apply to any product.

Go line by line with the PMM, one persona at a time. Never present all personas at once and ask for a reaction on the full set.

**Additional key messaging**
Phrases the customer would use. Pull from discovery notes, research quotes, or the voice of customer language bank if known. This feeds campaign copy and sales scripts.

**Pain points mapping**
For each key persona: what specific pain does this solve? Be concrete. Avoid generic statements like "saves time." Anchor to a real workflow moment.

Before drafting any pain points or messaging, run this check: do the feature's actual mechanics support the framing? If the feature involves manual steps (for example CSV upload or manual configuration), do not frame it around speed, automation, or ease compared to competitors who do those things better. Instead, anchor to independence, consolidation, or removing a dependency. Misleading positioning in the brief carries through to all downstream content and sales conversations. Flag this directly if the risk exists.

**Messaging framework mapping**
Map the feature to the pillars of your company's messaging framework. Every feature maps to at least one pillar, and many sit mainly in one. Be honest: if a feature doesn't directly support a pillar, say so. Do not force a mapping that isn't real.

**Why does the customer care?**
Separate primary personas from secondary. For primary: list tangible outcomes only. For secondary: keep it brief. Use the canonical brief as a reference for format and level of detail.

**How is this different from before?**
What existed before? What changed? Was this a gap, a replacement, or an extension? If it's completely new with no predecessor, say so clearly.

**Known limitations and objections**
Ask: What does this NOT do that people might expect? What questions have come up in sales or customer conversations? What myths need debunking? This section prevents over-selling and prepares sales and CS.

**Real-world examples**
One scenario per primary persona minimum. Each scenario should be story-led: start with a real problem, build the narrative around it, end with a concrete outcome. Use implied scale (a consumer app, a large subscriber base) rather than invented specific numbers. Use narrative beats, not a numbered checklist of steps. Generic use cases are not acceptable. The scenario should feel like something that actually happened to a real team.

**Competitive comparison**
PMM territory. Before writing a single differentiation claim, run a web search to verify it. Never assume a capability is unique to your product without checking. Specifically:

- Search for each named competitor plus "AI analysis" or the relevant feature before claiming you're the only one with it
- Check if any named competitor is sunsetting or has been acquired: this creates displacement opportunities worth calling out explicitly
- Check whether competitors charge per send, per contact, or per response where pricing is a differentiator
- Flag anything that needs further verification before publishing

Only include claims that are verifiable and defensible. If uncertain, omit rather than guess.

---

## Avoiding Over-Technical Language

Feature briefs are read by PMMs, sales reps, and CS teams, not just engineers. When a PM uses technical language, help them translate it.

Examples:
- "Responses are embedded and clustered with a vector index" becomes "Similar feedback is grouped together automatically, so you see themes instead of a pile of comments"
- "We added webhook support with retry and backoff" becomes "Your other tools get new responses as soon as they arrive, even if a connection drops for a moment"
- "The export job is queued and processed asynchronously" becomes "Big exports run in the background, and we email you when they're ready"

Ask the PM: "How would you explain this to a sales rep who needs to demo it next week?" That framing usually unlocks the plain-language version.

---

## Flagging Conflicts with Existing Positioning

If something the person tells you conflicts with known company positioning (from your launch reference, ICP reference, or tone of voice guide), flag it directly. Do not silently work around it.

Example flags:
- "You mentioned [old feature name]. Our banned-terms list says that feature was retired. Do you mean something else, or should we avoid referencing it here?"
- "You've described this with a term we use carefully because it can imply reduced user control. Should we reframe this?"
- "This sounds like it's under Surveys, but you mentioned Feedback Library earlier. Let's clarify before going further."

Be direct but collaborative. The goal is accuracy, not to block progress.

---

## Handoff Between PM and PMM

When a PM has completed their sections and a PMM comes in to complete the rest:

1. Ask the PMM: "Has a PM already started a brief for this feature? If so, share the Notion link."
2. Fetch the existing page via the Notion connector using the page ID.
3. Review what's filled in and what's missing.
4. Work through every PMM-touch section in order, not just the blank ones. Even sections the PM has filled in need a PMM review pass for framing, tone, and positioning accuracy.

**Full PMM section checklist (go through every one of these, in order):**

1. Company-level positioning: validate feature placement and canonical name
2. Can we talk about it: add any marketing-specific conditions
3. Key features: check language translates from product truth to benefit framing
4. Who is this for: own and complete
5. Taglines: own and finalize, organized by persona
6. Pain points: own the framing, not just the content
7. Messaging framework mapping: validate the mapping is honest
8. Why customers care: own the outcome framing
9. Real-world examples: shape for marketing use
10. Known limitations and objections: add sales framing layer
11. Competitive comparison: own entirely

Never start from scratch if a brief already exists. Always check first.

---

## Copy and Tone Rules (Apply Across All Sections)

**Always:**
- US English spelling and grammar
- Active voice and contractions
- Outcome-focused language: what does the user walk away with?
- Problem-first framing: pain before solution
- Plain language over technical jargon

**Never:**
- Em dashes or en dashes (firm brand rule, no exceptions)
- Internal persona codenames in external-facing copy: use actual job titles
- Anything on your banned-terms list (retired product names, retired features). Keep that list in your project knowledge.
- Buzzwords that imply AI acts without the user's control
- Vague superlatives ("best-in-class", "next-gen", "powerful")
- Implying AI replaces human judgment. Always: AI assists, AI handles grunt work.

---

## Quick Reference: Who Does What

| Section | PM | PMM |
|---|---|---|
| Company-level positioning | Fills in product placement | Validates and refines |
| Release dates | Owns | N/A |
| Can we talk about it | Owns | Adds marketing conditions |
| Key features | Owns | Translates to benefit language |
| Who is this for | Contributes persona context | Owns: primary/secondary framing, caveats, supporting data |
| Taglines | Optional first pass | Owns and finalizes, organized by persona |
| Pain points mapping | Contributes context | Owns framing |
| Messaging framework mapping | Contributes | Owns |
| Why customers care | Contributes | Owns |
| Real-world examples | Provides raw scenarios | Shapes for marketing use |
| Objections and limitations | Owns (product truth) | Adds sales framing |
| Competitive comparison | Background knowledge | Owns, with mandatory verification |
