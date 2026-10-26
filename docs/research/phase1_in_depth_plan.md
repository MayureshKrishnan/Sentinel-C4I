# SENTINEL - Phase 1 Deep-Dive Technical Implementation Plan

This document provides a comprehensive, line-by-line technical specification of everything we will build in **Phase 1: Pure Software Core**.

---

## 🎯 Phase 1 Core Objective

Build an isolated, robust, mathematically verified **Python FastAPI microservice** that accepts raw public/volunteer tip submissions, computes credibility scores using multi-vector spatial-temporal decay equations, filters social media noise with Naive Bayes, and optimizes search team dispatches using PuLP Linear Programming.

---

## 🏛️ Phase 1 Software Architecture & Module Breakdown

```
sentinel/backend/
├── app/
│   ├── main.py                  <-- FastAPI App Initialization & Route Registration
│   ├── models/
│   │   └── schemas.py            <-- Pydantic Data Models & Validation Rules
│   └── services/
│       ├── scoring.py            <-- Credibility Scoring & Exponential Decay Engine
│       ├── classifier.py         <-- Naive Bayes Sighting vs Noise Classifier
│       ├── terrain.py            <-- Terrain Mobility Speed Evaluator
│       └── optimizer.py          <-- PuLP Linear Programming Team Dispatch Solver
├── data/
│   └── synthetic_tips_250.json   <-- 250 Synthetic Benchmark Tip Dataset
└── tests/
    └── test_scoring.py           <-- PyTest Automated Verification Suite
```

---

## 🔬 In-Depth Module Specifications

### Module 1: Data Schemas (`backend/app/models/schemas.py`)
Defines strict Pydantic v2 data validation schemas to ensure API payload integrity:

* `TipSubmission`: Input model containing `source_type` (`responder`, `volunteer`, `public_verified`, `anonymous`), `latitude`, `longitude`, `observation_time` (ISO 8601), and `raw_text`.
* `TipScoreResponse`: Output model returning calculated `score` ($0-100$), `priority` (`CRITICAL`, `MEDIUM`, `LOW`), `is_noise` (boolean), `confidence_interval` (e.g., `[68, 79]`), and factor breakdowns ($C_{\text{source}}, V_{\text{spatial}}, I_{\text{content}}$).
* `DispatchOptimizationInput`: Accepts zone priority scores, zone areas, team sizes, and available volunteer count.
* `DispatchOptimizationOutput`: Returns optimal team-to-zone assignment pairings (e.g., `Zone Sector-12 [Score 91] -> Team Alpha (3 members)`).

---

### Module 2: Credibility Scoring Engine (`backend/app/services/scoring.py`)
Implements the master mathematical formulation:

$$S = \left( w_1 \cdot C_{\text{source}} + w_2 \cdot V_{\text{spatial}} + w_3 \cdot I_{\text{content}} \right) \times e^{-\lambda \cdot \Delta t}$$

1. **Source Reliability Vector ($C_{\text{source}}$)**:
   - First Responder = $1.0$ | Field Volunteer = $0.8$ | Verified Public = $0.5$ | Anonymous = $0.2$
2. **Spatial Proximity Vector ($V_{\text{spatial}}$)**:
   - Computes Haversine distance $D(LKP, Tip)$.
   - Evaluates max reachable radius $R_{\text{max}} = v_{\text{terrain}} \times \Delta t$.
   - Caps speed based on surface type (Paved Road = $5 \text{ km/h}$, Forest = $2 \text{ km/h}$, Water = $0 \text{ km/h}$, Slope penalty for $>30^\circ$).
   - Returns $V_{\text{spatial}} = \max\left(0, 1 - \frac{D}{R_{\text{max}}}\right)$.
3. **Content Richness Vector ($I_{\text{content}}$)**:
   - Keyword scoring: Clothing (+0.35), Physical features (+0.35), Landmark/Direction (+0.30).
   - Multiplied by Naive Bayes noise score multiplier ($1.0\times$ for Sighting, $0.1\times$ for Noise).
4. **Exponential Temporal Decay ($e^{-\lambda \cdot \Delta t}$)**:
   - Half-life $T_{1/2} = 6 \text{ hours} \implies \lambda = \frac{\ln(2)}{6} \approx 0.1155 \text{ hr}^{-1}$.
   - Score automatically halves every 6 hours post-observation.

---

### Module 3: Naive Bayes Noise Filter (`backend/app/services/classifier.py`)
* Uses `scikit-learn`'s `MultinomialNB` with `CountVectorizer`.
* Trained on synthetic corpus:
  - **SIGHTING**: *spotted, saw, walking, blue jacket, near bus stop, heading north, timestamp*.
  - **NOISE**: *hope he is found, please share, pray, post on facebook, retweet, news link*.
* If text is classified as `NOISE`, applies $0.1\times$ multiplier to $I_{\text{content}}$, de-prioritizing social media spam without discarding it completely.

---

### Module 4: PuLP Resource Allocation Solver (`backend/app/services/optimizer.py`)
* Formulates integer linear programming problem using Python `PuLP` solver:
  $$\max \sum_{z=1}^{N} \sum_{m=1}^{M} S_z \cdot x_{z,m}$$
* Constrained by volunteer team capacity $\sum_{z} t_m x_{z,m} \le \text{Capacity}_m$.
* Calculates optimal team assignments in milliseconds.

---

### Module 5: Automated PyTest Suite (`backend/tests/test_scoring.py`)
* **Test 1**: Verify temporal decay halving (Score at 0h vs 6h vs 12h).
* **Test 2**: Verify Haversine distance & terrain speed capping.
* **Test 3**: Verify Naive Bayes noise classification accuracy.
* **Test 4**: Verify PuLP solver returns valid binary team allocations.

---

### Module 6: 250 Synthetic Benchmark Dataset (`backend/data/synthetic_tips_250.json`)
* JSON dataset containing 250 simulated tips with 15 planted ground-truth sightings near Sector 12, Navi Mumbai (`18.9876° N, 73.0021° E`).
* Used to test backend performance and benchmark score clustering.
