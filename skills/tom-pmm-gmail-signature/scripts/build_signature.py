#!/usr/bin/env python3
"""Build a Gmail-ready Example Feedback email signature.

Stamps a person's name and role into the signature template. Brand graphics
are PNGs (Gmail strips SVG on paste). For each graphic the script either:

  * embeds the local PNG from assets/images/<key>.png as base64, if that file
    exists, so the result needs no image hosting, or
  * falls back to a hosted URL (IMAGE_BASE_URL + <key>.png) if it does not.

Only uses the Python standard library.

Usage:
    python build_signature.py --name "Jordan Lee" --role "Product Designer" \
        --out outputs/signature_gmail.html

All brand content below (links, labels, colors, image URL) is placeholder
content for Example Feedback, a fictional customer feedback platform.
Replace it with your own.
"""
import argparse
import base64
import html
import os

# Brand graphics, in display dimensions (width, height in px). Export the PNGs
# at 3x for retina sharpness; they are displayed at these sizes.
IMAGES = {
    "logo": (100, 18),
    "linkedin": (28, 28),
    "youtube": (28, 28),
    "website": (28, 28),
    "linkedin_pill": (28, 28),
    "youtube_pill": (28, 28),
    "website_pill": (28, 28),
    "ic_surveys": (14, 14),
    "ic_research": (14, 14),
    "ic_integrations": (14, 14),
}

# Where the PNGs are hosted, used when a local PNG is missing. Placeholder:
# replace with your own public image host or CDN folder.
IMAGE_BASE_URL = "https://example.com/email-signature/"

# Fixed brand content (not user-editable per person). Placeholders.
BRAND_NAME = "Example Feedback"
BRAND_URL = "https://example.com/"
FONT = "'Inter', Arial, Helvetica, sans-serif"
CATEGORY_LINE = "Customer Feedback Platform"
SOCIAL_LINKS = {
    "linkedin": "https://www.linkedin.com/company/example/",
    "youtube": "https://www.youtube.com/@example",
    "website": BRAND_URL,
}
PILLS = [
    ("ic_surveys", "Surveys", "https://example.com/surveys/"),
    ("ic_research", "Feedback Lab", "https://example.com/feedback-lab/"),
    ("ic_integrations", "30+ Integrations", "https://example.com/integrations/"),
]

# Placeholder palette, replace with your brand.
ACCENT = "#1F5AD6"        # CTA button fill, pill label text
ACCENT_TINT = "#E8F0FD"   # filled pill background
ACCENT_BORDER = "#CFE0FB" # pill border, nav dividers
INK = "#1A1A2E"           # name, category line
INK_SOFT = "#44475A"      # role
RULE = "#E2E3E9"          # vertical and horizontal rules


