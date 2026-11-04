---
name: weekly-person-slides
description: >
  Generate two branded Example Feedback weekly meeting slides (Done This Week + Next Week)
  for a specific marketing team member, pulling their tasks directly from Linear.
  Use this skill any time someone asks to:
  - "generate my slides for this week"
  - "create [person]'s weekly slides"
  - "pull my Linear tasks and make slides"
  - "update [name]'s done / next week slides"
  - "run the weekly slides for [name]"
  - "make the weekly deck for [person]"
  Always use this skill: do not generate weekly person slides without it.
compatibility:
  tools: [bash_tool, present_files, Linear MCP]
  node_packages: [pptxgenjs, lucide-static]
  assets: assets/
---

# Weekly Person Slides Skill

Generates two branded .pptx slides for one person:
1. **Done This Week:** completed Linear issues, blocked items, screenshot placeholders
2. **Next Week:** upcoming/in-progress issues as a bullet list + FYI panel

Example Feedback is a fictional company used in the examples. Replace the team table, colors and assets with your own (see "Make it yours" in README.md).

---

## Step 1: Identify the person

If a name is not given, ask: **"Which team member should I generate slides for?"**

Map the name to their Linear email/handle using this table (fill it in with your own team):

| Name | Linear assignee value | In Review counts as done? |
|---|---|---|
| Jordan Lee (Head of Marketing) | `jordan@example.com` | No |
| Alex Morgan (Product Marketing) | `alex@example.com` | No |
| Sam Rivera (Design) | `Sam Rivera` | **Yes** |
| Casey Kim (Partnerships) | `casey@example.com` | No |

Linear accepts either an email or a display name as the assignee value.

---

## Step 2: Determine the week

If the user says "this week", use the current date to infer the Monday to Friday range.
If they give explicit dates (e.g. "June 22 to 26"), use those.
Format as: `Week of [Month D to D, YYYY]`

---

## Step 3: Pull Linear data

Use `Linear:list_issues` twice:

**Done this week:** strictly completed tasks only:
```
assignee: <resolved value>
updatedAt: -P7D
limit: 50
```

Filter client-side, with strict rules:

✅ Include in Done bullets:
- `status == "Done"` AND `completedAt` falls within the week range

✅ Include in Blocked section (not Done bullets):
- `status == "Blocked"`

❌ Exclude from Done, no exceptions:
- `In Progress`: not done
- `In Review`: not done (still awaiting approval/feedback)
- `Todo`, `Backlog`, `Cancelled`: not done

**Exception: "In Review counts as done" people only.** Some roles (for example a designer whose workflow ends at In Review and never moves to "Done") are marked **Yes** in the table above. For those people only, include `In Review` items as done, prefixed with `[In review]`.

**Curation: pick 3 to 5 bullets maximum.**
After filtering, choose the most significant items. Prefer:
1. Items belonging to a project over standalone issues
2. Higher priority (`Urgent` > `High` > `Medium`)
3. Visible output (launched page, sent email, published content) over internal/admin tasks

If there are more than 5 qualifying done items, group related sub-tasks under one parent bullet with sub-bullets rather than listing each separately.

---

**Next week:** what's genuinely planned:
```
assignee: <resolved value>
limit: 50
```

✅ Include:
- `In Progress` items (actively being worked on)
- `Todo` with a `dueDate` within the next 7 days
- `Backlog` with a `dueDate` within the next 7 days

❌ Exclude:
- `Backlog` items with no due date (not committed)
- `Done`, `Cancelled`, `In Review` items

**Curation: pick 3 to 5 bullets maximum.**
Sort by: `dueDate` soonest first, then `priority` (Urgent > High), then recency of activity.

---

## Step 4: Generate the slides

Run the Node.js generator script below via `bash_tool`.

### Setup check
```bash
cd weekly-meeting
ls node_modules/pptxgenjs 2>/dev/null || npm install pptxgenjs lucide-static
```

If `weekly-meeting/` doesn't exist:
```bash
mkdir -p weekly-meeting
cp -r <this-skill-folder>/assets weekly-meeting/
cd weekly-meeting && npm init -y && npm install pptxgenjs lucide-static
```

### Write and run the generator

