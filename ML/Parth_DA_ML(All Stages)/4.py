"""
================================================================================
STAGE 4: Feature Engineering, Transformation & Selection
DATASET: WA_Fn-UseC_-Telco-Customer-Churn.csv (IBM Telco Customer Churn)
================================================================================

WHAT THIS STAGE COVERS (from Minutes.txt, Day 4 & Day 5):
  1. Strict Train / Test Fit-Transform Separation:
     - Drop pseudonymous PII ('customerID') under GDPR compliance
     - Stratified 80/20 Split on 'Churn' target BEFORE any transformations
     - Fitting transformers exclusively on train; applying them to validation/test
  2. Domain Feature Generation:
     - Ratio features: charge_per_tenure, total_to_monthly_ratio (implied tenure)
     - Aggregation features: active_services_count (sum of add-on digital services)
     - Risk interaction flag: has_fiber_no_techsupport (high-churn profile)
     - Contract loyalty ordinal ranking: Month-to-month=1, One year=2, Two year=3
  3. Categorical Encoding:
     - Binary mapping for 2-level nominal features
     - Rare category grouping (cardinality reduction)
     - Low-cardinality One-Hot Encoding (drop='first', handle_unknown='ignore')
  4. Numerical Transformation & Scaling:
     - Yeo-Johnson Power Transformation for right-skewed distributions
     - Z-Score Standardization (StandardScaler)
  5. Multistage Feature Selection:
     - Zero-Variance feature removal (VarianceThreshold = 0.0)
     - Quasi-Constant feature removal (VarianceThreshold = 0.01)
     - Multicollinearity Pearson correlation filter (r > 0.85)
     - Statistical Feature Selection: Mutual Information (SelectKBest, top k=15)
  6. Optional Dimensionality Reduction:
     - Principal Component Analysis (PCA with 95% explained variance retention)
  7. Production Artifact Serialization:
     - Exporting fitted preprocessing transformers via joblib
================================================================================
"""

import warnings
import logging
from pathlib import Path
from typing import List, Tuple
import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, PowerTransformer, StandardScaler
from sklearn.feature_selection import VarianceThreshold, SelectKBest, mutual_info_classif
from sklearn.decomposition import PCA

warnings.filterwarnings("ignore")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s]: %(message)s"
)
logger = logging.getLogger("Stage4_FeatureEng")

# Resolve Paths
CURRENT_DIR = Path(__file__).resolve().parent
CLEANED_PATH = CURRENT_DIR / "stage3_cleaned_telco.csv"
RAW_PATH = CURRENT_DIR / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
MODELS_DIR = CURRENT_DIR / "fitted_artifacts"
MODELS_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 80)
print("STAGE 4: FEATURE ENGINEERING, TRANSFORMATION & SELECTION")
print("=" * 80)

# Load dataset from Stage 3 or Raw fallback
if CLEANED_PATH.exists():
    df = pd.read_csv(CLEANED_PATH)
    logger.info(f"Loaded Stage 3 cleaned dataset: {CLEANED_PATH.name} ({len(df):,} rows)")
elif RAW_PATH.exists():
    df = pd.read_csv(RAW_PATH)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"].replace(" ", np.nan), errors="coerce").fillna(0.0)
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0}).astype(int)
    logger.info(f"Loaded Raw dataset: {RAW_PATH.name} ({len(df):,} rows)")
else:
    raise FileNotFoundError("Could not locate Telco dataset!")


# =============================================================================
# STEP 0: DATA LEAKAGE PREVENTION (STRICT FIT-TRANSFORM SEPARATION)
# =============================================================================
print("\n--- [STEP 0] DATA LEAKAGE PREVENTION: STRATIFIED TRAIN / TEST SPLIT ---")

# 0a. Drop PII identifier under GDPR mandate
if "customerID" in df.columns:
    df = df.drop(columns=["customerID"])
    logger.info("Dropped pseudonymous PII column 'customerID' before modeling.")

TARGET_COL = "Churn"
X = df.drop(columns=[TARGET_COL])
y = df[TARGET_COL]

