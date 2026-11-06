# tom-pmm-product-map

Grounds product tours, demo scripts and onboarding flows in a first-hand, screen-by-screen map of the product, so Claude never invents a screen name or button label.

Originally built: November 2026

## What it does

1. Loads `product-map.md` from the project files, in full.
2. Orients on the navigation model and the areas the capture left out.
3. Plans tours (6 to 9 stops, with the "aha moment" screen called out), writes demo scripts, designs onboarding flows and answers screen-level questions, all from the map.
4. Flags any screen that isn't in the map and suggests re-running the capture.

## Files

- `SKILL.md`: the instructions Claude follows.

## Requirements

- A `product-map.md` file in your Claude project. Each screen entry should have: What it is, How you got here, Key elements and Connects to. You can generate one by having Claude Cowork explore your product's UI.

## Make it yours

Replace Example Feedback, the navigation areas, the example screen names and the capture date with your own.
