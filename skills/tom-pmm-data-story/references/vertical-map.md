# Vertical map

Source column: `<companies_table>.<industry_shortlist_column>` in your warehouse (via Hex). In this setup it's a stored enrichment label (for example from Clay, generated from public company descriptions) synced into the warehouse. Reading it is a plain column read; it never calls the enrichment tool. Check and record its coverage on active paying accounts (with the date) before relying on it.

External copy uses the story label. Internal notes keep the warehouse label so the next story can reproduce the grouping.

| Warehouse shortlist label | Story label (external) | Role in stories |
|---|---|---|
| digital marketplace | marketplace apps | B2C; folded into "B2C software and apps" for headlines |
| retail | retail and loyalty apps | B2C; folded into "B2C software and apps" for headlines |
| media | media and streaming apps | B2C; folded into "B2C software and apps" for headlines |
| fintech | fintech and banking apps | B2C; a callout inside "B2C software and apps" |
| financial services | fintech and banking apps | merged with fintech |
| healthcare provider | healthcare software and apps | B2C; a callout inside "B2C software and apps" |
| e-learning | folded into "B2C software and apps" | B2C; never its own block |
| SaaS | split by free-text keywords: consumer software (B2C, folded into "B2C software and apps") or B2B software | B2B software secondary, never the lead |
| agency/consulting | agencies | included only when the number earns it, never the lead |
| manufacturing | manufacturers | included only when the number earns it, never the lead |
| wholesale | wholesalers | included only when the number earns it, never the lead |
| educational institutions | education | included only when the number earns it, never the lead |
| (blank) | left out | never shown; note the share of the cohort it represents in internal notes |

Swap the left column for the labels your own enrichment produces.

## Sub-verticals (from free-text keywords)

Use when a bucket is big enough to split and the split makes the story more specific. Ask Hex to group by keyword in `<industry_free_text_column>`.

| Keyword group | Story label |
|---|---|
| food, delivery, restaurant | food delivery apps |
| ride, mobility, taxi, transport, scooter | mobility apps |
| travel, booking, hotel, flight | travel apps |
| loyalty, rewards, points | loyalty apps |
| game, gaming, casino | gaming apps |
| job, recruitment | job marketplaces |
| automotive, car | automotive marketplaces |

## The headline bundle

For easy reading, every B2C-facing label above rolls up into one published label: **B2C software and apps**. In the fictional example story that was e-learning + media + digital marketplace + retail + SaaS consumer split + healthcare provider + fintech and financial services. Granular callouts (fintech and banking apps, healthcare software and apps) sit inside it as percentages of the block, only where the data shows a distinct pattern. Record the exact labels in the bundle in the internal notes so the next story groups the same way.

## Naming rules

- Always plural, always "apps" for B2C software cohorts, so the reader hears "companies like mine". Say "healthcare software and apps", never "telehealth".
- Never attach a country, a size or a download count to a vertical label. That's how a cohort becomes a name.
- Keep labels stable across stories. If a new warehouse label appears, add it here before using it.
