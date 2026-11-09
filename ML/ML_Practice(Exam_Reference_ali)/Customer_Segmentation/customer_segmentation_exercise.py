"""
Title: Unsupervised Customer Segmentation Pipeline with K-Means (Student Exercise)
Description: A modular Python exercise script for loading customer behavioral data, 
             scaling features for distance-based algorithms, training a K-Means clustering model, 
             evaluating cluster cohesion, profiling segments, and persisting artifacts using joblib.
"""

# Step 0: Import necessary libraries
# TODO: Import pandas, numpy, StandardScaler from sklearn.preprocessing, 
#       KMeans from sklearn.cluster, silhouette_score from sklearn.metrics, and joblib
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery, Setup & Feature Selection
    - Goal: Load 'customer_segmentation_data.csv' and inspect structure.
    - Drop non-analytical identifiers (e.g., 'customer_id').
    - Select numeric feature subset for clustering (e.g., annual income, spending score).
    """
    print("\n[PHASE 1] Discovery & Feature Selection")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    df = pd.read_csv("customer_segmentation_data.csv")

    # TODO: Drop ID column ('customer_id')
    # TODO: Select relevant features for clustering (e.g., 'annual_income_k', 'spending_score_1_100', 'purchase_frequency_monthly')
    feature_cols = ["annual_income_k", "spending_score_1_100", "purchase_frequency_monthly"]
    X = df[feature_cols].copy()

    print("Loaded records:", len(df))
    print("Selected Clustering Features:\n", X.head())
    return X


def phase_2_feature_scaling(X):
    """
    [Phase 2] Unsupervised Feature Scaling
    - Goal: Initialize and fit StandardScaler on clustering features.
    - Unsupervised algorithms like K-Means rely heavily on Euclidean distance, making scaling mandatory.
    """
    print("\n[PHASE 2] Unsupervised Feature Scaling")
    print("-" * 65)
    # TODO: Initialize StandardScaler()
    scaler = StandardScaler()

    # TODO: Fit and transform features X into X_scaled
    X_scaled = scaler.fit_transform(X)
    print("Features scaled successfully. Shape:", X_scaled.shape)
    return X_scaled, scaler


def phase_3_kmeans_model_induction(X_scaled, X):
    """
    [Phase 3] K-Means Model Induction
    - Goal: Instantiate KMeans clustering model (e.g., setting n_clusters=3).
    - Fit model to scaled data and assign cluster labels back to dataset.
    """
    print("\n[PHASE 3] K-Means Model Induction & Labeling")
    print("-" * 65)
    # TODO: Instantiate KMeans(n_clusters=3, random_state=42)
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

    # TODO: Fit model and generate cluster labels (.fit_predict(X_scaled))
    labels = kmeans.fit_predict(X_scaled)
    df_clustered = X.copy()
    df_clustered["cluster_id"] = labels

    print("Cluster counts:\n", df_clustered["cluster_id"].value_counts())
    return kmeans, labels, df_clustered


def phase_4_cluster_evaluation_and_profiling(X_scaled, labels, df_clustered):
    """
    [Phase 4] Cluster Evaluation & Business Profiling
    - Goal: Compute Silhouette Score to measure cluster separation and cohesion.
    - Group original data by assigned cluster labels to profile customer segments.
    """
    print("\n[PHASE 4] Cluster Evaluation & Profiling")
    print("-" * 65)
    # TODO: Compute silhouette_score(X_scaled, labels)
    score = silhouette_score(X_scaled, labels)
    print(f"Silhouette Score (k=3): {score:.4f}")

    # TODO: Append cluster labels to original dataframe and compute group means to profile segments
    feature_cols = ["annual_income_k", "spending_score_1_100", "purchase_frequency_monthly"]
    segment_profiles = df_clustered.groupby("cluster_id")[feature_cols].mean()
    print("\nSegment Profiles (Mean Values per Cluster):\n", segment_profiles)


def phase_5_joblib_model_persistence(model, scaler, feature_names):
    """
    [Phase 5] Unsupervised Model Persistence with Joblib
    - Goal: Save the trained KMeans model and fitted scaler to disk using joblib.
    - Test loading artifacts to predict the cluster segment of a new customer.
    """
    print("\n[PHASE 5] Model Persistence with Joblib")
    print("-" * 65)
    # TODO: Save model, scaler, and feature list using joblib.dump()
    model_path = "customer_kmeans_model.joblib"
    scaler_path = "customer_kmeans_scaler.joblib"

    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    print("KMeans Model and Scaler successfully saved using joblib.")

    # TODO: Load artifacts using joblib.load() and assign a new customer profile to a cluster
    loaded_model = joblib.load(model_path)
    loaded_scaler = joblib.load(scaler_path)

    sample_customer = pd.DataFrame([[50, 60, 5]], columns=feature_names)
    sample_scaled = loaded_scaler.transform(sample_customer)
    assigned_cluster = loaded_model.predict(sample_scaled)[0]

    print(f"Sample Customer Assigned Segment: Cluster {assigned_cluster}")


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_clustering_pipeline():
    """
    Facade function coordinating the entire unsupervised segmentation pipeline.
    """
    print("=" * 65)
    print("STARTING UNSUPERVISED CLUSTERING LIFECYCLE (K-Means)")
    print("=" * 65)
    
    # Executing phases chronologically
    X = phase_1_discovery_and_setup()
    X_scaled, scaler = phase_2_feature_scaling(X)
    model, labels, df_clustered = phase_3_kmeans_model_induction(X_scaled, X)
    phase_4_cluster_evaluation_and_profiling(X_scaled, labels, df_clustered)
    phase_5_joblib_model_persistence(model, scaler, list(X.columns))


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_clustering_pipeline()
