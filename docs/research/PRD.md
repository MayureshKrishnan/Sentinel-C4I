# SENTINEL - Product Requirements Document (PRD)

## 1. Executive Summary & Product Vision
**SENTINEL** (Search Intelligence & Tip Evaluation Network for Incident Leads) is an AI-assisted, time-critical missing person search coordination platform designed specifically for the **Golden Window** (the first 24–72 hours post-disappearance).

It transforms unstructured, noisy, multi-channel tip submissions into prioritized, geospatially-scored, terrain-aware search intelligence within seconds. The system operates as an intelligent coordination layer with **zero software licensing cost**, accessible to emergency search coordinators, law enforcement, volunteer search networks, and NGOs.

---

## 2. Target Users & Personas

| Persona | Role | Key Needs | Primary Touchpoint |
| :--- | :--- | :--- | :--- |
| **Incident Coordinator** | Search Lead / Police / Incident Commander | High-level situation map, prioritized leads, resource dispatch optimization, active learning override capabilities. | Desktop Command Dashboard (React + Leaflet) |
| **Field Search Volunteer** | NGO Member / Community Volunteer | Real-time position tracking, quick location verification, low-battery IoT hardware reporting. | Wearable IoT GPS Hardware Node (ESP8266 + NEO-6M) |
| **Public Tipster** | Eyewitness / Citizen | Mobile-friendly, frictionless tip submission form without required app installation or account creation. | Web Form / WhatsApp / Telegram / SMS |

---

## 3. Core Functional Requirements

### FR-1: Multi-Channel Tip Ingestion
* **FR-1.1**: Responsive web form capturing description, observation time, physical traits, clothing, and HTML5 GPS location.
* **FR-1.2**: Webhook endpoints for WhatsApp and SMS tip parsing (via Twilio/MSG91).
* **FR-1.3**: Automated IoT GPS pings from hardware nodes every 60 seconds as `source_type = volunteer`.

### FR-2: Deduplication & Parsing (n8n Workflow)
* **FR-2.1**: Spatial-temporal check against existing tips within 200m radius and 30-minute window.
* **FR-2.2**: Corroboration counter increment for duplicate leads to tighten confidence intervals.
* **FR-2.3**: Timestamp normalization to ISO 8601 UTC and automatic reverse geocoding.

### FR-3: AI & Credibility Scoring Engine (FastAPI)
* **FR-3.1**: Implementation of glass-box scoring formula:
  $$S = (w_1 \cdot C_{\text{source}} + w_2 \cdot V_{\text{spatial}} + w_3 \cdot I_{\text{content}}) \times e^{-\lambda \cdot \Delta t}$$
* **FR-3.2**: Naive Bayes text classification (SIGHTING vs NOISE keyword detection).
* **FR-3.3**: Exponential temporal decay calculation ($\lambda = 0.1155 \implies$ halves every 6 hours).
* **FR-3.4**: Dynamic terrain mobility model integrating IEEE GRSS satellite layers (Sentinel-2 land cover, SRTM DEM slope, ISRO Bhuvan LULC).

### FR-4: Live Command Dashboard (React + Leaflet)
* **FR-4.1**: Real-time map rendering with color-coded priority pins (Red 70+, Amber 35-69, Grey <35, Cyan Volunteer).
* **FR-4.2**: Dynamic density heatmap overlay and convex hull primary search zone polygons.
* **FR-4.3**: Real-time tip feed stream sorted by score with instant map location focus on click.
* **FR-4.4**: PuLP linear programming optimizer displaying team-to-zone dispatch suggestions.
* **FR-4.5**: Timeline scrubber to replay tip density progression over time.

### FR-5: Human-in-the-Loop Active Learning
* **FR-5.1**: Coordinator override interface (`[Upgrade]` / `[Dismiss]`).
* **FR-5.2**: Automated weight retraining ($w_1, w_2, w_3$) based on labeled override feedback.

---

## 4. Non-Functional Requirements (NFR)

* **Performance**: End-to-end tip processing latency $< 1000\text{ms}$ from ingestion to WebSocket map rendering.
* **Cost**: ₹0 software licensing cost. Built exclusively on free-tier services (Supabase, GitHub Pages, Railway/Fly.io) and open data.
* **Availability**: 99.9% uptime during active incident operations.
* **Privacy & Ethics**:
  * No facial recognition models or vector embeddings.
  * No live CCTV video processing.
  * Compliance with GDPR, CCPA, and India DPDP Act 2023.
