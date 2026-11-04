---
name: tom-pmm-demo-planner
description: >
  Plan, script, and log interactive product demos for the demo center of
  Example Feedback (a fictional customer feedback platform). Use this skill
  whenever someone on the team wants to plan an interactive demo, build a demo
  script, work out what screens to show in a click-through demo, or add a
  completed demo to the Notion demo center tracker. Triggers include plan a
  demo, help me build an interactive demo, what should I show in this demo,
  script a demo for X, or any mention of building or logging a demo center
  demo. Always use this skill before planning any interactive demo for the
  product, and do not freestyle demo screen planning without it.
---

# Interactive Demo Planner Skill

This skill plans demos recorded in your interactive demo tool (e.g. Arcade). The examples use Example Feedback, a fictional customer feedback platform with two product areas: Surveys and Research Projects. Replace the product areas, screens and IDs with your own.

## Prerequisites: Check These First

Before planning any demo, confirm two things with the person:

1. **Project access:** Are they working inside the marketing project in Claude that holds the product map? The product map (which lists every screen in the app) lives there. Without it, screen references will be inaccurate.

2. **Notion connection:** Is Notion connected? Completed demos get logged to the demo center tracker at Notion page `<YOUR_NOTION_DEMO_CENTER_PAGE_ID>` under the H2 "Demo Center". Ask: "Do you want me to log completed demos to the shared demo center page, or somewhere else?"

If either is missing, flag it before proceeding.

---

## How We Work

Go one demo at a time. Never plan multiple demos speculatively.

For each demo:
1. Propose the title, subtext, and step table
2. Get approval (or iterate) before the person starts recording
3. Once the demo link arrives, log it to Notion and update the Linear ticket
4. Move to the next demo

Never skip ahead. The person needs to record each demo before you move on.

---

## Demo Philosophy

Demos in the demo center are **solution-led, not feature-led.**

Each demo answers a pain point a specific ICP has. Features appear in the demo because they solve that pain, not because they exist.

Ask yourself before planning each demo: "What problem does this person have on a Tuesday, and how does Example Feedback solve it in this flow?"

The four primary ICPs:
- **Product Managers / Product Owners**: roadmap decisions, feature validation, activation
- **User Researchers / Insights Managers**: synthesis, multi-source analysis, stakeholder reports
- **Marketing / CRM / Lifecycle teams**: campaign feedback, enrichment, segmentation
- **CS / CX / Support leads**: satisfaction tracking, churn detection, retention

---

## Demo Format

Every demo has three elements:

### 1. Opening card
```
Title: [Demo name: matches the solution area, not a feature name]
Subtext: [One punchy sentence. Problem-first. Max 15 words. No em dashes or en dashes.]
```

### 2. Step table

| Step | Screen | What to point at | Callout label |
|------|--------|-----------------|---------------|

### Step rules
- **Maximum 5 steps.** Occasionally a 3.5 or 4.5 step is fine when two related moments need to be shown on the same screen. Never exceed 6 steps.
- **Two callouts on one screen is fine.** If two things on the same screenshot reinforce each other, use one step with two pointer targets. Label it clearly.
- **Screen references must come from the product map.** Always reference the product map (available in the marketing project) for exact screen names and file codes. Never invent screen names.
- **Use the screen codes from the product map** (e.g., 02d, 05b) so the person can navigate accurately.

### Callout label rules
- 8 to 15 words is the right length. Not a headline, not a sentence fragment.
- Problem-first or outcome-first. Not feature-first.
- Active voice. Contractions are fine.
- No em dashes, en dashes, or AI filler language.
- No vague superlatives ("powerful", "seamless", "best-in-class").
- Should reinforce the solution angle of the demo, not describe the UI mechanically.
- Each label should feel like it belongs in the same family as the others in the demo.

**Good examples:**
- "Every claim in your report backed by a direct quote. Challenge anything."
- "Set it up once. Your VoC report updates as new feedback arrives."
- "Screen and shortlist participants without jumping between tools"
- "Every piece of feedback, across every source, read in full. Nothing skipped. Nothing hallucinated."

