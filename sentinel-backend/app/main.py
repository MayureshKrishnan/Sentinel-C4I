import os
import sys
import math
import hashlib
from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# Support modular 3-folder team architecture: sentinel-engine & sentinel-backend
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
engine_path = os.path.join(root_dir, "sentinel-engine")
if os.path.exists(engine_path) and engine_path not in sys.path:
    sys.path.insert(0, engine_path)

try:
    from spatial_math import SpatialMathEngine
    from ml_clustering import MLClusteringEngine
    from indian_c4i import (
        compute_indian_transit_network,
        parse_indic_tip,
        generate_bsa_section_63_certificate
    )
except ImportError:
    from app.engine.spatial_math import SpatialMathEngine
    from app.engine.ml_clustering import MLClusteringEngine
    from app.engine.indian_c4i import (
        compute_indian_transit_network,
        parse_indic_tip,
        generate_bsa_section_63_certificate
    )
from app.db_sqlite import (
    init_db,
    get_all_cases,
    get_case_by_id,
    create_case,
    get_tips_by_case,
    insert_tip,
    update_tip_clustering
)

# Initialize database on module load
init_db()

app = FastAPI(
    title="Sentinel V2 Production API",
    description="Real-world C4I Multi-factor AI Credibility & Search Operation Backend with Indian Law Enforcement Integration",
    version="2.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_no_cache_header(request: Request, call_next):
    response = await call_next(request)
    path = request.url.path.lower()
    if path.endswith(".html") or path == "/" or path.endswith(".js") or path.endswith(".css"):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
    
    # Production Security Headers (Harden against clickjacking, MIME-sniffing, XSS)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response

# WebSocket Connection Manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in list(self.active_connections):
            try:
                await connection.send_json(message)
            except Exception:
                self.disconnect(connection)

manager = ConnectionManager()
spatial_engine = SpatialMathEngine()
ml_engine = MLClusteringEngine()

# Pydantic Schemas
class CaseCreateModel(BaseModel):
    name: str
    age: Optional[str] = "Unknown"
    lkp: str
    lkp_lat: float
    lkp_lng: float
    last_seen_time: Optional[str] = None
    med: Optional[str] = "None"
    cloth: Optional[str] = "Unknown"
    v_max_kmh: Optional[float] = 5.0
    cctns_fir: Optional[str] = None
    police_station: Optional[str] = None
    bns_section: Optional[str] = None

class TipInjectModel(BaseModel):
    case_id: str
    lat: float
    lng: float
    source: Optional[str] = "Anonymous Citizen"
    signal_type: Optional[str] = "Visual Sighting"
    message: Optional[str] = ""
    score: Optional[int] = 50
    confidence: Optional[float] = 0.8
    sighting_time: Optional[str] = None

# --- Cases Endpoints ---
@app.get("/api/v1/cases")
def list_cases():
    cases = get_all_cases()
    return {"status": "success", "count": len(cases), "cases": cases}

@app.get("/api/v1/cases/{case_id}")
def read_case(case_id: str):
    case = get_case_by_id(case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case folder not found.")
    return {"status": "success", "case": case}

@app.get("/api/v1/cases/{case_id}/isochrone")
def get_case_isochrone(case_id: str):
    case = get_case_by_id(case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case folder not found.")
    
    elapsed = 1.0
    if case.get("last_seen_time"):
        try:
            t_lkp = datetime.strptime(case["last_seen_time"], "%Y-%m-%d %H:%M:%S")
            diff = (datetime.now() - t_lkp).total_seconds() / 3600.0
            elapsed = max(0.8, min(4.0, diff))
        except Exception:
            elapsed = 1.0

    isochrone_data = spatial_engine.generate_anisotropic_isochrone(
        lkp_lat=float(case["lkp_lat"]),
        lkp_lng=float(case["lkp_lng"]),
        hours_elapsed=elapsed,
        base_slope_deg=3.4,
        num_vertices=24
    )
    return {"status": "success", "case_id": case_id, "isochrone": isochrone_data}

@app.get("/api/v1/cases/{case_id}/transit-chokepoints")
def get_transit_chokepoints(case_id: str):
    """
    Computes reachability across:
    1. Mumbai Suburban Railway Network (Local Trains)
    2. FASTag National Highway Perimeter Toll Nakas (80 km/h vehicular transit)
    """
    case = get_case_by_id(case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case folder not found.")

    elapsed = 1.0
    if case.get("last_seen_time"):
        try:
            t_lkp = datetime.strptime(case["last_seen_time"], "%Y-%m-%d %H:%M:%S")
            diff = (datetime.now() - t_lkp).total_seconds() / 3600.0
            elapsed = max(0.5, diff)
        except Exception:
            elapsed = 1.0

    network_data = compute_indian_transit_network(
        lkp_lat=float(case["lkp_lat"]),
        lkp_lng=float(case["lkp_lng"]),
        elapsed_hours=elapsed
    )
    return network_data

@app.get("/api/v1/cases/{case_id}/bsa-certificate")
def get_bsa_certificate(case_id: str):
    """
    Generates statutory Electronic Evidence Certificate under
    Section 63 of Bharatiya Sakshya Adhiniyam, 2023 with SHA-256 Merkle root.
    """
    case = get_case_by_id(case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case folder not found.")
    
    tips = get_tips_by_case(case_id)
    cert = generate_bsa_section_63_certificate(case, tips)
    return {"status": "success", "certificate": cert}

@app.post("/api/v1/cases")
async def add_case(payload: CaseCreateModel):
    cases = get_all_cases()
    new_id = f"CASE-{len(cases) + 1:02d}"
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    case_dict = {
        "id": new_id,
        "name": payload.name,
        "age": payload.age or "Unknown",
        "lkp": payload.lkp,
        "lkp_lat": payload.lkp_lat,
        "lkp_lng": payload.lkp_lng,
        "last_seen_time": payload.last_seen_time or now_str,
        "med": payload.med or "None",
        "cloth": payload.cloth or "Unknown",
        "v_max_kmh": payload.v_max_kmh or 5.0,
        "status": "ACTIVE",
        "img": f"https://ui-avatars.com/api/?name={payload.name.replace(' ', '+')}&background=1e3a8a&color=fff&size=256",
        "cctns_fir": payload.cctns_fir or f"CCTNS FIR-{len(cases)+240:03d}/2026",
        "police_station": payload.police_station or "Dadar Police Station, Zone-V, Mumbai",
        "bns_section": payload.bns_section or "BNS Section 137(2) [Kidnapping of Minor]",
        "created_at": now_str
    }
    create_case(case_dict)
    
    # Broadcast case creation event to connected dashboards
    await manager.broadcast({
        "type": "NEW_CASE",
        "case": case_dict
    })

    return {"status": "success", "case": case_dict}

# --- Tips Endpoints ---
@app.get("/api/v1/cases/{case_id}/tips")
def list_tips_for_case(case_id: str):
    tips = get_tips_by_case(case_id)
    return {"status": "success", "case_id": case_id, "tips": tips}

@app.post("/api/v1/tips/inject")
async def inject_tip(tip_input: TipInjectModel):
    # 1. Resolve Case Context
    case = get_case_by_id(tip_input.case_id)
    if not case:
        all_cases = get_all_cases()
        if not all_cases:
            raise HTTPException(status_code=400, detail="No active case folders exist.")
        case = all_cases[0]
        tip_input.case_id = case["id"]

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sighting_time_str = tip_input.sighting_time or now_str

    # Parse Indic Text (Marathi, Hindi, Hinglish)
    raw_message = tip_input.message or ""
    indic_parsed = parse_indic_tip(raw_message)
    processed_message = indic_parsed["translated_summary"] if indic_parsed["is_indic"] else raw_message
    lang_detected = indic_parsed["detected_lang"]

    # Calculate actual elapsed hours from LKP
    elapsed_hours = 2.0
    if case.get("last_seen_time"):
        try:
            t_lkp = datetime.strptime(case["last_seen_time"], "%Y-%m-%d %H:%M:%S")
            diff_hours = (datetime.now() - t_lkp).total_seconds() / 3600.0
            elapsed_hours = max(0.5, diff_hours)
        except Exception:
            elapsed_hours = 2.0

    lkp_coords = (float(case["lkp_lat"]), float(case["lkp_lng"]))
    tip_coords = (float(tip_input.lat), float(tip_input.lng))
    v_max = float(case.get("v_max_kmh") or 5.0)

    # Calculate Haversine Distance
    dist_km = spatial_engine.haversine_distance(lkp_coords[0], lkp_coords[1], tip_coords[0], tip_coords[1])
    req_speed = round(dist_km / max(0.1, elapsed_hours), 1)

    # Multi-Modal Velocity Hypothesis (Pedestrian vs Vehicular Corridor vs Impossible)
    is_pedestrian = (req_speed <= (v_max * 1.35))
    is_vehicular = (req_speed > (v_max * 1.35) and req_speed <= 110.0)
    is_physically_impossible = (req_speed > 110.0)

    # 3. Layer 2: Scikit-Learn DBSCAN Clustering
    existing_tips = get_tips_by_case(tip_input.case_id)
    tip_id = f"TIP-{len(existing_tips) + 1:03d}"

    # Run clustering over all tips for this case
    all_tips_for_clustering = [
        {"id": t["id"], "lat": t["lat"], "lng": t["lng"]} 
        for t in existing_tips
    ]
    all_tips_for_clustering.append({"id": tip_id, "lat": tip_input.lat, "lng": tip_input.lng})

    # Cluster radius 0.6 km
    clusters = ml_engine.find_clusters(all_tips_for_clustering, eps_km=0.6, min_samples=2)
    assigned_cluster = clusters.get(tip_id, -1)

    # 4. Layer 3: Final Credibility Scoring
    if is_pedestrian:
        is_feasible = True
        final_score = ml_engine.calculate_final_score(
            is_feasible=True,
            cluster_id=assigned_cluster,
            base_trust=tip_input.score or 50
        )
        if final_score >= 75:
            tier = "HIGH"
            reason = "Corroborated by DBSCAN Cluster & Physically Feasible"
        else:
            tier = "REVIEW"
            reason = "Pedestrian Feasible (Awaiting Corroboration)"
    elif is_vehicular:
        # Vehicular transit sighting: keep in REVIEW tier with highway flag
        is_feasible = True
        base_s = 45 if assigned_cluster == -1 else 82
        final_score = base_s
        if assigned_cluster != -1:
            tier = "HIGH"
            reason = f"Corroborated Highway Transit Cluster #{assigned_cluster} ({req_speed} km/h)"
        else:
            tier = "REVIEW"
            reason = f"Vehicular Transit Sighting ({req_speed} km/h Highway Corridor Anomaly)"
    else:
        is_feasible = False
        final_score = 0
        tier = "REJECTED"
        reason = f"EXCEEDS PHYSICAL LIMITS (Requires {req_speed} km/h)"

    # Compute SHA-256 for BSA Sec 63 digital chain-of-custody
    raw_hash_seed = f"{tip_id}|{tip_input.case_id}|{tip_input.lat}|{tip_input.lng}|{now_str}|{final_score}|{tier}|{tip_input.source}"
    sha256_hash = hashlib.sha256(raw_hash_seed.encode('utf-8')).hexdigest()

    # Prepare tip record
    current_tip_dict = {
        "id": tip_id,
        "case_id": tip_input.case_id,
        "source": tip_input.source or "Anonymous Citizen",
        "signal_type": tip_input.signal_type or "Visual Sighting",
        "sighting_time": sighting_time_str,
        "lat": tip_input.lat,
        "lng": tip_input.lng,
        "message": processed_message,
        "base_score": tip_input.score or 50,
        "final_score": final_score,
        "tier": tier,
        "reason": reason,
        "cluster_id": assigned_cluster,
        "distance_km": round(dist_km, 2),
        "original_text": raw_message if indic_parsed["is_indic"] else None,
        "lang_detected": lang_detected,
        "sha256_hash": sha256_hash,
        "created_at": now_str
    }

    # 5. Persistent DB Write
    insert_tip(current_tip_dict)

    # Re-evaluate previous tips if newly formed cluster changed their scores
    for t in existing_tips:
        new_c = clusters.get(t["id"], -1)
        if new_c != t.get("cluster_id"):
            re_score = ml_engine.calculate_final_score(
                is_feasible=(t.get("tier") != "REJECTED"),
                cluster_id=new_c,
                base_trust=t.get("base_score", 50)
            )
            re_tier = "HIGH" if re_score >= 75 else ("REVIEW" if re_score > 0 else "REJECTED")
            update_tip_clustering(t["id"], new_c, re_score, re_tier)

    # 6. Real-time WebSocket Broadcast
    broadcast_data = {
        "type": "NEW_TIP",
        "id": tip_id,
        "case_id": tip_input.case_id,
        "lat": tip_input.lat,
        "lng": tip_input.lng,
        "source": current_tip_dict["source"],
        "signal_type": current_tip_dict["signal_type"],
        "message": current_tip_dict["message"],
        "score": final_score,
        "tier": tier,
        "reason": reason,
        "distance_km": round(dist_km, 2),
        "cluster_id": assigned_cluster,
        "lang_detected": lang_detected,
        "sha256_hash": sha256_hash,
        "created_at": now_str
    }
    await manager.broadcast(broadcast_data)

    return {
        "status": "success",
        "message": "Tip processed through 3-Layer Credibility Engine with Indic NLP & Multi-modal Velocity",
        "tip": broadcast_data,
        "indic_analysis": indic_parsed
    }

# --- WebSocket Endpoint ---
@app.websocket("/ws/dashboard")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception:
        manager.disconnect(websocket)

# --- Mount Static Frontend Files (Searches sentinel-frontend, Sentinel-Frontend, etc.) ---
frontend_dir = os.path.abspath(os.path.join(root_dir, "sentinel-frontend"))
if not os.path.exists(frontend_dir):
    frontend_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "sentinel-frontend"))
if not os.path.exists(frontend_dir):
    frontend_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "Sentinel-Frontend"))
if not os.path.exists(frontend_dir):
    frontend_dir = os.path.abspath(os.path.join(os.getcwd(), "sentinel-frontend"))
if not os.path.exists(frontend_dir):
    frontend_dir = os.path.abspath(os.path.join(os.getcwd(), "Sentinel-Frontend"))
if not os.path.exists(frontend_dir):
    frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "static"))

def serve_html_file(filename: str):
    path = os.path.join(frontend_dir, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return HTMLResponse(
            content=content,
            status_code=200,
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate, max-age=0",
                "Pragma": "no-cache",
                "Expires": "0"
            }
        )
    raise HTTPException(status_code=404, detail="File not found")

@app.get("/pipeline.html")
@app.get("/pipeline")
async def serve_pipeline():
    return serve_html_file("pipeline.html")

@app.get("/architecture.html")
@app.get("/architecture")
async def serve_architecture():
    return serve_html_file("architecture.html")

@app.get("/dashboard.html")
@app.get("/dashboard")
async def serve_dashboard():
    return serve_html_file("dashboard.html")

@app.get("/submit_tip.html")
@app.get("/submit_tip")
async def serve_submit_tip():
    return serve_html_file("submit_tip.html")

@app.get("/index.html")
@app.get("/")
async def serve_index():
    return serve_html_file("index.html")

if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=False)
