DS785 Capstone Project
AI-Driven Regional Electric Vehicle Adoption Readiness Score

Bharani Sudhakar

Overview
This presentation covers the data collection, validation, cleaning, and preprocessing stage of my capstone project AI-Driven Regional Electric Vehicle Adoption Readiness Score Using Machine Learning Techniques.The objective of this phase is to prepare a analysis-ready dataset prior to EDA,Feature engineering and model development.

The presentation demonstrates the full preprocessing workflow applied to the Electric Vehicle Population Dataset obtained from the Washington State Open Data Portal (data.gov). The Presentation explains about below points.

1.Data sourcing and extraction process

2.Initial data profiling and dataset validation

3.Missing data assessment and mitigation strategy

4.Check Duplicate records

5.Formatting and categorical standardization

6.Numeric validation and outlier handling

7.Creation of derived variables required for regional aggregation

Dataset:

Electric Vehicle Population Dataset  
Source: Washington State Open Data Portal / data.gov

Data also in the raw folder.

The dataset contains electric vehicle registration records including:

Model Year
Electric Range
Electric Vehicle Type
CAFV Eligibility
Manufacturer and Model
County and State location
Utility provider
Vehicle identification number (DOL Vehicle ID)

Project Structure

Code/
run_pipeline.py
quality_check.py
cleaning_preprocessing.py

Data/
raw/
processed/

ReadMe.txt

Code Description

run_pipeline.py
Main pipeline script that executes the entire workflow.  
Loads the dataset, runs data quality checks, performs cleaning and preprocessing, and saves the processed datasets.

quality_check.py
Performs data quality validation including:
Schema inspection
Column validation
Missing value analysis
Duplicate record detection
Duplicate vehicle ID validation

cleaning_preprocessing.py
Handles data cleaning and feature preparation including:
Removing duplicate vehicles using DOL Vehicle ID
Dropping VIN identifier column
Handling missing values
Fixing data types
Standardizing categorical variables
Removing invalid electric range values
Feature engineering (BEV indicator, CAFV eligibility indicator, vehicle age)
Aggregating data to regional level

Processing Steps

1. Load raw EV dataset
2. Perform data quality checks
3. Identify missing values and duplicates
4. Remove duplicate vehicles
5. Handle missing values
6. Standardize categorical variables
7. Validate numeric ranges
8. Engineer additional features
9. Create regional aggregated dataset
10. Export cleaned datasets

Outputs

Processed vehicle dataset
Data/processed/Electric_Vehicle_Population_Data.csv

Regional aggregated dataset
Data/processed/ev_regional_dataset.csv

How to Run

Navigate to the Code directory and execute:

python3 run_pipeline.py

AI Tool Disclosure

AI tools were used for minor formatting assistance .Organizing and  comments.I completed code long back in notebook and later see the comments that code check in cannot be ipynb.So used AI to organize folder and later did all myself .Ai organized it but troubleshooting was done by myself.
Tried organizing Folder with the help of AI and which never worked it Manually pushed code succuessfully.
All code logic, data preparation steps, and validation checks were reviewed, verified, and tested manually to ensure correctness and alignment with the project methodology.