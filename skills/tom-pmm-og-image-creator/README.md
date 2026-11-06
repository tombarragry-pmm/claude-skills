# tom-pmm-og-image-creator

A tiny routing skill: whenever anyone asks for a blog OG image or banner, Claude opens the team's approved OG generator artifact instead of designing one itself. It keeps every blog banner on the brand-approved templates.

Originally built: November 2026

## What it does

1. Opens the OG generator artifact straight away, without asking.
2. Tells the person to pick an OG type, fill in the content and download.
3. Suggests the best OG type and a short headline if the article topic is known.
4. Refuses every workaround (HTML, image generation, editing an old image) and routes real gaps to the design team.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

- An OG generator published as a Claude artifact, built from your design team's templates.

## Make it yours

The examples use Example Feedback, a fictional customer feedback platform. Replace the artifact URL, the OG types and the design contact with your own.
