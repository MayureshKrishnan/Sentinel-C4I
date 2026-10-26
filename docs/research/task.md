# Execution Tasks: Phase 1 Backend

- `[x]` 1. **Project Setup & Schemas**
  - `[x]` Initialize virtual environment and install backend dependencies.
  - `[x]` Create `app/models/schemas.py` with Pydantic models.
- `[x]` 2. **Credibility Scoring Engine**
  - `[x]` Create `app/services/scoring.py` with the decay mathematical formula.
- `[x]` 3. **Naive Bayes Classifier**
  - `[x]` Create `app/services/classifier.py` and train with synthetic dataset.
- `[x]` 4. **PuLP Optimizer & API Router**
  - `[x]` Create `app/services/optimizer.py`.
  - `[x]` Create `app/main.py` with FastAPI endpoints.
- `[x]` 5. **Testing**
  - `[x]` Create `tests/test_scoring.py`.
  - `[x]` Verify temporal decay and noise detection passes.
