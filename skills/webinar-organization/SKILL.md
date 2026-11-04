---
name: webinar-organization
description: >-
  Walks anyone at Example Feedback (a fictional customer feedback platform) through running a partner
  webinar end-to-end, from kickoff through promotion, going live, and repurposing. Designed for people
  who've never run a webinar before so they don't forget anything. Use whenever someone mentions running,
  planning, organizing, or setting up a webinar with a partner, influencer, or external speaker. Triggers
  include "we're doing a webinar with X", "help me set up a webinar", "co-host with [partner]", "partner
  webinar", "co-marketing webinar", "webinar collaboration", "I've never run a webinar". Also use during
  execution: "what's left for the webinar", "did we forget anything", "how should we promote it", "what
  about post-webinar", "the webinar is next week". The skill figures out which stage the user is at, then
  walks them through what's needed, producing standard artifacts (brief doc, Linear project + tasks)
  along the way. Do NOT use for solo product webinars, internal team meetings, or sales demos.
---

# Webinar Organization

A skill for running a partner webinar end to end at Example Feedback, a fictional customer feedback platform. Designed so that someone who's never done one can follow it and not forget anything important.

All people, partner companies, numbers and quotes in this file are fictional. The team used throughout:

| Person | Role |
|---|---|
| Jordan Lee | CMO, usually the key POC and host |
| Sam Rivera | Content Marketing Manager, drives day-to-day |
| Alex Morgan | GTM Strategist, runs ads and outbound |
| Casey Nguyen | Lifecycle/email lead, runs segmentation and sendouts in Customer.io |
| Taylor Brooks | Designer |
| Morgan Patel | Video editor |

Replace them with your own team.

**What counts as a "partner webinar"**: any webinar Example Feedback co-hosts with someone external. That includes integration / product partners (like the Fabrikam webinar), but also influencers, industry experts, content creators, researchers: anyone we're running a webinar *with*, not just on our own. The workflow is the same; the framing shifts.

The canonical example is the Fabrikam webinar (Fabrikam is a fictional marketing automation platform with an integration into Example Feedback). Every template, task list, and checklist in this skill is modeled on that project.

**Webinar platform**: the examples use Contrast as the webinar platform (registration forms, registrant emails, studio, polls, recording export). If you use a different platform, swap the name throughout.

---

## How to use this skill

This is a **guided walkthrough**, not a single one-shot output. When the user invokes this skill, the first job is to figure out **what stage they're at** and start there. Don't dump the whole workflow on them.

The five stages:

1. **Kickoff**: partner just confirmed, nothing built yet
2. **Brief & Setup**: settling the details, building the landing page, getting visuals into production
3. **Promotion**: emails out, ads live, LinkedIn rolling
4. **Two Weeks Out**: slides finalized, dry run, polls, day-of prep (NOT the week of, this happens earlier)
5. **Post-webinar**: recording, repurposing, lead handoff

**First message: detect the stage.** Ask the user where they are if it's not obvious. Also ask if they want to cross-check their existing Linear project:

> "Got it, partner webinar. Two quick things:
> 1. Where are you right now: just kicking it off, brief stage, mid-promo, two weeks out, or post-webinar?
> 2. Do you already have a Linear project for this? If yes, I can cross-check it against the canonical task list to flag anything missing."

Then jump to the relevant stage section below. At the end of each stage, offer to move on to the next one, or stop if they only wanted help with the current stage.

The sections in this file:

- **Stage 1: Kickoff**: what to ask the user + partner upfront
- **Stage 2: Brief & Setup**: generate the brief, create the Linear project, flag blockers
- **Stage 3: Promotion**: channel mix, partner expectations
- **Stage 4: Two Weeks Out**: dry run, slides, polls
- **Stage 5: Post-webinar**: immediate-after + within-2-weeks tasks
- **The webinar brief structure** (full template for the .docx)
- **The canonical Linear task list** (all 29 tasks, organized by phase)
- **Working notes**: what to ask the partner, what goes wrong, standing bios, channel cheat-sheet, post-webinar Slack recap template
- **Cross-stage rules** (formatting, roles, platform standards)

---

## Stage 1: Kickoff

**Symptom**: "We're doing a webinar with [Partner]" / "Just got the go-ahead with [Partner]" / "Where do I start?"

### What needs to happen

The kickoff stage is about settling **what** the webinar is, not building any assets yet. The goal is to come out of this stage with enough clarity to fill in the brief.

### What to ask the user upfront

Ask in **one message**, accept partial answers. These are the essentials:

