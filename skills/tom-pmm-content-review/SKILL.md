---
name: tom-pmm-content-review
description: "Master reference for the writing standards of Example Feedback (a fictional customer feedback platform): tone of voice, grammar, product content framework, style guide, and AI-language mitigation. AUTOMATICALLY trigger whenever the user shares content about Example Feedback or written for Example Feedback: blog posts, landing pages, emails, help docs, branded text, social posts (company or personal profiles on LinkedIn, X/Twitter, etc.). The trigger is the topic (Example Feedback), not the channel. Private profiles included. Once triggered, you MUST ask before doing anything, every single time, even if the user said 'review this' or 'fix this'. NON-NEGOTIABLE. Ask exactly: 'Would you like me to review this against the Example Feedback Content Review Guide? I will cover: (1) tone of voice and grammar, (2) product content framework, (3) style guide, and (4) AI-sounding language.' Do not proceed without their reply."
---

# Example Feedback Content Review

This is your single source of truth for all Example Feedback content. It merges the Tone of Voice guide, the product content framework, the Style Guide, and the AI-language mitigation rules into one unified reference. Example Feedback is a fictional customer feedback platform; replace the product name, product areas, personas and integrations with your own.

**Naming rule**: whenever you refer to this skill in conversation (asking to run it, explaining what you checked, summarizing findings, or anything else), always call it the **Example Feedback Content Review Guide**. Never call it the "content guide", "brand guide", or any other shorthand.

---

## Output Format (Always Follow This)

When reviewing content, structure your response in two parts:

1. **Review & advice**: flag issues, explain why they matter, suggest fixes. Be specific and concise.
2. **Updated version**: always end with a fully revised version of the entire content, regardless of format or how minor the changes are. Present it in two ways:
   - **Code block**: wrap the revised content in a fenced code block (triple backticks, no language tag). This gives the user a clean copy button and a clearly bounded area to select from. Never put the revised content in flowing prose; always in the code block.
   - **Google Drive**: after the code block, ALWAYS use the Google Drive MCP tool (`Google Drive:create_file`) to save the revised content as a Google Doc. Name the file after the content type and date (e.g. "LinkedIn post, 18 May 2026"). Present the resulting Drive link to the user so they can open it directly. This step is mandatory, do not skip it. Only skip silently if the Google Drive tool is confirmed unavailable in the current session.

Do this even when the changes are minor. The user should never have to manually apply your suggestions: the revised version does that for them.

---

## 1. Core Principles (Apply to Everything)

### The Collect → Analyze → Act Framework
Every piece of content must connect to at least one of these pillars:

1. **Collect**: Reach users at the right place, right time, across web, mobile, in-product, and email
2. **Analyze**: Turn raw feedback into structured insights (dashboards, AI categorization, sentiment analysis, integrations)
3. **Act**: Close the loop: push insights to product, marketing, and CX teams; measure impact

Surveys are a means to an end. The end goal is action on feedback. Never position Example Feedback as just a "survey tool."

### Language Fundamentals
- **US English only** (spelling, grammar, punctuation)
- **Active voice** preferred: "Example Feedback helps you act on feedback" not "Feedback is acted upon"
- **Contractions** are natural and encouraged: we're, you'll, it's
- **No en dashes or em dashes**: use commas, colons, or periods instead
- **Short paragraphs**: 2 to 3 sentences max (4 sentences absolute ceiling)
- **Sentences under 20 words** wherever possible
- **Serial/Oxford comma** required: "polls, research, and CES surveys"

---

## 2. Brand Voice Attributes

| Attribute | In Practice |
|---|---|
| **Helpful / Supportive** | Solution-focused. Anticipate questions. Provide practical next steps. |
| **Clear / Straightforward** | Simple, precise language. Clarity over cleverness. |
| **Confident but Grounded** | Expertise backed by specifics, not vague promises. |
| **Customer-Centric** | Speak to reader needs, not just features. Show empathy for their challenges. |
| **Action-Oriented** | Guide the reader toward the next step. Direct, practical CTAs. |
| **Thought Leadership** | Show expertise in customer feedback, insights, and CX. Lead conversations. |

