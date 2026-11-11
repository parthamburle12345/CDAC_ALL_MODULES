"""
=============================================================================
CDAC ADVANCED MACHINE LEARNING - SURPRISE CODING TEST (PAPER 1 - SOLUTION)
=============================================================================
Candidate Name: Parth Amburle (Reference Solution Key)
Problem Domain: HR Analytics - Employee Attrition & Retention Risk Modeling
Algorithm     : Supervised Classification (Logistic Regression)
Artifacts     : attrition_model.joblib, attrition_scaler.joblib
=============================================================================
"""

# =============================================================================
# STEP 0: IMPORT REQUIRED LIBRARIES (5 Marks)
# =============================================================================
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# =============================================================================
# PHASE 1: DATA INGESTION & TARGET SEPARATION (10 Marks)
# =============================================================================
def phase_1_data_ingestion_and_target_separation():
    """
    [Phase 1] Data Ingestion & Target Separation
    - Load the CSV dataset 'employee_attrition_data.csv'.
    - Inspect dataset dimensions and column data types.
    - Separate the target classification column ('attrition') from predictors.
    - Drop non-predictive identifier columns.
    - Inspect the class distribution of the target variable.
    """
    print("\n[PHASE 1] Data Ingestion & Target Separation")
    print("-" * 65)
    # Step 1: Read 'employee_attrition_data.csv' into a pandas DataFrame
    df = pd.read_csv("employee_attrition_data.csv")

    # Step 2: Separate target variable (y) and predictor feature matrix (X)
    y = df["attrition"]
    X = df.drop(columns=["attrition"])

    # Step 3: Remove unique employee identifier ('emp_id') from feature matrix X
    if "emp_id" in X.columns:
        X = X.drop(columns=["emp_id"])

    # Step 4: Print shape of X, shape of y, and class balance of target (value counts)
    print("X shape:", X.shape, "| y shape:", y.shape)
    print("Target Class Distribution (0 = Stay, 1 = Leave):\n", y.value_counts())

    # Step 5: Return feature matrix X and target vector y
    return X, y


# =============================================================================
# PHASE 2: CATEGORICAL ENCODING & FEATURE PREPARATION (10 Marks)
# =============================================================================
def phase_2_categorical_encoding(X):
    """
    [Phase 2] Categorical Encoding & Feature Preparation
    - Identify categorical/nominal columns ('overtime', 'department').
    - Apply One-Hot Encoding to convert categories into numeric representation.
    - Avoid the dummy variable trap (drop first category).
    - Ensure resulting matrix contains only numerical data types.
    """
    print("\n[PHASE 2] Categorical Encoding & Feature Preparation")
    print("-" * 65)
    # Step 1: Create a safe copy of feature matrix X
    X = X.copy()

    # Step 2: Identify nominal categorical features requiring encoding
    cat_cols = ["overtime", "department"]
    existing_cats = [col for col in cat_cols if col in X.columns]

    # Step 3: Perform One-Hot Encoding with first category dropped
    X = pd.get_dummies(X, columns=existing_cats, drop_first=True)

    # Step 4: Ensure all encoded columns are numeric integers (0/1)
    bool_cols = X.select_dtypes(include=["bool"]).columns
    X[bool_cols] = X[bool_cols].astype(int)

    # Step 5: Display the head of the transformed feature matrix
    print("Transformed Feature Matrix Head:\n", X.head())

    # Step 6: Return transformed feature matrix X
    return X


# =============================================================================
# PHASE 3: TRAIN-TEST SPLIT & FEATURE SCALING (10 Marks)
# =============================================================================
def phase_3_split_and_scale(X, y):
    """
    [Phase 3] Train-Test Split & Feature Scaling
    - Partition dataset into 80% training and 20% testing sets.
    - Use stratified sampling to preserve the target class balance.
    - Fit StandardScaler strictly on the training set.
    - Transform both training and testing sets to prevent data leakage.
    """
    print("\n[PHASE 3] Train-Test Split & Feature Scaling")
    print("-" * 65)
    # Step 1: Split data into 80% train and 20% test folds with stratification on y (random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Step 2: Initialize a standard scaler instance
    scaler = StandardScaler()

    # Step 3: Fit scaler on training set, then transform both train and test sets
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Step 4: Print dimensions of the scaled training and testing partitions
    print(f"Train partition: {X_train_scaled.shape}, Test partition: {X_test_scaled.shape}")

    # Step 5: Return X_train_scaled, X_test_scaled, y_train, y_test, scaler
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


