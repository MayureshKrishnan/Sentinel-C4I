# SENTINEL: Search Intelligence & Tip Evaluation Network for Incident Leads

## Project Abstract & Core Specification

**Institute**: S.I.E.S. Graduate School of Technology  
**Department**: Electronics & Computer Science (TE-ECS, Sem-6, 2026–27)  
**Author**: Mayuresh  
**Project Role**: AI-Assisted, Time-Critical Missing Person Search Coordination Platform  

---

### 1. Executive Summary & Objective
**SENTINEL** is an open-source, zero-software-licensing-cost search intelligence and data orchestration network designed to optimize missing person search and rescue (SAR) operations during the **Golden Window** (the initial 24–72 hours post-disappearance).

The system acts as an intelligent bridge between noisy, multi-channel public tip submissions (Web, WhatsApp, Telegram, SMS, IoT GPS hardware nodes) and field search command centers. By transforming unstructured, high-volume inputs into geospatially-scored, terrain-adjusted priority leads within seconds, SENTINEL eliminates cognitive fatigue and manual triage bottlenecks for emergency response teams.

---

### 2. Thrust Area Alignment
1. **Primary**: **Geoscience and Remote Sensing Applications (GRSS)**
   - Integration of multi-spectral satellite imagery (Sentinel-2 land cover), digital elevation models (SRTM DEM 30m), and ISRO Bhuvan Land Use/Land Cover (LULC) maps to construct dynamic terrain cost models.
2. **Secondary**: **Agentic AI (Human-in-the-Loop Active Learning)**
   - Continuous model optimization via coordinator score overrides (upgrades/dismissals), retraining weights $w_1, w_2, w_3$ post-incident to adapt to regional tip reliability.
3. **Tertiary**: **Explainable & Interpretable AI (XAI)**
   - Fully glass-box mathematical scoring formula with explicit confidence intervals (`68–79 HIGH CONFIDENCE`), preventing black-box decision opaque risks during critical operations.

---

### 3. Problem Statement & Bottlenecks
During emergency SAR incidents, coordination centers are inundated with hundreds or thousands of unverified tips. Key operational failure modes addressed by SENTINEL:
* **Information Overload**: Duplicate tips across multiple channels without cross-platform deduplication.
* **Lack of Objective Prioritization**: Subjective human triage prone to cognitive bias and panic noise.
* **Coordination & Dispatch Lag**: Reliance on manual spreadsheets, radio relays, and phone calls.
* **Prohibitive Infrastructure Costs**: Commercial SAR tools cost lakhs in licensing, putting them out of reach for NGOs, local police stations, and volunteer teams.
* **Flat Terrain Assumption**: Existing spatial tools treat distances as isotropic uniform circles, ignoring terrain obstacles (forests, rivers, steep slopes).

---

### 4. Decoupled Pipeline Architecture
SENTINEL is built on an event-driven, decoupled microservices architecture:
1. **Ingestion Layer**: React Web Form, Twilio WhatsApp API, Twilio/MSG91 SMS webhook, Telegram Bot API, ESP8266 IoT GPS Hardware Nodes.
2. **Automation Layer (n8n Engine)**: Normalizes incoming inputs, performs spatial-temporal deduplication (200m radius, 30-min window), and routes parsed JSON payloads to FastAPI.
3. **Intelligence Layer (FastAPI + scikit-learn + PuLP)**: Runs Naive Bayes noise filtering, computes the multi-vector Credibility Scoring Matrix with exponential temporal decay, and solves linear program dispatch optimization for search zones.
4. **Storage & Real-Time Sync (Supabase PostgreSQL + PostGIS)**: Stores spatial points, terrain rasters, and broadcasts state updates via WebSockets in under 1 second.
5. **Presentation Layer (React + Leaflet.js)**: Live interactive Command Dashboard featuring heatmaps, convex hull search zones, live tip feeds, volunteer tracking, timeline scrubber, and resource allocation outputs.

---

### 5. Credibility Scoring Formula & Decision Matrix
Each lead receives a score $S \in [0, 100]$:
$$S = (w_1 \cdot C_{\text{source}} + w_2 \cdot V_{\text{spatial}} + w_3 \cdot I_{\text{content}}) \times e^{-\lambda \cdot \Delta t}$$

* **Baseline Weights**: $w_1 = 40$ (Source Reliability), $w_2 = 35$ (Spatial Proximity), $w_3 = 25$ (Content Richness). $\sum w_i = 100$.
* **Temporal Decay Rate**: $\lambda \approx 0.1155$ (score halves every 6 hours from observation timestamp).
* **Source Weights ($C_{\text{source}}$)**: First Responder = 1.0, Field Volunteer = 0.8, Verified Public = 0.5, Anonymous = 0.2.
* **Spatial Proximity ($V_{\text{spatial}}$)**: Haversine distance relative to Last Known Position (LKP) constrained by terrain max speed (Forest = 2 km/h, Road = 5 km/h, Water = Impassable).
* **Content Richness ($I_{\text{content}}$)**: Clothing features (+0.35), physical attributes (+0.35), direction/landmark hints (+0.30). Applied with a $0.1\times$ multiplier if Naive Bayes flags the text as noise.

#### Priority Routing Table:
* **70 – 100 (CRITICAL)**: Immediate WebSocket alert & pin rendering on live command map.
* **35 – 69 (MEDIUM)**: Queue for coordinator manual review.
* **0 – 34 (LOW)**: Archived for background spatial clustering queries.

---

### 6. Hardware IoT Volunteer Nodes
Low-cost hardware trackers push live coordinator/volunteer positions into the pipeline every 60s as `source_type = volunteer` ($C_{\text{source}} = 0.8$):
* **Unit A (Gateway Node)**: NodeMCU ESP8266 V3 + NEO-6M GPS (USB powered via coordinator laptop).
* **Unit B (Field Node)**: NodeMCU ESP8266 V3 + NEO-6M GPS + 18650 3.7V 2200mAh Li-ion battery + SS-12D00 power switch.
* **Total Hardware Cost**: ₹1,120 (~$13 USD).

---

### 7. Ethical Guardrails & Compliance
* **No Facial Recognition**: Images stored raw without feature vector embeddings.
* **No Live CCTV Video Processing**: Accepts text and GPS inputs only.
* **No Autonomous Law Enforcement Dispatch**: Human-in-the-loop advisory design.
* **Privacy & Security**: Row-Level Security (RLS) on Supabase, TLS 1.3 encryption, and compliance with DPDP Act 2023 / GDPR.
