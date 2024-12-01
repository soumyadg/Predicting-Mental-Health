def create_new_features(df):
    df['Income Per Child'] = df['Income'] / (df['Number of Children'] + 1)
    df['Is Physically Active'] = df['Physical Activity Level'].apply(lambda x: 1 if x == 'Active' else 0)
    df['Risky Habits'] = df['Smoking Status'].apply(lambda x: 1 if x != 'Non-smoker' else 0)
    return df
