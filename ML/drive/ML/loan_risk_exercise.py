"""
Title: Supervised Classification Pipeline for Loan Default Risk 
Description: A modular Python exercise script for loading clean loan applicant data, 
             identifying target/predictors, encoding categorical variables, 
             scaling features, training a Logistic Regression classifier, evaluating performance, 
             and persisting the trained pipeline artifacts using joblib.
"""

# Step 0: Import necessary libraries
import os
import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def phase_1_discovery_and_target_identification():
    """
    [Phase 1] Discovery, Setup & Target/Predictor Identification
    - Goal: Load 'loan_risk_data.csv' and inspect structure.
    - Drop non-predictive identifiers (e.g., 'applicant_id').
    - Identify Target feature (y: 'default_flag') and Predictor features (X).
    """
    print("\n[PHASE 1] Discovery & Target Identification")
    print("-" * 65)



    df = pd.read_csv(f"./Day11/ML_Practice/Bank_Loan_Risk/loan_risk_data.csv")

    print("Dataset Preview:\n", df.head())
    print("\nDataset Shape:", df.shape)

    # Separate target variable (y) and predictors (X)
    target_col = "default_flag"
    y = df[target_col]
    X = df.drop(columns=[target_col])

    # Drop non-predictive ID column if present
    if "applicant_id" in X.columns:
        X = X.drop(columns=["applicant_id"])

    # Inspect class balance of the target
    print("\nTarget Class Distribution:")
    print(y.value_counts())
    print("\nTarget Class Ratio:")
    print(y.value_counts(normalize=True).round(4))

    return X, y


def phase_2_feature_engineering_and_encoding(X):
    """
    [Phase 2] Categorical Encoding & Feature Engineering
    - Goal: Encode categorical variables (e.g., 'housing_status').
    - Optionally create engineered features (e.g., loan-to-income ratio).
    """
    print("\n[PHASE 2] Feature Engineering & Categorical Encoding")
    print("-" * 65)

    # Create copy to prevent SettingWithCopyWarning
    X = X.copy()

    # Optional Feature Engineering: loan-to-income ratio
    if "loan_amount_k" in X.columns and "annual_income_k" in X.columns:
        X["loan_to_income_ratio"] = X["loan_amount_k"] / (X["annual_income_k"] + 1e-5)
        print("Created feature: 'loan_to_income_ratio'")

    # One-hot encode categorical features (convert text columns into 0 and 1)
    X_encoded = pd.get_dummies(X, drop_first=True)

    print("\nTransformed Features Head:")
    print(X_encoded.head())
    print("\nTotal Features after encoding:", X_encoded.shape[1])

    return X_encoded


def phase_3_scaling_and_train_test_split(X, y):
    """
    [Phase 3] Train-Test Split & Feature Scaling
    - Goal: Split dataset into Training and Testing sets.
    - Fit StandardScaler on training data and transform both train and test sets.
    """
    print("\n[PHASE 3] Data Splitting & Feature Scaling")
    print("-" * 65)

    # Split dataset: 80% train, 20% test
    # stratify=y preserves the same percentage of defaults in train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    print(f"Training samples: {X_train.shape[0]} | Testing samples: {X_test.shape[0]}")

    # Scale numerical values to standard range (mean=0, std=1)
    scaler = StandardScaler()

    # Fit ONLY on training set, then transform both
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


def phase_4_model_training_and_testing(X_train_scaled, X_test_scaled, y_train, y_test):
    """
    [Phase 4] Model Training & Classification Metrics
    - Goal: Train a LogisticRegression model.
    - Predict on test set and calculate evaluation metrics (Accuracy, Confusion Matrix, Classification Report).
    """
    print("\n[PHASE 4] Model Training & Test Set Evaluation")
    print("-" * 65)

    # Train Logistic Regression model
    model = LogisticRegression(random_state=42)
    model.fit(X_train_scaled, y_train)

    # Make predictions on test set
    y_pred = model.predict(X_test_scaled)

    # Evaluation Metrics
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()

    print(f"Test Accuracy: {accuracy:.4f}\n")
    print("Confusion Matrix:")
    print(f"  [TN: {tn:4d}  |  FP: {fp:4d}]")
    print(f"  [FN: {fn:4d}  |  TP: {tp:4d}]\n")

    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    return model


def phase_5_joblib_model_persistence(model, scaler, feature_names):
    """
    [Phase 5] Model Persistence & Future Deployment Setup
    - Goal: Save the trained model, fitted scaler, and feature list using joblib.
    - Test loading saved artifacts to run an inference on a new applicant.
    """
    print("\n[PHASE 5] Model Persistence with Joblib")
    print("-" * 65)

    # 1. Save artifacts to disk
    joblib.dump(model, "loan_model.joblib")
    joblib.dump(scaler, "loan_scaler.joblib")
    joblib.dump(feature_names, "feature_names.joblib")
    print("Saved pipeline artifacts: 'loan_model.joblib', 'loan_scaler.joblib', 'feature_names.joblib'")

    # 2. Reload saved artifacts
    loaded_model = joblib.load("loan_model.joblib")
    loaded_scaler = joblib.load("loan_scaler.joblib")
    loaded_features = joblib.load("feature_names.joblib")

    # 3. Test sample inference with a single dummy applicant row
    sample_applicant = np.zeros((1, len(loaded_features)))
    sample_scaled = loaded_scaler.transform(sample_applicant)

    prediction = loaded_model.predict(sample_scaled)[0]
    probability = loaded_model.predict_proba(sample_scaled)[0][1]

    print("\nInference Verification Test:")
    print(f"Sample Applicant Default Prediction : {prediction} ({'Default' if prediction == 1 else 'No Default'})")
    print(f"Probability of Default             : {probability:.2%}")


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_ml_pipeline():
    """
    Facade function coordinating the entire loan risk classification pipeline.
    """
    print("=" * 65)
    print("STARTING LOAN RISK CLASSIFICATION LIFECYCLE (Logistic Regression)")
    print("=" * 65)

    # Executing phases chronologically
    X, y = phase_1_discovery_and_target_identification()
    X_encoded = phase_2_feature_engineering_and_encoding(X)
    X_tr_scaled, X_te_scaled, y_tr, y_te, scaler = phase_3_scaling_and_train_test_split(X_encoded, y)
    model = phase_4_model_training_and_testing(X_tr_scaled, X_te_scaled, y_tr, y_te)
    phase_5_joblib_model_persistence(model, scaler, X_encoded.columns.tolist())


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_ml_pipeline()