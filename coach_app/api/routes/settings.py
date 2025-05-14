# coach-app/api/routes/settings.py
from fastapi import APIRouter
from coach_app.models.schemas import NotificationSettings, UnitsSettings
from shared.database import db

router = APIRouter()

@router.get("/notifications", response_model=NotificationSettings)
async def get_notifications():
    doc = await db.settings.find_one({"type": "notification"}) or {}
    return NotificationSettings(**doc.get("value", {}))

@router.put("/notifications")
async def update_notifications(data: NotificationSettings):
    await db.settings.update_one(
        {"type": "notification"},
        {"$set": {"value": data.dict()}},
        upsert=True
    )
    return {"message": "Notification settings updated"}

@router.get("/units", response_model=UnitsSettings)
async def get_units():
    doc = await db.settings.find_one({"type": "units"}) or {}
    return UnitsSettings(**doc.get("value", {}))

@router.put("/units")
async def update_units(data: UnitsSettings):
    await db.settings.update_one(
        {"type": "units"},
        {"$set": {"value": data.dict()}},
        upsert=True
    )
    return {"message": "Units updated"}
