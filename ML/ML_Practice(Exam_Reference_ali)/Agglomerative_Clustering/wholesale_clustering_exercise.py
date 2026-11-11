"""
Title: Unsupervised B2B Client Segmentation with Agglomerative Clustering
Description: A modular Python exercise script for loading wholesale purchasing data, 
             scaling multi-dimensional expenditures, inducing an Agglomerative Hierarchical 
             Clustering model with Ward linkage, evaluating cluster cohesion via Silhouette score, 
             profiling client archetypes, and persisting pipeline artifacts using joblib.
"""

# =============================================================================
# Step 0: Import necessary libraries
# =============================================================================
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score


def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery, Setup & Feature Selection
    - Goal: Load 'wholesale_client_data.csv' and inspect structure.
    - Separate qualitative identifiers ('client_id', 'client_name') from numeric expenditures.
    - Select numeric features required for hierarchical clustering.
    """
    print("\n[PHASE 1] Discovery & Feature Selection")
    print("-" * 65)
    # Load CSV file using pandas
    df_original = pd.read_csv("wholesale_client_data.csv")

    # Select numerical spending features
    feature_cols = [
        "fresh_produce_k",
        "dairy_milk_k",
        "grocery_k",
        "frozen_goods_k",
        "delicatessen_k",
    ]
    X = df_original[feature_cols].copy()

    print("Loaded Wholesale Records:", len(df_original))
    print("Expenditure Features Head (k USD):\n", X.head())
    print("\nSummary Statistics:\n", X.describe().round(2))
    return X, df_original


def phase_2_feature_scaling(X):
    """
    [Phase 2] Unsupervised Feature Scaling
    - Goal: Fit StandardScaler on expenditure metrics to equalize Euclidean weightings.
    """
    print("\n[PHASE 2] Unsupervised Feature Scaling")
    print("-" * 65)
    # Initialize StandardScaler
    scaler = StandardScaler()

    # Fit and transform features X into X_scaled
    X_scaled = scaler.fit_transform(X)
    print("Features scaled successfully. Scaled shape:", X_scaled.shape)
    return X_scaled, scaler


def phase_3_agglomerative_model_induction(X_scaled, df_original):
    """
    [Phase 3] Agglomerative Clustering Model Induction
    - Goal: Instantiate AgglomerativeClustering with n_clusters=3 and Ward's linkage.
    - Fit model to scaled data and assign cluster labels back to dataset.
    """
    print("\n[PHASE 3] Agglomerative Clustering Model Induction")
    print("-" * 65)
    # Instantiate AgglomerativeClustering with Ward's linkage
    model = AgglomerativeClustering(n_clusters=3, metric="euclidean", linkage="ward")

    # Fit model and obtain cluster labels
    labels = model.fit_predict(X_scaled)

    # Attach cluster assignments back to original dataframe
    df_clustered = df_original.copy()
    df_clustered["cluster_id"] = labels

    print("Cluster value counts:\n", df_clustered["cluster_id"].value_counts())
    return model, labels, df_clustered


def phase_4_cluster_evaluation_and_profiling(X_scaled, labels, df_clustered):
    """
    [Phase 4] Cluster Evaluation & Business Profiling
    - Goal: Calculate Silhouette Score to measure cluster separation.
    - Calculate centroid spending profiles across clusters to define B2B client tiers.
    """
    print("\n[PHASE 4] Cluster Evaluation & Business Profiling")
    print("-" * 65)
    # Compute silhouette score
    score = silhouette_score(X_scaled, labels)
    print(f"Silhouette Score (k=3, Ward): {score:.4f}")

    # Compute mean expenditure profiles per cluster
    numeric_cols = [
        "fresh_produce_k",
        "dairy_milk_k",
        "grocery_k",
        "frozen_goods_k",
        "delicatessen_k",
    ]
    cluster_profiles = df_clustered.groupby("cluster_id")[numeric_cols].mean()
    print("\nCluster Centroid Profiles (Mean Spend in k USD):\n", cluster_profiles.round(2))

    print("\nSample Wholesale Client Cluster Assignments:")
    print(df_clustered[["client_name", "cluster_id"]].head(8))
    return cluster_profiles


def phase_5_joblib_model_persistence(model, scaler, feature_names, cluster_profiles):
    """
    [Phase 5] Unsupervised Model Persistence with Joblib
    - Goal: Save the trained Agglomerative model, scaler, and centroid profiles using joblib.
    - Test scoring a new incoming wholesale buyer by assigning to nearest cluster centroid.
    """
    print("\n[PHASE 5] Model Persistence with Joblib")
    print("-" * 65)
    # Define artifact paths
    model_path = "wholesale_agglomerative_model.joblib"
    scaler_path = "wholesale_scaler.joblib"
    profiles_path = "wholesale_centroids.joblib"

    # Serialize artifacts
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    joblib.dump(cluster_profiles, profiles_path)
    print("Agglomerative Model, Scaler, and Centroids successfully saved using joblib.")

    # Load artifacts using joblib.load()
    loaded_scaler = joblib.load(scaler_path)
    loaded_profiles = joblib.load(profiles_path)

    # Sample new buyer profile: High fresh produce & delicatessen spend (e.g. Italian Bistro)
    sample_buyer = pd.DataFrame(
        [[35.0, 6.5, 8.0, 2.5, 10.0]],
        columns=feature_names,
    )
    
    # Distance-based assignment to nearest cluster centroid
    scaled_sample = loaded_scaler.transform(sample_buyer)[0]
    scaled_centroids = loaded_scaler.transform(loaded_profiles[feature_names])
    distances = np.linalg.norm(scaled_centroids - scaled_sample, axis=1)
    assigned_cluster = int(np.argmin(distances))

    print(f"Sample Wholesale Buyer Inferred Segment: Cluster {assigned_cluster} (Nearest Centroid)")


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_clustering_pipeline():
    """
    Facade function coordinating the Agglomerative clustering pipeline.
    """
    print("=" * 65)
    print("STARTING HIERARCHICAL CLUSTERING LIFECYCLE (Agglomerative Ward)")
    print("=" * 65)
    
    # Executing phases chronologically
    X, df_original = phase_1_discovery_and_setup()
    X_scaled, scaler = phase_2_feature_scaling(X)
    model, labels, df_clustered = phase_3_agglomerative_model_induction(X_scaled, df_original)
    cluster_profiles = phase_4_cluster_evaluation_and_profiling(X_scaled, labels, df_clustered)
    phase_5_joblib_model_persistence(model, scaler, list(X.columns), cluster_profiles)


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_clustering_pipeline()

