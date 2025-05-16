# athlete_app/core/config.py
from dotenv import load_dotenv
load_dotenv()

import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConfigurationError

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "hydration_db")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 hours


client = AsyncIOMotorClient(MONGO_URI)
try:
    client.admin.command("ping")
except ConfigurationError as ce:
    import logging
    logging.error(f"MongoDB connection failed: {ce}")
    raise

db = client[DB_NAME]

def init_db():
    return db
