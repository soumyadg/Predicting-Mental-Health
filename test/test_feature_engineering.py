import unittest
from src.feature_engineering import create_new_features

class TestFeatureEngineering(unittest.TestCase):
    def test_create_new_features(self):
        df = pd.DataFrame({
            'Income': [50000, 60000, 70000],
            'Number of Children': [2, 1, 3],
            'Physical Activity Level': ['Active', 'Sedentary', 'Active']
        })
        df = create_new_features(df)
        self.assertTrue('Income Per Child' in df.columns)
        self.assertTrue('Is Physically Active' in df.columns)
