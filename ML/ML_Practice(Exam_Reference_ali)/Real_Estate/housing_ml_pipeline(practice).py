"""
Title: End-to-End Supervised Machine Learning Pipeline (Practice Template)
Description: A modular Python exercise script for loading clean housing data, 
             identifying target/predictors, encoding categorical variables, 
             scaling features, training a regression model, evaluating performance, 
             and persisting the trained pipeline artifacts using joblib.
"""

# =============================================================================
# Step 0: Import necessary libraries
# =============================================================================
# TODO 1: Import core data manipulation libraries: pandas as pd, numpy as np
# TODO 2: Import model selection utilities: train_test_split from sklearn.model_selection
# TODO 3: Import preprocessing scalers: StandardScaler from sklearn.preprocessing
# TODO 4: Import machine learning models: LinearRegression from sklearn.linear_model
# TODO 5: Import evaluation metrics: mean_squared_error, mean_absolute_error, r2_score from sklearn.metrics
# TODO 6: Import model serialization: joblib
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
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
    # TODO 1: Load CSV file 'housing_ml_data.csv' using pd.read_csv()
    #         - df = pd.read_csv("housing_ml_data.csv")
    df = pd.read_csv(r"D:\Engineering\CDAC_ALL_MODULES\ML\ML_Practice(Exam_Reference_ali)\Real_Estate\housing_ml_data.csv")

    # TODO 2: Separate continuous target feature y ('price_usd') and predictor matrix X:
    #         - y = df["price_usd"]
    #         - X = df.drop(columns=["price_usd"])
    y = df["price_usd"]
    X = df.drop(columns=["price_usd"])

    # TODO 3: Check and drop ID column ('house_id') from X if present:
    #         - if "house_id" in X.columns: X = X.drop(columns=["house_id"])
    if "house_id" in X.columns:
        X = X.drop(columns=["house_id"])

    # TODO 4: Print dimensions of X and y:
    #         - print(f"X shape: {X.shape} | y shape: {y.shape}")
    print(X.shape)
    print(y.shape)
    # TODO 5: Return predictor matrix X and continuous target series y
    return X,y


def phase_2_feature_engineering_and_encoding(X):
    """
    [Phase 2] Categorical Encoding & Feature Engineering (10 Marks)
    - Goal: Encode categorical variables (e.g., 'location_type', 'has_garage').
    - Optionally create engineered interaction features (e.g., sqft per bedroom).
    """
    print("\n[PHASE 2] Feature Engineering & Categorical Encoding ")
    print("-" * 65)
    # TODO 1: Create an explicit copy of feature matrix X (X = X.copy())
    X = (X.copy())

    # TODO 2: Identify categorical columns to encode: ['location_type', 'has_garage']
    #         - Check which of these columns exist in X.columns:
    #           existing_cats = [col for col in ["location_type", "has_garage"] if col in X.columns]
    #         - Apply One-Hot Encoding using pd.get_dummies(X, columns=existing_cats, drop_first=True)
    cat_cols = ["location_type","has_garage"]
    existing_cats = [col for col in cat_cols if col in X.columns]
    X = pd.get_dummies(X,columns=existing_cats, drop_first=True)

    # TODO 3: Construct engineered feature 'sqft_per_room' if 'square_feet' and 'num_bedrooms' exist:
    #         - X["sqft_per_room"] = X["square_feet"] / X["num_bedrooms"].replace(0, 1)
    if "square_feet" in X.columns and "num_bedrooms" in X.columns:
        X["sqft_per_room"] = X["square_feet"] / X["num_bedrooms"].replace(0, 1)

    # TODO 4: Display head of transformed feature matrix:
    #         - print("Transformed Feature Matrix Head:\n", X.head())
    print(X.head())
    # TODO 5: Return transformed feature matrix X
    return X


