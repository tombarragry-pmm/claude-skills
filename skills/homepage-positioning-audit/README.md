# homepage-positioning-audit

Audits a homepage, landing page or page prototype against Fletch PMM's public positioning and messaging frameworks and produces a scannable HTML audit with quoted, severity-rated findings.

Originally built: November 2026

## What it does

1. Reads the page copy from a URL or a screenshot.
2. Maps the copy to Fletch's homepage section flow (hero, problem, solution, value props, and anything below).
3. Grades the 4 positioning questions (what is it, who is it for, what does it replace, why is it better) as clear, partial or unclear, with quoted evidence.
4. Runs cross-cutting checks: capabilities vs benefits, audience anchoring, specificity, and common Fletch flags.
5. Builds an HTML artifact with a TL;DR scoreboard, section-by-section findings and suggested next moves, then offers follow-ups in chat. The audit itself is diagnostic only, with no rewrites.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

- Web fetch, for auditing live URLs. Screenshots need nothing extra.
- Artifacts enabled, for the HTML audit.

## Make it yours

The frameworks are Fletch PMM's public positioning concepts. Point the "Before you start" note at the Claude project that holds your own positioning context, and adjust the severity badge colors to your brand if you like.
