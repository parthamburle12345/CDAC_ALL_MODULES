"""
Title: End-to-End Supervised Machine Learning Pipeline (Student Exercise)
Description: A modular Python exercise script for loading clean housing data, 
             identifying target/predictors, encoding categorical variables, 
             scaling features, training a regression model, evaluating performance, 
             and persisting the trained pipeline artifacts using joblib.

"""

# Step 0: Import necessary libraries
# TODO: Import pandas, numpy, train_test_split, StandardScaler, OneHotEncoder / ColumnTransformer,
#       LinearRegression (or RandomForestRegressor), mean_squared_error, mean_absolute_error, r2_score, and joblib
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def phase_1_discovery_and_target_identification():
    """
    [Phase 1] Discovery, Setup & Target/Predictor Identification 
    - Goal: Load 'housing_ml_data.csv' and inspect structure.
    - Drop non-predictive identifiers (e.g., 'house_id').
    - Identify Target feature (y) and Predictor features (X).
    """
    print("\n[PHASE 1] Discovery & Target Identification ")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    df = pd.read_csv("housing_ml_data.csv")

    # TODO: Separate target feature y ('price_usd') and predictor features X
    y = df["price_usd"]
    X = df.drop(columns=["price_usd"])

    # TODO: Drop ID column ('house_id')
    if "house_id" in X.columns:
        X = X.drop(columns=["house_id"])

    # TODO: Print shapes of X and y
    print(f"X shape: {X.shape} | y shape: {y.shape}")
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
    # TODO: Apply one-hot encoding or ordinal encoding to categorical columns
    cat_cols = ["location_type", "has_garage"]
    existing_cats = [col for col in cat_cols if col in X.columns]
    X = pd.get_dummies(X, columns=existing_cats, drop_first=True)

    # TODO: Add engineered features if needed (e.g., X['sqft_per_room'] = X['square_feet'] / X['num_bedrooms'])
    if "square_feet" in X.columns and "num_bedrooms" in X.columns:
        X["sqft_per_room"] = X["square_feet"] / X["num_bedrooms"].replace(0, 1)

    # TODO: Display head of transformed feature matrix
    print("Transformed Feature Matrix Head:\n", X.head())
    return X


def phase_3_scaling_and_train_test_split(X, y):
    """
    [Phase 3] Train-Test Split & Feature Scaling (10 Marks)
    - Goal: Split dataset into 80% Training and 20% Testing sets.
    - Fit StandardScaler on training data and transform both train and test sets.
    """
    print("\n[PHASE 3] Data Splitting & Feature Scaling ")
    print("-" * 65)
    # TODO: Perform train_test_split (test_size=0.2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
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
    [Phase 4] Model Training & Testing Metrics (10 Marks)
    - Goal: Train a regression algorithm (e.g., LinearRegression / RandomForest).
    - Predict on test set and calculate evaluation metrics (MAE, RMSE, R-squared).
    """
    print("\n[PHASE 4] Model Training & Test Set Evaluation ")
    print("-" * 65)
    # TODO: Instantiate regression model and fit on (X_train_scaled, y_train)
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    # TODO: Generate predictions on X_test_scaled
    y_pred = model.predict(X_test_scaled)

    # TODO: Compute MAE, RMSE, and R2_score
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    print(f"MAE  : {mae:.2f}")
    print(f"RMSE : {rmse:.2f}")
    print(f"R2   : {r2:.4f}")
    return model, {"mae": mae, "rmse": rmse, "r2": r2}


def phase_5_joblib_model_persistence(model, scaler, feature_names):
    """
    [Phase 5] Model Persistence & Future Deployment Setup (5 Marks)
    - Goal: Save the trained model, fitted scaler, and feature list using joblib.
    - Test loading saved artifacts to run an inference on a new sample.
    """
    print("\n[PHASE 5] Model Persistence with Joblib ")
    print("-" * 65)
    # TODO: Use joblib.dump() to save the model and scaler to disk (.joblib files)
    model_path = "housing_regressor.joblib"
    scaler_path = "housing_scaler.joblib"

    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    print("Regression Model and Scaler successfully saved using joblib.")

    # TODO: Load saved artifacts using joblib.load() and perform sample inference
    loaded_model = joblib.load(model_path)
    loaded_scaler = joblib.load(scaler_path)

    sample_house = pd.DataFrame([np.zeros(len(feature_names))], columns=feature_names)
    sample_scaled = loaded_scaler.transform(sample_house)
    predicted_price = loaded_model.predict(sample_scaled)[0]

    print(f"Sample House Predicted Valuation: ${predicted_price:,.2f}")


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
