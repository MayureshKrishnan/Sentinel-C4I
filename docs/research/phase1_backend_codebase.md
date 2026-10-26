# SENTINEL - Phase 1 Pure Software Codebase Documentation & Source Files

This artifact contains the complete source code for **Phase 1: Pure Software Core**, implemented in Python FastAPI.

---

## 📁 Source File 1: Pydantic Data Schemas (`backend/app/models/schemas.py`)

```python
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class TipSubmission(BaseModel):
    incident_id: str = Field(default="INC-2026-NM01", example="INC-2026-NM01")
    source_type: str = Field(..., example="public_verified", description="responder, volunteer, public_verified, anonymous")
    latitude: float = Field(..., example=18.9876)
    longitude: float = Field(..., example=73.0021)
    observation_time: datetime = Field(..., example="2026-08-27T10:00:00Z")
    raw_text: str = Field(..., example="Saw a man matching description wearing blue jacket walking near Sector 12 bus stop")
    has_clothing_desc: bool = Field(default=False)
    has_physical_desc: bool = Field(default=False)
    has_direction_hint: bool = Field(default=False)

class FactorBreakdown(BaseModel):
    source_score: float
    spatial_score: float
    content_score: float
    temporal_decay_factor: float
    haversine_distance_km: float
    max_reachable_radius_km: float

class TipScoreResponse(BaseModel):
    tip_id: Optional[str] = None
    final_score: float = Field(..., description="Calculated score bounded 0 to 100")
    priority: str = Field(..., description="CRITICAL (70+), MEDIUM (35-69), LOW (<35)")
    is_noise: bool = Field(..., description="True if Naive Bayes flags social media noise")
    confidence_interval: List[int] = Field(..., description="Lower and upper bound confidence interval e.g. [68, 79]")
    factor_breakdown: FactorBreakdown

class SearchZone(BaseModel):
    zone_id: str
    zone_name: str
    total_score: float
    area_sq_km: float
    required_volunteers: int

class VolunteerTeam(BaseModel):
    team_id: str
    team_name: str
    member_count: int

class DispatchOptimizationInput(BaseModel):
    zones: List[SearchZone]
    teams: List[VolunteerTeam]

class TeamAssignment(BaseModel):
    zone_id: str
    zone_name: str
    zone_score: float
    assigned_team_id: str
    assigned_team_name: str
    assigned_members: int

class DispatchOptimizationResponse(BaseModel):
    status: str
    total_score_covered: float
    unassigned_zones_count: int
    assignments: List[TeamAssignment]
```

---

## 📁 Source File 2: Credibility Scoring Engine (`backend/app/services/scoring.py`)

