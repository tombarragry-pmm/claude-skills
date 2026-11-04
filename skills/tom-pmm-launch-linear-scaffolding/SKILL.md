---
name: tom-pmm-launch-linear-scaffolding
description: Set up Linear projects and issues for a feature launch at Example Feedback (a fictional customer feedback platform). Use this skill whenever the user asks to scaffold a launch in Linear, build the projects for a launch, set up Linear for a feature launch, kick off launch planning, or create launch tickets. Trigger on phrases like "scaffold the launch", "set up Linear for the [feature] launch", "build the launch projects", "create the launch tickets", "I'm launching [X]", "let's plan the [feature] launch", or any mention of building launch workstreams in Linear. Always use this skill before creating any launch-related projects or issues in Linear, even if the request seems simple.
---

# Launch Linear Scaffolding Skill

## What This Skill Does

Creates the full set of Linear projects and issues for a feature launch, following the user's standard launch workflow. The skill enforces project bucketing logic, naming conventions, and property defaults, and walks through projects one at a time so nothing gets created wrong in bulk.

The examples use Example Feedback, a fictional customer feedback platform, and a fictional feature called Feedback Inbox. Replace them with your own product and features.

This skill does NOT read the launch matrix (for example a Notion page) at runtime. The task lists are baked in below. If the matrix changes meaningfully, update this skill.

---

## How To Use This Skill

The workflow has hard sequential gates. Do not skip ahead. Do not batch projects.

### Step 1: Ask the two opening questions

Before doing anything else, ask the user:

1. **What level of launch is this?** Use `ask_user_input_v0` with options: "Full new feature launch" / "Major functionality update or change"

2. **What's the feature name?** This is free text (the user types it), used to prefix every project and issue, e.g. `[Feedback Inbox Launch]`. Don't use buttons here.

Do not proceed until both are answered.

If the user names a launch type outside these two (e.g. "Much-needed change" or "Minor change"), stop and confirm: this skill is only for Full launches and Major functionality updates. Smaller launches don't typically warrant a full Linear scaffold.

### Step 2: Propose the project list

Based on the launch level, propose the project list. Show the user the full list at once so they can react before any creation happens.

**For Full new feature launches** propose all 9 projects (see "The 9 Projects" below).

**For Major functionality update or change** propose the smaller default set (5 projects) and tell the user which other projects they can pull in from the Full launch playbook if they want. See "Major Launch Defaults" below.

Then ask the user for approval using `ask_user_input_v0` with options: "Looks good, proceed" / "I want to adjust the list". If they want to adjust, switch to free text and let them tell you what to change.

### Step 3: For each project (one at a time)

Run this loop for each project the user approved. Do NOT move to the next project until the current one is fully created in Linear.

For each project:

1. **Propose the issues** for that project.
   - For Full launches: include all ✅ items by default. For each ⚡️ case-to-case item, ask the user using `ask_user_input_v0` with the question "Include an issue for [item name]?" and options "Yes" / "No". One tool call per case-to-case item. Don't batch them.
   - For Major launches: include all ✅ items for the Major column by default. For each ⚡️ item, ask the user the same way: `ask_user_input_v0` with "Include an issue for [item name]?" and options "Yes" / "No". The user may also pull in items from the Full launch playbook for this project. Ask via free text if they want any extras.
2. **Confirm Initiative.** Ask the user which Linear Initiative this project rolls up to. Default assumption: one Initiative per launch (e.g. "Feedback Inbox Launch") that all 9 projects roll up to. Use `ask_user_input_v0` with options like "Use the same Initiative as the last project" / "Use a different one", falling back to free text if they pick "different".
3. **Confirm Label.** Propose the default Label for this project (see the project tables below). Use `ask_user_input_v0` with the question "Label for this project?" and options "Acquisition" / "Conversion" / "Brand" / "Operational". Pre-select or mention the default in the question text so the user knows what's recommended.
4. **Build the project in Linear** with the agreed properties.
5. **Build the issues in Linear**, each one mirroring the project's Label.
6. Confirm completion using `ask_user_input_v0` with options "Continue to next project" / "Pause here", then move on if continuing.

### Step 4: Ad-hoc additions

Before wrapping up, ask the user if there's anything else to build that wasn't in the standard matrix. Ideas sometimes come up offline and don't fit the generic list.

Use `ask_user_input_v0` with the question "Anything else to add?" and options "Yes, add something" / "No, all done".

If "No, all done": skip to Step 5.

If "Yes, add something": run this loop:

