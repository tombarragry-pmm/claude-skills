# tom-pmm-product-update-email

Writes the copy and produces the graphics for monthly product update emails and special edition launch emails, ready to paste into Customer.io.

Originally built: November 2026

## What it does

1. Runs a short intake: email type, features (with CTA URLs), audience, available screenshots and anything unusual.
2. Drafts all copy in chat using a fixed structure (hero, feature sections, irl examples, optional pinned insights, feedback board banner, footer), and waits for approval.
3. Picks a graphic type for each feature (UI close-up or illustrative explainer) and renders one HTML graphic per feature in a fixed visual language.
4. Delivers the copy as labeled blocks and the graphics as labeled HTML artifacts.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

None. The output is pasted into Customer.io by hand; no connector is needed.

## Make it yours

- The examples use Example Feedback, a fictional customer feedback platform. Replace the product name, product areas, tagline and default subheadline with your own.
- Replace the placeholder URLs (`https://example.com/feedback-board`, `https://app.example.com`).
- Replace the accent colors (`#2F6FEB`, `#E8F0FD`, `#1A1A2E`) with your brand colors, and change the font if you don't use Inter Tight.
