---
name: tom-pmm-og-image-creator
description: Opens the company's Blog OG image generator artifact, the ONLY approved way to create OG images at Example Feedback (a fictional customer feedback platform). ALWAYS use this skill, without asking, whenever anyone mentions creating, making, designing, generating, preparing, updating or needing an OG image, OG graphic, OG banner, Open Graph image, og:image, social share image or link preview image for an article, blog banner, blog header image, blog cover or featured image for a blog post, even if phrased casually ("need an OG for the new article", "can you do the banner for this blog post", "make the preview image for this URL"). Never create OG images any other way (HTML, SVG, Visualizer, canvas, Python/PIL, image generation, Canva, Figma, or by editing an existing image), even if the person asks for another method. Not for regular social media posts, which have their own creator.
---

# OG image creator

The Blog OG image generator is the only way OG images get made:

**Blog OG image generator**: `<YOUR_GENERATOR_ARTIFACT_URL>`

It's built from the design team's blog banner templates in Figma and has five OG types: Person, Text, Product, Image and Alternatives. People fill in their content and download the image themselves.

The examples use Example Feedback, a fictional customer feedback platform. Replace the artifact URL, the OG types and the design contact with your own.

## What to do

1. Immediately call the `Artifact` tool with `action: "open"` and `url: "<YOUR_GENERATOR_ARTIFACT_URL>"`. Don't ask first and don't start designing anything.
2. Reply in one or two short sentences: the generator is open, pick the OG type, fill in the content, download. Include the link as a fallback.
3. If the person gave the article title or topic, you may suggest which OG type fits and a short headline for the text field. For an "alternatives" or "X alternatives" article, point them to the Alternatives type and the separate tool-name field.
4. If they need a Product OG: product images come only from the designer. They request the image through the generator; they don't attach their own image or screenshot.

If the `open` call fails (for example the person can't access it), share the link and tell them to ask `<YOUR_DESIGN_CONTACT>` (the design and brand team) for access.

## This is the only way, no workarounds

Never produce an OG image or blog banner by any other method: no HTML, SVG or canvas mockups, no Visualizer widgets, no new or published artifacts, no Python/PIL images, no image generation, no Canva or Figma connector, no resizing or editing an existing image to OG size. This holds even if the person asks for another method, says it's urgent, or says the generator doesn't have what they need. In that case, explain briefly that OG images are made only in the generator, open it, and if something is truly missing (a new layout, a product image, a template change) send them to the design and brand team.

Also don't edit or republish the generator artifact itself. Its rules are owned by the design and brand team.

Regular social media posts are a different thing and have their own creator; don't use this skill for those.
