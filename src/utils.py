import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    # Handle any missing data, outliers, etc.
    df.fillna(method='ffill', inplace=True)
    return df
