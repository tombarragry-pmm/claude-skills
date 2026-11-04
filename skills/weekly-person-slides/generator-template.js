// Full-team weekly meeting deck: cover slide, then a "Done this week" and a
// "Next week" slide per person, then a closing slide.
// All names, tasks and URLs below are fictional examples. Replace TEAM with
// real data pulled from Linear (see SKILL.md, Step 3).

const PptxGenJS = require('pptxgenjs');
const path = require('path');
const fs = require('fs');
const os = require('os');

const ASSETS = path.join(__dirname, 'assets');
const LUCIDE_DIR = path.join(__dirname, 'node_modules', 'lucide-static', 'icons');
const TMP_ICON_DIR = path.join(os.tmpdir(), 'weekly-slides-icons');
if (!fs.existsSync(TMP_ICON_DIR)) fs.mkdirSync(TMP_ICON_DIR, { recursive: true });
const OUT_DIR = path.join(__dirname, 'outputs');
if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });

// ─── Colors (placeholder palette, replace with your brand) ─────────────────
const C = {
  pillDone:    '5CCFC0', // teal pill on the Done slide
  accent:      '5B8DEF', // accent text, links, arrows, Next week pill
  accentTint:  'E8F0FD', // right column background, FYI label background
  phBorder:    'B9CEF5', // screenshot placeholder dashed border
  phIcon:      '8FB0F2', // screenshot placeholder icon and label
  fyiBg:       'F6F9FF', // FYI panel background
  fyiBorder:   'DCE7FC', // FYI panel border
  fyiHint:     'B7C9EC', // FYI placeholder text
  text:        '1A1A1A',
  textMuted:   '666666',
  textFaint:   'BBBBBB',
  textGhost:   'CCCCCC',
  done:        '20C997', // check icon
  blocked:     'D64545', // blocked text and icon
  blockedBg:   'FCEAEA',
};

const M         = 0.55;
const MT        = 0.55;
const PILL_H    = 0.40;
const TITLE_Y   = MT + PILL_H + 0.30;
const BODY_Y    = TITLE_Y + 1.10;
const ICON_Y    = 7.5 - 0.55 - 0.28;
const CONTENT_W = 13.33 - M * 2;
const COL_R_X   = 7.5;
const COL_R_W   = 13.33 - COL_R_X - M;
const COL_L_W   = COL_R_X - M - 0.4;

// Next week layout: left bullet list + right FYI panel
const NW_CARDS_W  = 8.4;   // left area for the bullets
const NW_FYI_X    = 9.2;   // FYI panel start
const NW_FYI_W    = 13.33 - NW_FYI_X - M;

// assets/icon-black.svg: your brand icon (small square mark)
// assets/logo-black.svg: your wordmark logo
// assets/cover-bg.svg:   a full-slide background for the cover and closing slides
const ICON_BLACK = path.join(ASSETS, 'icon-black.svg');
const LOGO_BLACK = path.join(ASSETS, 'logo-black.svg');
const COVER_BG   = path.join(ASSETS, 'cover-bg.svg');
const WEEK_LABEL = 'Week of June 15 to 19, 2026';

// Placeholder issue links. Replace with your real Linear issue URLs.
const ISSUE = (key) => `https://example.com/linear/issue/${key}`;

