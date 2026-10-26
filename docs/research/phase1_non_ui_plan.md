# SENTINEL - Phase 1 Execution Plan (Excluding UI)

Since you are researching the frontend UI separately, we can focus **100% of Phase 1** on building and solidifying the **Backend Intelligence Engine, Satellite Processing, and IoT Hardware Firmware**.

---

## 🎯 Phase 1 Non-UI Task Division

```
                                [PHASE 1: NON-UI EXECUTION]
                                             |
                   +-------------------------+-------------------------+
                   |                                                   |
                   ▼                                                   ▼
       [STREAM 1: BACKEND & AI ENGINE]                      [STREAM 2: GIS, HARDWARE & WORKFLOWS]
       (Member 1 Focus)                                     (Member 3 Focus)
  1. FastAPI Microservice Core Setup                   1. Download & Process Satellite Rasters (QGIS)
  2. Mathematical Credibility Scoring Formula          2. Flash NodeMCU ESP8266 IoT Hardware Firmware
  3. Naive Bayes Sighting vs Noise Classifier          3. Build n8n Deduplication Workflow JSON
  4. PyTest Unit Verification Suite                    4. Generate Synthetic Test Dataset (CSV/JSON)
```

---

## 🛠️ Detailed Phase 1 Deliverables & Code Modules

### 🔹 Stream 1: Backend API & AI Engine (Member 1 Focus)

1. **FastAPI Microservice Setup** (`backend/app/main.py`):
   - Project directory initialization, Pydantic schemas, and CORS setup.
2. **Mathematical Credibility Scoring Module** (`backend/app/services/scoring.py`):
   - Implements $S = (40 \cdot C_{\text{source}} + 35 \cdot V_{\text{spatial}} + 25 \cdot I_{\text{content}}) \times e^{-0.1155 \cdot \Delta t}$.
   - Computes Haversine distance, temporal decay halving (6h), and priority routing (70+ CRITICAL, 35-69 MEDIUM, <35 LOW).
3. **Naive Bayes Sighting vs Noise Classifier** (`backend/app/services/classifier.py`):
   - Trains `scikit-learn` Multinomial Naive Bayes model on sighting keywords vs social media noise phrases.
4. **PyTest Mathematical Verification Suite** (`backend/tests/test_scoring.py`):
   - Automated unit tests to verify scoring accuracy, halving decay times, and edge cases.

---

### 🔹 Stream 2: GIS, Hardware Firmware & Workflows (Member 3 Focus)

1. **Satellite Terrain Preprocessing (QGIS GUI)**:
   - Download Sentinel-2 L2A & SRTM DEM tiles for Navi Mumbai.
   - Preprocess land cover (NDVI) & elevation slope ($\theta > 30^\circ$) into a GeoTIFF raster file in `gis/`.
2. **NodeMCU ESP8266 IoT Hardware Firmware** (`hardware/firmware/sentinel_node.ino`):
   - Arduino C++ code with `TinyGPS++` & `ESP8266HTTPClient` broadcasting GPS pings every 60s to FastAPI.
3. **n8n Deduplication Workflow** (`n8n/deduplication_workflow.json`):
   - Constructs visual n8n workflow for 200m spatial radius and 30-minute temporal deduplication.
4. **Synthetic Test Benchmark Dataset** (`backend/data/synthetic_tips_250.json`):
   - Creates a 250-entry test dataset with ground-truth sightings for pipeline testing.

---

## 🚀 Immediate Next Action

We can generate the actual working codebase for all Phase 1 non-UI modules inside:
`C:\Users\Mayuresh Krishnan\.gemini\antigravity\scratch\sentinel\`

Shall I generate the **Backend FastAPI Scoring Engine**, **PyTest Test Suite**, and **NodeMCU Arduino Firmware** code files right now?
