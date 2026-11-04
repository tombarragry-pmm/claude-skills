---
name: create-cms-feature-page
description: Build a new Example Feedback (a fictional customer feedback platform) product or feature landing page in a visual CMS, end to end, from a feature brief to a finished page JSON ready to import. Use this skill whenever the user asks to build, create, draft, plan, or write copy for a new feature page, product page, or landing page that lives in the CMS. Trigger on phrasings like "build a feature page", "create a new feature page", "I'm building a landing page for [feature]", "help me write the [feature] page", "new CMS page", "let's do a page for [feature]", or whenever the user uploads a CMS page-template JSON and wants the copy filled in. Always use this skill for company feature or landing pages built in the CMS, even if the request seems simple or only mentions one section. It governs the section-by-section working process, the page structure and component schema, per-slot character budgets, the copy rules, and assembling the final page JSON.
---

# Create CMS Feature Page

Write the copy for an Example Feedback feature or landing page section by section,
then assemble it into a page JSON file that imports cleanly into your visual CMS
(e.g. Builder.io). The user uploads a page template exported from the CMS at the
start and you hand back a filled file at the end. This file is self-contained:
the structure, the rules, and the assembly script are all below.

The examples use Example Feedback, a fictional customer feedback platform, and
its fictional research product, Feedback Lab. The component names below describe
one site's custom component library. Replace them with the names your own CMS
templates use.

---

## How we work

- **One section at a time, top to bottom.** Lock a section before moving to the
  next. Never batch ahead or draft the whole page speculatively.
- **Offer options, not a single draft.** For each slot, give an honest read of
  what is weak, then 2 to 3 short options to react to and hybridize, with a clear
  recommendation and a one-line rationale. The user prefers directional guidance
  over open questions.
- **Ask via the question buttons.** When you have a genuine fork or a clarifying
  question, use the `ask_user_input_v0` tool rather than burying it in prose, and
  batch related questions so nothing slips. Do not ask about things the brief
  already answers.
- **Minimal edits on revisions.** When the user asks for a targeted fix, change
  only that. Do not rewrite a line they already approved.