def phase_3_scaling_and_train_test_split(X, y):
    """
    [Phase 3] Train-Test Split & Feature Scaling (10 Marks)
    - Goal: Split dataset into 80% Training and 20% Testing sets.
    - Fit StandardScaler on training data and transform both train and test sets.
    """
    print("\n[PHASE 3] Data Splitting & Feature Scaling ")
    print("-" * 65)
    # TODO 1: Perform 80/20 train-test split:
    #         - X_train, X_test, y_train, y_test = train_test_split(
    #               X, y, test_size=0.2, random_state=42)
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    # TODO 2: Initialize StandardScaler() instance: scaler = StandardScaler()
    scaler = StandardScaler()

    # TODO 3: Fit scaler strictly on X_train, and transform both X_train and X_test:
    #         - X_train_scaled = scaler.fit_transform(X_train)
    #         - X_test_scaled = scaler.transform(X_test)
    X_train_scaled  = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # TODO 4: Print dimensions of train and test sets to verify consistency:
    #         - print(f"Train set: {X_train_scaled.shape}, Test set: {X_test_scaled.shape}")
    print(X_train_scaled)
    print(X_test_scaled)

    # TODO 5: Return (X_train_scaled, X_test_scaled, y_train, y_test, scaler)
    return X_train_scaled,X_test_scaled,y_train,y_test, scaler



def phase_4_model_training_and_testing(X_train_scaled, X_test_scaled, y_train, y_test):
    """
    [Phase 4] Model Training & Testing Metrics (10 Marks)
    - Goal: Train a regression algorithm (e.g., LinearRegression / RandomForest).
    - Predict on test set and calculate evaluation metrics (MAE, RMSE, R-squared).
    """
    print("\n[PHASE 4] Model Training & Test Set Evaluation ")
    print("-" * 65)
    # TODO 1: Instantiate LinearRegression() model: model = LinearRegression()
    model = LinearRegression()

    # TODO 2: Fit model on scaled training features and target valuations:
    #         - model.fit(X_train_scaled, y_train)
    model.fit(X_train_scaled,y_train)

    # TODO 3: Generate predictions on test set:
    #         - y_pred = model.predict(X_test_scaled)
    y_pred = model.predict(X_test_scaled)

    # TODO 4: Compute regression evaluation metrics:
    #         - mae = mean_absolute_error(y_test, y_pred)
    #         - rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    #         - r2 = r2_score(y_test, y_pred)
    #         - print(f"MAE  : {mae:.2f}")
    #         - print(f"RMSE : {rmse:.2f}")
    #         - print(f"R2   : {r2:.4f}")
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    print(f"MAE  : {mae:.2f}")
    print(f"RMSE : {rmse:.2f}")
    print(f"R2   : {r2:.4f}")


    # TODO 5: Return model and metrics dictionary: (model, {"mae": mae, "rmse": rmse, "r2": r2})
    return model, {"mae": mae, "rmse": rmse, "r2": r2}


def phase_5_joblib_model_persistence(model, scaler, feature_names):
    """
    [Phase 5] Model Persistence & Future Deployment Setup (5 Marks)
    - Goal: Save the trained model, fitted scaler, and feature list using joblib.
    - Test loading saved artifacts to run an inference on a new sample.
    """
    print("\n[PHASE 5] Model Persistence with Joblib ")
    print("-" * 65)
    # TODO 1: Define artifact paths:
    #         - model_path = "housing_regressor.joblib"
    #         - scaler_path = "housing_scaler.joblib"

    # TODO 2: Save model and scaler to disk using joblib.dump():
    #         - joblib.dump(model, model_path)
    #         - joblib.dump(scaler, scaler_path)
    #         - print("Regression Model and Scaler successfully saved using joblib.")

    # TODO 3: Load artifacts using joblib.load():
    #         - loaded_model = joblib.load(model_path)
    #         - loaded_scaler = joblib.load(scaler_path)

    # TODO 4: Create a sample house DataFrame with zeros matching feature_names:
    #         - sample_house = pd.DataFrame([np.zeros(len(feature_names))], columns=feature_names)

    # TODO 5: Scale sample house features using loaded_scaler.transform(sample_house)

    # TODO 6: Predict estimated valuation:
    #         - predicted_price = loaded_model.predict(sample_scaled)[0]
    #         - print(f"Sample House Predicted Valuation: ${predicted_price:,.2f}")
    pass


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
    
    # TODO: Uncomment and execute phases chronologically as you implement each function:
    X, y = phase_1_discovery_and_target_identification()
    X_encoded = phase_2_feature_engineering_and_encoding(X)
    X_tr_scaled, X_te_scaled, y_tr, y_te, scaler = phase_3_scaling_and_train_test_split(X_encoded, y)
    model, metrics = phase_4_model_training_and_testing(X_tr_scaled, X_te_scaled, y_tr, y_te)
    # phase_5_joblib_model_persistence(model, scaler, X_encoded.columns.tolist())


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_ml_pipeline()

