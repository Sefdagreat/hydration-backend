# athlete_app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from athlete_app.api.routes import auth, profile, data, user
from athlete_app.core.config import init_db  
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

app.include_router(auth.router, prefix="/auth")
app.include_router(profile.router, prefix="/user")
app.include_router(data.router, prefix="/data")
app.include_router(user.router, prefix="/account")
