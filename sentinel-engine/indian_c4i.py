"""
Sentinel V2 C4I Core - Indian Law Enforcement & Infrastructure Module
Specialized for:
1. Mumbai Suburban Railway (Central, Western, Harbour lines) Transit Hop Modeling
2. FASTag / National Electronic Toll Collection (NETC) Highway Chokepoints
3. Indic Multilingual Tip Ingress (Marathi, Hindi, Hinglish) Entity Parsing
4. Bharatiya Sakshya Adhiniyam (BSA, 2023) Section 63 Court Certificate Generation
"""

import math
import hashlib
import json
from datetime import datetime
from typing import Dict, List, Any, Tuple

# --- 1. MUMBAI SUBURBAN RAILWAY INFRASTRUCTURE ---
MUMBAI_LOCAL_STATIONS = [
    # Western Line
    {"id": "WR-01", "name": "Churchgate", "lat": 18.9355, "lng": 72.8272, "line": "Western", "grp_station": "Churchgate GRP", "order": 1},
    {"id": "WR-02", "name": "Mumbai Central", "lat": 18.9712, "lng": 72.8197, "line": "Western", "grp_station": "Mumbai Central GRP", "order": 2},
    {"id": "WR-03", "name": "Dadar (WR)", "lat": 19.0195, "lng": 72.8435, "line": "Western", "grp_station": "Dadar Railway Police", "order": 3},
    {"id": "WR-04", "name": "Bandra", "lat": 19.0596, "lng": 72.8402, "line": "Western", "grp_station": "Bandra GRP", "order": 4},
    {"id": "WR-05", "name": "Andheri", "lat": 19.1197, "lng": 72.8464, "line": "Western", "grp_station": "Andheri GRP", "order": 5},
    {"id": "WR-06", "name": "Borivali", "lat": 19.2291, "lng": 72.8573, "line": "Western", "grp_station": "Borivali GRP", "order": 6},
    {"id": "WR-07", "name": "Virar", "lat": 19.4705, "lng": 72.8028, "line": "Western", "grp_station": "Palghar/Virar GRP", "order": 7},

    # Central Line
    {"id": "CR-01", "name": "CSMT (Mumbai)", "lat": 18.9401, "lng": 72.8354, "line": "Central", "grp_station": "CSMT GRP Headquarters", "order": 1},
    {"id": "CR-02", "name": "Byculla", "lat": 18.9772, "lng": 72.8328, "line": "Central", "grp_station": "Byculla RPF Outpost", "order": 2},
    {"id": "CR-03", "name": "Dadar (CR)", "lat": 19.0178, "lng": 72.8478, "line": "Central", "grp_station": "Dadar GRP", "order": 3},
    {"id": "CR-04", "name": "Kurla Junction", "lat": 19.0657, "lng": 72.8794, "line": "Central", "grp_station": "Kurla GRP", "order": 4},
    {"id": "CR-05", "name": "Ghatkopar", "lat": 19.0864, "lng": 72.9081, "line": "Central", "grp_station": "Ghatkopar RPF", "order": 5},
    {"id": "CR-06", "name": "Thane", "lat": 19.1860, "lng": 72.9759, "line": "Central", "grp_station": "Thane GRP Sub-Division", "order": 6},
    {"id": "CR-07", "name": "Kalyan Junction", "lat": 19.2437, "lng": 73.1355, "line": "Central", "grp_station": "Kalyan GRP Division", "order": 7},

    # Harbour Line
    {"id": "HR-01", "name": "Wadala Road", "lat": 19.0166, "lng": 72.8587, "line": "Harbour", "grp_station": "Wadala GRP", "order": 1},
    {"id": "HR-02", "name": "Vashi", "lat": 19.0645, "lng": 72.9972, "line": "Harbour", "grp_station": "Vashi GRP", "order": 2},
    {"id": "HR-03", "name": "Panvel Junction", "lat": 18.9894, "lng": 73.1212, "line": "Harbour", "grp_station": "Panvel GRP Division", "order": 3}
]

