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
    df = pd.read_csv(r"D:\Engineering\CDAC_ALL_MODULES\ML\Day11\Practice5\ecommerce_customer_data.csv")
    # TODO: Print first 5 rows and verify dataset shape
    print(df.shape)
    print(df.head())
    # TODO: Check for any missing values
    print(df.isna().sum())
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
    iqr = spend.quantile(0.75) - spend.quantile(0.25)

    print(f"Mean: {mean_val}")
    print(f"median: {median_val}")
    print(f"STD: {std_val}")
    print(F"VAriance: {var_val}")
    print(f"IQR: {iqr}")    
    # TODO: Identify any values falling outside 1.5 * IQR bounds
    q1 = spend.quantile(0.75)
    q2 = spend.quantile(0.25)

    lower_bound = q1 - 1.5*iqr
    upper_bound = q2 - 1.5*iqr
    outlier = [(lower_bound > spend) | (spend > upper_bound)]
    print(f"Number of outliers: {len(outlier)}")
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
    print(corr_matrix)

    # TODO: Highlight correlations involving Annual_Spend_USD
    print(corr_matrix["Annual_Spend_USD"])
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
    X = df[['Browsing_Minutes']]
    y = df['Annual_Spend_USD']

    # TODO: Fit Linear Regression model and output slope & intercept
    model = LinearRegression()
    model.fit(X,y)
    print("Slope (Coefficient):", model.coef_[0])
    print(f"intercept: {model.intercept_}")
    return model,X,y


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