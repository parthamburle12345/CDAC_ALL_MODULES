"""
Title: Unsupervised Cricket Player Role Segmentation 
Description: A modular Python exercise script for loading cricket statistics, 
             scaling features, training a K-Means clustering model to group 
             players into functional roles (Batsmen, Bowlers, All-Rounders), 
             evaluating clusters, and persisting artifacts using joblib.
"""

# Step 0: Import necessary libraries
# TODO: Import pandas, numpy, StandardScaler from sklearn.preprocessing, 
#       KMeans from sklearn.cluster, silhouette_score from sklearn.metrics, and joblib
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import joblib


def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery, Setup & Feature Selection
    - Goal: Load 'cricket_player_stats.csv' and inspect structure.
    - Separate player names/identifiers from numeric statistics.
    - Select numeric features required for role clustering.
    """
    print("\n[PHASE 1] Discovery & Feature Selection")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    df = pd.read_csv('./Day11/ML_Practice/Cricket_Player_Statistics/cricket_player_stats.csv')

    # TODO: Retain 'player_name' for final profiling
    df_original = df.copy()

    # TODO: Select numerical features (e.g., 'runs_scored', 'batting_average', 'wickets_taken', 'bowling_economy')
    num_cols = ['runs_scored', 'batting_average', 'wickets_taken', 'bowling_economy']
    X = df[num_cols].copy()
    X = X.fillna(X.mean())
    print(df_original.head())
    
    return X, df_original




def phase_2_feature_scaling(X):
    """
    [Phase 2] Unsupervised Feature Scaling
    - Goal: Fit StandardScaler on performance metrics to equalize feature weightings.
    """
    print("\n[PHASE 2] Unsupervised Feature Scaling")
    print("-" * 65)
    # TODO: Initialize StandardScaler()
    scaler = StandardScaler()

    # TODO: Fit and transform features X into X_scaled
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled,scaler


def phase_3_kmeans_model_induction(X_scaled, df_original):
    """
    [Phase 3] K-Means Model Induction
    - Goal: Train KMeans model setting n_clusters=3 (Batsmen, Bowlers, All-Rounders).
    - Fit model to scaled data and assign cluster labels back to dataset.
    """
    print("\n[PHASE 3] K-Means Model Induction & Labeling")
    print("-" * 65)
    # TODO: Instantiate KMeans(n_clusters=3, random_state=42)
    model = KMeans(n_clusters=3,random_state=42)

    # TODO: Fit model and generate cluster labels using .fit_predict(X_scaled)
    labels = model.fit_predict(X_scaled)
    df_clustered = df_original.copy()
    df_clustered['cluster_id'] = labels

    return model, labels, df_clustered



def phase_4_cluster_evaluation_and_profiling(X_scaled, labels, df_clustered):
    """
    [Phase 4] Cluster Evaluation & Role Profiling
    - Goal: Calculate Silhouette Score to measure cluster separation.
    - Calculate average statistics per cluster and translate centroids into cricket roles.
    """
    print("\n[PHASE 4] Cluster Evaluation & Role Profiling")
    print("-" * 65)
    # TODO: Compute silhouette_score(X_scaled, labels)
    score = silhouette_score(X_scaled,labels)
    print(f'Silhouette Score :{score:.4f}')

    # TODO: Group df_clustered by 'cluster_id' and compute mean statistics to interpret roles
    profile = df_clustered.groupby('cluster_id')[['runs_scored', 'batting_average', 'wickets_taken', 'bowling_economy']].mean()
    print('Cluster Profiling :\n')
    print(profile)


def phase_5_joblib_model_persistence(model, scaler, feature_names):
    """
    [Phase 5] Unsupervised Model Persistence with Joblib
    - Goal: Save the trained KMeans model and scaler to disk using joblib.
    - Test loading artifacts to assign a new player profile to a role cluster.
    """
    print("\n[PHASE 5] Model Persistence with Joblib")
    print("-" * 65)
    # TODO: Save model, scaler, and feature list using joblib.dump()
    artifacts={
        'model': model,
        'scaler':scaler,
        'features':feature_names
    }
    joblib.dump(artifacts,'cricket_player_pipeline.joblib')

    # TODO: Load artifacts using joblib.load() and predict the cluster for a new player profile
    loaded = joblib.load('cricket_player_pipeline.joblib')
    new_data = pd.DataFrame([[3500, 42.5, 5, 8.2]],columns=loaded['features'])

    new_data_scaled = loaded['scaler'].transform(new_data)
    predict_cluster = loaded['model'].predict(new_data_scaled)[0]
    print(predict_cluster)


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_cricket_clustering_pipeline():
    """
    Facade function coordinating the cricket player segmentation pipeline.
    """
    print("=" * 65)
    print("STARTING CRICKET PLAYER ROLE CLUSTERING LIFECYCLE (K-Means)")
    print("=" * 65)
    
    # Executing phases chronologically
    X, df_original = phase_1_discovery_and_setup()
    X_scaled, scaler = phase_2_feature_scaling(X)
    model, labels, df_clustered = phase_3_kmeans_model_induction(X_scaled, df_original)
    phase_4_cluster_evaluation_and_profiling(X_scaled, labels, df_clustered)
    phase_5_joblib_model_persistence(model, scaler, list(X.columns))


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_cricket_clustering_pipeline()