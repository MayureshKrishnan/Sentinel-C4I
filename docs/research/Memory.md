# SENTINEL - Project Execution Memory (Memory.md)

> **Purpose**: This living memory log tracks implementation progress, current codebase status, architectural decisions, and key context to maintain seamless continuity across development turns and sessions.

---

## 1. Project Identity & Key Metrics
* **Project Name**: SENTINEL (Search Intelligence & Tip Evaluation Network for Incident Leads)
* **Target Domain**: Time-Critical Missing Person Search & Rescue (Golden Window 24–72 hours)
* **Primary Thrust Area**: IEEE GRSS (Geoscience and Remote Sensing Applications)
* **Software Licensing Cost**: ₹0
* **Hardware BOM**: ₹1,120 (NodeMCU ESP8266 + NEO-6M GPS)

---

## 2. Core Specification Documents Status

| Document File | Purpose / Coverage | Status |
| :--- | :--- | :--- |
| [PRD.md](file:///C:/Users/Mayuresh%20Krishnan/.gemini/antigravity/brain/d0c6925d-c5ef-4717-b37f-829f021b8c46/PRD.md) | Requirements, user personas, functional & non-functional requirements. | ✅ Completed |
| [Architecture.md](file:///C:/Users/Mayuresh%20Krishnan/.gemini/antigravity/brain/d0c6925d-c5ef-4717-b37f-829f021b8c46/Architecture.md) | Technical stack, data flow, directory layout, database schema. | ✅ Completed |
| [Rules.md](file:///C:/Users/Mayuresh%20Krishnan/.gemini/antigravity/brain/d0c6925d-c5ef-4717-b37f-829f021b8c46/Rules.md) | Coding standards, allowed/forbidden libraries, ethical guardrails. | ✅ Completed |
| [Phases.md](file:///C:/Users/Mayuresh%20Krishnan/.gemini/antigravity/brain/d0c6925d-c5ef-4717-b37f-829f021b8c46/Phases.md) | 5-phase 3-member structured development roadmap. | ✅ Completed |
| [Design.md](file:///C:/Users/Mayuresh%20Krishnan/.gemini/antigravity/brain/d0c6925d-c5ef-4717-b37f-829f021b8c46/Design.md) | Design system, dark glassmorphism theme, typography, priority colors. | ✅ Completed |
| [Memory.md](file:///C:/Users/Mayuresh%20Krishnan/.gemini/antigravity/brain/d0c6925d-c5ef-4717-b37f-829f021b8c46/Memory.md) | Active state tracker & memory log. | 🔄 Active |
| [team_implementation_plan.md](file:///C:/Users/Mayuresh%20Krishnan/.gemini/antigravity/brain/d0c6925d-c5ef-4717-b37f-829f021b8c46/team_implementation_plan.md) | 3-member task allocation & integration pipeline. | ✅ Completed |

---

## 3. Implementation Progress Tracker

### Current Phase: **Phase 1 Preparation**
- [x] Create foundational specification documents (PRD, Architecture, Rules, Phases, Design, Memory).
- [ ] Initialize codebase directory structure (`frontend/`, `backend/`, `hardware/`, `n8n/`, `gis/`).
- [ ] Implement FastAPI scoring engine backend (`backend/app/services/scoring.py`).
- [ ] Write `pytest` mathematical verification unit tests.
- [ ] Build React + Vite Command Dashboard frontend (`frontend/src/App.jsx`).

---

## 4. Key Formulas & Parameters Reference
$$S = (w_1 \cdot C_{\text{source}} + w_2 \cdot V_{\text{spatial}} + w_3 \cdot I_{\text{content}}) \times e^{-\lambda \cdot \Delta t}$$
* **Weights**: $w_1 = 40$, $w_2 = 35$, $w_3 = 25$.
* **Half-life**: $T_{1/2} = 6 \text{ hours} \implies \lambda = 0.1155 \text{ hr}^{-1}$.
* **Source Scores ($C_{\text{source}}$)**: Responder = 1.0, Volunteer = 0.8, Public Verified = 0.5, Anonymous = 0.2.
