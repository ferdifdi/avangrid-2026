# thinking.md: How to Think About an Avangrid Hackathon Problem

> **Who reads this:** any AI coding assistant (and every teammate) working on our 2026 Avangrid Energy Innovation Hackathon submission.
> **Rule:** read this file fully before writing analysis code, slides, or website copy. When in doubt, come back to Section 3 (the winning formula) and Section 4 (the reasoning protocol).

---

## 0. The event in one box

| Item | Value |
|---|---|
| Event | Avangrid 2026 Energy Innovation Hackathon (with Data for Good in Policy at Cornell) |
| Team | D4G Cornell 1: Tika Diagnestya, Muhammad Farhan Fadhilah, Ferdi Fadillah |
| Theme | Grid modernization in the utility sector |
| Format | Virtual, 32 hours, teams of 3. Problem statement + dataset + rubric released at kickoff |
| Kickoff | Thu Nov 12, 2026, 9:00 AM ET |
| Office hours | Nov 12, 12:00–5:00 PM ET and Nov 13, 10:00 AM–3:00 PM ET |
| Deadline | **Fri Nov 13, 2026, 5:00 PM ET**, upload to team SharePoint folder `24_D4G Cornell 1` |
| Required deliverables | (1) PowerPoint deck, (2) code or analytical tool (Excel, GitHub repo, etc.) |
| Finalists | Top 5 notified Nov 18 by noon. Present live Nov 19, 1:00–4:00 PM ET |
| Prizes | $5,000 / $2,500 / $1,000. Winners present at Avangrid's Annual Innovation Forum |

### Judging weights (memorize these)

| Criterion | Weight | What it really means |
|---|---|---|
| **Solution & Business Value** | **40%** | A clear, defensible *decision* with dollars, MW, or risk attached. Would an Avangrid manager act on it Monday? |
| **Analytics & Modeling** | **35%** | Correct formulation, honest assumptions, validation, sensitivity, uncertainty |
| Presentation & Communication | 15% | One story. Simple words. Every chart has a takeaway |
| Innovation & Creativity | 10% | A fresh angle, a reusable tool, an interactive demo, a smart incentive or policy idea |

**75% of the score is "good decision + good model".** A pretty dashboard with a weak decision loses. A plain model with a sharp, quantified, risk-aware recommendation wins.

---

## 1. What Avangrid always tests

Every verified past challenge asks for a **business decision**, not a forecast.

| Year | Challenge | Decision asked | Core method | Winner and why they won |
|---|---|---|---|---|
| 2022 | EV charging placement | *Where* to build chargers, and how many, under a budget | Demand forecast + integer programming | **Yale SOM.** Narrowed to I‑95 in Maine and delivered a **repeatable planning process** Avangrid could reuse on other corridors, not a one-off site list |
| 2023 A | School bus V2G | *How* to operate the fleet: when to charge or discharge | Scheduling optimization + incentive design | **MIT TPP.** Analyzed **both the district's and the utility's perspective**, and designed V2G arrangements and **incentives that benefit both** |
| 2023 B | Wind farm repowering | *Whether* and when to upgrade an aging asset | NPV + scenario analysis | MIT 1st overall; Yale 2nd used **real market data** (congestion, curtailment) |
| 2024 | Third hackathon | Prompt not public | Unknown | A team of **MIT PhD students** won |
| 2025 | Renewable PPA recontracting | *What price* to accept in a 5-year PPA vs merchant | Forecast + Monte Carlo + valuation | Lesson in the guide: **risk-aware, explainable pricing beats a better RMSE** |

### Three patterns

1. **Every challenge is a decision.** Where to invest, how to operate, whether to upgrade, what price to accept.
2. **Forecasting is an input, not the answer.** Predicting demand is basic. Predicting demand *and then optimizing a decision under cost and capacity limits* is what wins.
3. **One pipeline fits them all:**

```
Data → Forecast → Optimization → Financial evaluation → Risk / scenarios → Recommendation
```

---

## 2. Why the winners won (the deeper reading)

| Winning trait | 2022 Yale | 2023 MIT | 2025 lesson | How we copy it |
|---|---|---|---|---|
| Narrow the scope to something solvable and real | I‑95 Maine only | One district, 100 buses | One asset, one market first | Pick one concrete slice of the dataset, solve it fully, then show it generalizes |
| Deliver a **reusable tool or process**, not a single answer | Repeatable planning method | Fleet optimization platform | Transparent valuation framework | Package the model as a tool: parameters in, decision out |
| Multi-stakeholder view | — | District + utility + parents | Company risk tolerance | Always show who wins, who pays, and how to align them |
| Use real or realistic data and constraints | NREL tools, traffic data | Routes, chargers, tariffs | ERCOT/MISO/CAISO data, basis, negative prices | Respect physical and market constraints; cite public data sources |
| Quantify uncertainty | — | Price and fleet scenarios | Monte Carlo, P50/P90 | Scenarios + sensitivity (tornado) + downside case |
| Translate to money and policy | Budget-constrained ROI | Incentive structure | Recommended contract price | End with one number and one action |

