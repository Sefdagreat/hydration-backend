# athlete_app/core/model_loader.py

import os
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.normpath(os.path.join(BASE_DIR, '..', 'model', 'hydration_model_final.joblib'))
SCALER_PATH = os.path.normpath(os.path.join(BASE_DIR, '..', 'model', 'hydration_scaler_final.joblib'))
TRAIN_PATH = os.path.normpath(os.path.join(BASE_DIR, '..', 'model', 'cleaned_hydration_train.csv'))

# Feature order used in both training and prediction
FEATURE_ORDER = ["heart_rate", "body_temperature", "skin_conductance", "combined_metrics"]

# Load model and scaler
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
if not os.path.exists(SCALER_PATH):
    raise FileNotFoundError(f"Scaler file not found at {SCALER_PATH}")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Optional: load training data (e.g., for SHAP)
train_df = pd.read_csv(TRAIN_PATH)