# 0b. Stratified 80/20 train/test split (guarantees identical positive rate in both folds)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
X_train = X_train.reset_index(drop=True)
X_test  = X_test.reset_index(drop=True)
y_train = y_train.reset_index(drop=True)
y_test  = y_test.reset_index(drop=True)

logger.info(f"Stratified Split: Train={len(X_train):,} records | Test={len(X_test):,} records")
print(f"  * Training Set Size : {len(X_train):,} rows ({y_train.mean()*100:.2f}% Churn)")
print(f"  * Testing Set Size  : {len(X_test):,} rows ({y_test.mean()*100:.2f}% Churn)")


# =============================================================================
# STEP 1: DOMAIN FEATURE GENERATION
# =============================================================================
print("\n--- [STEP 1] DOMAIN FEATURE GENERATION ---")

def generate_domain_features(df_input: pd.DataFrame) -> pd.DataFrame:
    """
    Applies telecom domain feature transformations:
      1. Ratios: charge_per_tenure, total_to_monthly_ratio
      2. Service Aggregation: active_services_count
      3. Risk Interaction Flag: has_fiber_no_techsupport
      4. Contract Loyalty Ordinal Mapping
    """
    df_out = df_input.copy()

    # (A) Charge per month of tenure (with division-by-zero protection)
    safe_tenure = df_out["tenure"].replace(0, 1)
    df_out["charge_per_tenure"] = df_out["MonthlyCharges"] / safe_tenure

    # (B) Total-to-monthly charge ratio (approximates actual bill cycles)
    safe_monthly = df_out["MonthlyCharges"].replace(0, 1.0)
    df_out["total_to_monthly_ratio"] = df_out["TotalCharges"] / safe_monthly

    # (C) Digital Add-on Services Count
    service_cols = [
        "OnlineSecurity", "OnlineBackup", "DeviceProtection",
        "TechSupport", "StreamingTV", "StreamingMovies"
    ]
    existing_services = [c for c in service_cols if c in df_out.columns]
    # Count how many services are 'Yes'
    df_out["active_services_count"] = (df_out[existing_services] == "Yes").sum(axis=1)

    # (D) Fiber Optic with No TechSupport (Top empirical churn risk archetype)
    if "InternetService" in df_out.columns and "TechSupport" in df_out.columns:
        df_out["has_fiber_no_techsupport"] = (
            (df_out["InternetService"] == "Fiber optic") & (df_out["TechSupport"] == "No")
        ).astype(int)

    # (E) Contract Loyalty Score (Ordinal ranking)
    contract_loyalty_map = {"Month-to-month": 1, "One year": 2, "Two year": 3}
    if "Contract" in df_out.columns:
        df_out["contract_loyalty_score"] = df_out["Contract"].map(contract_loyalty_map).fillna(1).astype(int)

    return df_out

X_train = generate_domain_features(X_train)
X_test  = generate_domain_features(X_test)
logger.info(f"Generated 5 new domain features. Train feature count: {X_train.shape[1]}")
print(f"  * Generated Features: ['charge_per_tenure', 'total_to_monthly_ratio', 'active_services_count', 'has_fiber_no_techsupport', 'contract_loyalty_score']")


# =============================================================================
# STEP 2: CATEGORICAL ENCODING
# =============================================================================
print("\n--- [STEP 2] CATEGORICAL ENCODING (OHE & BINARY MAPPING) ---")

# 2a. Binary Yes/No Columns -> 0/1 mapping
binary_cols = ["Partner", "Dependents", "PhoneService", "PaperlessBilling"]
existing_binary = [c for c in binary_cols if c in X_train.columns]
for c in existing_binary:
    binary_map = {"Yes": 1, "No": 0}
    X_train[c] = X_train[c].map(binary_map).fillna(0).astype(int)
    X_test[c]  = X_test[c].map(binary_map).fillna(0).astype(int)

# Map gender
if "gender" in X_train.columns:
    X_train["gender"] = X_train["gender"].map({"Male": 1, "Female": 0}).fillna(0).astype(int)
    X_test["gender"]  = X_test["gender"].map({"Male": 1, "Female": 0}).fillna(0).astype(int)

# 2b. Multi-class Categoricals for One-Hot Encoding
nominal_cols = [
    "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup",
    "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies",
    "Contract", "PaymentMethod"
]
nominal_cols = [c for c in nominal_cols if c in X_train.columns]

