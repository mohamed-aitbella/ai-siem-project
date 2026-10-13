import os
import sys
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, accuracy_score

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from data_prep import load_and_prep_data

def train_anomaly_detector(data_path, model_save_path):
    print("Starting AI Model Training Phase...")
    
    X, y = load_and_prep_data(data_path)
    if X is None:
        print("Error: Failed to load data. Exiting.")
        return

    print("Training Isolation Forest model...")
    model = IsolationForest(n_estimators=100, contamination=0.3, random_state=42)
    model.fit(X)

    print("Evaluating model performance...")
    predictions = model.predict(X)
    predictions_mapped = [0 if p == 1 else 1 for p in predictions]

    accuracy = accuracy_score(y, predictions_mapped) * 100
    
    print("\n" + "="*45)
    print("           MODEL PERFORMANCE REPORT")
    print("="*45)
    print(f"Accuracy Score: {accuracy:.2f}%\n")
    print(classification_report(y, predictions_mapped, target_names=["Normal", "Anomaly"]))
    print("="*45 + "\n")

    os.makedirs(os.path.dirname(model_save_path), exist_ok=True)
    joblib.dump(model, model_save_path)
    print(f"Model successfully saved to: {model_save_path}")

if __name__ == "__main__":
    current_dir = os.getcwd()
    data_path = os.path.join(current_dir, "data", "network_traffic_sample.csv")
    model_path = os.path.join(current_dir, "models", "isolation_forest_model.joblib")

    train_anomaly_detector(data_path, model_path)