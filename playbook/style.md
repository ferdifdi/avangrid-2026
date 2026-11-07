# style.md: Visual and Writing Style Guide

> **Who reads this:** the AI coding assistant building `workspace/04_tool/web/` and anyone designing slides in `workspace/05_deck/`.
> **Goal:** modern, calm, classy, minimalist. It should feel like a premium energy-tech product, not a school project. Comfortable to read for 10 minutes. One "wow" moment per page, never ten.

---

## 1. Design principles

1. **One idea per screen.** Each section answers one question. If it needs two charts, it is two sections.
2. **Quiet base, loud accent.** Neutral background and text. Color is reserved for meaning (charging, exporting, savings, risk).
3. **Numbers are the hero.** Big, tabular, with units. Words support numbers, not the other way around.
4. **Whitespace is a feature.** Generous padding. Never fill a gap just because it exists.
5. **Motion explains.** Animate only things that move in reality (energy flow, vehicles, time). No decorative bouncing.
6. **Same look everywhere.** Website, deck, and charts share the same palette, fonts, and tone.

---

## 2. Color tokens

Define every color as a CSS variable on `:root`. Never hard-code hex values in components.

```css
:root {
  /* Neutrals */
  --bg:        #f7f6f2;   /* warm paper background */
  --surface:   #ffffff;   /* cards */
  --ink:       #111827;   /* primary text */
  --ink-2:     #4b5563;   /* secondary text */
  --ink-3:     #8a93a3;   /* captions, axis labels */
  --line:      #e7e4dc;   /* borders, gridlines */
  --night:     #0c1424;   /* hero, nav, dark panels */

  /* Brand accent (energy green) */
  --accent:    #0f9f6e;
  --accent-2:  #0b7a55;   /* hover / pressed */
  --accent-bg: #e3f6ee;   /* tinted backgrounds */

  /* Meaning colors (data) */
  --in:        #0ea371;   /* charging, import, gain */
  --out:       #f06a1d;   /* exporting, discharge, cost */
  --grid:      #2f6fe4;   /* utility, grid, neutral series */
  --warn:      #f5b301;   /* highlight, recommended, caution */
  --risk:      #d1574a;   /* downside, losses, failure */
  --alt:       #8b5cf6;   /* reserve / alternative series */
}
```

Dark mode (optional, if time allows):

```css
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #0b1020; --surface: #121a2c; --ink: #e8ecf3; --ink-2: #aab4c5;
    --ink-3: #7c879a; --line: #22304a;
  }
}
```

**Rules**
- Text contrast ≥ 4.5:1 against its background.
- Max 4 data colors in one chart. Gray (`--ink-3`) for "baseline" or "status quo".
- Green = good / in. Orange = out / cost. Red = risk only. Never use red and green as the only difference; add labels or patterns.
- Use the warm yellow `--warn` only to highlight the single recommended option (e.g., the recommended bar).

---

## 3. Typography

- **Display:** `Space Grotesk` 500/700 (headlines, big numbers).
- **Body:** `Inter` 400/500/600/700.
- Load from Google Fonts only. Fallback: `system-ui, -apple-system, Segoe UI, Roboto, sans-serif`.
- Numbers: `font-variant-numeric: tabular-nums`.

| Role | Size (desktop) | Size (mobile) | Weight | Line height |
|---|---|---|---|---|
| Hero H1 | clamp(38px, 6vw, 68px) | 38px | 700 | 1.1 |
| Section H2 | 36–40px | 28px | 700 | 1.15 |
| Card H3 | 18–21px | 18px | 700 | 1.2 |
| Lead text | 19px | 17px | 400 | 1.55 |
| Body | 15–16px | 15px | 400 | 1.55 |
| Caption / axis | 12–13px | 12px | 500 | 1.4 |
| Eyebrow label | 12px uppercase, letter-spacing .12em | same | 700 | 1 |
| KPI number | 26–56px display | 24–40px | 700 | 1 |

Max line length: 70 characters for paragraphs (`max-width: 720px`).

---

## 4. Spacing, layout, shape

- **Spacing scale:** 4, 8, 12, 16, 20, 24, 32, 40, 56, 88 px. Do not invent other values.
- **Container:** `max-width: 1180px`, side padding 28px desktop, **16px mobile**.
- **Sections:** 88px vertical padding desktop, 56px mobile. Separate with a 1px `--line` border.
- **Grid:** 12-column mental model; use 2-col (text + visual), 3-col (cards), 5-col (KPIs). Collapse to 1 column under 1000px.
- **Radius:** cards 16px, buttons and chips 999px (pill), inputs 10px.
- **Shadow (one only):** `0 1px 2px rgba(17,24,39,.04), 0 8px 24px rgba(17,24,39,.06)`.
- **No horizontal scroll** at 375px width. Test it.

---

## 5. Components

