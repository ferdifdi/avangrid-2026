# 04_tool: Interactive Analytical Tool (website)

## How the website gets its content

```
02_analysis/notebooks/*.ipynb  ──extract_notebooks.py──►  web/data/analyses.json + web/assets/nb/*
02_analysis/src/run_all.py     ──────────────────────────►  web/data/key_numbers.json
web/js/model.js  (browser port of the core model, for the live simulator)
```

1. Teammates finish notebooks in `02_analysis/notebooks/` using the markers in its README.
2. Run all cells, save, then:
   ```powershell
   python workspace/04_tool/extract_notebooks.py
   python workspace/02_analysis/src/run_all.py
   ```
3. Ask the AI to build or refresh the pages using `playbook/prompt.md` Part B. The analysis page renders straight from `analyses.json`, so re-running the extractor updates the site without code changes.

## Pages to build in `web/`

| File | Content source |
|---|---|
| `index.html` Story | `playbook/prompt.md` Part A10 + `key_numbers.json` |
| `simulator.html` | `js/model.js` (port of `02_analysis/src/optimize.py`) |
| `analysis.html` | `data/analyses.json`, grouped by type tag |

`css/style.css` and `js/common.js` are copied from the practice build. Adjust the color tokens in `style.css` to match `playbook/style.md`.

## Preview and deploy

```powershell
cd workspace/04_tool/web
python -m http.server 8000      # open http://localhost:8000
vercel link --yes --project d4g-avangrid-2026
vercel deploy --prod --yes
```

Use the local server, not double-click, once pages load JSON with `fetch`. Browsers block `fetch` on `file://`.
