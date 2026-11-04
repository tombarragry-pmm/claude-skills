# tom-pmm-launch-linear-scaffolding

Sets up the Linear projects and issues for a feature launch, one project at a time, using a fixed launch playbook with naming, label and property rules.

Originally built: November 2026

## What it does

1. Asks for the launch level (Full new feature launch or Major functionality update) and the feature name.
2. Proposes the project list: 9 projects for a Full launch, a smaller default set of 5 for a Major update.
3. For each project in turn, proposes the issues, asks about every case-to-case item one by one, confirms the Initiative and Label, then creates the project and its issues in Linear.
4. Offers ad-hoc additions (extra projects or issues) that aren't in the standard playbook.
5. Wraps up with a summary of what was created and what still needs follow-up.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

- The Linear connector (MCP), with permission to create projects and issues.
- A button/choice tool for quick answers (the skill refers to `ask_user_input_v0` in Claude.ai). Without it, the same questions work as plain text.

## Make it yours

- The examples use Example Feedback, a fictional customer feedback platform, and a fictional feature called Feedback Inbox. Swap in your own.
- Edit the 9 projects, their issues, owners and default Labels to match your own launch playbook.
- Change the team name (Marketing), the Label set (Acquisition, Conversion, Brand, Operational) and the default status and priority to match your Linear workspace.