- **Partner name** (and what kind of partner: a company / product partner, an influencer, an industry expert, a content creator? This shapes the framing.)
- **Tentative topic** (1 sentence is fine)
- **Tentative date + time**, and remind them: timezone matters. The default slot is one that works for US East + EU late afternoon, e.g. 11 AM EDT / 5 PM CEST. Push them to commit to a specific Tue/Wed/Thu, not "sometime in October."
- **Speakers**: who from Example Feedback, who from partner side (names + roles if known, partner side may be TBD)
- **Target audience** (job titles + segment, e.g., "Lifecycle Marketers, CMOs, CX Leaders, B2B SaaS")
- **Primary KPI** (default: # of registrants; default target = 100 minimum)
- **POCs**:
  - **Key POC on the Example Feedback side**: always ask, never assume. Could be the CMO, the Content Marketing Manager, or someone else depending on who's leading this one. Also ask who else is involved (e.g. the GTM Strategist if ads will run, the lifecycle/email lead for email, etc.).
  - **Partner side**: primary contact + secondary

If they can't answer some of these, that's fine, mark them `[TBD]` in the brief later. The brief is partly a tool for surfacing what's not yet confirmed.

### What else to flag before moving on

Before generating the brief, scan the **Working Notes** section below, especially "What to ask the partner upfront." Surface 1 or 2 of the most important questions to the user that they may not have thought about, e.g.:

- "Has the partner committed to specific promo numbers, emails, segment size, channels? Vague intent here is where webinars underdeliver on registrants."
- "Do you have their speaker bio + headshot, or are you waiting on it? If waiting, get a hard deadline."
- **(If the partner is an integration / product partner)**: "What's the integration angle, is the integration the core value of the webinar, or is it backdrop?" Skip this one if the partner is an influencer, expert, or anyone non-product.

### Then offer to move to Stage 2

> "Got enough to start the brief. Want me to draft it now, or do you want to nail anything down with the partner first?"

---

## Stage 2: Brief & Setup

**Symptom**: User has the kickoff info and wants to start building. Or they say "let's make the brief" / "what assets do we need."

### Step 2a: Generate the brief (.docx)

Use the docx skill to generate a Word doc. **Before writing any code, read the docx skill's `SKILL.md`**.

Then use the **Brief structure** section below for the exact section-by-section template. It mirrors the Fabrikam brief:

1. Campaign Overview (channel, market, KPI, audience, ownership, angle)
2. Webinar Info (topic, date, sub-topic, format, learnings, promo quotes, speakers + bios, company info)
3. Promotion Channels (email, in-app, website, LinkedIn, both sides)
4. Assets (landing page + UTMs, email content, key visuals, brand assets)
5. Partner to-dos
6. Proposed Agenda

**Filename**: `Webinar_ExampleFeedback_X_[PartnerName].docx` (e.g. `Webinar_ExampleFeedback_X_Contoso.docx`).

**Where info is missing**, use `[TBD]` or `[Partner to confirm by X]`. Don't invent specifics, placeholders are useful because they show the user what's still pending.

**Standing bio for Jordan Lee**: in the Working Notes section below. Use that. Jordan is **CMO** at Example Feedback.

Save to `outputs/`, present the file.

### Step 2b: Create the Linear project + tasks

After the brief is presented, ask:

> "Brief is done. Want me to set up the Linear project and the standard task list? Or if you've already started a project, I can audit it against the canonical list to flag anything missing."

If creating: use `Linear:save_issue` for each task, with the project set to `[Webinar] [PartnerName]` under the Marketing team (`<YOUR_TEAM_KEY>`). See the **Canonical Linear task list** section below for the full task list with default assignees, labels, and parent/child relationships.

Create every task with **"No priority"**. These go in weeks ahead of time and the team assigns priority when they pick the work up. See the priority rule in the canonical task list section.

If auditing an existing project: call `Linear:list_projects` to find it, `Linear:list_issues` to get its tasks, compare against the canonical list, and report what's there / what's missing / what's done. Group by stage. Offer to create the missing ones.

### Step 2c: Flag the time-sensitive setup tasks

Some Stage 2 tasks are blocking, call them out:

- **Webinar details locked**: exact date, exact time (both timezones), final topic, confirmed speakers (both sides). Without these, nothing else can ship.
- **Webinar form (Contrast)**: needs to be set up before the landing page can embed it. **Assign Sam Rivera.** If the user (or Sam) doesn't know how to set up the form in Contrast, offer to fetch instructions / write up the setup steps.
- **Contrast email templates check**: review the auto-emails Contrast sends to registrants (confirmation, reminders, post-webinar). Make sure they're branded correctly and the copy reads well. **Assign Sam Rivera.** Easy to forget, big impact.
- **Landing page (Webflow)**: needs the form, plus partner speaker bio + headshot. If the partner is slow, ship the page with placeholders and update later. **Assign Sam Rivera.** If Sam doesn't know the Webflow setup steps, offer to fetch / write up instructions.
- **Headshots**: the designer (Taylor) can't start until the partner sends theirs. Get a hard deadline from the partner in writing.
- **Key visuals**: needed for email invite, ads, and homepage banner. **Assign Taylor Brooks.** Default formats: email header (horizontal), social square, social horizontal banner, social share image. **Ask the user**: any extra formats needed for this webinar specifically (e.g. Substack header, Slack community banner, partner-side format)?

Remind the user: the partner speaker's bio + headshot is the most common bottleneck. Get a hard deadline from them in writing.

### Then offer to move to Stage 3

> "Setup is in motion. Ready to think through promotion, or wait until visuals come back?"

---

## Stage 3: Promotion

**Symptom**: Brief done, Linear set up, ~3 to 4 weeks before webinar. Or user says "how do we promote this" / "what about the LinkedIn stuff."

### What needs to happen

**Example Feedback side** (default mix, adjust for partner specifics):

- **Emails**: no set number. Identify any relevant audiences (leads, customers, segment by title/persona), then ask **Casey Nguyen** for help with segmentation and sendout in Customer.io.
- **Homepage banner**: for 2 weeks pre-webinar. **Assign Sam Rivera.** If Sam doesn't know the setup steps, offer to fetch / write up instructions.
- **LinkedIn organic**: company page + speakers' profiles + personal brands of team members. **Assign Sam Rivera** for coordination; drafting happens via the `linkedin-content` skill.
- **LinkedIn on the partner page**: coordinate with partner to post on their company page.
- **LinkedIn paid ads**: **assign Alex Morgan (GTM).** Run 1 to 2 weeks before, typically 3 creative angles.
- **LinkedIn outbound**: **assign Alex Morgan.** Outbound DM sequence to target audience.
- **In-app banner** (optional): for customers in the final week. Only run if there's clear customer-segment value.

**Always ask the user**: "Any other promotion methods specific to this partner? (e.g. partner's podcast, their newsletter, joint Slack community, industry publication, etc.)" Every partnership has its own quirks.

**Partner side**: should ideally match our volume. Surface this if it hasn't been settled:

> "What has the partner committed to on promotion? Vague intent is where webinars underdeliver on registrants. Default expectation is at least an email + LinkedIn organic from their side."

### LinkedIn content: hand off, don't draft here

This skill **does not draft LinkedIn posts**. It lists them as Linear tasks and hands off to the `linkedin-content` skill for actual drafting.

When the user wants LinkedIn content:
> "For the actual LinkedIn posts (company page, speakers' profiles, personal brands), use the linkedin-content skill, it has the voice profiles and patterns. I'll just make sure the Linear task is there."

### Channel cheat-sheet

See the "Channel cheat-sheet" subsection of the Working Notes section below for the standard channel mix on our side, who owns each, and rough timing.

### Then offer to move to Stage 4

> "Promotion is rolling. Want to walk through prep for the webinar itself (this happens **two weeks out**, not the week of), or come back closer to the date?"

---

## Stage 4: Two Weeks Out

**Symptom**: ~2 weeks before the webinar. User says "we're live in two weeks" / "what about the slides" / "are we ready."

**IMPORTANT**: This stage is **two weeks before** the webinar, not the week of. If the user comes to you the week of, flag that they're behind on at least the dry run and slide finalization.

### What needs to happen

- **Slides (if applicable) + pitch finalized**: the Example Feedback speaker owns this. Should be done before the dry run.
- **Dry run with partner speaker**: around a week before the webinar. **Must happen in Contrast's studio**, not over Google Meet or Zoom. The point is for everyone to get familiar with the actual platform.
- **Slides graphics polish**: **assign Taylor Brooks (designer)** for a fast pass on the deck. This is the one point where raising the Linear priority is right: the task was created with No priority weeks ago, and now it genuinely is urgent. Suggest bumping it to Urgent and let the user confirm.
- **Polls set up in Contrast**: must be in the platform 24h before at the latest. Contrast needs them set up in advance.
- **Speaker Q&A primers**: moderators (usually Jordan or whoever's hosting) should have 3 to 5 backup questions ready in case the live Q&A is quiet.
- **Confirm partner is set**: final speaker confirmation, tech check, time zone double-check.

### What to remind the user

- "Have you done the dry run with the partner speaker, **in Contrast's studio**, not Google Meet? It should happen ~1 week before, not the morning of."
- "Are the polls set up in Contrast? They need to be in the platform 24h before."
- "Do you have backup Q&A questions in case the live Q&A is quiet?"

### Then offer to move to Stage 5

> "Once it runs, come back and I'll walk you through repurposing."

---

## Stage 5: Post-webinar

**Symptom**: The webinar happened. User says "it's done" / "what now" / "we need to repurpose this."

### What needs to happen IMMEDIATELY after (same day or next)

- **Disable the top website banner.** Easy to forget. The webinar is no longer upcoming.
- **Swap the landing page images to "on-demand" versions.** Taylor preps these immediately with all the key visual variants. Coordinate with Taylor the day of / morning after.
- **Pull the numbers and update the Webinar Numbers tracker** (in Google Drive). Landing page views come from Mixpanel; registrations come from Contrast. CTR = registrations / views. These numbers then anchor the Slack recap.
- **Prep a Slack recap post**: narrative recap to leadership + team channels. Vibe-led, benchmark-anchored numbers, recognizable company names from the registrant list, attendee quotes from the chat, specific shoutouts, what's next. The full structure + a worked example are in the **Working Notes** section below under "Post-webinar event summary." Read that before drafting.

### What needs to happen (within ~2 weeks of)

- **Lock the recording**: get the file into Drive within 24h, even if it's the raw export. Export from Contrast. The polished version can wait, the asset can't.
- **Short clip(s)**: 30 to 60s social clips from key moments. **Assign Sam Rivera.** This is the highest-leverage post-webinar deliverable, push for it.
- **Gated material** (optional): only if there's genuinely dense reusable content (e.g. tutorial-style demo from the partner speaker). Otherwise skip. Fabrikam's was canceled.
- **LinkedIn recap posts**: hand off to the `linkedin-content` skill, or **assign Sam Rivera** to draft.
- **Nurturing sequence**: email follow-up to registrants and attendees in Customer.io. **Assign Casey Nguyen.**
- **Lead passing to partner**: confirm format with them (CSV? Crossbeam sync? Direct integration?). Don't assume.

### Linear tasks for this stage

See the "Phase 5: Post-webinar" subsection in the Canonical Linear task list below. If those tasks weren't created at project setup, offer to create them now (still with No priority).

The same-day items above are the second point where bumping priority is fair, since the banner and the landing page images are actively wrong until someone fixes them. Offer to raise those two, leave the rest alone.

---

## Cross-stage rules

These apply everywhere in this skill:

- **The brief is always a `.docx`**, saved to `outputs/`, filename pattern `Webinar_ExampleFeedback_X_[PartnerName].docx`.
- **Default language is English**. Generate another language only if asked.
- **No em dashes in any output** (brief, Linear descriptions, LinkedIn task notes). This is a house content rule.
- **Use smart quotes** (`’` `“` `”`) in all generated content.
- **Never invent specifics**, partner contact emails, registration counts, partner speaker bios. Use `[TBD]` or `[Partner to confirm]`.
- **Roles**: Jordan Lee is **CMO**. Sam Rivera is **Content Marketing Manager**. Alex Morgan is GTM Strategist. Casey Nguyen handles lifecycle/email. Taylor Brooks is the designer. Morgan Patel is the video editor.
- **Every Linear task is created with "No priority"** (priority `0`). The list goes in weeks ahead of the webinar, so priority isn't ours to guess. The team sets it when they pick the work up. The only exceptions are deliberate bumps later on, flagged in Stage 4 and Stage 5.
- **LinkedIn drafting is handed off to `linkedin-content`**, not done here. This skill only ensures the task exists in Linear.
- **Visual design is handed off to Taylor** via Linear tasks. This skill doesn't generate images, just specifies what's needed.
- **Webinar platform = Contrast** (the current standard in this example). Forms, registrant emails, dry runs, and recording exports all happen there.

### What this skill does NOT do

- Solo product webinars (use a simpler workflow)
- Internal team meetings or sales demos
- Drafting LinkedIn content (use `linkedin-content`)
- Designing visuals (assigned to Taylor via Linear)
- Writing the slide deck itself (assigned to the Example Feedback speaker)
- Writing detailed landing page copy (separate doc, linked from the brief)
- Blog posts / written recaps (out of scope)

---

# Brief structure

This is the section-by-section template for the .docx brief, modeled on the Fabrikam webinar doc. Build the Word doc with these exact sections, in this order. Each section is a header followed by a table.

## Section 1: Campaign Overview

**Header (H1)**: `Campaign Overview`

**Table**: 2 columns, no headers (label column on left, value on right). 7 rows:

| Label | Value |
|---|---|
| **Campaign** | Webinar Partnership |
| **Communication channel** | *Slack* (or note partner channel) |
| **Market** | Global (EN): US + EU (adjust if different) |
| **KPI** | **Primary goal**: # leads from webinar (registrants). *Aiming at minimum 100 registrants* (adjust target) |
| **Target Audience** | [Job titles + segment, e.g.: Lifecycle Marketers, CMOs, CX Leaders, Growth, Product Managers. B2B & B2C SME & Mid-market companies] |
| **Ownership** | **Example Feedback Marketing:** Key POC: [name + email, always ask, do not assume]. Other roles involved: [Content Marketing Manager, GTM Strategist for ads, lifecycle/email lead, etc., list whoever is on this webinar]. **[Partner]:** Key POC: [name + email], Secondary: [name + email]. Crossbeam shared (if applicable) |
| **Communication Angle** | [1 or 2 sentence framing of what the webinar is really about and why it matters to the audience. For Fabrikam it was: "Practical webinar on using survey answers (zero-party data) in automations to improve customer engagement (based on the Fabrikam <> Example Feedback integration)"] |

## Section 2: Webinar Info

**Header (H1)**: `Webinar Info:`

**Table**: 3 columns: blank header / **Info** / **Actions**. Each row covers one piece of webinar info:

| | Info | Actions |
|---|---|---|
| **Webinar Topic** | [Working title, punchy, audience-facing. E.g. "Your Journeys Are Guessing: Put Survey Answers to Work"] | Decide on final topic + agenda with [Partner] |
| **Webinar date** | [Day, date, time in BOTH EDT and CEST, e.g. "Thu, Oct 8, 11 AM EDT / 5 PM CEST"] | Confirm the date with [Partner] |
| **Webinar sub-topic (explainer) H2** | [The landing page hook, 2 to 4 sentences. Should pose a question or claim, then say what attendees will see. Mention the integration if relevant.] | |
| **Webinar format** | [E.g. "45 min discussion/presentation with supporting slides (showcasing specific flows) + 15 min Q&A. Hosted by Example Feedback."] | |
| **Webinar: What you will learn** | [3 bullet points with a bold lead + an arrow + 1-sentence payoff. Example pattern: "**Why X only tells part of the story** → [payoff]"] | |
| **Webinar, quotes / highlights to use in promotion** | [1 or 2 stats or source-backed quotes the team can lift for ads, emails, posts. Include the source URL.] | |
| **Webinar speakers names** | **Host:** [Example Feedback speaker]. **Partner:** [Partner speaker] | |
| **Example Feedback Speaker photo + bio** | [Full bio paragraph, 3 to 5 sentences, ending with something humanizing. Default bio for Jordan is in Working Notes below.] | |
| **[Partner] Speaker + bio** | [Partner speaker bio + headshot link] | [Partner] please add |
| **Company info** | Example Feedback is a customer feedback platform that helps businesses collect, understand, and act on customer insights. | Add a few sentences (<5 sentences) about your company & product |

## Section 3: Promotion Channels

**Header (H1)**: `Promotion Channels:`

Two tables side by side conceptually (or one combined table). The Fabrikam brief had two, keep the same. Both are 3 columns: blank / **Example Feedback** / **Partner**.

**Table 3a: Pre-launch promotion scope** (optional, if it's worth listing intended segment sizes early):

| | Example Feedback | Partner |
|---|---|---|
| Email marketing | 1 email: Segment size [X]k (leads); 1 email: segment size [X]k (relevant customers) | 1 email: leads ([X]k) |
| In-app | Homepage banner for 2 weeks | |

**Table 3b: Detailed promotion plan**:

| | Example Feedback | [Partner] |
|---|---|---|
| Email marketing | Invite email sendout [date]. Follow up sendout. **Segment size:** [X]k ([describe segments, e.g. "[X]k marketer-persona customers + [X]k relevant leads/content followers"]) | Email promotion [cadence, e.g. "once a week before the webinar"]. **Segment size:** [X]k, [describe titles/segments] |
| Website | Homepage banner, *all EN-website users* | TBD: anon messaging, website banner |
| In-app | In-app for customers | TBD: in-app banners for specific titles, last week of promotion |
| LinkedIn | Organic: Post on company page ([doc link]). Posts on speakers' profiles ([doc link]). Posts on team personal brands ([doc link]) | Organic post on company page |
| Other (please add rows) | | |

## Section 4: Assets

**Header (H1)**: `Assets:`

**Table**: 3 columns: **Asset** / **To be created by / ETA** / **Details for partner**.

| Asset | To be created by / ETA | Details for partner |
|---|---|---|
| Webinar Landing Page with UTMs | **Example Feedback** [date, usually ~2 weeks before webinar] | [Landing page URL placeholder: `https://example.com/webinars/[slug]/`] |
| UTM links | **email** | `https://example.com/webinars/[slug]/?utm_source=partner&utm_medium=email&utm_campaign=[partner-slug]` |
| UTM links | **Social / LinkedIn** | `https://example.com/webinars/[slug]/?utm_source=partner&utm_medium=social&utm_campaign=[partner-slug]` |
| Email content to customers/leads | **Example Feedback** [date, ~2 weeks before] | [Link to email copy proposal Google Doc] |
| Key visuals: Horizontal banner, Square banner | **Example Feedback** [date, ~2 weeks before] | [Email header image link]. [Social share link]. [LinkedIn Square link] |
| Example Feedback Brand Assets / Logo | [LINK to drive folder] | |
| [Partner] logo link + brandbook if possible | | [Partner to provide] |

## Section 5: [Partner] to dos

**Header (H1)**: `[Partner] to dos:`

Bulleted list of what the partner needs to confirm/deliver:

- Confirm webinar topic & rough agenda & speakers with partner
- Confirm webinar date with partner
- Confirm the webinar format (depending on the speakers & final topics) with partner
- Confirm promotional channels ([Partner])
- Share speakers' bio + photo
- Content build-out session after speaker is confirmed + what slides we will want to bring together

Then a short follow-up line, `[Partner] to-dos:` (sub-header or bold), and a free-text line for the deadline e.g. "[Partner POC] to get: date confirmed, speaker confirmed, speaker headshot and bio hopefully by [day, date]"

## Section 6: Proposed Agenda

**Header (H1)**: `Proposed Agenda (45 min + 15 min Q&A)` (adjust totals if different)

A summary line:
- **10 min**: discussion
- **40 min**: deck
- **5 min**: quick overview of the Example Feedback <> [Partner] integration

Then sub-sections (H3) for each segment of the agenda. The Fabrikam structure was:

### Intro (5 min)
- Quick intro to speakers & Example Feedback + [Partner] (mention the integration, why we're here)
- Agenda covered (1 slide)
- **Polls**
- Question from [Host] to [Partner speaker]: [opening question that anchors the rest]

### 2. [Topic block 1] (~10 min)
- [Concept explained] → [who covers it]
- [Stats + trends]
- [Mini-showcase of integration]

### 3. Use cases (~15 min)
- Presenting most interesting use cases of [topic] + why should you care
- Showcase campaign examples (hyper-personalized journeys, onboarding, retention triggers)

### 4. AI-native features (~20 min)
- Example Feedback: [feature names]
- [Partner]: [feature names]

### 5. Live Q&A (~5 min)
- Address attendee challenges, scenarios, and implementation questions

## Formatting notes for the .docx

- Use **Heading 1** for the six section headers.
- Use **Heading 3** for agenda sub-sections (Intro, topic block, Use cases, AI features, Q&A).
- Tables: use the docx skill's table patterns (dual width, DXA, ShadingType.CLEAR, cell padding). Apply light shading (`D5E8F0` or similar) to label/header cells to mirror the source doc style.
- Use proper bullets via `LevelFormat.BULLET`, never unicode `•`.
- No em dashes anywhere in the body (house content rule). Use commas, parentheses, or full stops.
- Use smart quotes (`’` `“` `”`). The docx unpack tool handles this if generating via XML editing.
- Apostrophes: smart only (`Jordan’s` not `Jordan's`).
- Where the source doc has a hyperlink (e.g. landing page URL, doc links), include it as an actual hyperlink, not just blue text.

---

# Canonical Linear task list

Every task that should exist for a partner webinar, organized by phase. Based on the Fabrikam webinar Linear project (`[Webinar] Fabrikam`), updated with the current platform (Contrast) and current team roles.

**Project naming**: `[Webinar] [PartnerName]` (e.g. `[Webinar] Fabrikam`)
**Team**: Marketing (`<YOUR_TEAM_KEY>`)
**Default lead**: Sam Rivera (Content Marketing Manager) for day-to-day driving; Jordan Lee (CMO) for strategic decisions.

When creating in Linear, use `Linear:save_issue` with `project: "[Webinar] [PartnerName]"` and the team set to Marketing.

**Priority: always create these tasks with "No priority" (Linear priority `0`).**

This matters more than it sounds. The whole list gets created 4 to 6 weeks out, before anyone has decided what's actually urgent. Dropping 29 High-priority tasks into the Marketing team makes the board look like a crisis, trains people to ignore priority flags, and buries whatever genuinely is urgent that week. The team triages and assigns priority themselves once the work is live. Don't set priority on creation, don't infer it from the phase a task sits in, and don't offer to "helpfully" mark the early ones High.

Priority gets raised later, deliberately, by whoever owns the work. Two places in this skill call for that (slides graphics before the dry run, and the same-day post-webinar tasks) and both are escalations *after* creation, not creation defaults.

## Phase 1: Setup (4 to 6 weeks before)

### 1. Webinar form: Contrast setup
- **Default assignee**: Sam Rivera
- **Labels**: Operational
- **Description**: Set up the registration form in Contrast (the webinar platform). Configure iFrame for landing page embed, custom branding, GDPR/ToS settings.
- **Note**: If Sam doesn't have the Contrast setup steps written down, offer to fetch/write them up as part of this task.

### 2. Contrast email templates check
- **Default assignee**: Sam Rivera
- **Labels**: Operational
- **Description**: Review the auto-emails Contrast sends to registrants (confirmation, reminder 24h before, reminder 1h before, post-webinar thank you, on-demand follow-up). Make sure templates are branded, copy is on-voice, and partner is referenced correctly.
- **Note**: Easy to forget, big impact. Do this BEFORE promotion goes out.

### 3. Webinar landing page (Webflow)
- **Default assignee**: Sam Rivera
- **Labels**: Operational
- **Description**: Build the landing page in Webflow. Add final copy when components are ready. Slug pattern: `example.com/webinars/[topic-slug]-[partner-slug]-webinar/`. Embed the Contrast form. Page can ship with `[TBD]` placeholders for partner speaker bio/headshot if they're slow.
- **Note**: If Sam doesn't have the Webflow setup steps written down, offer to fetch/write them up as part of this task.

### 4. Webinar headshots
- **Default assignee**: Taylor Brooks (designer)
- **Parent**: Webinar landing page
- **Labels**: Design
- **Description**: Prepare headshots in landing page format for both speakers (Example Feedback + partner). Partner needs to send their speaker headshot before this can start. Block until received.

## Phase 2: Visuals (3 to 4 weeks before)

### 5. Key visuals
- **Default assignee**: Taylor Brooks
- **Labels**: Design
- **Description**: Required formats:
  1. Email header image (horizontal banner)
  2. Social image: square
  3. Social image: horizontal banner
  4. Social share image (for landing page)
- **Ask user**: any additional formats needed (Substack header, Slack community banner, partner-side format, etc.)?
- Reference info for designer: H1 (webinar title), logos (Example Feedback + partner), tag (Live Webinar), date info in both timezones, speakers.

### 6. Design ads
- **Default assignee**: Taylor Brooks
- **Parent**: LinkedIn paid ads
- **Labels**: Design
- **Description**: 3 ad creatives:
  1. Default: webinar topic + speakers (standard format)
  2. Big-headline version of the campaign hook ("[Question / claim from sub-topic] CTA: Join our webinar | Example Feedback + [Partner]")
  3. Stat-led version using the headline quote from the brief (Section 2 of the brief)
- Briefs live in Figma. Link from the issue.

### 7. Slides graphics
- **Default assignee**: Taylor Brooks
- **Labels**: Design
- **Description**: Link to the working deck. Designer uplifts slides, both flagged ones and any others worth polishing. Deadline = before dry run.

### 8. Homepage banner
- **Default assignee**: Sam Rivera
- **Labels**: Lead Gen
- **Description**: Add to homepage by [date, usually ~2 weeks before webinar]. Link to brief. Remove immediately after the webinar (see Post-webinar tasks).
- **Note**: If Sam doesn't have the homepage banner setup steps written down, offer to fetch/write them up.

### 9. Resources banner
- **Default assignee**: Taylor Brooks
- **Parent**: Homepage banner (optional)
- **Labels**: Design
- **Description**: Smaller version of the social/horizontal banner, sized for the website resources area.

## Phase 3: Promotion (2 to 3 weeks before through webinar day)

### 10. Email campaigns
- **Default assignee**: Casey Nguyen
- **Labels**: Email marketing
- **Description**: Set up email invite + follow-up in Customer.io. Segment by relevant audiences (leads + customers, filtered by title/persona). No set number of emails, driven by audience size and relevance. Coordinate sendout timing with the partner's email schedule.

### 11. LinkedIn paid ads
- **Default assignee**: Alex Morgan
- **Labels**: Lead Gen
- **Description**: Launch LI ads 1 to 2 weeks before webinar, depending on the partner's email sendout date. Three creative angles (see Design ads task).

### 12. LinkedIn outbound
- **Default assignee**: Alex Morgan
- **Labels**: Lead Gen
- **Description**: Outbound DM sequence to target audience on LinkedIn. Coordinate with paid ads timing, typically starts 1 to 2 weeks before webinar.

### 13. Organic promo: social media (all voices)
- **Default assignee**: Sam Rivera
- **Description**: Posts to schedule on:
  - Example Feedback company page
  - Speakers' profiles (both Example Feedback + partner if they'll post)
  - Team personal brands (4 to 6 team members)
- LinkedIn posts Google Doc has three tabs: company / speakers / personal brands.
- **Hand-off**: drafting handled via the `linkedin-content` skill, not this one. This task is just the coordination.

### 14. LinkedIn on partner page
- **Default assignee**: Sam Rivera (coordinator); execution by partner
- **Description**: Coordinate with partner to post about the webinar on their company LinkedIn page. Provide them with copy + visual if helpful.

### 15. In-app invite (optional)
- **Default assignee**: Sam Rivera
- **Labels**: Lead Gen
- **Description**: In-app message inviting customers. Usually 1 week before webinar. **Note**: this was canceled for Fabrikam. Only run if there's clear customer-segment value.

### 16. Partner-specific promotion channels
- **Default assignee**: Sam Rivera (varies)
- **Description**: Catch-all for any promotion methods specific to this partner: their podcast, newsletter, joint Slack community, industry publication appearance, etc. Created during Stage 3 after asking the user "any other channels specific to this partner?"

## Phase 4: Two weeks out (slides + dry run)

### 17. Slides + pitch finalized
- **Default assignee**: Example Feedback speaker (usually Jordan Lee or whoever is hosting)
- **Description**: Build the deck, finalize order, polls, and Q&A primers. Done BEFORE dry run.

### 18. Dry run with partner speaker
- **Default assignee**: Example Feedback speaker + Sam Rivera (coordinator)
- **Description**: ~1 week before webinar. **Must happen in Contrast's studio**, not Google Meet/Zoom. Speakers get familiar with the platform interface, audio/video tested, transitions practiced.

### 19. Polls set up in Contrast
- **Default assignee**: Sam Rivera
- **Description**: Configure polls in Contrast at least 24h before the webinar. Polls are part of the Intro section per the standard agenda.

## Phase 5: Post-webinar

### Immediately after (same day or next):

### 20. Disable top website banner
- **Default assignee**: Sam Rivera
- **Description**: Remove the webinar banner from the homepage. Webinar is no longer upcoming.

### 21. Swap landing page images to on-demand
- **Default assignee**: Sam Rivera (with Taylor for assets)
- **Description**: Taylor preps "on-demand" versions of all key visuals immediately after the webinar. Sam swaps them on the landing page so the page now markets the recording instead of a live event.

### 22. Pull metrics + update the Webinar Numbers tracker
- **Default assignee**: Sam Rivera
- **Description**: Update the **Webinar Numbers** tracker doc in Google Drive with this webinar's performance. Pull:
  - **Landing page views** from Mixpanel
  - **Registrations** from Contrast
  - Calculate landing page CTR (registrations / views)
- Use these numbers to anchor the Slack recap (benchmark against past webinars in the same doc).

### 23. Prep event summary (Slack)
- **Default assignee**: Sam Rivera
- **Description**: Post a recap in Slack (leadership channel + team channel). This is a narrative post: vibe + benchmark-anchored numbers + recognizable company names from the registrant list + attendee quotes + shoutouts + what's next. NOT a sterile metrics report. See the Working Notes section below for the full structure + a worked example from the "Feedback at the Speed of AI" webinar.

### Within ~2 weeks:

### 24. Lock the recording
- **Default assignee**: Sam Rivera
- **Description**: Export the recording from Contrast and upload to Drive within 24h of the webinar. Raw export is fine initially, the polished version can wait.

### 25. Short clip(s) for social
- **Default assignee**: Sam Rivera (Morgan Patel as editor when needed)
- **Description**: 30 to 60s clip showing a key moment. Rough cut from full recording → polished clip. **Highest-leverage post-webinar deliverable.**

### 26. Gated material (optional)
- **Default assignee**: Sam Rivera
- **Labels**: Lead Gen
- **Description**: Treat partner speaker's deep-dive (if relevant) as gated material. Separate landing page / form, tutorial delivery flow.
- **Note**: Fabrikam's version was eventually canceled. Only create if there's clearly something dense and reusable worth gating.

### 27. LinkedIn recap posts
- **Default assignee**: Sam Rivera
- **Description**: Post-webinar recap content on LinkedIn. **Hand off drafting to `linkedin-content` skill.**

### 28. Nurturing sequence
- **Default assignee**: Casey Nguyen
- **Labels**: Lead Gen
- **Description**: Email nurturing sequence for webinar registrants & attendees in Customer.io.

### 29. Leads passing to partner
- **Default assignee**: Sam Rivera (with Jordan Lee if needed)
- **Labels**: Lead Gen
- **Description**: Pass registrant data to partner. Confirm format with them (CSV? Crossbeam sync? Direct integration?). Don't assume.

## Auditing an existing project

When asked to audit a project, walk through this list and report:

- ✅ **Present and Done**: task exists, completed
- 🟡 **Present, in progress**: task exists, not yet done
- ❌ **Missing**: no equivalent task in the project

Group findings by phase, and at the end ask if the user wants the missing ones created.

For **canceled** tasks (like in-app invite or gated material in the Fabrikam case), don't flag as missing, list them as "consciously skipped" if the user is doing the same.

## Task creation order

When creating from scratch, create in this order so parent/child links work. All of them go in with **No priority**, including the post-webinar ones.

1. Webinar form (Contrast)
2. Contrast email templates check
3. Webinar landing page (Webflow)
4. Headshots, parent: landing page
5. Key visuals
6. Homepage banner
7. LinkedIn paid ads
8. Design ads, parent: LinkedIn paid ads
9. Resources banner, parent: Homepage banner (optional)
10. Email campaigns
11. LinkedIn outbound
12. Organic promo (social media)
13. LinkedIn on partner page
14. Slides graphics
15. Slides + pitch finalized
16. Dry run
17. Polls setup
18. (Optional) In-app invite
19. (Optional) Partner-specific channels
20. Disable top banner (post-webinar)
21. Swap landing page images (post-webinar)
22. Pull metrics + update the Webinar Numbers tracker (post-webinar)
23. Prep event summary Slack post (post-webinar)
24. Lock the recording (post-webinar)
25. Short clip(s) (post-webinar)
26. (Optional) Gated material (post-webinar)
27. LinkedIn recap posts (post-webinar)
28. Nurturing sequence (post-webinar)
29. Leads passing (post-webinar)

---

# Working Notes

Personal notes for running a partner webinar. The institutional knowledge that doesn't fit in a brief or a task list: what to ask the partner upfront, what tends to go wrong, what to keep in mind at each stage.

**This is a living section.** Add/edit anything that's missing or off. It should grow each time we run a new partner webinar.

## What to ask the partner upfront (kickoff call)

These are the things that need to be settled in the first 1 or 2 conversations. If they're not, the brief stalls.

- **Date: exact slot in BOTH timezones.** The default is a slot that works for US East + EU late afternoon (e.g. 11 AM EDT / 5 PM CEST). Don't accept "sometime in October", push for a specific Tue/Wed/Thu.
- **Their speaker: name + role + bio + headshot.** Bio should be 3 to 5 sentences with at least one humanizing detail. Get this in writing; don't accept "we'll figure it out." The Fabrikam brief had a clear "Robin to confirm by [date]" hard deadline, do the same.
- **Their promotion commitment.** Get specifics, not vague intent. Ask: how many emails, what segment size, when, will they do website banner / in-app / LinkedIn organic / LinkedIn on their company page. The Fabrikam brief had the partner committing to a [X]k email segment + website banner + in-app for specific titles + LinkedIn organic. If they can't commit to numbers, you can't forecast registrants.
- **Their POC + secondary POC.** Always get two contacts on their side. The primary will go on vacation. Crossbeam is shared.
- **What they want from the framing.** What's the angle and why does the audience care? If it's an integration / product partner, ask whether the integration is the *core value* of the webinar or just backdrop (for Fabrikam it was backdrop; zero-party data was the actual topic). If it's an influencer or expert, ask what *their* angle is: what's the take they want to push, what's their hook with their own audience. Different partners want different things.
- **Any partner-specific promotion channels.** Some partners have podcasts, newsletters, Slack communities, industry pubs. Ask explicitly. Don't assume LinkedIn + email is everything.


## What tends to go wrong

- **Partner speaker bio + headshot lands late.** Build a hard internal deadline for "if we don't have this by [day], we go live on the landing page with a placeholder." Don't let it block the page.
- **Two emails from us, one from them.** We usually overdeliver on promotion. Be upfront that we expect their email volume to be in the same ballpark, or registrants come 80/20 from our side.
- **The "what you will learn" bullets sound generic.** Push back hard on this in the brief stage. The Fabrikam ones worked because each bullet had a *specific* claim ("Why usage data only tells part of the story") + a payoff. Vague bullets ("Learn about feedback automation") don't drive registrations.
- **The agenda gets too dense.** 45 min runs short when there are two speakers. Build in poll time, build in transition time. The Fabrikam agenda was 10 min discussion + 40 min deck + 5 min integration overview + 15 min Q&A, but in practice the discussion + deck overlap, so don't pad the deck content beyond ~30 min of actual material.
- **The stat in the promo quote dates badly.** The Fabrikam brief used an industry stat from the previous year, fine at the time, but make sure the year is plausible vs. the webinar date. Don't reuse old stats from previous webinars without rechecking.
- **Contrast emails get forgotten.** The platform sends auto-emails (confirmation, reminders, post-webinar). Check the templates before promotion goes out. Generic platform copy reflects badly on the brand.
- **Dry run done on the wrong platform.** Always run the dry run **in Contrast's studio**, not on Google Meet or Zoom. Speakers need to be familiar with the actual interface, not just the topic.


## Things to keep in mind at each stage

### Brief stage
- The brief is also a tool for surfacing what's *not yet decided*. Mark every unconfirmed item as `[TBD]` or `[Partner to confirm by X]`, don't fudge it.
- The standard ownership trio: **CMO Jordan Lee** as key POC, **Content Marketing Manager Sam Rivera** driving day-to-day, **GTM Strategist Alex Morgan** for ads + outbound.
- The "Communication Angle" row is the most important, it's the one-line framing that everything else (landing page H1, ad copy, email subject, LinkedIn posts) flows from. Spend time on it.

### Setup stage
- The Contrast form blocks the landing page, set it up first.
- Check Contrast auto-emails (confirmation, reminders) BEFORE promotion goes out. Cheap fix, big impact on perceived professionalism.
- Landing page lives in Webflow. Page can ship with `[TBD]` placeholders for partner speaker bio/headshot. Update when they land.
- Key visuals: confirm formats needed beyond the defaults (email header, social square, social horizontal, social share). Some webinars need a Substack header, partner-side banner, Slack community image, etc.

### Promotion stage
- Default promo stack on our side:
  - Emails (no set number, segment by relevant audiences with Casey Nguyen's help)
  - Homepage banner for 2 weeks
  - LinkedIn organic: company page + speakers' profiles + personal brands
  - LinkedIn on partner's company page (coordinate with them)
  - LinkedIn paid ads (Alex)
  - LinkedIn outbound (Alex)
  - Optional in-app banner for customers in final week
- The LinkedIn organic content has its own Google Doc with three tabs: company page / speakers / personal brands. Link this from the Linear task.
- Personal brand posts should come from each team member's voice. Use the `linkedin-content` skill for those.
- Always ask: "any other promotion channels specific to this partner?"

### Two-weeks-out stage
- Dry run **in Contrast studio**, not Google Meet. Non-negotiable.
- Polls in Contrast: have them ready 24h before the webinar at the latest.
- Slide graphics get bumped to "Urgent" in Linear in the two weeks before, not at creation. Taylor needs that signal to land when it's real, which only works if the rest of the board isn't already flagged.

### Post-webinar stage
- **Same day or next day**: disable the top website banner, swap landing page images to on-demand versions (Taylor preps these with all key visual variants), pull metrics + update the **Webinar Numbers** tracker in Google Drive (LP views from Mixpanel, registrations from Contrast, CTR = registrations / views), prep an event summary Slack post for leadership + team.
- The event summary template lives in this file (see section below). It explicitly benchmarks against past webinars, that's why updating the **Webinar Numbers** tracker has to happen first.
- Recording: get the file in Drive within 24h of the webinar, even if it's the raw Contrast export. The full Material Repurposing task can wait but the asset needs to be locked.
- The short clip is the highest-leverage post-webinar deliverable. 30 to 60s, sped up if needed, focused on one moment. Sam Rivera owns this (with Morgan Patel as editor when needed).
- Gated material from the partner speaker is *only worth doing* if there's something genuinely dense and reusable (a tutorial-style deep dive). Otherwise skip it. Fabrikam's was eventually canceled.
- Lead passing to the partner: confirm the format with them (CSV? Crossbeam sync? Direct integration?). Don't assume.


## Standing bios

Pre-written bios for recurring speakers, ready to drop into the brief. Update here when bios change. (The bio below is fictional. Replace it with your own speakers' bios.)

### Jordan Lee: CMO
> Jordan Lee is the CMO at Example Feedback, where they lead go-to-market strategy and growth. Jordan has run marketing for consumer apps and B2B SaaS companies, from early-stage startups to global brands. With a background in lifecycle marketing and customer research, Jordan pairs data-first thinking with automation-focused execution. Outside Example Feedback, Jordan mentors early-stage founders on go-to-market. A weekend trail runner, parent of two, and long-time advocate of remote-first teams.

## Channel cheat-sheet (our side)

What we typically commit to. The Fabrikam webinar is the anchor; adjust per partner.

| Channel | Default scope | Owner |
|---|---|---|
| Emails | No set number. Segment by relevant audiences (leads + customers, by title/persona) | Casey Nguyen (for segmentation + sendout in Customer.io) |
| Homepage banner | 2 weeks pre-webinar, all EN-website users | Sam Rivera (Web team if Sam needs help) |
| LinkedIn organic: company page | 2 or 3 posts in run-up week | Sam Rivera (drafting via `linkedin-content`) |
| LinkedIn organic: speakers' profiles | 1 or 2 posts each | Sam Rivera + speaker review |
| LinkedIn organic: personal brands | 1 post each from 4 to 6 team members | Sam Rivera (drafting via `linkedin-content`) |
| LinkedIn on partner page | Coordinate with partner | Partner-side, Sam Rivera coordinates |
| LinkedIn paid ads | 1 to 2 weeks before, 3 creatives | Alex Morgan (GTM) |
| LinkedIn outbound | DM sequence to target audience | Alex Morgan |
| In-app banner | Customers, final week (optional) | Sam Rivera |


## Post-webinar event summary (Slack message to leadership + team)

Right after the webinar, post a recap in Slack. This is NOT a sterile metrics report. It's a narrative recap that mixes numbers with what actually happened in the room, who deserves credit, and what's next.

### Structure (in order)

1. **Title in square brackets** with the format `[Webinar name: short recap]`, e.g. `[Feedback at the Speed of AI: webinar with Dana recap]`
2. **Opening line of vibe**: one sentence on how it went overall. Don't bury the lede. ("We're post webinar now and…it went so so well!")
3. **Topline benchmark**: call out one or two metrics that *matter in context*, comparing to past webinars. Don't just list numbers, frame them. ("31% landing page conversion rate. Our recent Product webinar hit 12%. Our email-tool comparison series ran between 5% and 11%. This is the strongest LP CR we've put up on a webinar.")
4. **Registration + live attendee numbers**, plus a **taste of who actually signed up**: drop 15 to 25 recognizable company names from the registrant list, link to the full sheet. This is what makes leadership care.
5. **Shoutouts**: name the speakers and call out specifically what each of them did well. Be generous. Add ad-libbed thanks for the rest of the team (slide design, behind-the-scenes prep).
6. **Moments from the chat / live event**: 2 to 4 direct quotes from attendees, with names + companies. Quote them in *their* words. Add a sentence after each on why it landed.
7. **DMs / extra signals**: if anyone DM'd a team member after the session, share that too.
8. **What's next**: bullets:
   - Nurturing campaign (who's running it)
   - Repurposing plan (clips, recap posts, on-demand)
   - Anything coming with the speaker after (extra video, ad spot, follow-up content)
9. **Sign-off**: short thanks to the team. Warm, not corporate.

### Reference example (Feedback at the Speed of AI, fictional)

Everything in this example (people, companies, quotes, numbers) is made up to show the shape of a good recap.

> [Feedback at the Speed of AI: webinar with Dana recap] We're post webinar now and...it went so so well! Easily the most engaged audience we've had on a webinar so far (I actually had to download the chat history to go through it properly), and our highest-converting webinar landing page by a wide margin.
> The topic and bringing in Dana landed exactly the way we hoped.
>
> - 31% landing page conversion rate. Our recent Product webinar hit 12%. Our email-tool comparison series ran between 5% and 11%. This is the strongest LP CR we've put up on a webinar.
> - 180 people registered, over 55 watched live
>
> Who actually signed up? A taste of the companies in the registrant list: Contoso, Northwind Traders, Fabrikam, Adventure Works, Tailspin Toys, Wingtip Toys, Woodgrove Bank, Litware, Proseware, Alpine Ski House, Coho Winery, Lucerne Publishing, Margie's Travel, Blue Yonder Airlines, Wide World Importers, Fourth Coffee, Trey Research, VanArsdel, [and more](link)...
>
> Dana and @Casey Nguyen were both incredible. Dana brought the substance and the trust, Casey drove the conversation forward and ran a really clean live demo of the new Research Projects! Big kudos to both. But I'm biased, so especially big kudos to @Casey Nguyen, you were so well prepared!!
>
> And the audience showed up too. A few moments from the chat worth pulling out:
>
> "We finally stopped losing interview notes in random docs. Having one place to ask questions changed how often people actually look." Priya (Proseware)
> Priya is currently stitching this together by hand with a shared doc and a chatbot: "it's the only way I've gotten the wider team to read research at all."
>
> "I treat AI output like a first draft from a new hire. Useful, fast, and always worth a second look." Marco (Trey Research)
> Best framing of the AI trust problem I've seen in a webinar chat. Stealing this.
>
> "Long transcripts are where the summaries fall apart." Lena (Litware)
> Lena flagged the exact pain point Casey went on to explain in the demo. Felt like the audience writing the script for us.
>
> And a DM that came in to @Jamie Ortiz after the session:
> "Hi Jamie, great session today. Really useful to hear how other teams handle this. Keen to try the product." Chris (Wingtip Toys)
>
> What's next?
> - @Casey Nguyen is sending out the nurturing campaign for the 180 registrants.
> - I'm repurposing the session into (hopefully) a lot of content. Attaching some immediate clips that caught our attention.
> - More with Dana: a video of her actually testing Research Projects, plus the thought-leadership ad we've got lined up.
>
> Thank you to everyone who worked hard on this, it took quite a bit of our time, but it was so worth it

### Things to keep in mind when writing this

- **Don't lead with the deck of metrics.** Lead with vibe, then a single benchmark-anchored number. Save the rest for later in the post.
- **Always benchmark against past webinars.** Naked numbers don't land. "31%" means nothing on its own; "31% vs. our usual 5 to 11%" tells the story.
- **The company-name list does real work.** It signals to leadership that we're reaching the right audience without you having to argue the point. Pull 15 to 25 names from the registrant list, prioritize recognizable ones.
