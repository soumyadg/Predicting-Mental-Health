import unittest
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from src.model_evaluation import plot_feature_importance
import pandas as pd

X, y = make_classification(n_samples=100, n_features=5, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

class TestModelEvaluation(unittest.TestCase):
    def test_plot_feature_importance(self):
        # Convert X to a DataFrame to pass to the plot function
        X_df = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(X.shape[1])])
        plot_feature_importance(model, X_df.columns)  # Pass the feature names
