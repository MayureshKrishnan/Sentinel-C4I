import sqlite3
import os
import json
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sentinel.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Cases Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cases (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        age TEXT,
        lkp TEXT,
        lkp_lat REAL NOT NULL,
        lkp_lng REAL NOT NULL,
        last_seen_time TEXT,
        med TEXT,
        cloth TEXT,
        v_max_kmh REAL DEFAULT 5.0,
        status TEXT DEFAULT 'ACTIVE',
        img TEXT,
        cctns_fir TEXT DEFAULT 'PENDING_REGISTRATION',
        police_station TEXT DEFAULT 'Dadar Police Station, Zone-V, Mumbai',
        bns_section TEXT DEFAULT 'BNS Section 137(2) [Kidnapping of Minor]',
        created_at TEXT
    )
    """)

    # Tips Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tips (
        id TEXT PRIMARY KEY,
        case_id TEXT NOT NULL,
        source TEXT,
        signal_type TEXT,
        sighting_time TEXT,
        lat REAL NOT NULL,
        lng REAL NOT NULL,
        message TEXT,
        base_score INTEGER DEFAULT 50,
        final_score INTEGER DEFAULT 0,
        tier TEXT DEFAULT 'REVIEW',
        reason TEXT,
        cluster_id INTEGER DEFAULT -1,
        distance_km REAL DEFAULT 0.0,
        original_text TEXT,
        lang_detected TEXT DEFAULT 'en',
        sha256_hash TEXT,
        created_at TEXT,
        FOREIGN KEY (case_id) REFERENCES cases(id)
    )
    """)

    conn.commit()

    # Dynamic Column Migration for existing databases
    cursor.execute("PRAGMA table_info(cases)")
    case_cols = [row["name"] for row in cursor.fetchall()]
    if "cctns_fir" not in case_cols:
        cursor.execute("ALTER TABLE cases ADD COLUMN cctns_fir TEXT DEFAULT 'PENDING_REGISTRATION'")
    if "police_station" not in case_cols:
        cursor.execute("ALTER TABLE cases ADD COLUMN police_station TEXT DEFAULT 'Dadar Police Station, Zone-V, Mumbai'")
    if "bns_section" not in case_cols:
        cursor.execute("ALTER TABLE cases ADD COLUMN bns_section TEXT DEFAULT 'BNS Section 137(2) [Kidnapping of Minor]'")

    cursor.execute("PRAGMA table_info(tips)")
    tip_cols = [row["name"] for row in cursor.fetchall()]
    if "original_text" not in tip_cols:
        cursor.execute("ALTER TABLE tips ADD COLUMN original_text TEXT")
    if "lang_detected" not in tip_cols:
        cursor.execute("ALTER TABLE tips ADD COLUMN lang_detected TEXT DEFAULT 'en'")
    if "sha256_hash" not in tip_cols:
        cursor.execute("ALTER TABLE tips ADD COLUMN sha256_hash TEXT")

    conn.commit()

    # Pre-seed default operational cases if table is empty
    cursor.execute("SELECT COUNT(*) as cnt FROM cases")
    count = cursor.fetchone()["cnt"]
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if count == 0:
        cursor.execute("""
        INSERT INTO cases (id, name, age, lkp, lkp_lat, lkp_lng, last_seen_time, med, cloth, v_max_kmh, status, img, cctns_fir, police_station, bns_section, created_at)
        VALUES 
        ('CASE-01', 'Arjun Mehta', '14', 'Dadar Railway Station, Mumbai', 19.0178, 72.8478, ?, 'Diabetic - Requires Insulin', 'Blue school uniform, navy backpack', 5.0, 'ACTIVE', 'https://ui-avatars.com/api/?name=Arjun+Mehta&background=1e3a8a&color=fff&size=256', 'CCTNS FIR-248/2026', 'Dadar Police Station, Zone-V, Mumbai', 'BNS Section 137(2) [Kidnapping of Minor]', ?),
        ('CASE-02', 'Raj Kondvilkar', '72', 'Bandra Terminus, Mumbai', 19.0596, 72.8295, ?, 'Dementia - Disoriented', 'White kurta, brown spectacles', 3.5, 'ACTIVE', 'https://ui-avatars.com/api/?name=Raj+Kondvilkar&background=374151&color=fff&size=256', 'CCTNS GD-089/2026', 'Bandra Police Station, Zone-IX, Mumbai', 'Missing Person Diary [Senior Citizen Disoriented]', ?)
        """, (now_str, now_str, now_str, now_str))
        conn.commit()
    else:
        # Update existing seed cases with Indian CCTNS identifiers if they are default
        cursor.execute("""
        UPDATE cases 
        SET cctns_fir = 'CCTNS FIR-248/2026',
            police_station = 'Dadar Police Station, Zone-V, Mumbai City',
            bns_section = 'BNS Section 137(2) [Kidnapping of Minor]'
        WHERE id = 'CASE-01' AND (cctns_fir = 'PENDING_REGISTRATION' OR cctns_fir IS NULL)
        """)
        cursor.execute("""
        UPDATE cases 
        SET cctns_fir = 'CCTNS GD-089/2026',
            police_station = 'Bandra Police Station, Zone-IX, Mumbai City',
            bns_section = 'Missing Person Diary [Senior Citizen Disoriented]'
        WHERE id = 'CASE-02' AND (cctns_fir = 'PENDING_REGISTRATION' OR cctns_fir IS NULL)
        """)
        conn.commit()

    conn.close()

# Database Helper Functions
def get_all_cases():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cases ORDER BY created_at DESC")
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows

def get_case_by_id(case_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cases WHERE id = ?", (case_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def create_case(case_data: dict):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO cases (id, name, age, lkp, lkp_lat, lkp_lng, last_seen_time, med, cloth, v_max_kmh, status, img, cctns_fir, police_station, bns_section, created_at)
    VALUES (:id, :name, :age, :lkp, :lkp_lat, :lkp_lng, :last_seen_time, :med, :cloth, :v_max_kmh, :status, :img, :cctns_fir, :police_station, :bns_section, :created_at)
    """, case_data)
    conn.commit()
    conn.close()
    return case_data

def get_tips_by_case(case_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tips WHERE case_id = ? ORDER BY created_at DESC", (case_id,))
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows

def insert_tip(tip_data: dict):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO tips (id, case_id, source, signal_type, sighting_time, lat, lng, message, base_score, final_score, tier, reason, cluster_id, distance_km, original_text, lang_detected, sha256_hash, created_at)
    VALUES (:id, :case_id, :source, :signal_type, :sighting_time, :lat, :lng, :message, :base_score, :final_score, :tier, :reason, :cluster_id, :distance_km, :original_text, :lang_detected, :sha256_hash, :created_at)
    """, tip_data)
    conn.commit()
    conn.close()
    return tip_data

def update_tip_clustering(tip_id: str, cluster_id: int, final_score: int, tier: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE tips 
    SET cluster_id = ?, final_score = ?, tier = ?
    WHERE id = ?
    """, (cluster_id, final_score, tier, tip_id))
    conn.commit()
    conn.close()
