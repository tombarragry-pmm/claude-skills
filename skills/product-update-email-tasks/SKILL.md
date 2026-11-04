---
name: product-update-email-tasks
description: Set up the Linear project and standard issues for a monthly product update email at Example Feedback (a fictional customer feedback platform). Use this skill whenever the user needs to kick off a new product update email cycle, including phrases like "set up the product update", "create the issues for this month's email", "scaffold the product update newsletter", "it's product update time", "start the [month] product update", or any mention of setting up or kicking off a monthly product update email. The skill builds the project first, then the three standard issues inside it. Always use this skill for monthly product update email setup. Do not create the project or issues without it.
---

# Product Update Email Tasks Skill

## What This Skill Does

Scaffolds the Linear project and standard issues for a monthly product update email. Run this at the start of each month's product update cycle.

The examples use Example Feedback, a fictional customer feedback platform, and a fictional content lead called Sam Rivera. Replace them with your own product and team.

Two phases:
1. **Gather information:** confirm the month, features to cover, and any additional context
2. **Build in Linear:** create the project first, then the three issues in order

Never create issues before confirming the feature list with the user.

---

## Phase 1: Gather Information

Before touching Linear, confirm:

**Required:**
- Month and year (e.g. July 2026)
- Bigger updates to cover (usually 2 to 4 features)

**Optional (note as TBD if unknown):**
- Additional content to promote in the footer (webinar recordings, blog posts, etc.)

**Defaults (apply unless told otherwise):**
- Target date: last day of the month
- Priority: High
- Team: Marketing
- Assignee for all issues: the user ("me")
- Design sub-issue: unassigned, no description

---

## Phase 2: Build in Linear

### Step 1: Create the project

```
Title:       [Month Product Update] Newsletter
             e.g. [July Product Update] Newsletter

Summary:     Launch a product update email this month, via email, covering the highlighted features

Description:
**This month's bigger updates:**
- [feature 1]
- [feature 2]
- [feature 3 if applicable]

**Additional content to promote:**
- [item] or TBD

Priority:    High
Status:      In Progress
Team:        Marketing
Lead:        me (the user)
Label:       Conversion
Initiatives: Retention AND Activation (always both)
Start date:  today
Target date: last day of the month
```

### Step 2: Create Issue 1: Email copy and creation

```
Title:       [Month] product update - email copy and creation
             e.g. July product update - email copy and creation

Description:
Write copy and build the [Month] product update email in Customer.io Design Studio.

**Features to cover:**
- [feature 1]
- [feature 2]
- [feature 3 if applicable]

**Footer:**
Additional content TBD - see linked content team ask issue.

**Target send date:** [last day of month, written out e.g. July 31, 2026]

Assignee:    me (the user)
Priority:    High
State:       Todo
Label:       Email marketing
Project:     [project created in Step 1]
Team:        Marketing
```

### Step 3: Create Issue 2: Email design (sub-issue of Issue 1)

```
Title:       Email design - [Month] product update
             e.g. Email design - July product update

Description: (leave empty, do not add anything)
Assignee:    unassigned
Priority:    High
State:       Todo
Label:       Email marketing
Parent:      Issue 1 (the email copy and creation issue)
Project:     [project created in Step 1]
Team:        Marketing
```

### Step 4: Create Issue 3: Content team ask

```
Title:       Ask content team - additional content for product update footer

Description:
Check with Sam / the content team what additional content should be featured in the footer of the [Month] product update email.

This could include blog posts, guides, how-tos, or other resources published or promoted this month. Feed the answer back into [Issue 1 identifier] before copy is drafted.

Assignee:    Sam Rivera (content-lead@example.com)
Priority:    High
State:       Todo
Label:       Email marketing
Project:     [project created in Step 1]
Team:        Marketing
```

---

## Key Reference Details

**Content lead's Linear user ID:** `<CONTENT_LEAD_LINEAR_USER_ID>` (content-lead@example.com)

**Issue creation order matters:** Always create Issue 1 first. Use its returned identifier as the `parentId` for Issue 2, and reference it by identifier in the description of Issue 3.

**Labels are two different namespaces:**
- Project-level label: `Conversion`
- Issue-level label: `Email marketing` (apply to all three issues)

**Initiatives:** Always set both "Retention" and "Activation" on the project.

---

## What Changes Month to Month

- Month and year in all titles and descriptions
- Feature list in the project description and Issue 1 description
- Additional content to promote in the footer (if known)
- Target date (last day of the relevant month)

Everything else is fixed.
