---
name: tom-pmm-inapp-changelog
description: Write in-app changelog posts for Example Feedback (a fictional customer feedback platform). Use this skill whenever the user asks to write, draft, or create an in-app changelog post, in-app changelog entry, or in-product release announcement. Trigger on phrases like "write an in-app post for X", "create a changelog widget entry for X", "draft an in-app changelog for X", or "help me announce X in the product". This skill is distinct from the public changelog skill (tom-pmm-changelog): in-app posts are shorter, more conversational, emoji-led, and always include a CTA button.
---

# In-App Changelog Skill

Your in-app changelog tool (e.g. Beamer) is Example Feedback's in-app changelog widget. Posts appear directly inside the product and need to be immediately scannable, punchy, and outcome-focused. Readers are active users, not prospects: write for people who already use the product and want to know what changed and why it helps them.

---

## Post Structure

Every in-app post has exactly this structure:

```
[TAG]  [Date: auto-filled by the changelog tool]

[TITLE]

[OPENING PARAGRAPH]

[IMAGE: provided by the user, do not write placeholder copy]

[BENEFIT BULLETS]

[OPTIONAL SECTION: plan/access notes only, not a default]

[CTA BUTTON]
```

---

## 1. Tag

One tag per post. Choose based on what the update is about:

| Tag | Use for |
|---|---|
| `Surveys` | Any update to survey creation, distribution, logic, targeting, or analysis |
| `AI Insights` | Any update to AI Insights, Insight Projects, Reports, themes, the AI analyst, or data sources |
| `New` | Everything else: team permissions, access controls, targeting updates, operational/platform changes |

---

## 2. Title

**Specs:**
- 1 line only: never wrap
- 5 to 9 words
- 30 to 50 characters (not counting emoji)
- Optional emoji at the end: use for marquee feature launches, not routine updates
- Must make the update immediately clear: no clever ambiguity at the expense of clarity

**What works:**
- Tension/reveal: "CSAT was hiding some of the story"
- Outcome-first: "Filter your feedback, improve your insights"
- Introducing pattern: "Introducing Archive for your Workspace"
- Parallel structure: "Speak their language, read yours"
- Direct action: "Pause new comments on your surveys"

**What doesn't work:**
- Starting with the feature name as a noun ("Smart Follow-Up Questions")
- Vague transformation language ("Take your research to the next level")
- Marketing superlatives ("Powerful new feedback controls")
- Two ideas crammed into one line

---

## 3. Opening Paragraph

**Specs:**
- 20 to 40 words
- 110 to 220 characters
- 2 to 3 sentences maximum

**Rules:**
- Lead with context or pain, not the feature name
- Introduce the feature name in sentence 2 (can bold it on first mention)
- "You/your" voice throughout: never "we're excited to announce"
- Active voice, contractions are fine
- US English
- No em dashes or en dashes: use colons or periods instead

**What works:**
- "Ever feel like you're spending more time stitching feedback together than actually using it? [**Feature name**] changes that."
- "Tracking NPS across multiple channels used to mean jumping between tabs. [**Feature name**] keeps it all in one place."

**What doesn't work:**
- "We're thrilled to introduce..."
- "This powerful new feature allows users to..."
- Repeating the title in the first sentence
- Starting with "Now you can..."

---

## 4. Image Slot

The user provides all images. Do not write placeholder text or suggest what should go in the image. Leave this slot blank in the draft: note it as `[IMAGE]`.

---

## 5. Benefit Bullets

**Specs:**
- 3 to 4 bullets: never fewer than 3, never more than 4
- Each bullet: 10 to 20 words
- No full stops at the end of bullets

**Two formats: use consistently within a post:**

**Format A: Emoji + outcome statement (plain)**
```
🔔  Get real-time notifications without leaving your inbox
👥  Keep your whole team in the loop automatically
📍  Pin the feedback that matters most
```

**Format B: Emoji + bold lead phrase + brief explanation**
```
🔔  **Real-time alerts** - stay updated without refreshing the page
👥  **Team-wide visibility** - everyone sees the same updates in one place
📍  **Pinned feedback** - never lose track of the responses that matter
```

