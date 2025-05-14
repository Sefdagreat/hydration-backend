# coach-app/api/routes/alerts.py
from fastapi import APIRouter
from coach_app.models.schemas import Athlete, Alert
from shared.database import db

router = APIRouter()

@router.get("/", response_model=list[Alert])
async def get_all_alerts():
    return [doc async for doc in db.alerts.find()]

@router.get("/{athlete_id}", response_model=list[Alert])
async def get_alerts_by_athlete(athlete_id: str):
    return [doc async for doc in db.alerts.find({"athlete_id": athlete_id})]

@router.post("/")
async def create_alert(data: Alert):
    await db.alerts.insert_one(data.dict())
    return {"message": "Alert created"}
