---
name: research-project-description
description: Generate project descriptions for Research Projects, the research product area of Example Feedback (a fictional customer feedback platform). Use this skill whenever someone provides a research use case, topic, or question and wants a research project description written. Also trigger when someone asks for a project title, short description, or full project template for Research Projects. Even a vague hint like "write me a project for churn analysis" or "I want to research onboarding drop-off" should trigger this skill.
---

# Research Project Description Skill

Generates ready-to-use project templates for Research Projects, the research product area of Example Feedback (a fictional customer feedback platform). Replace the product names with your own. Each template has three components: a title, a short description, and a full project description.

## How this skill is used

The user will typically give you a brief hint: a use case, a research question, or a topic. From that, generate a complete project template. The user may edit the output; write it to be useful out of the box but easy to personalize.

## Core principles

**Multi-source by default.** Research Projects connects signals across multiple data sources. Project descriptions should reflect this, so never frame a project as single-source analysis. Always position the research as looking for patterns across sources.

**Source-agnostic for non-survey data.** Example Feedback owns survey data, so you can be specific about survey signal types (NPS detractors, CSAT responses, in-product survey feedback etc.). For all other data sources, describe the *type of signal or feedback* rather than naming a specific tool. Use phrases like "feedback related to lost deals", "support interactions", "product usage patterns", "public review feedback", not "Salesforce", "Zendesk", "G2".

**Researcher tone.** Write as a smart, experienced researcher briefing themselves and their team. Not a formal academic brief, not a corporate document. Clear, direct, and purposeful.

**Templates are starting points.** Descriptions should be specific enough to use immediately, but loose enough that a researcher can adapt them to their own data sources and context without the logic breaking.

---

## Output format

Every output contains all three components in this order:

### 1. Title
- Max 40 characters
- Clear and descriptive
- No em dashes, en dashes or special punctuation

### 2. Short description
- Max 150 characters
- One or two sentences
- Communicates what the research will reveal or achieve
- No em dashes or en dashes
- Written to intrigue and inform, not to instruct

### 3. Project description
Use this structure exactly, with **bold section headers** and asterisk bullets (*):

---

[Opening paragraph: 2 to 3 sentences. Set the research context, name the sources being compared, and state the goal. Lead with the cross-source framing: what two or more signals are being connected and why.]

**Research objectives / questions:**
* [Question 1]
* [Question 2]
* [Question 3]
* [Question 4]

**Themes and patterns to look for:**
* [Theme 1: short label and explanation]
* [Theme 2: short label and explanation]
* [Theme 3: short label and explanation]
* [Theme 4: short label and explanation]

**Insights to uncover:**
* [Insight 1]
* [Insight 2]
* [Insight 3]

**How findings will be used:**
* [Usage 1]
* [Usage 2]
* [Usage 3]

---

## Example templates

Use these as quality and tone references when generating new templates.

---

### Template: Detractor & Lost Deal Pattern Match

**Title:** Detractor & Lost Deal Pattern Match

**Short description:** Find out whether dissatisfied customers and lost prospects are saying the same things, and whether your teams should be fixing the same root cause.

**Project description:**

This project compares themes from NPS detractor responses with feedback related to lost deals, looking for shared patterns in how dissatisfaction is expressed across both sources. The goal is to understand whether the friction existing customers describe mirrors the reasons prospects chose not to move forward, which would suggest systemic issues rather than isolated post-sale complaints.

**Research objectives / questions:**
* What are the dominant themes in detractor feedback, and do the same themes appear in lost deal feedback?
* Are there patterns that surface strongly in one source but not the other, and what might that tell us?
* Is the language used to express disappointment consistent across both signals, or does framing differ by context?
* Are there segments (by plan, industry, or lifecycle stage) where the overlap is stronger or weaker?

**Themes and patterns to look for:**
* Shared language: similar words or phrases appearing independently in both sources
* Divergent signals: issues raised frequently by detractors that don't appear in lost deal feedback, or vice versa
* Intensity differences: topics that appear in both sources but with notably different emotional weight
* Segment clustering: whether certain customer types are over-represented in both signals simultaneously

**Insights to uncover:**
* A shortlist of themes with strong cross-source corroboration, the issues most likely to reflect real systemic problems
* Any gaps between what existing customers complain about and what prospects cite as reasons not to buy
* Hypotheses about whether dissatisfaction and lost deals share a common root cause

**How findings will be used:**
* Brief product and GTM teams on issues that appear to affect both retention and acquisition
* Inform whether messaging or product priorities need to shift based on consistent cross-source evidence
* Identify areas for follow-up research where signals diverge and need further investigation

---

### Template: Churn Signal Pattern Analysis

**Title:** Churn Signal Pattern Analysis

