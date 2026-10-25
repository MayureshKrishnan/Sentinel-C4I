# SENTINEL V2 — Tactical C4I Decision Support System

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![Leaflet.js](https://img.shields.io/badge/GIS-Leaflet.js-199900.svg)](https://leafletjs.com/)
[![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn%20DBSCAN-F7931E.svg)](https://scikit-learn.org/)
[![Indian Legal Compliance](https://img.shields.io/badge/Compliance-BSA%20Sec--63%20%7C%20CCTNS-darkred.svg)](https://www.mha.gov.in/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/MayureshKrishnan/Sentinel-C4I)

> **Autonomous Multi-Factor Intelligence Triaging, Spatial Kinematics, and Indian Law Enforcement Evidentiary Compliance for Missing Person Search Operations.**

---

## 👥 Engineering Team & Module Distribution

This project is engineered in 3 distinct, decoupled architectural tiers enabling collaborative development:

| Tier / Folder | Lead Responsibilities | Core Technologies |
| :--- | :--- | :--- |
| **`sentinel-frontend/`**<br>*(Member 1)* | **Tactical HUD & Public Ingress Portal**<br>• GIS Leaflet.js Mapping & Tobler Isochrone HUD<br>• 5 Unified Black-Metal Web Consoles<br>• Real-time Audio/Visual Alert Streamers<br>• Academic Project Reports & Diagrams | HTML5, Tailwind CSS, Leaflet.js, WebSockets |
| **`sentinel-backend/`**<br>*(Member 2)* | **Asynchronous API Core & Database**<br>• FastAPI REST API Endpoints & Route Handlers<br>• Bidirectional WebSockets (`/ws/dashboard`)<br>• CCTNS Case Directory & SQLite Database Engine<br>• Production Security Headers & CORS Enforcement | Python 3.10, FastAPI, Uvicorn, SQLite, WebSockets |
| **`sentinel-engine/`**<br>*(Member 3)* | **AI/ML & Legal Evidence Forensics**<br>• Scikit-Learn DBSCAN Density Clustering<br>• Tobler Slope Calculus & Haversine Distance<br>• Suburban Rail (17 stations) & FASTag Toll Corridors<br>• Indic Devanagari Marathi & Hinglish NLP<br>• Section 63 BSA 2023 SHA-256 Court Certificates | Scikit-Learn, NumPy, Math, Re, SHA-256 |

---

## ⚡ Core Technical Innovations

### 1. 3-Layer Autonomous Credibility Engine
Every civilian tip is evaluated through three computational filters before reaching the command console:
* **Layer 1: Topographic Spatial Calculus & Tobler Walking Isochrone**:
  Evaluates pedestrian walking velocity over elevation slope:
  $$W = 6 \cdot e^{-3.5 \cdot |\tan(\theta) + 0.05|}$$
  Calculates maximum theoretical walking perimeters from Last Known Position (LKP) across elapsed time $\Delta t$.
* **Layer 2: Unsupervised Spatial Density Clustering (DBSCAN)**:
  Applies Scikit-Learn DBSCAN ($\varepsilon = 0.5\text{ km}$, $\text{min\_samples} = 2$) using Haversine spherical distance metrics to detect corroborated multi-eyewitness clusters without requiring pre-set cluster counts.
* **Layer 3: Heuristic & Source Credibility Weighting**:
  Integrates reporter reliability coefficients, eyewitness line-of-sight proximity, and biometric hash confirmations.

### 2. Multi-Modal Transit Chokepoint Modeling ($>80\text{ km/h}$ Mobility Solution)
Standard SAR software assumes uniform pedestrian dispersal and collapses when a subject boards a train or vehicle. Sentinel introduces a tripartite velocity gate ($v_{\text{obs}} = \frac{d}{\Delta t}$):
* **Pedestrian Regime ($v \le 6\text{ km/h}$)**: Verified within Tobler walking isochrone polygon.
* **Vehicular Corridor Anomaly ($6 < v \le 110\text{ km/h}$)**: Sighting dynamically correlated against:
  * **17 Mumbai Suburban Railway Stations** (Western & Central Railway corridors: Churchgate, Dadar, Kurla, Andheri, Borivali, Thane, Kalyan, etc.).
  * **5 Mumbai Entry Toll Plazas** (NHAI FASTag plazas: Dahisar, Mulund EEH, Mulund LBS, Vashi, Airoli).
  * Auto-escalates interception recommendations to Highway Patrol and Railway Police units.
* **Physics Reject ($v > 110\text{ km/h}$)**: Discarded as an impossible kinematic outlier and archived to the immutable audit reject log.

### 3. Vernacular Indic NLP Parser (Devanagari Marathi & Hinglish)
Overcomes the Anglo-centric barrier of conventional emergency dispatch systems:
* Processes raw Devanagari script (e.g., *"दादर पश्चिम फूल मार्केट जवळ निळा शर्ट घातलेला मुलगा दिसला, खूप घाबरलेला वाटत होता"*).
* Processes colloquial Romanized Hinglish (*"Bandra station auto stand ke paas dekha..."*).
* Autonomously extracts Indian urban landmarks (*naka, mandir, station, chowk, flower market*), attire, and emotional states (*frightened, injured*).

### 4. Bharatiya Sakshya Adhiniyam (BSA), 2023 Section 63 Digital Court Certificates
Complies with India's new criminal justice framework (effective July 1, 2024, replacing Section 65B of the Indian Evidence Act, 1872):
* Every incoming tip is cryptographically hashed with **SHA-256** at the exact millisecond of ingestion:
  $$\text{Hash}_i = \text{SHA-256}(P_i \parallel \text{Hash}_{i-1})$$
* Generates an official, print-ready statutory certificate under **Section 63(4) BSA, 2023** signed by the System In-Charge for direct submission in Indian Magistrate Courts.
* Cross-referenced with **CCTNS FIR numbers** (`CCTNS FIR-248/2026`) and General Diary (GD) records.

---

## 📁 Repository Structure

```text
Sentinel-C4I/
│
├── sentinel-frontend/                 # [Member 1] UI/UX, Leaflet.js GIS & Reports
│   ├── index.html                     # Landing page with spatial radar & architecture overview
│   ├── dashboard.html                 # Tactical C4I console, live map, triage feed, BSA modal
│   ├── submit_tip.html                # Public civilian portal with Indic quick demos
│   ├── pipeline.html                  # Algorithmic pipeline & terminology glossary
│   ├── architecture.html              # Multi-tier hardware/software system schema
│   ├── Stage_1_Report_Clean.txt       # Complete academic project report draft
│   └── Stage_1_Report.md              # Markdown version of project report
│
├── sentinel-backend/                  # [Member 2] Asynchronous FastAPI Core & DB
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                    # Server endpoints, WebSockets, Security Headers
│   │   └── db_sqlite.py               # SQLite CCTNS schemas & audit ledger
│   ├── requirements.txt               # Backend Python dependencies
│   ├── sentinel.db                    # Pre-seeded database with active Mumbai cases
│   └── .env.example                   # Environment configuration template
│
├── sentinel-engine/                   # [Member 3] AI/ML, Kinematics & Legal Forensics
│   ├── __init__.py
│   ├── indian_c4i.py                  # Suburban Rail (17 stns), FASTag Tolls, Indic NLP, BSA-63
│   ├── ml_clustering.py               # Scikit-Learn DBSCAN clustering engine
│   └── spatial_math.py                # Tobler hiking function, Haversine spherical calculus
│
├── Dockerfile                         # Production multi-stage container
├── render.yaml                        # 1-click cloud deployment blueprint
├── Procfile                           # Process manager definition
└── README.md                          # Platform documentation
```

---

## 🚀 Quickstart Guide

### 1. Clone the repository
```bash
git clone https://github.com/MayureshKrishnan/Sentinel-C4I.git
cd Sentinel-C4I
```

### 2. Set up Virtual Environment & Dependencies
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install -r sentinel-backend/requirements.txt
```

### 3. Launch the Complete Synchronized Platform
```bash
cd sentinel-backend
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

### 4. Access the Platform
* **Command Console**: [http://127.0.0.1:8000/dashboard.html](http://127.0.0.1:8000/dashboard.html)
* **Public Tip Intake**: [http://127.0.0.1:8000/submit_tip.html](http://127.0.0.1:8000/submit_tip.html)
* **Data Pipeline**: [http://127.0.0.1:8000/pipeline.html](http://127.0.0.1:8000/pipeline.html)
* **System Schema**: [http://127.0.0.1:8000/architecture.html](http://127.0.0.1:8000/architecture.html)
* **Interactive API Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## ⚖️ Statutory Legal Compliance Notice
This software implements digital chain of custody mechanisms satisfying **Section 63 of the Bharatiya Sakshya Adhiniyam, 2023** (Act No. 47 of 2023, Ministry of Law and Justice, Government of India). Electronic evidence certificates generated by this platform are cross-referenced with CCTNS FIR registries and signed with cryptographic Merkle hashes for direct admissibility in courts of law.

---

## 📄 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
