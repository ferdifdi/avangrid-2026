# Data Dictionary

| Folder | Rule |
|---|---|
| `raw/` | Exactly as received from Avangrid. Read-only. Not committed to git |
| `external/` | Public data we add. Record the URL and download date below |
| `processed/` | Output of `02_analysis/src/load.py`. Safe to regenerate |

## Files

| File | Folder | Source | Grain | Key columns (unit) | Notes |
|---|---|---|---|---|---|
| [ ] | raw | Avangrid | [ ] | [ ] | [ ] |

## External sources (cite on appendix slide)

| Source | URL | Downloaded | Used for |
|---|---|---|---|
| [ e.g. EIA wholesale prices ] | [ ] | [ ] | [ ] |

## Conventions

- Timestamps: ISO 8601, one timezone for everything: [ America/New_York or UTC ]
- Energy in MWh, power in MW, money in USD (nominal unless stated)
- Column names: `snake_case`
