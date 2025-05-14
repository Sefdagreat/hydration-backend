# coach-app/api/routes/dashboard.py
from fastapi import APIRouter
from shared.database import db

router = APIRouter()

@router.get("/")
async def dashboard():
    total = await db.athletes.count_documents({})
    dehydrated = await db.athletes.count_documents({"status": "Dehydrated"})
    hydrated_pct = 100 - (dehydrated * 100 // total) if total else 0
    trend = [round(80 + i % 5, 1) for i in range(7)]  # Dummy trend
    return {
        "total_athletes": total,
        "hydrated_pct": hydrated_pct,
        "hydration_trend": trend
    }
