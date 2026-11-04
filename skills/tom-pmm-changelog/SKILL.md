---
name: tom-pmm-changelog
description: Write changelog posts for the public product changelog of Example Feedback (a fictional customer feedback platform). Use this skill whenever the user (or anyone on the team) asks to write, draft, or create a changelog entry, product update post, or release note. Trigger even for casual requests like "write a changelog for X feature" or "help me announce this change". Always use this skill for public changelog posts: do not write them without it.
---

# Public Changelog Skill

Generates changelog posts for Example Feedback's public product changelog (e.g. `https://example.com/changelog`).

---

## What a changelog post looks like

Each post has these components:

### 1. Title
- Short, noun-led, descriptive: not clickbait
- Typically 3 to 7 words
- Common patterns:
  - `[Feature] inside the [context]` → "Language reference inside the survey"
  - `[Action] + [object]` → "Minimize button on web surveys"
  - `[Adjective] + [noun]` → "Updated Team Invite Options"
  - `[Feature] in [scope]` → "Response attributes in web, in-product, and mobile surveys"
  - `[Adjective] + [noun] + [qualifier]` → "Alternative CSAT Calculator"
- Capitalize each word (title case)
- No punctuation at the end

### 2. Body (1 to 3 short paragraphs)
- Opens with what changed or what's new: no preamble
- Factual and direct. Not salesy.
- Addressed to "you" (the user/customer)
- Specific: names the feature, surface (web, mobile, in-product), and context
- Uses US English spelling (e.g. "minimized", "customize")

### 3. Why it matters
- Subheading: **Why it matters**
- 1 to 3 sentences
- Explains the practical value to the user
- Stays grounded: no hype, no superlatives
- Focuses on what the user can now do that they couldn't before, or what friction is removed

### 4. Optional: Bullet list
- Used when a feature has multiple sub-changes or configuration options
- Short bullets: one idea per line
- No full stops at the end of bullets (consistent with the tone)

### 5. Optional: Visual
- If a screenshot or mockup is provided, note where it would appear (after the title/intro, or after a section)
- Do not describe images in copy: they speak for themselves

---

## Tone guide

| Do | Don't |
|---|---|
| Direct, factual, specific | Vague, fluffy, hype-led |
| "You can now..." | "We're thrilled to announce..." |
| Named surfaces (web, mobile, in-product) | Generic ("everywhere", "your workflows") |
| Active voice | Passive voice |
| Short sentences | Long compound clauses |
| Consistent US English spelling | Mixed spelling conventions |

**Voice examples:**
- ✅ "You can now set a default language for your survey and let respondents switch between options."
- ❌ "We're excited to introduce our brand-new multi-language survey experience!"
- ✅ "The minimize button now lets respondents collapse a survey instead of exiting it entirely."
- ❌ "This powerful new UX improvement gives users more control over their survey experience."

---

## Workflow

1. **Ask for the brief** (if not already provided):
   - What feature/change is being announced?
   - Which surfaces does it affect? (web widget, in-product surveys, mobile, AI Insights, etc.)
   - Is there a "why it matters" angle you want to emphasize?
   - Any screenshot to include? (optional)

2. **Draft the post** following the structure above

3. **Present for review:** changelog posts are short, so show the full draft in one go

4. **Iterate** based on feedback: typical tweaks are title wording, "why it matters" framing, or adding/removing bullets

---

## Examples for reference

Use these as style anchors. Match the register and structure. (These are illustrative examples for the fictional Example Feedback product. Replace them with real posts from your own changelog once you have a few.)

**Example 1: Single feature, clear why-it-matters:**
> **Minimize Button on Web Surveys**
> 
> The close button on web surveys now minimizes the survey instead of closing it entirely.
> 
> **Why it matters**  
> Respondents who dismiss a survey midway are often just pausing, not opting out. This lets them return to the survey without starting over.

**Example 2: Multi-surface feature:**
> **Response Attributes in Web, In-Product, and Mobile Surveys**
> 
> You can now attach custom attributes to individual survey responses across all three survey surfaces.
> 
> **Why it matters**  
> Linking responses to user properties like plan, role, or company makes segmentation and analysis faster, with no manual cross-referencing needed.

**Example 3: Update to existing feature:**
> **Updated Team Invite Options**
> 
> Team invite flows now include additional permission controls when adding new members.
> 
> - Set role at the point of invite
> - Restrict access by workspace
> - Bulk invite via CSV
> 
> **Why it matters**  
> Larger teams need tighter access control from day one. These changes reduce the admin overhead of onboarding new members.

---

## Output format

Deliver the post as clean markdown: no HTML, no extra commentary. Just the post, ready to paste into the changelog CMS.
