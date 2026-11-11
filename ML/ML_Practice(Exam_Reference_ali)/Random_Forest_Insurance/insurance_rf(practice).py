="""
Title: Supervised Regression Pipeline with Random Forest Regressor (Practice Template)
Description: A modular Python exercise script for loading medical insurance data, 
             identifying target/predictors, encoding nominal categories, 
             scaling features, training an ensemble Random Forest regressor, 
             evaluating performance (MAE, RMSE, R-squared), inspecting feature importances, 
             and persisting the trained pipeline artifacts using joblib.
"""

# =============================================================================
# Step 0: Import necessary libraries
# =============================================================================
import numpy as np
import pandas as pd
import joblib 
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def phase_1_discovery_and_target_identification():
    """
    [Phase 1] Discovery, Setup & Target/Predictor Identification
    - Goal: Load 'insurance_charges_data.csv' and inspect structure.
    - Drop non-predictive identifiers (e.g., 'patient_id').
    - Identify Target feature (y: 'charges_usd') and Predictor features (X).
    """
    print("\n[PHASE 1] Discovery & Target Identification")
    print("-" * 65)
    # TODO 1: Load CSV file 'insurance_charges_data.csv' using pd.read_csv()
    #         - df = pd.read_csv("insurance_charges_data.csv")
    df = pd.read_csv(r"D:\Engineering\CDAC_ALL_MODULES\ML\ML_Practice(Exam_Reference_ali)\Random_Forest_Insurance\insurance_charges_data.csv")

    # TODO 2: Separate continuous target feature y ('charges_usd') and predictor matrix X:
    y = df["charges_usd"]
    X = df.drop(columns=["charges_usd"])

    # TODO 3: Check and drop ID column ('patient_id') from X if present:
    #         - if "patient_id" in X.columns: X = X.drop(columns=["patient_id"])
    if "patient_id" in X.columns:
        X = X.drop(columns=["patient_id"])

    # TODO 4: Inspect and display shape of X, shape of y, and summary statistics of charges:
    #         - print("X shape:", X.shape, "| y shape:", y.shape)
    #         - print("Target Charges Summary (USD):\n", y.describe())
    print(X.shape)
    print(y.shape)
    print(y.describe())
    # TODO 5: Return predictor feature matrix X and target series y
    return X,y


def phase_2_feature_engineering_and_encoding(X):
    """
    [Phase 2] Categorical Encoding & Feature Engineering
    - Goal: Encode categorical variables (e.g., 'smoker', 'region').
    - Optionally construct engineered interaction features (e.g., BMI x Smoker interaction).
    """
    print("\n[PHASE 2] Feature Engineering & Categorical Encoding")
    print("-" * 65)
    # TODO 1: Create an explicit copy of feature matrix X (X = X.copy())
    X = (X.copy())
    # TODO 2: Apply One-Hot Encoding to categorical columns ['smoker', 'region']:
    #         - cat_cols = ["smoker", "region"]
    #         - existing_cats = [col for col in cat_cols if col in X.columns]
    #         - X = pd.get_dummies(X, columns=existing_cats, drop_first=True)
    cat_cols = ["smoker", "region"]
    existing_cols = [col for col in cat_cols if col in X.columns]
    X = pd.get_dummies(X, columns=existing_cols,drop_first=True)

    # TODO 3: Convert any boolean columns created by get_dummies to integers (0/1):
    #         - bool_cols = X.select_dtypes(include=["bool"]).columns
    #         - X[bool_cols] = X[bool_cols].astype(int)
    bool_cols = X.select_dtypes(include=["bool"]).columns
    X[bool_cols] = X[bool_cols].astype(int)

    
    # TODO 4: Engineer interaction feature 'bmi_smoker_interaction' if columns exist:
    #         - if "smoker_yes" in X.columns and "bmi" in X.columns:
    #               X["bmi_smoker_interaction"] = X["bmi"] * X["smoker_yes"]
    if "smoker_yes" in X.columns and "bmi" in X.columns:
        X["bmi_smoker_interaction"] = X["bmi"] * X["smoker_yes"]


    # TODO 5: Display head of transformed feature matrix:
    #         - print("Transformed Feature Matrix Head:\n", X.head())
    print(X.head())

    # TODO 6: Return transformed feature matrix X
    return X


def phase_3_scaling_and_train_test_split(X, y):
    """
    [Phase 3] Train-Test Split & Feature Scaling
    - Goal: Split dataset into 80% Training and 20% Testing sets.
    - Fit StandardScaler on training data and transform both train and test sets.
    """
    print("\n[PHASE 3] Data Splitting & Feature Scaling")
    print("-" * 65)
    # TODO 1: Perform 80/20 train-test split:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # TODO 2: Initialize StandardScaler() instance: scaler = StandardScaler()
    scaler = StandardScaler()

    # TODO 3: Fit scaler strictly on X_train, and transform both X_train and X_test:
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # TODO 4: Print dimensions of train and test sets to verify consistency:
    print(X_train_scaled.shape)
    print(X_test_scaled.shape)

    # TODO 5: Return (X_train_scaled, X_test_scaled, y_train, y_test, scaler)
    return X_train_scaled,X_test_scaled,y_train,y_test,scaler


