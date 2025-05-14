# athlete-app/api/routes/auth.py
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from athlete_app.models.schemas import User
from athlete_app.core.config import db
from athlete_app.core.security import create_access_token

router = APIRouter()

@router.post("/signup")
async def signup(user: User):
    print("Received signup for:", user.username)  # Debug
    if await db.users.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already exists")
    await db.users.insert_one({**user.dict(), "profile": {}, "settings": {}})
    return {"message": "Signup successful"}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await db.users.find_one({"username": form_data.username})
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}