---

## 3. Persona Targeting

**Important:** Never use internal persona code names (Roadmap Builder, Insight Seeker, etc.) in external content. Always use actual job titles.

### Primary Personas (95% of content)

**Product Managers & Designers (internal: Roadmap Builder)**
- Technical terms OK: SDK, APIs, event triggers, attribute targeting
- Emphasize ease of integration and low developer effort
- Be factual and concise: they value accuracy over marketing spin
- Example: "Install our lightweight SDK in minutes and trigger surveys at specific funnel steps"
- Key integrations: Amplitude, Mixpanel, product analytics tools

**User Researchers & Insights Managers (internal: Insight Seeker)**
- More academic and structured tone
- Emphasize multi-channel data collection and analysis workflows
- Prioritize clarity and transparency on methodology, integrations, and reporting
- Example: "Collect feedback across web, app, and email, then analyze with AI-powered categorization"
- Key integrations: Salesforce, HubSpot, Zendesk, BI tools

**Product Marketers & Growth Teams (internal: Growth Driver)**
- Conversational but data-driven
- Emphasize automation, personalization, and segmentation
- Highlight campaign results and retention impact
- Example: "Trigger email and website surveys directly from your CRM to fuel retention campaigns"
- Key integrations: HubSpot, Customer.io, Klaviyo, marketing automation platforms

**Customer Success & Support Teams (internal: Loyalty Keeper)**
- Empathetic but metrics-focused
- Emphasize CSAT/NPS tracking, support tool integration, proactive issue detection
- Focus on customer retention and real-time satisfaction monitoring
- Example: "Monitor satisfaction in real time and catch issues before customers churn"
- Key integrations: Zendesk, Intercom, Salesforce Service Cloud

### Secondary Personas (5% of content)
Consider these when primary personas need to justify decisions upward:
- **Operations/RevOps teams**: workflow automation, CRM/automation infrastructure
- **Executives/Analysts (CMO, CPO, CXO)**: high-level business impact, ROI, cross-functional dashboards

---

## 4. Content Type Guidelines

### Marketing / Landing Pages / Ads
- Tone: Persuasive, energetic, grounded in real value
- Structure: Headline → Value proposition → Proof points → CTA
- Focus: Results and outcomes over feature lists
- Example: "Launch surveys and identify trends so you can make roadmap decisions in minutes, not weeks"

### Blog / Thought Leadership
- Tone: Conversational, confident, authoritative
- Support points with data, examples, and persona context
- Position Example Feedback as a feedback intelligence expert, not just a survey tool

### Product Emails & Updates
- Tone: Excited but informative
- Structure: What's new → Why it matters → How to use it → Next steps
- Example: "Smart Follow-ups: Set up surveys that automatically dig past the surface"

### Help Center / Documentation
- Tone: Patient, precise, educational
- Structure: Overview → Requirements → Step-by-step → Troubleshooting
- Always include specific limitations and plan availability
- Prioritize accuracy above all else

### Case Studies & Testimonials
- Tone: Story-driven but results-focused
- Structure: Challenge → Solution → Implementation → Results
- Include specific metrics and real customer quotes

---

## 5. Technical Accuracy Standards

Before finalizing any content, verify the following against your Feature & Capability Knowledge Base:

**Survey Types & Channels**
- Specific limitations (e.g., a trigger that works on desktop only)
- Technical requirements (e.g., JavaScript tracking code installation)
- Supported platforms and integration specifics

**Feature Terminology**
- Use exact names: "Feedback Tab" not "feedback widget" (in the examples)
- Plan-specific availability: list your plan tiers here (e.g. Free / Basic / Pro / Enterprise)
- SDK version requirements for specific features

**Capability Claims**
- Precise limits (e.g., the exact character limit for text answers)
- API and webhook specifications
- Data export formats and options

**Red Flags: Never Include**
- Generic "survey tool" positioning without specific context
- Vague promises unsupported by documentation
- Features not confirmed in the knowledge base
- Incorrect technical specifications
- Conflating features across different plan tiers
- Retired product names: in the examples, "Insight Library" is now called **Research Projects**

