import math

class SpatialMathEngine:
    def __init__(self):
        # Earth mean radius in km
        self.R = 6371.0088
        # Human exhaustion decay constant (lambda)
        self.lambda_decay = 0.06 
        # Average Indian Train/Bus speed in km/h
        self.avg_transit_speed_kmh = 55.0 

    def calculate_tobler_speed(self, slope_degrees: float) -> float:
        """ 
        Calculates human walking speed in km/h based on terrain slope using Tobler's Hiking Function:
        v = 6 * exp(-3.5 * |tan(slope_rad) + 0.05|)
        """
        slope_fraction = math.tan(math.radians(slope_degrees))
        speed = 6.0 * math.exp(-3.5 * abs(slope_fraction + 0.05))
        return round(speed, 2)

    def calculate_expanding_radius(self, hours_elapsed: float, average_slope: float) -> float:
        """ Calculates the maximum walking distance using Tobler + Exhaustion Integral Calculus. """
        v0 = self.calculate_tobler_speed(average_slope)
        max_distance = (v0 / self.lambda_decay) * (1.0 - math.exp(-self.lambda_decay * hours_elapsed))
        return round(max_distance, 2)

    def destination_point(self, lat1: float, lng1: float, distance_km: float, bearing_deg: float) -> list:
        """ Calculates (lat, lng) destination point on Earth sphere given distance and bearing. """
        d_r = distance_km / self.R
        b_r = math.radians(bearing_deg)
        lat1_r = math.radians(lat1)
        lng1_r = math.radians(lng1)

        lat2_r = math.asin(
            math.sin(lat1_r) * math.cos(d_r) + 
            math.cos(lat1_r) * math.sin(d_r) * math.cos(b_r)
        )
        lng2_r = lng1_r + math.atan2(
            math.sin(b_r) * math.sin(d_r) * math.cos(lat1_r),
            math.cos(d_r) - math.sin(lat1_r) * math.sin(lat2_r)
        )
        return [round(math.degrees(lat2_r), 5), round(math.degrees(lng2_r), 5)]

    def generate_anisotropic_isochrone(
        self, 
        lkp_lat: float, 
        lkp_lng: float, 
        hours_elapsed: float = 1.0, 
        base_slope_deg: float = 3.5, 
        num_vertices: int = 24
    ) -> dict:
        """
        Generates realistic, non-circular, anisotropic search perimeter polygons 
        using Tobler's Hiking Function across varying directional slopes and geographic friction.
        """
        inner_coords = []
        outer_coords = []
        slopes_sampled = []
        speeds_sampled = []

        # Outer time multiplier (physics gate threshold, typically 2x elapsed hours)
        outer_hours = max(2.0, hours_elapsed * 1.8)

        for i in range(num_vertices):
            angle = i * (360.0 / num_vertices)

            # Terrain slope variation per directional azimuth (simulating ridges, valleys, and roads)
            # Produces an irregular, realistic organic shape
            directional_slope = (
                base_slope_deg + 
                2.6 * math.sin(math.radians(angle * 2.0)) + 
                1.4 * math.cos(math.radians(angle * 3.0))
            )
            # Clamp slope to realistic limits (-3 deg descent to +12 deg ascent)
            directional_slope = max(-3.0, min(12.0, directional_slope))
            slopes_sampled.append(directional_slope)

            # Evaluate Tobler's speed for this direction
            v = self.calculate_tobler_speed(directional_slope)
            speeds_sampled.append(v)

            # Compute exhausted travel distances
            dist_inner = (v / self.lambda_decay) * (1.0 - math.exp(-self.lambda_decay * hours_elapsed))
            dist_outer = (v / self.lambda_decay) * (1.0 - math.exp(-self.lambda_decay * outer_hours))

            # Geographic coastline/barrier constraint for Mumbai coastal zone:
            # Bearings 240 deg - 300 deg face the Arabian Sea
            if 18.8 <= lkp_lat <= 19.3 and 72.7 <= lkp_lng <= 73.1:
                if 235 <= angle <= 305:
                    dist_inner = min(dist_inner, 2.3)
                    dist_outer = min(dist_outer, 3.8)

            inner_pt = self.destination_point(lkp_lat, lkp_lng, dist_inner, angle)
            outer_pt = self.destination_point(lkp_lat, lkp_lng, dist_outer, angle)

            inner_coords.append(inner_pt)
            outer_coords.append(outer_pt)

        avg_slope = round(sum(slopes_sampled) / len(slopes_sampled), 1)
        min_speed = round(min(speeds_sampled), 1)
        max_speed = round(max(speeds_sampled), 1)

        return {
            "inner_polygon": inner_coords,
            "outer_polygon": outer_coords,
            "metrics": {
                "average_slope_deg": avg_slope,
                "min_speed_kmh": min_speed,
                "max_speed_kmh": max_speed,
                "num_vertices": num_vertices,
                "hours_elapsed": hours_elapsed,
                "isochrone_type": "TOBLER_ANISOTROPIC_POLYGON"
            }
        }

    def haversine_km(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """ Calculates great-circle distance between two points in km. """
        p1, p2 = math.radians(lat1), math.radians(lat2)
        dphi, dlmb = p2 - p1, math.radians(lon2 - lon1)
        a = math.sin(dphi / 2.0) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlmb / 2.0) ** 2
        return 2.0 * self.R * math.asin(math.sqrt(a))

    def haversine_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        return self.haversine_km(lat1, lon1, lat2, lon2)

    def is_feasible(self, lkp: tuple, tip: tuple, hours_since_lkp: float, v_max_kmh: float = 5.0) -> tuple:
        """ Layer 1 Physics Gate: checks if distance is physically reachable. """
        d = self.haversine_km(lkp[0], lkp[1], tip[0], tip[1])
        return (d <= v_max_kmh * hours_since_lkp, round(d, 2))
