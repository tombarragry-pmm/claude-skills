---
name: tom-pmm-product-update-email
description: Generate copy and graphics for monthly product update emails and special edition product launch emails for Example Feedback (a fictional customer feedback platform). Use this skill whenever someone asks to write, draft, or plan a product update email, newsletter, or product launch announcement email. Also trigger when someone mentions feature sections, irl examples, email graphics, or UI mockup graphics for an email. Trigger even for vague requests like "help me write this month's product update" or "I want to announce this feature via email". Always use this skill when working on Customer.io product update templates.
---

# Product Update Email Skill

This skill helps the user write copy and generate graphics for monthly product update emails and special-edition product launch emails sent via Customer.io. The examples use Example Feedback, a fictional customer feedback platform. Replace the product names, URLs and colors with your own.

## Workflow

**Always chat-first.** All copy is drafted and approved in conversation before any graphics are produced. Never jump straight to graphics.

### Step 1: Intake

Ask the user for:
1. **Email type:** standard monthly recap OR special edition (launch teaser, year-end recap, etc.)
2. **Features to include:** name, one-line description, and CTA destination URL for each
3. **Audience:** active customers/users, trial users, prospects, or a mix (this affects CTA framing)
4. **Any screenshots or product images available:** if yes, note them for the graphics step; if no, you'll generate illustrative graphics instead
5. **Anything unusual:** special tone, a webinar to promote, a survey to embed, a personal sign-off, etc.

If the user provides feature names and context upfront, extract what you can and only ask for what's missing.

---

### Step 2: Draft copy (in conversation)

Draft all copy blocks in chat. Get approval before moving to graphics. Structure follows the email type.

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

**Pinned insights** (gray card, optional: ask the user if they have resources to include)
- 2 or 3 content items (best practice guide, video tutorial, webinar, etc.)
- Each: pill label + title + 1-line description + CTA link

**Feedback board banner** (accent color, always included)
- Fixed copy: `See, vote on, and suggest new Example Feedback features`
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
- Can include a personal sign-off from the sender (photo + name + title, e.g. *[Your name], [Title] @ Example Feedback*)
- Can embed a survey directly in the email body
- Webinar CTAs and GIF/demo previews are encouraged

---

### Step 3: Graphics

After copy is approved, produce graphics for each feature section. One graphic per feature.

#### Choosing the graphic type

**Use UI close-up** when:
- The user has a product screenshot available
- The feature is best understood by seeing the actual UI
- The feature is a settings panel, toggle, form, or data view

**Use illustrative explainer** when:
- No screenshot is available
- The feature is conceptual (e.g. AI behavior, data flow, language detection)
- A side-by-side comparison would explain the feature better than a single screenshot
- The feature involves conversation, routing, or a before/after state

#### Visual language (apply to all graphics)

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

The accent colors are placeholders. Replace them with your brand colors.

**Illustrative explainer patterns (use these as starting points):**

- **Chat bubble pattern:** user bubble (light accent `#E8F0FD`) top-right with avatar, product response bubble (white) bottom-left with your logo mark. Show a realistic question + processing state + answer. Good for: AI assistants and other AI features.
- **Side-by-side comparison:** two cards or phone frames side by side, each labeled with a dark tooltip. Good for: light/dark mode, before/after states, two calculation methods.
- **UI crop with callout:** white card showing a focused piece of UI, dark tooltip pointing to the key element. Good for: settings panels, toggles, permissions modals.
- **Browser/app frame:** ghosted accent-colored browser chrome with a survey widget overlaid on top. Good for: web survey features, localization, targeting.
- **Slack/messaging mock:** conversation thread in a white rounded card with user avatars. Good for: notification routing, team collaboration features.

**Size:** target ~480px wide for the main feature image, ~400px for irl example images. Render as HTML and export.

**Do not** put text labels directly on charts or data visualizations within the graphic. Let the UI elements speak for themselves.

---

### Step 4: Output format

Deliver copy as clearly labeled blocks ready to paste into Customer.io:
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

Deliver graphics as rendered HTML artifacts (one per feature), clearly labeled.

---

## Tone guidelines

- **Short and direct.** Body copy is 1 or 2 sentences. No padding.
- **Problem-led.** Start with what the user was struggling with, not what the feature does.
- **Active voice.** Always.
- **Accent highlights** on H2s: 1 or 2 key words, never the whole headline.
- **irl examples** use a realistic workplace quote as the H2. Make it something a PM, researcher, or CX manager would actually say.
- **CTAs** are lowercase action phrases with → arrow. Not "Click here" or "Learn more" alone. Make them specific.
- **Prospects** get benefit-led CTAs ("See how it works →"). **Customers** get action CTAs ("Try it now →", "Set this up →").
- Occasional personality is welcome in special editions. Emoji used sparingly and only when it fits the tone.

---

## Product areas (for pill labels and feature framing)

Example Feedback's product areas are listed below. Replace them with your own product's areas.

- **Feedback Inbox:** all feedback from every source in one place
- **AI Insights:** automatic themes, summaries and a chat interface for asking questions about feedback
- **Research Projects:** multi-source research projects with AI-generated reports
- **Surveys:** in-product, web, email, and link surveys
- **Integrations:** connections to chat, help desk, CRM, call recording, app store and product analytics tools
- **Dashboards:** custom visualizations across surveys and sources
- **Team & Permissions:** folders, access controls, team grouping

---

## Notes

- The feedback board banner and footer are **always** included. Never omit them.
- Pinned insights are **optional**. Ask the user if they have resources to include before drafting.
- "irl: examples" section is standard in monthly recaps; in special editions, replace with numbered use-case examples instead.
- If the user is sending to **prospects**, soften product-app CTAs (e.g. `See how it works →` instead of `Log back in →`).
- Graphics are produced **after** copy approval, never before.
