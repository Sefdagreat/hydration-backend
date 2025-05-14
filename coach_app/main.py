# coach-app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from coach_app.api.routes import dashboard, athletes, alerts, profile, settings, auth
from shared.database import db

app = FastAPI(
    title="Coach App API",
    version="1.0.0",
    description="APIs for coaching dashboard to monitor athlete hydration status"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await db.command("ping")

@app.get("/ping")
async def ping():
    return {"status": "alive"}

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(athletes.router, prefix="/athletes", tags=["Athletes"])
app.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])
app.include_router(profile.router, prefix="/profile", tags=["Profile"])
app.include_router(settings.router, prefix="/settings", tags=["Settings"])