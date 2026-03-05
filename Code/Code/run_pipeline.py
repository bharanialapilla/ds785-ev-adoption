# run_pipeline.py
import os
import pandas as pd
from quality_check import run_quality_checks
from cleaning_preprocessing import clean_preprocess, build_regional_aggregation
#Read source CSV
df = pd.read_csv("../Data/raw/Electric_Vehicle_Population_Data.csv")
#run quality check
run_quality_checks(df)

df_clean = clean_preprocess(df)

os.makedirs("../Data/processed", exist_ok=True)

df_clean.to_csv("../Data/processed/EV_Vehicle_Population_Data_clean.csv", index=False)

print("\nSaved cleaned dataset")
print("Final shape:", df_clean.shape)

regional_df = build_regional_aggregation(df_clean)

regional_df.to_csv("../Data/processed/ev_regional_dataset.csv", index=False)

print("\nSaved regional dataset")