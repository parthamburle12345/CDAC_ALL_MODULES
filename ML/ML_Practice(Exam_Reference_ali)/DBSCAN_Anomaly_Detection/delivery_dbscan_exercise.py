"""
Title: Density-Based Urban Logistics Hotspot & Anomaly Discovery with DBSCAN
Description: A modular Python exercise script for loading vehicle telemetry data, 
             scaling spatial and operational features, inducing a DBSCAN density model, 
             isolating operational anomalies/noise (label -1), evaluating core cluster cohesion 
             via Silhouette score, profiling fulfillment hubs, and persisting pipeline artifacts using joblib.
"""

# =============================================================================
# Step 0: Import necessary libraries
# =============================================================================
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score


def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery, Setup & Telemetry Feature Selection
    - Goal: Load 'delivery_fleet_telemetry.csv' and inspect structure.
    - Separate qualitative identifiers ('delivery_id', 'vehicle_id') from numeric metrics.
    - Select continuous spatial and operational metrics for density clustering.
    """
    print("\n[PHASE 1] Discovery & Feature Selection")
    print("-" * 65)
    # Load CSV file using pandas
    df_original = pd.read_csv("delivery_fleet_telemetry.csv")

    # Select continuous spatial and operational features
    feature_cols = [
        "latitude",
        "longitude",
        "delivery_delay_min",
        "package_weight_kg",
    ]
    X = df_original[feature_cols].copy()

    print("Loaded Telemetry Drops:", len(df_original))
    print("Telemetry Features Head:\n", X.head())
    print("\nSummary Statistics:\n", X.describe().round(2))
    return X, df_original


def phase_2_feature_scaling(X):
    """
    [Phase 2] Unsupervised Feature Scaling
    - Goal: Fit StandardScaler on coordinates and operational metrics.
    - Density clustering with Euclidean distance requires isotropic standardization.
    """
    print("\n[PHASE 2] Unsupervised Feature Scaling")
    print("-" * 65)
    # Initialize StandardScaler
    scaler = StandardScaler()

    # Fit and transform features X into X_scaled
    X_scaled = scaler.fit_transform(X)
    print("Features standardized successfully. Scaled shape:", X_scaled.shape)
    return X_scaled, scaler


def phase_3_dbscan_model_induction(X_scaled, df_original):
    """
    [Phase 3] DBSCAN Model Induction & Noise Segregation
    - Goal: Instantiate DBSCAN(eps=0.65, min_samples=3) to cluster dense areas.
    - Fit model and assign cluster labels (with -1 identifying noise/outliers).
    """
    print("\n[PHASE 3] DBSCAN Model Induction & Noise Segregation")
    print("-" * 65)
    # Instantiate DBSCAN with calibrated neighborhood and density thresholds
    model = DBSCAN(eps=0.65, min_samples=3, metric="euclidean")

    # Fit model and predict cluster labels
    labels = model.fit_predict(X_scaled)

    # Attach cluster assignments back to original dataframe
    df_clustered = df_original.copy()
    df_clustered["cluster_id"] = labels

    # Count dense clusters and noise records
    unique_labels = set(labels)
    n_clusters = len(unique_labels - {-1})
    n_noise = list(labels).count(-1)

    print(f"Discovered Dense Clusters: {n_clusters}")
    print(f"Identified Noise / Outlier Points: {n_noise}")
    print("Cluster Value Distribution:\n", df_clustered["cluster_id"].value_counts())
    return model, labels, df_clustered


def phase_4_cluster_evaluation_and_profiling(X_scaled, labels, df_clustered):
    """
    [Phase 4] Cluster Evaluation & Anomaly Profiling
    - Goal: Calculate Silhouette Score on valid non-noise clusters.
    - Profile centroid statistics for dense fulfillment zones.
    - Inspect and report isolated operational anomalies.
    """
    print("\n[PHASE 4] Cluster Evaluation & Anomaly Profiling")
    print("-" * 65)
    # Mask to isolate core cluster points from noise (-1)
    core_mask = labels != -1

    if len(set(labels[core_mask])) > 1:
        score = silhouette_score(X_scaled[core_mask], labels[core_mask])
        print(f"Silhouette Score (Core Non-Noise Points): {score:.4f}")
    else:
        print("Insufficient cluster count to compute silhouette score.")

    # Compute mean operational profiles per discovered fulfillment hub
    numeric_cols = [
        "latitude",
        "longitude",
        "delivery_delay_min",
        "package_weight_kg",
    ]
    hub_profiles = df_clustered[core_mask].groupby("cluster_id")[numeric_cols].mean()
    print("\nFulfillment Hub Centroid Profiles (Mean Metrics):\n", hub_profiles.round(3))

    # Display isolated operational anomalies
    print("\nOperational Anomalies Detected (Noise Points / Label -1):")
    anomalies = df_clustered[df_clustered["cluster_id"] == -1]
    print(anomalies[["delivery_id", "vehicle_id", "delivery_delay_min", "package_weight_kg"]])
    return hub_profiles


def phase_5_joblib_model_persistence(model, scaler, feature_names, X_scaled, labels):
    """
    [Phase 5] Pipeline Persistence & Streaming Anomaly Screening
    - Goal: Save the trained DBSCAN model, scaler, and core training points using joblib.
    - Test scoring a new delivery drop using epsilon-neighborhood proximity check.
    """
    print("\n[PHASE 5] Model Persistence & Anomaly Screening")
    print("-" * 65)
    # Define artifact paths
    model_path = "dbscan_fleet_model.joblib"
    scaler_path = "dbscan_scaler.joblib"
    core_points_path = "dbscan_core_data.joblib"

    # Save artifacts (storing core scaled points and labels for proximity classification)
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    joblib.dump({"X_scaled": X_scaled, "labels": labels, "feature_names": feature_names}, core_points_path)
    print("DBSCAN Model, Scaler, and Core Telemetry successfully saved using joblib.")

    # Load artifacts using joblib.load()
    loaded_scaler = joblib.load(scaler_path)
    loaded_data = joblib.load(core_points_path)

    # Test Sample A: Normal delivery drop near Downtown Core (Lat 18.521, Lon 73.855, Delay 8 min, Weight 4.5 kg)
    sample_normal = pd.DataFrame([[18.521, 73.855, 8, 4.5]], columns=feature_names)
    sample_normal_scaled = loaded_scaler.transform(sample_normal)[0]

    # Test Sample B: Extreme outlier breakdown drop (Lat 19.100, Lon 74.300, Delay 150 min, Weight 90 kg)
    sample_outlier = pd.DataFrame([[19.100, 74.300, 150, 90.0]], columns=feature_names)
    sample_outlier_scaled = loaded_scaler.transform(sample_outlier)[0]

    # Screening helper function: compute min distance to known core cluster points
    def screen_telemetry_point(scaled_pt, eps=0.65):
        core_pts = loaded_data["X_scaled"][loaded_data["labels"] != -1]
        core_lbls = loaded_data["labels"][loaded_data["labels"] != -1]
        distances = np.linalg.norm(core_pts - scaled_pt, axis=1)
        min_idx = np.argmin(distances)
        if distances[min_idx] <= eps:
            return f"Assigned to Cluster {core_lbls[min_idx]} (Min Dist: {distances[min_idx]:.3f})"
        else:
            return f"ALERT: Outlier / Operational Anomaly Detected (Min Dist: {distances[min_idx]:.3f} > eps {eps})"

    print(f"Sample A (Downtown Drop) -> {screen_telemetry_point(sample_normal_scaled)}")
    print(f"Sample B (Extreme Delay) -> {screen_telemetry_point(sample_outlier_scaled)}")


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_clustering_pipeline():
    """
    Facade function coordinating the DBSCAN density clustering pipeline.
    """
    print("=" * 65)
    print("STARTING DENSITY-BASED SPATIAL CLUSTERING LIFECYCLE (DBSCAN)")
    print("=" * 65)
    
    # Executing phases chronologically
    X, df_original = phase_1_discovery_and_setup()
    X_scaled, scaler = phase_2_feature_scaling(X)
    model, labels, df_clustered = phase_3_dbscan_model_induction(X_scaled, df_original)
    phase_4_cluster_evaluation_and_profiling(X_scaled, labels, df_clustered)
    phase_5_joblib_model_persistence(model, scaler, list(X.columns), X_scaled, labels)


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_clustering_pipeline()

