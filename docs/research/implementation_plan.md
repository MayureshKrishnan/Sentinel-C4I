# Sentinel Phase 1: Backend Intelligence Core

This plan outlines the architecture and execution strategy for Member 1's backend responsibilities (FastAPI, AI Scoring Engine, Linear Programming Optimizer). 

## User Review Required
> [!IMPORTANT]  
> Please review the dependencies and API endpoints below. Once approved, I will immediately execute the Python codebase and write the test suite.

## Proposed Changes

We will create a new directory `sentinel-api` alongside the existing `sentinel-ui` folder.

### 1. Project Initialization & Dependencies
- Create a `backend` directory with `app/` and `tests/` folders.
- Setup a `requirements.txt` with the following:
  - `fastapi` and `uvicorn` (REST API Server)
  - `pydantic` (Data Validation)
  - `scikit-learn` (Naive Bayes Classifier)
  - `pulp` (Resource Allocation Optimizer)
  - `pytest` (Automated Testing)

### 2. Core Python Services
- **[NEW] `app/models/schemas.py`**: Pydantic schemas for `TipSubmission`, `TipScoreResponse`, `SearchZone`, and `DispatchOptimizationResponse`.
- **[NEW] `app/services/scoring.py`**: Implements the mathematical equation $S = (w_1C + w_2V + w_3I)e^{-\lambda\Delta t}$.
- **[NEW] `app/services/classifier.py`**: A Naive Bayes `MultinomialNB` text classifier trained to detect fake news / social media noise.
- **[NEW] `app/services/optimizer.py`**: A PuLP linear programming script to maximize volunteer allocation to high-priority search zones.

### 3. API Router
- **[NEW] `app/main.py`**: The FastAPI application exposing two endpoints:
  - `POST /api/v1/tips/score`: Receives a raw tip, classifies it, runs the scoring formula, and returns the computed trust score.
  - `POST /api/v1/dispatch/optimize`: Receives available teams and search zones, returning the optimal deployment plan.

### 4. Testing Suite
- **[NEW] `tests/test_scoring.py`**: PyTest file to mathematically prove the 6-hour half-life decay works, and to verify the Naive Bayes model correctly blocks noise.

## Verification Plan

### Automated Tests
I will run `pytest tests/` to confirm:
1. A tip from 6 hours ago scores exactly ~50% lower than a tip from right now.
2. The phrase "please share this on facebook" is correctly classified as `NOISE = True`.

### Manual Verification
Once the tests pass, I will spin up the `uvicorn` server and we can test hitting the backend directly!
