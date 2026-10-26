# SENTINEL - Cloud Systems & Infrastructure Architecture

## ☁️ Executive Cloud Overview: **100% Free-Tier Cloud Architecture (₹0 Licensing Cost)**

SENTINEL utilizes a **Decoupled Multi-Cloud Microservices Strategy**. Each component of the system runs on specialized, production-grade cloud infrastructure leveraging generous free-tier allowances.

```
                              +-------------------------------------------------------------+
                              |              SENTINEL CLOUD INFRASTRUCTURE                  |
                              +-------------------------------------------------------------+
                                                             |
         +-------------------+-------------------------------+-------------------+-------------------+
         |                   |                               |                   |                   |
         ▼                   ▼                               ▼                   ▼                   ▼
  [DATABASE CLOUD]    [API BACKEND CLOUD]           [AUTOMATION CLOUD]   [FRONTEND CDN CLOUD]  [SATELLITE API CLOUD]
  **Supabase**        **Railway.app / Fly.io**      **Render.com**       **GitHub Pages**      **Copernicus Cloud**
- PostgreSQL DB     - Python 3.11 + FastAPI         - n8n Automation     - React + Vite UI     - Live Sentinel-2
- PostGIS Spatial   - AI Scoring Microservice         Engine             - CDN + SSL           - Satellite API
- Realtime WS       - PuLP Linear Program Solver    - Webhook Router     - Zero-downtime static
```

---

## 🛠️ Detailed Breakdown of Each Cloud System Used

| Cloud Platform | Service Type | Role in SENTINEL | Free Tier Limit | Cost |
| :--- | :--- | :--- | :--- | :--- |
| **Supabase** | Managed Cloud DB & Realtime WebSockets | Stores `incidents`, `tips`, and `volunteer_nodes`. PostGIS spatial queries & WebSocket push alerts. | 500 MB Database, 50,000 Monthly Active Users | **₹0** |
| **Railway.app / Fly.io** | Cloud Application Hosting | Hosts the Python **FastAPI Analytics Engine** (Scoring formula, Naive Bayes classifier, PuLP solver). | 500 execution hours / month | **₹0** |
| **Render.com** | Workflow Cloud Hosting | Hosts **n8n Community Edition** to handle WhatsApp/SMS webhook ingestion & deduplication. | 750 free hours / month | **₹0** |
| **GitHub Pages / Vercel** | Global CDN Frontend Hosting | Hosts the **React.js Command Dashboard** UI (accessible globally via HTTPS URL). | Unlimited static hosting + SSL | **₹0** |
| **Copernicus Data Space Cloud** | ESA Satellite Data Cloud | Serves live **Sentinel-2 L2A** multi-spectral imagery & NDVI layers on-demand via API. | Unlimited open access requests | **₹0** |

---

## 🔒 Security, Authentication & Data Protection on Cloud

1. **Row-Level Security (RLS)**: Supabase RLS policies ensure public web tipsters can only *write* incoming tips, while search coordinators require **JWT Authentication** to view or modify incident data.
2. **TLS 1.3 Encryption**: All cloud-to-cloud streams (Webhooks, REST APIs, WebSockets) are encrypted via TLS 1.3.
3. **GDPR & India DPDP Act 2023 Compliance**: Raw tip data is stored in isolated Supabase rows; no face embeddings or mass surveillance vectors are processed on the cloud.

---

## 💡 Bulletproof Panel Answer
> *"Our project uses a **decoupled multi-cloud architecture** built entirely on free-tier production platforms: **Supabase** for PostGIS spatial data and real-time WebSockets, **Railway/Fly.io** for our FastAPI scoring backend, **Render** for n8n automation, **GitHub Pages** for our React dashboard CDN, and **ESA Copernicus Cloud** for live satellite API queries—achieving **zero software licensing cost**."*
