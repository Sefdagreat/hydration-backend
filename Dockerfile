#Dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf athlete_app/model/*.joblib  # ✅ moved here with `&&`

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN ls -lh athlete_app/model/

ENV PYTHONPATH=/app

CMD ["bash", "-c", "python check/model.py && uvicorn main:app --host 0.0.0.0 --port 8000"]
