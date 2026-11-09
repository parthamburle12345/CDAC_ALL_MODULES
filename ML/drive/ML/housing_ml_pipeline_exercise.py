"""
Title: End-to-End Supervised Machine Learning Pipeline (Student Exercise)
Description: A modular Python exercise script for loading clean housing data, 
             identifying target/predictors, encoding categorical variables, 
             scaling features, training a regression model, evaluating performance, 
             and persisting the trained pipeline artifacts using joblib.
"""

# Step 0: Import necessary libraries
import os
import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def phase_1_discovery_and_target_identification():
    """
    [Phase 1] Discovery, Setup & Target/Predictor Identification 
    - Goal: Load 'housing_ml_data.csv' and inspect structure.
    - Drop non-predictive identifiers (e.g., 'house_id').
    - Identify Target feature (y) and Predictor features (X).
    """
    print("\n[PHASE 1] Discovery & Target Identification ")
    print("-" * 65)
    
    # Load CSV with fallback paths
    
    
    df = pd.read_csv(f"./Day11/ML_Practice/Real_Estate/housing_ml_data.csv")

    print("Dataset Preview:\n", df.head())
    print("\nTotal Records & Features:", df.shape)

    # Separate target feature y ('price_usd') and predictor features X
    target_col = "price_usd"
    y = df[target_col]
    X = df.drop(columns=[target_col])

    # Drop non-predictive ID column if it exists
    if "house_id" in X.columns:
        X = X.drop(columns=["house_id"])

    print(f"Features shape (X): {X.shape}")
    print(f"Target shape   (y): {y.shape}")

    return X, y


def phase_2_feature_engineering_and_encoding(X):
    """
    [Phase 2] Categorical Encoding & Feature Engineering (10 Marks)
    - Goal: Encode categorical variables (e.g., 'location_type', 'has_garage').
    - Optionally create engineered interaction features (e.g., sqft per bedroom).
    """
    print("\n[PHASE 2] Feature Engineering & Categorical Encoding ")
    print("-" * 65)

    X = X.copy()

    # Feature Engineering: sqft per room / bedroom
    if "square_feet" in X.columns and "num_bedrooms" in X.columns:
        X["sqft_per_bedroom"] = X["square_feet"] / (X["num_bedrooms"] + 1e-5)
        print("Engineered feature added: 'sqft_per_bedroom'")

    # One-hot encoding categorical features
    X_encoded = pd.get_dummies(X, drop_first=True)

    print("\nEncoded Feature Matrix Head:")
    print(X_encoded.head())
    print(f"\nTotal Features after encoding: {X_encoded.shape[1]}")

    return X_encoded


def phase_3_scaling_and_train_test_split(X, y):
    """
    [Phase 3] Data Splitting & Feature Scaling (10 Marks)
    - Goal: Split dataset into 80% Training and 20% Testing sets.
    - Fit StandardScaler on training data and transform both train and test sets.
    """
    print("\n[PHASE 3] Data Splitting & Feature Scaling ")
    print("-" * 65)

    # 80/20 train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    print(f"Training set size: {X_train.shape[0]} rows")
    print(f"Testing set size : {X_test.shape[0]} rows")

    # Fit StandardScaler strictly on training set, then transform both
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


def phase_4_model_training_and_testing(X_train_scaled, X_test_scaled, y_train, y_test):
    """
    [Phase 4] Model Training & Testing Metrics (10 Marks)
    - Goal: Train a regression algorithm (LinearRegression).
    - Predict on test set and calculate evaluation metrics (MAE, RMSE, R-squared).
    """
    print("\n[PHASE 4] Model Training & Test Set Evaluation ")
    print("-" * 65)

    # Train model
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    # Predict on test set
    y_pred = model.predict(X_test_scaled)

    # Evaluation metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print(f"R-squared (R2) Score : {r2:.4f}")
    print(f"Mean Absolute Error (MAE): ${mae:,.2f}")
    print(f"Root Mean Squared Error (RMSE): ${rmse:,.2f}")

    metrics = {"MAE": mae, "RMSE": rmse, "R2": r2}
    return model, metrics


def phase_5_joblib_model_persistence(model, scaler, feature_names):
    """
    [Phase 5] Model Persistence & Future Deployment Setup (5 Marks)
    - Goal: Save the trained model, fitted scaler, and feature list using joblib.
    - Test loading saved artifacts to run an inference on a new sample.
    """
    print("\n[PHASE 5] Model Persistence with Joblib ")
    print("-" * 65)

    # 1. Save pipeline artifacts
    joblib.dump(model, "housing_regressor.joblib")
    joblib.dump(scaler, "housing_scaler.joblib")
    joblib.dump(feature_names, "housing_features.joblib")
    print("Saved artifacts: 'housing_regressor.joblib', 'housing_scaler.joblib', 'housing_features.joblib'")

    # 2. Reload saved artifacts
    loaded_model = joblib.load("housing_regressor.joblib")
    loaded_scaler = joblib.load("housing_scaler.joblib")
    loaded_features = joblib.load("housing_features.joblib")

    # 3. Perform a quick inference test using a sample row
    sample_house = np.zeros((1, len(loaded_features)))
    sample_scaled = loaded_scaler.transform(sample_house)
    predicted_price = loaded_model.predict(sample_scaled)[0]

    print("\nSample Inference Verification:")
    print(f"Predicted House Price for baseline sample: ${predicted_price:,.2f}")


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_ml_pipeline():
    """
    Facade function coordinating the entire machine learning pipeline.
    """
    print("=" * 65)
    print("STARTING END-TO-END MACHINE LEARNING LIFECYCLE ")
    print("=" * 65)

    # Executing phases chronologically
    X, y = phase_1_discovery_and_target_identification()
    X_encoded = phase_2_feature_engineering_and_encoding(X)
    X_tr_scaled, X_te_scaled, y_tr, y_te, scaler = phase_3_scaling_and_train_test_split(X_encoded, y)
    model, metrics = phase_4_model_training_and_testing(X_tr_scaled, X_te_scaled, y_tr, y_te)
    phase_5_joblib_model_persistence(model, scaler, X_encoded.columns.tolist())


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_ml_pipeline()