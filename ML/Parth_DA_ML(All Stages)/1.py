"""
================================================================================
STAGE 1: Problem Definition & Scoping
DATASET: WA_Fn-UseC_-Telco-Customer-Churn.csv (IBM Telco Customer Churn)
================================================================================

WHAT THIS STAGE COVERS (from Minutes.txt):
  1. Business Objective Translation:
     a) Defining success criteria
     b) Mapping ML loss metrics directly to business impact:
        [Recall, AUC-ROC, Log-Loss] -> Revenue retention & churn prevention cost
  2. Feasibility & Constraints:
     a) Latency budgets (batch vs real-time)
     b) Hardware Infrastructure
     c) Regulations / Privacy Constraints:
        - GDPR: General Data Protection Regulation (European customers / PII masking)
        - HIPAA: Health Insurance Portability & Accountability Act (US Regulation)
  3. Real Dataset Scoping:
     - Automated inspection of actual Telco dataset schema, class imbalance, and volume
================================================================================
"""

import logging
from pathlib import Path
import numpy as np
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s]: %(message)s"
)
logger = logging.getLogger("Stage1_Scoping")

# Resolve Dataset Path
CURRENT_DIR = Path(__file__).resolve().parent
DATASET_PATH = CURRENT_DIR / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

print("=" * 80)
print("STAGE 1: PROBLEM DEFINITION & SCOPING")
print("=" * 80)

# =============================================================================
# 1. LOAD & INSPECT RAW DATASET FOR SCOPING
# =============================================================================
if not DATASET_PATH.exists():
    raise FileNotFoundError(f"[ERROR] Target dataset not found at: {DATASET_PATH}")

raw_df = pd.read_csv(DATASET_PATH)
n_rows, n_cols = raw_df.shape

logger.info(f"Loaded target dataset: {DATASET_PATH.name}")
logger.info(f"Raw shape: {n_rows:,} records across {n_cols} columns")

# =============================================================================
# 2. BUSINESS OBJECTIVE TRANSLATION
# =============================================================================
"""
Business Problem:
  Telecommunications companies face high customer acquisition costs ($300 - $600 per customer).
  Losing existing subscribers (churn) directly degrades recurring annual revenue (ARR).

Target Objective:
  Build a predictive classification model that identifies subscribers at high risk
  of churn prior to billing/renewal cycles, enabling targeted retention campaigns.

ML Formulation:
  Supervised Binary Classification
  Target: 'Churn' ('Yes' -> 1 [Positive Class], 'No' -> 0 [Negative Class])
"""

# Quantify Target Distribution from actual dataset
churn_counts = raw_df["Churn"].value_counts()
churn_pcts = raw_df["Churn"].value_counts(normalize=True) * 100

print("\n--- [1] BUSINESS METRIC & LOSS MAPPING ---")
print(f"Target Column        : 'Churn'")
print(f"Total Cohort Size    : {n_rows:,} subscribers")
print(f"Churned (Class 1)    : {churn_counts.get('Yes', 0):,} ({churn_pcts.get('Yes', 0):.2f}%)")
print(f"Retained (Class 0)   : {churn_counts.get('No', 0):,} ({churn_pcts.get('No', 0):.2f}%)")
print(f"Class Imbalance Ratio: ~{churn_pcts.get('No', 0)/churn_pcts.get('Yes', 1):.1f}:1 (Negative : Positive)")

print("""
Loss Metric to Business Impact Mapping:
  - False Negative (FN) Cost: High. Customer cancels service unmitigated ($500+ ARR loss).
  - False Positive (FP) Cost: Low. Wasted retention incentive/discount offer (~$25 - $50 cost).
  - Decision Rule: We prioritize RECALL over raw Precision because missing a churner 
    is 10x more costly than offering a promotion to a loyal subscriber.
""")

success_criteria = {
    "Primary ML Metric"       : "Recall (Class 1) >= 0.78  (Catch >= 78% of all churners)",
    "Secondary Metric"        : "AUC-ROC >= 0.84           (Consistent probability ranking)",
    "Calibration / Loss"      : "Log-Loss <= 0.42          (Well-calibrated probabilities for CRM)",
    "Precision Guardrail"     : "Precision >= 0.55         (Limit retention discount waste)"
}

for k, v in success_criteria.items():
    print(f"  * {k:<25}: {v}")

