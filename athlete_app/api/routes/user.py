# athlete-app/api/routes/user.py
from fastapi import APIRouter, HTTPException, Depends
from athlete_app.models.schemas import PasswordChange
from athlete_app.api.deps import get_current_user
from athlete_app.core.config import db

router = APIRouter()

@router.post("/password")
async def change_password(data: PasswordChange, user=Depends(get_current_user)):
    if user["password"] != data.current_password:
        raise HTTPException(status_code=403, detail="Incorrect current password")
    await db.users.update_one({"username": user["username"]}, {"$set": {"password": data.new_password}})
    return {"message": "Password changed"}

@router.delete("/delete")
async def delete_account(user=Depends(get_current_user)):
    await db.users.delete_one({"username": user["username"]})
    return {"message": "Account deleted"}
