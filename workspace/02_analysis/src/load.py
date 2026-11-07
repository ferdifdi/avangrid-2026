"""Read raw files, clean them, write analysis-ready data to 01_data/processed/.

Rules: never modify raw files; align timestamps to one timezone; keep units explicit.
"""
import pandas as pd
from config import DATA_RAW, DATA_PROC


def read_raw() -> dict:
    """Load every CSV/XLSX in raw/ into a dict of DataFrames keyed by file stem."""
    frames = {}
    for f in sorted(DATA_RAW.glob("*")):
        if f.suffix.lower() == ".csv":
            frames[f.stem] = pd.read_csv(f)
        elif f.suffix.lower() in (".xlsx", ".xls"):
            for sheet, df in pd.read_excel(f, sheet_name=None).items():
                frames[f"{f.stem}__{sheet}"] = df
    return frames


def clean(frames: dict) -> dict:
    """Challenge-specific cleaning. TODO after the data audit."""
    out = {}
    for name, df in frames.items():
        df = df.copy()
        df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
        out[name] = df.drop_duplicates()
    return out


def run() -> dict:
    DATA_PROC.mkdir(parents=True, exist_ok=True)
    frames = clean(read_raw())
    for name, df in frames.items():
        df.to_csv(DATA_PROC / f"{name}.csv", index=False)
    print(f"[load] {len(frames)} table(s) processed")
    return frames


if __name__ == "__main__":
    run()