# =============================================================================
# 3. FEASIBILITY & CONSTRAINTS SPECIFICATION
# =============================================================================
print("\n--- [2] FEASIBILITY & CONSTRAINTS PROFILE ---")

# 2a. Latency Budgets
latency_constraints = {
    "Operational Mode"        : "Batch Scoring (Monthly billing cycle alignment)",
    "Batch SLA"               : "Process entire ~7,000 subscriber base within < 15 minutes",
    "Real-time Requirement"   : "None for Stage 1-4 baseline (Optional: REST microservice < 100ms)",
    "Retraining Cadence"      : "Monthly drift-triggered retraining pipeline"
}
for k, v in latency_constraints.items():
    print(f"  [Latency]   {k:<22}: {v}")

# 2b. Hardware & Infrastructure
memory_usage_mb = raw_df.memory_usage(deep=True).sum() / (1024 * 1024)
infra_profile = {
    "Raw In-Memory Footprint" : f"{memory_usage_mb:.2f} MB",
    "Target Environment"      : "Single standard compute node (4 CPU cores, 8 GB RAM)",
    "Storage Footprint"       : f"{(DATASET_PATH.stat().st_size / (1024 * 1024)):.2f} MB CSV on disk"
}
for k, v in infra_profile.items():
    print(f"  [Hardware]  {k:<22}: {v}")

# 2c. Regulatory & Privacy Governance
privacy_governance = {
    "GDPR (Europe)"           : "Applicable: 'customerID' is unique pseudonymous PII -> Must DROP from feature space",
    "Right to Explanation"    : "Mandatory: Model must support post-hoc XAI (SHAP / Tree SHAP / LIME)",
    "HIPAA (US Health)"       : "Not Applicable: Dataset contains consumer telecom telemetry only, no PHI/ePHI",
    "Data Minimization"       : "Exclude demographic identifiers that offer zero domain value"
}
for k, v in privacy_governance.items():
    print(f"  [Privacy]   {k:<22}: {v}")

# =============================================================================
# 4. DATA CONTRACT & SCHEMA AUDIT
# =============================================================================
print("\n--- [3] TELEMETRY SCHEMA & DOMAIN ATTRIBUTE AUDIT ---")
schema_summary = []
for col in raw_df.columns:
    sample_val = raw_df[col].dropna().iloc[0] if not raw_df[col].dropna().empty else None
    col_dtype = str(raw_df[col].dtype)
    n_unique = raw_df[col].nunique()
    
    # Identify role
    if col == "customerID":
        role = "PII Key (DROP)"
    elif col == "Churn":
        role = "Target (Binary)"
    elif col in ["MonthlyCharges", "TotalCharges", "tenure"]:
        role = "Continuous Numerical"
    elif col == "SeniorCitizen":
        role = "Binary Integer Flag"
    else:
        role = f"Categorical ({n_unique} levels)"
        
    schema_summary.append({
        "Column": col,
        "Dtype": col_dtype,
        "Uniques": n_unique,
        "Sample": str(sample_val)[:18],
        "Designation": role
    })

schema_df = pd.DataFrame(schema_summary)
print(schema_df.to_string(index=False))

# =============================================================================
# 5. FORMAL STAGE 1 DELIVERABLE: PROBLEM STATEMENT CARD
# =============================================================================
print("\n" + "=" * 80)
print("STAGE 1 PROBLEM STATEMENT CARD (Signed Off)")
print("=" * 80)
card = {
    "Project Name"            : "Enterprise Telecom Customer Churn Defense",
    "Dataset File"            : DATASET_PATH.name,
    "Cohort Size"             : f"{n_rows:,} rows, {n_cols} columns",
    "Target Definition"       : "Churn (Yes=1, No=0) | Baseline positive rate: 26.54%",
    "Primary Evaluation Metric": "Recall >= 0.78 & AUC-ROC >= 0.84",
    "Business Optimization"   : "Minimise customer loss while guarding retention budget",
    "Regulatory Compliance"   : "GDPR compliant (PII customerID stripped prior to modeling)",
    "Serving Architecture"    : "Batch inference prior to monthly customer billing cycle",
    "Downstream Pipeline"     : "Handoff to Stage 2: Data Ingestion & Low-Level Hygiene (2.py)"
}
for k, v in card.items():
    print(f"  {k:<28}: {v}")
print("=" * 80)
