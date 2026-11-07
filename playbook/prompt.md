# prompt.md: Master Prompt for the AI Assistant

> **How to use**
> 1. On Nov 12 after kickoff, fill every `[ ___ ]` in **Part A**. Delete the hint text in *italics* after filling. Keep the ✅ V2G example lines only as guidance; remove them before sending.
> 2. Paste Part A + Part B into the AI assistant together, plus this line:
>    *"Before starting, read `playbook/thinking.md` and `playbook/style.md`. Work only inside `workspace/`."*
> 3. Re-send Part A whenever the analysis changes so the AI stays in sync.
>
> Blanks marked **(R)** are required on day 1. Others can be filled as work progresses.

---

# PART A: The Material (what we are solving and what we found)

## A1. Challenge

- **Challenge title (R):** [ ___ ]
  - ✅ *Example: School bus electrification and vehicle-to-grid (V2G)*
- **Problem statement in Avangrid's words (R):** [ paste the official prompt ]
- **The decision, in one sentence (R):** "Avangrid must decide [ ___ ] subject to [ ___ ] in order to [ ___ ]."
  - ✅ *Avangrid must decide when 100 school buses charge and discharge, subject to every route being covered, in order to cut costs and the evening peak.*
- **Decision type (R):** [ where-to-invest / how-to-operate / whether-to-upgrade / what-price / which-first ]
- **Scope we chose (R):** [ region, asset, time window, subset of data ]
  - *Narrow it. Yale won 2022 by focusing only on I-95 in Maine.*
- **Why it matters (stakes):** [ $ at risk, MW, customers, reliability, emissions ]

## A2. Stakeholders

| Stakeholder | What they want | How we measure it | Hard limit (never break) |
|---|---|---|---|
| [ e.g. Avangrid utility ] | [ ___ ] | [ ___ ] | [ ___ ] |
| [ e.g. customers / ratepayers ] | [ ___ ] | [ ___ ] | [ ___ ] |
| [ e.g. regulator / community ] | [ ___ ] | [ ___ ] | [ ___ ] |

✅ *District wants low bills ($/yr). Utility wants a lower peak (MW). Parents want 100% routes covered (hard limit).*

## A3. Data

| Dataset | Source | Grain (hourly/daily/asset) | Rows × cols | Key fields | Issues found |
|---|---|---|---|---|---|
| [ provided dataset 1 ] | Avangrid | [ ___ ] | [ ___ ] | [ ___ ] | [ missing, timezone, units ] |
| [ public data, e.g. EIA, NREL, NYISO, ISO-NE ] | [ URL ] | [ ___ ] | [ ___ ] | [ ___ ] | [ ___ ] |

- **Data files live in:** `workspace/01_data/raw/` (never edit), cleaned in `01_data/processed/`.
- **Key assumptions (R):** list in `workspace/00_brief/assumptions.md`, then summarize here: [ ___ ]

## A4. Model formulation (R)

- **Decision variables:** [ ___ ]  ✅ *c_t charge, d_t discharge per bus per hour*
- **Objective:** [ maximize / minimize ___ ]  ✅ *max Σ price × (d − c) − wear cost*
- **Constraints:**
  1. [ physical ___ ]  ✅ *battery between 20% and 100%*
  2. [ operational ___ ]  ✅ *≥ 80% charge before every route*
  3. [ budget / regulatory ___ ]  ✅ *depot grid connection ≤ 1.5 MW*
- **Uncertain inputs:** [ prices, demand, weather, failures ___ ]
- **Method / solver:** [ LP / MILP / dynamic programming / Monte Carlo / ML forecast + optimization ]
- **Baseline to beat:** [ status quo rule ___ ]  ✅ *plug in and charge immediately*

## A5. Analyses (fill one row per analysis we actually ran)

Each analysis must have a **type tag**, a **question**, a **chart**, and a **one-sentence answer**.

| # | Type tag | Question (plain words) | Chart type | Answer (one sentence with a number) | Result file |
|---|---|---|---|---|---|
| 1 | ⚡ Energy optimization | [ When/where should ___ ? ] | [ heatmap ] | [ ___ ] | `03_results/figures/[ ]` |
| 2 | 📐 Mathematical modeling | [ Which inputs matter most? ] | [ tornado ] | [ ___ ] | [ ] |
| 3 | 🔮 Forecasting | [ How much ___ will there be? ] | [ line + band ] | [ ___ ] | [ ] |
| 4 | 💰 Cost-benefit | [ Is it worth it? NPV / payback ] | [ bars + KPIs ] | [ ___ ] | [ ] |
| 5 | 🎲 Risk / scenarios | [ How sure are we? P50/P90 ] | [ distribution / scenarios ] | [ ___ ] | [ ] |
| 6 | 🎁 Incentive / policy design | [ What should the utility pay or change? ] | [ sweep curve ] | [ ___ ] | [ ] |
| 7 | 👥 Stakeholder analysis | [ Who wins, who pays? ] | [ scorecard ] | [ ___ ] | [ ] |
| 8 | ✅ Validation | [ Does the model reproduce history? ] | [ backtest ] | [ ___ ] | [ ] |

