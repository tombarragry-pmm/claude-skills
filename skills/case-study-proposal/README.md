# case-study-proposal

Turns what a CSM or seller knows about a customer or prospect into a customer-facing Google Doc (a full case study proposal or quick LinkedIn post guidelines), backed by research across product usage, CS and CRM data, and logs it in Linear for marketing to approve.

Originally built: November 2026

## What it does

1. Asks the requester a few quick questions: customer or prospect, whether they have an angle, and the account details.
2. Researches the account in Hex (product usage), Custify (CS notes) and HubSpot (deal context), depending on customer or prospect and angle or no angle.
3. Writes out 1 to 2 story angles in full (what we found, evidence, the ask, trade-off, route), maps them to a list of needed story topics, and lets the requester pick.
4. Picks the route itself (full case study for a customer, full case study for a prospect, or a quick LinkedIn post) and builds the matching Google Doc from HTML, with yellow answer boxes and a promoted-post image.
5. Checks the doc, logs a To Do issue in the Linear Customer Stories project for the marketing owners, and replies with both links. Also runs in batch mode for a list of logos.

## Files

- `SKILL.md`: the instructions Claude follows.
- `references/case-study-customer.md`: doc template for a full case study with an existing customer.
- `references/case-study-prospect.md`: doc template for a full case study with a prospect.
- `references/linkedin-post-route.md`: doc template for quick LinkedIn post guidelines.

## Requirements

- Google Drive connector (create and download files), for building and checking the Google Doc.
- Linear connector, for the Customer Stories issue.
- Hex, HubSpot and (optionally) Custify connectors, for the research pass. The skill continues with whatever sources are available.
- An interactive question tool (buttons) is helpful but optional.

## Make it yours

The examples use Example Feedback, a fictional customer feedback platform. Replace the Fixed assets in `SKILL.md` (the sponsored-post image URL, customer stories links, reference stories, LinkedIn URLs), the case study owner and social owner names and emails, the Linear team, project and mentions, the product area names, and the list of case study topics your team needs.
