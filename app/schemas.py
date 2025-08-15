# app/schemas.py

from pydantic import BaseModel

# Input schema for /predict
class HeartFeatures(BaseModel):
    age: float
    sex: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

# Output schema for /predict
class PredictionOutput(BaseModel):
    heart_disease: bool
