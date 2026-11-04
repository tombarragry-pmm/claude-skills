# making-a-remotion-video

Plans, scripts and writes Remotion video code scene by scene, using a shared set of brand tokens, reusable components, proven scene patterns and lessons learned from real productions.

Originally built: November 2026

## What it does

1. Splits the work: storyboard, copy and timing in chat; scene building, preview and rendering in Claude Code.
2. Applies brand tokens from one styles file and reuses a small component library (glow orb, headline, logo header).
3. Builds scenes from proven patterns: text scenes, typewriter swaps, alternating text and product video beats, logo walls.
4. Handles product clips: checks specs with FFmpeg, converts timecodes to source frames, and extracts frames for review.
5. Enforces timing and animation rules (frame-driven animation, clamped interpolation, recalculated sequence offsets) and the hard lessons learned.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

- Node.js and a Remotion project, plus FFmpeg for clip inspection and frame extraction.
- Claude Code for building and rendering. Figma is optional, for exporting brand assets.

## Make it yours

The examples use Example Feedback, a fictional customer feedback platform. Replace the brand tokens in `src/styles.ts` (the colors here are placeholders), put your own white logo at `public/images/logo-primary-white.svg`, swap the headline copy, composition ID and output file name, and point the reference video and Figma file key and node IDs at your own.
