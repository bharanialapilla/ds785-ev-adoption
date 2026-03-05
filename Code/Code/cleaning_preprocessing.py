# cleaning_preprocessing.py
import pandas as pd

def clean_preprocess(df):

    df = df.copy()
    #Dropping Duplicate ids

    if "DOL Vehicle ID" in df.columns:
        df = df.drop_duplicates(subset=["DOL Vehicle ID"])

    if "VIN (1-10)" in df.columns:
        df = df.drop(columns=["VIN (1-10)"])

    #Drop City or Country

    df = df.dropna(subset=["County", "City"])

    #Fix postal code validation

    if "Postal Code" in df.columns:
        df["Postal Code"] = pd.to_numeric(df["Postal Code"], errors="coerce").round(0).astype("Int64")
    
    #Eelctric range impute value using median

    if "Electric Range" in df.columns:
        df["Electric Range"] = pd.to_numeric(df["Electric Range"], errors="coerce")
        df["Electric Range"] = df["Electric Range"].fillna(df["Electric Range"].median())

    for col in ["County", "City", "Make", "Model", "State"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.upper()

    if "Electric Vehicle Type" in df.columns:
        df["Electric Vehicle Type"] = df["Electric Vehicle Type"].astype(str).str.upper().str.strip()

    caf_col = "Clean Alternative Fuel Vehicle (CAFV) Eligibility"

    if caf_col in df.columns:
        df[caf_col] = df[caf_col].astype(str).str.upper().str.strip()

    if "Electric Range" in df.columns:
        df = df[df["Electric Range"] >= 0]

    print("\nCleaned shape:", df.shape)

    print("\nMissing after cleaning (only >0):")
    print(df.isna().sum().sort_values(ascending=False).loc[lambda s: s > 0])

    ev_type_col = "Electric Vehicle Type"

    #Categorize variable

    if ev_type_col in df.columns:
        df["is_BEV"] = df[ev_type_col].astype(str).str.contains("BEV|BATTERY", case=False, na=False).astype(int)

    if caf_col in df.columns:
        df["is_CAFV_eligible"] = df[caf_col].astype(str).str.contains("ELIGIBLE", case=False, na=False).astype(int)

    CURRENT_YEAR = 2025
    df["vehicle_age"] = CURRENT_YEAR - df["Model Year"]

    return df

#Build Regional Aggregation
def build_regional_aggregation(df):

    regional_df = (
        df.groupby(["State", "County"])
        .agg(
            total_ev=("DOL Vehicle ID", "count"),
            avg_range=("Electric Range", "mean"),
            bev_share=("is_BEV", "mean"),
            cafv_share=("is_CAFV_eligible", "mean"),
            unique_makes=("Make", "nunique"),
            unique_models=("Model", "nunique"),
            avg_vehicle_age=("vehicle_age", "mean")
        )
        .reset_index()
    )

    for c in ["avg_range", "bev_share", "cafv_share", "avg_vehicle_age"]:
        regional_df[c] = regional_df[c].astype(float).round(4)

    print("\nRegional dataset shape:", regional_df.shape)
    print(regional_df.head())

    return regional_df