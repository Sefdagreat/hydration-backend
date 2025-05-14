# athlete-app/api/routes/profile.py
from fastapi import APIRouter, Depends
from athlete_app.models.schemas import UserProfile
from athlete_app.api.deps import get_current_user
from athlete_app.core.config import db

router = APIRouter()

@router.post("/profile")
async def update_profile(profile: UserProfile, user=Depends(get_current_user)):
    await db.users.update_one({"username": user["username"]}, {"$set": {"profile": profile.dict()}})
    return {"message": "Profile updated"}

@router.get("/profile")
async def get_profile(user=Depends(get_current_user)):
    record = await db.users.find_one({"username": user["username"]})
    return record.get("profile", {})
