# SENTINEL - Phase 1 Pure Software Core Plan (Excluding UI & Hardware)

Excluding both the **Frontend UI** and **IoT Hardware Firmware**, we can focus **100% of Phase 1** on building the **Pure Software Analytics Engine, AI Classifiers, Automation Workflows, and Synthetic Datasets**.

---

## 🎯 Phase 1 Pure Software Component Map

```
sentinel/
└── backend/
    ├── app/
    │   ├── api/
    │   │   └── endpoints.py      <-- REST API routes (/score_tip, /optimize_dispatch)
    │   ├── models/
    │   │   └── schemas.py        <-- Pydantic request/response validation models
    │   ├── services/
    │   │   ├── scoring.py        <-- Credibility Matrix & Temporal Decay Engine
    │   │   ├── classifier.py     <-- Naive Bayes Sighting vs Noise Filter
    │   │   ├── terrain.py        <-- Terrain-adjusted mobility & speed limits
    │   │   └── optimizer.py      <-- PuLP Linear Programming Team Dispatch Solver
    │   └── main.py               <-- FastAPI app setup & CORS config
    ├── data/
    │   └── synthetic_tips.json   <-- 250 Synthetic Benchmark Tip Dataset
    └── tests/
        └── test_scoring.py       <-- PyTest mathematical verification suite
```

---

## 📋 What We Will Build Right Now in Phase 1

### 1. Pydantic Validation Schemas (`backend/app/models/schemas.py`)
- `TipSubmissionRequest`: Validates incoming tip JSON (raw text, lat, lng, source type, observation time).
- `ScoredTipResponse`: Returns calculated score (0-100), priority badge (`CRITICAL`, `MEDIUM`, `LOW`), Naive Bayes classification (`SIGHTING` vs `NOISE`), confidence interval, and decay multiplier.
- `DispatchOptimizationRequest` & `Response`: Input team sizes and search zone priority scores; returns optimal PuLP assignments.

### 2. Credibility Matrix & Temporal Decay Engine (`backend/app/services/scoring.py`)
- Implements glass-box scoring formula:
  $$S = (40 \cdot C_{\text{source}} + 35 \cdot V_{\text{spatial}} + 25 \cdot I_{\text{content}}) \times e^{-0.1155 \cdot \Delta t}$$
- Computes Haversine distance, max reachable terrain speeds (Road 5 km/h, Forest 2 km/h, Slope penalty), and 6-hour temporal decay halving.

### 3. Naive Bayes Sighting vs Noise Classifier (`backend/app/services/classifier.py`)
- Trains `scikit-learn` Multinomial Naive Bayes model on sighting keywords (*spotted, saw, walking, blue jacket*) vs social media noise (*hope he is found, please share, pray*).
- Applies $0.1\times$ deprioritization multiplier if text is classified as NOISE.

### 4. PuLP Linear Programming Resource Solver (`backend/app/services/optimizer.py`)
- Solves linear programming assignment problem to match available volunteer search teams to high-priority search zones to maximize total score coverage.

### 5. Automated PyTest Test Suite (`backend/tests/test_scoring.py`)
- Unit tests verifying score outputs, 6-hour decay halving, Haversine accuracy, Naive Bayes predictions, and PuLP solver outputs.

### 6. Synthetic 250-Tip Benchmark Dataset (`backend/data/synthetic_tips.json`)
- 250 realistic tip entries with 15 planted ground-truth sightings near Sector 12, Navi Mumbai (`18.9876° N, 73.0021° E`) for system evaluation.