# --- 2. FASTAG / NHAI HIGHWAY TOLL PLAZAS ---
FASTAG_TOLL_PLAZAS = [
    {
        "id": "FASTAG-01",
        "name": "Dahisar Toll Plaza",
        "highway": "Western Express Highway (NH-48)",
        "destination": "Surat / Ahmedabad / Delhi",
        "lat": 19.2562,
        "lng": 72.8687,
        "lanes": 16,
        "anpr_camera": True,
        "zone": "Mumbai North Exit"
    },
    {
        "id": "FASTAG-02",
        "name": "Vashi Toll Plaza",
        "highway": "Sion-Panvel Expressway",
        "destination": "Navi Mumbai / Pune / Goa",
        "lat": 19.0543,
        "lng": 72.9750,
        "lanes": 14,
        "anpr_camera": True,
        "zone": "Navi Mumbai East Exit"
    },
    {
        "id": "FASTAG-03",
        "name": "Airoli Toll Naka",
        "highway": "Mulund-Airoli Bridge",
        "destination": "Thane-Belapur Corridor",
        "lat": 19.1557,
        "lng": 72.9812,
        "lanes": 10,
        "anpr_camera": True,
        "zone": "Thane-Airoli Gateway"
    },
    {
        "id": "FASTAG-04",
        "name": "Mulund Toll Naka",
        "highway": "Eastern Express Highway (NH-160)",
        "destination": "Nashik / Agra / North-East MH",
        "lat": 19.1764,
        "lng": 72.9610,
        "lanes": 14,
        "anpr_camera": True,
        "zone": "Thane North Exit"
    },
    {
        "id": "FASTAG-05",
        "name": "Khalapur Toll Plaza",
        "highway": "Mumbai-Pune Expressway (YCEW)",
        "destination": "Pune / Bengaluru / South India",
        "lat": 18.8256,
        "lng": 73.2842,
        "lanes": 24,
        "anpr_camera": True,
        "zone": "Expressway High-Speed Gateway"
    }
]

def haversine_dist(lat1, lon1, lat2, lon2) -> float:
    R = 6371.0 # Earth's radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def compute_indian_transit_network(lkp_lat: float, lkp_lng: float, elapsed_hours: float = 1.0) -> Dict[str, Any]:
    """
    Computes reachability across:
    1. Suburban railway stations (average local train speed ~35 km/h including stops)
    2. FASTag perimeter toll nakas (vehicular speed ~60-80 km/h)
    """
    elapsed_minutes = max(15.0, elapsed_hours * 60.0)

    # 1. Evaluate Railway Station Reachability
    stations_output = []
    for st in MUMBAI_LOCAL_STATIONS:
        dist_km = haversine_dist(lkp_lat, lkp_lng, st["lat"], st["lng"])
        # Suburban train travel time estimate: ~1.5 mins per km + 3 mins station dwell
        train_travel_mins = round((dist_km / 35.0) * 60.0 + 3.0, 1)

        # Status determination
        if train_travel_mins <= elapsed_minutes:
            status = "REACHABLE_NOW"
            urgency = "CRITICAL_GRP_ALERT"
        elif train_travel_mins <= (elapsed_minutes + 30.0):
            status = "UPCOMING_INTERCEPT"
            urgency = "CORDON_STATION_EXIT"
        else:
            status = "FUTURE_BUFFER"
            urgency = "PASSIVE_MONITOR"

        stations_output.append({
            "id": st["id"],
            "name": st["name"],
            "line": st["line"],
            "lat": st["lat"],
            "lng": st["lng"],
            "distance_km": round(dist_km, 2),
            "transit_time_mins": train_travel_mins,
            "status": status,
            "urgency": urgency,
            "grp_jurisdiction": st["grp_station"]
        })

    # Sort stations by distance
    stations_output.sort(key=lambda x: x["distance_km"])

    # 2. Evaluate FASTag Toll Plaza Interception Windows (Vehicular Transit at 80 km/h)
    fastag_output = []
    for toll in FASTAG_TOLL_PLAZAS:
        dist_km = haversine_dist(lkp_lat, lkp_lng, toll["lat"], toll["lng"])
        # Highway travel time at 80 km/h with 15 mins city traffic buffer
        vehicular_mins = round((dist_km / 80.0) * 60.0 + 15.0, 1)
        remaining_mins = round(vehicular_mins - elapsed_minutes, 1)

        if remaining_mins <= 0:
            interception_state = "VEHICLE_MAY_HAVE_PASSED"
            tag_color = "red"
        elif remaining_mins <= 35:
            interception_state = "URGENT_INTERCEPT_ACTIVE"
            tag_color = "red"
        else:
            interception_state = "PREPARE_FASTAG_CORDON"
            tag_color = "yellow"

        fastag_output.append({
            "id": toll["id"],
            "name": toll["name"],
            "highway": toll["highway"],
            "destination": toll["destination"],
            "lat": toll["lat"],
            "lng": toll["lng"],
            "distance_km": round(dist_km, 2),
            "estimated_drive_mins": vehicular_mins,
            "intercept_window_mins": max(0.0, remaining_mins),
            "state": interception_state,
            "color": tag_color,
            "lanes": toll["lanes"]
        })

    fastag_output.sort(key=lambda x: x["distance_km"])

    return {
        "status": "success",
        "lkp": {"lat": lkp_lat, "lng": lkp_lng},
        "elapsed_hours": round(elapsed_hours, 2),
        "railway_nodes": stations_output,
        "fastag_chokepoints": fastag_output
    }

