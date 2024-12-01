import unittest
from src.models import train_random_forest, train_logistic_regression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=100, n_features=5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

class TestModels(unittest.TestCase):
    def test_train_random_forest(self):
        model = train_random_forest(X_train, y_train)
        self.assertTrue(model)

    def test_train_logistic_regression(self):
        model = train_logistic_regression(X_train, y_train)
        self.assertTrue(model)
