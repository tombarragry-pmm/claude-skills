# tom-pmm-create-inapp-post

Takes finished changelog copy and creates the post in your in-app changelog tool by driving its web UI in Chrome, saving as a draft unless you explicitly say to publish.

Originally built: November 2026

## What it does

1. Collects the inputs: title, body, optional action link, channels, segmentation, publication date, comments/reactions, and draft or publish.
2. Opens the post composer in the logged-in browser and fills the title and body.
3. Adds the action link, publication date and post settings, working around known UI snags (URL protocol, re-rendering date picker).
4. Checks channels and segmentation, then saves as a draft (or publishes only on explicit confirmation).
5. Verifies the post in the feed and reports back, looping once per post for bulk runs.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

- Claude in Chrome, connected to a browser where you are already logged in to your in-app changelog tool.
- The steps were written against Beamer's web UI. Other tools work if you update the labels.

## Make it yours

Replace `<CHANGELOG_TOOL_URL>` with your tool's app URL, update button and field labels if your tool differs, and set your own default channels. Pair it with `tom-pmm-inapp-changelog` for the copy.
