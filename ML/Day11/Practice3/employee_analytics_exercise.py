"""
Title: Employee Productivity & Analytics Lifecycle 
Description: Fill in the TODO sections across the 5 lifecycle phases.

"""

# Step 0: Import necessary libraries
# TODO: Import pandas, numpy, scikit-learn LinearRegression, and metrics
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error


def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery & Data Setup (5 Marks)
    - Goal: Load 'employee_productivity.csv' and inspect structure.
    - Check for null values and print summary info.
    """
    print("\n[PHASE 1] Discovery & Data Setup")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    df = pd.read_csv("employee_productivity.csv")

    # TODO: Print first 5 rows and verify shape
    print("Dataset Shape:", df.shape)
    print("First 5 Rows:\n", df.head())

    # TODO: Check for missing values
    print("Missing Values:\n", df.isna().sum())
    return df


def phase_2_descriptive_statistics(df):
    """
    [Phase 2] Descriptive Statistics & Data Measures 
    - Goal: Compute measures of central tendency and dispersion 
      for 'Weekly_Tasks_Completed'.
    - Check for potential outliers using IQR method.
    """
    print("\n[PHASE 2] Descriptive Statistics ")
    print("-" * 65)
    # TODO: Calculate Mean, Median, Std Dev, and IQR for Weekly_Tasks_Completed
    tasks = df["Weekly_Tasks_Completed"]
    mean_val = tasks.mean()
    median_val = tasks.median()
    std_val = tasks.std()
    q75, q25 = np.percentile(tasks, [75, 25])
    iqr = q75 - q25

    print(f"Weekly_Tasks_Completed -> Mean: {mean_val:.2f}, Median: {median_val:.2f}, Std: {std_val:.2f}, IQR: {iqr:.2f}")

    # TODO: Identify any values falling outside 1.5 * IQR bounds
    lower_bound = q25 - 1.5 * iqr
    upper_bound = q75 + 1.5 * iqr
    outliers = df[(tasks < lower_bound) | (tasks > upper_bound)]
    print(f"Outliers outside [{lower_bound:.2f}, {upper_bound:.2f}]: {len(outliers)}")
    return df


def phase_3_bivariate_association(df):
    """
    [Phase 3] Bivariate Association & Correlation 
    - Goal: Examine relationships between Training Hours, Experience, 
      and Tasks Completed.
    - Compute Pearson correlation matrix.
    """
    print("\n[PHASE 3] Bivariate Association ")
    print("-" * 65)
    # TODO: Select numeric columns and compute Pearson correlation matrix
    numeric_df = df.select_dtypes(include=[np.number])
    corr_matrix = numeric_df.corr()
    print("Correlation Matrix:\n", corr_matrix)

    # TODO: Highlight the correlation between Training_Hours and Weekly_Tasks_Completed
    corr_val = corr_matrix.loc["Training_Hours", "Weekly_Tasks_Completed"]
    print(f"Correlation (Training_Hours vs Weekly_Tasks_Completed): {corr_val:.4f}")
    return df


def phase_4_predictive_modeling(df):
    """
    [Phase 4] Predictive Analytics & Regression Modeling 
    - Goal: Predict 'Weekly_Tasks_Completed' based on 'Training_Hours'.
    - Train a Simple Linear Regression model.
    """
    print("\n[PHASE 4] Predictive Modeling ")
    print("-" * 65)
    # TODO: Set X = df[['Training_Hours']] and y = df['Weekly_Tasks_Completed']
    X = df[["Training_Hours"]]
    y = df["Weekly_Tasks_Completed"]

    # TODO: Fit Linear Regression model and output slope & intercept
    model = LinearRegression()
    model.fit(X, y)
    print(f"Model Fitted -> Slope: {model.coef_[0]:.4f}, Intercept: {model.intercept_:.4f}")
    return model, X, y


def phase_5_evaluation_and_reporting(model, X, y, df):
    """
    [Phase 5] Evaluation & Prescriptive Recommendation (5 Marks)
    - Goal: Evaluate model using R-squared and MAE.
    - Provide operational HR recommendations based on data.
    """
    print("\n[PHASE 5] Evaluation & HR Recommendations (5 Marks)")
    print("-" * 65)
    # TODO: Calculate R2 score and Mean Absolute Error (MAE)
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    print(f"R2 Score: {r2:.4f}")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")

    # TODO: Print prescriptive action item for employee training investments
    print("HR Recommendation: Training hours have a positive correlation with weekly task throughput. Continue investing in structured employee onboarding and upskilling programs.")


def run_analytics_lifecycle():
    """
    Facade Orchestrator function.
    """
    print("=" * 65)
    print("STARTING EMPLOYEE ANALYTICS LIFECYCLE (Out of 40 Marks)")
    print("=" * 65)
    
    # Executing phases chronologically
    df = phase_1_discovery_and_setup()
    df = phase_2_descriptive_statistics(df)
    df = phase_3_bivariate_association(df)
    model, X, y = phase_4_predictive_modeling(df)
    phase_5_evaluation_and_reporting(model, X, y, df)


if __name__ == "__main__":
    run_analytics_lifecycle()
