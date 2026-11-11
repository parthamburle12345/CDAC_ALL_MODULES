"""
=============================================================================
CDAC ADVANCED MACHINE LEARNING - SURPRISE CODING TEST (PAPER 1)
=============================================================================
Candidate Name: Parth Amburle
Exam Duration : 45 Minutes
Total Marks   : 50 Marks
Problem Domain: HR Analytics - Employee Attrition & Retention Risk Modeling
Algorithm     : Supervised Classification (Logistic Regression / Random Forest)

NOTE: A fully executable master solution is available in:
      paper1_solution.py
=============================================================================
"""

# =============================================================================
# STEP 0: IMPORT REQUIRED LIBRARIES (5 Marks)
# =============================================================================
# TODO 1: Import core data manipulation and numeric libraries
# TODO 2: Import model selection utility for dataset splitting
# TODO 3: Import preprocessing scaler for standardizing features
# TODO 4: Import supervised classification model (LogisticRegression or RandomForestClassifier)
# TODO 5: Import classification evaluation metrics (accuracy, confusion matrix, classification report)
# TODO 6: Import joblib for model serialization
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
    # TODO 1: Read 'employee_attrition_data.csv' into a pandas DataFrame
    df = pd.read_csv(r"D:\Engineering\CDAC_ALL_MODULES\ML\ML_Practice(Exam_Reference_ali)\Coding_Exam_1\employee_attrition_data.csv")

    # TODO 2: Separate target variable (y) and predictor feature matrix (X)
    y = df["attrition"]
    X = df.drop(columns=["attrition"])

    # TODO 3: Remove unique employee identifier ('emp_id') from feature matrix X
    if "emp_id" in X.columns:
        X = X.drop(columns=["emp_id"])

    # TODO 4: Print shape of X, shape of y, and class balance of target (value counts)
    print("X shape:", X.shape)
    print("y shape:", y.shape)
    print("Class balance (attrition):\n", y.value_counts())

    # TODO 5: Return feature matrix X and target vector y
    return X,y


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
    # TODO 1: Create a safe copy of feature matrix X
    X = X.copy()

    # TODO 2: Identify nominal categorical features requiring encoding
    cat_cols = ["overtime","department"]
    existing_cats = [col for col in cat_cols if col in X.columns]

    # TODO 3: Perform One-Hot Encoding with first category dropped
    X = pd.get_dummies(X, columns=existing_cats, drop_first=True)

    # TODO 4: Ensure all encoded columns are numeric (0/1)
    bool_cats = X.select_dtypes(include=["bool"]).columns
    X[bool_cats] = X[bool_cats].astype(int)

    # TODO 5: Display the head of the transformed feature matrix
    print(X.head())
    # TODO 6: Return transformed feature matrix X
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
    # TODO 1: Split data into 80% train and 20% test folds with stratification on y (random_state=42)
    X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.2 ,random_state=42,stratify=y)

    # TODO 2: Initialize a standard scaler instance
    scaler = StandardScaler()
    
    # TODO 3: Fit scaler on training set, then transform both train and test sets
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # TODO 4: Print dimensions of the scaled training and testing partitions
    print(X_train_scaled.shape)
    print(X_test_scaled.shape)

    # TODO 5: Return X_train_scaled, X_test_scaled, y_train, y_test, scaler
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler   


# =============================================================================
# PHASE 4: MODEL TRAINING & PERFORMANCE EVALUATION (15 Marks)
# =============================================================================
def phase_4_model_training_and_evaluation(X_train_scaled, X_test_scaled, y_train, y_test):
    """
    [Phase 4] Model Training & Performance Evaluation
    - Instantiate and train a supervised classifier (Logistic Regression or Random Forest).
    - Generate predictions on the holdout test set.
    - Calculate and print Accuracy Score.
    - Print the Confusion Matrix.
    - Display the comprehensive Classification Report (Precision, Recall, F1).
    """
    print("\n[PHASE 4] Model Training & Performance Evaluation")
    print("-" * 65)
    # TODO 1: Instantiate classification model with random_state=42
    model = LogisticRegression(random_state =42)

    # TODO 2: Fit model on scaled training data and labels
    model.fit(X_train_scaled,y_train)
    # TODO 3: Predict class labels for the holdout test set
    y_pred = model.predict(X_test_scaled)

    # TODO 4: Compute and print the Accuracy Score
    acc = accuracy_score(y_test,y_pred)
    # TODO 5: Display the Confusion Matrix
    cm = confusion_matrix(y_test,y_pred)
    # TODO 6: Print the Classification Report showing Precision, Recall, and F1-score
    cr = classification_report(y_test,y_pred)

    print(f"Accuracy Score:{acc}")
    print(f"confusion matrix: {cm}")
    print(f"Classification Report:\n{cr}")

    # TODO 7: Return the trained model
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
    # TODO 1: Define artifact filenames for model and scaler (.joblib)
    model_path = "attrition_model.joblib"
    scaler_path = "attrition_scaler.joblib"
    
    # TODO 2: Serialize and save model and scaler using joblib.dump()
    joblib.dump(model, model_path)
    joblib.dump(scaler,scaler_path)

    # TODO 3: Load saved artifacts back into memory using joblib.load()
    loaded_model = joblib.load(model_path)
    loaded_scaler = joblib.load(scaler_path)

    # TODO 4: Create a synthetic test employee profile matching feature_names
    sample_employee = pd.DataFrame([np.zeros(len(feature_names))],columns=feature_names)

    # TODO 5: Scale the synthetic test sample using the loaded scaler
    sample_scaled = loaded_scaler.transform(sample_employee)

    # TODO 6: Predict attrition outcome (class and probability) and print the prediction
    prediction = loaded_model.predict(sample_scaled)[0]
    prob = loaded_model.predict_proba(sample_scaled)[0][1]

    print(prediction)
    print(prob)


# =============================================================================
# THE FACADE FUNCTION (Exam Orchestrator)
# =============================================================================
def run_exam_pipeline():
    """
    Coordinates and executes the entire machine learning pipeline.
    Uncomment phases sequentially as you complete each implementation.
    """
    print("=" * 65)
    print("STARTING CDAC ML CODING EXAM (PAPER 1 - ATTRITION RISK)")
    print("=" * 65)
    
    # TODO: Uncomment and execute phases chronologically as you implement each function:
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
