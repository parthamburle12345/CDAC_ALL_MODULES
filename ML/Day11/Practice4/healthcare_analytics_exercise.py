"""
Title: Healthcare Patient Analytics Lifecycle 
Description: Fill in the TODO sections across the 5 lifecycle phases using 
             'patient_health_data.csv'.

"""

# Step 0: Import necessary libraries
# TODO: Import pandas, numpy, LinearRegression from sklearn.linear_model, and evaluation metrics
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error


def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery & Data Setup 
    - Goal: Load 'patient_health_data.csv' and inspect structure.
    - Check for null values and print summary info.
    """
    print("\n[PHASE 1] Discovery & Data Setup")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    df = pd.read_csv("patient_health_data.csv")

    # TODO: Print first 5 rows and verify dataset shape
    print("Dataset Shape:", df.shape)
    print("First 5 Rows:\n", df.head())

    # TODO: Check for any missing values
    print("Missing Values:\n", df.isna().sum())
    return df


def phase_2_descriptive_statistics(df):
    """
    [Phase 2] Descriptive Statistics & Data Measures 
    - Goal: Compute measures of central tendency and dispersion 
      for 'Systolic_BP'.
    - Check for potential outliers using the IQR method.
    """
    print("\n[PHASE 2] Descriptive Statistics ")
    print("-" * 65)
    # TODO: Calculate Mean, Median, Std Dev, Variance, and IQR for Systolic_BP
    sbp = df["Systolic_BP"]
    mean_val = sbp.mean()
    median_val = sbp.median()
    std_val = sbp.std()
    var_val = sbp.var()
    q75, q25 = np.percentile(sbp, [75, 25])
    iqr = q75 - q25

    print(f"Systolic_BP -> Mean: {mean_val:.2f}, Median: {median_val:.2f}, Std: {std_val:.2f}, Variance: {var_val:.2f}, IQR: {iqr:.2f}")

    # TODO: Identify any values falling outside 1.5 * IQR bounds
    lower_bound = q25 - 1.5 * iqr
    upper_bound = q75 + 1.5 * iqr
    outliers = df[(sbp < lower_bound) | (sbp > upper_bound)]
    print(f"Outliers outside [{lower_bound:.2f}, {upper_bound:.2f}]: {len(outliers)}")
    return df


def phase_3_bivariate_association(df):
    """
    [Phase 3] Bivariate Association & Correlation 
    - Goal: Examine relationships between BMI, Daily Steps, and Systolic BP.
    - Compute Pearson correlation matrix.
    """
    print("\n[PHASE 3] Bivariate Association ")
    print("-" * 65)
    # TODO: Select numeric columns and compute Pearson correlation matrix
    numeric_df = df.select_dtypes(include=[np.number])
    corr_matrix = numeric_df.corr()
    print("Correlation Matrix:\n", corr_matrix)

    # TODO: Highlight correlations involving Systolic_BP
    print("Correlations with Systolic_BP:\n", corr_matrix["Systolic_BP"])
    return df


def phase_4_predictive_modeling(df):
    """
    [Phase 4] Predictive Analytics & Regression Modeling 
    - Goal: Predict 'Systolic_BP' based on 'BMI'.
    - Train a Simple Linear Regression model.
    """
    print("\n[PHASE 4] Predictive Modeling ")
    print("-" * 65)
    # TODO: Set X = df[['BMI']] and y = df['Systolic_BP']
    X = df[["BMI"]]
    y = df["Systolic_BP"]

    # TODO: Fit Linear Regression model and output slope & intercept
    model = LinearRegression()
    model.fit(X, y)
    print(f"Model Fitted -> Slope: {model.coef_[0]:.4f}, Intercept: {model.intercept_:.4f}")
    return model, X, y


def phase_5_evaluation_and_reporting(model, X, y, df):
    """
    [Phase 5] Evaluation & Prescriptive Recommendations (5 Marks)
    - Goal: Evaluate model performance using R-squared and MAE.
    - Provide prescriptive clinical recommendations based on findings.
    """
    print("\n[PHASE 5] Evaluation & Clinical Action (5 Marks)")
    print("-" * 65)
    # TODO: Calculate R2 score and Mean Absolute Error (MAE)
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    print(f"R2 Score: {r2:.4f}")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")

    # TODO: Print prescriptive clinical action items
    print("Clinical Recommendation: Higher BMI indicates elevated Systolic BP risk. Recommend targeted lifestyle, nutrition, and cardiovascular monitoring interventions.")


def run_analytics_lifecycle():
    """
    Facade Orchestrator function.
    """
    print("=" * 65)
    print("STARTING HEALTHCARE ANALYTICS LIFECYCLE ")
    print("=" * 65)
    
    # Executing phases chronologically
    df = phase_1_discovery_and_setup()
    df = phase_2_descriptive_statistics(df)
    df = phase_3_bivariate_association(df)
    model, X, y = phase_4_predictive_modeling(df)
    phase_5_evaluation_and_reporting(model, X, y, df)


if __name__ == "__main__":
    run_analytics_lifecycle()
