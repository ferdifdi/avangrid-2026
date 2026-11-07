"""Extract analysis blocks from notebooks into website data.

Usage:  python workspace/04_tool/extract_notebooks.py
Reads:  workspace/02_analysis/notebooks/*.ipynb   (saved with outputs)
Writes: workspace/04_tool/web/data/analyses.json
        workspace/04_tool/web/assets/nb/<notebook>_<n>.png|svg

Markers are documented in 02_analysis/notebooks/README.md.
Uses only the standard library.
"""
import base64
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE.parent
NB_DIR = WS / "02_analysis" / "notebooks"
OUT_JSON = HERE / "web" / "data" / "analyses.json"
IMG_DIR = HERE / "web" / "assets" / "nb"

TYPES = {
    "energy-optimization": ("⚡", "Energy optimization"),
    "modeling": ("📐", "Mathematical modeling"),
    "forecasting": ("🔮", "Forecasting"),
    "cost-benefit": ("💰", "Cost-benefit"),
    "risk": ("🎲", "Risk / scenarios"),
    "incentive": ("🎁", "Incentive / policy design"),
    "stakeholder": ("👥", "Stakeholder analysis"),
    "validation": ("✅", "Validation"),
}
HEAD_RE = re.compile(r"^#{1,6}\s*ANALYSIS\s*\|\s*([\w-]+)\s*\|\s*(.+)$", re.I)


def src(cell):
    s = cell.get("source", "")
    return "".join(s) if isinstance(s, list) else s


def text_of(out):
    if out.get("output_type") == "stream":
        t = out.get("text", "")
    else:
        t = out.get("data", {}).get("text/plain", "")
    return "".join(t) if isinstance(t, list) else t


def last_json(outputs):
    for out in reversed(outputs):
        data = out.get("data", {})
        if "application/json" in data:
            return data["application/json"]
        t = text_of(out).strip()
        if t:
            for line in reversed(t.splitlines()):
                line = line.strip()
                if line.startswith(("{", "[")):
                    try:
                        return json.loads(line)
                    except json.JSONDecodeError:
                        pass
            try:
                return json.loads(t)
            except json.JSONDecodeError:
                pass
    return None


def main():
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    notebooks = sorted(p for p in NB_DIR.glob("*.ipynb") if not p.name.startswith("00_TEMPLATE"))
    analyses, key_numbers, warnings = [], {}, []
    img_n = 0

    for nb_path in notebooks:
        nb = json.loads(nb_path.read_text(encoding="utf-8"))
        cur = None
        for cell in nb.get("cells", []):
            body = src(cell).strip()
            first = body.splitlines()[0].strip() if body else ""

            if cell["cell_type"] == "markdown":
                m = HEAD_RE.match(first)
                if m:
                    t = m.group(1).lower()
                    if t not in TYPES:
                        warnings.append(f"{nb_path.name}: unknown type '{t}'")
                    ico, name = TYPES.get(t, ("•", t))
                    cur = {"id": f"a{len(analyses) + 1}", "notebook": nb_path.name, "type": t, "type_icon": ico,
                           "type_name": name, "question": m.group(2).strip(), "what": "", "answer": "",
                           "method": "", "figures": [], "tables": [], "text": [], "data": {}}
                    analyses.append(cur)
                    rest = body.splitlines()[1:]
                    body = "\n".join(rest)
                if cur is None:
                    continue
                for line in body.splitlines():
                    s = line.strip()
                    if s.lower().startswith("what this shows:"):
                        cur["what"] = s.split(":", 1)[1].strip()
                    elif s.startswith("**Answer:**"):
                        cur["answer"] = s[len("**Answer:**"):].strip()
                    elif s.startswith("**Method:**"):
                        cur["method"] = s[len("**Method:**"):].strip()
                continue

            if cell["cell_type"] != "code":
                continue
            outputs = cell.get("outputs", [])
            tags = cell.get("metadata", {}).get("tags", [])

            if first.startswith("# export-key"):
                obj = last_json(outputs)
                if isinstance(obj, dict):
                    key_numbers.update(obj)
                else:
                    warnings.append(f"{nb_path.name}: export-key cell has no JSON output")
                continue
            if first.startswith("# export-data"):
                name = first.split(":", 1)[1].strip() if ":" in first else f"data{len(cur['data']) if cur else 0}"
                obj = last_json(outputs)
                if cur is None:
                    warnings.append(f"{nb_path.name}: export-data '{name}' before any ANALYSIS heading")
                elif obj is None:
                    warnings.append(f"{nb_path.name}: export-data '{name}' has no JSON output")
                else:
                    cur["data"][name] = obj
                continue
            if not (first.startswith("# export") or "export" in tags) or cur is None:
                continue

            for out in outputs:
                data = out.get("data", {})
                if "image/png" in data or "image/svg+xml" in data:
                    img_n += 1
                    stem = f"{nb_path.stem}_{img_n}"
                    if "image/svg+xml" in data:
                        svg = data["image/svg+xml"]
                        (IMG_DIR / f"{stem}.svg").write_text("".join(svg) if isinstance(svg, list) else svg, encoding="utf-8")
                        cur["figures"].append(f"assets/nb/{stem}.svg")
                    else:
                        png = data["image/png"]
                        png = "".join(png) if isinstance(png, list) else png
                        (IMG_DIR / f"{stem}.png").write_bytes(base64.b64decode(png))
                        cur["figures"].append(f"assets/nb/{stem}.png")
                elif "text/html" in data:
                    h = data["text/html"]
                    cur["tables"].append("".join(h) if isinstance(h, list) else h)
                else:
                    t = text_of(out).strip()
                    if t:
                        cur["text"].append(t)

    for a in analyses:
        if not a["answer"]:
            warnings.append(f"{a['notebook']}: '{a['question']}' has no **Answer:** line")

    OUT_JSON.write_text(json.dumps({"analyses": analyses, "key_numbers": key_numbers,
                                    "types": {k: {"icon": v[0], "name": v[1]} for k, v in TYPES.items()}},
                                   indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[extract] {len(notebooks)} notebook(s) -> {len(analyses)} analyses, {img_n} figure(s) -> {OUT_JSON}")
    for w in warnings:
        print("  WARNING:", w)
    return 0


if __name__ == "__main__":
    sys.exit(main())
