# -*- coding: utf-8 -*-
"""
example_deck.py  -  canonical usage pattern for slide_kit.

Run it to see the engine produce a PPTX + PDF:
    cd scripts && python3 example_deck.py

Copy this structure when building a real deck. For real work, export to an
outputs/ folder (or wherever your environment delivers files to the user).

All content below is fictional: Example Feedback is a made-up customer
feedback platform and Jordan Lee is a placeholder presenter.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slide_kit import (cover, statement, divider, agenda, split, bullets, cards, close,
                       render, export_pptx, export_pdf, mark, doc, foot, TEALL, INK, TEALD)

# A custom flow slide, to show how to compose beyond the archetypes using the shared CSS.
def flow_three(eyebrow, title_html, page):
    return doc(f"""
<div class='stage'>
  <div class='pad'>
    <div class='eyebrow'>{eyebrow}</div>
    <h1 class='t' style='margin-top:16px'>{title_html}</h1>
    <div style='position:absolute;left:76px;right:76px;top:250px;display:flex;gap:26px'>
      <div class='card' style='flex:1;height:200px;padding:28px'>
        <div style='font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--acc)'>Collect</div>
        <div style='margin-top:40px;font-size:24px;font-weight:800;line-height:1.15'>Feedback on every channel</div></div>
      <div style='display:flex;align-items:center;font-size:32px;color:var(--accL);font-weight:700'>&#8594;</div>
      <div style='flex:1;height:200px;padding:28px;border-radius:18px;background:var(--acc);color:#fff;position:relative;overflow:hidden'>
        {mark('#ffffff','190px','right:-60px;bottom:-70px;',0.12)}
        <div style='font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#b7cdf7'>Analyze</div>
        <div style='margin-top:40px;font-size:24px;font-weight:800;line-height:1.15'>Themes and answers</div></div>
      <div style='display:flex;align-items:center;font-size:32px;color:var(--accL);font-weight:700'>&#8594;</div>
      <div class='card' style='flex:1;height:200px;padding:28px;background:var(--tealL);border-color:#a6e2da'>
        <div style='font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--tealD)'>Act</div>
        <div style='margin-top:40px;font-size:24px;font-weight:800;line-height:1.15'>Into your stack</div></div>
    </div>
  </div>
  {foot(page)}
</div>""")

slides = [
    cover("Example Feedback", "Turn feedback into<br><hl>product direction</hl>", "A short overview", "Jordan Lee"),
    statement("The premise", "Most feedback never becomes a <hlt>decision</hlt>. That is the gap we close.", 2),
    divider("01", "How it works.", 3),
    flow_three("The loop", "Collect, analyze, <hl>act</hl>.", 4),
    agenda("What we&#8217;ll cover", [
        ("01", "Where Example Feedback fits"),
        ("02", "The feedback layer"),
        ("03", "Use cases"),
    ], 5),
    split("The 30-second version", "Example Feedback is a<br><hlt>customer feedback platform</hlt>", "Two products: Surveys and Feedback Lab",
          [("Collect", "Run NPS, CSAT and CES on every channel"),
           ("Analyze", "Turn scattered responses into clear themes"),
           ("Act", "Push what you learn into your stack")], 6),
    cards("Use cases", "Turn scores into <hl>action</hl>.", [
        ("01", "Rescue detractors", "A low score triggers a save play automatically.", True),
        ("02", "Grow promoters", "Happy customers flow into referral and review asks.", False),
        ("03", "Act post-purchase", "A CSAT dip routes to support, a high score to upsell.", False),
    ], 7),
    close("Feedback in.<br><hlt>Decisions out.</hlt>", "example.com"),
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "example_output")
    png = os.path.join(out, "png")
    render(slides, png)
    os.makedirs(out, exist_ok=True)
    export_pptx(png, os.path.join(out, "Example-Deck.pptx"))
    export_pdf(png, os.path.join(out, "Example-Deck.pdf"))
    print("Built", len(slides), "slides ->", out)
