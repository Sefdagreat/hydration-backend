# athlete-app/services/predictor.py
import pandas as pd
from athlete_app.core.model_loader import model, scaler, FEATURE_ORDER

def normalize_skin_conductance(raw_value: float) -> float:
    # Scale integer sensor values to match model range (0.5 - 2.5 scale)
    return raw_value * 1.25

def predict_hydration(data: dict) -> tuple[str, float]:
    # Normalize SC and calculate combined metrics
    data = data.copy()
    data["skin_conductance"] = normalize_skin_conductance(data["skin_conductance"])
    combined = sum([data["heart_rate"], data["body_temperature"], data["skin_conductance"]]) / 3
    data["combined_metrics"] = combined

    # Align features for model input
    input_df = pd.DataFrame([data])[FEATURE_ORDER]
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    return prediction, combined