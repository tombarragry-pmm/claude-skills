---
name: tom-pmm-cio-email-creation
description: Create Customer.io Design Studio emails for Example Feedback (a fictional customer feedback platform) lifecycle campaigns, onboarding sequences, and activation programs. Use this skill whenever the user asks to build, create, or write any email in Customer.io, including campaign emails, journey actions, activation nudges, or lifecycle sends. Trigger on any mention of "build this email", "create an email in Customer.io", "add an email to this campaign", or "write the Customer.io email". Always use this skill before writing any Design Studio markup or calling the Customer.io MCP to create email actions or templates.
---

# Customer.io Email Creation Skill

## Overview

This skill governs how Claude creates emails in Customer.io for Example Feedback. It covers copy, Design Studio markup, sender identities, and the full API workflow to create, link, and publish email actions inside campaigns or journeys.

The IDs, token paths and URLs below are placeholders. Fill in the "Environment Reference" section at the bottom with your own workspace values before using this skill.

---

## Step-by-Step Workflow

1. **Pick the right base template** (see Template Reference below)
2. **Agree copy and confirm CTA URL:** subject, preheader, body angles, and the exact CTA URL must all be locked before building. Never proceed without a confirmed URL.
3. **Create the action in the campaign** via the campaigns API (if needed)
4. **Create the Design Studio email** via POST /v1/environments/<YOUR_WORKSPACE_ID>/design_studio/emails with the full content, envelope (from_id + reply_to_id), and parent_folder_id
5. **Link the email to the campaign action** via POST /design_studio/emails/{node_id}/link
6. **Publish** via POST /design_studio/emails/{node_id}/publish
7. **Verify** by reading the template to confirm content landed

**CRITICAL: Never stop after link. A linked but unpublished email leaves the action sending nothing.**

---

## Template Reference

Four base templates live in a dedicated "Claude Emails" folder (folder ID: `<YOUR_TEMPLATES_FOLDER_ID>`) in Customer.io Design Studio. Always start from one of these.

| Name | Node ID | Use when |
|---|---|---|
| Template: Webinar invite | `<WEBINAR_TEMPLATE_NODE_ID>` | Event/webinar announcements, date-anchored CTAs |
| Milestone with Inspiration | `<MILESTONE_TEMPLATE_NODE_ID>` | Milestone celebrations, progress nudges, tip-style nurture emails |
| Template: Multiple Use Cases | `<USE_CASES_TEMPLATE_NODE_ID>` | Multi-section emails, feature discovery, onboarding |
| Template: 3 Step Setup | `<SETUP_TEMPLATE_NODE_ID>` | Step-by-step setup flows, activation sequences |

To use a template: fetch its content via GET /v1/environments/<YOUR_WORKSPACE_ID>/design_studio/emails/{node_id} and use content.html as the base markup. Replace only the content nodes, keep the structure intact.

To match an existing email's structure: use GET /v1/environments/<YOUR_WORKSPACE_ID>/ds/journeys/{template_id} to get the node_id, then GET /design_studio/emails/{node_id} to read its markup.

---

## Sender Identities

Always use integer IDs in the envelope, never strings or email addresses. Look up the IDs for your own sender identities in Customer.io and fill in this table.

| Name | Email | ID |
|---|---|---|
| [Your name] from Example Feedback | you@example.com | `<PERSONAL_SENDER_ID>` |
| Example Feedback Support | support@example.com | `<SUPPORT_SENDER_ID>` |
| Example Feedback News | news@example.com | `<NEWS_SENDER_ID>` |
| Example Feedback Team | hello@example.com | `<TEAM_SENDER_ID>` |
| [Colleague] from Example Feedback | colleague@example.com | `<COLLEAGUE_SENDER_ID>` |

Default for all lifecycle/nurture emails: from_id: `<PERSONAL_SENDER_ID>` (you), reply_to_id: `<SUPPORT_SENDER_ID>` (Support).

---

## Global Style Tokens

Always use these token IDs with the globalStyles.* syntax. Never hardcode hex values.

Customer.io appends a random suffix to each global style token in your workspace (for example `accentmain_abc123xyz`). Copy the exact token paths from your own Design Studio global styles and replace the `<suffix>` placeholders below.

### Colors
| Name | Token path |
|---|---|
| Accent main | globalStyles.colors.accentmain_<suffix> |
| Accent light | globalStyles.colors.accentlight_<suffix> |
| Accent medium | globalStyles.colors.accentmedium_<suffix> |
| Black | globalStyles.colors.black_<suffix> |
| White | globalStyles.colors.white_<suffix> |
| Gray | globalStyles.colors.gray_<suffix> |
| Light Gray | globalStyles.colors.lightGray_<suffix> |
| Dark mode gray | globalStyles.colors.darkmodegray_<suffix> |
| Dark mode badge | globalStyles.colors.darkmodebadge_<suffix> |

