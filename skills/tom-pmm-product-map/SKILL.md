---
name: tom-pmm-product-map
description: Gives Claude detailed screen-by-screen knowledge of the Example Feedback product (a fictional customer feedback platform) by reading a live product map from the project files. Use this skill whenever anyone needs product context, such as planning a product tour, writing a demo script, building an onboarding flow, understanding navigation paths, describing what a screen looks like, or referencing specific UI elements. Trigger on any phrase like "plan a product tour", "what does the survey editor look like", "how do I get to Feedback Library", "map out the product", "what screens should we show", "build a demo flow", or any task that requires knowing the product UI. Always use this skill before generating any product tour, demo, or screen-level content. Do not rely on general knowledge of the product without loading the map first.
---

# Product Map

This skill loads a first-hand product map of the Example Feedback application from the project files. All product tour planning, demo scripting, and screen-level content must be grounded in this map.

The examples use Example Feedback, a fictional customer feedback platform. Replace the navigation areas and screen names with your own product's.

---

## Step 1: Load the product map

Read the file `product-map.md` from the project files in full. Do not summarize or truncate it. Every screen entry is needed.

If the file is not present, tell the user and ask them to add `product-map.md` to the project files before continuing.

---

## Step 2: Orient yourself

Once the map is loaded, note:

- **Navigation model:** six top-level areas (Home, Surveys, Boards, AI Chat, Hub (Feedback Library), Integrations), accessible from a fixed left rail
- **Excluded areas (per capture brief):** user profile, workspace settings, org settings, billing, password and security. These were intentionally not explored.

---

## Step 3: Use the map

Apply the product map to the task at hand. Common use cases:

### Product tour planning
Identify the strongest 6 to 9 screen sequence for the target audience. For each stop, reference the screen's **Key elements** to describe what the user sees, and use **Connects to** to build the logical flow between stops.

When recommending a tour sequence, call out:
- The single best "aha moment" screen: the one that lands the value proposition most clearly
- Any screens to skip for a given audience (for example, skip Configure/Share for a Feedback Library-focused demo)

### Demo script writing
Use **What it is** and **Key elements** for accurate screen descriptions. Use **How you got here** to write accurate navigation instructions. Never invent screen names, button labels, or UI elements. Use only what the map records.

### Onboarding flow design
Use **Connects to** fields to map logical next steps from any given screen. Use the **New Research Project wizard** and **Create New Survey flow** screens as the primary onboarding entry points.

### General product questions
Answer any question about what a screen is, what it contains, or how to navigate to it using the map entries directly.

---

## Keeping the map current

The product map was last captured: **<CAPTURE_DATE>**

If the user mentions a screen or feature that does not appear in the map, flag it and suggest re-running the Cowork capture task to regenerate `product-map.md` and re-upload it to the project files.
