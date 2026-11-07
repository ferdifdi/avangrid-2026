"""Tornado (one-at-a-time), scenarios, and break-even search."""
from typing import Callable


def tornado(metric_fn: Callable[[dict], float], params: dict, ranges: dict) -> list:
    """metric_fn(params) -> float. Returns rows sorted by impact (largest first)."""
    base = metric_fn(params)
    rows = []
    for name, (lo, hi) in ranges.items():
        v_lo = metric_fn({**params, name: lo})
        v_hi = metric_fn({**params, name: hi})
        rows.append({"param": name, "low": lo, "high": hi, "value_low": v_lo,
                     "value_high": v_hi, "base": base, "range": abs(v_hi - v_lo)})
    return sorted(rows, key=lambda r: r["range"], reverse=True)


def scenarios(metric_fn: Callable[[dict], float], params: dict, overrides: dict) -> dict:
    return {name: metric_fn({**params, **o}) for name, o in overrides.items()}


def break_even(metric_fn: Callable[[dict], float], params: dict, name: str,
               lo: float, hi: float, target: float = 0.0, iters: int = 40):
    """Bisection: value of `name` where metric crosses `target`. None if no crossing."""
    f = lambda x: metric_fn({**params, name: x}) - target
    a, b = lo, hi
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        return None
    for _ in range(iters):
        m = (a + b) / 2
        fm = f(m)
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a + b) / 2