| Component | Spec |
|---|---|
| **Nav** | Sticky, dark `--night` with 92% opacity + blur. Brand left, pill links right. Active link = accent pill. Thin progress bar at bottom |
| **Hero** | Dark radial gradient, headline with one accent-colored phrase, one lead line, 4 stat chips, 2 buttons, one subtle looping animation |
| **Eyebrow** | Small dot + uppercase label above every H2 ("2 · The opportunity") |
| **Card** | White surface, 1px line, 16px radius, 22px padding, single shadow |
| **KPI tile** | Uppercase label (12px), big number (display), one-line context. Green number if good, orange if bad |
| **Main point / answer box** | Warm yellow tint `#fff8e1`, 4–5px left border `--warn`, bold first phrase. One or two sentences max |
| **Intent line** | Light blue tint box: "What this shows: …" above complex visuals |
| **Type tag** | Pill with emoji + type name, colored per analysis type (see §7) |
| **Buttons** | Primary = accent fill, dark text. Ghost = transparent with border. Dark = `--night`. Pill shape, 12×20 padding |
| **Sliders** | Native range with `accent-color`. Label left, live value right in accent color |
| **Checklist** | Large hit area (padding 8–10px), emoji icon + bold label, optional muted sub-label |
| **Details / "How we got this"** | Collapsed by default, small accent summary text |
| **Tables** | Uppercase small headers, 1px row lines, no zebra stripes, numbers right-aligned |

---

## 6. Charts (Chart.js 4.4.1)

- Set global defaults once (font Inter 12px, color `--ink-2`, gridlines `#ece9e0`, tooltip dark `#111827`, legend boxes 12px, `maintainAspectRatio: false`).
- **Title = question.** "Buy low, sell high?" not "Price vs power".
- **Under the chart: one-sentence answer** computed from data.
- Axis titles with units always ("$ per day", "MW", "State of charge %").
- Remove x-gridlines on bar charts. Keep y-gridlines light.
- Legend at bottom. Max 5 entries.
- Highlight the recommended option with `--warn`; everything else muted.
- Shade context bands (e.g., route hours, peak window) with 6–12% opacity fills.
- Heatmaps: HTML grid cells with opacity scaled to value; hover title shows exact value.
- Chart height: 260px standard, 320–400px for tall/tornado.
- Tornado: horizontal floating bars from base value; low = `--risk` 85%, high = `--in` 85%; sorted by range.
- Waterfall: floating bars; starting total `--grid`, decreases `--out`, increases `--in`, final `--warn`.

---

## 7. Analysis type tags

| Tag | Emoji | Background | Text |
|---|---|---|---|
| Energy optimization | ⚡ | `#dcf5ea` | `#087a54` |
| Mathematical modeling | 📐 | `#e7effd` | `#1d4fb0` |
| Forecasting | 🔮 | `#e6f6fb` | `#0e6f8a` |
| Cost-benefit | 💰 | `#fff1c2` | `#8a6200` |
| Risk / scenarios | 🎲 | `#fbe3e1` | `#a2352a` |
| Incentive / policy design | 🎁 | `#fde6d8` | `#b4480d` |
| Stakeholder analysis | 👥 | `#efe7ff` | `#6233c7` |
| Validation | ✅ | `#eef0f4` | `#374151` |

---

## 8. Motion

- Durations: 200ms (hover), 450ms (chart update), 700ms (scroll reveal).
- Easing: `ease` or `cubic-bezier(.2,.7,.2,1)`.
- Scroll reveal: fade + 24px rise, once per element, via `IntersectionObserver`.
- Energy flow: animated `stroke-dashoffset` on SVG paths; direction = flow direction; width ∝ magnitude.
- Respect `prefers-reduced-motion: reduce`: disable loops and reveals.
- The page must look complete with animations off (screenshots, thumbnails, print).

---

## 9. Writing style (on screen and on slides)

- **Short.** One idea per sentence, about 12–20 words. Titles ≤ 8 words.
- **Plain words.** "Depot wire limit", not "interconnection capacity constraint". Explain any needed term once.
- **Findings, not descriptions.** "Peak drops 2.4 MW" beats "This chart shows the feeder load".
- **Numbers with units and comparison.** "$151k saved per year vs plug-in charging."
- **Active voice, present tense.**
- Emoji: only as icons in tags, checklists, and captions. Max one per line.
- No walls of text. If a paragraph exceeds 3 lines, split it or move it to "How we got this".

---

## 10. Accessibility and quality

- Every interactive control has a label; SVG scenes have `role="img"` and `aria-label`.
- Focus states visible (don't remove outlines).
- Hit targets ≥ 40px on mobile.
- Color is never the only signal; pair with text or icons.
- All external scripts from cdnjs with exact versions (Chart.js 4.4.1, KaTeX 0.16.9).

---

## 11. Slides (PowerPoint) alignment

- Same palette and fonts (install Inter and Space Grotesk, or fall back to Segoe UI).
- 16:9, white or `--bg` background, dark `--night` only for title and section dividers.
- Slide title = the takeaway sentence ("V2G cuts the evening peak by 2.4 MW").
- One chart or one diagram per slide. Export charts from the website or Python at 2× resolution into `05_deck/assets/`.
- Bottom-left footer: team name; bottom-right: slide number.

---

## 12. Do and don't

| Do | Don't |
|---|---|
| One accent color, used with intent | Rainbow charts |
| Big numbers with small labels | Tiny numbers buried in paragraphs |
| Question titles + answer sentences | Generic titles like "Results" |
| Collapse methods behind "How we got this" | Show every assumption upfront |
| Real system animation (flows, vehicles) | Decorative particle effects |
| Consistent spacing scale | Random margins |
| Test at 375px and in headless screenshots | Ship without looking |
