# product-update-email-tasks

Kicks off a monthly product update email cycle by creating one Linear project and the three standard issues inside it (copy and build, design, and a content ask for the footer).

Originally built: November 2026

## What it does

1. Confirms the month and year, the 2 to 4 bigger updates to cover, and any extra content for the footer.
2. Creates the Linear project with fixed defaults (title pattern, label, initiatives, target date at month end).
3. Creates Issue 1, email copy and creation, assigned to the user.
4. Creates Issue 2, email design, as an unassigned sub-issue of Issue 1.
5. Creates Issue 3, an ask to the content lead about footer content, linked back to Issue 1.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

- The Linear connector (MCP), with permission to create projects and issues.

## Make it yours

- The examples use Example Feedback, a fictional customer feedback platform, and a fictional content lead, Sam Rivera. Replace them with your own product and teammate.
- Replace `<CONTENT_LEAD_LINEAR_USER_ID>` and `content-lead@example.com` with your content lead's Linear user ID and email.
- Change the team (Marketing), labels (Conversion, Email marketing) and initiatives (Retention, Activation) to the ones in your Linear workspace.
- If you don't build emails in Customer.io Design Studio, change the tool named in Issue 1.