### Spacing
| Name | Token path |
|---|---|
| small | globalStyles.spacing.small_<suffix> |
| medium | globalStyles.spacing.medium_<suffix> |
| large | globalStyles.spacing.large_<suffix> |
| x-large | globalStyles.spacing.xlarge_<suffix> |
| xx-large | globalStyles.spacing.xxlarge_<suffix> |

---

## Standard Email Structure (lifecycle/nurture, confirmed from existing re-engagement emails)

```html
<x-base title="...">
  <x-section margin="0px 0px 50px" padding="0px" outer-background="#f8f8fa">
    <x-box background="#ffffff">
      <x-image href="https://example.com/?utm_source=newsletter&utm_medium=email&utm_campaign=footer"
               src="https://example.com/images/email-top-banner.png" />
      <x-box :margin="Component.utils.spacing(globalStyles.spacing.small_<suffix>, '0px')"
             :padding="Component.utils.spacing(globalStyles.spacing.large_<suffix>, globalStyles.spacing.xxlarge_<suffix>)"
             height="auto" width="auto" background="#ffffff">
        <x-paragraph :color="globalStyles.colors.accentmain_<suffix>" :font-size="25" text-align="center">
          Headline with <strong>emphasis</strong>
        </x-paragraph>
        <x-hr />
        <x-paragraph :color="globalStyles.colors.black_<suffix>">Body text</x-paragraph>
        <x-list list-style="disc" :color="globalStyles.colors.black_<suffix>"
                font-family="'Inter Tight', sans-serif" :font-size="16" :line-height="1.6" margin="0 0 24px">
          <li>Item</li>
        </x-list>
        <x-cta :margin="Component.utils.spacing(globalStyles.spacing.xxlarge_<suffix>, '0px')"
               :padding="Component.utils.spacing('8px', globalStyles.spacing.large_<suffix>)"
               href="{{CTA_URL}}">CTA label</x-cta>
        <x-paragraph :color="globalStyles.colors.black_<suffix>">
          Any questions? Just hit reply to this email, we're all ears.
        </x-paragraph>
      </x-box>
    </x-box>
  </x-section>
  <final-unsubscribe-footer></final-unsubscribe-footer>
</x-base>
```

Key rules:
- Outer x-section uses margin="0px 0px 50px" for bottom encasing
- final-unsubscribe-footer is a custom component in this workspace: always include it, never write your own unsubscribe block (if your workspace has no such component, create one once and reuse it)
- No sign-off in the email body: the from identity handles sender branding
- Empty block rule: never leave empty or wrapper-only blocks in the markup
- No em dashes or en dashes anywhere in the markup

---

## API Workflow (full commands)

### Create
```
POST /v1/environments/<YOUR_WORKSPACE_ID>/design_studio/emails
{
  "name": "Email name",
  "parent_folder_id": "<YOUR_TEMPLATES_FOLDER_ID>",
  "content": {
    "subject": "...",
    "preheader_text": "...",
    "html": "<x-base>...</x-base>"
  },
  "envelope": { "from_id": <PERSONAL_SENDER_ID>, "reply_to_id": <SUPPORT_SENDER_ID> }
}
```
Response: { "email": { "id": "<node_uuid>" } }

### Link to campaign action
```
POST /v1/environments/<YOUR_WORKSPACE_ID>/design_studio/emails/{node_id}/link
{ "target": { "type": "campaign_action", "action_id": 123 } }
```

### Publish
```
POST /v1/environments/<YOUR_WORKSPACE_ID>/design_studio/emails/{node_id}/publish
{}
```

### Update and republish
```
PUT /v1/environments/<YOUR_WORKSPACE_ID>/design_studio/emails/{node_id}
{ "content": { "html": "..." }, "envelope": { "from_id": <PERSONAL_SENDER_ID>, "reply_to_id": <SUPPORT_SENDER_ID> } }
```
Then publish again.

### Find node behind a template
```
GET /v1/environments/<YOUR_WORKSPACE_ID>/ds/journeys/{template_id}
Response: { "node_id": "..." }
```

---

## Copy Rules

- No em dashes or en dashes. Use periods or colons.
- US English spelling
- Active voice, contractions are fine
- Never use retired product names: never say "Feedback Center", always "Feedback Inbox"
- Never imply AI replaces the researcher
- Lead with outcome or pain, not feature name
- Single CTA per email
- No sign-off in the body
- Always ask the user for the CTA URL before building. Never use a placeholder.

---

## Environment Reference

Fill these in once for your workspace:

- Workspace ID: `<YOUR_WORKSPACE_ID>`
- Claude Emails folder: `<YOUR_TEMPLATES_FOLDER_ID>`
- From identity ([Your name] from Example Feedback): `<PERSONAL_SENDER_ID>`
- Reply-to identity (Example Feedback Support): `<SUPPORT_SENDER_ID>`
