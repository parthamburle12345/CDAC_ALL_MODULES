"""
Title: E-Commerce Customer Analytics Lifecycle 
Description: Fill in the TODO sections across the 5 lifecycle phases using 
             'ecommerce_customer_data.csv'.

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
    - Goal: Load 'ecommerce_customer_data.csv' and inspect structure.
    - Check for null values and print summary info.
    """
    print("\n[PHASE 1] Discovery & Data Setup")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    df = pd.read_csv("ecommerce_customer_data.csv")

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
      for 'Annual_Spend_USD'.
    - Check for potential outliers using the IQR method.
    """
    print("\n[PHASE 2] Descriptive Statistics")
    print("-" * 65)
    # TODO: Calculate Mean, Median, Std Dev, Variance, and IQR for Annual_Spend_USD
    spend = df["Annual_Spend_USD"]
    mean_val = spend.mean()
    median_val = spend.median()
    std_val = spend.std()
    var_val = spend.var()
    q75, q25 = np.percentile(spend, [75, 25])
    iqr = q75 - q25

    print(f"Annual_Spend_USD -> Mean: {mean_val:.2f}, Median: {median_val:.2f}, Std: {std_val:.2f}, Variance: {var_val:.2f}, IQR: {iqr:.2f}")

    # TODO: Identify any values falling outside 1.5 * IQR bounds
    lower_bound = q25 - 1.5 * iqr
    upper_bound = q75 + 1.5 * iqr
    outliers = df[(spend < lower_bound) | (spend > upper_bound)]
    print(f"Outliers outside [{lower_bound:.2f}, {upper_bound:.2f}]: {len(outliers)}")
    return df


def phase_3_bivariate_association(df):
    """
    [Phase 3] Bivariate Association & Correlation 
    - Goal: Examine relationships between Browsing Minutes, Items in Cart, and Annual Spend.
    - Compute Pearson correlation matrix.
    """
    print("\n[PHASE 3] Bivariate Association")
    print("-" * 65)
    # TODO: Select numeric columns and compute Pearson correlation matrix
    numeric_df = df.select_dtypes(include=[np.number])
    corr_matrix = numeric_df.corr()
    print("Correlation Matrix:\n", corr_matrix)

    # TODO: Highlight correlations involving Annual_Spend_USD
    print("Correlations with Annual_Spend_USD:\n", corr_matrix["Annual_Spend_USD"])
    return df


def phase_4_predictive_modeling(df):
    """
    [Phase 4] Predictive Analytics & Regression Modeling 
    - Goal: Predict 'Annual_Spend_USD' based on 'Browsing_Minutes'.
    - Train a Simple Linear Regression model.
    """
    print("\n[PHASE 4] Predictive Modeling")
    print("-" * 65)
    # TODO: Set X = df[['Browsing_Minutes']] and y = df['Annual_Spend_USD']
    X = df[["Browsing_Minutes"]]
    y = df["Annual_Spend_USD"]

    # TODO: Fit Linear Regression model and output slope & intercept
    model = LinearRegression()
    model.fit(X, y)
    print(f"Model Fitted -> Slope: {model.coef_[0]:.4f}, Intercept: {model.intercept_:.4f}")
    return model, X, y


def phase_5_evaluation_and_reporting(model, X, y, df):
    """
    [Phase 5] Evaluation & Prescriptive Recommendations 
    - Goal: Evaluate model performance using R-squared and MAE.
    - Provide prescriptive business recommendations based on findings.
    """
    print("\n[PHASE 5] Evaluation & Business Action")
    print("-" * 65)
    # TODO: Calculate R2 score and Mean Absolute Error (MAE)
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    print(f"R2 Score: {r2:.4f}")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")

    # TODO: Print prescriptive marketing action items
    print("Marketing Recommendation: Browsing minutes strongly predict annual customer spend. Invest in UI/UX engagement strategies and personalized recommendations to increase session duration.")


def run_analytics_lifecycle():
    """
    Facade Orchestrator function.
    """
    print("=" * 65)
    print("STARTING E-COMMERCE ANALYTICS LIFECYCLE ")
    print("=" * 65)
    
    # Executing phases chronologically
    df = phase_1_discovery_and_setup()
    df = phase_2_descriptive_statistics(df)
    df = phase_3_bivariate_association(df)
    model, X, y = phase_4_predictive_modeling(df)
    phase_5_evaluation_and_reporting(model, X, y, df)


if __name__ == "__main__":
    run_analytics_lifecycle()
