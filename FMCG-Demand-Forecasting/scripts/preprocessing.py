\"\"\"Preprocessing utilities for FMCG demand forecasting.

Based on the capstone workflow (see presentation report and notebooks):
- Parse dates; validate derived calendar fields.
- Validate sales formulas: gross = units_sold * list_price; net = gross * (1 - discount_pct).
- Keep zero-sales rows (treat as valid no-sale observations unless business rules say otherwise).
- Aggregate daily -> monthly SKU demand for segmentation and forecasting.
- For XYZ, build a complete SKU-month grid and fill missing months with 0 before CV.
\"\"\"

from __future__ import annotations

import pandas as pd


def load_sales_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df


def monthly_sku_demand(df: pd.DataFrame) -> pd.DataFrame:
    \"\"\"Aggregate to monthly SKU demand (sum of units_sold).\"\"\"
    tmp = df.copy()
    tmp["year_month"] = tmp["date"].dt.to_period("M")
    return (
        tmp.groupby(["year_month", "sku_id"], as_index=False)["units_sold"]
        .sum()
        .rename(columns={"units_sold": "demand"})
    )