---

## 6. Formatting & Structure

- **Clear headings and subheadings** for scannability
- **Bullets/lists** only where multiple points genuinely benefit from list format
- **Short paragraphs** (2 to 3 sentences max)
- Bold for key takeaways sparingly: one per major section at most
- Use **examples** relevant to personas to ground claims
- **Headlines are not full sentences**: no period at the end
- Use **numerals** for all numbers in headlines
- **H1** wraps the blog post title; **H2** wraps subheadings

### Headline Capitalization
- Capitalize letters before and after a hyphen in headlines (E-Commerce, E-Learning)
- No all caps
- Sentence case for subheadings; title case only for main titles

---

## 7. Grammar & Style Rules

### Punctuation
- **Oxford comma** always: "x, y, and z"
- **No en dashes**, ever
- **No em dashes**, ever. Use commas, colons, or split into two sentences
- Punctuation goes inside quotation marks (US style): `"great," she said`
- No spaces around hyphens
- **Hyphen use**: compound modifiers before a noun (well-known company), ranges (March 1-4)

### Voice & Pronouns
- Active voice strongly preferred
- Use "they/their" for singular when gender is unknown
- No first-person singular (I think, in my experience) in brand content
- Do not refer to people as "that": use "who"

### Common Spelling
- email (not e-mail)
- e-commerce (E-Commerce in headlines)
- startup (not start-up)
- internet (lowercase)
- okay (not OK)
- toward (not towards)
- afterward (not afterwards)
- worldwide (not world wide)

### Common Word Choices
- Do not use "period" when you mean a duration of time: "for two weeks" not "for a period of two weeks"
- "including" implies an inexhaustive list: don't follow with "and more" or "and others"
- "comprise" means "consist of": "is comprised of" is always wrong
- "that" for essential clauses; "which" (with commas) for nonessential clauses; "who" for people
- "farther" for physical distance; "further" for degree or time
- "such as" preferred over "like" for examples

### Quotations
- No block quotes in blog posts: paraphrase instead
- Block quotes are acceptable in case studies and testimonials
- Cite a direct source when quoting experts; don't quote Wikipedia

### Competition
- Never call competitors "market leaders"
- Don't criticize competitors publicly
- Describe Example Feedback's benefits more specifically and compellingly than competitors

---

## 8. Removing AI-Style Writing ("AI-isms")

Example Feedback content must sound like a person wrote it: direct, specific, confident. The following patterns are banned.

### Hard Bans
- **No en dashes or em dashes** (covered above, reinforced here)
- **No robotic filler phrases**: "it's worth noting that," "let's be clear," "to be honest," "quite frankly," "needless to say"
- **No AI transition stacking**: "Moreover," "Furthermore," "Additionally": restructure or use "and," "also," or "on top of that"
- **No chatbot artifacts**: "I hope this helps!", "Certainly!", "Great question!", "Feel free to reach out"
- **No hollow intensifiers**: "genuine," "truly," "real" (as in "a real improvement")
- **No vague openers**: "In today's landscape," "In an era where," "In the rapidly evolving world of"
- **No empty conclusions**: "The future looks bright," "Only time will tell," "As we move forward"
- **No "let's" transition openers**: "Let's explore," "Let's take a look," "Let's dive in": just start with the point

### Word Replacements
Always replace these:

