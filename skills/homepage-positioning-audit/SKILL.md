---
name: homepage-positioning-audit
description: Audit a homepage or landing page against Fletch PMM's public positioning and messaging frameworks. Use this skill whenever a marketer wants to review, audit, critique, or sanity-check a homepage, landing page, or page prototype, including phrasing like "audit this page", "is this homepage clear?", "review this against Fletch", "Fletch-check this", "give me Anthony Pierri's take", or simply sharing a URL or screenshot of a page draft. Triggers on both URLs and screenshots. Always use this skill for Fletch-style page audits. Do not freestyle homepage critique without it.
---

# Homepage Positioning Audit

A skill for auditing homepages and landing page prototypes against Fletch PMM's (Anthony Pierri's) public positioning and messaging frameworks. The deliverable is always an HTML artifact the marketer can read, share, and act on.

The examples use Example Feedback, a fictional customer feedback platform. The method works for any B2B SaaS page.

## Before you start

At the top of your reply (in chat, not in the artifact), include this note **once per conversation**:

> *Heads up: for the sharpest audit, run this skill inside the Claude project that holds your company's positioning context. Without it, the audit will still run, but it can't flag where the page diverges from your actual positioning.*

Then proceed with the audit. Don't repeat the note on follow-up turns in the same conversation.

## Inputs

The marketer will give you either:
- **A URL:** fetch it with `web_fetch` to get the live copy
- **A screenshot:** read all the copy directly from the image

In both cases, every conclusion you draw must quote the exact copy from the page. Never paraphrase the page when making a finding. If a piece of copy is unreadable in a screenshot, say so and skip it rather than guess.

## Frameworks (the lens you audit against)

You're applying Fletch's playbook for B2B SaaS homepages. Use these in the priority order below.

### 1. The 4 positioning questions (the backbone)

A clear homepage answers these for the visitor inside the first scroll:
1. **What is it?** What category of product is this
2. **Who is it for?** What kind of company / role / situation
3. **What does it replace?** Current alternative or status quo
4. **Why is it better?** The differentiation

For each, judge **clear / partial / unclear**, with quoted evidence from the page.

### 2. The homepage section flow

Fletch's recommended structure:
- **Hero:** answers "what is it" + "who's it for" in one breath, ideally referencing the situation
- **Problem section:** the pain the champion currently has, in their lived experience
- **Solution intro:** how the product addresses that pain (high-level, capability-led)
- **Value propositions:** typically 3, each tied to a specific capability that solves part of the problem
- **(Optional below):** segmentation by persona/use-case, social proof, deeper feature dives, FAQ, CTA

Identify which of these sections actually exist on the page, which are missing or weak, and where the order breaks down.

### 3. Capabilities > Features > Benefits

- **Capabilities** = what someone *does* with the product (action-oriented, tool-agnostic)
- **Features** = the technical building blocks that power capabilities
- **Benefits** = the outcomes / why the capability matters

Fletch's rule: **lead with capabilities**, not abstract benefits. Vague outcome copy ("drive growth", "make better decisions", "unlock insights") is a flag. Look for action verbs tied to a specific job.

### 4. Audience anchoring

The page should be anchored on one of:
- **Vertical:** a company type or persona/department
- **Horizontal:** a shared situation/JTBD (process or desired outcome)

Diagnose: who is this page for? Is the anchor specific or vague? Vague = a finding.