*Delete rows that do not fit the challenge; add rows if needed. Keep 6–10.*

## A6. Key numbers (R, single source of truth)

All numbers come from `workspace/03_results/key_numbers.json`. Fill the headline ones here:

| Metric | Value | Unit | Compared with |
|---|---|---|---|
| Headline value | [ ___ ] | [ $/yr ] | [ baseline ] |
| Second metric (grid) | [ ___ ] | [ MW ] | [ ___ ] |
| NPV or payback | [ ___ ] | [ $ / years ] | [ ___ ] |
| Downside case | [ ___ ] | [ ___ ] | [ P90 / worst scenario ] |
| Break-even point | [ ___ ] | [ ___ ] | [ input where decision flips ] |

✅ *$151k/yr saved vs plug-in · 2.4 MW peak cut · charger payback 8.9 yr (2.8 yr with $0.10 bonus).*

## A7. Solution and recommendation (R)

- **Our recommendation in one sentence:** [ ___ ]
- **Product concept** (the reusable tool):
  - Inputs: [ ___ ]
  - Processing: [ ___ ]
  - Outputs: [ ___ ]
- **Incentive / policy / contract proposal:** [ ___ ]
- **Implementation roadmap:** Phase 1 [ pilot ___ ] → Phase 2 [ scale ___ ] → Phase 3 [ ___ ]
- **What makes us different (innovation):** [ ___ ]

## A8. Limitations and next steps

- Not modeled: [ ___ ] and why it is acceptable: [ ___ ]
- With more time we would: [ ___ ]

## A9. Tools

- Analysis: [ Python 3.11, pandas, NumPy, PuLP/Pyomo/OR-Tools, scikit-learn/LightGBM, statsmodels ]
- Tool / front end: static HTML + Chart.js (copy of `practice/` pattern), hosted on Vercel
- Deck: PowerPoint (required format)
- Repo: GitHub [ private? URL ___ ]

## A10. Story arc (one line each; this drives both deck and website)

1. Hook: [ ___ ]  ✅ *School buses that power the city while they wait.*
2. Problem: [ ___ ]
3. Opportunity: [ ___ ]
4. Reality check (constraints): [ ___ ]
5. Our model: [ ___ ]
6. Key findings: [ ___ ]
7. Recommendation + value: [ ___ ]
8. Lesson / call to action: [ ___ ]

---

# PART B: How to Build the Website (the interactive analytical tool)

> Paste Part A above this. Then give the AI these instructions.

## B0. Instructions to the AI

You are building the interactive companion tool for our hackathon submission.
- Read `playbook/thinking.md` (how to reason) and `playbook/style.md` (how it must look) first.
- Use the content in Part A as the **only** source of facts. Never invent numbers. Read numbers from `workspace/03_results/key_numbers.json` and model logic from `workspace/02_analysis/src/`.
- Build in `workspace/04_tool/web/`. Static HTML + CSS + vanilla JS + Chart.js 4.4.1 from cdnjs. No build step.
- Reuse the structure of `practice/` (story, simulator, analysis pages). `css/style.css` and `js/common.js` are already copied as a base.
- Simple language: short sentences, one idea per sentence, no jargon without a one-line explanation.
- Every chart gets: a question title, a one-line "what this shows", and a one-sentence answer computed from the data.

## B1. Site map

| Page | File | Job | Rubric it serves |
|---|---|---|---|
| Story | `index.html` | Explain problem → solution in 2 minutes of scrolling | Presentation, Business Value |
| Simulator | `simulator.html` | Let judges change inputs and watch the decision change live | Innovation, Modeling |
| Analysis | `analysis.html` | Show every analysis grouped by type tag with answers | Modeling, Business Value |
| Method (optional) | `method.html` | Formulation, data, assumptions, validation, limitations | Modeling |

Navigation: sticky top bar with brand + 3–4 links. Scroll progress bar on long pages.

## B2. Story page (`index.html`): sections in order

Follow A10. Each section = eyebrow label + title (≤ 8 words) + one lead sentence + one visual + one "Main point" box.

1. **Hero:** big headline, one sub-line, 4 stat chips from `key_numbers.json`, 2 buttons (See how / Play simulator), one small looping animation that represents the asset.
2. **Problem:** a simple visual (timeline strip, map, or diagram) + main point.
3. **Opportunity:** one chart showing the gap we exploit (price spread, risk, overload) + a mini table.
4. **Back-of-envelope value:** an interactive calculator with 4–5 sliders that reproduces the simple math.
5. **Reality check:** 4–6 constraint icon cards + a waterfall chart from theory to real value.
6. **The model:** 3 equations max (KaTeX), each with a plain-English line under it.
7. **Stakeholders:** 3 cards with a quote ("Lower my bills") and the metric each one wins by.
8. **Solution:** Inputs → Optimize → Outputs pipeline with animated connectors.
9. **Lesson / CTA:** one bold quote + buttons to Simulator and Analysis.

