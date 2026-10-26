# SENTINEL - Implementation Roadmap & 3-Member Task Division (Phases.md)

## Phase Breakdown & Team Assignment Matrix

| Phase | Core Objective | Member 1 (Most Tech - Backend/AI) | Member 2 (Technical - Frontend/UI) | Member 3 (Least Tech - GIS/HW/Docs) |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | Independent Isolated Dev | FastAPI Microservice & Credibility Scoring Formula | React + Vite UI Shell & Mock Map Components | QGIS Satellite Terrain Layer & Hardware Node Flashing |
| **Phase 2** | DB & Real-Time Setup | Supabase PostGIS DB & FastAPI API Integration | Supabase WebSocket Real-Time Listener Hookup | n8n Deduplication Workflow & Synthetic Test Dataset |
| **Phase 3** | Integration & PuLP | PuLP Linear Programming Resource Solver | Live Tip Feed, Timeline Scrubber & PuLP Strip | Hardware GPS Node Field Connectivity Testing |
| **Phase 4** | Active Learning & Polish | Coordinator Override Weight Retraining Logic | Dark Glassmorphic Styling & UI Micro-Animations | System Integration Testing & Dataset Precision Validation |
| **Phase 5** | Validation & Demo | PyTest Backend Unit & Integration Tests | UI Performance & Mobile View Optimization | Project Documentation, Slide Deck & Live Demo Plan |

---

## Phase 1: Isolated Zero-Dependency Development

### 👤 Member 1 (Backend & AI)
- [ ] Initialize Python FastAPI project structure (`backend/app`).
- [ ] Implement `CredibilityScorer` class evaluating $S = (w_1 C_{\text{source}} + w_2 V_{\text{spatial}} + w_3 I_{\text{content}}) e^{-\lambda \Delta t}$.
- [ ] Build Naive Bayes text classifier (`scikit-learn`) for `SIGHTING` vs `NOISE` classification.

### 👤 Member 2 (Frontend & UI)
- [ ] Initialize React + Vite project structure (`frontend/src`).
- [ ] Build Leaflet.js interactive map with custom color-coded pin markers using local `mock_tips.json`.
- [ ] Build left `SubjectProfile` panel and right `LiveTipFeed` skeleton.

### 👤 Member 3 (GIS & Hardware)
- [ ] Download Sentinel-2 land cover and SRTM DEM tiles for demo area (Navi Mumbai).
- [ ] Preprocess terrain cost raster using QGIS GUI and export GeoTIFF.
- [ ] Assemble NodeMCU ESP8266 + NEO-6M GPS hardware components on breadboard and flash Arduino sketch using Arduino IDE.

---

## Phase 2: Inter-Service Integration Pipeline

```
[Member 3: Synthetic CSV] ---> [Member 3: n8n Workflow] ---> [Member 1: FastAPI Endpoint]
                                                                      │
                                                                      ▼
[Member 2: React Dashboard] <--- [Member 2: WebSocket] <--- [Member 1: Supabase DB]
```

### 👤 Member 1
- [ ] Connect FastAPI to Supabase PostgreSQL database.
- [ ] Expose REST endpoints `/api/v1/score_tip` and `/api/v1/hardware_ping`.

### 👤 Member 2
- [ ] Replace static `mock_tips.json` in React app with dynamic Supabase WebSocket real-time subscription.
- [ ] Implement marker click auto-centering and tip highlighting.

### 👤 Member 3
- [ ] Build n8n deduplication workflow node (200m radius, 30-min window).
- [ ] Generate 200–300 synthetic tips in Excel/CSV for automated testing.

---

## Phase 3: Resource Allocation & Hardware Connection

### 👤 Member 1
- [ ] Implement PuLP linear programming model in FastAPI for optimal volunteer team to search zone assignment.

### 👤 Member 2
- [ ] Build bottom `ResourceAllocationOptimizer` display strip and right `TimelineScrubber` replay control.

### 👤 Member 3
- [ ] Power on physical IoT NodeMCU hardware node via mobile hotspot and verify pings enter pipeline.

---

## Phase 4 & 5: Active Learning, Validation & Demo

* **Member 1**: Implements active learning weight update function upon coordinator score overrides.
* **Member 2**: Finalizes dark navy glassmorphic aesthetic polish and responsive layout.
* **Member 3**: Evaluates Precision@K metrics on synthetic dataset, finalizes presentation deck and demonstration plan.
