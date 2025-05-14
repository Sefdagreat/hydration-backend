# athlete-app/api/routes/data.py
from fastapi import APIRouter, Depends
from datetime import datetime
from athlete_app.models.schemas import SensorData
from athlete_app.api.deps import get_current_user
from athlete_app.core.config import db
from athlete_app.services.predictor import predict_hydration
from bson import ObjectId
from fastapi import Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/receive")
async def receive_data(data: SensorData, user=Depends(get_current_user)):
    input_data = data.dict()
    prediction, combined = predict_hydration(input_data)

    await db.sensor_data.insert_one({
        "user": user["username"],
        **input_data,
        "combined_metrics": combined,
        "timestamp": datetime.utcnow()
    })

    await db.predictions.insert_one({
        "user": user["username"],
        "hydration_status": prediction,
        "timestamp": datetime.utcnow()
    })

    return {
        "raw_sensor_data": input_data,
        "processed_combined_metrics": combined,
        "hydration_state_prediction": prediction
    }

@router.get("/status/latest")
async def get_latest_status(user=Depends(get_current_user)):
    record = await db.predictions.find_one(
        {"user": user["username"]}, sort=[("timestamp", -1)]
    )
    if record and "_id" in record:
        record["_id"] = str(record["_id"])  # Fix serialization issue
    return record or {"hydration_status": "Unknown"}

@router.get("/logs")
async def get_logs(user=Depends(get_current_user)):
    cursor = db.predictions.find({"user": user["username"]}).sort("timestamp", -1)
    logs = []
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])  # Fix for each document
        logs.append(doc)
    return logs

@router.post("/raw")
async def receive_raw_sensor_data(payload: list[dict], user=Depends(get_current_user)):
    sensor_map = {item['sensor_type']: item for item in payload}
    try:
        heart_rate = float(sensor_map['MAX30102']['value'])
        body_temperature = float(sensor_map['MLX90614']['value'])
        skin_conductance = float(sensor_map['GSR']['value'])
    except KeyError as e:
        return JSONResponse(status_code=400, content={"error": f"Missing sensor: {e}"})

    structured = {
        "heart_rate": heart_rate,
        "body_temperature": body_temperature,
        "skin_conductance": skin_conductance
    }

    prediction, combined = predict_hydration(structured)

    await db.sensor_data.insert_one({
        "user": user["username"],
        **structured,
        "combined_metrics": combined,
        "timestamp": datetime.utcnow()
    })

    await db.predictions.insert_one({
        "user": user["username"],
        "hydration_status": prediction,
        "timestamp": datetime.utcnow()
    })

    return {
        "prediction": prediction,
        "combined_metrics": combined
    }

@router.get("/time")
async def get_server_time():
    return {"timestamp": int(datetime.utcnow().timestamp())}

@router.get("/ping")
async def ping():
    return {"status": "alive"}