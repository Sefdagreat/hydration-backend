# athlete-app/api/deps.py
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from athlete_app.core.security import decode_token
from athlete_app.core.config import db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = await db.users.find_one({"username": payload["sub"]})
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user
