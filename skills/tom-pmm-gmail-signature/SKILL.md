---
name: tom-pmm-gmail-signature
description: Generate a ready-to-paste branded Gmail email signature for an Example Feedback (a fictional customer feedback platform) team member. Use this skill WHENEVER someone wants to create, build, set up, update, or regenerate an email signature for themselves or a colleague at the company, most explicitly when they write "create a gmail signature", but also for phrasings like "make me an email signature", "I need a new signature", "build a signature for [name]", or "set up my Gmail signature". The skill collects (or confirms) the person's name and role plus an optional "Book a call with me" button, generates a single self-contained HTML file with the company logo, social icons, and feature pills as PNGs (so Gmail won't strip them), and hands over step-by-step paste instructions. Do not use for signatures for other companies, for signatures in other clients only (Outlook desktop, Apple Mail) unless Gmail is also involved, or for general email-template design.
---

# Branded Gmail signature builder

This skill produces a branded email signature that a team member can paste
straight into their Gmail settings. The brand layout, logo, social icons,
feature pills, and the "Customer Feedback Platform" category line are fixed. The
only things that change per person are **name** and **role/title**.

The examples use Example Feedback, a fictional customer feedback platform.
Replace the brand content in `scripts/build_signature.py` with your own.

The hard problem this skill solves: Gmail strips SVG graphics on paste, so the
brand graphics must be PNGs. The build script embeds local PNGs as base64 so the
result needs no image hosting, and falls back to hosted image URLs when a PNG is
not available locally.

## Brand images

The script expects these PNGs in `assets/images/` (exported at 3x the display
size for retina sharpness). They are not included in this repo: add your own.

| File | Display size | What it is |
|------|--------------|------------|
| `logo.png` | 100 x 18 | Full logo (mark + wordmark) |
| `linkedin.png`, `youtube.png`, `website.png` | 28 x 28 | Solid accent social icons |
| `linkedin_pill.png`, `youtube_pill.png`, `website_pill.png` | 28 x 28 | Light accent "pill" style social icons, used when the booking button is on |
| `ic_surveys.png`, `ic_research.png`, `ic_integrations.png` | 14 x 14 | Small icons for the three feature pills |

If a PNG is missing, the script uses `IMAGE_BASE_URL + <name>.png` instead
(placeholder: `https://example.com/email-signature/`). Set `IMAGE_BASE_URL` to
your own public image host if you prefer hosted images.

## Workflow

Follow these four steps in order.

### 1. Trigger

Activate when the person asks to create or update a Gmail signature (see the
description for trigger phrasings). The canonical phrase is "create a gmail
signature".

### 2. Collect or confirm name, role, and an optional booking button

You need two required pieces of information (full name and role/title) plus one
optional extra: whether to include a "Book a call with me" button, and if so, the
link it should point to. The button is per-person: some people have it, most don't.

- If any are already known from the conversation or from what you remember about
  the person, **state them back with each field clearly labeled and ask the person
  to confirm or correct**. Always use this labeled layout (one field per line) so
  it's easy to scan and hard to mis-skim:

  ```
  Full name: Jordan Lee
  Role: Product Designer
  ```

  Then ask whether everything is correct or they'd like to change anything.
- If they're unknown, ask for both in one short, clearly structured prompt
  rather than separate questions. Make the question easy to answer by
  labeling exactly what you need, e.g.:

  ```
  I just need two things for your signature:
  - Full name:
  - Role:
  ```

  When they reply, confirm back using the same labeled layout above before
  generating.

**Always ask about the booking button.** After you have the name and role, ask
whether they want a "Book a call with me" button (it's off by default). If they
say yes, ask for the link to put in it (e.g. a Calendly, Google Calendar, or
Chili Piper URL) and include it in the confirmation, like:

```
Full name: Jordan Lee
Role: Product Designer
Book a call button: yes -> https://example.com/book/jordan-lee
```

If they don't want it, confirm "Book a call button: no" and omit it. Never invent
a booking link. If they want the button but haven't given a URL, ask for it.

Do not invent a role. If the person hasn't given one and you don't know it, ask.

Wait for confirmation before generating the file. Getting the name or title wrong
in a signature is the kind of error that's annoying to discover after it's been
sent on real email, so the quick confirm is worth it.

### 3. Generate the signature file

Run the bundled build script. It only needs Python's standard library. The brand
PNGs are read from `assets/images/` if present, so there is no dependency to
install.

```bash
python scripts/build_signature.py \
  --name "FULL NAME" \
  --role "ROLE / TITLE" \
  --out outputs/signature_gmail.html
```

Add `--booking-url "https://..."` only if the person asked for the booking button.
Omit the flag entirely when they don't want it: the button then doesn't render.

The signature restyles automatically based on the booking button, all handled
by the script, no extra flags needed:

- **With** `--booking-url`: the bottom feature row becomes lightweight footer-nav
  links (icon + label, divider lines, no fill) so it doesn't compete with the
  CTA, and the social icons switch to the light accent pill style.
- **Without** it: the bottom feature row stays as filled light accent pills, and
  the social icons stay solid accent.

(Run it from the skill directory, or pass `--images-dir` pointing at
`assets/images`.) The script writes a single self-contained HTML file whose page
contains only the signature, which makes the select-all-and-copy step clean. If
it prints a note that PNGs were not found, the signature uses hosted image URLs:
check that `IMAGE_BASE_URL` points at real images before handing it over.

Then present the file to the person with the `present_files` tool (or save it to
an outputs folder) so they can download it.

If you want to show the person what it looks like before they install it, you may
render a quick inline preview, but this is optional. The file itself is the
deliverable.

### 4. Give the paste instructions

Read `references/gmail-paste-instructions.md` and give the person the install
steps **as a numbered, click-by-click list** (step 1 download, step 2 open, and so
on). Be explicit about where to click, e.g. "click the download icon in the
top-right corner of the file card". **Step 1 is always to download the file**: the
chat preview is not a real browser tab, so the copy step won't work until the file
is saved (this is a common stumbling point). Follow the numbered steps in the
reference through to testing in a new compose window. Also flag the two expected
quirks so they aren't surprised: the font falls back to Arial, and Gmail may
square off the pill corners.

## What not to change

The logo, social links (LinkedIn, YouTube, website), the three feature pills (in
the example: Surveys, Feedback Lab, 30+ Integrations), and the "Customer
Feedback Platform" category line are all fixed brand elements. Don't edit them
per person. If someone wants to change the brand content itself (new tagline,
different links, an extra social icon), that's a change to the template in
`scripts/build_signature.py`, not a per-person input. Confirm with them that
they intend a template change before editing it.
