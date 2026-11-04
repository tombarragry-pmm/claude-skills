---
name: making-a-remotion-video
description: Use this skill whenever the user asks for help planning, scripting, or generating Remotion video code for Example Feedback (a fictional customer feedback platform) or their own brand. Triggers include any mention of Remotion, video production, product demo video, feature announcement video, social clip, or motion graphics. Also trigger when the user shares a storyboard or asks for scene structure help. This skill covers the Remotion framework fundamentals, brand tokens, a reusable component library, proven scene patterns, the video asset workflow, and hard lessons learned from production.
---

# Making a Remotion Video

The examples use Example Feedback, a fictional customer feedback platform. Swap the brand tokens, logo, copy and file names for your own.

## How We Work

**Workflow split:**

In Claude.ai (chat interface):
- Write storyboard and scene structure
- Draft all on-screen copy
- Specify timing and scene lengths
- Analyze product video clips via frame extraction
- Approve each scene before Claude Code builds it

In Claude Code (terminal):
- Build and iterate on scenes one at a time
- Preview via `npx remotion studio`
- Render with `npx remotion render [CompositionID]`

**Always work scene by scene. Never build the full video in one prompt.**

---

## Project Setup

```
Terminal workflow: cd ~/Desktop/[project], then claude
Use the terminal, not the Claude Code desktop app: in our setup the desktop app caused worktree issues
Skills: npx skills add remotion-dev/skills
```

Composition defaults: 1920x1080, 30fps

---

## Brand Tokens

All tokens live in `src/styles.ts`. Never hardcode colors in scene files. The values below are placeholders: replace them with your brand.

```ts
export const brand = {
  accent: '#2F6FEB',        // Primary brand accent: main backgrounds, CTAs
  accentDark: '#1D52C2',    // Pressed/darker accent (placeholder, replace with your brand)
  accentLight: '#E8F0FD',   // Light accent tint
  accentDeep: '#142F6B',    // Very dark accent (placeholder, replace with your brand)
  teal: '#5CCFC0',          // Teal highlight: use sparingly, with TealGlowOrb only
  dark: '#1A1A2E',          // Near-black: dark scene backgrounds
  darkAlt: '#0f0f0f',       // Pure dark: behind product videos
  white: '#ffffff',
  textMuted: '#CFE0FB',     // Muted white-accent for sublines on accent bg
  textOnDark: '#ffffff',
}

export const fonts = {
  primary: "'Inter', 'Helvetica Neue', sans-serif",
}
```

---

## Reusable Component Library

All components live in `src/components/index.tsx`. Always import from here, never recreate.

### TealGlowOrb

A radial gradient that drifts slowly across the scene. Creates the ambient glow effect.

```tsx
<TealGlowOrb
  startY={200}   // Starting Y position in px
  endY={600}     // Ending Y position in px
  duration={180} // Frames to travel from startY to endY
  size={1400}    // Diameter: keep at 1400 so edges bleed off screen
  opacity={0.6}
/>
```

Key rule: size must be 1400 or larger. The orb should always look like ambient light, never a visible circle.

Gradient: `radial-gradient(circle, rgba(140,235,220,1) 0%, rgba(92,207,192,0.7) 20%, rgba(92,207,192,0.2) 55%, transparent 70%)`

### SceneHeadline

Multi-line headline with staggered entrance and optional outline/stroke emphasis word.

```tsx
<SceneHeadline
  lines={["Feedback in the morning.", "Decisions by lunch."]}
  emphasisWord="Decisions"  // Renders as outline/stroke style
  startFrame={15}
  lineDelay={20}            // Frames between each line
  fontSize={110}            // Default 110
/>
```

emphasisWord treatment: `WebkitTextStroke: '2px white', color: 'transparent'`

### LogoHeader

```tsx
<LogoHeader
  size="small"    // 'small' = top center, 'large' = centered on canvas
  startFrame={0}
/>
```

Uses `staticFile('images/logo-primary-white.svg')`: put your own white logo at `public/images/logo-primary-white.svg`. Present in every scene.

---

## Scene Patterns

### Standard Text Scene

```tsx
export const SceneX = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: brand.accent }}>
      <TealGlowOrb startY={200} endY={600} duration={180} />
      <LogoHeader size="small" startFrame={0} />
      <SceneHeadline
        lines={["Your headline here."]}
        emphasisWord="headline"
        startFrame={15}
      />
    </AbsoluteFill>
  );
};
```

### Swapping Text Scene (typewriter delete/type)

Pattern: anchor word stays center. Changing part types in, holds, deletes, next phrase types in.

```tsx
// Delete: phrase.substring(0, Math.round(interpolate(frame, [deleteStart, deleteEnd], [phrase.length, 0], clamped)))
// Type: phrase.substring(0, Math.round(interpolate(frame, [typeStart, typeEnd], [0, phrase.length], clamped)))
// Cursor blink: Math.floor(frame / 12) % 2 === 0 ? '|' : ''
```

### Text + Product Beat Structure