// ─── TEAM DATA (fictional) ─────────────────────────────────────────────────
const TEAM = [
  {
    name: 'Jordan Lee', role: 'Head of Marketing', area: 'Demand Gen & Strategy',
    done: [
      {
        text: 'Contact page redesign',
        url: ISSUE('TEAM-101'),
        subbullets: [
          { text: 'Inquiry type dropdown added and mapped to the CRM', url: ISSUE('TEAM-102') },
          { text: 'New routing workflow live (low-priority queue for general inquiries)', url: null },
        ],
      },
      { text: 'Outbound kickoff deck for the sales team', url: ISSUE('TEAM-110') },
      { text: 'Competitor comparison: research and messaging', url: ISSUE('TEAM-114') },
    ],
    blocked: [
      { text: 'Paid search campaign launch (ad account access pending)', url: ISSUE('TEAM-120') },
    ],
    next: [
      { text: 'Unblock and launch paid search campaign', url: ISSUE('TEAM-120') },
      { text: 'Comparison landing page: final review', url: ISSUE('TEAM-121') },
      { text: 'Q3 budget review with finance', url: ISSUE('TEAM-125') },
    ],
  },
  {
    name: 'Alex Morgan', role: 'Product Marketing', area: 'PMM & Launches',
    done: [
      { text: 'New email signature: project completed', url: ISSUE('TEAM-130') },
      { text: 'In-app changelog kicked off: existing entries audited, budget approved', url: ISSUE('TEAM-131') },
      { text: 'Early access program: Customer.io segment, invite and thank-you automations', url: ISSUE('TEAM-133') },
    ],
    blocked: [],
    next: [
      { text: 'June product update email: copy and build', url: ISSUE('TEAM-140') },
      { text: 'Feature launch: brief review with customer success', url: ISSUE('TEAM-141') },
      { text: 'Update email footer with new feature page link', url: ISSUE('TEAM-142') },
    ],
  },
  {
    // Example of the "In Review counts as done" exception (see SKILL.md, Step 1)
    name: 'Sam Rivera', role: 'Design', area: 'Cross-functional',
    done: [
      { text: 'Comparison page: social image and page graphics', url: ISSUE('TEAM-150') },
      { text: 'Feature page images regenerated', url: ISSUE('WEB-151') },
      { text: '[In review] Homepage graphics', url: ISSUE('WEB-152') },
      { text: '[In review] Webinar page design', url: ISSUE('WEB-153') },
    ],
    blocked: [],
    next: [
      { text: 'Homepage graphics: awaiting review feedback', url: ISSUE('WEB-152') },
      { text: 'Blog article page: new layout in Figma', url: ISSUE('WEB-155') },
      { text: 'Webinar page: awaiting review feedback', url: ISSUE('WEB-153') },
    ],
  },
  {
    name: 'Casey Kim', role: 'Partnerships', area: 'Tech Partnerships',
    done: [],
    blocked: [],
    next: [
      { text: 'Joint webinar with Contoso: debrief and follow-up', url: ISSUE('TEAM-160') },
      { text: 'Northwind Traders integration landing page: in progress', url: ISSUE('TEAM-161') },
      { text: 'Fabrikam integration: in progress', url: ISSUE('TEAM-162') },
    ],
    note: 'No completed issues found in Linear this week. Please add manually.',
  },
];

// ─── Helpers ───────────────────────────────────────────────────────────────
function addIcon(slide) {
  const sz = 0.28;
  slide.addImage({ path: ICON_BLACK, x: 13.33 - M - sz, y: ICON_Y, w: sz, h: sz });
}

function addPill(slide, label, bgColor = C.pillDone, textColor = C.text) {
  const text = label.toUpperCase();
  const w = Math.max(1.5, text.length * 0.105 + 0.6);
  slide.addShape('roundRect', { x: M, y: MT, w, h: PILL_H, fill: { color: bgColor }, line: { type: 'none' }, rectRadius: 0.2 });
  slide.addText(text, { x: M, y: MT, w, h: PILL_H, fontFace: 'Inter', fontSize: 12, bold: true, color: textColor, align: 'center', valign: 'middle', charSpacing: 0.5 });
}

function addLucideIcon(slide, name, opts = {}) {
  const { x, y, w = 0.28, h = 0.28, color = C.accent, strokeWidth = 2 } = opts;
  const srcPath = path.join(LUCIDE_DIR, `${name}.svg`);
  if (!fs.existsSync(srcPath)) return;
  let svg = fs.readFileSync(srcPath, 'utf8')
    .replace(/stroke="currentColor"/g, `stroke="#${color}"`)
    .replace(/stroke-width="2"/g, `stroke-width="${strokeWidth}"`);
  const key = `${name}-${color}`.replace(/[^a-z0-9]/gi, '_');
  const tmp = path.join(TMP_ICON_DIR, `${key}.svg`);
  fs.writeFileSync(tmp, svg);
  slide.addImage({ path: tmp, x, y, w, h });
}

function addPersonHeader(slide, person, colW = COL_L_W) {
  slide.addText(person.name, { x: M, y: TITLE_Y, w: colW, h: 0.65, fontFace: 'Inter', fontSize: 26, bold: true, color: C.text, valign: 'top' });
  slide.addText(`${person.role}  ·  ${person.area}`, { x: M, y: TITLE_Y + 0.65, w: colW, h: 0.28, fontFace: 'Inter', fontSize: 12, color: C.accent, valign: 'top' });
}

function addImagePlaceholder(slide, x, y, w, h, label) {
  slide.addShape('rect', { x, y, w, h, fill: { color: C.accentTint }, line: { color: C.phBorder, pt: 1.5, dashType: 'dash' } });
  const is = 0.38, ix = x + (w - is) / 2, iy = y + h / 2 - 0.46;
  slide.addShape('rect', { x: ix, y: iy, w: is, h: is * 0.75, fill: { type: 'none' }, line: { color: C.phIcon, pt: 1.5 }, rectRadius: 0.04 });
  slide.addShape('ellipse', { x: ix + is * 0.3, y: iy + is * 0.12, w: is * 0.38, h: is * 0.38, fill: { type: 'none' }, line: { color: C.phIcon, pt: 1.5 } });
  slide.addText(label, { x, y: y + h / 2 + 0.05, w, h: 0.34, fontFace: 'Inter', fontSize: 10, color: C.phIcon, align: 'center', valign: 'top', italic: true });
}

