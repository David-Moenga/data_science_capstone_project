# FMCG Global Demand Planning & Forecasting (Capstone)

This project is an end-to-end data science capstone focused on demand planning for a fast-moving consumer goods (FMCG) context using historical sales/inventory-style data (2021–2023).

## What’s in this folder (target structure)

- `data/raw/` — raw inputs (not committed with large/sensitive data by default)
- `data/processed/` — cleaned/aggregated datasets
- `notebooks/`
  - `01_data_preparation.ipynb` (planned)
  - `02_exploratory_analysis.ipynb` (planned)
  - `03_abc_xyz_analysis.ipynb` (planned)
  - `04_statistical_analysis.ipynb` (planned)
  - `05_feature_engineering.ipynb` (planned)
  - `06_demand_forecasting.ipynb` — current consolidated capstone notebook
- `scripts/`
  - `preprocessing.py` (planned)
  - `forecasting.py` (planned)
- `outputs/figures/`, `outputs/forecasts/`
- `presentation/` — includes the full capstone report (`FMCG_Global_Demand_Planning_Forecasting_Capstone_Report.docx`)

## Summary (from the report)

- Dataset (supplied): ~1.1M records, 2021–01-01 to 2023-12-31, 7 countries, 9 cities, 13 stores, 102 SKUs, 4 channels (daily observations aggregated for segmentation/forecasting).
- Data quality: no missing values/duplicates in checked fields; key calculations validated; noted caveats on `stock_out_flag` vs `stock_on_hand` definitions.
- EDA highlights: Italy largest absolute net sales share in this dataset; Snacks + Beverages ~49.5% of net sales; Hypermarkets lead channels; clear weekend higher average daily demand and seasonal patterns.
- Inventory segmentation (monthly SKU aggregation):
  - ABC by inventory consumption value (units×purchase cost): A = 50 SKUs (49.02% of SKUs, 80.04% of value), B 29 (15.30%), C 23 (4.66%).
  - XYZ by CV of monthly demand (with zero-filled months): all 102 classified as **X** under CV≤0.5 (very stable at aggregated level). Combined focus: **AX** group (80.04% of value).
- Hypothesis test (weekday vs weekend daily demand): Welch t-test and paired weekly t-test both reject H0 (α=0.05); weekend mean ~19.77% higher than weekday mean (association in this dataset).
- Forecasting (monthly SKU demand): chronological split 2022 train / 2023 test (2021 used for lags). Rolling one-month-ahead style using actual prior lags.
  - Seasonal-naive (same month last year): WAPE 4.49%, MAE ~796.37, RMSE ~1389.05
  - Random Forest (lags, calendar, SKU/category): WAPE 4.38%, MAE ~775.87, RMSE ~1352.76 (modest improvement; `lag_12` dominates importance).

## Notes & limitations

- Data provenance/currency not independently verified; treat as analytical exercise unless validated.
- XYZ/segmentation done at overall SKU level (can mask store/channel volatility).
- Model is a prototype decision-support tool; validate on real operational data before deployment.

## Full report

See `presentation/FMCG_Global_Demand_Planning_Forecasting_Capstone_Report.docx`.
