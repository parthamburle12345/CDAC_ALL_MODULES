"""
Title: Supervised Classification Pipeline for Loan Default Risk 
Description: A modular Python exercise script for loading clean loan applicant data, 
             identifying target/predictors, encoding categorical variables, 
             scaling features, training a Logistic Regression classifier, evaluating performance, 
             and persisting the trained pipeline artifacts using joblib.
"""

# Step 0: Import necessary libraries
# TODO: Import pandas, numpy, train_test_split, StandardScaler, 
#       LogisticRegression, accuracy_score, classification_report, confusion_matrix, and joblib
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def phase_1_discovery_and_target_identification():
    """
    [Phase 1] Discovery, Setup & Target/Predictor Identification
    - Goal: Load 'loan_risk_data.csv' and inspect structure.
    - Drop non-predictive identifiers (e.g., 'applicant_id').
    - Identify Target feature (y: 'default_flag') and Predictor features (X).
    """
    print("\n[PHASE 1] Discovery & Target Identification")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    df = pd.read_csv(r"D:\Engineering\CDAC_ALL_MODULES\ML\ML_Practice(Exam_Reference_ali)\Bank_Loan_Risk\loan_risk_data.csv")

    # TODO: Separate target feature y ('default_flag') and predictor features X
    y = df["default_flag"]
    X = df.drop(columns=["default_flag"])

    # TODO: Drop ID column ('applicant_id')
    if "applicant_id" in X.columns:
        X = X.drop(columns=["applicant_id"])

    # TODO: Inspect class distribution of target variable
    print("X shape:", X.shape, "| y shape:", y.shape)
    print("Target Class Distribution:\n", y.value_counts())
    return X, y


def phase_2_feature_engineering_and_encoding(X):
    """
    [Phase 2] Categorical Encoding & Feature Engineering
    - Goal: Encode categorical variables (e.g., 'housing_status').
    - Optionally create engineered features (e.g., loan-to-income ratio).
    """
    print("\n[PHASE 2] Feature Engineering & Categorical Encoding")
    print("-" * 65)
    X = X.copy()
    # TODO: Apply one-hot encoding to categorical columns using pd.get_dummies()
    X = pd.get_dummies(X, columns=["housing_status"], drop_first=True)

    # TODO: Add engineered features if desired (e.g., X['loan_to_income_ratio'] = X['loan_amount_k'] / X['annual_income_k'])
    X["loan_to_income_ratio"] = X["loan_amount_k"] / X["annual_income_k"]

    # TODO: Display head of transformed feature matrix
    print("Transformed Feature Matrix Head:\n", X.head())
    return X


def phase_3_scaling_and_train_test_split(X, y):
    """
    [Phase 3] Train-Test Split & Feature Scaling
    - Goal: Split dataset into Training and Testing sets.
    - Fit StandardScaler on training data and transform both train and test sets.
    """
    print("\n[PHASE 3] Data Splitting & Feature Scaling")
    print("-" * 65)
    # TODO: Perform train_test_split (test_size=0.2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # TODO: Initialize StandardScaler and scale numerical features
    scaler = StandardScaler()

    # TODO: Fit scaler on X_train, transform X_train and X_test
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print(f"Train set: {X_train_scaled.shape}, Test set: {X_test_scaled.shape}")
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


def phase_4_model_training_and_testing(X_train_scaled, X_test_scaled, y_train, y_test):
    """
    [Phase 4] Model Training & Classification Metrics
    - Goal: Train a LogisticRegression model.
    - Predict on test set and calculate evaluation metrics (Accuracy, Confusion Matrix, Classification Report).
    """
    print("\n[PHASE 4] Model Training & Test Set Evaluation")
    print("-" * 65)
    # TODO: Instantiate LogisticRegression(random_state=42) and fit on training data
    model = LogisticRegression(random_state=42)
    model.fit(X_train_scaled, y_train)

    # TODO: Generate predictions on test set
    y_pred = model.predict(X_test_scaled)

    # TODO: Compute accuracy_score and classification_report
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}")
    print("Confusion Matrix:\n", cm)
    print("Classification Report:\n", classification_report(y_test, y_pred))
    return model


def phase_5_joblib_model_persistence(model, scaler, feature_names):
    """
    [Phase 5] Model Persistence & Future Deployment Setup
    - Goal: Save the trained model, fitted scaler, and feature list using joblib.
    - Test loading saved artifacts to run an inference on a new applicant.
    """
    print("\n[PHASE 5] Model Persistence with Joblib")
    print("-" * 65)
    # TODO: Use joblib.dump() to save the model and scaler to disk (.joblib files)
    model_path = "loan_model.joblib"
    scaler_path = "loan_scaler.joblib"

    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    print("Model and Scaler successfully saved using joblib.")

    # TODO: Load saved artifacts using joblib.load() and perform sample inference
    loaded_model = joblib.load(model_path)
    loaded_scaler = joblib.load(scaler_path)

    sample_applicant = np.zeros((1, len(feature_names)))
    sample_scaled = loaded_scaler.transform(sample_applicant)
    prediction = loaded_model.predict(sample_scaled)[0]
    prob = loaded_model.predict_proba(sample_scaled)[0][1]

    print(f"Inference Test on Sample -> Predicted Default Flag: {prediction} (Default Probability: {prob:.4f})")


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