| Replace | With |
|---|---|
| delve / delve into | explore, dig into, look at |
| landscape (metaphor) | field, space, industry, world |
| realm | area, field, domain |
| embark | start, begin |
| testament to | shows, proves, demonstrates |
| robust | strong, reliable, solid |
| comprehensive | thorough, complete, full |
| leverage (verb) | use |
| pivotal | important, key, critical |
| meticulous / meticulously | careful, detailed, precise |
| seamless / seamlessly | smooth, easy, without friction |
| utilize | use |
| game-changer / game-changing | describe what specifically changed |
| vibrant | describe what makes it active, or cut |
| thriving | growing, active (or cite a number) |
| deep dive | look at, examine, explore |
| unpack | explain, break down, walk through |
| intricate / intricacies | complex, detailed (or name the complexity) |
| holistic | complete, full (or describe what's included) |
| actionable | practical, useful, concrete |
| impactful | effective, significant (or describe the impact) |
| thought leader / thought leadership | expert, authority (describe their contribution) |
| best practices | what works, proven methods, standard approach |
| synergy / synergies | describe the actual combined effect |
| in order to | to |
| due to the fact that | because |
| serves as | is |
| boasts | has |
| commence | start, begin |
| cutting-edge | latest, newest, advanced |

### Patterns to Watch
- **Uniform paragraph length**: Vary deliberately. Some paragraphs can be one sentence.
- **Compulsive rule of three**: Vary groupings. Use two or four items instead of always three.
- **Bold overuse**: Strip bold from most phrases. One bolded phrase per major section at most.
- **Vague attributions**: "Experts believe," "Studies show" without citing the specific source. Either cite or state the claim directly.
- **Promotional vagueness**: Replace "a vibrant hub of innovation" with plain description: "has 12 startups"
- **Significance inflation**: "marking a pivotal moment in the evolution of...": state what happened and let the reader judge

---

## 9. Messaging Quick Reference by Use Case

| Use Case | Primary Audience | Core Message | Key Features | CTA Example |
|---|---|---|---|---|
| Product Development & UX | Product Managers, Designers, UX Researchers | Make roadmap decisions based on real user feedback | In-product surveys, event triggers, behavioral targeting, Research Projects | "Start collecting product feedback in minutes" |
| Marketing & Growth | Product Marketers, Growth Marketers, Marketing Ops | Use feedback to fuel personalization, reduce churn, improve campaigns | Email surveys, CRM integration, website surveys, multi-language support | "Connect Example Feedback to your marketing stack" |
| Customer Experience | Customer Success Managers, CX Leaders, Support Teams | Monitor satisfaction and catch issues before customers churn | CSAT/NPS surveys, support tool integration, alert systems | "Set up CSAT tracking in your help desk" |
| Research & Insights | User Researchers, Customer Insights Managers | Transform scattered feedback into structured, actionable insights | Multi-source aggregation, AI categorization, Research Projects, Ask AI | "Connect all your feedback sources" |

---

## 10. Quality Checklist

Before finalizing any deliverable:

- [ ] **Technical accuracy**: All claims verified against the Feature & Capability Knowledge Base
- [ ] **Persona alignment**: Serves primary personas with appropriate language and examples
- [ ] **Tone consistency**: Helpful, clear, confident, customer-centric, action-oriented
- [ ] **Framework connection**: References collect → analyze → act
- [ ] **Red flags cleared**: No generic positioning, AI filler, unsupported claims, internal persona names, or retired product names
- [ ] **Readability**: Short paragraphs, clear structure, scannable format
- [ ] **CTAs present**: Next steps are clear and actionable
- [ ] **No en dashes or em dashes**: Zero instances
- [ ] **No AI-isms**: Word replacements applied, filler phrases removed
- [ ] **US English**: Spelling, grammar, punctuation all correct

---

## 11. Common Mistakes

### Content
- "Example Feedback is a survey tool" → "Example Feedback turns customer feedback into product direction"
- Feature dumping without context or benefits
- "Best survey software" without specific evidence
- Writing for executives when targeting Product Managers
- Missing plan-specific limitations
- Using "Roadmap Builder" or "Insight Seeker" in external content
- Using a retired product name: in the examples, always say "Research Projects", never "Insight Library"

### Technical
- Wrong character limits, plan availability, or integration capabilities
- Not mentioning SDK installation or JavaScript code requirements
- "Easy integration" without specifying the method
- Claiming automation that requires manual setup

### Tone
- En dashes or em dashes (both banned)
- Robotic patterns and generic superlatives without proof
- "Leverage our comprehensive solution suite" → write like a human
- Talking about what the product does, not what customers achieve
