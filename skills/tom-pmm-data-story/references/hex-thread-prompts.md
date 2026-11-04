# Hex thread prompts for data stories

Hex Threads run against your product data warehouse. Ask in plain language, one thread per story, follow-ups in the same thread so Hex keeps the definitions. A thread takes a few minutes: warn the user, then poll `get_thread` until the status is IDLE.

Replace everything in square brackets. Replace the `<placeholder>` table and column names with the ones in your own warehouse. Keep the fixed definitions as written so every data story counts the same way.

## Main prompt

```
I'm building a marketing "data story" about [TOPIC: feature or integration, e.g. the help desk integration]. I need aggregate usage numbers, grouped by vertical, with no account names in the output. Please answer in plain language with the numbers, plus tables.

Fixed definitions, please use exactly these:
- Cohort: active paying accounts (your standard status definition, deleted accounts excluded) that actually used [TOPIC] in the window. Prefer event-level evidence (responses sent, surveys triggered, tickets or records created) over "configured" flags. If you have to fall back to a configured-integrations list, say so.
- Window: [DATA WINDOW, e.g. the last 12 full months, January 2025 to December 2025].
- Vertical label: <companies_table>.<industry_shortlist_column>. Do not use <crm_industry_field> or <signup_industry_field>.

Questions:
1. Cohort size: how many accounts are in the cohort, and how many of those have a vertical label.
2. Hero total: the biggest volume number that expresses [TOPIC] over the window, for example [EXAMPLES: responses sent to the help desk, tickets created from responses, surveys connected]. Give the exact figure.
3. Breakdown of the hero total and the cohort size by vertical label, largest first.
4. Dimension numbers for the cohort over the window: distinct countries or markets of respondents (if available), distinct survey languages, survey channels used (web, in-product, mobile SDK, email, link), number of surveys involved, and the date of the earliest and latest event.
5. Concentration, internal only: what share of the hero total comes from the single biggest account, and from the top 3. No names, just shares.
6. Trend: the hero total by month over the window, so I can see whether it grew.
7. Definitions and caveats: which tables you used, what "used [TOPIC]" means in the data, and anything I should not claim.
```

## Follow-ups (same thread, `continue_thread`)

Sub-verticals, when a vertical bucket needs splitting:

```
For the accounts labeled [digital marketplace / retail / SaaS] in this cohort, group them again using keywords in the free-text industry field (<industry_free_text_column>): food delivery, mobility or ride-hailing, travel, loyalty, gaming, consumer app, B2B. Show the hero total and the account count per group, no names.
```

Workflow evidence, to support an inferred workflow sentence:

```
For the same cohort, what does the data show about how [TOPIC] is used? For example: which survey types feed it (NPS, CSAT, CES, other), whether it's triggered on specific answers or scores, which channels the surveys run on, and how many surveys per account connect to it. Aggregates only.
```

Adjacent proof, when the story needs a second number:

```
For the same cohort and window, give me totals for [ADJACENT METRIC, e.g. responses collected on mobile SDK surveys, surveys running in more than one language, Feedback Library projects created]. Exact figures, grouped by vertical label.
```

## Reading the answer

- Copy the exact figures into the internal notes block with the thread URL.
- Note Hex's definition of "used [TOPIC]" word for word. The story's workflow sentence has to stay inside it.
- If Hex fell back to configured flags, the story can say "accounts with [TOPIC] connected" but not "accounts sending responses to [TOPIC]".
- If a vertical total is carried almost entirely by one account, keep the vertical if the number is strong, write it as the plural cohort, and flag the concentration in the internal notes.
