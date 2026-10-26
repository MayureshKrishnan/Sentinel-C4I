# SENTINEL: Live Command Dashboard Specification

## UI Architecture & Layout Grid

The SENTINEL Live Command Dashboard is designed as a single-page, zero-latency emergency command UI built with **React**, **Tailwind CSS / Custom Glassmorphism**, **Leaflet.js**, and **Supabase Realtime WebSockets**.

```
+---------------------------------------------------------------------------------------------------+
|  SENTINEL EMERGENCY COMMAND CENTER | INCIDENT #2026-NM01 | STATUS: ACTIVE | GOLDEN WINDOW: 14h 22m|
+------------------------------------+------------------------------------+-------------------------+
|                                    |                                    |                         |
|  LEFT PANEL: SUBJECT PROFILE       | CENTER PANEL: INTERACTIVE MAP      | RIGHT PANEL: LIVE FEED  |
|                                    | (Leaflet.js + OpenStreetMap)       |                         |
|  [ Photo Placeholder ]             |                                    | [91] Responder (Palm)   |
|  Name: Arjun Mehta                 |  - Color-coded Pins:              | [78] Volunteer (Sec 12) |
|  Age: 34                           |    * RED: Critical (70+)         | [55] Public (Park Gate) |
|  LKP: Sector 12, Navi Mumbai       |    * AMBER: Medium (35-69)       |                         |
|  LKP Time: 14:32 IST               |    * GREY: Low (<35)            |-------------------------|
|  Medical: Diabetic (Urgent ⚠)      |    * CYAN: Volunteer Node       | VOLUNTEER TRACKER       |
|  Clothing: Blue jacket, dark jeans |  - Priority Heatmap Overlay        | Unit A: 18.9876, 73.0021|
|  Physical: 5'10", black backpack   |  - Convex Hull Search Boundaries   | Unit B: 18.9912, 73.0045|
|                                    |  - Confidence Zone Banner:         | Last ping: 14s ago      |
|                                    |    "3 corroborating tips -         |                         |
|                                    |     HIGH CONFIDENCE [71-88]"       |-------------------------|
|                                    |                                    | TIMELINE SLIDER         |
|                                    |                                    | <--- [ 14:00 ] --->     |
+------------------------------------+------------------------------------+-------------------------+
| BOTTOM STRIP: RESOURCE ALLOCATION OPTIMIZER (PuLP Linear Programming Output)                      |
| [Sector-12 (Score 91) -> Team Alpha (3)] | [Palm Ave (Score 78) -> Team Bravo (2)] | [Unassigned: 2]   |
+---------------------------------------------------------------------------------------------------+
```

---

## Panel Detailed Features

### 1. Subject Profile Panel (Left Sidebar)
* **Demographics**: Photo, Full Name, Age, LKP coordinates, LKP timestamp.
* **Medical Flags**: Prominently highlighted alert badge (e.g., `DIABETIC - REQUIRES INSULIN WITHIN 24h`).
* **Attributes**: Height, clothing items, distinguishing physical features used by the content evaluator.

### 2. Interactive Search Map (Center Canvas)
* **Library**: Leaflet.js + OpenStreetMap tiles.
* **Markers**: Color-coded SVGs matching lead scores:
  * 🔴 **CRITICAL (Score 70–100)**
  * 🟡 **MEDIUM (Score 35–69)**
  * ⚪ **LOW (Score 0–34)**
  * 🟢/🔷 **VOLUNTEER HARDWARE PINGS**
* **Overlays**: Heatmap density layer toggle & convex hull bounding polygon highlighting high-density sighting clusters.
* **Confidence Banner**: Dynamic status string rendered above map:
  > `3 corroborating tips — HIGH CONFIDENCE [71–88]`

### 3. Live Tip Feed (Right Upper Sidebar)
* Real-time list sorted descending by credibility score.
* Clicking any tip card centers and zooms the map onto its exact coordinate pin.
* Manual Coordinator Override Buttons (`[Upgrade to Critical]`, `[Dismiss Lead]`) that trigger active learning retraining.

### 4. Volunteer Tracker (Right Middle Sidebar)
* Displays real-time GPS coordinates, Wi-Fi latency, and battery status for **Unit A (Gateway)** and **Unit B (Field Node)**.

### 5. Timeline Scrubber (Right Lower Sidebar)
* Interactive time slider allowing search coordinators to replay tip arrival density hour-by-hour over the past 24–72 hours, revealing direction of movement vectors.

### 6. Resource Allocation Optimizer (Bottom Strip)
* Displays optimal field team dispatch assignments computed by the PuLP linear programming backend:
  > `Zone Sector-12 [Score 91] → Team Alpha (3 members) · Zone Palm Ave [Score 78] → Team Bravo (2 members) · 2 zones unassigned — awaiting volunteers`
