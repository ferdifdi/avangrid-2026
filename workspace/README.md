# workspace/: Where the Work Happens

Team D4G Cornell 1 · Avangrid 2026 Energy Innovation Hackathon · Nov 12–13, 2026

This folder becomes our **GitHub repository** (the required "code or analytical tool" deliverable). Keep it clean and runnable.

## Tree

```
workspace/
├── README.md                  ← this file (becomes the repo front page; rewrite on Nov 13)
├── .gitignore
├── 00_brief/                  ← understand the problem (fill first)
│   ├── challenge.md           official prompt + our decision sentence + scope
│   ├── rubric.md              detailed rubric from kickoff + how we hit each item
│   ├── data_audit.md          what the data looks like, issues, joins
│   ├── assumptions.md         every assumption with source/reason (goes to appendix)
│   └── office_hours.md        questions to ask + answers received
├── 01_data/
│   ├── README.md              data dictionary
│   ├── raw/                   files exactly as received. NEVER edit. Not committed
│   ├── external/              public data we add (EIA, NREL, ISO). Cite source
│   └── processed/             cleaned, joined, analysis-ready data
├── 02_analysis/
│   ├── README.md              how to run, what each module does
│   ├── requirements.txt
│   ├── notebooks/             DROP .ipynb HERE. Markers in its README feed the website
│   │   ├── README.md          marker rules (## ANALYSIS | type | question, **Answer:**, # export)
│   │   └── 00_TEMPLATE.ipynb  copy this to start a notebook
│   └── src/                   the real pipeline (importable, reproducible)
│       ├── config.py          all parameters and paths in one place
│       ├── load.py            read raw → write processed
│       ├── baseline.py        status-quo / simplest answer
│       ├── optimize.py        the decision model
│       ├── evaluate.py        $ value, NPV, payback, stakeholder metrics
│       ├── sensitivity.py     tornado, scenarios, break-even
│       └── run_all.py         one command: everything → 03_results/
├── 03_results/
│   ├── key_numbers.json       SINGLE SOURCE OF TRUTH for deck + tool
│   ├── findings.md            one-sentence answer per analysis (type tag + number)
│   ├── figures/               PNG/SVG charts for the deck (2× resolution)
│   └── tables/                CSV outputs
├── 04_tool/
│   ├── README.md
│   ├── extract_notebooks.py   notebooks → web/data/analyses.json + chart images
│   └── web/                   interactive website (Story · Simulator · Analysis)
│       ├── css/style.css      base styles (from practice build; adjust tokens per style.md)
│       ├── js/common.js       shared chart defaults and helpers
│       └── data/              JSON copied from 03_results for the browser
├── 05_deck/
│   ├── outline.md             slide-by-slide draft (see playbook/deck.md)
│   └── assets/                images and exported charts for slides
└── 06_submission/
    └── checklist.md           final checks + what goes to SharePoint
```

## Flow

```
00_brief  →  01_data  →  02_analysis/src/run_all.py  →  03_results  →  04_tool + 05_deck  →  06_submission
 (think)     (clean)         (model + evaluate)           (numbers)        (show + tell)         (ship)
```

## Run

```powershell
cd workspace/02_analysis
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/run_all.py
cd ..; python 04_tool/extract_notebooks.py
```

## Rules

1. `01_data/raw/` is read-only and never committed (Avangrid data may be confidential).
2. Every number in the deck or tool comes from `03_results/key_numbers.json`.
3. Notebooks hold the analyses and feed the website through `04_tool/extract_notebooks.py`. Headline numbers that the deck uses must also come out of `run_all.py` or an `# export-key` cell.
4. Every assumption goes in `00_brief/assumptions.md`.
5. Keep the GitHub repo **private** unless Avangrid allows public data.
