# tom-pmm-cio-email-creation

Builds lifecycle, onboarding and activation emails in Customer.io Design Studio through the Customer.io API, from base template to a published email linked to a campaign action.

Originally built: November 2026

## What it does

1. Picks one of four base Design Studio templates for the email's purpose.
2. Agrees subject, preheader, body copy and the exact CTA URL with you before building anything.
3. Creates the campaign action if needed, then creates the Design Studio email with the right sender identities and folder.
4. Links the email to the campaign action and publishes it, so the action actually sends.
5. Reads the email back to verify the content landed.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

- The Customer.io connector (MCP), with write access to Design Studio and campaigns.
- Four base templates in a Design Studio folder, a custom unsubscribe footer component, and global style tokens set up in your workspace.

## Make it yours

The examples use Example Feedback, a fictional customer feedback platform. Replace the workspace ID, folder ID, template node IDs, sender identity IDs and addresses, global style token paths (including their random suffixes), banner image and website URLs, and the retired product name rule in the copy rules.
