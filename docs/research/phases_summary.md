# SENTINEL - Project Implementation Phases Summary

We have divided the **SENTINEL** project into **5 Structured Implementation Phases**, designed for **3 team members** to work simultaneously with zero blocking dependencies.

---

## 📌 The 5 Project Phases At a Glance

| Phase # | Phase Name | Primary Goal | Team Member Tasks |
| :--- | :--- | :--- | :--- |
| **Phase 1** | **Isolated Zero-Dependency Development** | Build standalone core engine, frontend UI shell, and hardware sketch without relying on other team members. | **M1**: FastAPI scoring formula + Naive Bayes<br>**M2**: React + Leaflet UI map + Mock tips JSON<br>**M3**: QGIS Satellite rasters + ESP8266 Firmware sketch |
| **Phase 2** | **Supabase DB & Real-Time Sync** | Enable spatial database storage and `< 1s` WebSocket live map updates. | **M1**: FastAPI to Supabase DB integration<br>**M2**: Connect React UI to Supabase WebSockets<br>**M3**: n8n deduplication workflow (200m / 30min) |
| **Phase 3** | **Resource Allocation & Hardware Connection** | Add PuLP linear program optimizer and connect live hardware nodes. | **M1**: PuLP team-to-zone dispatch solver<br>**M2**: Build PuLP bottom strip & Timeline scrubber<br>**M3**: Power on NodeMCU GPS node & verify live pings |
| **Phase 4** | **Active Learning & Ethical Guardrails** | Implement human-in-the-loop score overrides & UI design polish. | **M1**: Coordinator override weight retraining logic<br>**M2**: Dark Glassmorphism aesthetic polish (`Design.md`)<br>**M3**: Generate 250 synthetic tip benchmark dataset |
| **Phase 5** | **Validation, PyTest & Panel Demo** | System verification, automated tests, and live outdoor demonstration. | **M1**: PyTest backend unit testing suite<br>**M2**: Mobile responsiveness & performance optimization<br>**M3**: Evaluate Precision@K metrics & slide deck prep |

---

## 👥 Member Division Summary

* 👤 **Member 1 (Backend Lead)**: Focuses on Python, FastAPI, Credibility Scoring Matrix, Naive Bayes classifier, PuLP linear programming, and PyTest.
* 👤 **Member 2 (Frontend Lead)**: Focuses on React.js, Leaflet interactive maps, priority color markers (Red/Amber/Grey/Cyan), dark glassmorphic styling, and WebSockets.
* 👤 **Member 3 (GIS/Hardware/Workflow Coordinator - Accessible Tech)**: Focuses on QGIS GUI satellite setup, NodeMCU ESP8266 Arduino flashing, n8n visual automation, synthetic dataset generation, and presentation slides.

---

## 📑 Document References
* Full 5-phase breakdown: [Phases.md](file:///C:/Users/Mayuresh%20Krishnan/.gemini/antigravity/brain/d0c6925d-c5ef-4717-b37f-829f021b8c46/Phases.md)
* 3-Member task allocation: [team_implementation_plan.md](file:///C:/Users/Mayuresh%20Krishnan/.gemini/antigravity/brain/d0c6925d-c5ef-4717-b37f-829f021b8c46/team_implementation_plan.md)
* Live memory log: [Memory.md](file:///C:/Users/Mayuresh%20Krishnan/.gemini/antigravity/brain/d0c6925d-c5ef-4717-b37f-829f021b8c46/Memory.md)
