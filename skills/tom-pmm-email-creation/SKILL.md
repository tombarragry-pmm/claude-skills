---
name: tom-pmm-email-creation
description: Generate copy, graphics, and Customer.io drafts for all broadcast and campaign emails for Example Feedback (a fictional customer feedback platform), including monthly product updates, product launch announcements, webinar invites, event invites, and onboarding emails. Use this skill whenever someone asks to write, draft, or plan any email for the product, whether it's a one-time broadcast or a multi-step campaign. Trigger when someone mentions email type (product update, webinar, event, onboarding), audience segments, feature sections, email graphics, UI mockups for email, or Customer.io template creation. Trigger even for vague requests like "help me write this month's product update", "I want to announce a webinar", "draft an onboarding email", or "send something to our trial users". Always use this skill before writing any product email of any kind.
---

# Product Email Skill

This skill helps a marketing team write copy, produce graphics, and build emails directly in Customer.io for product updates, webinar invites, event invites, and onboarding campaigns. The examples use Example Feedback, a fictional customer feedback platform. Replace the product names, URLs and colors with your own.

**Always chat-first.** All copy is drafted and approved in conversation before graphics are produced or anything is built in Customer.io. Never jump straight to tools.

---

## Step 1: Intake

Ask for anything not already provided:

1. **Email type:** product update (monthly or special edition), webinar invite, event invite, or onboarding email
2. **Broadcast or campaign?** A one-time send to a list (broadcast/newsletter in Customer.io) or a triggered sequence (campaign)?
3. **Audience:** active customers, trial users, prospects, attendees, or a mix (affects CTA framing and tone)
4. **Key content:** feature names, webinar/event details, sequence goal, or whatever is relevant to the type
5. **Anything unusual:** personal sign-off, embedded survey, co-host/speaker, special tone

If the user provides context upfront, extract what you can and only ask for what's missing.

---

## Step 2: Draft copy (in conversation)

Follow the structure for the chosen email type below. Get copy approval before moving to graphics or Customer.io.

---

### 2A: Product Update Email

#### Standard Monthly Recap

**Hero section**
- Accent pill label: `Monthly Product Update`
- H1: `[Month] Recap`
- Subheadline: short, benefit-led. Default: *"This month's new features, built to help you hear customers sooner and act faster"*. Vary this when content warrants it.

**Feature sections** (one per feature, repeat the pattern)
- Category pill: short label for the feature area (e.g. "New Integration", "AI Insights Update")
- H2: punchy headline, 6 to 10 words. Use accent-colored `<span>` highlights on 1 or 2 key words for emphasis. Mix sentence structures: questions, statements, commands.
- Body copy: 1 or 2 sentences max. Lead with the user problem or outcome, not the feature name. Plain, direct language.
- CTA link: action-oriented, lowercase arrow style, e.g. `Connect your help desk tickets →`

**irl: examples section** (2 examples per email, one per feature if 2 features)
- Section header: `irl: examples` (large, bold)
- Definition line: *adverb: when Example Feedback features change how you **collect**, **understand** and **act** on feedback.*
- Each example:
  - Category pill: feature name
  - Pull quote headline: a realistic (made-up) user quote in quotation marks, e.g. `"We fixed it before the next sprint"`
  - 3 bullet points: a mini workflow showing the before → action → outcome
  - Small CTA link

**Pinned insights** (gray card, optional: ask if there are resources to include)
- 2 or 3 content items (best practice guide, video tutorial, webinar, etc.)
- Each: pill label + title + 1-line description + CTA link

**Feedback board banner** (accent color, always included)
- Fixed copy: `See, vote, and suggest new Example Feedback features`
- CTA: `Visit the feedback board →` → `https://example.com/feedback-board`

**Footer** (always included)
- Logo + tagline: *Every customer voice, in one place.*
- `Log back in to try these new features` → `https://app.example.com`
- Unsubscribe / manage preferences (Customer.io liquid tags)

---

#### Special Edition Emails

Use when: product launch teasers, year-end recaps, major announcements, or any email that breaks the monthly cadence.

**Rules for special editions:**
- Drop the standard feature section structure entirely
- Lead with a single bold story or hook. Make the pill label reflect the occasion (e.g. `Coming Soon`, `2026 Product Recap`)
- H1 can be more expressive and creative: numbers, humor, and personality are welcome
- Use 2 or 3 "examples" or use-case stories instead of feature sections
- Can include a personal sign-off from the sender (photo + name + title)
- Can embed a survey directly in the email body
- Webinar CTAs and GIF/demo previews are encouraged

---

### 2B: Webinar Invite Email

Use for: any email promoting a live webinar or online event.

**Tone:** Personal, conversational, slightly provocative. Reads like it came from a person, not a marketing team.

**Sender:** Always from a named person (usually the marketer who owns the webinar). Include a photo sign-off.

