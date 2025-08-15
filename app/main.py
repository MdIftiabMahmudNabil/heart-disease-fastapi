# app/main.py

from fastapi import FastAPI
from app.schemas import HeartFeatures
import joblib
import numpy as np

# Load the heart model
model = joblib.load("model/heart_model.joblib")

# Create FastAPI app
app = FastAPI(
    title="Heart Disease Prediction API",
    description="API for predicting heart disease presence using FastAPI",
    version="1.0"
)

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "API is running"}

@app.get("/info")
def model_info():
    """Basic model info"""
    # Best effort to expose features if available
    try:
        features = model.feature_names_in_.tolist()
    except Exception:
        features = ["age","sex","cp","trestbps","chol","fbs","restecg",
                    "thalach","exang","oldpeak","slope","ca","thal"]
    return {
        "model_type": type(model).__name__,
        "features": features
    }

@app.post("/predict")
def predict_species(data: HeartFeatures):
    """Make prediction from input features"""
    features = np.array([[
        data.age, data.sex, data.cp, data.trestbps, data.chol,
        data.fbs, data.restecg, data.thalach, data.exang,
        data.oldpeak, data.slope, data.ca, data.thal
    ]])
    prediction = int(model.predict(features)[0])
    return {"heart_disease": bool(prediction == 1)}