Also locate the page on Fletch's specificity slider:
- **Specific use-case** = small audience, high resonance ✅ (Fletch's usual recommendation)
- **Middle** = let visitors self-select into sub-pages
- **Platform message** = large audience, low resonance ⚠️ usually too broad

### 5. Common Fletch flags to watch for

- Buzzwords with no specificity ("AI-powered", "next-gen", "all-in-one")
- Wordplay or clever taglines that obscure meaning
- Outcome copy aimed at execs who never visit the page (vs the actual buyer/user)
- Trying to talk to multiple personas in one breath
- Hero that requires the visitor to already know what category the product is in
- Problem section that describes a pain abstractly instead of in the champion's lived experience
- Heavy reliance on benefits with no capability copy backing them up

## Workflow

1. **Fetch or read the page.** URL → `web_fetch`. Screenshot → read directly.
2. **Map copy to the section flow.** Identify Hero / Problem / Solution / Value Props (and anything below). Note what copy belongs to each, in order.
3. **Run the 4 positioning questions check.** For each, find the quoted copy that answers it (or note that nothing does) and grade clear / partial / unclear.
4. **Run cross-cutting checks:** capabilities-vs-benefits, audience anchoring, specificity, common flags.
5. **Compile findings** with severity:
   - **critical:** breaks core positioning clarity (e.g., visitor can't tell what the product is)
   - **major:** meaningful weakness that costs resonance or conversion
   - **minor:** nit, polish, sharpening opportunity
6. **Build the artifact** (structure below).
7. **Close the chat reply** with 3 to 5 specific follow-up offers (e.g., "want me to draft a sharper hero?", "want to workshop the problem section?"). Do not include rewrites in the audit itself.

## Output: the artifact

Always create a single HTML artifact. Make it scannable, not a wall of text.

### Structure

**TL;DR (top of the artifact)**
- One-sentence verdict on the page
- Scoreboard for the 4 positioning questions: clear / partial / unclear, each with a short quote of the supporting copy (or a "nothing on the page answers this" note)

**Section-by-section findings**
For each section identified on the page (Hero, Problem, Solution, Value Props, etc.):
- Section name + the exact copy that's in it (rendered as a quoted block)
- A list of findings, each with:
  - Severity badge (critical / major / minor)
  - The exact quoted phrase being critiqued
  - The Fletch principle it bumps against (named, briefly)
  - A short "what to consider": diagnostic only, **not** a rewrite

**Cross-cutting checks**
A short panel covering:
- **Audience anchor:** vertical / horizontal / vague (with quoted evidence)
- **Specificity:** use-case / middle / platform (where the page sits)
- **Capabilities vs benefits balance:** observation with quoted examples
- **Top recurring flags:** the 2 or 3 patterns showing up most often

**Suggested next moves**
A small list (3 to 5) of concrete things the marketer could ask Claude to do next. Examples:
- "Draft 3 sharper hero options anchored on [specific situation]"
- "Rewrite the problem section using the champion's lived experience"
- "Generate value prop copy that leads with capabilities"
- "Audit a competitor's hero against ours"

### Visual style

Follow your brand's sensibility: clean, readable, restrained. Specifically:
- Severity badges color-coded: critical = red, major = amber, minor = neutral gray
- Quoted page copy: rendered in a styled blockquote so it's visually distinct from your commentary
- The 4-positioning-question scoreboard should sit at the top as a row of pills or a small table, not buried lower
- Use clear hierarchy with headings: the marketer should be able to scan section names and severity badges first, then read into the findings they care about
- Make it work inline in chat on a laptop screen

## Hard rules

1. **Every finding must quote exact copy from the page.** No paraphrasing, no "the hero is unclear". Instead: "the H1 'Turn every voice into your next move' fails the *what is it* question because [reason]."
2. **The audit is diagnostic only.** No rewrites or suggested copy inside the artifact. Rewrites come in follow-up turns if the marketer asks.
3. **Severity is honest.** If something genuinely passes Fletch, say so. Don't manufacture critical findings to look thorough.
4. **No generic Fletch-101 explanations in the artifact.** The marketers running this know the framework. Cite the principle by name and move on.
5. **Cite sections by their exact heading or position** ("the third value prop card", "the section starting with 'Built for product teams'") so the marketer knows exactly what you mean.
6. **If you can't audit something** (copy unreadable in a screenshot, page didn't load, framework doesn't apply), say so explicitly rather than fudging.
7. **Don't over-quote.** When the same phrase recurs, quote it once and reference it.
8. **Scope is copy and messaging only.** Do not critique visual design, layout, imagery, or color choices. Early prototypes haven't been through a designer yet, and design feedback is out of scope for this audit. If a marketer asks Claude to audit visual design, point them to the right channel: this skill is for Fletch messaging review.
