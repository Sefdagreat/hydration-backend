# backend/check/model.py

import joblib
from pathlib import Path

model_path = Path("athlete_app/model/hydration_model_balanced.joblib")

try:
    joblib.load(model_path)
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"❌ Failed to load model at {model_path}:\n{e}")
