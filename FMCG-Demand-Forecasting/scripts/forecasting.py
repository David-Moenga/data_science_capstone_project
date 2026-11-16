\"\"\"Forecasting helpers (skeleton) from capstone notes.

- Baseline: seasonal naive using lag_12 (same month last year).
- Model: tree ensemble (e.g. RandomForest) with calendar + lag features.
- Metrics: MAE, RMSE, WAPE (see report for definitions).
\"\"\"

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error


def wape(y_true, y_pred) -> float:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    denom = np.abs(y_true).sum()
    if denom == 0:
        return float("nan")
    return float(np.abs(y_true - y_pred).sum() / denom * 100.0)


def evaluate_forecast(y_true, y_pred) -> dict:
    return {
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "rmse": float(np.sqrt(mean_squared_error(y_true, y_pred))),
        "wape": wape(y_true, y_pred),
    }