def phase_4_model_training_and_testing(X_train_scaled, X_test_scaled, y_train, y_test, feature_names):
    """
    [Phase 4] Random Forest Regressor Training & Evaluation Metrics
    - Goal: Train a RandomForestRegressor ensemble.
    - Predict on test set and calculate evaluation metrics (MAE, RMSE, R-squared).
    - Inspect feature importances.
    """
    print("\n[PHASE 4] Model Training & Test Set Evaluation")
    print("-" * 65)
    # TODO 1: Instantiate RandomForestRegressor(n_estimators=100, max_depth=6, random_state=42)
    model = RandomForestRegressor(n_estimators=100, max_depth=6, random_state=42)


    # TODO 2: Fit regressor on scaled training features and target labels:
    #         - model.fit(X_train_scaled, y_train)
    model.fit(X_train_scaled,y_train)

    # TODO 3: Generate predictions on test set:
    #         - y_pred = model.predict(X_test_scaled)
    y_pred = model.predict(X_test_scaled)

    # TODO 4: Compute regression evaluation metrics:
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Absolute Error (MAE) : ${mae:,.2f}")
    print(f"Root Mean Squared Error (RMSE) : ${rmse:,.2f}")
    print(f"R-squared Score (R2) : {r2:.4f}")

    # TODO 5: Inspect and display top feature importances:
    importances = pd.Series(model.feature_importances_, index=feature_names).sort_values(ascending=False)
    print("\nTop Feature Importances:\n", importances)

    # TODO 6: Return trained model
    return model



def phase_5_joblib_model_persistence(model, scaler, feature_names):
    """
    [Phase 5] Model Persistence & Future Deployment Setup
    - Goal: Save the trained model, fitted scaler, and feature list using joblib.
    - Test loading saved artifacts to run an inference on a new patient.
    """
    print("\n[PHASE 5] Model Persistence with Joblib")
    print("-" * 65)
    # TODO 1: Define artifact paths:
    #         - model_path = "insurance_rf_model.joblib"
    #         - scaler_path = "insurance_scaler.joblib"
    model_path = "insurance_rf_model.joblib"
    scaler_path = "insurance_scaler.joblib"

    # TODO 2: Save model and scaler to disk using joblib.dump():
    #         - joblib.dump(model, model_path)
    #         - joblib.dump(scaler, scaler_path)
    #         - print("Random Forest Regressor and Scaler successfully saved using joblib.")
    joblib.dump(model,model_path)
    joblib.dump(scaler,scaler_path)

    # TODO 3: Load artifacts using joblib.load():
    #         - loaded_model = joblib.load(model_path)
    #         - loaded_scaler = joblib.load(scaler_path)
    loaded_model = joblib.load(model_path)
    loaded_scaler = joblib.load(scaler_path)

    # TODO 4: Create a sample patient profile DataFrame matching feature_names with zeros:
    #         - sample_patient = pd.DataFrame([np.zeros(len(feature_names))], columns=feature_names)
    #         - Assign attributes: age=35, bmi=31.2, children=1, smoker_yes=1, bmi_smoker_interaction=31.2

    # TODO 5: Scale sample patient features using loaded_scaler.transform(sample_patient)
    sample_scaled = pd.DataFrame([np.zeros(len(feature_names))], columns=feature_names)
    predicted_charge = loaded_model.predict(sample_scaled)[0]
    print(predicted_charge)

    # TODO 6: Predict estimated medical charges:
    #         - predicted_charge = loaded_model.predict(sample_scaled)[0]
    #         - print(f"Sample Patient Predicted Annual Medical Charges: ${predicted_charge:,.2f}")
    


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_ml_pipeline():
    """
    Facade function coordinating the entire Random Forest regression pipeline.
    """
    print("=" * 65)
    print("STARTING RANDOM FOREST REGRESSION LIFECYCLE (Insurance Cost)")
    print("=" * 65)
    
    # TODO: Uncomment and execute phases chronologically as you implement each function:
    X, y = phase_1_discovery_and_target_identification()
    X_encoded = phase_2_feature_engineering_and_encoding(X)
    X_tr_scaled, X_te_scaled, y_tr, y_te, scaler = phase_3_scaling_and_train_test_split(X_encoded, y)
    model = phase_4_model_training_and_testing(X_tr_scaled, X_te_scaled, y_tr, y_te, X_encoded.columns.tolist())
    # phase_5_joblib_model_persistence(model, scaler, X_encoded.columns.tolist())


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_ml_pipeline()

