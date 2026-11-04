# tom-pmm-nurture-email

Writes short, plain text nurture emails to leads and prospects, sent from a named person with a single clear CTA (usually booking a demo).

Originally built: November 2026

## What it does

1. Asks for the trigger (event, content download, free trial), sender, booking link, recipient segment and any hook.
2. Picks the matching playbook: post-event follow-up, content download follow-up, or free trial check-in.
3. Drafts the email in the house voice, using value props and a matching customer story where useful.
4. Outputs a subject line, preview text and body, then checks it against a generation checklist.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

None.

## Make it yours

- The examples use Example Feedback, a fictional customer feedback platform. Replace the product name, value props and feature names (e.g. Feedback Inbox).
- Every customer story, stat and URL in the customer stories table is fictional (including the "+15%" response-rate stat). Replace them with your own published, verified stories and numbers before using this for real.
- Adjust the voice rules, example emails and sender names to match your team.