**Structure:**
- **Subject line:** `[Webinar] Speaker Name. Short Topic Phrase. Date.` For example: `[Webinar] Jordan Lee. Feedback Without the Busywork. May 6.`
- **Preheader:** Tease the value of attending: what the reader will take away or why this matters now
- **Banner image:** Linked to the webinar registration page. Full-width, visually captures the speaker/topic.
- **Hook copy:** 2 or 3 short, punchy lines that set up the tension or problem. No fluff, no "we're excited to announce". Start with something the reader will feel.
- **Bold statement:** One sentence in `**bold**` that lands the core tension or challenge
- **Event details:** Speaker + co-host if applicable → date → time (include PT / ET / CET) → what they'll cover (2 or 3 bullets or a short paragraph)
- **Primary CTA:** `Register Now`. Prominent, single, linked to the registration page
- **Personal sign-off:** Photo of sender + name + title (e.g. *[Sender name], [Title] @ Example Feedback*)
- **Footer:** Standard Customer.io liquid unsubscribe block (conditional on subscription cycle)

**Rules:**
- No pills, no feature sections, no product UI: just story and CTA
- Never say "we're excited to" or "thrilled to announce"
- The hook should create mild tension or curiosity, not just summarize what the webinar is about
- One CTA only. Don't add secondary links that dilute the register action.

---

### 2C: Event Invite Email

Use for: in-person events, conferences, meetups, sponsored sessions, or any live event the company is hosting or attending.

**Tone:** Warm, clear, personal. If the company is sponsoring a major event, it can be slightly more elevated, but never cold or corporate.

**Sender:** Named person. Include sign-off.

**Structure:**
- **Subject line:** Lead with the event name or a benefit, e.g. `Meet us at [Event Name]` or `[Event] Come find us at [Venue/City]`
- **Preheader:** What the reader can do or get by showing up
- **Banner image or hero block:** Event name, date, location, company presence (booth/session/etc.)
- **Opening line:** Why the company is there, in one sentence. What's happening that makes this worth stopping by.
- **What to expect:** 2 or 3 bullets on what the reader can do (attend a talk, book a demo, grab swag, meet the team)
- **Date + location block:** Bold and clearly visible: city, venue, booth/room number if known
- **CTA:** Specific action: `Book a time to meet us →` / `Register for our session →` / `Add it to your calendar →`
- **Personal sign-off:** Name + title
- **Footer:** Standard unsubscribe block

**Rules:**
- Logistics must be unmissable: date, location, and how to find the team should be scannable in 5 seconds
- If there's a limited slot (demo booking, session seat), create urgency without being pushy
- Keep body copy short. This is an orientation email, not a content email

---

### 2D: Onboarding Email

Use for: any triggered or manual sequence sent to new users, trial users, or newly activated accounts.

**Tone:** Plain text. Personal. Like a real person is following up, because they are.

**Sender:** Named person, usually a CS rep or the person who owns the relationship.

**Type:** This is almost always a **campaign** (triggered), not a broadcast. Confirm with the user.

**Structure per email in the sequence:**
- **Subject line:** Short, specific, no clickbait. References the user's situation or a single goal. e.g. `Getting started with surveys` / `One thing to try this week`
- **Preheader:** Extends the subject and adds one more layer of context
- **Opening:** Acknowledge where the user is (just signed up, been active X days, completed a step, etc.)
- **Single goal per email:** One thing to do, one idea to explore, or one feature to try. Don't stack goals
- **Body:** 2 or 3 short paragraphs max. Problem → why it matters → what to do next
- **CTA:** One link. Specific and action-oriented: `Set up your first survey →` / `See your first insight →`
- **Sign-off:** Name only. No photo needed in plain text

**Sequence planning:**
- Ask how many emails in the sequence and the send cadence (e.g. Day 0, Day 3, Day 7)
- Each email in the sequence should have a distinct goal. Don't repeat the same value prop twice
- Avoid covering everything. Onboarding sequences that try to do too much fail

**Rules:**
- Plain text format always: no banners, no pills, no feature cards
- Never start with "Welcome to [Product]!" because it reads like a template
- Don't make the user feel behind. Frame guidance as opportunity, not correction
- If this is a campaign, clarify the trigger event (e.g. signup, trial activation, first survey created)

---

## Step 3: Graphics

*Only applies to product update emails and special editions. Webinar/event/onboarding emails don't use custom graphics. Use banner images or no images.*

After copy is approved, produce graphics for each feature section. One graphic per feature.

#### Choosing the graphic type

**Use UI close-up** when:
- A product screenshot is available
- The feature is best understood by seeing the actual UI
- The feature is a settings panel, toggle, form, or data view

**Use illustrative explainer** when:
- No screenshot is available
- The feature is conceptual (e.g. AI behavior, data flow, language detection)
- A side-by-side comparison would explain the feature better than a single screenshot

#### Visual language (apply to all graphics)

Accent colors are placeholders. Swap in your own brand palette.

```
Background:     #000000 (true black)
Card fill:      #FFFFFF with border-radius: 16px
Accent:         #2F6FEB
Light accent:   #E8F0FD
Near-black text:#1A1A2E
Gray text:      #6B7280
Font:           Inter Tight, sans-serif
Tooltip style:  Dark (#1A1A1A) rounded rectangle with white text, speech bubble pointer
Card shadow:    subtle, e.g. box-shadow: 0 4px 24px rgba(0,0,0,0.10)
```

