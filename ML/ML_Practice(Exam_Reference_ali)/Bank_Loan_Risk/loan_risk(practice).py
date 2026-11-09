"""
Title: Supervised Classification Pipeline for Loan Default Risk (Practice Template)
Description: A modular Python exercise script for loading clean loan applicant data, 
             identifying target/predictors, encoding categorical variables, 
             scaling features, training a Logistic Regression classifier, evaluating performance, 
             and persisting the trained pipeline artifacts using joblib.
"""

# =============================================================================
# Step 0: Import necessary libraries
# =============================================================================
# TODO 1: Import core data manipulation libraries: pandas as pd, numpy as np
# TODO 2: Import model selection utilities: train_test_split from sklearn.model_selection
# TODO 3: Import preprocessing scalers: StandardScaler from sklearn.preprocessing
# TODO 4: Import machine learning models: LogisticRegression from sklearn.linear_model
# TODO 5: Import evaluation metrics: accuracy_score, classification_report, confusion_matrix from sklearn.metrics
# TODO 6: Import model serialization: joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib


def phase_1_discovery_and_target_identification():
    """
    [Phase 1] Discovery, Setup & Target/Predictor Identification
    - Goal: Load 'loan_risk_data.csv' and inspect structure.
    - Drop non-predictive identifiers (e.g., 'applicant_id').
    - Identify Target feature (y: 'default_flag') and Predictor features (X).
    """
    print("\n[PHASE 1] Discovery & Target Identification")
    print("-" * 65)
    # TODO 1: Load CSV file 'loan_risk_data.csv' using pd.read_csv()
    #         - df = pd.read_csv("loan_risk_data.csv")
    df = pd.read_csv(r"D:\Engineering\CDAC_ALL_MODULES\ML\ML_Practice(Exam_Reference_ali)\Bank_Loan_Risk\loan_risk_data.csv")

    # TODO 2: Separate target classification column y ('default_flag') and predictor matrix X:
    #         - y = df["default_flag"]
    #         - X = df.drop(columns=["default_flag"])
    y = df["default_flag"]
    X = df.drop(columns=["default_flag"])
    # TODO 3: Drop non-predictive ID column ('applicant_id') from X if present:
    #         - if "applicant_id" in X.columns: X = X.drop(columns=["applicant_id"])
    if "applicant_id" in X.columns:
        X = X.drop(columns=["applicant_id"])


    # TODO 4: Inspect and display shape of X, shape of y, and target class balance:
    #         - print("X shape:", X.shape, "| y shape:", y.shape)
    #         - print("Target Class Distribution:\n", y.value_counts())
    print(X.shape)
    print(y.value_counts())

    # TODO 5: Return predictor feature matrix X and target series y
    return X,y

def phase_2_feature_engineering_and_encoding(X):
    """
    [Phase 2] Categorical Encoding & Feature Engineering
    - Goal: Encode categorical variables (e.g., 'housing_status').
    - Optionally create engineered features (e.g., loan-to-income ratio).
    """
    print("\n[PHASE 2] Feature Engineering & Categorical Encoding")
    print("-" * 65)
    # TODO 1: Create an explicit copy of feature matrix X (X = X.copy())
    X = (X.copy())

    # TODO 2: Apply One-Hot Encoding to categorical column 'housing_status':
    #         - X = pd.get_dummies(X, columns=["housing_status"], drop_first=True)
    X = pd.get_dummies(X, columns=["housing_status"], drop_first=True)

    # TODO 3: Construct engineered domain ratio feature 'loan_to_income_ratio':
    #         - X["loan_to_income_ratio"] = X["loan_amount_k"] / X["annual_income_k"]
    X["loan_to_income_ratio"] = X["loan_amount_k"] / X["annual_income_k"]

    # TODO 4: Display head of transformed feature matrix:
    #         - print("Transformed Feature Matrix Head:\n", X.head())
    print(X.head(5))

    # TODO 5: Return transformed feature matrix X
    return X


