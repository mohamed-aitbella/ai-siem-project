import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

def load_and_prep_data(filepath):
    print(f"[+] Loading data from: {filepath}...")
    
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print("[-] Error: Data file not found!")
        return None, None

    print("[+] Encoding categorical features...")
    le = LabelEncoder()
    if 'protocol_type' in df.columns:
        df['protocol_type'] = le.fit_transform(df['protocol_type'])

    X = df.drop('label', axis=1)
    y = df['label'].apply(lambda x: 1 if x == 'anomaly' else 0)

    print("[+] Scaling features...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("[✓] Data preparation complete!\n")
    return X_scaled, y

if __name__ == "__main__":
    current_dir = os.getcwd()
    data_path = os.path.join(current_dir, "data", "network_traffic_sample.csv")
    
    X, y = load_and_prep_data(data_path)
    
    if X is not None:
        print("--- Results ---")
        print(f"Data Shape: {X.shape} (Rows, Columns)")
        print(f"Number of normal traffic: {sum(y == 0)}")
        print(f"Number of attacks (anomalies): {sum(y == 1)}")