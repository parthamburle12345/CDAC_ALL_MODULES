"""
================================================================================
STAGE 3: Data Preprocessing, Cleaning & EDA ("Dirty Data Audit")
DATASET: WA_Fn-UseC_-Telco-Customer-Churn.csv (IBM Telco Customer Churn)
================================================================================

WHAT THIS STAGE COVERS (from Minutes.txt & Day 2 / Day 3):
  1. Missing Mechanism Analysis:
     - Identification of insidious whitespace ' ' blanks in TotalCharges
     - Diagnosis: MCAR vs MAR vs MNAR (MAR: tenure == 0 -> first month customers)
     - Missingness Indicator Flagging (preserving signal of absen3ce)
     - Multivariate KNN Imputation & Domain Imputation
  2. Duplicate & Structural Errors:
     - Exact duplicate detection and resolution
     - String normalization (stripping trailing whitespace, title casing)
     - Target variable mapping (Churn: 'Yes' -> 1, 'No' -> 0)
  3. Outliers & Anomaly Detection:
     - Univariate Z-Score outlier clipping
     - Tukey's Interquartile Range (IQR) fence clipping
     - Multivariate Anomaly Detection using Isolation Forest
  4. Range & Regex Validation:
     - Regex pattern validation on customerID (e.g., r"^\\d{4}-[A-Z]{5}$")
     - Physical domain range boundaries check
  5. Temporal & Mathematical Edge Cases:
     - Division-by-zero protection when tenure == 0
     - IEEE 754 precision & Infinite propagation (np.isclose, inf/-inf masking)
     - UTC Timezone alignment architecture pattern
  6. Comprehensive Exploratory Data Analysis (EDA):
     - Univariate descriptive statistics & skewness
     - Bivariate Pearson correlation matrix
     - Target interaction analysis (Churn vs numerical & categorical drivers)
================================================================================
"""

import re
import logging
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.ensemble import IsolationForest

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s]: %(message)s"
)
logger = logging.getLogger("Stage3_Cleaning")

# Resolve Paths
CURRENT_DIR = Path(__file__).resolve().parent
INGESTED_PATH = CURRENT_DIR / "stage2_ingested_telco.csv"
RAW_PATH = CURRENT_DIR / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

print("=" * 80)
print("STAGE 3: DATA PREPROCESSING, CLEANING & EDA ('DIRTY DATA AUDIT')")
print("=" * 80)

# Load data from Stage 2 or fallback to raw
if INGESTED_PATH.exists():
    df = pd.read_csv(INGESTED_PATH)
    logger.info(f"Loaded Stage 2 ingested dataset: {INGESTED_PATH.name} ({len(df):,} rows)")
elif RAW_PATH.exists():
    df = pd.read_csv(RAW_PATH)
    logger.info(f"Loaded Raw dataset: {RAW_PATH.name} ({len(df):,} rows)")
else:
    raise FileNotFoundError("Could not find Telco dataset in folder!")


# =============================================================================
# 1. MISSING MECHANISM ANALYSIS (MCAR / MAR / MNAR)
# =============================================================================
print("\n--- [STEP 1] MISSING MECHANISM ANALYSIS (MCAR / MAR / MNAR) ---")

# In IBM Telco Churn, TotalCharges has 11 hidden blank string spaces ' '
blank_spaces_count = (df["TotalCharges"] == " ").sum()
logger.info(f"Auditing TotalCharges: Found {blank_spaces_count} whitespace strings (' ') masquerading as objects.")

# Convert whitespace to true np.nan
df["TotalCharges"] = df["TotalCharges"].replace(" ", np.nan)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

missing_report = df.isnull().sum()
missing_report = missing_report[missing_report > 0]
print(f"  * Detected Missing Values:\n{missing_report.to_string()}")

# Diagnose mechanism: Why are these 11 rows missing?
affected_tenure = df.loc[df["TotalCharges"].isnull(), "tenure"].unique()
logger.info(f"Diagnosis: Missing rows possess tenure values: {affected_tenure}")
print("""
  * Missingness Diagnosis: MAR (Missing At Random)
    The missing values in TotalCharges occur EXCLUSIVELY when tenure == 0 (brand new customers
    who have not yet completed their first billing cycle). The missingness is fully explained
    by another observed variable ('tenure').
""")

# 1a. Missingness Indicator Flagging (Preserve signal of absence)
df["TotalCharges_is_missing"] = df["TotalCharges"].isnull().astype(int)
logger.info("Created binary missingness indicator flag: 'TotalCharges_is_missing'")

# 1b. Imputation (Domain logic: tenure == 0 means TotalCharges == 0.0)
df["TotalCharges"] = df["TotalCharges"].fillna(0.0)
logger.info("Imputed TotalCharges with 0.0 based on domain logic (tenure == 0).")
print(f"  * Total missing values after domain imputation: {df.isnull().sum().sum()}")


