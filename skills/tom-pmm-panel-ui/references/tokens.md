# App tokens

Every color in a mockup comes from this file. `render_screen.py` reads it: any hex code that appears here counts as a valid token, and any hex code that doesn't is reported as an ERROR. Replace these placeholder values with your product's real tokens, measured from the live app.

## Color

### Surfaces

| Token | Hex | Use |
|---|---|---|
| `--canvas` | `#F1F2F5` | Behind the floating shell cards |
| `--surface` | `#F8F8FA` | Content area inside the shell |
| `--card` | `#FFFFFF` | Blocks on top of the surface |
| `--muted` | `#E2E3E9` | Quiet fills: secondary buttons, disabled controls |

### Text

| Token | Hex | Use |
|---|---|---|
| `--ink` | `#1A1A2E` | Default text and headings |
| `--ink-2` | `#44475A` | Secondary text |
| `--ink-3` | `#6B6E7B` | Muted text. Only on white or `--surface`, never on `--muted` |

### Brand and interactive

| Token | Hex | Use |
|---|---|---|
| `--primary` | `#2F6FEB` | The one primary action per view, focus rings, links |
| `--primary-hover` | `#1F5AD6` | Primary hover. A solid shade, never an opacity |
| `--primary-strong` | `#1A48A8` | Active item in the main navigation |
| `--primary-tint` | `#E8F0FD` | Selected rows, soft highlights |

### Borders

| Token | Hex | Use |
|---|---|---|
| `--border` | `#D0D2DA` | Default border on content boxes |

### Status

| Token | Hex | Use |
|---|---|---|
| `--success` | `#3B8C82` | Success text |
| `--success-tint` | `#C9EFEA` | Success pill background |
| `--warning` | `#D4602F` | Warning text |
| `--warning-tint` | `#FAC3B1` | Warning pill background |
| `--error` | `#C8414F` | Error text, destructive actions |
| `--error-tint` | `#FCE4E6` | Error pill background |

## Typography

Inter, bundled in `assets/vendor/fonts` so renders work offline.

| Preset | Size / weight / line height | Use |
|---|---|---|
| Page title | 20 / 600 / 28 | `SectionHeader` title |
| Section title | 16 / 600 / 24 | Card and settings section titles |
| Body | 14 / 400 / 20 | Default |
| Label | 14 / 500 / 20 | Buttons, form labels |
| Small | 12 / 500 / 16 | Meta rows, pills |

Nothing below 10px.

## Sizes

- Controls: 40px high. 30px only for pills and compact tiles.
- Radius: 12px on shell cards, 6px on content boxes and controls, full pill on status tags.
- Shadows: only on floating elements (shell cards, menus, popovers, dialogs, toasts). Cards on the surface are flat with a border.
- Spacing: an 8px grid. 24px inside cards, 32px between sections.
