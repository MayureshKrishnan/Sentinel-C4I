# Production Dockerfile for Sentinel V2 C4I Platform (24/7 Always-Live Cloud)
FROM python:3.10-slim

# Create standard non-root user (UID 1000 required for cloud container environments)
RUN useradd -m -u 1000 user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    PYTHONPATH=/home/user/app/sentinel-backend:/home/user/app/sentinel-engine \
    PORT=10000

WORKDIR $HOME/app

# Install dependencies
COPY --chown=user:user sentinel-backend/requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy all 3 architectural tiers
COPY --chown=user:user sentinel-backend/ /home/user/app/sentinel-backend/
COPY --chown=user:user sentinel-engine/ /home/user/app/sentinel-engine/
COPY --chown=user:user sentinel-frontend/ /home/user/app/sentinel-frontend/

USER user
EXPOSE 10000 8000 7860

CMD ["sh", "-c", "cd sentinel-backend && uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-10000}"]