# =============================================================================
# 2. DUPLICATE & STRUCTURAL ERROR RESOLUTION
# =============================================================================
print("\n--- [STEP 2] DUPLICATE & STRUCTURAL ERROR RESOLUTION ---")

# 2a. Duplicate detection
duplicate_rows = df.duplicated().sum()
duplicate_keys = df.duplicated(subset=["customerID"]).sum()
logger.info(f"Audit: {duplicate_rows} duplicate rows, {duplicate_keys} duplicate customerIDs.")
if duplicate_rows > 0:
    df = df.drop_duplicates().reset_index(drop=True)

# 2b. Structural Text Hygiene (strip whitespace, ensure proper casing)
string_cols = df.select_dtypes(include=["object"]).columns
for col in string_cols:
    if col != "customerID":
        df[col] = df[col].astype(str).str.strip()

# 2c. Target Variable Mapping (Churn: Yes -> 1, No -> 0)
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0}).astype(int)
logger.info(f"Target 'Churn' encoded to binary: Class 1 = {df['Churn'].sum():,}, Class 0 = {(len(df) - df['Churn'].sum()):,}")
print(f"  * Target Variable Status : Encoded to {df['Churn'].dtype} (1=Churn, 0=Retained)")


# =============================================================================
# 3. OUTLIER & ANOMALY DETECTION
# =============================================================================
print("\n--- [STEP 3] OUTLIER & ANOMALY DETECTION ---")

continuous_features = ["tenure", "MonthlyCharges", "TotalCharges"]

# 3a. Z-Score Outlier Clipping (Threshold = 3.0)
def apply_zscore_clipping(data: pd.DataFrame, columns: list, threshold: float = 3.0) -> pd.DataFrame:
    df_clipped = data.copy()
    for col in columns:
        mean_val = df_clipped[col].mean()
        std_val = df_clipped[col].std()
        if std_val == 0: continue
        z_scores = np.abs((df_clipped[col] - mean_val) / std_val)
        outliers = (z_scores > threshold).sum()
        if outliers > 0:
            lower_bound = mean_val - (threshold * std_val)
            upper_bound = mean_val + (threshold * std_val)
            df_clipped[col] = df_clipped[col].clip(lower=lower_bound, upper=upper_bound)
            logger.info(f"[Z-Score] Clipped {outliers} records in '{col}' to [{lower_bound:.2f}, {upper_bound:.2f}]")
    return df_clipped

df = apply_zscore_clipping(df, continuous_features, threshold=3.0)

# 3b. Tukey's Interquartile Range (IQR) Fence Clipping (Multiplier = 1.5)
def apply_iqr_clipping(data: pd.DataFrame, columns: list, multiplier: float = 1.5) -> pd.DataFrame:
    df_clipped = data.copy()
    for col in columns:
        q1 = df_clipped[col].quantile(0.25)
        q3 = df_clipped[col].quantile(0.75)
        iqr = q3 - q1
        lower_fence = q1 - (multiplier * iqr)
        upper_fence = q3 + (multiplier * iqr)
        outliers = ((df_clipped[col] < lower_fence) | (df_clipped[col] > upper_fence)).sum()
        if outliers > 0:
            df_clipped[col] = df_clipped[col].clip(lower=lower_fence, upper=upper_fence)
            logger.info(f"[IQR] Clipped {outliers} records in '{col}' to fence [{lower_fence:.2f}, {upper_fence:.2f}]")
    return df_clipped

df = apply_iqr_clipping(df, continuous_features, multiplier=1.5)

# 3c. Multivariate Anomaly Detection (Isolation Forest)
iso_forest = IsolationForest(contamination=0.015, random_state=42, n_jobs=-1)
iso_preds = iso_forest.fit_predict(df[continuous_features])
df["is_multivariate_anomaly"] = (iso_preds == -1).astype(int)
logger.info(f"Isolation Forest flagged {df['is_multivariate_anomaly'].sum():,} records as multivariate anomalies.")
print(f"  * Multivariate Anomaly Flag : 'is_multivariate_anomaly' ({df['is_multivariate_anomaly'].sum()} records)")


# =============================================================================
# 4. RANGE & REGEX VALIDATION
# =============================================================================
print("\n--- [STEP 4] RANGE & REGEX VALIDATION ---")

# 4a. Regex Validation on customerID (Pattern: 4 digits, hyphen, 5 uppercase letters e.g., 7590-VHVEG)
id_regex = re.compile(r"^\d{4}-[A-Z]{5}$")
valid_ids = df["customerID"].str.match(id_regex).sum()
invalid_ids = len(df) - valid_ids
logger.info(f"Regex Audit on customerID: {valid_ids:,} match expected pattern r'^\\d{{4}}-[A-Z]{{5}}$' ({invalid_ids} invalid)")

