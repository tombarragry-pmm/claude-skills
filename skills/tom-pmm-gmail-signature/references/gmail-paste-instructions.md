# Installing the signature in Gmail

Give the person these steps once the HTML file is generated. The file contains
only the signature (no extra chrome), so a select-all copies exactly the right
thing. Keep the tone friendly and walk through it in order.

## Why a special file is needed

Gmail's signature editor strips out SVG graphics entirely. The company logo,
social icons, and pill icons are usually vector by default, so a naive copy-paste
would drop every image and leave only text. The generated file solves this by
using a PNG for each graphic (embedded as base64, or hosted). When the rendered
signature is copied from a browser and pasted into Gmail, Gmail re-uploads
embedded images to its own servers automatically, so they stay put and the saved
signature remains small.

## Steps to give the person

Always present these as a numbered, click-by-click list. Be explicit about where
to click: name the actual button or menu item, don't just say "open" or "save".

1. **Download this HTML file first.** On the file card shown in the chat, click the
   download icon (the small downward-arrow button in its top-right corner). It
   saves to the Downloads folder. (The preview in the chat is not a real browser
   tab, so the copy step will not work until the file is downloaded.)
2. **Open the downloaded file.** Go to the Downloads folder, find the file, and
   double-click it to open it in a browser. If double-clicking opens the wrong app
   or shows raw code, open Chrome first, press Cmd+O (Mac) or Ctrl+O (Windows), and
   pick the file. The page should show only the signature: no title at the top and
   no paragraph at the bottom. If those appear, the wrong file was opened.
3. **Select the signature.** Click anywhere on the signature, then press Cmd+A
   (Mac) or Ctrl+A (Windows) to select all of it.
4. **Copy it.** Press Cmd+C (Mac) or Ctrl+C (Windows). Copy the rendered signature
   from the browser view, not the HTML source.
5. **Open Gmail signature settings.** In Gmail, click the gear icon (top right) →
   See all settings → stay on the General tab → scroll to the Signature section.
   If there's no signature yet, click "Create new" and name it.
6. **Paste it.** Click inside the signature box and press Cmd+V (Mac) or Ctrl+V
   (Windows).
7. **Save.** Scroll to the very bottom of the page and click "Save changes". This
   step is easy to miss: without it, nothing is saved.
8. **Set it as default.** Just below the signature box, use the "Signature defaults"
   dropdowns to choose this signature for new emails and for replies/forwards, so
   it inserts automatically.
9. **Test it.** Open a new compose window; the signature should appear on its own.
   Sending a test email to yourself is the best confirmation.

## Things to mention so they aren't surprised

- **Font falls back to Arial.** Inter is not a web-safe email font, so Gmail and
  most clients render the text in Arial. It's very close, just slightly different
  letterforms.
- **Pill corners may square off.** Gmail sometimes strips `border-radius`. The
  pills keep their accent fill and border (a `bgcolor` attribute protects the
  fill), so they still read as buttons, just possibly with square corners.
- **If an image drops on paste**, use Gmail's "Insert image" button (the mountain
  icon in the signature toolbar). With this file the images are embedded and
  normally come through fine, but that button is the reliable fallback.

## Optional: hosted-image version for IT / team rollout

For a crisper, more bulletproof rollout across many people, IT can host the PNGs
from `assets/images/` at public URLs (your CDN, public cloud storage, etc.), set
`IMAGE_BASE_URL` in `scripts/build_signature.py` to that folder, and remove the
local PNGs so the script references them with `<img src>` instead of base64. This
keeps images sharp on every client and the signature tiny. Only pursue this if
the person asks for a team-wide deployment: the embedded-PNG file is the right
default for an individual setting up their own signature.
