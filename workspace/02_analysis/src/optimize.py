"""The decision model.

Write the formulation in playbook/prompt.md Part A4 first, then implement here:
  decision variables, objective, constraints, uncertain inputs, output.

Suggested solvers: PuLP (LP/MILP, bundled CBC), OR-Tools, Pyomo + HiGHS,
or exact dynamic programming for small sequential problems (see practice/js/model.js).
"""


def run(data: dict, params: dict) -> dict:
    """Return the optimized outcome. Same keys as baseline.run()."""
    # TODO: build and solve the model
    return {"name": "Optimized", "annual_cost": 0.0, "grid_metric": 0.0, "feasible": True, "decision": None}
