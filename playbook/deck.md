# deck.md: PowerPoint Structure (required deliverable)

> The deck is **mandatory** and is what judges read first. The website is a bonus that supports it.
> Build the deck in `workspace/05_deck/`. Every number must come from `workspace/03_results/key_numbers.json`.
> Slide titles are **takeaway sentences**, not topics.

## Main deck: 10–12 slides (finalist talk ≈ 8–10 minutes)

| # | Slide | Title pattern (takeaway) | Content | Rubric served |
|---|---|---|---|---|
| 1 | Title | "[Product name]: [one-line promise]" | Team D4G Cornell 1, names, one hero visual | Presentation |
| 2 | The decision | "Avangrid must decide [X] to [Y]" | Problem in 3 bullets, stakes in $ / MW, decision sentence | Business Value |
| 3 | Our answer up front | "We recommend [X], worth [$ / MW]" | 3 headline KPIs + one-line recommendation | Business Value |
| 4 | Data and scope | "We used [N] datasets covering [scope]" | Data table, scope choice, key cleaning steps | Modeling |
| 5 | Model | "One model decides [every hour / every asset]" | Variables, objective, constraints (3 equations, plain-English lines) + pipeline diagram | Modeling |
| 6 | Baseline vs optimized | "[Optimized] beats [status quo] by [X]" | Main comparison chart | Modeling + Value |
| 7 | Key insight | "[Surprising finding]" | Heatmap / playbook chart | Modeling + Innovation |
| 8 | Risk and sensitivity | "The decision holds unless [break-even]" | Tornado + scenarios / P50–P90 | Modeling |
| 9 | Stakeholders and incentive | "[Deal] makes it win-win" | Scorecard + recommended incentive / policy | Business Value + Innovation |
| 10 | Financials | "Pays back in [N] years, NPV [$]" | Cost-benefit, payback, NPV | Business Value |
| 11 | Tool demo | "Avangrid can rerun this on any [asset]" | Screenshot / QR of web tool + GitHub link; 30–60 s live demo | Innovation + Presentation |
| 12 | Roadmap and ask | "Pilot [X] in [Q], scale by [Y]" | 3-phase roadmap, next steps, limitations in 2 bullets | Business Value |

## Appendix (backup for Q&A)

- A1 Assumptions table (from `00_brief/assumptions.md`)
- A2 Data audit and cleaning
- A3 Full formulation and solver details
- A4 Validation / backtest
- A5 Extra scenarios and sensitivities
- A6 Limitations and what we would do with more time
- A7 References (data sources, past winners, papers)

## Speaker split (3 people)

| Speaker | Slides | Focus |
|---|---|---|
| Speaker 1 | 1–3, 12 | Story, decision, recommendation, roadmap |
| Speaker 2 | 4–8 | Data, model, findings, risk |
| Speaker 3 | 9–11 | Stakeholders, money, live demo |

## Rules

- One message per slide. ≤ 25 words of body text.
- Every chart: question in title, answer in subtitle, source in footer.
- Practice the full talk twice with a timer before Nov 13, 4:00 PM ET.
- Export the final file as `.pptx` and `.pdf` into `workspace/06_submission/`.
