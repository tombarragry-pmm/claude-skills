---
name: how-to-talk-about-our-integration
description: Checks customer-facing content and campaign ideas against the live feature brief for Example Feedback's MCP integration (Example Feedback is a fictional customer feedback platform) before anything is written. Use whenever someone at the company is drafting, brainstorming, or reviewing anything a customer or prospect will see that touches the MCP integration, the AI agent, the Assistant Layer, Feedback Agent, or connecting the product to AI assistants like Claude, ChatGPT or Slack. Triggers include landing pages, emails, changelog and in-app posts, social posts, ads, decks, sales talk tracks, battle cards, objection handling, demo scripts, help center articles and CS outreach, plus positioning brainstorms, launch planning, and any "how should we talk about our MCP" question. Do NOT use for internal product or research work such as validating a roadmap idea, synthesizing customer feedback, writing a PRD, or debugging the integration itself. Always offer this before writing MCP or agent messaging: the brief holds claims not yet cleared externally and positioning that goes stale fast.
---

# How to talk about our MCP integration

The examples use Example Feedback, a fictional customer feedback platform, and fictional launch names ("Assistant Layer", "Feedback Agent"). Replace them with your own product, feature names and brief location.

## Why this skill exists

A fast-moving launch has positioning that shifts week to week, and its feature brief contains three kinds of landmine that general knowledge cannot see:

1. Claims that are marked unverified or TBC and are not cleared to go external yet.
2. Competitive claims with a verification date on them, which decay.
3. Deliberate framing choices where the obvious way to say something is the wrong way to say it.

Writing launch copy without the brief produces output that is fluent, confident, and wrong in ways that need a full rewrite rather than an edit. This skill exists so that work lands on the product marketer's desk already correct, instead of getting sent back.

**This skill deliberately contains no copy of the brief's contents.** The brief is the source of truth and it changes. Everything substantive comes from the live page, every time.

## Step 1: Decide whether this skill applies at all

The discriminating test is **not** the person's job title. It is:

> Will the output be seen by a customer or a prospect?

If yes, and the subject touches the MCP integration, agents, the Assistant Layer, or connecting the product to AI assistants, this skill applies. That covers marketing, sales, support and CS work equally.

If the person is doing internal product or research work, this skill does not apply. Examples of work to leave alone: pressure-testing a roadmap call, synthesizing what customers actually said, prioritizing a backlog, writing a PRD or spec, investigating a bug, or analyzing adoption numbers. In these cases do not mention this skill at all. Offering it here is noise, and it interrupts someone who is reasoning rather than publishing.

Borderline case worth getting right: someone using the integration to *do research* is internal work, so stay quiet. Someone writing about the fact that the integration *can* do research is customer-facing, so offer.

## Step 2: Offer it, never assume it

Do not silently load the brief and start applying rules. Ask first, in roughly these words:

> Would you like me to also use the skill our product marketer created, to make sure your content or idea sits within the guidelines in the feature brief?

Present this as a selectable option rather than an open prose question, using the interactive question tool available on the surface (`ask_user_input_v0` in Claude.ai). People answer buttons and skip past questions, and this needs an actual answer before any drafting starts.

Ask **once per conversation.** Once someone has said yes, apply the brief silently for the rest of the session and stop asking. Once someone has said no, respect it and do not re-offer unless they change task.

## Step 3: Get the brief, or stop

Fetch the live page:

- URL: `<YOUR_FEATURE_BRIEF_URL>`
- Page ID: `<YOUR_NOTION_PAGE_ID>`

If the Notion connector is unavailable, try these in order:

1. Ask them to connect Notion. It is the fastest fix and it makes every future run work.
2. Ask them to open the link, export the page, and upload it.

If neither happens, **stop**. Say plainly that you cannot check their content against the brief and that anything you write about the integration may contradict approved positioning. Then either help with a part of the task that does not touch launch messaging, or hand it back. Do not reconstruct the brief from memory, from other skills, from the product itself, or from what the positioning was last time. A confident guess is the exact failure this skill prevents.

## Step 4: Interrogate the brief before writing

Read the whole page, then answer these questions from it. Do not assume the answers carry over from a previous session.

**Clearance and timing**
- Does the brief permit external mention right now, and to whom?
- What is the release timing, and is there an early access stage?
- Which items are marked TBC, unverified, or pending? Those are not usable externally without checking with the brief's owner first.
- Do any competitive claims carry a verification date? If that date is more than roughly a month old, treat the claims as needing a re-check before they go external.

**Positioning**
- How does the brief describe company-level positioning, and how does this feature fit into it?
- What is the one-sentence description, and the hero tagline?

**The differentiation argument**
- What does the brief say is genuinely differentiating, and what does it say is *not* differentiating?
- Are there framings the brief tells you to avoid, or to substitute with different language?
- Are there competitive angles the brief explicitly tells you not to lean on?

**Boundaries of what is true**
- What does the brief say the feature can and cannot do?
- What does the brief admit the company cannot control or does not offer? Never write past these lines to make the story neater.

**Audience and language**
- Which persona is this piece for, and what does the brief say that persona cares about?
- Which taglines and raw customer phrases does the brief offer for that persona? Prefer these over inventing new lines, because they have been chosen deliberately.

## Step 5: Flag conflicts, do not quietly fix them

If their draft, idea, or brief-to-you conflicts with the feature brief, say so before writing. Be specific and short:

> Heads up, one thing to change. You have framed this as [their version]. The brief says [what the brief says], because [the reason given in the brief]. I would go with [corrected version].

Then ask how they want to proceed as a selectable choice, not a prose question. Give them the corrected version, their version with the risk stated, or a rethink of the angle.

Flag every conflict, not only the serious ones. A quiet correction teaches nobody, and the person walks away still holding the wrong model. Naming it is most of the value here.

Two things that always get an explicit flag, even if the person seems certain:

- They want to use a claim the brief marks unverified, TBC, or pending.
- They want to lean on a competitive or differentiation angle the brief warns off.

## Step 6: Write

Once the brief is loaded and conflicts are settled, write the thing. Pull language from the brief's taglines, key messaging phrases, and pain-point mapping rather than inventing fresh claims.

This skill governs **substance**, not format. Other skills own format, and they still apply on top: use the relevant skill for in-app posts, changelog entries, landing page copy, emails, slides, or visuals. If a format skill and the brief disagree on a factual claim, the brief wins.

House style still applies throughout: no em dashes or en dashes, rewrite the sentence instead. Plain language over jargon. Outcome-focused titles. Precise product terminology.

## Never do these

- Never write launch or agent messaging from memory when the brief was unreachable.
- Never present an unverified or TBC item as settled fact.
- Never smooth over a limitation the brief is candid about, in order to make the copy stronger.
- Never repackage the brief wholesale into a customer-facing asset. It is an internal document and it contains competitive intelligence, unverified answers, and internal notes.
