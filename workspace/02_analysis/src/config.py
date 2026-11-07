"""All paths and parameters in one place. Edit values here, never inside model code."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # workspace/
DATA_RAW = ROOT / "01_data" / "raw"
DATA_EXT = ROOT / "01_data" / "external"
DATA_PROC = ROOT / "01_data" / "processed"
RESULTS = ROOT / "03_results"
FIGURES = RESULTS / "figures"
TABLES = RESULTS / "tables"
KEY_NUMBERS = RESULTS / "key_numbers.json"
WEB_DATA = ROOT / "04_tool" / "web" / "data"

# ---- Base-case parameters (log each one in 00_brief/assumptions.md) ----
PARAMS = {
    "discount_rate": 0.07,      # utility-style WACC, assumption
    "horizon_years": 10,
    "capex": 0.0,               # $ upfront cost of the recommended option
    # add challenge-specific parameters here
}

# ---- Sensitivity ranges: name -> (low, high) ----
SENSITIVITY = {
    "discount_rate": (0.05, 0.09),
    # "price_multiplier": (0.8, 1.2),
}

# ---- Scenarios: name -> parameter overrides ----
SCENARIOS = {
    "low": {},
    "base": {},
    "high": {},
}