function textWithLink(text, url, fontSize, textColor, linkColor) {
  const runs = [{ text, options: { fontFace: 'Inter', fontSize, color: textColor, bold: false } }];
  if (url) runs.push({ text: ' ↗', options: { fontFace: 'Inter', fontSize: fontSize - 2, color: linkColor, bold: false, hyperlink: { url } } });
  return runs;
}

// ─── DONE SLIDE ────────────────────────────────────────────────────────────
function addDoneSlide(pptx, person) {
  const s = pptx.addSlide();
  addPill(s, 'Done this week');
  addPersonHeader(s, person);

  // Right col screenshots
  s.addShape('rect', { x: COL_R_X - 0.25, y: 0, w: 13.33 - (COL_R_X - 0.25), h: 7.5, fill: { color: C.accentTint }, line: { type: 'none' } });
  addImagePlaceholder(s, COL_R_X + 0.05, 0.5, COL_R_W, 3.05, 'Screenshot / result #1');
  addImagePlaceholder(s, COL_R_X + 0.05, 3.75, COL_R_W, 3.3, 'Screenshot / result #2');

  // Generous spacing between bullets
  const MAIN_ROW_H   = 0.70;  // tall enough for wrapping text
  const MAIN_GAP     = 0.22;  // breathing room between items
  const SUB_ROW_H    = 0.38;
  const SUB_GAP      = 0.10;
  const SUB_INDENT   = 0.38;
  const ICON_SZ      = 0.28;

  let y = BODY_Y + 0.12;

  if (person.done.length === 0) {
    s.addText('No completed issues found this week. Please add manually.', {
      x: M, y, w: COL_L_W, h: 0.5, fontFace: 'Inter', fontSize: 13, color: C.textFaint, italic: true, valign: 'top',
    });
  }

  person.done.forEach(item => {
    addLucideIcon(s, 'check-circle-2', { x: M, y: y + 0.14, w: ICON_SZ, h: ICON_SZ, color: C.done });
    s.addText(textWithLink(item.text, item.url, 15, C.text, C.accent), {
      x: M + 0.40, y, w: COL_L_W - 0.40, h: MAIN_ROW_H, valign: 'middle', wrap: true,
    });
    y += MAIN_ROW_H + MAIN_GAP;

    (item.subbullets || []).forEach(sub => {
      s.addShape('rect', { x: M + SUB_INDENT + 0.02, y: y + 0.16, w: 0.10, h: 0.025, fill: { color: C.textFaint }, line: { type: 'none' } });
      s.addText(textWithLink(sub.text, sub.url, 12, C.textMuted, C.accent), {
        x: M + SUB_INDENT + 0.20, y, w: COL_L_W - SUB_INDENT - 0.12, h: SUB_ROW_H, valign: 'middle',
      });
      y += SUB_ROW_H + SUB_GAP;
    });

    if (item.subbullets && item.subbullets.length) y += 0.06;
  });

  // Blocked section
  if (person.blocked && person.blocked.length > 0) {
    y += 0.14;
    const bw = 1.05;
    s.addShape('roundRect', { x: M, y, w: bw, h: 0.26, fill: { color: C.blockedBg }, line: { type: 'none' }, rectRadius: 0.07 });
    s.addText('BLOCKED', { x: M, y, w: bw, h: 0.26, fontFace: 'Inter', fontSize: 9, bold: true, color: C.blocked, align: 'center', valign: 'middle', charSpacing: 1 });
    y += 0.36;

    person.blocked.forEach(item => {
      addLucideIcon(s, 'alert-triangle', { x: M, y: y + 0.10, w: ICON_SZ, h: ICON_SZ, color: C.blocked });
      s.addText(textWithLink(item.text, item.url, 13, C.blocked, C.blocked), {
        x: M + 0.40, y, w: COL_L_W - 0.40, h: SUB_ROW_H + 0.10, valign: 'middle',
      });
      y += SUB_ROW_H + 0.20;
    });
  }

  if (person.note && person.done.length === 0) {
    s.addText(person.note, { x: M, y: 6.7, w: COL_L_W, h: 0.35, fontFace: 'Inter', fontSize: 10, color: C.textGhost, italic: true, valign: 'top' });
  }

  addIcon(s);
}


