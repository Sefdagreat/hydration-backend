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
RUN ls -lh athlete_app/model/ && python -c "import joblib; joblib.load('athlete_app/model/hydration_model_balanced.joblib')"


# 🔥 Crucial line to fix import of backend module
ENV PYTHONPATH=/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
