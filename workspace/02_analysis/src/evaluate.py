"""Turn model outputs into business value: $ savings, NPV, payback, stakeholder metrics."""


def annuity_factor(rate: float, years: int) -> float:
    return (1 - (1 + rate) ** -years) / rate if rate else float(years)


def npv(capex: float, annual_benefit: float, rate: float, years: int) -> float:
    return -capex + annual_benefit * annuity_factor(rate, years)


def payback_years(capex: float, annual_benefit: float) -> float:
    return capex / annual_benefit if annual_benefit > 0 else float("inf")


def compare(baseline: dict, optimized: dict, params: dict) -> dict:
    """Value of the optimized plan vs the baseline."""
    savings = baseline["annual_cost"] - optimized["annual_cost"]
    return {
        "annual_savings": savings,
        "grid_metric_change": baseline["grid_metric"] - optimized["grid_metric"],
        "npv": npv(params["capex"], savings, params["discount_rate"], params["horizon_years"]),
        "payback_years": payback_years(params["capex"], savings),
    }


def stakeholder_scorecard(results: list) -> list:
    """One row per strategy. TODO: add the metric each stakeholder cares about."""
    return [{"strategy": r["name"], "cost": r["annual_cost"], "grid": r["grid_metric"], "reliable": r["feasible"]} for r in results]
