# Dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Optional: verify model files exist (not load)
RUN ls -lh athlete_app/model/

ENV PYTHONPATH=/app

# ✅ Final: run model check before starting the app
CMD ["bash", "-c", "python check/model.py && uvicorn main:app --host 0.0.0.0 --port 8000"]
