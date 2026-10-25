import numpy as np
from sklearn.cluster import DBSCAN
import math

class MLClusteringEngine:
    def __init__(self):
        self.R = 6371.0088 # Earth radius in km

    def find_clusters(self, tips_data: list, eps_km: float = 0.5, min_samples: int = 3) -> dict:
        """
        tips_data: List of dicts [{"id": 1, "lat": 19.0596, "lng": 72.8295}, ...]
        Returns a mapping of tip IDs to their assigned cluster ID (-1 means Noise).
        """
        if not tips_data or len(tips_data) < min_samples:
            return {t['id']: -1 for t in tips_data}

        # Extract coordinates and convert to radians for the Haversine metric
        coords = np.array([[t['lat'], t['lng']] for t in tips_data])
        coords_radians = np.radians(coords)
        
        # eps must be in radians for the haversine metric in sklearn
        eps_radians = eps_km / self.R

        # Run DBSCAN
        db = DBSCAN(eps=eps_radians, min_samples=min_samples, metric='haversine', algorithm='ball_tree')
        labels = db.fit_predict(coords_radians)

        results = {}
        for i, tip in enumerate(tips_data):
            results[tip['id']] = int(labels[i])
            
        return results

    def calculate_final_score(self, is_feasible: bool, cluster_id: int, base_trust: int = 50) -> int:
        """
        Layer 3: Weighted Heuristic Scoring
        is_feasible (Layer 1 - Haversine) acts as a strict gate.
        cluster_id (Layer 2 - DBSCAN): -1 is noise (no corroboration).
        """
        if not is_feasible:
            return 0 # Fails physics check

        score = 0
        
        # Spatial Gate Passed (Base score for being physically possible)
        score += 30 
        
        # Trust Weight
        score += (base_trust * 0.2)
        
        # Cluster Corroboration Weight
        if cluster_id != -1:
            score += 50 # Massive boost if corroborated by others

        return min(int(score), 100)
