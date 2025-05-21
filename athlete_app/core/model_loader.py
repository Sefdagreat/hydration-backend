# athlete_app/core/model_loader.py

import os
import joblib
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler

# Load paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.normpath(os.path.join(BASE_DIR, '..', 'model', 'hydration_model.joblib'))
SCALER_PATH = os.path.normpath(os.path.join(BASE_DIR, '..', 'model', 'hydration_scaler.joblib'))
TRAIN_PATH = os.path.normpath(os.path.join(BASE_DIR, '..', 'model', 'train_ecg_sigmoid.csv'))

# Feature order used in both training and prediction
FEATURE_ORDER = [
    "heart_rate",
    "body_temperature",
    "skin_conductance",
    "ecg_sigmoid",
    "combined_metrics"
]

_model = None
_scaler = None
_train_df = None

def get_model():
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
        _model = joblib.load(MODEL_PATH)
    return _model

def get_scaler():
    global _scaler
    if _scaler is None:
        if not os.path.exists(SCALER_PATH):
            raise FileNotFoundError(f"Scaler file not found at {SCALER_PATH}")
        _scaler = joblib.load(SCALER_PATH)
    return _scaler

def get_train_df():
    global _train_df
    if _train_df is None:
        _train_df = pd.read_csv(TRAIN_PATH)
    return _train_df

print("📦 MODEL_PATH:", os.path.abspath(MODEL_PATH))
print("📦 SCALER_PATH:", os.path.abspath(SCALER_PATH))