**Bad examples:**
- "Click the connect tab" (mechanical, not outcome-focused)
- "Powerful integrations for your stack" (vague superlative)
- "Responses in. Automations triggered." (too short, too punchy for this format)

---

## Workflow After Recording

Once the person shares a demo link:

### 1. Log to Notion
Add a new row to the Demo Center table on Notion page `<YOUR_NOTION_DEMO_CENTER_PAGE_ID>` with:
- **Product**: Surveys / Research Projects / Cross-product
- **Title**: Demo title
- **Subheading**: Demo subtext
- **Demo Link**: The link provided

Use `notion-update-page` with `update_content` to append a new table row. Match the exact HTML table structure already on the page.

### 2. Update Linear
Find the matching Linear issue in the demo hub project (issue range `<TEAM_KEY>-XXXX`). Update it with:
- **Description**: `Interactive demo link: [URL]`
- **Status**: In Review

Use `save_issue` with the issue ID, description, and state fields.

### 3. Confirm and move on
Tell the person both are done and move to the next demo.

---

## Callout Iteration Protocol

When the person flags a callout label they don't like:
1. Ask what angle they want (or read the context from what they said)
2. Offer 3 alternatives, each with a meaningfully different approach
3. If they want something close to what they wrote themselves, refine their version rather than replacing it
4. Once confirmed, update the full table before moving on

Never rewrite a callout the person has approved. Only change what they flag.

---

## Copy Rules (Apply to All Demo Content)

- US English only
- No em dashes or en dashes: use colons or periods instead
- Active voice throughout
- No "focused", "powerful", "seamless", "next-gen", "best-in-class"
- Always use current product names. In the examples: always "Research Projects", never the old name "Insight Library"
- Never reference retired features (in the examples: "priority score" or "priority threshold")
- Never imply AI replaces the researcher: AI assists, AI handles grunt work
- Internal persona code names (e.g. "Roadmap Builder", "Insight Seeker") never appear in demo content

---

## Product References

Replace these with the screens from your own product map. The list below is a fictional example.

**Surveys product screens** (from product map):
- 02a: Surveys list
- 02b: Create new survey: method picker
- 02c: Create new survey: format picker
- 02d: Survey editor: Questions
- 02e: Survey editor: Question types
- 02g: Survey editor: Configure
- 02h: Survey editor: Connect (integrations)
- 02i: Survey editor: Share
- 02j: Survey editor: Analyze / Results
- 02k: Survey editor: Analyze / Individual responses

**Research Projects screens** (from product map):
- 04: AI chat: Ask AI
- 05a: Research Projects landing
- 05b: Research project: Report
- 05c: Research project: Insights
- 05d: Research project: Dashboard
- 05e: Research project: Data
- 05f: Research project: Setup
- 05g: Research Projects settings: Context
- 05h: Research Projects settings: Data sources
- 05i: New research project: Wizard

**Note:** Some screens (audience targeting panel, specific targeting conditions) are not in the product map. Flag these explicitly when they are needed for a demo: the person will need to navigate there manually and you should describe what to look for.

---

## Notion Table Structure Reference

The demo center table uses this HTML structure:

```html
<tr>
<td>Product (Surveys / Research Projects / Cross-product)</td>
<td>Demo title</td>
<td>Demo subtext</td>
<td>[Demo URL](Demo URL)</td>
</tr>
```

Always append new rows before the closing `</table>` tag. Match the existing row structure exactly.

---

## Linear Project Reference

- Project: Interactive Demo Hub for Website (`<YOUR_LINEAR_PROJECT_ID>`)
- Team: Marketing
- Issue range: `<TEAM_KEY>-XXXX` to `<TEAM_KEY>-YYYY` (original scaffolded issues)
- All issues: High priority, assigned to the person running the session
- Status flow: Backlog → In Review (when the demo link is added)