def phase_3_scaling_and_train_test_split(X, y):
    """
    [Phase 3] Train-Test Split & Feature Scaling
    - Goal: Split dataset into Training and Testing sets.
    - Fit StandardScaler on training data and transform both train and test sets.
    """
    print("\n[PHASE 3] Data Splitting & Feature Scaling")
    print("-" * 65)
    # TODO 1: Split dataset into 80% train and 20% test folds with stratification on y:
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, stratify=y, random_state=42)


    # TODO 2: Initialize StandardScaler() instance: scaler = StandardScaler()
    scaler = StandardScaler()
    
    # TODO 3: Fit scaler strictly on X_train, and transform both X_train and X_test:
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # TODO 4: Print dimensions of train and test sets to verify consistency:
    #         - print(f"Train set: {X_train_scaled.shape}, Test set: {X_test_scaled.shape}")
    print(X_test_scaled.shape)
    # TODO 5: Return (X_train_scaled, X_test_scaled, y_train, y_test, scaler)
    return X_train_scaled,X_test_scaled,y_train,y_test,scaler


def phase_4_model_training_and_testing(X_train_scaled, X_test_scaled, y_train, y_test):
    """
    [Phase 4] Model Training & Classification Metrics
    - Goal: Train a LogisticRegression model.
    - Predict on test set and calculate evaluation metrics (Accuracy, Confusion Matrix, Classification Report).
    """
    print("\n[PHASE 4] Model Training & Test Set Evaluation")
    print("-" * 65)
    # TODO 1: Instantiate LogisticRegression(random_state=42)
    lr = LogisticRegression(random_state=42)
    # TODO 2: Fit model on scaled training features and target labels:
    #         - model.fit(X_train_scaled, y_train)
    lr.fit(X_train_scaled,y_train)
    # TODO 3: Generate predictions on test set:
    #         - y_pred = model.predict(X_test_scaled)
    y_pred = lr.predict(X_test_scaled)
    # TODO 4: Compute and display evaluation metrics:
    #         - acc = accuracy_score(y_test, y_pred)
    #         - cm = confusion_matrix(y_test, y_pred)
    #         - print(f"Accuracy: {acc:.4f}")
    #         - print("Confusion Matrix:\n", cm)
    #         - print("Classification Report:\n", classification_report(y_test, y_pred))
    acc = accuracy_score(y_test,y_pred)
    cm = confusion_matrix(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}")
    print("Confusion Matrix:\n", cm)
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # TODO 5: Return trained model
    return lr

def phase_5_joblib_model_persistence(lr, scaler, feature_names):
    
    """
    [Phase 5] Model Persistence & Future Deployment Setup
    - Goal: Save the trained model, fitted scaler, and feature list using joblib.
    - Test loading saved artifacts to run an inference on a new applicant.
    """
    print("\n[PHASE 5] Model Persistence with Joblib")
    print("-" * 65)
    # TODO 1: Define artifact paths:
    lr_path = "loan_lr.joblib"
    scaler_path = "load_scaler.joblib"

    # TODO 2: Save model and scaler to disk using joblib.dump():
    joblib.dump(lr,lr_path)
    joblib.dump(scaler,scaler_path)

    # TODO 3: Load artifacts using joblib.load():
    loaded_lr = joblib.load(lr_path)
    loaded_scaler = joblib.load(scaler_path)
    # TODO 4: Create a sample applicant array matching feature dimensions:
    sample_application = np.zeros((1, len(feature_names)))

    # TODO 5: Scale sample applicant using loaded_scaler.transform(sample_applicant)
    sample_scaled = loaded_scaler.transform(sample_application)

    # TODO 6: Predict default flag and default probability for the sample:
    prediction = loaded_lr.predict(sample_scaled)[0]
    prob = loaded_lr.predict_proba(sample_scaled)[0][1]

    print(prediction)
    print(prob)

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
    
    # TODO: Uncomment and execute phases chronologically as you implement each function:
    X, y = phase_1_discovery_and_target_identification()
    X_encoded = phase_2_feature_engineering_and_encoding(X)
    X_tr_scaled, X_te_scaled, y_tr, y_te, scaler = phase_3_scaling_and_train_test_split(X_encoded, y)
    lr = phase_4_model_training_and_testing(X_tr_scaled, X_te_scaled, y_tr, y_te)
    phase_5_joblib_model_persistence(lr, scaler, X_encoded.columns.tolist())


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_ml_pipeline()