Note: Format B uses a hyphen (not an em or en dash) between the bold phrase and the explanation.

**Rules:**
- Each bullet must add something new: no repeating the opening paragraph
- Focus on what the user gets or achieves, not what the feature does technically
- Pair bullets to cover distinct angles (e.g. speed + control, individual + team, before + after)
- No jargon, no vague action words like "manage", "leverage", "validate"
- Never list technical specifications as benefits

---

## 6. Optional Section

Include only when one of these applies:
- The feature is restricted to certain plans
- The feature has a limited availability window
- There is a meaningful access caveat (e.g. Workspace Admin only)

**Format:**
```
*[Feature name] is available on [Plan] and above.*
```
or
```
*Available to Workspace Admins and Owners only.*
```

Do not include a "Want to learn more? Check out our support article" link unless the user explicitly asks for it.

---

## 7. CTA Button

Always present. Always directs to the in-product action.

**Rules:**
- Action verb first: what does the user do?
- Specific to the feature: not "Learn more" or generic "Try it"
- 2 to 5 words
- Optional emoji at the end (match the title emoji if one was used)

**Strong CTA examples:**
- "Try Smart Follow-Ups"
- "Start your first project"
- "Set up Slack notifications"
- "Run an Insight Project"
- "Add a data source"
- "Explore your reports"

**Weak CTA examples (avoid):**
- "Learn more here"
- "Read the update"
- "Click here"
- "Find out more"

---

## Tone Rules

**Always:**
- US English spelling and grammar
- Active voice and contractions
- Outcome-first: what does the user walk away with?
- Direct: no hedging, no filler
- "You/your" throughout

**Never:**
- Em dashes or en dashes: use hyphens, colons, or periods
- "Powerful", "seamless", "next-gen", "best-in-class", "focused", "excited"
- "Feedback Center" (retired name: always "Feedback Inbox")
- "Pulse score" or "pulse threshold" (retired features)
- Framing that implies AI replaces the researcher: always AI assists, AI handles the grunt work
- Internal persona names (never "Insight Explorer", "Roadmap Builder": use real job titles if needed)

---

## Workflow

Work sequentially and gate each step before moving forward.

**Step 1: Brief**

Ask the user for:
- What is the feature or update?
- What tag should it use? (Surveys / AI Insights / New)
- What can users do now that they couldn't before?
- Any plan restrictions or access caveats?
- Is there a primary outcome angle to lead with?

**Step 2: Title**

Draft 3 title options (a/b/c) following the specs. Get approval before writing anything else.

**Step 3: Opening paragraph**

Draft the opening. Get approval or feedback before writing bullets.

**Step 4: Bullets + optional section + CTA**

Draft all three together (they're short enough to review as a unit).

**Step 5: Full post**

Assemble the approved components into the final post, ready to paste into your in-app changelog tool (or hand to the `tom-pmm-create-inapp-post` skill to create it for you).

---

## Full Example

```
[AI Insights]

Run research in minutes, not days 🚀

Insight Projects now let you run a focused project across all your feedback sources at once. Connect your surveys, support tickets, and call transcripts, then let AI draft the report while you stay in control.

[IMAGE]

🔍  **One project, all your sources** - no more stitching feedback together manually
📄  **AI-drafted report** - structured findings ready to edit and share in minutes
✅  **Every conclusion is cited** - click any finding to see the feedback behind it
🎯  **You direct the synthesis** - set the scope, filter the noise, own the output

*Insight Projects are available on Pro and Enterprise plans.*

[CTA] Run your first project
```

---

## Reference: Source Patterns

These email feature headlines are useful title inspiration. They show the tension/reveal and parallel structure that works for this voice:

- "CSAT was hiding some of the story"
- "Surveys that know when to stay quiet"
- "Filter your feedback, improve your insights"
- "Speak their language, read yours"
- "Unlock insights from recordings"
- "Group teams, organize surveys, and move faster"
- "No more starting from scratch when you have follow-up questions"

Replace these with headlines from your own past emails once you have them.