- **Treat inherited placeholder or off-spec copy as if it does not exist.**
  Templates are repurposed from other pages and often carry stale or inaccurate
  copy (a different feature's text, claims that are not true at launch). Do not
  preserve it; write fresh, accurate copy.
- **Respect the character budgets** below as guidance when proposing copy.

---

## How a session runs

**0. Read the brief first.** The feature brief tells you what the feature does,
who it is for, and where the value sits. Every copy decision flows from it. If it
is a Notion page, fetch it. Read it before the template.

**1. Read and map the template.** The user uploads a CMS page-template JSON.
Parse it, list the blocks, and confirm it matches the canonical structure below.
Flag any inherited copy you will replace and anything that breaks the launch
facts.

**2. Set the strategy.** From the brief, name the primary and secondary personas
(use real job titles, never internal codenames). Agree the hero angle by offering
2 to 3 distinct directions. Keep the directions you do not lead with: weave them
into the feature sections so the page still speaks to secondary personas.

**3. Work the sections in order:** hero, opening grid, showcase A and its cards,
showcase B and its cards, how-it-works carousel, testimonial, FAQ. Lock each
before the next.

**4. Assemble the file** using the script at the bottom of this skill. Start from
the uploaded template, swap only copy, preserve IDs, symbols, and images, fix
leftover button hrefs, draft page metadata. Run the validation (symbols
unchanged, no dashes, valid JSON). Save as `<feature>.page.json` and
`present_files` it.

**5. Hand over the end-state flags** (the things copy work cannot finish):
- Images are still the template's assets. They need swapping in the CMS.
- Plan availability copy, if the brief marks it TBC, cannot be written yet.
- SEO metadata and the URL slug are drafts to confirm.
- The testimonial needs a real quote (never invent one).
- Confirm any disputed facts from the brief (for example, an integration count).

---

## The page structure (canonical)

An Example Feedback feature page is these 13 blocks, top to bottom. Always parse
the template the user uploaded to confirm, and find blocks by component **name
and role**, not by index, since a block being added or removed shifts every
later index. The assembly script already does this.

| # | Component name | Role | Editable? |
|---|---|---|---|
| 0 | `Hero Section` | Eyebrow, H1, subhead, two CTAs, image | Yes |
| 1 | `Symbol` | Logo / "trusted by" strip | NO |
| 2 | `Feature Grid With Icons` | Opening 3-card overview (has its own H2 + intro) | Yes |
| 3 | `Feature Showcase` | Big feature A (`mirrored` layout) | Yes |
| 4 | `Feature Grid With Icons` | 3 cards supporting showcase A (no header) | Yes |
| 5 | `Feature Showcase` | Big feature B (`default` layout) | Yes |
| 6 | `Feature Grid With Icons` | 3 cards supporting showcase B (no header) | Yes |
| 7 | `Feature Carousel` | "How it works", 3 numbered steps | Yes |
| 8 | `Testimonial` | Quote, attribution, CTA | Yes |
| 9 | `FAQ` | Title, intro, Q&A items | Yes |
| 10 to 12 | `Symbol` | Closing CTA band, footer, nav | NO |

The opening grid is the only `Feature Grid With Icons` with a `Heading 2` child.
The other two carry cards only and attach to the showcase directly above them.

### Component fields

- **Hero Section** `options`: `layout`, `theme`, `backgroundColor`. Children in
  order: `Image`; `Badge / Label` (`children` plain = eyebrow, `variant`);
  `Heading 1` (`children` HTML); `Paragraph` (`children` HTML = subhead);
  `Button` x2 (`children` plain, `href`, `actionType`, `size`, `variant`).
- **Feature Grid With Icons** `options`: `cards[]`, `columns` (`"3"`), `theme`,
  `backgroundColor`, `sectionId`, `entranceAnimation`. The opening grid also has
  a `Heading 2` and a `Paragraph` child. Each card:
  `{ "icon", "text", "description", "image", "imageAlt" }` where `text` is the
  header (plain) and `description` is the body (plain, not wrapped).
- **Feature Showcase** `options`: `layout` (`default` or `mirrored`), `theme`,
  `backgroundColor`, `sectionId`, `entranceAnimation`. Children in order:
  `Image`; `Badge / Label` (badge); `Heading 2` (HTML); `Paragraph` (body, HTML);
  `Button`. Alternate the layout between the two showcases.
- **Feature Carousel** `options`: `theme`, `features[]`, `backgroundColor`.
  Children: `Badge / Label`, `Heading 2` (HTML). Each feature:
  `{ "icon", "title", "description", "image", "imageAlt" }`. Keep the `"1. "`,
  `"2. "`, `"3. "` prefix on `title`: the component renders the number as part of
  the string.
- **Testimonial** `options`: `theme`, `backgroundColor`. Children in order:
  `Image` (logo); `Paragraph` (segment, plain); `Paragraph` (quote, HTML, may
  hold `<strong>`); `Image` (avatar); `Paragraph` (name, plain); `Paragraph`
  (role, plain); `Button`.
- **FAQ** `options`: `title` (plain), `description` (plain), `items[]`, `theme`,
  `backgroundColor`, `entranceAnimation`. Each item:
  `{ "question" (plain), "answer" (HTML, wrapped in <p>) }`. The title and
  description boilerplate can usually stay.
- **Symbol** `options`: `symbol = { "model": "symbol", "entry": "<id>" }`. Never
  edit. A symbol is a shared block: its content lives in a separate CMS entry
  shared across pages, so editing it changes every page that uses it.

### Formatting

- **HTML-wrapped** (`<p>...</p>`): `Heading 1`, `Heading 2`, `Paragraph`
  `children`; FAQ `answer`. Preserve inline markup like `<strong>`.
- **Plain text**: `Badge / Label` and `Button` `children`; card `text` and
  `description`; carousel `title` and `description`; FAQ `question`, `title`,
  `description`.
- **Buttons**: `Start Free` to `https://app.example.com/signup`; `Book a Call`
  or `Book a demo` to `/book-a-demo/`. Fix leftover hrefs (`/features`, `/blog`).
- **Images**: every `Image` and card `icon` / `image` points at the template's
  assets. Copy work cannot produce the right URLs, so leave them and flag them
  for manual swap in the CMS.
- **Metadata**: `data.title`, `data.description`, and
  `data.softwareApplicationJsonLd` carry SEO inherited from the previous page.
  Draft fresh ones, including the URL slug, and flag for review.
- **Entities**: `&nbsp;` and `&amp;` may appear and are fine to keep or use.

---

## Character budgets (guidance, not hard caps)

Derived from shipped pages. Use them to keep proposals in range, and recalibrate
them against your own live pages.

| Slot | Target characters | Notes |
|---|---|---|
| Hero eyebrow | 12 to 20 | Title Case, short action phrase |
| Hero H1 | 45 to 55 | the one place to be punchy or use contrast |
| Hero subhead | 100 to 120 | one sentence, outcome-focused |
| Section badge (showcase, carousel) | 12 to 20 | short phrase, verb-led |
| Section H2 (grid, showcase, carousel) | 35 to 45 | clear over clever |
| Opening grid intro | 100 to 115 | one to two sentences |
| Showcase body | 80 to 90 | output or outcome, not mechanism |
| Grid card header (`text`) | 15 to 30 | benefit, not feature name |
| Grid card description | 45 to 70 | one sentence; cut second clauses |
| Carousel step title | 18 to 30 | keep the "1." prefix |
| Carousel step description | 55 to 75 | one sentence |
| FAQ question | 25 to 80 | the customer's actual question |
| FAQ answer | 90 to 270 | lead with the direct answer, then 1 to 2 sentences |

---

## Copy rules (non-negotiable)

**Always:** US English; active voice and contractions; problem-first framing
(what pain does this solve before what the feature does); outcome-focused (what
the user walks away with); connect to Collect, Analyze, Act where it fits.

**Never:**
- Em dashes or en dashes. Use colons or periods. (Firm brand rule, no exceptions.)
- Retired product names. Keep a list here (for example, "Old Product Name" is
  retired; the product is "Feedback Lab").
- Retired feature names (list any features that no longer exist so they never
  appear in copy).
- "Agentic" framing that implies AI replaces the researcher or reduces control.
  AI assists; the human stays in control. Verifiability matters: conclusions
  trace back to real feedback.
- Internal persona names in copy (internal codenames like "Data Detective" or
  "Roadmap Pilot"). Use real job titles.
- Vague superlatives ("best-in-class", "powerful", "next-gen", "seamless").
- Feature-dumping without an outcome.
- Claiming anything not true at launch. Verify technical claims against your
  feature and capability knowledge base. Roadmap features are framed honestly
  ("not right now, but it's on our roadmap") and usually handled in the FAQ, not
  as a card or a "coming soon" pill.

---

## Voice patterns (how the user sharpens copy)

Match these when proposing, so revisions are lighter:
- Cut card descriptions hard. One sentence, around 50 to 65 characters. Drop the
  trailing second clause.
- Concrete over abstract: "20+ sources", "30+ tools", numerals not words.
- Abbreviate where the reader knows it ("VoC").
- Frame to the outcome or the stakeholder moment ("Fuel for your next meeting"
  beats "Fuel for Feedback Lab").
- Lead integration examples with the tools your own team uses or your audience
  knows best (e.g. Customer.io), then the next most common ones.
- Title Case the hero eyebrow; keep badges to a short verb-led phrase.
- Imperative, active verbs: "Send", "Run", "Build", "Feed".

---

## Assembly script

When the copy is locked, write this to a file (for example
`fill_page.py`), paste the locked copy into the `COPY` dict, and run it
against the uploaded template:

    python fill_page.py TEMPLATE.json <feature>.page.json

It edits only copy, finds blocks by role so it survives index shifts, wraps `<p>`
where needed, fixes leftover button hrefs, and never touches symbols, IDs, or
images. It refuses to write if a symbol changed and reports any em or en dashes.
Read the validation line before presenting; it must show symbols preserved and
zero dashes. Then `present_files` the output and list the end-state flags.

Set `SIGNUP`, `DEMO`, `BRAND_NAME` and `BRAND_URL` to your own values before
running.

```python
#!/usr/bin/env python3
"""Fill a CMS feature-page template with locked copy.

Usage: python fill_page.py TEMPLATE.json OUTPUT.json
Paste the copy locked in chat into COPY (plain text; the script wraps <p>).
Set any field or section to None to leave the template's value untouched.
"""
import json, sys

COPY = {
    "hero": {"eyebrow": None, "h1": None, "subhead": None},            # 12-20 / 45-55 / 100-120
    "opening_grid": {"h2": None, "intro": None, "cards": []},          # cards: 3x {"head","desc"}
    "showcase_a": {"badge": None, "h2": None, "body": None, "cards": []},
    "showcase_b": {"badge": None, "h2": None, "body": None, "cards": []},
    "carousel": {"badge": None, "h2": None, "steps": []},              # steps: 3x {"title","desc"}; keep "1." prefix
    "testimonial": {"segment": None, "quote": None, "name": None, "role": None},
    "faq": {"title": None, "description": None, "items": []},          # items: {"q","a"}
    "meta": {"title": None, "description": None, "jsonld_name": None, "jsonld_url": None},
}

SIGNUP = "https://app.example.com/signup"
DEMO = "/book-a-demo/"
BRAND_NAME = "Example Feedback"
BRAND_URL = "https://example.com/"

def cname(b): return (b.get("component") or {}).get("name")
def opts(b): return (b.get("component") or {}).get("options", {})

def wrap_p(t):
    if t is None: return None
    t = t.strip()
    return t if t.startswith("<") else "<p>" + t + "</p>"

def leaves(block, target):
    out = []
    def rec(x):
        if cname(x) == target: out.append(x)
        for c in (x.get("children") or []): rec(c)
    for c in (block.get("children") or []): rec(c)
    return out

def set_children(block, comp, value, idx=0, wrap=False):
    if value is None: return
    found = leaves(block, comp)
    if idx < len(found):
        found[idx]["component"]["options"]["children"] = wrap_p(value) if wrap else value

def set_cards(block, cards):
    if not cards: return
    for card, spec in zip(opts(block).get("cards", []), cards):
        if spec.get("head") is not None: card["text"] = spec["head"]
        if spec.get("desc") is not None: card["description"] = spec["desc"]

def fix_hrefs(block):
    for bt in leaves(block, "Button"):
        o = bt["component"]["options"]
        label = (o.get("children") or "").lower()
        if "start" in label: o["href"] = SIGNUP
        elif "book" in label or "demo" in label: o["href"] = DEMO

def main(tpl, out):
    doc = json.load(open(tpl))
    blocks = doc["data"]["blocks"]
    sym_before = [opts(b).get("symbol", {}).get("entry") for b in blocks if cname(b) == "Symbol"]

    grids = [b for b in blocks if cname(b) == "Feature Grid With Icons"]
    showcases = [b for b in blocks if cname(b) == "Feature Showcase"]
    heroes = [b for b in blocks if cname(b) == "Hero Section"]
    carousels = [b for b in blocks if cname(b) == "Feature Carousel"]
    testimonials = [b for b in blocks if cname(b) == "Testimonial"]
    faqs = [b for b in blocks if cname(b) == "FAQ"]
    opening = next((g for g in grids if leaves(g, "Heading 2")), None)
    attached = [g for g in grids if g is not opening]

    if heroes and COPY.get("hero"):
        h, c = heroes[0], COPY["hero"]
        set_children(h, "Badge / Label", c.get("eyebrow"))
        set_children(h, "Heading 1", c.get("h1"), wrap=True)
        set_children(h, "Paragraph", c.get("subhead"), wrap=True)
        fix_hrefs(h)

    if opening and COPY.get("opening_grid"):
        c = COPY["opening_grid"]
        set_children(opening, "Heading 2", c.get("h2"), wrap=True)
        set_children(opening, "Paragraph", c.get("intro"), wrap=True)
        set_cards(opening, c.get("cards"))

    for key, sc, grid in zip(["showcase_a", "showcase_b"], showcases, attached):
        c = COPY.get(key) or {}
        set_children(sc, "Badge / Label", c.get("badge"))
        set_children(sc, "Heading 2", c.get("h2"), wrap=True)
        set_children(sc, "Paragraph", c.get("body"), wrap=True)
        fix_hrefs(sc)
        set_cards(grid, c.get("cards"))

    if carousels and COPY.get("carousel"):
        cz, c = carousels[0], COPY["carousel"]
        set_children(cz, "Badge / Label", c.get("badge"))
        set_children(cz, "Heading 2", c.get("h2"), wrap=True)
        for f, spec in zip(opts(cz).get("features", []), c.get("steps", [])):
            if spec.get("title") is not None: f["title"] = spec["title"]
            if spec.get("desc") is not None: f["description"] = spec["desc"]

    if testimonials and COPY.get("testimonial"):
        t, c = testimonials[0], COPY["testimonial"]
        vals = [c.get("segment"), wrap_p(c.get("quote")), c.get("name"), c.get("role")]
        for el, v in zip(leaves(t, "Paragraph"), vals):
            if v is not None: el["component"]["options"]["children"] = v
        fix_hrefs(t)

    if faqs and COPY.get("faq"):
        f, c = faqs[0], COPY["faq"]
        o = f["component"]["options"]
        if c.get("title") is not None: o["title"] = c["title"]
        if c.get("description") is not None: o["description"] = c["description"]
        if c.get("items"):
            o["items"] = [{"question": it["q"], "answer": wrap_p(it["a"])} for it in c["items"]]

    m = COPY.get("meta") or {}
    if m.get("title") is not None: doc["data"]["title"] = m["title"]
    if m.get("description") is not None: doc["data"]["description"] = m["description"]
    if m.get("jsonld_name") or m.get("jsonld_url"):
        doc["data"]["softwareApplicationJsonLd"] = json.dumps({
            "@context": "https://schema.org", "@type": "SoftwareApplication",
            "name": m.get("jsonld_name") or BRAND_NAME, "applicationCategory": "BusinessApplication",
            "operatingSystem": "Web", "description": m.get("description") or doc["data"].get("description"),
            "url": m.get("jsonld_url") or BRAND_URL, "screenshot": doc["data"].get("featuredImage"),
            "provider": {"@type": "Organization", "name": BRAND_NAME, "url": BRAND_URL},
        }, indent=2)

    sym_after = [opts(b).get("symbol", {}).get("entry") for b in blocks if cname(b) == "Symbol"]
    assert sym_before == sym_after, "Symbol blocks changed. Aborting so shared content is not damaged."

    dashes = []
    def scan(o, path="root"):
        if isinstance(o, str):
            if "\u2014" in o or "\u2013" in o: dashes.append((path, o))
        elif isinstance(o, dict):
            for k, v in o.items(): scan(v, path + "." + k)
        elif isinstance(o, list):
            for i, v in enumerate(o): scan(v, path + "[" + str(i) + "]")
    scan(doc)

    json.dump(doc, open(out, "w"), ensure_ascii=False, separators=(",", ":"))
    json.load(open(out))
    print("blocks:", len(blocks), "| symbols preserved:", sym_before == sym_after)
    print("em/en dashes found:", len(dashes))
    for path, s in dashes[:10]: print("  DASH at", path, "->", s[:80])
    print("written:", out)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "template.json",
         sys.argv[2] if len(sys.argv) > 2 else "feature-page.page.json")
```