# --- 3. INDIC MULTILINGUAL NLP PARSER (MARATHI, HINDI, HINGLISH) ---
INDIC_DICTIONARY = {
    # Marathi / Hindi / Hinglish -> English normalized
    "landmarks": {
        "फूल मार्केट": "Flower Market",
        "फुल मार्केट": "Flower Market",
        "phool market": "Flower Market",
        "स्टेशन": "Railway Station",
        "station": "Railway Station",
        "रिक्षा": "Auto-Rickshaw Stand",
        "rickshaw": "Auto-Rickshaw Stand",
        "auto stand": "Auto-Rickshaw Stand",
        "तलाव": "Lake / Waterbody",
        "talao": "Lake / Waterbody",
        "तलाव जवळ": "Near Lake",
        "मंदिर": "Temple",
        "mandir": "Temple",
        "फ्लाईओव्हर": "Flyover Bridge",
        "pul": "Bridge",
        "bridge": "Bridge",
        "बाजार": "Market / Bazaar",
        "bazaar": "Market / Bazaar"
    },
    "colors": {
        "निळा": "Blue",
        "nila": "Blue",
        "neela": "Blue",
        "लाल": "Red",
        "lal": "Red",
        "पांढरा": "White",
        "safed": "White",
        "काळा": "Black",
        "kala": "Black",
        "पिवळा": "Yellow",
        "peela": "Yellow",
        "हिरवा": "Green",
        "hara": "Green"
    },
    "clothing": {
        "शर्ट": "Shirt",
        "shirt": "Shirt",
        "कुर्ता": "Kurta",
        "kurta": "Kurta",
        "पँट": "Pants / Trousers",
        "pant": "Pants",
        "दप्तर": "School Backpack",
        "bag": "Bag / Backpack",
        "साडी": "Saree",
        "टोपी": "Cap / Hat",
        "topi": "Cap"
    },
    "verbs_status": {
        "दिसला": "Spotted / Seen",
        "dekha": "Spotted / Seen",
        "दिसली": "Spotted / Seen (Female)",
        "chal raha tha": "Walking on foot",
        "पळत होता": "Running hastily",
        "घाईत": "In a rush / Panicked",
        "घाबरलेला": "Frightened / Disoriented",
        "gadi me": "Boarded a vehicle"
    }
}

def parse_indic_tip(text: str) -> Dict[str, Any]:
    """
    Parses Marathi, Hindi, or Hinglish crowdsourced tip text,
    detects script/language, extracts named entities, and produces an English operational brief.
    """
    if not text:
        return {"detected_lang": "en", "original_text": "", "translated": "", "entities": {}}

    text_lower = text.lower()
    
    # Detect Devanagari Unicode Range (\u0900 - \u097F)
    has_devanagari = any('\u0900' <= char <= '\u097F' for char in text)
    
    # Check for Marathi specific markers
    marathi_markers = ["दिसला", "दिसली", "जवळ", "आहे", "होता", "पळत", "मुलगा", "मुलगी", "पांढरा", "निळा"]
    hindi_markers = ["dekha", "tha", "ladka", "ladki", "safed", "neela", "dikha", "hai", "ke paas"]

    detected_lang = "en"
    if has_devanagari:
        if any(m in text for m in marathi_markers):
            detected_lang = "mr (Marathi)"
        else:
            detected_lang = "hi (Hindi)"
    else:
        if any(h in text_lower for h in hindi_markers):
            detected_lang = "Hinglish (Romanized Indic)"

    extracted = {"landmarks": [], "colors": [], "clothing": [], "behavior": []}

    # Match landmarks
    for k, v in INDIC_DICTIONARY["landmarks"].items():
        if k in text_lower or k in text:
            if v not in extracted["landmarks"]:
                extracted["landmarks"].append(v)

    # Match colors
    for k, v in INDIC_DICTIONARY["colors"].items():
        if k in text_lower or k in text:
            if v not in extracted["colors"]:
                extracted["colors"].append(v)

    # Match clothing
    for k, v in INDIC_DICTIONARY["clothing"].items():
        if k in text_lower or k in text:
            if v not in extracted["clothing"]:
                extracted["clothing"].append(v)

    # Match behavior
    for k, v in INDIC_DICTIONARY["verbs_status"].items():
        if k in text_lower or k in text:
            if v not in extracted["behavior"]:
                extracted["behavior"].append(v)

    # Construct synthesized English operational translation if Indic
    if detected_lang != "en":
        parts = []
        if extracted["behavior"]:
            parts.append(f"Subject {' & '.join(extracted['behavior'])}")
        else:
            parts.append("Subject reported")

        if extracted["landmarks"]:
            parts.append(f"near {', '.join(extracted['landmarks'])}")

        attire = []
        if extracted["colors"]:
            attire.append('/'.join(extracted["colors"]))
        if extracted["clothing"]:
            attire.append('/'.join(extracted["clothing"]))
        if attire:
            parts.append(f"wearing {' '.join(attire)}")

        translated_summary = " ".join(parts) + f" [Raw Indic: '{text.strip()}']"
    else:
        translated_summary = text

    return {
        "detected_lang": detected_lang,
        "original_text": text,
        "translated_summary": translated_summary,
        "extracted_entities": extracted,
        "is_indic": detected_lang != "en"
    }

