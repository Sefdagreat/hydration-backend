# coach-app/core/config.py
from dotenv import load_dotenv
import os
from pydantic import BaseSettings

load_dotenv()  # <-- important for Railway/local switching

class Settings(BaseSettings):
    mongo_uri: str = os.getenv("MONGO_URI")
    db_name: str = os.getenv("DB_NAME", "hydration_db")
    secret_key: str = os.getenv("SECRET_KEY", "your-secret-key")
    algorithm: str = "HS256"

settings = Settings()
