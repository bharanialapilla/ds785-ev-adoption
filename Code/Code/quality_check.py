# quality_check.py
import pandas as pd

def run_quality_checks(df):
    print("\n==== DATA QUALITY CHECKS ====\n")

    df.info()

    print("\n[Columns]")
    print(list(df.columns))

    missing = df.isna().sum().sort_values(ascending=False)
    missing_pct = (missing / len(df) * 100).round(3)
    #Missing value table
    missing_table = pd.DataFrame({
        "missing": missing,
        "missing_pct": missing_pct
    }).query("missing > 0")

    print("\n[Missing values per column]")
    print(missing_table)

    print("\n[Full-row duplicates]")
    print(df.duplicated().sum())

    print("\n[Duplicate DOL Vehicle IDs]")
    if "DOL Vehicle ID" in df.columns:
        print(df.duplicated(subset=["DOL Vehicle ID"]).sum())