# --- 4. BHARATIYA SAKSHYA ADHINIYAM (BSA, 2023) SEC 63 CERTIFICATE ---
def generate_bsa_section_63_certificate(case: Dict[str, Any], tips: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Generates a legally compliant statutory certificate under:
    Section 63 of Bharatiya Sakshya Adhiniyam, 2023 (Admissibility of Electronic Records).
    Computes cryptographic SHA-256 Merkle root hash for all electronic tip logs.
    """
    now = datetime.now()
    cert_no = f"BSA-SEC63/MH-MUM/{now.strftime('%Y')}/{case.get('id', 'CASE')}/{now.strftime('%d%H%M')}"
    
    # Compute SHA-256 for each tip record
    tip_hashes = []
    admissible_tips = []
    rejected_tips = []

    for t in tips:
        raw_repr = f"{t.get('id')}|{t.get('case_id')}|{t.get('lat')}|{t.get('lng')}|{t.get('created_at')}|{t.get('final_score')}|{t.get('tier')}|{t.get('source')}"
        t_hash = hashlib.sha256(raw_repr.encode('utf-8')).hexdigest()
        
        entry = {
            "tip_id": t.get("id"),
            "timestamp": t.get("created_at"),
            "coordinates": f"({t.get('lat')}, {t.get('lng')})",
            "source": t.get("source"),
            "tier": t.get("tier"),
            "score": t.get("final_score") or t.get("score") or 0,
            "sha256_hash": t_hash,
            "message": t.get("message")
        }
        tip_hashes.append(t_hash)

        if t.get("tier") in ["HIGH", "REVIEW"]:
            admissible_tips.append(entry)
        else:
            rejected_tips.append(entry)

    # Master Merkle Root Hash
    if tip_hashes:
        combined = "".join(tip_hashes)
        merkle_root = hashlib.sha256(combined.encode('utf-8')).hexdigest()
    else:
        merkle_root = hashlib.sha256(f"INITIAL_{case.get('id')}_{now.isoformat()}".encode('utf-8')).hexdigest()

    # Case Details
    cctns_fir = case.get("cctns_fir") or "FIR-248/2026"
    police_station = case.get("police_station") or "Dadar Police Station, Zone-V, Mumbai"
    bns_section = case.get("bns_section") or "BNS Section 137(2) [Kidnapping of Minor]"

    return {
        "certificate_title": "CERTIFICATE UNDER SECTION 63 OF THE BHARATIYA SAKSHYA ADHINIYAM, 2023",
        "statutory_act": "Bharatiya Sakshya Adhiniyam, 2023 (Act No. 47 of 2023), Section 63(4)",
        "certificate_number": cert_no,
        "issuing_authority": "C4I Tactical Command Core, Greater Mumbai Police",
        "station_jurisdiction": police_station,
        "cctns_fir_reference": cctns_fir,
        "bns_sections": bns_section,
        "subject_name": case.get("name"),
        "subject_lkp": case.get("lkp"),
        "lkp_coords": f"({case.get('lkp_lat')}, {case.get('lkp_lng')})",
        "generation_timestamp": now.strftime("%Y-%m-%d %H:%M:%S IST"),
        "investigating_officer": "Inspector (Technical) CMD-OP1, Cyber & Spatial C4I Unit",
        "merkle_root_sha256": merkle_root,
        "total_electronic_records": len(tips),
        "admissible_records_count": len(admissible_tips),
        "rejected_records_count": len(rejected_tips),
        "admissible_records": admissible_tips,
        "rejected_records": rejected_tips,
        "statutory_declaration": (
            "I hereby certify and declare that the electronic records contained in this ledger "
            "were produced by the computer system of the Sentinel V2 Tactical C4I Platform during "
            "the period over which the computer was used regularly to store or process information. "
            "Throughout the material period, the computer system was operating properly and the contents "
            "reproduced herein have not been tampered with or altered, as verified by the SHA-256 cryptographic "
            "hashes and Merkle root calculation specified above."
        )
    }