Write a file `weekly-meeting/generate-person-slides.js` using the template below,
substituting `PERSON` and `WEEK_LABEL` with the real values pulled from Linear.

Then run:
```bash
cd weekly-meeting && node generate-person-slides.js
```

For a full-team deck (cover slide, two slides per person, closing slide), use `generator-template.js` in this skill folder instead: copy it into `weekly-meeting/`, replace its `TEAM` array with real data for each person, and run it the same way.

---

## Generator template

```javascript
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

// ── Colors (placeholder palette, replace with your brand) ─────────────────
// TEAL pill on Done slide, ACCENT text/links/arrows, TINT backgrounds,
// PHB/PHI screenshot placeholder border/icon, FYI_* the FYI panel.
const TEAL='5CCFC0', ACCENT='5B8DEF', TINT='E8F0FD', PHB='B9CEF5', PHI='8FB0F2';
const FYI_BG='F6F9FF', FYI_BORDER='DCE7FC', FYI_HINT='B7C9EC';

// ── Layout constants ───────────────────────────────────────────────────────
const M=0.55, MT=0.55, PILL_H=0.40, TITLE_Y=MT+PILL_H+0.30, BODY_Y=TITLE_Y+1.10;
const ICON_Y=7.5-0.55-0.28, CONTENT_W=13.33-M*2;
const COL_R_X=7.5, COL_R_W=13.33-COL_R_X-M, COL_L_W=COL_R_X-M-0.4;
const NW_FYI_X=9.2, NW_FYI_W=13.33-NW_FYI_X-M;
const ICON_BLACK=path.join(ASSETS,'icon-black.svg');
const LOGO_BLACK=path.join(ASSETS,'logo-black.svg');

// ── REPLACE THESE WITH REAL DATA ──────────────────────────────────────────
const WEEK_LABEL = '__WEEK_LABEL__';   // e.g. 'Week of June 22 to 26, 2026'

const PERSON = {
  name: '__NAME__',          // e.g. 'Alex Morgan'
  role: '__ROLE__',          // e.g. 'Product Marketing'
  area: '__AREA__',          // e.g. 'PMM & Launches'
  done: [
    // { text: 'Task title', url: '<LINEAR_ISSUE_URL>' }
    // Optional: subbullets: [{ text: 'Sub-task', url: '<LINEAR_ISSUE_URL>' }]
    // For in-review items (only for "In Review counts as done" people) prefix text with '[In review] '
    // Blocked items go in the blocked array below
  ],
  blocked: [
    // { text: 'Blocked task', url: '<LINEAR_ISSUE_URL>' }
  ],
  next: [
    // { text: 'Upcoming task', url: '<LINEAR_ISSUE_URL>' }
  ],
};
// ── END DATA ──────────────────────────────────────────────────────────────

// Helpers
function addIcon(s){const sz=0.28;s.addImage({path:ICON_BLACK,x:13.33-M-sz,y:ICON_Y,w:sz,h:sz});}
function addPill(s,label,bg=TEAL,tc='1A1A1A'){const t=label.toUpperCase(),w=Math.max(1.5,t.length*0.105+0.6);s.addShape('roundRect',{x:M,y:MT,w,h:PILL_H,fill:{color:bg},line:{type:'none'},rectRadius:0.2});s.addText(t,{x:M,y:MT,w,h:PILL_H,fontFace:'Inter',fontSize:12,bold:true,color:tc,align:'center',valign:'middle',charSpacing:0.5});}
function lucide(s,name,opts={}){const{x,y,w=0.28,h=0.28,color=ACCENT,strokeWidth=2}=opts,src=path.join(LUCIDE_DIR,`${name}.svg`);if(!fs.existsSync(src))return;let svg=fs.readFileSync(src,'utf8').replace(/stroke="currentColor"/g,`stroke="#${color}"`).replace(/stroke-width="2"/g,`stroke-width="${strokeWidth}"`);const k=`${name}-${color}`.replace(/[^a-z0-9]/gi,'_'),tmp=path.join(TMP_ICON_DIR,`${k}.svg`);fs.writeFileSync(tmp,svg);s.addImage({path:tmp,x,y,w,h});}
function header(s,p,cw=COL_L_W){s.addText(p.name,{x:M,y:TITLE_Y,w:cw,h:0.65,fontFace:'Inter',fontSize:26,bold:true,color:'1A1A1A',valign:'top'});s.addText(`${p.role}  ·  ${p.area}`,{x:M,y:TITLE_Y+0.65,w:cw,h:0.28,fontFace:'Inter',fontSize:12,color:ACCENT,valign:'top'});}
function ph(s,x,y,w,h,lbl){s.addShape('rect',{x,y,w,h,fill:{color:TINT},line:{color:PHB,pt:1.5,dashType:'dash'}});const is=0.38,ix=x+(w-is)/2,iy=y+h/2-0.46;s.addShape('rect',{x:ix,y:iy,w:is,h:is*0.75,fill:{type:'none'},line:{color:PHI,pt:1.5},rectRadius:0.04});s.addShape('ellipse',{x:ix+is*0.3,y:iy+is*0.12,w:is*0.38,h:is*0.38,fill:{type:'none'},line:{color:PHI,pt:1.5}});s.addText(lbl,{x,y:y+h/2+0.05,w,h:0.34,fontFace:'Inter',fontSize:10,color:PHI,align:'center',valign:'top',italic:true});}
function twl(text,url,fs,tc,lc){const r=[{text,options:{fontFace:'Inter',fontSize:fs,color:tc,bold:false}}];if(url)r.push({text:' ↗',options:{fontFace:'Inter',fontSize:fs-2,color:lc,bold:false,hyperlink:{url}}});return r;}

function doneSlide(pptx,p){
  const s=pptx.addSlide();
  addPill(s,'Done this week');
  s.addText(WEEK_LABEL,{x:13.33-M-4.5,y:MT,w:4.5,h:PILL_H,fontFace:'Inter',fontSize:11,color:'AAAAAA',align:'right',valign:'middle'});
  header(s,p);
  s.addShape('rect',{x:COL_R_X-0.25,y:0,w:13.33-(COL_R_X-0.25),h:7.5,fill:{color:TINT},line:{type:'none'}});
  ph(s,COL_R_X+0.05,0.5,COL_R_W,3.05,'Screenshot / result #1');
  ph(s,COL_R_X+0.05,3.75,COL_R_W,3.3,'Screenshot / result #2');
  const RH=0.56,RG=0.22,SH=0.34,SG=0.10,SI=0.38;
  let y=BODY_Y+0.12;
  if(!p.done.length){s.addText('No completed issues this week. Please add manually.',{x:M,y,w:COL_L_W,h:0.5,fontFace:'Inter',fontSize:13,color:'BBBBBB',italic:true,valign:'top'});}
  p.done.forEach(item=>{
    lucide(s,'check-circle-2',{x:M,y:y+0.14,color:'20C997'});
    s.addText(twl(item.text,item.url,15,'1A1A1A',ACCENT),{x:M+0.40,y,w:COL_L_W-0.40,h:RH,valign:'middle',wrap:true});
    y+=RH+RG;
    (item.subbullets||[]).forEach(sub=>{s.addShape('rect',{x:M+SI+0.02,y:y+0.16,w:0.10,h:0.025,fill:{color:'BBBBBB'},line:{type:'none'}});s.addText(twl(sub.text,sub.url,12,'666666',ACCENT),{x:M+SI+0.20,y,w:COL_L_W-SI-0.12,h:SH,valign:'middle'});y+=SH+SG;});
    if(item.subbullets&&item.subbullets.length)y+=0.06;
  });
  if(p.blocked&&p.blocked.length){y+=0.14;const bw=1.05;s.addShape('roundRect',{x:M,y,w:bw,h:0.26,fill:{color:'FCEAEA'},line:{type:'none'},rectRadius:0.07});s.addText('BLOCKED',{x:M,y,w:bw,h:0.26,fontFace:'Inter',fontSize:9,bold:true,color:'D64545',align:'center',valign:'middle',charSpacing:1});y+=0.36;p.blocked.forEach(item=>{lucide(s,'alert-triangle',{x:M,y:y+0.10,color:'D64545'});s.addText(twl(item.text,item.url,13,'D64545','D64545'),{x:M+0.40,y,w:COL_L_W-0.40,h:SH+0.10,valign:'middle'});y+=SH+0.20;});}
  addIcon(s);
}

function nextSlide(pptx,p){
  const s=pptx.addSlide();
  addPill(s,'Next week',ACCENT,'FFFFFF');
  s.addText(WEEK_LABEL,{x:13.33-M-4.5,y:MT,w:4.5,h:PILL_H,fontFace:'Inter',fontSize:11,color:'AAAAAA',align:'right',valign:'middle'});
  header(s,p,CONTENT_W);
  const FYI_Y=BODY_Y+0.10,FYI_H=7.5-FYI_Y-0.55;
  s.addShape('roundRect',{x:NW_FYI_X-0.1,y:FYI_Y-0.1,w:NW_FYI_W+0.1,h:FYI_H,fill:{color:FYI_BG},line:{color:FYI_BORDER,pt:1},rectRadius:0.12});
  s.addShape('roundRect',{x:NW_FYI_X+0.18,y:FYI_Y+0.18,w:0.70,h:0.26,fill:{color:TINT},line:{type:'none'},rectRadius:0.07});
  s.addText('FYI',{x:NW_FYI_X+0.18,y:FYI_Y+0.18,w:0.70,h:0.26,fontFace:'Inter',fontSize:9,bold:true,color:ACCENT,align:'center',valign:'middle',charSpacing:1.5});
  s.addText('Add context, links or notes here…',{x:NW_FYI_X+0.18,y:FYI_Y+0.62,w:NW_FYI_W-0.28,h:FYI_H-0.82,fontFace:'Inter',fontSize:12,color:FYI_HINT,italic:true,valign:'top',wrap:true});
  const MRH=0.55,MRG=0.10;let y=FYI_Y;
  p.next.forEach(item=>{lucide(s,'arrow-right',{x:M,y:y+0.16,color:ACCENT});s.addText(twl(item.text,item.url,15,'1A1A1A',ACCENT),{x:M+0.40,y,w:NW_FYI_X-M-0.65,h:MRH,valign:'middle',wrap:true});y+=MRH+MRG;});
  if(!p.next.length)s.addText('No upcoming issues found. Please add manually.',{x:M,y,w:NW_FYI_X-M-0.65,h:0.4,fontFace:'Inter',fontSize:10,color:'CCCCCC',italic:true,valign:'top'});
  addIcon(s);
}

async function build(){
  const pptx=new PptxGenJS();
  pptx.layout='LAYOUT_WIDE';
  pptx.defineLayout({name:'LAYOUT_WIDE',width:13.33,height:7.5});
  doneSlide(pptx,PERSON);
  nextSlide(pptx,PERSON);
  const safeName = PERSON.name.toLowerCase().replace(/[^a-z0-9]/g,'-').replace(/-+/g,'-');
  const out=path.join(OUT_DIR,`weekly-slides-${safeName}.pptx`);
  await pptx.writeFile({fileName:out});
  console.log('✅ Written:', out);
}
build().catch(e=>{console.error(e);process.exit(1);});
```

---

## Step 5: Present the file

After the script runs successfully, call `present_files` with the output path printed by the script.

Then offer: *"Want me to run this for another team member, or update any of the data?"*

---

## Edge cases

| Situation | Handling |
|---|---|
| No done tasks found | Empty done slide with gray placeholder text |
| More than 5 done items | Pick the 3 to 5 most significant; group related sub-tasks under one parent bullet |
| In Progress items in done | Exclude: never show as done. Not done = not done. |
| In Review items (most people) | Exclude from Done slide: still in progress |
| "In Review counts as done" people | In Review = done for them only: prefix with `[In review]` |
| Next week > 5 items | Pick top 3 to 5 by due date, then priority |
| Next week has no due-dated items | Use top 3 In Progress items |
| Week label not specified | Infer from current date (Monday to Friday of current week) |
| Node/npm not installed | Install before generating: see setup check above |
| Assets missing | Copy `assets/` from this skill folder into `weekly-meeting/` |

---

## Output filename format

```
weekly-slides-[firstname-lastname].pptx
```
e.g. `weekly-slides-alex-morgan.pptx`, `weekly-slides-sam-rivera.pptx`