// ─── NEXT WEEK SLIDE ───────────────────────────────────────────────────────
function addNextSlide(pptx, person) {
  const s = pptx.addSlide();
  addPill(s, 'Next week', C.accent, 'FFFFFF');
  addPersonHeader(s, person, CONTENT_W);

  // ── FYI panel (right) ───────────────────────────────────────────────────
  const FYI_Y  = BODY_Y + 0.10;
  const FYI_H  = 7.5 - FYI_Y - 0.55;

  // Panel background
  s.addShape('roundRect', {
    x: NW_FYI_X - 0.1, y: FYI_Y - 0.1, w: NW_FYI_W + 0.1, h: FYI_H,
    fill: { color: C.fyiBg }, line: { color: C.fyiBorder, pt: 1 }, rectRadius: 0.12,
  });

  // FYI label
  s.addShape('roundRect', {
    x: NW_FYI_X + 0.18, y: FYI_Y + 0.18, w: 0.70, h: 0.26,
    fill: { color: C.accentTint }, line: { type: 'none' }, rectRadius: 0.07,
  });
  s.addText('FYI', {
    x: NW_FYI_X + 0.18, y: FYI_Y + 0.18, w: 0.70, h: 0.26,
    fontFace: 'Inter', fontSize: 9, bold: true, color: C.accent,
    align: 'center', valign: 'middle', charSpacing: 1.5,
  });

  // Single large editable text placeholder below the label
  s.addText('Add context, links or notes here…', {
    x: NW_FYI_X + 0.18, y: FYI_Y + 0.62, w: NW_FYI_W - 0.28, h: FYI_H - 0.82,
    fontFace: 'Inter', fontSize: 12, color: C.fyiHint, italic: true,
    valign: 'top', wrap: true,
  });

  // ── Bullet list (left area) ─────────────────────────────────────────────
  const MAIN_ROW_H = 0.55;
  const MAIN_GAP   = 0.10;
  const ICON_SZ    = 0.28;
  let y = FYI_Y;

  person.next.forEach(item => {
    addLucideIcon(s, 'arrow-right', { x: M, y: y + 0.20, w: ICON_SZ, h: ICON_SZ, color: C.accent });
    s.addText(textWithLink(item.text, item.url, 15, C.text, C.accent), {
      x: M + 0.40, y, w: NW_FYI_X - M - 0.65, h: MAIN_ROW_H,
      valign: 'middle', wrap: true,
    });
    y += MAIN_ROW_H + MAIN_GAP;
  });

  if (person.note && person.next.length === 0) {
    s.addText(person.note, { x: M, y: y + 0.1, w: NW_FYI_X - M - 0.65, h: 0.4,
      fontFace: 'Inter', fontSize: 10, color: C.textGhost, italic: true, valign: 'top' });
  }

  addIcon(s);
}

// ─── COVER + CLOSING ───────────────────────────────────────────────────────
function addCover(pptx) {
  const s = pptx.addSlide();
  s.addImage({ path: COVER_BG, x: 0, y: 0, w: 13.33, h: 7.5 });
  s.addText('Marketing\nWeekly\nMeeting', { x: M, y: 0.85, w: 7.2, h: 3.8, fontFace: 'Inter', fontSize: 52, bold: true, color: C.text, valign: 'top' });
  s.addText(WEEK_LABEL, { x: M, y: 5.0, w: 7.0, h: 0.45, fontFace: 'Inter', fontSize: 20, color: C.accent });
  s.addText('Example Feedback Marketing Team', { x: M, y: 5.5, w: 7.0, h: 0.38, fontFace: 'Inter', fontSize: 16, color: C.accent });
  s.addImage({ path: LOGO_BLACK, x: M, y: 6.9, w: 1.4, h: 0.26 });
}

function addClosing(pptx) {
  const s = pptx.addSlide();
  s.addImage({ path: COVER_BG, x: 0, y: 0, w: 13.33, h: 7.5 });
  s.addText('See you\nnext week.', { x: M, y: 2.3, w: 8, h: 3.5, fontFace: 'Inter', fontSize: 72, bold: true, color: C.text, valign: 'top' });
  s.addImage({ path: LOGO_BLACK, x: M, y: 6.9, w: 1.4, h: 0.26 });
}

// ─── MAIN ──────────────────────────────────────────────────────────────────
async function build() {
  const pptx = new PptxGenJS();
  pptx.layout = 'LAYOUT_WIDE';
  pptx.defineLayout({ name: 'LAYOUT_WIDE', width: 13.33, height: 7.5 });
  addCover(pptx);
  TEAM.forEach(p => { addDoneSlide(pptx, p); addNextSlide(pptx, p); });
  addClosing(pptx);
  const out = path.join(OUT_DIR, 'marketing-weekly-template.pptx');
  await pptx.writeFile({ fileName: out });
  console.log(`✅ ${TEAM.length * 2 + 2} slides → ${out}`);
}
build().catch(e => { console.error(e); process.exit(1); });
