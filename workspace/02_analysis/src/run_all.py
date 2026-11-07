"""One command to reproduce every result:  python src/run_all.py

Writes 03_results/key_numbers.json (single source of truth) and copies it
to 04_tool/web/data/ for the website.
"""
import json
import shutil
from datetime import datetime, timezone

import config
import load
import baseline
import optimize
import evaluate
import sensitivity


def main():
    for d in (config.FIGURES, config.TABLES, config.WEB_DATA):
        d.mkdir(parents=True, exist_ok=True)

    data = load.run()
    params = dict(config.PARAMS)

    base = baseline.run(data, params)
    opt = optimize.run(data, params)
    value = evaluate.compare(base, opt, params)

    metric = lambda p: evaluate.compare(baseline.run(data, p), optimize.run(data, p), p)["npv"]
    torn = sensitivity.tornado(metric, params, config.SENSITIVITY)
    scen = sensitivity.scenarios(metric, params, config.SCENARIOS)

    key = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "decision": opt.get("decision"),
        "headline": {
            "annual_savings_usd": round(value["annual_savings"], 2),
            "grid_metric_change": round(value["grid_metric_change"], 3),
            "npv_usd": round(value["npv"], 2),
            "payback_years": value["payback_years"] if value["payback_years"] != float("inf") else None,
        },
        "strategies": evaluate.stakeholder_scorecard([base, opt]),
        "tornado": torn,
        "scenarios": scen,
        "params": params,
    }
    config.KEY_NUMBERS.write_text(json.dumps(key, indent=2, default=str))
    shutil.copy(config.KEY_NUMBERS, config.WEB_DATA / "key_numbers.json")
    print(f"[run_all] wrote {config.KEY_NUMBERS}")


if __name__ == "__main__":
    main()