**Short description:** Identify whether customers who churn leave consistent feedback signals beforehand, and whether those signals appear across more than one source.

**Project description:**

This project looks for patterns in feedback submitted by customers who later churned, with the goal of identifying whether dissatisfaction signals appeared consistently in the period leading up to cancellation. The aim is to understand whether churn is preceded by predictable themes, and whether those themes are visible across multiple feedback sources or concentrated in one.

**Research objectives / questions:**
* What topics and sentiments appear most frequently in feedback from customers who churned?
* Do the same themes appear across different feedback sources, or does each channel surface different signals?
* Is there a point in the customer journey where negative sentiment tends to spike before churn?
* Are there segments where churn-related feedback patterns are more pronounced?

**Themes and patterns to look for:**
* Recurring complaints: issues that appear consistently in the weeks or months before cancellation
* Channel divergence: topics that appear in one feedback source but are absent from others
* Sentiment trajectory: whether tone shifts gradually or drops sharply before churn
* Segment patterns: whether churn signals are concentrated in particular customer types or lifecycle stages

**Insights to uncover:**
* A set of early warning themes that could inform retention triggers
* Which feedback sources carry the strongest predictive signal for churn
* Whether churn-related feedback differs meaningfully by customer segment

**How findings will be used:**
* Inform the design of early warning monitoring across feedback sources
* Brief customer success and product teams on the themes most associated with churn risk
* Identify gaps in current feedback coverage that may be missing early churn signals

---

### Template: Enterprise vs SMB Experience Split

**Title:** Enterprise vs SMB Experience Split

**Short description:** Compare how enterprise and SMB customers describe their experience to find where needs diverge and where a shared fix could serve both.

**Project description:**

This project compares feedback themes across enterprise and SMB customer segments to understand whether the two groups encounter fundamentally different problems, or whether the same issues surface at different intensities. The goal is to establish whether product and support investments should be segmented by customer type, or whether there is a shared set of priorities that serves both.

**Research objectives / questions:**
* Which feedback themes are unique to enterprise customers, and which are unique to SMB?
* Where do the two segments agree, and does that consensus point to issues that should be prioritized universally?
* Are satisfaction levels and friction points distributed differently across segments even when the themes overlap?
* Do enterprise and SMB customers describe their goals and workflows differently in ways that affect how feedback should be interpreted?

**Themes and patterns to look for:**
* Segment-exclusive themes: issues that appear clearly in one group and not the other
* Shared pain with different causes: similar complaints that stem from different underlying problems
* Intensity gaps: topics where both segments raise the same issue but with notably different frequency or urgency
* Workflow divergence: differences in how each segment describes using the product day-to-day

**Insights to uncover:**
* A clear picture of where enterprise and SMB needs diverge, grounded in feedback patterns rather than assumptions
* Shared themes that represent universal priorities regardless of segment
* Hypotheses about why the two segments experience the product differently

**How findings will be used:**
* Inform segmented product and support roadmap decisions
* Help the team avoid over-indexing on one segment's feedback when making universal product changes
* Surface themes that warrant dedicated follow-up research for one or both segments

---

### Template: Review vs Survey Feedback Gap

**Title:** Review vs Survey Feedback Gap

**Short description:** Find out if customers say different things in public reviews versus private surveys, and whether your owned feedback is capturing the full picture.

**Project description:**

This project compares the themes that appear in public review feedback with those surfaced through private survey responses, to understand whether customers express themselves differently depending on the channel. The goal is to identify blind spots and validate whether current survey programs are capturing the full picture, or whether important signals are only visible in public feedback.

**Research objectives / questions:**
* Do the dominant complaint and praise themes in public reviews match what appears in survey responses?
* Are there topics customers raise publicly that rarely or never appear in surveys, and what might explain that gap?
* Does sentiment intensity differ between public and private feedback on the same themes?
* Are there patterns in what customers choose to say publicly versus privately that could inform how surveys are designed?

**Themes and patterns to look for:**
* Shared themes: topics that surface consistently across both public and private channels
* Public-only signals: issues or praise that appears in reviews but is absent from survey data
* Survey-only signals: themes that customers share privately but don't raise in public forums
* Tone differences: whether the same topic is framed more positively or negatively depending on the channel

**Insights to uncover:**
* A clear view of whether owned feedback sources are representative of the broader customer voice
* Specific gaps where public feedback is surfacing issues not captured by current survey design
* Hypotheses about why certain themes appear in one channel but not the other

**How findings will be used:**
* Inform improvements to survey design to better capture themes currently only visible in public feedback
* Give the team confidence about which feedback sources to prioritize for different research questions
* Identify topics that warrant dedicated survey questions or follow-up research