# Fit OneHotEncoder exclusively on train partition
ohe_encoder = OneHotEncoder(drop="first", sparse_output=False, handle_unknown="ignore")
ohe_encoder.fit(X_train[nominal_cols])

def apply_ohe_transform(df_data: pd.DataFrame, encoder: OneHotEncoder, cols: List[str]) -> pd.DataFrame:
    encoded_matrix = encoder.transform(df_data[cols])
    encoded_feature_names = encoder.get_feature_names_out(cols)
    encoded_df = pd.DataFrame(encoded_matrix, columns=encoded_feature_names, index=df_data.index)
    df_remaining = df_data.drop(columns=cols)
    return pd.concat([df_remaining, encoded_df], axis=1)

X_train = apply_ohe_transform(X_train, ohe_encoder, nominal_cols)
X_test  = apply_ohe_transform(X_test, ohe_encoder, nominal_cols)

# Ensure column alignment between train and test
X_train, X_test = X_train.align(X_test, join="left", axis=1, fill_value=0.0)

logger.info(f"Categorical Encoding complete. New dimension: {X_train.shape[1]} features.")
print(f"  * After OHE: {X_train.shape[1]} total columns in feature matrix")


# =============================================================================
# STEP 3: NUMERICAL TRANSFORMATION & SCALING
# =============================================================================
print("\n--- [STEP 3] NUMERICAL TRANSFORMATION & SCALING ---")

continuous_cols = [
    "tenure", "MonthlyCharges", "TotalCharges",
    "charge_per_tenure", "total_to_monthly_ratio"
]
continuous_cols = [c for c in continuous_cols if c in X_train.columns]

# 3a. Yeo-Johnson Power Transformation on skewed columns
power_transformer = PowerTransformer(method="yeo-johnson")
skewed_features = ["TotalCharges", "charge_per_tenure", "total_to_monthly_ratio"]
skewed_features = [c for c in skewed_features if c in X_train.columns]

power_transformer.fit(X_train[skewed_features])
X_train[skewed_features] = power_transformer.transform(X_train[skewed_features])
X_test[skewed_features]  = power_transformer.transform(X_test[skewed_features])
logger.info(f"Fitted Yeo-Johnson Power Transform on {skewed_features}")

# 3b. Z-Score Standardization (StandardScaler)
scaler = StandardScaler()
scaler.fit(X_train[continuous_cols])
X_train[continuous_cols] = scaler.transform(X_train[continuous_cols])
X_test[continuous_cols]  = scaler.transform(X_test[continuous_cols])
logger.info(f"Fitted StandardScaler on {continuous_cols}")

print(f"  * Scaled {len(continuous_cols)} continuous columns to mean=0, std=1")


# =============================================================================
# STEP 4: MULTISTAGE FEATURE SELECTION
# =============================================================================
print("\n--- [STEP 4] MULTISTAGE FEATURE SELECTION ---")

# (A) Zero-Variance Filter
vt_zero = VarianceThreshold(threshold=0.0)
vt_zero.fit(X_train)
zero_var_mask = vt_zero.get_support()
dropped_zero = [col for col, keep in zip(X_train.columns, zero_var_mask) if not keep]
X_train = X_train.loc[:, zero_var_mask]
X_test  = X_test.loc[:, zero_var_mask]
logger.info(f"Zero-Variance filter dropped: {dropped_zero if dropped_zero else 'None'}")

# (B) Quasi-Constant Filter (threshold=0.01)
vt_quasi = VarianceThreshold(threshold=0.01)
vt_quasi.fit(X_train)
quasi_mask = vt_quasi.get_support()
dropped_quasi = [col for col, keep in zip(X_train.columns, quasi_mask) if not keep]
X_train = X_train.loc[:, quasi_mask]
X_test  = X_test.loc[:, quasi_mask]
logger.info(f"Quasi-Constant filter dropped: {dropped_quasi if dropped_quasi else 'None'}")

