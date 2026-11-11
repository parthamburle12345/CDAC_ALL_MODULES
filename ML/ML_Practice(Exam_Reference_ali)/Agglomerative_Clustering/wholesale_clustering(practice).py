"""
Title: Unsupervised B2B Client Segmentation with Agglomerative Clustering (Practice Template)
Description: A modular Python exercise script for loading wholesale purchasing data, 
             scaling multi-dimensional expenditures, inducing an Agglomerative Hierarchical 
             Clustering model with Ward linkage, evaluating cluster cohesion via Silhouette score, 
             profiling client archetypes, and persisting pipeline artifacts using joblib.
"""

# =============================================================================
# Step 0: Import necessary libraries
# =============================================================================
# TODO 1: Import core data manipulation libraries: pandas as pd, numpy as np
# TODO 2: Import preprocessing scalers: StandardScaler from sklearn.preprocessing
# TODO 3: Import hierarchical clustering: AgglomerativeClustering from sklearn.cluster
# TODO 4: Import validation metrics: silhouette_score from sklearn.metrics
# TODO 5: Import model serialization: joblib
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering

def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery, Setup & Feature Selection
    - Goal: Load 'wholesale_client_data.csv' and inspect structure.
    - Separate qualitative identifiers ('client_id', 'client_name') from numeric expenditures.
    - Select numeric features required for hierarchical clustering.
    """
    print("\n[PHASE 1] Discovery & Feature Selection")
    print("-" * 65)
    # TODO 1: Load CSV dataset 'wholesale_client_data.csv' using pd.read_csv()
    #         - df_original = pd.read_csv("wholesale_client_data.csv")
    df = pd.read_csv(r"D:\Engineering\CDAC_ALL_MODULES\ML\ML_Practice(Exam_Reference_ali)\Agglomerative_Clustering\wholesale_client_data.csv")

    # TODO 2: Retain qualitative column 'client_name' in df_original for qualitative profiling
    feature_cols=["fresh_produce_k","dairy_milk_k","grocery_k","frozen_goods_k","delicatessen_k"]
    # TODO 3: Select numerical spending columns into feature matrix X:
    #         - feature_cols = ["fresh_produce_k", "dairy_milk_k", "grocery_k", "frozen_goods_k", "delicatessen_k"]
    #         - X = df_original[feature_cols].copy()
    X = df[feature_cols].copy()

    # TODO 4: Inspect loaded record count, display head, and print summary statistics:
    #         - print("Loaded Wholesale Records:", len(df_original))
    #         - print("Expenditure Features Head (k USD):\n", X.head())
    #         - print("\nSummary Statistics:\n", X.describe().round(2))
    print(X.head())
    print(X.describe().round(2))

    # TODO 5: Return numeric feature matrix X and full original DataFrame df_original
    return X,df


def phase_2_feature_scaling(X):
    """
    [Phase 2] Unsupervised Feature Scaling
    - Goal: Fit StandardScaler on expenditure metrics to equalize Euclidean weightings.
    """
    print("\n[PHASE 2] Unsupervised Feature Scaling")
    print("-" * 65)
    # TODO 1: Initialize StandardScaler() instance: scaler = StandardScaler()
    scaler = StandardScaler()
    # TODO 2: Fit and transform features X into X_scaled:
    #         - X_scaled = scaler.fit_transform(X)
    X_scaled = scaler.fit_transform(X)


    # TODO 3: Print confirmation and shape of X_scaled:
    #         - print("Features scaled successfully. Scaled shape:", X_scaled.shape)
    print(X_scaled.shape)
    # TODO 4: Return scaled features array X_scaled and fitted scaler object
    return X_scaled, scaler


def phase_3_agglomerative_model_induction(X_scaled, df_original):
    """
    [Phase 3] Agglomerative Clustering Model Induction
    - Goal: Instantiate AgglomerativeClustering with n_clusters=3 and Ward's linkage.
    - Fit model to scaled data and assign cluster labels back to dataset.
    """
    print("\n[PHASE 3] Agglomerative Clustering Model Induction")
    print("-" * 65)
    # TODO 1: Instantiate AgglomerativeClustering with:
    #         - n_clusters = 3
    #         - metric = "euclidean"
    #         - linkage = "ward"
    model = AgglomerativeClustering(n_clusters=3, metric="euclidean", linkage="ward")


    # TODO 2: Fit model and generate cluster labels using .fit_predict(X_scaled):
    #         - labels = model.fit_predict(X_scaled)

    labels = model.fit_predict(X_scaled)

    # TODO 3: Attach cluster assignments back to a copy of df_original:
    #         - df_clustered = df_original.copy()
    #         - df_clustered["cluster_id"] = labels
    df_clustered = df_original.copy()
    df_clustered["cluster_id"] = labels


    # TODO 4: Print cluster frequency counts:
    print("Cluster value counts:\n", df_clustered["cluster_id"].value_counts())

    # TODO 5: Return (model, labels, df_clustered)
    return model,labels,df_clustered


def phase_4_cluster_evaluation_and_profiling(X_scaled, labels, df_clustered):
    """
    [Phase 4] Cluster Evaluation & Business Profiling
    - Goal: Calculate Silhouette Score to measure cluster separation.
    - Calculate centroid spending profiles across clusters to define B2B client tiers.
    """
    print("\n[PHASE 4] Cluster Evaluation & Business Profiling")
    print("-" * 65)
    # TODO 1: Compute silhouette score using silhouette_score(X_scaled, labels):
    #         - score = silhouette_score(X_scaled, labels)
    #         - print(f"Silhouette Score (k=3, Ward): {score:.4f}")
    score = silhouette_score(X_scaled, labels)
    print(f"Silhouette Score (k=3, Ward): {score:.4f}")

    # TODO 2: Group df_clustered by 'cluster_id' and compute mean expenditure across numeric spending columns:
    feature_cols=["fresh_produce_k","dairy_milk_k","grocery_k","frozen_goods_k","delicatessen_k"]
    cluster_profiles = df_clustered.groupby("cluster_id")[feature_cols].mean()
    print("\nCluster Centroid Profiles (Mean Spend in k USD):\n", cluster_profiles.round(2))

    # TODO 3: Display sample client names alongside their assigned cluster:
    print("\nSample Wholesale Client Cluster Assignments:")
    print(df_clustered[["client_name", "cluster_id"]].head(8))
    

    # TODO 4: Return cluster_profiles DataFrame
    return cluster_profiles


def phase_5_joblib_model_persistence(model, scaler, feature_names, cluster_profiles):
    """
    [Phase 5] Unsupervised Model Persistence with Joblib
    - Goal: Save the trained Agglomerative model, scaler, and centroid profiles using joblib.
    - Test scoring a new incoming wholesale buyer by assigning to nearest cluster centroid.
    """
    print("\n[PHASE 5] Model Persistence with Joblib")
    print("-" * 65)
    # TODO 1: Define artifact paths:
    model_path = "wholesale_agglomerative_model.joblib"
    scaler_path = "wholesale_scaler.joblib"
    profiles_path = "wholesale_cluster_profiles.joblib"

    # TODO 2: Save model, scaler, and cluster_profiles to disk using joblib.dump():
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    joblib.dump(cluster_profiles, profiles_path)
    print(f"Artifacts successfully saved to disk: {model_path}, {scaler_path}, {profiles_path}")

    # TODO 3: Load artifacts using joblib.load():
    loaded_scaler = joblib.load(scaler_path)
    loaded_profiles = joblib.load(profiles_path)

    # TODO 4: Create a sample new wholesale buyer profile DataFrame:
    sample_buyer = pd.DataFrame([[35.0, 6.5, 8.0, 2.5, 10.0]],columns=feature_names)

    # TODO 5: Standardize the sample using loaded_scaler.transform()
    scaled_sample = loaded_scaler.transform(sample_buyer)[0]
    scaled_centroids = loaded_scaler.transform(loaded_profiles[feature_names])
    distances = np.linalg.norm(scaled_centroids - scaled_sample, axis=1)
    assigned_cluster = int(np.argmin(distances))

    # TODO 6: Compute Euclidean distance between the sample and cluster centroids to find the closest segment:
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
    
    # TODO: Uncomment and execute phases chronologically as you implement each function:
    X, df = phase_1_discovery_and_setup()
    X_scaled, scaler = phase_2_feature_scaling(X)
    model, labels, df_clustered = phase_3_agglomerative_model_induction(X_scaled, df)
    cluster_profiles = phase_4_cluster_evaluation_and_profiling(X_scaled, labels, df_clustered)
    phase_5_joblib_model_persistence(model, scaler, list(X.columns), cluster_profiles)


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_clustering_pipeline()

