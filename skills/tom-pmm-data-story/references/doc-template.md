# Data story doc template

Use this structure. Part A is internal and never published. Part B is the story that goes to the customer stories hub. The model for Part B is `references/example-story.md`: read it first and match its shape. Keep paragraphs to two or three sentences. No em dashes or en dashes anywhere.

---

# Data story: [Topic] (draft)

## Part A: internal notes (do not publish)

- Topic: [feature or integration]
- Lead persona: [job title]. Bonus section addresses: [other job titles]
- Data window: [start month to end month]. Note whether the last month is partial and whether to re-cut to 12 full months before publishing
- Hex thread: [URL]
- Cohort definition used by Hex: [copy Hex's wording, including the counting method]. Cohort size, and the size per use case if the story has several
- Hero and supporting totals, exact, with how they overlap if they do
- What the numbers are and are not: [what the warehouse actually measures, and the claims that must not be made]
- Vertical label source: `<companies_table>.<industry_shortlist_column>` (enrichment label, stored column); sub-verticals from `<industry_free_text_column>` keywords where used
- Bundle composition: [the warehouse labels inside each published label, with their numbers, so the next story groups the same way]
- Percentages used in the story: [numerator / denominator for each]
- Share of cohort with no vertical label: [x%]
- Concentration: top account carries [x%] of the hero total, top 3 carry [y%]. Names stay in this block only
- Numbers from outside Hex: [number, who produced it, when, and that it was not cross-checked]
- Numbers considered and cut: [number: reason] (one per line)
- Help center articles used: [URLs]
- Quotes used: [quote library entry, person, company]
- Open items: [to confirm] (one per line, or "none")

---

## Part B: the story

# How [partner or product] customers [verb] [number] [thing] and [number] [thing] into [outcome], using Example Feedback

Shape rules: fact first, hook as the tail. Rounded-down numbers in the title (1.2M+, 300K+). Name the partner or feature, name your product, use an action verb (turn, fix, close the loop). Never a storage verb (centralize, collect, gather). Never hook-first.

[Date] · [author mention]

**Feature:** [name] · **Built for:** [job titles] · **Cohort:** [one easy-reading label, e.g. B2C software and apps] · **Data window:** [months]

One-line hook. The tension the story resolves, in one sentence a CX reader recognizes.

Platform framing, two or three sentences: what Example Feedback is (a Voice of Customer platform), and how the feature or integration runs. For integrations, name both directions: feedback out and feedback in.

Method sentence: "We looked at how Example Feedback's [partner] customers use [feature], with a focus on our [cohort], and at what scale. The numbers below cover all [partner] customers from [month] to [month]."

## By the numbers

| [Hero, rounded] | [Supporting, rounded] | [Dimension] |
|---|---|---|
| **[what it is]** in 12 months: **[the idea it proves]** | **[what it is]** in the same 12 months: **[the idea it proves]** | [channels, markets or languages, in a sentence] |

Each cell carries the concept it proves (inner loop, outer loop, channels), so the strip teaches the vocabulary the story uses. No survey counts anywhere in the strip.

## [Framework section, e.g. Inner loop and outer loop]

One line: the frame every reader should hold. Then a three-column table:

| Loop | What it fixes | Where it runs in Example Feedback and [partner] |
|---|---|---|
| **[Loop 1]** | [one customer's problem] | [where the workflow runs] |
| **[Loop 2]** | [the pattern behind many] | [where the workflow runs] |

One payoff line after the table.

> "[Verbatim quote from the Notion quote library]"
>
> **[Name]**, [Title] at [Company]

Quotes are social proof for the pattern, pulled with the `tom-pmm-customer-quote-finder` skill. They are never the subject of the story and never invented.

## The [n] use cases, by the numbers

| Use case | Loop | What happens | Last 12 months |
|---|---|---|---|
| 1. [name] | [loop] | [one sentence, inside the help center capability] | [exact number] |
| 2. [name] | [loop] | [one sentence] | [exact number] |
| 3. [name] | [loop] | [one sentence] | [exact number] |

One line under the table stating any overlap and the deduplicated total.

## The problem every [persona] knows

Two short paragraphs. A customer the reader recognizes, the moment the feedback went nowhere, and the loop that never closed.

## The shift: [what changes]

One paragraph. How the workflow closes the first loop and starts the second, from the same data.

> "[Second quote from the library, if one fits]"
>
> [Name], [Title], [Company]

## How each use case works

### 1. [Use case name]

One paragraph: the mechanics in plain words, within what the help center confirms. What the reader can cut the data by (issue type, brand, market).

{screenshot}

### 2. [Use case name]

Same shape.

{screenshot}

### 3. [Use case name]

Same shape. For Feedback Library use cases, follow its messaging guide: AI drafts, the researcher directs, every finding links to its source.

{screenshot}

## Where it's happening: [cohort label]

Cohort paragraph with its exact number and why this cohort cares.

**[Sub-vertical 1]** [percentage of the cohort], [percentage by direction or use case]. Which use case is the core for them and why.

**[Sub-vertical 2]** Same shape.

Percentages of the parent block, never raw numbers, in these callouts. Only call out a sub-vertical where the data shows a distinct pattern.

## How to set it up

1. [Step linking the help center article] (use case 1)
2. [Step linking the help center article] (use case 2)
3. [Step linking the help center article] (use case 3)

## The result: [one line that pays off the frame]

One paragraph: the two loops in one breath, then the proof line (the comparison that makes the feature the obvious choice, e.g. "the most-used help desk integration on Example Feedback, at 2.1x the next one").

Want to see what [feature] could do at your scale? [Book a call](https://example.com/contact/) or [try Example Feedback for free](https://example.com/signup).
