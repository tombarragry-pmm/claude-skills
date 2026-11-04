# webinar-organization

Walks a first-timer through running a partner webinar end to end, from kickoff to repurposing, so nothing important gets forgotten. Produces a Word brief and a Linear project with a standard task list along the way.

Originally built: November 2026

## What it does

1. Works out which of five stages the user is at (kickoff, brief and setup, promotion, two weeks out, post-webinar) and starts there.
2. At kickoff, collects the essentials (partner, topic, date in two time zones, speakers, audience, KPI, contacts) and flags the questions people usually forget to ask the partner.
3. Generates the webinar brief as a .docx using a fixed six-section template.
4. Creates the Linear project and the 29 standard tasks (all with No priority), or audits an existing project against that list.
5. Guides promotion, the two-weeks-out prep (dry run, slides, polls) and the post-webinar work, including a narrative Slack recap with a worked example.

## Files

- `SKILL.md`: the instructions Claude follows.

Not included: the original folder also held a packaged `.skill` archive of the same skill. It was left out on purpose.

## Requirements

- The docx skill, to build the Word brief.
- The Linear connector (MCP), to create or audit the project and tasks.
- Optional: a separate `linkedin-content` skill, which this skill hands LinkedIn drafting off to.

## Make it yours

- All people (Jordan Lee, Sam Rivera, Alex Morgan, Casey Nguyen, Taylor Brooks, Morgan Patel), the partner (Fabrikam) and everything in the Slack recap example are fictional. Replace the team table and default assignees with your own team.
- Replace Example Feedback (a fictional customer feedback platform) with your company name, and `<YOUR_TEAM_KEY>` with your Linear team key.
- Swap the tools if yours differ: Contrast (webinar platform), Webflow (landing pages), Mixpanel (page views), Customer.io (email), Crossbeam (partner data sharing).
- Replace the placeholder landing page URLs (`https://example.com/webinars/...`), the standing bio, and the default registrant target (100).
