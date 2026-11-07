# gameplan.md: 32-Hour Plan and Roles

> Times are Eastern Time (ET). Deadline is **Fri Nov 13, 5:00 PM ET**. Upload by **4:30 PM** to leave a buffer.

## Before the event (Nov 9–11)

| When | Task | Owner |
|---|---|---|
| Nov 9 noon | Read the preparation materials; add notes to `workspace/00_brief/challenge.md` | All |
| Nov 9–10 | Test SharePoint folder `24_D4G Cornell 1` and Microsoft Teams access | All |
| Nov 10 noon | Confirm team roster is correct (deadline to report errors) | Ferdi |
| Nov 10–11 | Set up Python env (`pip install -r workspace/02_analysis/requirements.txt`), Vercel login, GitHub repo (private) | Ferdi |
| Nov 10–11 | Re-read `thinking.md`; practice the 2023 V2G and 2025 PPA examples | All |
| Nov 11 | Draft generic deck template in PowerPoint using `style.md` colors | Tika |

## Suggested roles

Adjust after kickoff based on the problem.

| Role | Owner (suggested) | Owns |
|---|---|---|
| **Modeling lead** | Farhan | Formulation, optimization, sensitivity, validation (`02_analysis/`) |
| **Data + business lead** | Tika | Data audit, assumptions, financials, stakeholder analysis, deck story (`00_brief/`, `05_deck/`) |
| **Tool + integration lead** | Ferdi | Pipeline, `key_numbers.json`, web tool, GitHub, submission (`04_tool/`, `06_submission/`) |

Everyone: office-hour questions, Q&A rehearsal.

## Day 1: Thu Nov 12

| Time | Milestone | Output |
|---|---|---|
| 9:00 | Kickoff. Capture challenge, dataset, rubric, submission rules | `00_brief/challenge.md`, `rubric.md` |
| 9:45 | **Decision sentence** agreed by all 3 (`thinking.md` Step 1) | Part A1 of `prompt.md` filled |
| 10:00 | Data audit (30–60 min). Scope chosen | `00_brief/data_audit.md` |
| 11:00 | Formulation on paper: variables, objective, constraints, baseline | Part A4 filled |
| 11:30 | Prepare 5 sharp office-hour questions | `00_brief/office_hours.md` |
| 12:00–1:00 | **Office hours**: validate decision framing, data meaning, what Avangrid values most | Notes |
| 1:00 | Baseline model running end to end | `03_results/key_numbers.json` v1 |
| 3:00 | Optimized model v1 beats baseline | Comparison table |
| 4:00 | Office hours round 2: show early results, ask about assumptions | Notes |
| 5:00 | **Checkpoint 1:** headline number exists. Story arc drafted (A10) | Deck skeleton |
| 5–9 PM | Sensitivity, scenarios, stakeholder + financial analysis | Figures in `03_results/figures/` |
| 9 PM | **Checkpoint 2:** all analyses have a one-sentence answer (A5) | Part A5–A7 filled |
| 9 PM–1 AM | Tool build starts (web or Excel). Deck draft v1 | `04_tool/`, `05_deck/` |
| 1 AM | Sleep in shifts. At least 5 hours each | — |

## Day 2: Fri Nov 13

| Time | Milestone | Output |
|---|---|---|
| 8:00 | Review overnight work. Fix the weakest analysis | — |
| 10:00–11:00 | Office hours: test the recommendation and the incentive or policy idea | Notes |
| 11:00 | **Model freeze.** No new analyses after this | Final `key_numbers.json` |
| 11:00–2:00 | Deck v2, tool polish, README for repo | — |
| 2:00 | **Content freeze.** Numbers checked across deck, tool, JSON | `06_submission/checklist.md` |
| 2:00–3:30 | Two timed rehearsals. Q&A drill (`thinking.md` §8) | — |
| 3:30 | Export PPTX + PDF, tag GitHub release, deploy tool | — |
| **4:30** | **Upload to SharePoint** and confirm files open | Done |
| 5:00 | Official deadline | — |

## Finalist round (if selected)

| When | Task |
|---|---|
| Nov 18 noon | Finalist notice |
| Nov 18 afternoon | Tighten deck to the time limit, add backup slides, 3 full rehearsals |
| Nov 19, 1–4 PM | Present. Live demo ≤ 60 s. Each speaker ready to answer any Q&A question |

## Golden rules

1. Decision first, model second, polish last.
2. Never be more than 2 hours away from a complete, submittable version.
3. One source of numbers: `key_numbers.json`.
4. Ask office hours what Avangrid would actually do with the answer.
5. Sleep matters more than one more chart.
