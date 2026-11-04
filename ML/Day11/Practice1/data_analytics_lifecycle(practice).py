"""
Title: End-to-End Data Analytics Lifecycle
Description: A modular Python script demonstrating business discovery, 
             data preparation, exploration, statistics, and predictive modeling.
"""

# ==========================================
# IMPORTS (Libraries for Data, Stats, & Viz)
# ==========================================
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score,mean_absolute_error
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# SUB-STEP FUNCTIONS (The Lifecycle Phases)
# ==========================================

def phase_1_discovery_and_setup():
    """
    Module 1: Foundations, Business Understanding & Setup
    - Define business objective (e.g., Coffee Shop Revenue Analysis).
    - Load the 25-record real-world CSV dataset.
    - Initial inspection (head, info, missing values).
  
    """
    print("Executing Phase 1: Discovery & Data Setup...")
    # TODO: Load dataset using pandas
    df = pd.read_csv(r"D:\Engineering\CDAC_ALL_MODULES\ML\Day11\Practice1\coffee_shop_data.csv")

    # TODO: Perform basic inspection (shape, data types, missing values)
    print(df.shape)
    print(df.isna().sum())
    print(df.head())
    return df

def phase_2_descriptive_statistics(df):
    """
    Module 2: Descriptive Statistics & Data Measures
    - Calculate Central Tendency (Mean, Median, Mode).
    - Calculate Dispersion (Standard Deviation, Variance, IQR, Range).
    - Check Distribution Shape & Outliers.
  
    """
    print("Executing Phase 2: Descriptive Statistics & Measures...")
    # TODO: Compute summary statistics (mean, median, std, IQR)
    rev = df["Daily_Revenue_USD"]
    mean_val = rev.mean()
    median_val = rev.median()
    std_val = rev.std()
    iqr = rev.quantile(0.75) - rev.quantile(0.25)

    print(f"Mean: {mean_val}")
    print(f"median: {median_val}")
    print(f"STD: {std_val}")
    print(f"IQR: {iqr}")

    # TODO: Identify and handle any outliers
    q1 = rev.quantile(0.25)
    q3 = rev.quantile(0.75)

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers = df[(rev < lower_bound) | (rev > upper_bound)]
    print(len(outliers))
    return df


def phase_3_bivariate_association(df):
    """
    Module 4: Bivariate & Multivariate Association
    - Analyze relationships between variables (e.g., Marketing Spend vs. Revenue).
    - Compute Covariance and Pearson Correlation Matrix.
    - Generate exploratory visualizations (Scatter plots, Correlation heatmap).
  
    """
    print("Executing Phase 3: Bivariate Association & Visualization...")
    # TODO: Compute correlation matrix
    corr_df = df.select_dtypes(include=[np.number])
    corr_matrix = corr_df.corr()

    # TODO: Plot correlation heatmap and scatter plots
    plt.figure(figsize =(8,5))
    sns.heatmap(corr_matrix, annot = True, cmap = "coolwarm")
    plt.title("correlation heatmap")
    plt.show()

    mkt_rev_corr = corr_matrix.loc["Marketing_Spend_USD", "Daily_Revenue_USD"]
    print("Marketing vs Revenue Correlation:", mkt_rev_corr)
    
    
    
    plt.figure(figsize=(7, 5))
    sns.scatterplot(data=df, x="Marketing_Spend_USD", y="Daily_Revenue_USD")
    plt.title("Marketing Spend vs Daily Revenue")
    plt.show()

    return df



def phase_4_predictive_modeling(df):
    """
    Module 6 & 8: Predictive Analytics & Regression Modeling
    - Set up a simple predictive model (e.g., Simple Linear Regression).
    - Train the model on independent variables to predict revenue.
    - Establish a baseline evaluation.
   
    """
    print("Executing Phase 4: Predictive Modeling...")
    # TODO: Define features (X) and target (y)
    X = df[["Marketing_Spend_USD"]]
    y = df["Daily_Revenue_USD"]

    # TODO: Fit a simple linear regression model
    model = LinearRegression()
    model.fit(X,y)
    
    # TODO: Extract model coefficients and intercept
    slope = model.coef_[0]
    intercept = model.intercept_
    print(slope,intercept)
    return model,X,y



def phase_5_evaluation_and_reporting(model,X,y,df):
    """
    Module 6 & 7: Model Evaluation, Generalization & Business Decision
    - Evaluate model performance (e.g., R-squared, Mean Absolute Error).
    - Discuss generalization and overfitting risks on small data.
    - Translate technical findings into prescriptive business recommendations.
    [Allocation: 5 Marks]
    """
    print("Executing Phase 5: Evaluation & Business Action...")
    # TODO: Calculate evaluation metrics
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    mae = mean_absolute_error(y,y_pred)
    print(f"R2 Score: {r2:.4f}")
    print(f"MAE: {mae:.2f}")

    # TODO: Print final business recommendations based on findings
    print("Business Recommendation: Marketing spend has a strong positive impact on daily revenue; maintain targeted campaigns while monitoring customer acquisition ROI.")


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_analytics_lifecycle():
    """
    Facade function that coordinates the entire data analytics 
    lifecycle in chronological order.
    """
    print("=" * 60)
    print("STARTING COMPLETE DATA ANALYTICS LIFECYCLE (Out of 40 Marks)")
    print("=" * 60)
    
    df = phase_1_discovery_and_setup()
    print("-" * 60)
    
    df = phase_2_descriptive_statistics(df)
    print("-" * 60)
    
    df = phase_3_bivariate_association(df)
    print("-" * 60)
    
    model, X,y  = phase_4_predictive_modeling(df)
    print("-" * 60)
    
    phase_5_evaluation_and_reporting(model,X,y,df)
    
    print("=" * 60)
    print("ANALYTICS LIFECYCLE COMPLETED SUCCESSFULLY")
    print("=" * 60)


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_analytics_lifecycle()