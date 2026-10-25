# Multi-Stage Production Dockerfile for Sentinel V2 C4I Modular Architecture
FROM python:3.10-slim as builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY sentinel-backend/requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Final Runtime Image
FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/app/sentinel-backend:/app/sentinel-engine
ENV PORT=8000

# Copy 3 modular folders
COPY sentinel-backend/ /app/sentinel-backend/
COPY sentinel-engine/ /app/sentinel-engine/
COPY sentinel-frontend/ /app/sentinel-frontend/

EXPOSE 8000

CMD ["sh", "-c", "cd sentinel-backend && uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
