---
name: tom-pmm-nurture-email
description: Generate plain text nurture emails from Example Feedback (a fictional customer feedback platform). Use this skill whenever someone asks to write, draft, or create a nurture email, follow-up email, or outreach email from the company. Also trigger when someone mentions an event follow-up, content download follow-up, lead nurture, or post-webinar email. Always use this skill when the request involves emailing leads or prospects on behalf of the company, even if they just say "write me an email" in the context of a marketing or campaign task.
---

# Nurture Email Generator

This skill generates short, plain-text nurture emails in the company's voice. Emails are sent from a named person, have a single CTA (book a demo), and are written for two primary triggers: post-event/webinar follow-up and content download follow-up.

The examples use Example Feedback, a fictional customer feedback platform. All customer stories, names and numbers below are made up. Replace them with your own approved stories and stats.

## How to use this skill

When triggered, ask the user for any context you don't already have:

**Required inputs:**
- **Trigger:** What prompted this email? (e.g. "attended our session at [Event]", "downloaded our [Report]", "signed up for free trial")
- **Sender name:** Who is this email from? (e.g. "Jordan", "Sam", "Alex")
- **Booking link:** Leave as `[booking link]` placeholder if not provided
- **Recipient segment:** Who is this going to? (e.g. ICP leads, free trial users, event attendees)
- **Any specific angle or hook:** e.g. a relevant customer story, a specific pain point relevant to the audience, a stat to lead with

If the user is working inside a Claude project that holds the team's writing context (brand voice, value props, campaign notes), draw on that context before generating.

---

## Output format

Always output:

```
SUBJECT: [subject line]

PREVIEW: [preview text: 1 sentence, adds intrigue or context beyond subject]

---

[email body]
```

---

## Voice & style guide

Derived from approved email examples. Follow these rules closely.

### Tone
- Conversational, human, direct: reads like a real person wrote it
- Confident but not pushy; helpful but not hand-holdy
- Light wit is welcome but never forced
- Avoid corporate-speak: no "leverage", "synergies", "holistic", "seamlessly"

### Structure
- 1 or 2 short paragraphs + CTA
- Lead with a relatable problem or observation, not a product pitch
- Problem → relevance to reader → how Example Feedback solves it → CTA
- CTA is always booking a demo (unless specified otherwise)

### Sentence style
- Short sentences. No padding.
- Use line breaks to create rhythm
- Lists are OK when showing 3+ proof points, but keep them tight (one line each)
- Parenthetical asides work well for adding personality: "(spoiler: they don't anymore!)"

### What works
- Open with a pain point the reader recognizes
- Use "Does this sound familiar:" as a hook when appropriate
- Social proof via customer names and specific numbers
- Dual CTA (primary: book demo / secondary: free trial) works well for colder audiences
- Mention integrations that are relevant to the reader's likely stack (Jira, Slack, HubSpot, Intercom, Zendesk, Gong)
- A response-rate stat about embedding the first survey question in an email (useful for event/research audiences). The example below uses a made-up +15%. Use your own verified number.
- Partner context works well for partner-event emails (e.g. "as a key Fabrikam partner")

### What to avoid
- Long intros
- Listing every feature
- Vague CTAs ("learn more", "check it out")
- Overusing "we"
- Starting with "I hope this email finds you well" or similar

### Placeholders to always use (personalization handled externally)
- `[first name]`: recipient first name
- `[booking link]`: sender's calendar link
- `[sender name]`: if variable
- `[company name]`: if personalizing by company

---

## Value props (use selectively, not all at once)

- Feedback is everywhere but insights are nowhere: Example Feedback connects them
- Integrate feedback into existing workflows (Jira, Slack, HubSpot, Intercom, Zendesk)
- AI categorization organizes hundreds of responses automatically, no manual analysis
- Feedback Inbox: one place for all feedback sources
- Run targeted surveys at key moments: post-feature launch, cancellation, post-support
- Embedding the first survey question in an email lifts response rate (made-up example stat: +15%)
- Most-installed feedback integration in a partner's marketplace (made-up example claim)
- Multilingual, proven at scale
- Zero-party data for personalization

---

## Customer stories reference

Use these to add credibility. Always link to the full story. Match the story to the reader's likely industry/pain point.

All companies, stats and URLs in this table are fictional. Replace the table with your own published customer stories.