1. Ask via `ask_user_input_v0` "Project or issue?" with options "New project" / "New issue in an existing project".
2. **If new project:**
   - Ask for the project name (free text, the user types it). Apply the `[Feature Name Launch]` prefix automatically.
   - Confirm Label via `ask_user_input_v0` with options "Acquisition" / "Conversion" / "Brand" / "Operational".
   - Confirm Initiative via `ask_user_input_v0` with options "Same as the other projects" / "Different one" (fall back to free text if different).
   - Build the project with the standard property defaults (Team: Marketing, Status: To-Do, Priority: High, Lead/Members blank, Launch Date blank).
   - Then ask via `ask_user_input_v0` "Add issues to this project now?" with options "Yes" / "No, leave it empty for now".
   - If yes, loop: ask for each issue name (free text), apply the prefix, mirror the project's Label, create it, then ask "Another issue?" via buttons.
3. **If new issue in an existing project:**
   - Show the user the list of projects already created and ask via `ask_user_input_v0` which one it goes in (use the project names as options).
   - Ask for the issue name (free text). Apply the `[Feature Name Launch]` prefix.
   - Mirror the parent project's Label.
   - Create the issue.
4. After each ad-hoc creation, ask via `ask_user_input_v0` "Anything else?" with options "Yes, add another" / "No, all done". Loop until "No, all done".

### Step 5: Wrap up

When all projects are built, give the user a summary:
- Number of projects created
- Total issues created
- Anything that was skipped or needs follow-up (Initiatives not yet created, Members to assign, Launch Dates to fill in)

---

## Default Properties

### Project-level (set on every project)

| Property | Default |
|---|---|
| Team | Marketing |
| Status | To-Do |
| Priority | High |
| Lead | TBC (leave blank, the user assigns later) |
| Members | TBC (leave blank, the user assigns later) |
| Launch Date | blank |
| Initiative | confirm per project |
| Label | confirm per project: one of Acquisition, Conversion, Brand, Operational |

### Issue-level (set on every issue)

| Property | Default |
|---|---|
| Team | Marketing |
| Status | To-Do |
| Assignee | TBC (leave blank, the user assigns later) |
| Priority | blank |
| Label | mirror the parent project's Label |

---

## Naming Convention

Every project and issue title must be prefixed with `[Feature Name Launch]`. Examples:

- Project: `[Feedback Inbox Launch] Pre-launch alignment`
- Issue: `[Feedback Inbox Launch] Internal User Council launch`

The feature name comes from the answer to Step 1, Question 2. Do not abbreviate or modify it.

---

## The 9 Projects (Full New Feature Launch)

Each project below lists its default Label and the issues to create. Items marked ⚡️ are case-to-case: ask the user before including.

### Project 1: Pre-launch alignment
**Default Label:** Operational
**Owners:** Product Marketing (with Product support)

Issues:
- Internal User Council launch (share prototype with stakeholders)
- PO/PM to guide PMM through feature
- Research Team & PMM sync
- Update / add to Customer Advisory Board
- Decision around Beta Launch or Early Access
- Dedicated Slack channel (beta)
- Early Access segment in Customer.io
- Join the waitlist newsletter
- Create Feature Brief for whole team
- Update Feature Brief based on Beta feedback
- Claude knowledge base updated
- Product training (technical)
- Kick off call & brainstorm (marketing)
- Office Hours: Tour & Messaging overview
- Office Hours: post launch messaging check
- ⚡️ Sneak Peek webinar

### Project 2: Sales, Support & CSM enablement
**Default Label:** Operational
**Owners:** Product Marketing (with Support and Sales support)

Issues:
- 1-pager (Sales & Support collateral)
- Technical FAQ
- FAQ article: best practices / further guides
- Plain text email template announcing feature for CSMs
- Plain text email template announcing feature for Sales
- Update competitive battle cards
- ⚡️ Leave-behind deck update
- ⚡️ Competitive comparison sheet

### Project 3: Email: Launch broadcasts
**Default Label:** Conversion
**Owners:** Product Marketing

Issues:
- Dedicated launch email
- Monthly Product Update email inclusion
- Communication to leads who closed-lost based on the lack of this feature

### Project 4: Email: Lifecycle & activation
**Default Label:** Conversion
**Owners:** Product Marketing (with Customer Marketing)

Issues:
- Event-based adoption & milestone emails
- Updated customer onboarding emails
- ⚡️ Update post-sale lifecycle emails

### Project 5: Website
**Default Label:** Acquisition
**Owners:** Product Marketing + Website Team

Issues:
- Update homepage
- Feature/Integration page (update or create)
- Update solution pages
- ⚡️ Pricing page update

### Project 6: Content & SEO
**Default Label:** Acquisition
**Owners:** Content / SEO team