---

## 3. The winning formula (our north star)

A winning submission answers these 7 questions, in this order, in plain words:

1. **Decision.** What exactly must Avangrid decide? (one sentence, starts with a verb: *invest, operate, upgrade, price, prioritize*)
2. **Stakes.** Why does it matter in $, MW, customers, reliability, or emissions?
3. **Model.** What are the decision variables, objective, and constraints?
4. **Answer.** What does the model recommend? (a number, a ranked list, a schedule, a price)
5. **Value.** How much better is it than the status quo, and for whom?
6. **Risk.** How sure are we? What breaks it? (scenarios, sensitivity, downside)
7. **Action.** What should Avangrid do Monday, and how does the tool keep working after us?

> If a slide, chart, or web section does not serve one of these 7 questions, cut it.

### The scoring map

| Rubric item | Our evidence |
|---|---|
| Solution & Business Value (40%) | Recommendation with $ / MW, NPV or payback, stakeholder scorecard, implementation roadmap, incentive or policy proposal |
| Analytics & Modeling (35%) | Formulation slide, baseline vs optimized comparison, validation/backtest, sensitivity tornado, scenarios or Monte Carlo, assumptions log |
| Presentation (15%) | 10-slide story, one takeaway per slide, consistent numbers from `key_numbers.json`, live demo under 60 seconds |
| Innovation (10%) | Interactive tool (web simulator), novel framing (e.g., incentive design, risk-adjusted price), reusable for other assets |

---

## 4. Reasoning protocol for the AI assistant

When a new problem statement arrives, think in this exact order. Write each step into `workspace/00_brief/` before coding.

### Step 1: Reframe the prompt as a decision
- Rewrite the problem as: *"Avangrid must decide ___ subject to ___ in order to ___."*
- Identify the decision type:

| Type | Typical method | Past example |
|---|---|---|
| Where / how many (allocation, siting) | Integer or linear programming | 2022 EV chargers |
| When / how much (operations, scheduling) | LP, MILP, dynamic programming | 2023 V2G |
| Whether / when (investment) | NPV, real options, scenarios | 2023 repowering |
| What price (contracting) | Forecast + Monte Carlo + certainty equivalent | 2025 PPA |
| Which first (prioritization) | Risk scoring, cost-benefit ranking, knapsack | Likely 2026 candidate |

### Step 2: Map the stakeholders
- Who pays, who benefits, who carries risk, who must never be hurt (hard constraint)?
- Typical: Avangrid utility, ratepayers/customers, regulators (PUC), asset owners, communities, environment.

### Step 3: Audit the data in 30 minutes
- What is the grain (hourly, daily, per asset, per feeder)? Timezones? Units (kW vs MW, kWh vs MWh)?
- Missing values, outliers, duplicates? Never join hourly prices to daily data.
- Log every assumption in `00_brief/assumptions.md` with a source or reason.

### Step 4: Build the baseline first
- The simplest model that answers the decision (status quo, rule of thumb, seasonal average).
- Every fancy model must **beat the baseline** in validation, or we keep the baseline.

### Step 5: Formulate the decision model
Write it before coding:
- **Decision variables** (what we choose)
- **Objective** (what we maximize or minimize; usually $ or MW or risk-adjusted value)
- **Constraints** (physical, operational, budget, regulatory, stakeholder hard limits)
- **Uncertain inputs** (prices, demand, weather, failures)
- **Output** (the recommendation format)

### Step 6: Value it in money
- Convert to annual $, NPV, payback, $/MW, $/customer, or cost per outage-minute avoided.
- Compare at least three options: **do nothing**, **simple fix**, **our optimized plan**.

### Step 7: Stress it
- Sensitivity (one-at-a-time tornado) on the 6–10 most uncertain inputs.
- Scenarios (low / base / high) or Monte Carlo with correlated inputs.
- Report the downside (P90 or worst case), not only the average.
- Find the **break-even**: the input value where the decision flips.

### Step 8: Design the deal or policy
- Who must change behavior? What incentive, tariff, contract, or program makes everyone better off?
- Recommend the **smallest** incentive that achieves the goal; more is a pure transfer.

### Step 9: Package as a reusable tool
- Parameters in, recommendation out. Runs end to end with one command (`python src/run_all.py`).
- Interactive front end (our web simulator) for judges to play with.

### Step 10: Tell it as a story
- Follow `deck.md`. Every chart has a one-sentence takeaway written as a finding, not a description.

