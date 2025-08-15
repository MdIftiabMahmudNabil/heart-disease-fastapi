import os
import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from app.schemas import HeartFeatures

MODEL_PATH = os.getenv("MODEL_PATH", "model/heart_model.joblib")

app = FastAPI(title="Heart Disease Prediction API", version="1.0.0")

_model = None
_model_info = {"model_type": "unknown", "features": []}

def _load_model():
    global _model, _model_info
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model not found at: {MODEL_PATH}. Please train first.")
        _model = joblib.load(MODEL_PATH)
        _model_info["model_type"] = type(_model).__name__
        try:
            _model_info["features"] = _model.feature_names_in_.tolist()
        except Exception:
            pass
    return _model

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    try:
        _ = _load_model()
        return {"model_path": MODEL_PATH, **_model_info}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict")
def predict(payload: HeartFeatures):
    try:
        model = _load_model()
        x = np.array([[
            payload.age, payload.sex, payload.cp, payload.trestbps, payload.chol,
            payload.fbs, payload.restecg, payload.thalach, payload.exang,
            payload.oldpeak, payload.slope, payload.ca, payload.thal
        ]], dtype=float)
        pred = model.predict(x)[0]
        return {"heart_disease": bool(int(pred) == 1)}
    except FileNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")