```python
import math
from datetime import datetime, timezone
from typing import Tuple

class CredibilityScorer:
    # Baseline Weights: sum = 100
    W1_SOURCE = 40.0
    W2_SPATIAL = 35.0
    W3_CONTENT = 25.0

    # Temporal Decay: Half-life = 6 hours
    HALF_LIFE_HOURS = 6.0
    LAMBDA_DECAY = math.log(2) / HALF_LIFE_HOURS  # ~0.1155 hr^-1

    # Source Ratings (C_source)
    SOURCE_WEIGHTS = {
        "responder": 1.0,
        "volunteer": 0.8,
        "public_verified": 0.5,
        "anonymous": 0.2
    }

    # Incident LKP Baseline (Sector 12, Navi Mumbai)
    DEFAULT_LKP_LAT = 18.9876
    DEFAULT_LKP_LNG = 73.0021

    @staticmethod
    def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Calculates distance between two lat/lng points in kilometers."""
        R = 6371.0  # Earth radius in km
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) ** 2 +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(dlon / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    @classmethod
    def compute_score(
        cls,
        source_type: str,
        tip_lat: float,
        tip_lng: float,
        observation_time: datetime,
        current_time: datetime,
        has_clothing: bool,
        has_physical: bool,
        has_direction: bool,
        is_noise: bool,
        lkp_lat: float = DEFAULT_LKP_LAT,
        lkp_lng: float = DEFAULT_LKP_LNG,
        terrain_speed_kmh: float = 3.5  # Mixed terrain average speed
    ) -> Tuple[float, str, list, dict]:
        """
        Computes master credibility score:
        S = (w1*C_source + w2*V_spatial + w3*I_content) * e^(-lambda * delta_t)
        """
        # 1. Source Reliability (C_source)
        c_source = cls.SOURCE_WEIGHTS.get(source_type.lower(), 0.2)

        # 2. Elapsed Time & Decay (e^-lambda*dt)
        if observation_time.tzinfo is None:
            observation_time = observation_time.replace(tzinfo=timezone.utc)
        if current_time.tzinfo is None:
            current_time = current_time.replace(tzinfo=timezone.utc)

        delta_t_hours = max(0.0, (current_time - observation_time).total_seconds() / 3600.0)
        decay_factor = math.exp(-cls.LAMBDA_DECAY * delta_t_hours)

        # 3. Spatial Proximity (V_spatial)
        distance_km = cls.haversine_distance(lkp_lat, lkp_lng, tip_lat, tip_lng)
        max_reachable_radius = max(0.5, terrain_speed_kmh * delta_t_hours)
        
        if distance_km > max_reachable_radius:
            v_spatial = max(0.0, 1.0 - (distance_km - max_reachable_radius) / max_reachable_radius)
        else:
            v_spatial = 1.0 - (distance_km / (max_reachable_radius * 2.0))
        v_spatial = max(0.0, min(1.0, v_spatial))

        # 4. Content Richness (I_content)
        i_base = 0.0
        if has_clothing:
            i_base += 0.35
        if has_physical:
            i_base += 0.35
        if has_direction:
            i_base += 0.30

        # Apply Naive Bayes noise multiplier
        noise_multiplier = 0.1 if is_noise else 1.0
        i_content = i_base * noise_multiplier

        # 5. Master Scoring Formula
        raw_score = (cls.W1_SOURCE * c_source +
                     cls.W2_SPATIAL * v_spatial +
                     cls.W3_CONTENT * i_content)
        
        final_score = round(raw_score * decay_factor, 1)
        final_score = max(0.0, min(100.0, final_score))

        # Priority Matrix
        if final_score >= 70.0:
            priority = "CRITICAL"
        elif final_score >= 35.0:
            priority = "MEDIUM"
        else:
            priority = "LOW"

        # Confidence Interval calculation
        margin = 5 if c_source >= 0.8 else 9
        ci_lower = max(0, int(final_score - margin))
        ci_upper = min(100, int(final_score + margin))

        breakdown = {
            "source_score": round(c_source, 2),
            "spatial_score": round(v_spatial, 2),
            "content_score": round(i_content, 2),
            "temporal_decay_factor": round(decay_factor, 4),
            "haversine_distance_km": round(distance_km, 2),
            "max_reachable_radius_km": round(max_reachable_radius, 2)
        }

        return final_score, priority, [ci_lower, ci_upper], breakdown
```

---

## 📁 Source File 3: Naive Bayes Text Classifier (`backend/app/services/classifier.py`)

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class TipTextClassifier:
    def __init__(self):
        self.vectorizer = CountVectorizer(stop_words='english')
        self.model = MultinomialNB()
        self._train_baseline_model()

    def _train_baseline_model(self):
        # Synthetic training corpus
        sighting_texts = [
            "saw a man matching description wearing blue jacket near sector 12",
            "spotted person walking heading north along palm avenue at 14:30",
            "eyewitness saw missing individual near park entrance black backpack",
            "found person sitting near bus stop sector 15 wearing dark jeans",
            "responder spotted male height 5ft 10in walking towards station",
            "volunteer saw subject heading east on main road"
        ]
        
        noise_texts = [
            "hope he is found soon please pray for his family",
            "please share this post on facebook and retweet",
            "praying for his safe return share maximum link below",
            "fake news do not share unverified rumors on whatsapp",
            "god bless hope police find him fast share with friends",
            "join our whatsapp group for daily emergency news updates"
        ]

        X_train = sighting_texts + noise_texts
        y_train = ["SIGHTING"] * len(sighting_texts) + ["NOISE"] * len(noise_texts)

        X_vec = self.vectorizer.fit_transform(X_train)
        self.model.fit(X_vec, y_train)

    def predict_is_noise(self, raw_text: str) -> bool:
        """Returns True if the text is classified as social media NOISE."""
        if not raw_text or len(raw_text.strip()) < 5:
            return False
        
        vec = self.vectorizer.transform([raw_text.lower()])
        prediction = self.model.predict(vec)[0]
        return prediction == "NOISE"