def image_src(images_dir, key):
    """Base64 data URI for a local PNG, or the hosted URL if the file is missing."""
    path = os.path.join(images_dir, f"{key}.png")
    if os.path.isfile(path):
        with open(path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode()
    return IMAGE_BASE_URL + f"{key}.png"


def build(name, role, images_dir, booking_url=None):
    src = {k: image_src(images_dir, k) for k in IMAGES}

    def img(key, alt):
        w, h = IMAGES[key]
        return (f'<img src="{src[key]}" width="{w}" height="{h}" alt="{alt}" '
                f'style="display:block; border:0; outline:none; '
                f'width:{w}px; height:{h}px;">')

    name_e = html.escape(name)
    role_e = html.escape(role)

    # Optional "Book a call with me" CTA, only rendered if a link is given.
    booking_row = ""
    if booking_url:
        booking_e = html.escape(booking_url)
        booking_row = (
            f'<tr><td style="padding:14px 0 0;">'
            f'<a href="{booking_e}" style="text-decoration:none; color:#FFFFFF;">'
            f'<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;"><tr>'
            f'<td bgcolor="{ACCENT}" style="background:{ACCENT}; border-radius:999px; '
            f'padding:6px 16px; font-family:{FONT}; font-size:12px; line-height:16px; '
            f'font-weight:600; color:#FFFFFF; white-space:nowrap;">Book a call with me</td>'
            f'</tr></table></a></td></tr>'
        )

    social_cells = []
    social_suffix = "_pill" if booking_url else ""
    for i, base in enumerate(["linkedin", "youtube", "website"]):
        key = base + social_suffix
        pad = "14px 8px 0 0" if i < 2 else "14px 0 0 0"
        alt = base.capitalize()
        social_cells.append(
            f'<td style="padding:{pad};">'
            f'<a href="{SOCIAL_LINKS[base]}">{img(key, alt)}</a></td>')
    social_row = "".join(social_cells)

    pill_cells = []
    n = len(PILLS)
    if booking_url:
        # Footer-nav style (icon + label, divider lines between, no fill), used
        # alongside the booking-call CTA so the row doesn't compete with it.
        for i, (icon, label, url) in enumerate(PILLS):
            if i == 0:
                pad = "16px 14px 0 0"
            elif i == n - 1:
                pad = "16px 0 0 14px"
            else:
                pad = "16px 14px 0 14px"
            pill_cells.append(
                f'<td style="vertical-align:middle; padding:{pad};">'
                f'<a href="{url}" style="text-decoration:none;">'
                f'<table cellpadding="0" cellspacing="0" border="0"><tr>'
                f'<td style="vertical-align:middle; padding:0 6px 0 0; line-height:0;">{img(icon, "")}</td>'
                f'<td style="font-family:{FONT}; font-size:12px; font-weight:600; color:{ACCENT}; '
                f'vertical-align:middle; white-space:nowrap;">{html.escape(label)}</td>'
                f'</tr></table></a></td>')
            if i < n - 1:
                pill_cells.append(
                    f'<td style="vertical-align:middle; padding:16px 0 0;">'
                    f'<div style="width:1px; height:16px; background:{ACCENT_BORDER}; '
                    f'font-size:0; line-height:0;">&nbsp;</div></td>')
    else:
        # Filled pill style (light accent chips), used when there is no CTA button.
        for i, (icon, label, url) in enumerate(PILLS):
            pad = "16px 8px 0 0" if i < n - 1 else "16px 0 0 0"
            pill_cells.append(
                f'<td style="vertical-align:middle; padding:{pad};">'
                f'<a href="{url}" style="text-decoration:none;">'
                f'<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;"><tr>'
                f'<td bgcolor="{ACCENT_TINT}" style="background:{ACCENT_TINT}; border:1px solid {ACCENT_BORDER}; '
                f'border-radius:999px; padding:7px 14px;">'
                f'<table cellpadding="0" cellspacing="0" border="0"><tr>'
                f'<td style="vertical-align:middle; padding:0 6px 0 0; line-height:0;">{img(icon, "")}</td>'
                f'<td style="font-family:{FONT}; font-size:12px; font-weight:600; color:{ACCENT}; '
                f'vertical-align:middle; white-space:nowrap;">{html.escape(label)}</td>'
                f'</tr></table></td></tr></table></a></td>')
    pill_row = "".join(pill_cells)

    signature = f'''<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse; font-family:{FONT}; color:{INK};">
  <tr>
    <td style="padding:0 0 16px;">
      <table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse; width:100%;">
        <tr>
          <td valign="top" style="vertical-align:top; padding:0; white-space:nowrap;">
            <table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
              <tr><td style="font-family:{FONT}; font-size:15px; line-height:20px; font-weight:700; color:{INK}; padding:0 0 4px;">{name_e}</td></tr>
              <tr><td style="font-family:{FONT}; font-size:12px; line-height:16px; font-weight:400; color:{INK_SOFT}; padding:0;">{role_e}</td></tr>{booking_row}
            </table>
          </td>
          <td style="padding:0 18px;"><div style="width:1px; height:72px; background:{RULE}; font-size:0; line-height:0;">&nbsp;</div></td>
          <td valign="top" style="vertical-align:top; text-align:left; width:281px; padding:0;">
            <a href="{BRAND_URL}">{img("logo", BRAND_NAME)}</a>
            <div style="font-family:{FONT}; font-size:12px; line-height:16px; font-weight:600; color:{INK}; padding:6px 0 0;">{CATEGORY_LINE}</div>
            <table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;"><tr>{social_row}</tr></table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
  <tr>
    <td style="padding:0;">
      <table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse; border-top:1px solid {RULE};"><tr>{pill_row}</tr></table>
    </td>
  </tr>
</table>'''

    page = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>{BRAND_NAME} email signature: {name_e}</title></head>
<body style="margin:0; padding:24px; background:#FFFFFF;">
{signature}
</body></html>'''
    return page


def main():
    p = argparse.ArgumentParser(description=f"Build a Gmail-ready {BRAND_NAME} signature.")
    p.add_argument("--name", required=True)
    p.add_argument("--role", required=True)
    p.add_argument("--out", required=True, help="Output HTML path")
    p.add_argument("--booking-url", default=None,
                   help="Optional URL for the 'Book a call with me' button")
    p.add_argument("--images-dir", default=None,
                   help="Path to assets/images (defaults to ../assets/images relative to this script)")
    args = p.parse_args()

    images_dir = args.images_dir or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "assets", "images")

    missing = [k for k in IMAGES if not os.path.isfile(os.path.join(images_dir, f"{k}.png"))]
    if missing:
        print(f"Note: {len(missing)} PNG(s) not found in {images_dir}; "
              f"using hosted URLs under {IMAGE_BASE_URL} for: {', '.join(missing)}")

    page = build(args.name, args.role, images_dir, booking_url=args.booking_url)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"Wrote {args.out} ({len(page)} chars)")


if __name__ == "__main__":
    main()