# =============================================================================
# PHASE 4: MODEL TRAINING & PERFORMANCE EVALUATION (15 Marks)
# =============================================================================
def phase_4_model_training_and_evaluation(X_train_scaled, X_test_scaled, y_train, y_test):
    """
    [Phase 4] Model Training & Performance Evaluation
    - Instantiate and train a supervised classifier (Logistic Regression).
    - Generate predictions on the holdout test set.
    - Calculate and print Accuracy Score.
    - Print the Confusion Matrix.
    - Display the comprehensive Classification Report (Precision, Recall, F1).
    """
    print("\n[PHASE 4] Model Training & Performance Evaluation")
    print("-" * 65)
    # Step 1: Instantiate classification model with random_state=42
    model = LogisticRegression(random_state=42)

    # Step 2: Fit model on scaled training data and labels
    model.fit(X_train_scaled, y_train)

    # Step 3: Predict class labels for the holdout test set
    y_pred = model.predict(X_test_scaled)

    # Step 4: Compute and print the Accuracy Score
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    cr = classification_report(y_test, y_pred)

    print(f"Accuracy Score: {acc:.4f} ({acc * 100:.2f}%)")
    print("Confusion Matrix:\n", cm)
    print("Classification Report:\n", cr)

    # Step 7: Return the trained model
    return model


# =============================================================================
# PHASE 5: MODEL PERSISTENCE & INFERENCE TEST (10 Marks)
# =============================================================================
def phase_5_model_persistence_and_inference(model, scaler, feature_names):
    """
    [Phase 5] Model Persistence & Sample Inference
    - Save the trained classifier and fitted scaler to disk as .joblib files.
    - Deserialize artifacts from disk.
    - Construct a synthetic employee profile to simulate real-world scoring.
    - Scale the sample and predict attrition status along with class probability.
    """
    print("\n[PHASE 5] Model Persistence with Joblib")
    print("-" * 65)
    # TODO: Use joblib.dump() to save the model and scaler to disk (.joblib files)
    model_path = "attrition_model.joblib"
    scaler_path = "attrition_scaler.joblib"

    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    print("Logistic Regression Model and Scaler successfully saved using joblib.")

    # TODO: Load saved artifacts using joblib.load() and perform sample inference
    loaded_model = joblib.load(model_path)
    loaded_scaler = joblib.load(scaler_path)

    sample_employee = pd.DataFrame([np.zeros(len(feature_names))], columns=feature_names)
    sample_scaled = loaded_scaler.transform(sample_employee)
    prediction = loaded_model.predict(sample_scaled)[0]
    prob = loaded_model.predict_proba(sample_scaled)[0][1]

    print(f"Sample Employee Attrition Prediction: {prediction} (Attrition Probability: {prob:.4f})")


# =============================================================================
# THE FACADE FUNCTION (Exam Orchestrator)
# =============================================================================
def run_exam_pipeline():
    """
    Coordinates and executes the entire machine learning pipeline chronologically.
    """
    print("=" * 65)
    print("STARTING CDAC ML CODING EXAM (PAPER 1 - ATTRITION RISK - SOLUTION)")
    print("=" * 65)
    
    X, y = phase_1_data_ingestion_and_target_separation()
    X_encoded = phase_2_categorical_encoding(X)
    X_tr_scaled, X_te_scaled, y_tr, y_te, scaler = phase_3_split_and_scale(X_encoded, y)
    model = phase_4_model_training_and_evaluation(X_tr_scaled, X_te_scaled, y_tr, y_te)
    phase_5_model_persistence_and_inference(model, scaler, X_encoded.columns.tolist())


# =============================================================================
# MAIN GUARD
# =============================================================================
if __name__ == "__main__":
    run_exam_pipeline()

