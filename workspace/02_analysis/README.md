# 02_analysis

| Module | Job | Pipeline step (thinking.md) |
|---|---|---|
| `src/config.py` | Paths, base parameters, sensitivity ranges, scenarios | — |
| `src/load.py` | Raw → processed data | Step 3 data audit |
| `src/baseline.py` | Status-quo answer | Step 4 baseline |
| `src/optimize.py` | Decision model | Step 5 formulation |
| `src/evaluate.py` | $ value, NPV, payback, stakeholder scorecard | Steps 6 & 8 |
| `src/sensitivity.py` | Tornado, scenarios, break-even | Step 7 stress test |
| `src/run_all.py` | Runs everything, writes `03_results/key_numbers.json` | Step 9 package |

Notebooks in `notebooks/` are for exploration. Name them `01_eda.ipynb`, `02_baseline.ipynb`, and so on. Move anything that feeds the deck into `src/`.

```powershell
python src/run_all.py
```
