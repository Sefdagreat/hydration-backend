# athlete-app/services/predictor.py
import pandas as pd
from athlete_app.core.model_loader import model, scaler, FEATURE_ORDER

def normalize_skin_conductance(raw_value: float) -> float:
    return raw_value * 1.25  # Convert from hardware scale

def predict_hydration(data: dict) -> tuple[str, float]:
    data = data.copy()

    data["skin_conductance"] = normalize_skin_conductance(data["skin_conductance"])

    # Calculate combined metrics across 4 features
    combined = (
        data["heart_rate"]
        + data["body_temperature"]
        + data["skin_conductance"]
        + data["ecg_sigmoid"]
    ) / 4
    data["combined_metrics"] = combined

    input_df = pd.DataFrame([data])[FEATURE_ORDER]
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    return prediction, combined