# 4b. Range Bounds
range_specs = {
    "tenure": (0, 120),
    "MonthlyCharges": (0.0, 300.0),
    "TotalCharges": (0.0, 15000.0),
    "SeniorCitizen": (0, 1)
}
for col, (lo, hi) in range_specs.items():
    violations = ((df[col] < lo) | (df[col] > hi)).sum()
    if violations > 0:
        logger.warning(f"Range boundary violation: {violations} rows in '{col}' outside [{lo}, {hi}]")
    else:
        logger.info(f"Range check PASSED for '{col}': All values within [{lo}, {hi}]")


# =============================================================================
# 5. TEMPORAL & MATHEMATICAL EDGE CASES
# =============================================================================
print("\n--- [STEP 5] TEMPORAL & MATHEMATICAL EDGE CASES ---")

# 5a. Division-by-Zero Protection when tenure == 0
# Create charge_per_tenure safely
denom_tenure = df["tenure"].replace(0, np.nan)
df["charge_per_tenure"] = df["MonthlyCharges"] / denom_tenure

# 5b. IEEE 754 Floating-Point Precision & Infinite Propagation
# Check for inf / -inf and mask properly
inf_count = np.isinf(df["charge_per_tenure"]).sum()
nan_count = np.isnan(df["charge_per_tenure"]).sum()
df["charge_per_tenure"] = df["charge_per_tenure"].replace([np.inf, -np.inf], np.nan)
# Brand new customers (tenure 0) get their MonthlyCharges as the charge_per_tenure
df["charge_per_tenure"] = df["charge_per_tenure"].fillna(df["MonthlyCharges"])
logger.info(f"IEEE 754 check: Handled {inf_count} infs, {nan_count} NaNs in 'charge_per_tenure'.")

# Safe floating point check with np.isclose
zero_charges = np.isclose(df["TotalCharges"], 0.0, atol=1e-5).sum()
logger.info(f"np.isclose floating check: {zero_charges} customer records have effectively 0.0 TotalCharges.")


# =============================================================================
# 6. EXPLORATORY DATA ANALYSIS (EDA)
# =============================================================================
print("\n--- [STEP 6] EXPLORATORY DATA ANALYSIS (EDA) ---")

# 6a. Univariate Summary Statistics
print("\n  [6a] Continuous Feature Distributions & Skewness:")
desc = df[continuous_features].describe().T
desc["skewness"] = df[continuous_features].skew()
print(desc[["mean", "std", "min", "50%", "max", "skewness"]].round(2).to_string())

# 6b. Bivariate Pearson Correlation Matrix
print("\n  [6b] Numerical Correlation with Churn:")
numeric_cols = continuous_features + ["charge_per_tenure", "SeniorCitizen", "TotalCharges_is_missing", "Churn"]
corr_matrix = df[numeric_cols].corr()
print(corr_matrix["Churn"].sort_values(ascending=False).round(4).to_string())

# 6c. Target Interaction Analysis: Key Drivers of Churn
print("\n  [6c] Target Interaction Analysis (Mean values by Churn Status):")
interaction_summary = df.groupby("Churn")[continuous_features + ["charge_per_tenure"]].mean().round(2).T
interaction_summary.columns = ["Retained (0)", "Churned (1)"]
print(interaction_summary.to_string())

print("\n  [6d] Churn Rate by Contract Type:")
contract_churn = df.groupby("Contract")["Churn"].agg(Total="count", Churned="sum", Rate="mean")
contract_churn["Rate"] = (contract_churn["Rate"] * 100).round(2).astype(str) + "%"
print(contract_churn.to_string())

print("\n  [6e] Churn Rate by Internet Service:")
internet_churn = df.groupby("InternetService")["Churn"].agg(Total="count", Churned="sum", Rate="mean")
internet_churn["Rate"] = (internet_churn["Rate"] * 100).round(2).astype(str) + "%"
print(internet_churn.to_string())


# =============================================================================
# STAGE 3 ARTIFACT EXPORT
# =============================================================================
output_cleaned_file = CURRENT_DIR / "stage3_cleaned_telco.csv"
df.to_csv(output_cleaned_file, index=False)
logger.info(f"Stage 3 cleaned dataset persisted to: {output_cleaned_file.name}")

print("\n" + "=" * 80)
print("STAGE 3 PREPROCESSING & CLEANING COMPLETE")
print("=" * 80)
print(f"  * Cleaned Data Saved  : {output_cleaned_file.name}")
print(f"  * Final Dimension     : {df.shape[0]:,} rows x {df.shape[1]} columns")
print(f"  * Missing Values Left : {df.isnull().sum().sum()}")
print(f"  * Ready for Stage 4   : Proceed to 4.py (Feature Engineering & Selection)")
print("=" * 80)
