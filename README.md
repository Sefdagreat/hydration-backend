# Smart Hydration Backend API

This backend supports two FastAPI services:

- `athlete-app/`: Sensor data intake, user login, hydration ML prediction
- `coach-app/`: Coach dashboard, athlete management, alerts

---

## 🏁 How to Run (Dev)

1. Create `.env` in root with:

```env
MONGO_URI=...
DB_NAME=hydration_db
SECRET_KEY=...
