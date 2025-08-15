# model/train_model.py

import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the Heart Disease dataset from CSV
df = pd.read_csv("data/heart.csv")

# Features and target (binary: 0 = absence, 1 = presence)
feature_cols = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]
X = df[feature_cols].values
y = df["target"].astype(int).values

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train a classifier (Random Forest)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Ensure output directory exists and save the model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/heart_model.joblib")

print("Model trained and saved successfully.")
