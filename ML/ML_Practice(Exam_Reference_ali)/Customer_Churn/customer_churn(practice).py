"""
Title: Supervised Classification Pipeline with Random Forest (Practice Template)
Description: A modular Python exercise script for loading clean customer churn data, 
             identifying target/predictors, encoding categorical variables, 
             scaling features, training a Random Forest classifier, evaluating performance, 
             and persisting the trained pipeline artifacts using joblib.
"""

# =============================================================================
# Step 0: Import necessary libraries
# =============================================================================
# TODO 1: Import core data manipulation libraries: pandas as pd, numpy as np
# TODO 2: Import model selection utilities: train_test_split from sklearn.model_selection
# TODO 3: Import preprocessing scalers: StandardScaler from sklearn.preprocessing
# TODO 4: Import machine learning models: RandomForestClassifier from sklearn.ensemble
# TODO 5: Import evaluation metrics: accuracy_score, classification_report, confusion_matrix from sklearn.metrics
# TODO 6: Import model serialization: joblib
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def phase_1_discovery_and_target_identification():
    """
    [Phase 1] Discovery, Setup & Target/Predictor Identification
    - Goal: Load 'customer_churn_data.csv' and inspect structure.
    - Drop non-predictive identifiers (e.g., 'customer_id').
    - Identify Target feature (y: 'churn_flag') and Predictor features (X).
    """
    print("\n[PHASE 1] Discovery & Target Identification")
    print("-" * 65)
    # TODO 1: Load CSV dataset 'customer_churn_data.csv' using pd.read_csv()
    df = pd.read_csv(r"D:\Engineering\CDAC_ALL_MODULES\ML\ML_Practice(Exam_Reference_ali)\Customer_Churn\customer_churn_data.csv")
    
    # TODO 2: Separate target feature y ('churn_flag') and predictor feature matrix X:
    #         - y = df["churn_flag"]
    #         - X = df.drop(columns=["churn_flag"])
    y = df["churn_flag"]
    X = df.drop(columns=["churn_flag"])

    # TODO 3: Check and drop non-predictive ID column ('customer_id') from X if present:
    #         - if "customer_id" in X.columns: X = X.drop(columns=["customer_id"])
    if "customer_id" in X.columns:
        X = X.drop(columns=["customer_id"])

    # TODO 4: Inspect and display shape of X, shape of y, and class distribution of target:
    #         - print("X shape:", X.shape, "| y shape:", y.shape)
    #         - print("Target Class Distribution:\n", y.value_counts())
    print(y.shape)
    print(y.head(5))
    # TODO 5: Return feature matrix X and target series y
    return X,y


def phase_2_feature_engineering_and_encoding(X):
    """
    [Phase 2] Categorical Encoding & Feature Engineering
    - Goal: Encode categorical variables (e.g., 'contract_type', 'internet_service').
    - Optionally create engineered interaction features (e.g., charges per tenure month).
    """
    print("\n[PHASE 2] Feature Engineering & Categorical Encoding")
    print("-" * 65)
    # TODO 1: Create an explicit copy of feature matrix X (X = X.copy()) to prevent SettingWithCopy warnings
    X= (X.copy())

    # TODO 2: Identify categorical columns to encode: ['contract_type', 'internet_service']
    #         - Check which of these columns exist in X.columns:
    #           existing_cats = [col for col in ["contract_type", "internet_service"] if col in X.columns]
    #         - Apply One-Hot Encoding using pd.get_dummies(X, columns=existing_cats, drop_first=True)
    cat_cols = ["contract_type", "internet_service"]
    existing_cats = [col for col in cat_cols if col in X.columns]
    X = pd.get_dummies(X, columns=existing_cats, drop_first=True)


    # TODO 3: Engineer domain ratio feature 'avg_monthly_spend' if 'total_charges' and 'tenure_months' exist:
    #         - X["avg_monthly_spend"] = X["total_charges"] / X["tenure_months"].replace(0, 1)
    if "total_charges" in X.columns and "tenure_months" in X.columns:
        X["avg_monthly_spend"] = X["total_charges"] / X["tenure_months"].replace(0, 1)

    # TODO 4: Display head of transformed feature matrix:
    #         - print("Transformed Feature Matrix Head:\n", X.head())
    print(X.head())

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
    #         - X_train, X_test, y_train, y_test = train_test_split(
    #               X, y, test_size=0.2, random_state=42, stratify=y
    #           )
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=42, stratify=y)


    # TODO 2: Initialize StandardScaler() instance: scaler = StandardScaler()
    scaler = StandardScaler()
    # TODO 3: Fit scaler strictly on X_train, and transform both X_train and X_test:
    #         - X_train_scaled = scaler.fit_transform(X_train)
    #         - X_test_scaled = scaler.transform(X_test)
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # TODO 4: Print dimensions of train and test sets to verify consistency:
    #         - print(f"Train set: {X_train_scaled.shape}, Test set: {X_test_scaled.shape}")
    print(X_train_scaled)
    print(X_test_scaled)

    # TODO 5: Return (X_train_scaled, X_test_scaled, y_train, y_test, scaler)
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


def phase_4_model_training_and_testing(X_train_scaled, X_test_scaled, y_train, y_test):
    """
    [Phase 4] Random Forest Training & Classification Metrics
    - Goal: Train a RandomForestClassifier model.
    - Predict on test set and calculate evaluation metrics (Accuracy, Precision, Recall, F1).
    """
    print("\n[PHASE 4] Model Training & Test Set Evaluation")
    print("-" * 65)
    # TODO 1: Instantiate RandomForestClassifier(random_state=42, n_estimators=50)
    model = RandomForestClassifier(random_state=42, n_estimators=50)
    

    # TODO 2: Fit model on scaled training features and labels:
    #         - model.fit(X_train_scaled, y_train)
    model.fit(X_train_scaled, y_train)

    # TODO 3: Generate predictions on test set:
    #         - y_pred = model.predict(X_test_scaled)
    y_pred = model.predict(X_test_scaled)
    # TODO 4: Compute and print evaluation metrics:
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}")
    print("Confusion Matrix:\n", cm)
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # TODO 5: Return trained model
    return model


def phase_5_joblib_model_persistence(model, scaler, feature_names):
    """
    [Phase 5] Model Persistence & Future Deployment Setup
    - Goal: Save the trained model, fitted scaler, and feature list using joblib.
    - Test loading saved artifacts to run an inference on a new sample.
    """
    print("\n[PHASE 5] Model Persistence with Joblib")
    print("-" * 65)
    model_path = "customer_churn_model.joblib"
    scaler_path = "customer_churn_scaler.joblib"

    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    print("Random Forest Model and Scaler successfully saved using joblib.")

    # TODO: Load saved artifacts using joblib.load() and perform sample inference
    loaded_model = joblib.load(model_path)
    loaded_scaler = joblib.load(scaler_path)

    sample_customer = pd.DataFrame([np.zeros(len(feature_names))], columns=feature_names)
    sample_scaled = loaded_scaler.transform(sample_customer)
    prediction = loaded_model.predict(sample_scaled)[0]
    prob = loaded_model.predict_proba(sample_scaled)[0][1]

    print(f"Sample Customer Churn Prediction: {prediction} (Churn Probability: {prob:.4f})")




# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_ml_pipeline():
    """
    Facade function coordinating the entire classification pipeline.
    """
    print("=" * 65)
    print("STARTING SUPERVISED CLASSIFICATION LIFECYCLE (Random Forest)")
    print("=" * 65)
    
    # TODO: Uncomment and execute phases chronologically as you implement each function:
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

