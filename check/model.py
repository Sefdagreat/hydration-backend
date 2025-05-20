# check/model.py
import joblib
from pathlib import Path
import sys

model_path = Path("athlete_app/model/hydration_model_balanced.joblib")
scaler_path = Path("athlete_app/model/hydration_scaler_balanced.joblib")

try:
    joblib.load(model_path)
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"❌ Failed to load model at {model_path}:\n{e}")
    sys.exit(1)  # 🔥 Exit with error

try:
    joblib.load(scaler_path)
    print("✅ Scaler loaded successfully.")
except Exception as e:
    print(f"❌ Failed to load scaler at {scaler_path}:\n{e}")
    sys.exit(1)  # 🔥 Exit with error
