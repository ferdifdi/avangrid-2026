# notebooks/: Drop Folder for Analysis Notebooks

Put every `.ipynb` here. The website is built from them by running:

```powershell
python workspace/04_tool/extract_notebooks.py
```

The extractor reads each notebook (with its saved outputs) and writes:
- `04_tool/web/data/analyses.json`: every analysis block (type, question, answer, method, charts, tables, data)
- `04_tool/web/assets/nb/*.png|svg`: chart images from cell outputs

**Run all cells and save the notebook before extracting.** Outputs that are not saved cannot be extracted.

## Naming

`01_eda.ipynb`, `02_baseline.ipynb`, `03_optimization.ipynb`, `04_cost_benefit.ipynb`, ... Copy `00_TEMPLATE.ipynb` to start.

## Markers (the only rules to remember)

| Cell type | Starts with | Meaning |
|---|---|---|
| Markdown | `## ANALYSIS \| <type> \| <question>` | Starts a new analysis block |
| Markdown | `What this shows:` | One-line explanation under the chart title |
| Markdown | `**Answer:**` | The one-sentence finding (goes in the yellow answer box) |
| Markdown | `**Method:**` | Short method (goes in "How we got this") |
| Code | `# export` | Charts, tables, and text outputs of this cell go to the website |
| Code | `# export-data: <name>` | Last output must be JSON (`print(json.dumps(obj))`). Saved as `data.<name>` for interactive charts |
| Code | `# export-key` | Last output must be JSON. Merged into `key_numbers` (headline numbers) |

`<type>` must be one of: `energy-optimization`, `modeling`, `forecasting`, `cost-benefit`, `risk`, `incentive`, `stakeholder`, `validation`.

## Example

```markdown
## ANALYSIS | cost-benefit | Does the charger pay for itself?
What this shows: yearly savings split by day type.
```

```python
# export
fig, ax = plt.subplots(); ax.bar(days, savings); ax.set_ylabel("$ per year")
```

```markdown
**Answer:** Pays back in 8.9 years, or 2.8 years with a $0.10/kWh utility bonus.
**Method:** 180 school days + 165 non-school days, 7% discount rate.
```

```python
# export-data: payback
print(json.dumps({"labels": days, "savings": savings}))
```

## Tips

- Use `plt.savefig` is not needed; inline outputs are extracted automatically.
- Tables: display a DataFrame (`df.head(10)`) in an `# export` cell; it becomes an HTML table.
- Keep each block to one chart and one answer. That maps 1:1 to a website section and a slide.
