# Smart Hydration Backend API

This backend powers both the athlete and coach apps for hydration monitoring using FastAPI.

---

## 🔗 Live API URL (Railway)

Replace with your actual Railway domain:

```
https://hydration-backend.up.railway.app
```

## 📦 Project Structure (Unified)

```bash
backend/
├── main.py                 # Unified entrypoint for FastAPI
├── athlete_app/
│   ├── api/routes/
│   │   ├── auth.py
│   │   ├── profile.py
│   │   ├── data.py
│   │   └── user.py
│   ├── core/
│   │   ├── config.py
│   │   ├── model_loader.py
│   │   └── security.py
│   ├── models/schemas.py
│   ├── services/predictor.py
│   └── model/
│       ├── hydration_model_final.joblib
│       ├── hydration_scaler_final.joblib
│       └── cleaned_hydration_train.csv
├── coach_app/
│   ├── api/routes/
│   │   ├── dashboard.py
│   │   ├── athletes.py
│   │   ├── alerts.py
│   │   ├── profile.py
│   │   ├── settings.py
│   │   └── auth.py
│   ├── core/config.py
│   ├── models/schemas.py
│   └── services/utils.py
├── shared/database.py
├── .env.example
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
cd backend

# 2. Copy environment variables
cp .env.example .env

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the unified FastAPI app
uvicorn main:app --reload --port 8000
```

Swagger Docs: http://localhost:8000/docs

---

## 🧪 API Endpoints

### 🔐 Auth

| Method | Path               | Description      |
| ------ | ------------------ | ---------------- |
| POST   | /auth/signup       | Signup (athlete) |
| POST   | /auth/login        | Login (athlete)  |
| POST   | /coach/auth/signup | Signup (coach)   |
| POST   | /coach/auth/login  | Login (coach)    |

### 🧍 Athlete

| Method | Path                | Description              |
| ------ | ------------------- | ------------------------ |
| POST   | /data/receive       | Submit sensor data       |
| GET    | /data/status/latest | Latest hydration state   |
| GET    | /data/logs          | Hydration prediction log |

### 👤 Athlete Profile

| Method | Path              | Description         |
| ------ | ----------------- | ------------------- |
| GET    | /user/profile     | Get athlete profile |
| POST   | /user/profile     | Update profile      |
| POST   | /account/password | Change password     |
| DELETE | /account/delete   | Delete account      |

### 🧑‍🏫 Coach Dashboard

| Method | Path                  | Description       |
| ------ | --------------------- | ----------------- |
| GET    | /dashboard            | Overview stats    |
| GET    | /athletes/            | List all athletes |
| POST   | /athletes/add         | Add athlete       |
| DELETE | /athletes/remove/{id} | Remove athlete    |

### 🚨 Alerts

| Method | Path         | Description       |
| ------ | ------------ | ----------------- |
| GET    | /alerts/     | Get all alerts    |
| GET    | /alerts/{id} | Alerts by athlete |
| POST   | /alerts/     | Create new alert  |

### ⚙️ Coach Settings

| Method | Path                    | Description          |
| ------ | ----------------------- | -------------------- |
| GET    | /settings/units         | Get preferred units  |
| PUT    | /settings/units         | Update unit settings |
| GET    | /settings/notifications | Get notifications    |
| PUT    | /settings/notifications | Update notifications |

---

## ⚙️ Environment Variables (`.env`)

```env
MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/
DB_NAME=hydration_db
SECRET_KEY=your-secret-key
GSR_MULTIPLIER=1.25
```

---

## 🧼 Deployment with Railway

1. Push your GitHub repo
2. Go to [https://railway.app](https://railway.app)
3. Create a new project → Deploy from GitHub
4. Railway auto-detects `Dockerfile`
5. Set environment variables in the Railway dashboard
6. App builds & deploys to a public URL

Access your API at:

```
https://<your-railway-app>.up.railway.app/docs
```

---

## ✅ Tips

- Keep `.env` out of GitHub (`.gitignore`)
- Use `.env.example` to share safely
- Use tags in Swagger to test routes by user role

---

## 👨‍💻 Author

- Jan Josef Randrup
- Smart Hydration Capstone Backend
