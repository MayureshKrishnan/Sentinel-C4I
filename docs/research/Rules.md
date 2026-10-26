# SENTINEL - AI Coding & Architectural Rules (Rules.md)

## 1. Technological & Library Guardrails

### Approved Tech Stack & Libraries
* **Frontend**: React, Vite, Vanilla CSS + Tailwind CSS, Leaflet.js (`react-leaflet`), Lucide Icons (`lucide-react`).
* **Backend**: Python 3.11+, FastAPI, Pydantic v2, `scikit-learn` (Naive Bayes), `PuLP` (Linear Programming solver), `numpy`, `rasterio` (offline GIS scripts).
* **Database & WebSockets**: `@supabase/supabase-js`, `psycopg2-binary` / `asyncpg` with PostGIS extension.

### Explicitly Forbidden Technologies & Practices
* ❌ **DO NOT** use paid third-party APIs (Mapbox paid tiers, Google Maps API, OpenAI API). Everything must run on free tiers and open-source models.
* ❌ **DO NOT** implement facial recognition, biometric models, or face vector embeddings. Image attachments must remain raw files.
* ❌ **DO NOT** add live video/CCTV streaming ingestion pipelines. Accepts text and GPS coordinates only.
* ❌ **DO NOT** build automated police or law enforcement dispatch triggers. System must remain **advisory-only** with human coordinator authorization required.
* ❌ **DO NOT** use dummy fallback values or swallow exceptions silently when API calls or scoring calculations fail.

---

## 2. Code Quality & Implementation Guidelines

### Mathematical & Algorithmic Rigor
1. **Scoring Formula Parameters**:
   - $w_1 = 40$ (Source Reliability), $w_2 = 35$ (Spatial Proximity), $w_3 = 25$ (Content Richness).
   - $\lambda = 0.1155$ ($T_{1/2} = 6 \text{ hours}$).
   - Formulas must be transparent, modular, and fully covered by unit tests.
2. **Deterministic Outputs**:
   - Scores must be rounded to integers $0-100$ for primary categorization, while displaying confidence interval ranges (`68–79 HIGH CONFIDENCE`) to prevent false point-precision assumptions.

### Error Handling & Reliability
1. All API endpoints must use **Pydantic schemas** to validate incoming JSON structure.
2. If coordinates are missing or invalid, return explicit `422 Unprocessable Entity` with details rather than guessing `(0, 0)`.
3. Database transactions must use async connections where possible to ensure high concurrency under burst tip loads.

---

## 3. UI & Design System Rules

1. **Aesthetics**: Follow a sleek **Dark Navy / Tactical Operations** design theme (`#0B132B`, `#1C2541`, `#3A506B`, `#48CAE4`).
2. **No Placeholders**: Render working interactive map components, live mock data generators, or generated visual assets.
3. **Color Priority Coding**:
   - 🔴 **CRITICAL (70-100)**: `#FF3B30` / `#E63946`
   - 🟡 **MEDIUM (35-69)**: `#FF9500` / `#F4A261`
   - ⚪ **LOW (0-34)**: `#8E8E93` / `#6C757D`
   - 🟢 **VOLUNTEER TRACKER**: `#2EC4B6` / `#00F5D4`
