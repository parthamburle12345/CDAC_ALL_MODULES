"""
Title: Healthcare Classification Lifecycle
Description: Module 7 Supervised Segmentation & Classification Exercise.

"""

# Step 0: Import necessary libraries
# TODO: Import pandas, LogisticRegression from sklearn.linear_model, accuracy_score, and confusion_matrix
import pandas as pd 
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix



def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery & Data Setup 
    - Goal: Load 'patient_classification_data.csv' and inspect class distribution.
    """
    print("\n[PHASE 1] Discovery & Data Setup")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    df = pd.read_csv(r"D:\Engineering\CDAC_ALL_MODULES\ML\Day11\Practice4\patient_classification_data.csv")


    # TODO: Check class balance of 'High_Risk_Hypertension' (value_counts)
    print("Dataset shape:",df.shape)
    print("Class Distrubution of High_Risk_Hypertension:", df['High_Risk_Hypertension'].value_counts())
    return df


def phase_2_supervised_segmentation(df):
    """
    [Phase 2] Supervised Segmentation & Feature Selection 
    - Goal: Analyze feature differences between risk groups.
    """
    print("\n[PHASE 2] Supervised Segmentation")
    print("-" * 65)
    # TODO: Group data by 'High_Risk_Hypertension' and calculate mean of numeric features (BMI, Daily_Steps)
    group_mean = df.groupby('High_Risk_Hypertension')[["BMI", "Daily_Steps"]].mean()
    print(group_mean)
    return df

def phase_3_classification_modeling(df):
    """
    [Phase 3] Classification Model Induction 
    - Goal: Train a Logistic Regression model to classify high-risk patients.
    """
    print("\n[PHASE 3] Classification Modeling")
    print("-" * 65)
    # TODO: Define features X = df[['BMI', 'Daily_Steps']] and target y = df['High_Risk_Hypertension']
    X = df[["BMI", "Daily_Steps"]]
    y = df["High_Risk_Hypertension"]

    
    # TODO: Fit LogisticRegression model
    model = LogisticRegression()
    model.fit(X,y)
    print("Model trained successfully")
    return model,X,y


def phase_4_model_evaluation(model, X, y):
    """
    [Phase 4] Evaluating Classifiers & Generalization 
    - Goal: Compute Accuracy and Confusion Matrix.
    - Provide clinical prescriptive actions.
    """
    print("\n[PHASE 4] Model Evaluation & Clinical Action")
    print("-" * 65)
    # TODO: Generate predictions and calculate accuracy_score and confusion_matrix
    y_pred = model.predict(X)
    acc = accuracy_score(y,y_pred)
    cm = confusion_matrix(y,y_pred)
    print(f"Accuracy Matrix: {acc}")
    print(f"Confusion Matrix: {cm}")

    
    
    # TODO: Print prescriptive clinical intervention recommendations
    print("Clinical Recommendation: Supervised segmentation accurately distinguishes high-risk hypertension patients; initiate early preventative care protocols.")



def run_analytics_lifecycle():
    """
    Facade Orchestrator function.
    """
    print("=" * 65)
    print("STARTING HEALTHCARE CLASSIFICATION LIFECYCLE ")
    print("=" * 65)
    
    df = phase_1_discovery_and_setup()
    df = phase_2_supervised_segmentation(df)
    model, X, y = phase_3_classification_modeling(df)
    phase_4_model_evaluation(model, X, y)


if __name__ == "__main__":
    run_analytics_lifecycle()