Alternate text beats and product video beats:

```tsx
// Text beat (60 frames)
<Sequence from={0} durationInFrames={60}>
  <AbsoluteFill style={{ backgroundColor: brand.accent }}>
    <TealGlowOrb ... /><LogoHeader ... /><SceneHeadline ... />
  </AbsoluteFill>
</Sequence>

// Product video beat (variable frames = source video frame count)
<Sequence from={60} durationInFrames={248}>
  <AbsoluteFill style={{ backgroundColor: brand.darkAlt }}>
    <Video
      src={staticFile('videos/your-clip.mp4')}
      startFrom={0}
      endAt={248}
      style={{ width: '100%', height: '100%', objectFit: 'contain' }}
    />
  </AbsoluteFill>
</Sequence>
```

### Logo Wall Scene

```tsx
// Heading: "Trusted by over [N] companies including:"
// 2 rows of 6 logos, all white via filter: brightness(0) invert(1)
// Logos in public/images/logos/ as PNG files (only use customer logos you have permission to show)
// Grid: gap 80px columns, 80px rows, logos width 130 to 220px each
```

---

## Video Asset Workflow

### Check specs before using any clip

```
Use FFmpeg to check the frame rate, resolution, and duration of "public/videos/[filename]"
```

### Frame rate calculator

```
startFrom/endAt use SOURCE fps, not Remotion fps (30)

CleanShot X records at ~57.55fps (targeting 60fps):
  timecode 00:14 = 14 × 60 = 840 startFrom

Standard 30fps screen recording:
  timecode 00:14 = 14 × 30 = 420 startFrom
```

### Review clips before editing

```
Use FFmpeg to extract one frame every 5 seconds from "public/videos/[filename]"
and save as JPG in public/frames/[folder-name]/
Name each frame: frame-0000.jpg, frame-0005.jpg etc.
```

Upload frames to Claude.ai chat. Claude identifies key moments and writes the Remotion prompt with correct startFrom/endAt values.

### objectFit rules

- `cover`: fills canvas, crops edges. Use when video is close to 1920x1080.
- `contain`: shows full frame with letterboxing. Use for 1920x930 or non-standard ratios.

---

## Composition Timing Rules

When any scene's durationInFrames changes, ALL subsequent scene from= values must shift.

```tsx
<AbsoluteFill>
  <Sequence from={0} durationInFrames={S1}><Scene1 /></Sequence>
  <Sequence from={S1} durationInFrames={S2}><Scene2 /></Sequence>
  <Sequence from={S1+S2} durationInFrames={S3}><Scene3 /></Sequence>
</AbsoluteFill>
```

Total = sum of all durationInFrames values.

Sequence resets useCurrentFrame() to 0 automatically. No manual localFrame offset needed.

---

## Animation Rules (Non-Negotiable)

```
ALWAYS: All animations via useCurrentFrame(), no CSS transitions
ALWAYS: clamp on every interpolate:
  { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
NEVER: CSS transition, CSS animation, setTimeout, setInterval
```

Spring config for natural feel (not bouncy):
```ts
spring({ fps, frame, config: { damping: 80, stiffness: 400, mass: 0.6 } })
```

Never use damping below 50: it causes visible overshoot.

---

## Hard Lessons Learned

**Text over product video = unreadable at distance.**
Always separate: text-only beats and product-only beats. Clean cuts between them.

**Animated React UI mockups look unprofessional.**
Do not build fake animated product UIs with cursor movement. They never look right. Use real screen recordings.

**Real product video beats everything else.**
Short well-chosen clips from real recordings always look better than React mockups.

**Remotion Studio cache.**
If animations look wrong after code changes, restart: `npx remotion studio`. Safe: all code is in files.

**Logo assets.**
Never download from the Figma API via curl: files corrupt silently. Always export manually from Figma as PNG 4x. Store in `public/images/logos/`. Apply white: `filter: 'brightness(0) invert(1)'`.

**Black gaps between scenes.**
Caused by scene from= values out of sync in MyVideo.tsx. Always recalculate ALL subsequent offsets when any duration changes.

**CleanShot frame rate.**
CleanShot X records at ~57.55fps. Always use 60 as the divisor for startFrom/endAt.

---

## Render Command

```bash
npx remotion render EventBooth --output out/event-booth.mp4
```

Expect 5 to 15 minutes for 1080p.

---

## Reference Files

**Reference video:** `public/videos/reference-video.mp4` (a finished video whose style you want to match)
Visual style target:
- Accent background (`brand.accent`, #2F6FEB) throughout
- Logo small top center every scene
- Large centered headlines weight 900
- Emphasis word in outline/stroke style
- TealGlowOrb drifting slowly each scene
- Clean cuts between scenes

**Figma Design System:** `https://www.figma.com/design/<YOUR_FIGMA_FILE_KEY>/<YOUR_DESIGN_SYSTEM>`
- Colors: node `<COLORS_NODE_ID>`
- Logo: node `<LOGO_NODE_ID>`