# (C) Multicollinearity Pearson Correlation Filter (r > 0.85)
corr_matrix = X_train.corr().abs()
upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
high_corr_cols = [col for col in upper_tri.columns if any(upper_tri[col] > 0.85)]
if high_corr_cols:
    X_train = X_train.drop(columns=high_corr_cols)
    X_test  = X_test.drop(columns=high_corr_cols)
    logger.info(f"Correlation Filter dropped collinear features (r > 0.85): {high_corr_cols}")
else:
    logger.info("Correlation Filter: No pairwise collinearity exceeding r > 0.85 found.")

# (D) Statistical Scoring: Mutual Information (SelectKBest, top k=15)
TOP_K = min(15, X_train.shape[1])
mi_selector = SelectKBest(score_func=mutual_info_classif, k=TOP_K)
mi_selector.fit(X_train, y_train)

selected_features = [col for col, keep in zip(X_train.columns, mi_selector.get_support()) if keep]
mi_scores = dict(zip(X_train.columns, mi_selector.scores_))

X_train_selected = X_train[selected_features]
X_test_selected  = X_test[selected_features]

print(f"\n  Top {TOP_K} Features Selected via Mutual Information:")
for rank, (feat, score) in enumerate(sorted(mi_scores.items(), key=lambda item: item[1], reverse=True)[:TOP_K], 1):
    print(f"    {rank:2d}. {feat:<38}: MI Score = {score:.4f}")


# =============================================================================
# STEP 5: OPTIONAL DIMENSIONALITY REDUCTION (PCA)
# =============================================================================
print("\n--- [STEP 5] OPTIONAL DIMENSIONALITY REDUCTION (PCA) ---")

pca = PCA(n_components=0.95, random_state=42)
X_train_pca = pca.fit_transform(X_train_selected)
X_test_pca  = pca.transform(X_test_selected)

cum_var = np.sum(pca.explained_variance_ratio_) * 100
logger.info(f"PCA reduced {X_train_selected.shape[1]} features -> {X_train_pca.shape[1]} components capturing {cum_var:.2f}% cumulative variance.")
print(f"  * PCA Reduced Dimensions : {X_train_pca.shape[1]} components")
print(f"  * Total Variance Retained: {cum_var:.2f}%")


# =============================================================================
# STEP 6: PRODUCTION ARTIFACT SERIALIZATION
# =============================================================================
print("\n--- [STEP 6] PRODUCTION ARTIFACT SERIALIZATION ---")

artifacts = {
    "ohe_encoder.joblib"       : ohe_encoder,
    "power_transformer.joblib" : power_transformer,
    "std_scaler.joblib"        : scaler,
    "mi_selector.joblib"       : mi_selector,
    "pca.joblib"               : pca,
    "selected_features.joblib" : selected_features
}

for filename, obj in artifacts.items():
    joblib.dump(obj, MODELS_DIR / filename)
logger.info(f"Serialized {len(artifacts)} production transformers into: {MODELS_DIR.name}/")

# Export Final Engineered Matrices
train_export = CURRENT_DIR / "train_features.csv"
test_export  = CURRENT_DIR / "test_features.csv"

train_full = pd.concat([X_train_selected, y_train.rename(TARGET_COL)], axis=1)
test_full  = pd.concat([X_test_selected, y_test.rename(TARGET_COL)], axis=1)

train_full.to_csv(train_export, index=False)
test_full.to_csv(test_export, index=False)
logger.info(f"Persisted train feature matrix: {train_export.name} ({train_full.shape})")
logger.info(f"Persisted test feature matrix : {test_export.name} ({test_full.shape})")


# =============================================================================
# FINAL SUMMARY
# =============================================================================
print("\n" + "=" * 80)
print("STAGE 4 FEATURE ENGINEERING COMPLETE")
print("=" * 80)
print(f"  * Final Train Shape     : {X_train_selected.shape[0]:,} rows x {X_train_selected.shape[1]} features")
print(f"  * Final Test Shape      : {X_test_selected.shape[0]:,} rows x {X_test_selected.shape[1]} features")
print(f"  * Train Features Export : {train_export.name}")
print(f"  * Test Features Export  : {test_export.name}")
print(f"  * Artifacts Saved In    : {MODELS_DIR.name}/")
print(f"  * Pipeline Status       : Ready for Stage 5: Model Training, Experimentation & Validation")
print("=" * 80)
