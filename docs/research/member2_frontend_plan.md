# SENTINEL - Member 2 (Frontend UI Lead) Phase 1 Execution Plan

Welcome **Member 2**! As the **Frontend Architect & UI Engineering Lead**, your responsibility is to build the **Tactical Command Center Dashboard** using **React.js**, **Vite**, **Leaflet.js**, and **Tailwind CSS**.

In **Phase 1**, you will build the complete interactive dashboard layout using a local `mock_tips.json` file. This means your UI development is **100% independent**—you do NOT have to wait for Member 1's backend or Member 3's hardware!

---

## 🎨 Design Theme & Aesthetic Specs (`Design.md`)
- **Theme**: Dark Navy / Tactical Operations Glassmorphism.
- **Background**: `#060B19` (Deep Space Dark)
- **Panel Surface**: `#0F172A` with subtle backdrop blur `backdrop-filter: blur(12px)`
- **Priority Colors**:
  - 🔴 **CRITICAL (Score 70+)**: `#EF4444` (Pulsing Red Marker)
  - 🟡 **MEDIUM (Score 35–69)**: `#F59E0B` (Amber Gold Marker)
  - ⚪ **LOW (Score <35)**: `#64748B` (Muted Slate Marker)
  - 🟢 **VOLUNTEER PINGS**: `#10B981` (Cyan Neon Marker)

---

## 📐 Dashboard Layout Grid Structure

```
+---------------------------------------------------------------------------------------------------+
|  SENTINEL EMERGENCY COMMAND CENTER | INCIDENT #INC-2026-NM01 | GOLDEN WINDOW: 14h 22m RECOVERING |
+------------------------------------+------------------------------------+-------------------------+
|                                    |                                    |                         |
|  LEFT PANEL: SUBJECT PROFILE       | CENTER CANVAS: INTERACTIVE MAP     | RIGHT PANEL: LIVE FEED  |
|                                    | (Leaflet.js + OpenStreetMap)       |                         |
|  [ Photo Placeholder ]             |                                    | [91] Responder (Palm)   |
|  Name: Arjun Mehta                 |  - Color-coded Markers:            | [78] Volunteer (Sec 12) |
|  Age: 34                           |    * RED: Critical (70+)         | [55] Public (Park Gate) |
|  LKP: Sector 12, Navi Mumbai       |    * AMBER: Medium (35-69)       |                         |
|  LKP Time: 14:32 IST               |    * GREY: Low (<35)            |-------------------------|
|  Medical: Diabetic (Urgent ⚠)      |    * CYAN: Volunteer Node       | VOLUNTEER TRACKER       |
|  Clothing: Blue jacket, dark jeans |  - Heatmap Density Layer Toggle    | Unit A: 18.9876, 73.0021|
|  Physical: 5'10", black backpack   |  - Convex Hull Zone Polygon        | Unit B: 18.9912, 73.0045|
|                                    |  - Confidence Zone Banner:         | Last ping: 14s ago      |
|                                    |    "3 corroborating tips -         |                         |
|                                    |     HIGH CONFIDENCE [71-88]"       |-------------------------|
|                                    |                                    | TIMELINE SLIDER         |
|                                    |                                    | <--- [ 14:00 ] --->     |
+------------------------------------+------------------------------------+-------------------------+
| BOTTOM STRIP: RESOURCE ALLOCATION OPTIMIZER (PuLP Linear Programming Assignment Output)           |
| [Sector-12 (Score 91) -> Team Alpha (3)] | [Palm Ave (Score 78) -> Team Bravo (2)] | [Unassigned: 2]   |
+---------------------------------------------------------------------------------------------------+
```

---

## 🛠️ Step-by-Step Instructions to Setup & Run Your UI

### 1. Open Terminal & Navigate to `frontend/`:
```bash
cd "C:\Users\Mayuresh Krishnan\.gemini\antigravity\scratch\sentinel\frontend"
```

### 2. Install Node Dependencies:
```bash
npm install leaflet react-leaflet lucide-react @supabase/supabase-js
```

### 3. Run Dev Server:
```bash
npm run dev
```
Open `http://localhost:5173` in your browser to view your live UI!

---

## 📁 Key React Components You Will Own

1. `src/components/Map/InteractiveMap.jsx`: The Leaflet map component with Leaflet custom marker pins. Clicking any pin zooms in and highlights the lead.
2. `src/components/Profile/SubjectProfile.jsx`: Renders missing subject details (Arjun Mehta, 34, Diabetic alert badge).
3. `src/components/TipFeed/LiveTipFeed.jsx`: Real-time tip feed stream sorted by credibility score.
4. `src/components/Volunteer/VolunteerTracker.jsx`: Tracks hardware GPS node coordinates for Unit A (Gateway) and Unit B (Field Node).
5. `src/components/Optimizer/ResourceOptimizer.jsx`: Bottom strip displaying team-to-zone dispatch recommendations.
6. `src/components/Timeline/TimelineScrubber.jsx`: Hour-by-hour tip density scrubber slider.
