from pathlib import Path

import pandas as pd

CSV = Path(__file__).parent / "data" / "monthly_tourism_synthetic.csv"


def load_tourism(region="Central NSW", purpose="Holiday"):
    """Load one monthly tourism series, indexed by month."""
    df = pd.read_csv(CSV, parse_dates=["Month"])
    df = df.query("Region == @region and Purpose == @purpose").sort_values("Month")
    y = df.set_index(df["Month"].dt.to_period("M"))["Trips"].astype(float)
    y.index.name = "Period"
    y.name = f"{region} {purpose.lower()} trips"
    return y
