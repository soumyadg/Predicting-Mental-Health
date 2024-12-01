import unittest
from src.data_preprocessing import load_data, check_missing_data

class TestDataPreprocessing(unittest.TestCase):
    def test_load_data(self):
        df = load_data('depression_data.csv')
        self.assertEqual(len(df), 413768)  # Example number of rows

    def test_check_missing_data(self):
        df = load_data('depression_data.csv')
        missing_data = check_missing_data(df)
        self.assertEqual(missing_data.sum(), 0)  # Assuming no missing data