## B3. Simulator page (`simulator.html`)

- **Layout:** left control panel (sticky), right main area.
- **Controls (keep visible ≤ 6):** scenario buttons, 1–2 key sliders, on/off toggles, a constraint checklist. Everything else under a collapsible "⚙️ Advanced settings".
- **Animated scene (SVG):** a visual of the real system (assets, grid, flows). Elements move with simulated time. Flow lines change color by direction (green = in, orange = out) and width by size.
- **Time control:** play/pause, time slider, speed select. One-line caption that explains what is happening right now.
- **KPI row (5 tiles):** headline $, savings vs baseline, extra value of our strategy, grid metric, reliability check (must show ✅ 100% when hard constraints hold).
- **4 charts in a 2×2 grid**, each titled as a question with a one-line answer under it.
- **Model:** port the core model from `02_analysis/src/` to `js/model.js` so it runs in the browser in under 100 ms per run. If it is too heavy, precompute scenario grids into `data/*.json` and interpolate.
- **Infeasible inputs:** show a friendly alert explaining which constraint broke and how to fix it.

## B4. Analysis page (`analysis.html`)

- Header with type-tag chips that jump to each section.
- Top controls: base scenario + 1 global slider.
- **Key answers row:** one card per type tag, auto-written from results.
- Sections grouped by type tag (from A5). Each block: tag, question (h3), one muted line, chart (right), yellow **answer box** with the computed sentence, and a collapsed "How we got this" with the method.
- Answers must be computed from data, never hard-coded. If a claim depends on the data (e.g., "X wins for all"), check it in code and show an alternative sentence when false.

## B5. Data flow

```
02_analysis/notebooks/*.ipynb  (saved with outputs, using the markers)
   → python 04_tool/extract_notebooks.py
   → 04_tool/web/data/analyses.json   (every analysis: type, question, answer, method, figures, tables, data)
   → 04_tool/web/assets/nb/*.png|svg  (chart images from notebook outputs)
02_analysis/src/run_all.py
   → 03_results/key_numbers.json      (headline numbers, copied to web/data/)
04_tool/web/js/model.js               (browser port of the core model, same results ±1%)
```

- `analysis.html` must render its sections **from `data/analyses.json`** (fetch on load, group by `type`, one block per analysis). Use the notebook PNG as a fallback; when `data.<name>` exists, redraw it as an interactive Chart.js chart in the style of `style.md`.
- The yellow answer box uses `answer`; "How we got this" uses `method`; the muted line uses `what`.
- Headline numbers merge `key_numbers.json` with `analyses.json → key_numbers` (notebook values win only if `run_all` left them null).
- Pages that `fetch` JSON need a local server: `python -m http.server 8000` inside `web/`.

Add a quick check: the browser model and the Python model must agree on the base case. Print both in the console during development.

## B6. Quality checks before publishing

- Open every page headless (Chrome `--headless --dump-dom` and `--screenshot`) and confirm no console errors.
- Check at 375 px phone width: no horizontal scroll.
- All numbers match `key_numbers.json` and the deck.
- Every chart has axis titles with units and a takeaway sentence.
- Lighthouse-style sanity: images compressed, no unused libraries.

## B7. Deploy

```powershell
cd workspace/04_tool/web
vercel link --yes --project d4g-avangrid-2026
vercel deploy --prod --yes
```

Never deploy `01_data/raw` or anything marked confidential by Avangrid. Keep a `.vercelignore` with `*.docx`, `*.xlsx`, `*.csv` unless a file is meant to be public.

---

# PART C: Short prompts for later steps (copy as needed)

- **Data audit:** "Read `01_data/raw/`. Report grain, units, timezones, missing values, outliers, and join keys. Write findings to `00_brief/data_audit.md`. Do not modify raw files."
- **Baseline:** "Build the simplest baseline that answers the decision in A1. Save results to `03_results/tables/baseline.csv` and add headline numbers to `key_numbers.json`."
- **Optimization:** "Implement the formulation in A4 in `02_analysis/src/optimize.py`. Compare to the baseline. Report value in $ and in the grid metric."
- **Sensitivity:** "Run a one-at-a-time tornado on the 8 most uncertain inputs and 3 scenarios. Find the break-even input where the decision flips."
- **Deck:** "Using `playbook/deck.md`, Part A, and `key_numbers.json`, draft the 10-slide PowerPoint outline with one takeaway headline per slide."
- **Q&A drill:** "Act as an Avangrid judge. Ask the 8 questions in `thinking.md` Section 8 about our solution, then critique our answers."
