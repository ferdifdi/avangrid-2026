"""Status quo / simplest answer to the decision. Every other model must beat this."""


def run(data: dict, params: dict) -> dict:
    """Return the baseline outcome in the same units as optimize.run().

    TODO: implement the status-quo rule from 00_brief/challenge.md
    (e.g. charge immediately, replace oldest asset first, accept forward price).
    """
    return {"name": "Status quo", "annual_cost": 0.0, "grid_metric": 0.0, "feasible": True}
