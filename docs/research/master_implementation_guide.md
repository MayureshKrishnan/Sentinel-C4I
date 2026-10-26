# SENTINEL - Master Step-by-Step Preparation & Implementation Guide

This guide walks you through the entire lifecycle of building **SENTINEL** from scratch—from installing software tools to delegating tasks among 3 team members, coding, integrating, testing, and presenting to the panel.

---

## 📋 STEP 0: System & Software Prerequisites Checklist

Before writing any code, ensure the team's laptops have the following free tools installed:

### Required Software (Download & Install):
1. **VS Code** (Code editor for Members 1 & 2): [Download VS Code](https://code.visualstudio.com/)
2. **Python 3.11+** (For Member 1): [Download Python](https://www.python.org/downloads/) *(Check "Add Python to PATH" during installation)*
3. **Node.js LTS v18 or v20** (For Member 2): [Download Node.js](https://nodejs.org/)
4. **Arduino IDE 2.x** (For Member 3): [Download Arduino IDE](https://www.arduino.cc/en/software)
5. **CH340 USB Driver** (For Member 3 - required for NodeMCU recognition): [Download Driver](https://sparks.gogo.co.nz/ch340.html)
6. **QGIS 3.x Desktop** (For Member 3): [Download QGIS](https://qgis.org/)
7. **Free Supabase Account** (For Database): [Create Account](https://supabase.com/)

---

## 🚀 STEP 1: Project Workspace Initialization

We will build the complete project inside your designated local directory:
`C:\Users\Mayuresh Krishnan\.gemini\antigravity\scratch\sentinel`

### Workspace Directory Structure:
```
sentinel/
├── backend/            <-- Member 1 (FastAPI, AI Engine, PuLP)
├── frontend/           <-- Member 2 (React.js, Leaflet Map UI)
├── hardware/           <-- Member 3 (Arduino ESP8266 Firmware)
├── n8n/                <-- Member 3 (Workflow JSON)
└── gis/                <-- Member 3 (QGIS Satellite rasters)
```

---

## 👥 STEP 2: Parallel Implementation Execution (Phase 1)

All 3 team members work **simultaneously** on their respective components:

### 👤 MEMBER 1: Backend & AI Engine (`backend/`)
1. **Setup Environment**:
   ```bash
   cd backend
   python -m venv venv
   .\venv\Scripts\activate
   pip install fastapi uvicorn pydantic scikit-learn pulp numpy
   ```
2. **Build `backend/app/services/scoring.py`**:
   Implement formula $S = (40 \cdot C_{\text{source}} + 35 \cdot V_{\text{spatial}} + 25 \cdot I_{\text{content}}) \cdot e^{-0.1155 \cdot \Delta t}$.
3. **Build `backend/app/services/classifier.py`**:
   Train Naive Bayes `SIGHTING` vs `NOISE` text filter.
4. **Build `backend/app/main.py`**:
   Expose API endpoints `/api/v1/score_tip` and `/api/v1/optimize_dispatch`.
5. **Test Backend**: Run `uvicorn app.main:app --reload` and test API via `http://localhost:8000/docs`.

---

### 👤 MEMBER 2: Command Dashboard UI (`frontend/`)
1. **Initialize App**:
   ```bash
   npx -y create-vite@latest frontend --template react
   cd frontend
   npm install leaflet react-leaflet lucide-react @supabase/supabase-js
   ```
2. **Build Mock Data**: Create `frontend/src/data/mock_tips.json` for **100% independent** UI building.
3. **Build Components**:
   - `InteractiveMap.jsx`: Leaflet map with red (70+), amber (35-69), grey (<35), and cyan (volunteer) markers.
   - `SubjectProfile.jsx`: Missing person profile panel (Arjun Mehta, 34, Diabetic alert).
   - `LiveTipFeed.jsx`: Real-time tip list sorted by score.
   - `ResourceOptimizer.jsx`: Bottom strip showing PuLP team assignments.
4. **Style Theme**: Apply dark navy glassmorphic theme in `frontend/src/index.css`.
5. **Test UI**: Run `npm run dev` and view dashboard at `http://localhost:5173`.

---

### 👤 MEMBER 3: Hardware, Satellite GIS & Workflows (`hardware/`, `gis/`, `n8n/`)
1. **Hardware Node Flashing (Arduino IDE GUI)**:
   - Open Arduino IDE -> Preferences -> Add Board URL: `http://arduino.esp8266.com/stable/package_esp8266com_index.json`.
   - Install `esp8266` board package & `TinyGPS++` library.
   - Connect NodeMCU via USB cable, select port, open `hardware/firmware/sentinel_node.ino`, and click **Upload**.
2. **QGIS Satellite Layer Setup (QGIS GUI)**:
   - Open QGIS -> Download Sentinel-2 geotiff & SRTM DEM tile for Navi Mumbai.
   - Load layers -> Compute NDVI -> Export combined `terrain_cost_navi_mumbai.tif`.
3. **n8n Deduplication Workflow Setup**:
   - Install/Run n8n or use free cloud trial -> Import `n8n/deduplication_workflow.json`.
4. **Synthetic Dataset Generation**:
   - Create CSV with 250 realistic tip entries (lat, lng, raw_text, source_type, timestamp) for validation testing.

---

## 🔗 STEP 3: System Integration & Pipeline Hookup (Phase 2)

Once Phase 1 components are individually verified:

1. **Database Setup**:
   - Log into Supabase -> Create new project -> Run PostGIS SQL scripts from [Architecture.md](file:///C:/Users/Mayuresh%20Krishnan/.gemini/antigravity/brain/d0c6925d-c5ef-4717-b37f-829f021b8c46/Architecture.md) in SQL Editor (`incidents`, `tips`, `volunteer_nodes`).
2. **Connect FastAPI to Supabase** (Member 1):
   - Member 1 adds Supabase connection string to FastAPI so computed scores automatically write to database.
3. **Connect React to WebSockets** (Member 2):
   - Member 2 replaces `mock_tips.json` with dynamic Supabase WebSocket real-time subscription (`supabase.channel('public:tips').on(...)`).
4. **Connect Hardware & n8n** (Member 3):
   - Member 3 powers on ESP8266 node via phone hotspot -> Pings enter n8n -> n8n routes to FastAPI -> FastAPI writes to Supabase -> React UI map updates pin in under 1 second!

---

## 📊 STEP 4: Validation & Presentation Preparation

1. **Run Precision@K Test**: Feed Member 3's 250 synthetic tips into the pipeline and verify top 20% scored leads cluster around true ground-truth position.
2. **Hardware Live Field Test**: Carry Unit B outdoors; verify live movement coordinates update on Member 2's command map screen.
3. **Final Panel Demo Walkthrough**:
   - Show subject profile (Arjun Mehta).
   - Simulate incoming WhatsApp/Web tip -> Watch score 91 push instantly to map.
   - Demonstrate PuLP Optimizer output string.
   - Showcase Hardware Node live GPS pings.
