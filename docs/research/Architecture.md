# SENTINEL - Architecture Specification Document

## 1. System Flow & Data Pipeline Architecture

```
[Ingestion Channels]
├── Web Form (React + HTML5 Geo)
├── WhatsApp / SMS (Twilio & MSG91)
├── IoT GPS Hardware Nodes (ESP8266 + NEO-6M)
└── Telegram Bot API
        │
        ▼
[n8n Workflow Engine (Automation Layer)]
├── Deduplication Check (200m radius, 30-min window)
├── Schema Normalization (ISO 8601 UTC)
└── Webhook POST Payload Dispatcher
        │
        ▼
[FastAPI Analytics Engine (Intelligence Layer)]
├── Naive Bayes Noise Filter (SIGHTING vs NOISE)
├── IEEE GRSS Satellite Terrain Mobility Evaluator (PostGIS Raster)
├── Multi-Factor Credibility Scoring (Source + Spatial + Content)
├── Exponential Temporal Decay Application (Score Halves / 6 hrs)
└── PuLP Linear Programming Resource Allocator
        │
        ▼
[Supabase Database & Real-Time Broadcast]
├── PostgreSQL + PostGIS Spatial DB (Persistent Storage)
└── Supabase Realtime WebSockets (<1s Push)
        │
        ▼
[React Command Dashboard (Presentation Layer)]
├── Live Map & Priority Markers (Leaflet.js + OSM)
├── Priority Heatmap Overlay & Convex Hull Zones
├── Real-time Tip Feed & Subject Profile Panel
├── Volunteer GPS Live Tracker Panel
└── Timeline Scrubber & PuLP Optimizer Output Strip
```

---

## 2. Technical Stack Matrix

| Layer | Primary Technology | Supplementary Libraries / APIs | Cost |
| :--- | :--- | :--- | :--- |
| **Frontend UI** | React.js (Vite) | Leaflet.js, OpenStreetMap, Tailwind CSS, Lucide Icons | Free |
| **Backend API** | Python 3.11 + FastAPI | Pydantic, scikit-learn (Naive Bayes), PuLP (Solver) | Free Tier |
| **Automation** | n8n Community Edition | Webhook nodes, JSON parser, HTTP Request nodes | Free Tier / Self-Host |
| **Database** | Supabase (PostgreSQL) | PostGIS spatial extension, WebSockets Realtime | Free Tier (500MB) |
| **GIS / Satellite** | IEEE GRSS Open Layers | Sentinel-2 (Copernicus), SRTM DEM 30m, ISRO Bhuvan | Free |
| **Hardware IoT** | Arduino C++ | TinyGPS++, ESP8266WiFi, ESP8266HTTPClient | ₹1,120 Hardware |

---

## 3. Recommended Repository File & Directory Structure

```
sentinel/
├── README.md
├── PRD.md
├── Architecture.md
├── Rules.md
├── Phases.md
├── Design.md
├── Memory.md
│
├── frontend/                     # React + Vite Command Dashboard
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Map/             # Leaflet Map, Heatmap & Pin layers
│   │   │   ├── Profile/         # Missing subject profile panel
│   │   │   ├── TipFeed/         # Real-time lead feed stream
│   │   │   ├── Volunteer/       # Hardware GPS tracker panel
│   │   │   ├── Optimizer/       # PuLP resource allocation strip
│   │   │   └── Timeline/        # Hour-by-hour replay scrubber
│   │   ├── hooks/               # Supabase WebSocket realtime listeners
│   │   ├── services/            # API client service calls
│   │   ├── App.jsx
│   │   ├── index.css            # Custom CSS & Glassmorphism Design System
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── backend/                      # FastAPI Microservice & AI Engine
│   ├── app/
│   │   ├── api/                 # API endpoints (scoring, pings, optimization)
│   │   ├── core/                # System configuration & environment variables
│   │   ├── services/
│   │   │   ├── scoring.py       # Credibility matrix & temporal decay formula
│   │   │   ├── classifier.py    # Naive Bayes noise vs sighting classifier
│   │   │   ├── terrain.py       # GRSS satellite PostGIS lookup
│   │   │   └── optimizer.py     # PuLP linear programming assignment solver
│   │   ├── models/              # Pydantic schemas & database tables
│   │   └── main.py              # FastAPI app initialization & CORS setup
│   ├── tests/                   # PyTest unit test suite
│   └── requirements.txt
│
├── hardware/                     # ESP8266 IoT Firmware & Diagrams
│   ├── firmware/
│   │   └── sentinel_node.ino    # Arduino C++ firmware for NodeMCU + NEO-6M
│   └── schematics/
│       └── wiring_diagram.png
│
├── n8n/                          # Automation Workflows
│   └── deduplication_workflow.json
│
└── gis/                          # GRSS Preprocessing Scripts
    ├── terrain_cost_builder.py   # Rasterio NDVI + DEM slope raster generator
    └── sample_patch_navi_mumbai.tif
```
