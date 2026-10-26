# SENTINEL - Revised 5-Phase Roadmap & Team Task Allocation

## Executive Skill Alignment

This updated roadmap aligns the implementation of **SENTINEL** precisely with your team's technical comfort levels:

```
                                  SENTINEL PLATFORM
                                          |
        +---------------------------------+---------------------------------+
        |                                 |                                 |
        ▼                                 ▼                                 ▼
[MEMBER 1: MOST TECHNICAL]       [MEMBER 2: TECHNICAL]            [MEMBER 3: LEAST TECHNICAL]
Backend & AI Core                Frontend & UI Engineering        GIS, Hardware & Workflows
- FastAPI & REST Microservices   - React.js + Vite Application     - Satellite QGIS Preprocessing
- Credibility Scoring Math       - Leaflet Interactive Map        - ESP8266 Hardware Flashing
- Naive Bayes AI Classifier      - Real-time WebSockets Sync      - n8n Automation Workflows
- PuLP Linear Program Solver     - Dashboard Components           - Synthetic Datasets & Slides
- PyTest & Supabase DB           - Dark Glassmorphism Theme       - Presentation & Demo Setup
```

---

## 👥 Task Allocation by Skill Level

### 👤 Member 1 (Most Technical Lead)
**Role**: **Backend Architect & AI Intelligence Lead**  
**Focus**: Complex Mathematics, Algorithms, Database Schemas, API Endpoints, Automated Testing

* **Phase 1**: Build Python FastAPI backend, Credibility Scoring Formula ($S = (40 C_{\text{src}} + 35 V_{\text{sp}} + 25 I_{\text{cnt}}) e^{-\lambda \Delta t}$), Naive Bayes noise classifier, and PyTest test suite.
* **Phase 2**: Connect FastAPI to Supabase PostgreSQL + PostGIS database.
* **Phase 3**: Build PuLP linear programming resource allocation optimizer (`optimizer.py`).
* **Phase 4**: Implement active learning score override weight retraining algorithm.
* **Phase 5**: Perform system stress testing, concurrency validation, and backend security audits.

---

### 👤 Member 2 (Technical Lead)
**Role**: **Frontend Architect & UI Engineer**  
**Focus**: User Interface, WebSockets, Interactive Maps, React Components

* **Phase 1**: Initialize React + Vite application, build Leaflet map shell with priority color markers (Red 70+, Amber 35-69, Grey <35, Cyan Volunteer) using local `mock_tips.json`.
* **Phase 2**: Connect React UI to Supabase Realtime WebSockets for `< 1s` push updates.
* **Phase 3**: Build bottom `ResourceAllocationOptimizer` strip and right `TimelineScrubber` replay control.
* **Phase 4**: Apply dark glassmorphic UI design system (`Design.md`), smooth pin bounce micro-animations, and responsive layout polish.
* **Phase 5**: Perform frontend browser compatibility testing, mobile layout optimization, and UI latency checks.

---

### 👤 Member 3 (Least Technical Coordinator)
**Role**: **GIS Satellite, IoT Hardware & Workflow Coordinator (GUI / Accessible Tech)**  
**Focus**: QGIS GUI Processing, Arduino IDE Flashing, Visual n8n Workflows, Documentation, PPT & Demo Setup

* **Phase 1**: 
  - Download Sentinel-2 L2A & SRTM DEM geotiff tiles for Navi Mumbai.
  - Process terrain cost raster using **QGIS GUI software** (no coding).
  - Connect NodeMCU ESP8266 + NEO-6M GPS hardware components on breadboard and flash pre-written sketch via **Arduino IDE GUI**.
* **Phase 2**: Import visual `n8n/deduplication_workflow.json` into n8n and test 200m spatial / 30-min temporal rules.
* **Phase 3**: Power on physical IoT NodeMCU hardware node via mobile hotspot and verify live GPS pings enter the pipeline.
* **Phase 4**: Generate 250 realistic tip entries in Excel/CSV for synthetic benchmark testing.
* **Phase 5**: Evaluate Precision@K metrics, prepare project poster/slides, and organize live outdoor demonstration.

---

## 🗓️ Revised 5-Phase Master Timeline Matrix

| Phase | Phase Name | Member 1 (Most Tech) | Member 2 (Technical) | Member 3 (Least Tech) |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | **Isolated Zero-Dependency Dev** | FastAPI Backend, Scoring Formula & Naive Bayes Classifier | React UI Layout, Leaflet Map & Mock Tips JSON | QGIS Terrain Setup & Arduino Hardware Node Flashing |
| **Phase 2** | **Supabase DB & Real-Time Sync** | Connect FastAPI to Supabase PostgreSQL/PostGIS DB | Connect React UI to Supabase Realtime WebSockets | Setup n8n Deduplication Workflow & Generate CSV Data |
| **Phase 3** | **Resource Allocation & Hardware** | Build PuLP LP Solver for Volunteer Team Allocation | Build PuLP UI Strip & Timeline Replay Scrubber | Field Test IoT Hardware Node Pings via Hotspot |
| **Phase 4** | **Active Learning & UI Polish** | Implement Coordinator Override Weight Retraining | Dark Glassmorphism Styling & Micro-Animations | Compute Precision@K Metrics on Synthetic Dataset |
| **Phase 5** | **Validation & Panel Presentation** | PyTest Backend Unit & Integration Tests | Frontend Mobile & Latency Optimization | Finalize Slide Deck, Poster & Live Demo Setup |

---

## 📑 Updated Document References
* Detailed skill division plan: [team_implementation_plan.md](file:///C:/Users/Mayuresh%20Krishnan/.gemini/antigravity/brain/d0c6925d-c5ef-4717-b37f-829f021b8c46/team_implementation_plan.md)
* 5-Phase master roadmap: [Phases.md](file:///C:/Users/Mayuresh%20Krishnan/.gemini/antigravity/brain/d0c6925d-c5ef-4717-b37f-829f021b8c46/Phases.md)
* Active progress tracker: [Memory.md](file:///C:/Users/Mayuresh%20Krishnan/.gemini/antigravity/brain/d0c6925d-c5ef-4717-b37f-829f021b8c46/Memory.md)