Issues:
- Dedicated launch blog post
- Dedicated case study
- ⚡️ Update review site messaging + graphics

### Project 7: In-product & changelog
**Default Label:** Conversion
**Owners:** Product Marketing

Issues:
- Changelog update
- In-app tour tooltip (via Product)
- Interactive tour (in your interactive demo tool, e.g. Arcade)

### Project 8: Webinars & live events
**Default Label:** Acquisition
**Owners:** Product Marketing + Product

Issues:
- Product webinar
- ⚡️ Update overview video
- ⚡️ Update Getting Started webinar
- ⚡️ Event collateral

### Project 9: Social & demand gen
**Default Label:** Acquisition
**Owners:** Demand + Content + Product Marketing

Issues:
- ⚡️ Social posts
- ⚡️ Influencer campaign
- ⚡️ Paid promo or ABM campaign

---

## Major Launch Defaults

For Major functionality update or change launches, the default scaffold is smaller. Propose these 5 projects by default:

1. **Pre-launch alignment** (reduced issue set, see below)
2. **Sales, Support & CSM enablement** (reduced issue set)
3. **Email: Launch broadcasts** (Monthly Product Update only, no dedicated launch email)
4. **In-product & changelog** (Changelog only by default)
5. **Website**: ⚡️ confirm whether to include

After proposing the default 5, tell the user: "You can also pull in items from these Full launch projects if needed: Email Lifecycle, Webinars, Content & SEO. Social & demand gen is rarely in scope for Major launches. Flag it if you want it."

If the user asks to add a Full launch project that's not in the Major default, confirm once: "Just confirming you want to add [X]. This isn't standard for a Major launch. Proceed?"

### Major launch reduced issue sets

**Pre-launch alignment (Major):**
- PO/PM to guide PMM through feature
- Update / add to Customer Advisory Board
- Create Feature Brief for whole team
- Product training (technical)
- Office Hours: Tour & Messaging overview
- ⚡️ Internal User Council launch
- ⚡️ Research Team & PMM sync
- ⚡️ Decision around Beta Launch or Early Access
- ⚡️ Dedicated Slack channel
- ⚡️ Early Access segment in Customer.io
- ⚡️ Office Hours: post launch messaging check

**Sales, Support & CSM enablement (Major):**
- 1-pager
- Technical FAQ
- FAQ article: best practices
- Plain text email for CSMs
- Plain text email for Sales
- ⚡️ Update competitive battle cards

**Email: Launch broadcasts (Major):**
- Monthly Product Update email inclusion
- ⚡️ Dedicated launch email

**In-product & changelog (Major):**
- Changelog update
- ⚡️ In-app tour tooltip
- ⚡️ Interactive tour (interactive demo tool)

**Website (Major):**
- ⚡️ All website tasks are case-to-case for Major launches. Confirm each.

---

## Important Rules

1. **One project at a time.** Never batch-create multiple projects in Linear in a single pass. Confirm issues, confirm Initiative, confirm Label, build project, build issues, then move on.

2. **Naming is non-negotiable.** Every title must start with `[Feature Name Launch]`. No exceptions.

3. **Don't read the launch matrix.** The matrix is baked in here. Trust this list, not the source doc.

4. **Case-to-case items always ask, item by item.** Never auto-include a ⚡️ item, even if it seems obvious. For each ⚡️ item, ask explicitly: "Do you want an issue for [item name]?" Don't batch the questions. Don't assume yes from earlier answers. The user decides each one separately.

5. **Members and Lead stay blank.** The user assigns these in the Linear UI after creation. Don't try to assign people.

6. **Label confirmation is required.** Always propose the default Label, but wait for the user to confirm or override before creating the project.

7. **Mirror project Label on issues.** Issues take the same Label as their parent project. No exceptions, no per-issue Label decisions.

8. **If anything's unclear, stop and ask.** Better to clarify than create the wrong thing in Linear.

9. **Use buttons, not free text, wherever possible.** The user is often on mobile or short on time. Use `ask_user_input_v0` for every yes/no, every multiple choice, and every approval gate. Only fall back to free text when the answer genuinely can't be a button (e.g. typing the feature name, naming a new Initiative).

---

## Linear Tool Notes

Use the Linear MCP tools to create projects and issues. Before creating anything:

- Look up the Marketing team ID
- Look up the Label IDs for Acquisition / Conversion / Brand / Operational (create them if they don't exist, but flag this to the user first)
- Look up the Initiative ID the user specifies (or create one if needed, flag first)

When creating projects, use `save_project` (or equivalent project-creation tool). When creating issues, use `save_issue` and link them to the project.

If a tool call fails, stop and surface the error to the user rather than retrying blindly.
