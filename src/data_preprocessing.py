import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def check_missing_data(df):
    missing_values = df.isnull().sum()
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title("Heatmap of Missing Values")
    plt.show()
    return missing_values

def encode_categorical_data(df):
    categorical_columns = df.select_dtypes(include=['object']).columns
    label_encoder = LabelEncoder()
    for col in categorical_columns:
        df[col] = label_encoder.fit_transform(df[col])
    return df
