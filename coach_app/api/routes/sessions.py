# coach_app/api/routes/sessions.py

from fastapi import APIRouter, Depends, HTTPException
from coach_app.api.deps import get_current_coach
from shared.database import db
from bson import ObjectId

router = APIRouter()

@router.get("/session/logs/{athlete_id}")
async def get_athlete_sessions(athlete_id: str, coach=Depends(get_current_coach)):
    sessions = db.sessions.find({"user": athlete_id}, sort=[("start_time", -1)])
    results = []
    async for s in sessions:
        s["_id"] = str(s["_id"])
        results.append(s)
    if not results:
        raise HTTPException(status_code=404, detail=f"No sessions found for athlete: {athlete_id}")
    return results