| Company | Industry | Key stat/outcome | URL |
|---|---|---|---|
| **Northwind Health** | Health tech | 41% → 82% satisfaction in a week; weekly analysis cut from 6h → 45 min; 4 tools consolidated into one | https://example.com/customer-stories/northwind-health |
| **Contoso Bank** | Mobile banking (fintech) | +6 point NPS improvement; up to 70% survey completion rate; 5 automated workflows | https://example.com/customer-stories/contoso-bank |
| **Fabrikam Tax** | Fintech / tax app | Retains mobile users with personalized journeys built on survey answers | https://example.com/customer-stories/fabrikam-tax |
| **Tailspin Homes** | Proptech / real estate | Saves 8+ hours per week using survey data in CRM workflows | https://example.com/customer-stories/tailspin-homes |
| **Woodgrove Pay** | Fintech | 40% faster feature validation using customer feedback | https://example.com/customer-stories/woodgrove-pay |
| **Litware** | SaaS / email marketing | Turned customer insights into product improvements | https://example.com/customer-stories/litware |
| **Adventure Works** | Enterprise / industrial tech | CSAT improved by 15% | https://example.com/customer-stories/adventure-works |
| **Margie's Travel** | Travel tech | Survey data + CRM powering a better booking experience | https://example.com/customer-stories/margies-travel |
| **Alpine Fitness** | Health & fitness (1000+) | Built a reliable engine for user insights | https://example.com/customer-stories/alpine-fitness |
| **Fourth Coffee Media** | Media / publishing | Data-driven reader journey with surveys | https://example.com/customer-stories/fourth-coffee-media |

> If you need more detail on a specific story, fetch the URL above before writing the email.

---

## Email type playbook

### Post-event / webinar follow-up
- Sender: the speaker or someone from the team who was present
- Open: thank them for attending, reference the event by name
- Hook: a relevant insight or stat from the session, or a question that bridges their problem to Example Feedback
- Keep it warm and human: this is a warm lead
- Soft CTA: offer a walkthrough, not a hard sell
- LinkedIn connect offer works well for speaker emails
- Example subject styles: "Quick follow-up from [Event]", "You were at [Event]. Worth a chat?"

### Content download follow-up
- Sender: someone from the team (account manager, growth, etc.)
- Open: acknowledge the download implicitly (don't be creepy about it)
- Hook: the core insight or problem the content addresses
- Bridge to Example Feedback: "here's what teams like yours do about it"
- Use numbered list format for 3 proof points if email is longer
- Use customer stories to anchor claims
- Dual CTA (demo + free trial) appropriate for colder/unknown-intent leads
- Example subject styles: "Everything you've collected sits in your survey tool. Nothing changes.", "Feedback is everywhere. Insights are nowhere."

### Free trial ICP follow-up
- Very short: 2 or 3 sentences + CTA
- Personal tone, as if checking in
- Reference their progress if possible ("I see you're off to a solid start")
- CTA: 15-min call this week
- No pitch, no bullet points: pure human warmth

---

## Example emails (voice reference)

### Example 1: Free trial ICP (very short, warm)
> Hey [name],
> I was just checking in to see how you were getting along, and I see you're off to a solid start with Example Feedback!
> I help teams turn their first few days into quick wins they can share with their teams. Usually it's by showing them how to integrate feedback into their existing workflows so it's accessible when they need it.
> Worth a 15-min call this week? Here's my calendar: [booking link]

### Example 2: Lead intro (problem-led, structured)
> Subject: Everything you've collected sits in your survey tool. Nothing changes.
>
> Hi [first name],
> Most teams we work with collect feedback but struggle with what comes next. Everything they've collected sits in their survey tool. Nothing changes.
>
> Here's a few ways you can change that (with Example Feedback of course!)
>
> 1. Connect feedback to your existing workflow: push it to Jira, Slack, or your marketing automation tool.
> 2. Let AI handle the analysis: no one has time to read hundreds of responses.
> 3. Focus on specific moments: right after a feature launch, when someone cancels, after a support interaction.
>
> Want to see this in action? Book a 20-minute demo and we'll focus on your specific use case.
> [booking link]
> Or start exploring on your own with our free trial.

### Example 3: Post-event speaker email (warm, low pressure)
> Hi [first name],
> Thanks for joining our session at [Event], great to have you there.
>
> By the way, did you know that embedding the first survey question in an email can lift response rates by around 15%?
>
> If you're open to evaluating your current survey or VoC stack, we'd be happy to give you a walkthrough and check if Example Feedback might be a fit (if not, we'll suggest other solutions, promise!).
>
> Grab a slot with our team here: [booking link]

### Example 4: Case study-led (Northwind Health, fictional)
> Hey [first name],
> Does this problem sound familiar: feedback is everywhere, but insights are nowhere to be seen. Northwind Health, a customer of ours, had the exact same issue (spoiler: they don't anymore!)
>
> Their VoC lead spent 6 hours every week just trying to make sense of scattered feedback. After connecting everything to Example Feedback's Feedback Inbox, that dropped to 45 minutes.
>
> We can show you in 20 minutes how to do the same. Grab a time here: [booking link]
> Not ready for a call? Start with our free trial.

---

## Generation checklist

Before outputting, verify:
- [ ] Subject line is punchy: ideally a pain point or surprising statement, not a feature name
- [ ] Preview text adds information, doesn't just repeat the subject
- [ ] Email opens with the reader's problem, not the product's features
- [ ] Length is short (1 or 2 paragraphs + CTA max, unless list format is used)
- [ ] CTA is clear and specific (not "learn more")
- [ ] Personalization placeholders are in place
- [ ] Tone matches the trigger type (warm for events, problem-led for downloads)
- [ ] No filler phrases ("I hope this finds you well", "don't hesitate to reach out")