**Illustrative explainer patterns:**
- **Chat bubble pattern:** user bubble (light accent) top-right, product response (white) bottom-left. Good for: AI assistants and other AI features.
- **Side-by-side comparison:** two cards labeled with dark tooltips. Good for: before/after states, two methods.
- **UI crop with callout:** white card with focused UI + dark tooltip. Good for: settings panels, toggles.
- **Browser/app frame:** ghosted accent-colored browser chrome with a survey widget overlaid. Good for: web survey features.
- **Slack/messaging mock:** conversation thread in a white rounded card. Good for: notification routing, team features.

**Size:** ~480px wide for feature images, ~400px for irl example images. Render as HTML and export.

**Do not** put text labels directly on charts or data visualizations within the graphic.

---

## Step 4: Output format

#### Product update emails: copy output

```
--- HERO ---
Pill: Monthly Product Update
H1: March Recap
Subheadline: ...

--- FEATURE 1: [Name] ---
Category pill: ...
H2: ...
Body: ...
CTA: [link text] → [URL]

--- IRL EXAMPLE 1 ---
Pill: ...
Pull quote: "..."
Bullets:
• ...
• ...
• ...
CTA: [link text] → [URL]
```

#### Webinar / event / onboarding emails: copy output

```
SUBJECT: ...
PREHEADER: ...

---

[email body, formatted as it would appear]

---
Sign-off: [Name], [Title]
```

---

## Step 5: Build in Customer.io

After copy (and graphics, if applicable) are approved, offer to build the email directly in Customer.io using the Customer.io connector.

### Important limitation: rich text emails

**The Customer.io MCP connector only supports Design Studio (component-based) templates. It cannot create rich text emails.** Rich text emails (the kind that look like a plain Gmail message) must be built manually in the Customer.io UI.

If the email type is one that should use rich text (webinar invites, event invites, onboarding emails, anything personal and plain-text in style), tell the user upfront:

> *"The Customer.io connector can't create rich text emails directly. I'll give you the copy ready to paste, but you'll need to create the template in Customer.io yourself using the rich text editor. I can walk you through it if helpful."*

For product update emails that use Design Studio templates, the connector works normally.

### Connector check

**Before proceeding, verify the Customer.io connector is active.** If it is not connected:
- Tell the user: *"To build this in Customer.io, you'll need to connect the Customer.io MCP connector. Head to Settings → Connectors in Claude and search for Customer.io to connect it."*
- Do not attempt to build anything until the connector is confirmed working.

### Broadcast vs campaign: what to build

| Type | Customer.io object | When to use |
|---|---|---|
| Broadcast | Newsletter | One-time send to a segment or list |
| Campaign | Campaign + actions | Triggered sequence (e.g. on signup, on event) |

Confirm which the user wants before building. If they said "broadcast" in Step 1, default to newsletter. If they said "campaign", default to a campaign with actions.

### Build steps

1. **Create the template** using the approved copy and graphics
2. **Name it clearly**, e.g. `Product Update: May 2026` or `Webinar: Jordan Lee` or `Onboarding Seq: Email 01`
3. **Set the sender:** confirm the from name and address (default: `[Your name] from Example Feedback` / `you@example.com` unless specified)
4. **Set subject + preheader** from approved copy
5. **For newsletters (broadcasts):** attach to an existing newsletter or create a new one with a clear name
6. **For campaigns:** confirm the trigger event and delay settings before creating actions

### After building

Always provide the direct Customer.io editor link after creating the template or newsletter so the user can review before sending.

Format: `Review it here → [Customer.io editor URL]`

---

## Tone guidelines (all email types)

- **Short and direct.** Body copy is 1 or 2 sentences per paragraph. No padding.
- **Problem-led.** Start with what the user was struggling with or what's at stake.
- **Active voice.** Always.
- **Prospects** get benefit-led CTAs (`See how it works →`). **Customers** get action CTAs (`Try it now →`, `Set this up →`).
- **Never:** "We're excited to announce", "leverage", "synergies", "seamlessly", "holistic"
- **Occasional personality** is welcome, especially in webinar and special edition emails.
- **Emoji** used sparingly and only when it fits the tone.

---

## Product areas (for pill labels and feature framing)

Example Feedback's product areas are listed below. Replace them with your own product's areas.

- **Surveys:** in-product, web, email, and link surveys
- **Feedback Inbox:** all feedback from every source in one place
- **AI Insights:** automatic themes and summaries across feedback
- **Dashboards:** custom visualizations across surveys and sources
- **Integrations:** connections to chat, help desk, CRM and product analytics tools
- **Team & Permissions:** folders, access controls, team grouping

---

## Notes

- The feedback board banner and footer are **always** included in product update emails. Never omit them.
- Pinned insights are **optional** in product updates. Ask before drafting.
- Graphics are produced **after** copy approval, never before.
- Customer.io is built **after** copy (and graphics) are approved, never before.
- For prospects, soften product-app CTAs (`See how it works →` instead of `Log back in →`).
- Onboarding emails are almost always campaigns, not broadcasts. Confirm before building.
