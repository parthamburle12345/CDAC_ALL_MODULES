import pickle
import os

class ExperimentSnapshot:
    def __init__(self, experiment_id, model_type, hyperparameters, metrics, timestamp):
        self.experiment_id = experiment_id
        self.model_type = model_type
        self.hyperparameters = dict(hyperparameters)
        self.metrics = dict(metrics)
        self.timestamp = timestamp

    def get_best_metric(self, metric_name):
        """Returns the numeric score for metric_name from metrics."""
        return self.metrics.get(metric_name)


def save_experiment(snapshot, file_path):
    """Serializes ExperimentSnapshot instance to binary file using pickle."""
    with open(file_path, "wb") as f:
        pickle.dump(snapshot, f)


def load_experiment(file_path):
    """Deserializes ExperimentSnapshot from file. Raises FileNotFoundError if missing."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Experiment file not found: {file_path}")
    
    with open(file_path, "rb") as f:
        return pickle.load(f)


# Example Walkthrough
if __name__ == "__main__":
    pkl_path = os.path.join(os.path.dirname(__file__), "experiment_01.pkl")

    exp = ExperimentSnapshot(
        experiment_id="EXP-2026-001",
        model_type="RandomForest",
        hyperparameters={"n_estimators": 100, "max_depth": 10},
        metrics={"accuracy": 0.942, "f1_score": 0.938},
        timestamp="2026-09-01 10:00:00"
    )

    save_experiment(exp, pkl_path)

    restored_exp = load_experiment(pkl_path)
    print(restored_exp.model_type)                    # Output: RandomForest
    print(restored_exp.get_best_metric("accuracy"))   # Output: 0.942