---

## 5. Likely 2026 topics (theme: grid modernization) and starter formulations

The prompt is unknown until Nov 12. Prepare mental templates for these:

| Possible topic | Decision | Starter model | Key value metric |
|---|---|---|---|
| Non-wires alternatives / upgrade deferral | Upgrade a substation or deploy batteries/DR instead? | NPV comparison + peak-shaving optimization | Deferral value $, NPV |
| Asset replacement prioritization (transformers, poles, cables) | Which assets to replace first under a budget? | Failure-risk model × consequence → knapsack | Risk reduced per $ |
| DER hosting capacity | How much solar/EV can each feeder take? Where to upgrade? | Power-flow proxy + constraint screening + LP | MW unlocked per $ |
| Battery storage siting and dispatch | Where to place storage and how to run it? | MILP siting + dispatch (like V2G) | Arbitrage + capacity + reliability $ |
| EV / data-center load growth | How much new load is coming, where, and how to serve it? | Load forecast + scenario + capacity planning | Unserved load avoided, capex timing |
| Outage and resilience (storms, vegetation) | Where to harden or trim first? | Outage prediction + cost-benefit ranking | Customer-minutes avoided per $ (SAIDI/SAIFI) |
| Demand response / time-of-use design | What price or incentive cuts the peak most fairly? | Price elasticity + optimization + equity check | Peak MW cut, bill impact by group |
| Grid-edge forecasting (AMI smart-meter data) | Use meter data to detect overloads or theft? | Anomaly detection + action ranking | Losses avoided $ |
| Interconnection queue | Which projects to approve or study first? | Scoring + constraint screening | MW connected per study-month |

For any of these, Sections 3 and 4 apply unchanged.

---

## 6. Anti-patterns that lose points

- Building a forecast and stopping there ("here is our RMSE").
- No baseline, so no way to show value.
- Recommending something that breaks a hard constraint (reliability, safety, regulation).
- Ignoring who pays and who benefits.
- One deterministic answer with no uncertainty.
- Numbers that differ between deck, tool, and code. Use `03_results/key_numbers.json` as the single source of truth.
- Jargon on slides. Long paragraphs. Charts without takeaways.
- Overbuilding the website while the model is unfinished. **Model first, story second, polish last.**
- Silent assumptions. Every assumption goes in `assumptions.md` and on an appendix slide.

---

## 7. Quality bar before submission

- [ ] The decision is stated in one sentence on slide 2.
- [ ] Baseline vs recommended plan, with $ and MW (or the relevant unit).
- [ ] Formulation shown: variables, objective, constraints.
- [ ] Validation or backtest: does the model reproduce history?
- [ ] Sensitivity tornado + at least 3 scenarios + downside number.
- [ ] Stakeholder scorecard: who wins, who pays.
- [ ] Incentive, policy, or implementation roadmap.
- [ ] Tool runs end to end from a clean clone in one command.
- [ ] All numbers in deck = numbers in tool = `key_numbers.json`.
- [ ] Limitations slide: what we did not model and why it is OK.

---

## 8. Judge Q&A prep (finalist round)

Prepare a 20-second answer for each:

1. What is the single decision you recommend, and what is it worth?
2. What is your biggest assumption, and what happens if it is wrong?
3. How did you validate the model?
4. Why this method and not a simpler one?
5. Who loses under your plan, and how do you compensate them?
6. How would Avangrid use this tool next month on a different asset or region?
7. What regulatory or tariff barrier could block this?
8. What would you do with one more week?

---

## 9. Formula sheet (from past challenges)

```
EV demand:        D_i = Traffic_i × EVShare_i × ChargingRate_i ;  Chargers_i = ceil(D_i / SessionsPerCharger)
Battery SOC:      E_{t+1} = E_t + η_c c_t − d_t/η_d − e_t(drive)
Generation:       G = MW × 8760 × CapacityFactor
NPV:              NPV = −C0 + ΔCF × (1 − (1+r)^−T) / r
Capture price:    P_capture = Σ G_t P_t / Σ G_t
Covariance:       E[GP] = E[G]E[P] + Cov(G,P)
Basis:            R_t = G_t (P_hub,t + Basis_t)
PPA price:        P_PPA = (E[R] − RiskPremium) / E[Generation]
Merchant-equiv:   P_me = Σ d_t E[G_t P_t] / Σ d_t E[G_t]
Payback:          years = Capex / Annual net benefit
```

---

## 10. Our practice reference

The 2023 V2G practice build lives in `../practice/`, live at https://bus-to-grid.vercel.app. It shows the full pattern: story page, interactive simulator, and an analysis page grouped by five lenses (energy optimization, mathematical modeling, cost-benefit, incentive design, stakeholder analysis). Reuse its structure; replace its content.