```

---

## 📁 Source File 4: PuLP Linear Programming Solver (`backend/app/services/optimizer.py`)
```python
import pulp
from typing import List, Dict

class ResourceOptimizer:
    @staticmethod
    def solve_dispatch(zones: List[Dict], teams: List[Dict]) -> Dict:
        """
        Solves linear program matching teams to high-priority search zones:
        max sum(S_z * x_{z,m})
        """
        prob = pulp.LpProblem("Sentinel_Dispatch_Optimization", pulp.LpMaximize)

        # Decision Variables x_{z,m}
        x = {}
        for z in zones:
            for m in teams:
                var_name = f"assign_{z['zone_id']}_{m['team_id']}"
                x[(z['zone_id'], m['team_id'])] = pulp.LpVariable(var_name, cat=pulp.LpBinary)

        # Objective Function: Maximize total score covered
        prob += pulp.lpSum(z['total_score'] * x[(z['zone_id'], m['team_id'])] for z in zones for m in teams)

        # Constraint 1: Each zone gets at most 1 team
        for z in zones:
            prob += pulp.lpSum(x[(z['zone_id'], m['team_id'])] for m in teams) <= 1

        # Constraint 2: Each team assigned to at most 1 zone
        for m in teams:
            prob += pulp.lpSum(x[(z['zone_id'], m['team_id'])] for z in zones) <= 1

        # Constraint 3: Member capacity check
        for z in zones:
            for m in teams:
                if m['member_count'] < z['required_volunteers']:
                    prob += x[(z['zone_id'], m['team_id'])] == 0

        prob.solve(pulp.PULP_CBC_CMD(msg=0))

        assignments = []
        assigned_zone_ids = set()
        total_score_covered = 0.0

        for z in zones:
            for m in teams:
                if pulp.value(x[(z['zone_id'], m['team_id'])]) == 1.0:
                    assignments.append({
                        "zone_id": z['zone_id'],
                        "zone_name": z['zone_name'],
                        "zone_score": z['total_score'],
                        "assigned_team_id": m['team_id'],
                        "assigned_team_name": m['team_name'],
                        "assigned_members": m['member_count']
                    })
                    assigned_zone_ids.add(z['zone_id'])
                    total_score_covered += z['total_score']

        unassigned_count = len(zones) - len(assigned_zone_ids)

        return {
            "status": "Optimal",
            "total_score_covered": round(total_score_covered, 1),
            "unassigned_zones_count": unassigned_count,
            "assignments": assignments
        }
```

---

## 📁 Source File 5: Automated PyTest Suite (`backend/tests/test_scoring.py`)

```python
import pytest
from datetime import datetime, timedelta, timezone
from app.services.scoring import CredibilityScorer
from app.services.classifier import TipTextClassifier

def test_temporal_decay_halving():
    """Verifies score decays by ~50% after exactly 6 hours (half-life)."""
    now = datetime.now(timezone.utc)
    t_0h = now
    t_6h = now - timedelta(hours=6)

    score_0h, _, _, _ = CredibilityScorer.compute_score(
        "responder", 18.9876, 73.0021, t_0h, now, True, True, True, False
    )
    score_6h, _, _, _ = CredibilityScorer.compute_score(
        "responder", 18.9876, 73.0021, t_6h, now, True, True, True, False
    )

    # 6-hour score should be ~50% of 0-hour score
    assert score_6h == pytest.approx(score_0h * 0.5, abs=2.0)

def test_naive_bayes_classifier():
    """Verifies sighting text vs social media noise predictions."""
    classifier = TipTextClassifier()
    assert classifier.predict_is_noise("saw man wearing blue jacket near sector 12") == False
    assert classifier.predict_is_noise("please share this link on facebook and pray") == True
```
