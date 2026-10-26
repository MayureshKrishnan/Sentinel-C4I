# 🌐 SENTINEL: Team Onboarding & Project Context

Welcome to the **Sentinel Project**. This document serves as the master onboarding guide for all team members. It explains what we are building, the problem we are solving, the architecture we are using, and precisely what each member is responsible for.

---

## 1. What is Sentinel?
**Sentinel** is an AI-powered Tactical Command Center designed for disaster response and the discovery/management of "hidden gems" (undocumented heritage sites, natural wonders, etc.). 

**The Problem:** During disasters or when unverified discoveries are reported on social media, authorities are overwhelmed with noise, fake reports, and a lack of real-time ground truth. This leads to wasted resources and delayed responses.

**The Solution:** Sentinel solves this by fusing real-time crowd-sourced tips with live IoT hardware telemetry and AI credibility scoring. It automatically filters out fake reports, visually maps the valid ones on a 3D globe, and mathematically calculates the most efficient way to deploy volunteer teams.

---

## 2. Core Features (The "Wow" Factor)
1. **AI Credibility Scoring:** Every incoming tip is run through a mathematical formula and a Naive Bayes classifier to assign a "Trust Score" (0-100%). Fake reports are instantly dropped.
2. **Resource Allocation Optimizer:** When a valid event is confirmed, a linear programming algorithm (PuLP) automatically calculates which volunteer team should be deployed based on distance, terrain difficulty, and team availability.
3. **Hardware Integration:** We are building custom IoT nodes (using cheap ESP8266 + GPS modules) that local volunteers can carry. These ping the dashboard in real-time with their exact coordinates.
4. **Surreal Command Center UI:** A high-end, dark-mode, glassmorphic React dashboard featuring a 3D interactive Deck.gl globe that visualizes the data in real-time via WebSockets.

---

## 3. Technology Stack Architecture

We are building this with a modern, decoupled architecture to allow all three members to work simultaneously without blocking each other.

* **Frontend (UI):** React.js + Vite + Tailwind CSS + Framer Motion + Deck.gl (3D Maps).
* **Backend (API & AI):** Python + FastAPI + PuLP (Linear Programming) + scikit-learn (Naive Bayes).
* **Database (Storage & Sync):** Supabase (PostgreSQL + PostGIS for spatial data + Realtime WebSockets).
* **Hardware & Workflow:** NodeMCU ESP8266 + NEO-6M GPS modules, Arduino IDE (C++), QGIS (for satellite terrain processing), and n8n (for visual automation workflows).

---

## 4. Team Task Allocation (Who is doing what?)

The project is split into 5 phases. To ensure we execute perfectly, tasks are divided strictly based on technical expertise.

### 🧑‍💻 Member 1 (Most Technical): Backend Architect & AI Intelligence Lead
**Your Mission:** Build the "brain" of Sentinel.
* **API Engine:** Write the Python FastAPI backend to handle incoming data.
* **The Math:** Implement the Credibility Scoring Formula: $S = (w_1C + w_2V + w_3I)e^{-\lambda\Delta t}$ (Factoring in source credibility, spatial verification, and time-decay).
* **The AI:** Build a Naive Bayes classifier to detect "noise" or fake reports.
* **The Logic:** Build the `optimizer.py` script using PuLP to mathematically assign the closest available volunteer teams to incoming alerts, factoring in terrain cost.
* **Database Setup:** Manage the Supabase PostgreSQL database and PostGIS spatial queries.

### 🎨 Member 2 (Technical): Frontend Architect & UI Engineer
**Your Mission:** Build the "face" of Sentinel. *(Note: Phase 1 of this is already completed!)*
* **The Shell:** Build the React + Vite application architecture.
* **3D Visualization:** Implement the Deck.gl persistent 3D globe that seamlessly transitions between pages.
* **Command Center UI:** Build the Dashboard components (Live Telemetry, Incoming Feed, Resource Allocation strip) using a dark "Obsidian & Neon Cyan" glassmorphic aesthetic.
* **Real-time Sync:** Connect the UI to Supabase via WebSockets so the dashboard updates instantly (sub-second latency) without needing to refresh the page.

### 🌍 Member 3 (Least Technical): GIS, Hardware & Workflow Coordinator
**Your Mission:** Build the "ground truth" of Sentinel using accessible, GUI-based tools.
* **GIS (Maps):** Download free Sentinel-2 L2A satellite data and SRTM DEM topography maps. Use QGIS (visual software) to process these into terrain maps.
* **Hardware:** Assemble the physical IoT nodes by plugging the NodeMCU ESP8266 and GPS module into a breadboard. Use the Arduino IDE to flash pre-written code onto the boards.
* **Workflows:** Set up visual automation flows using `n8n` to handle data deduplication (e.g., if two reports come from within 200m in 30 minutes, merge them).
* **Presentation:** Generate synthetic mock data (CSV files) for testing, build the final presentation slides, and manage the live hardware demonstration during the pitch.

---

## 5. How We Collaborate
* **Independence:** Member 1 can build the FastAPI backend locally. Member 2 can build the UI using hardcoded `mock.json` data. Member 3 can build the hardware and workflows independently. 
* **Integration (Phase 2):** We will connect everything together via Supabase. Member 1 writes data to Supabase. Member 2 reads data from Supabase. Member 3's hardware pings data into Supabase.

**Let's get to work.**
