# SENTINEL - Member 2 Mock Data Spec (`mock_tips.json`)

Use this static JSON dataset to build and test your **React + Leaflet Command Dashboard** in Phase 1 without needing Member 1's backend or Member 3's hardware!

---

```json
[
  {
    "id": "TIP-001",
    "score": 91,
    "priority": "CRITICAL",
    "source_type": "responder",
    "raw_text": "First responder verified sighting of man matching description wearing blue jacket walking north along Palm Ave.",
    "latitude": 18.9912,
    "longitude": 73.0045,
    "location_name": "Palm Avenue, Navi Mumbai",
    "observation_time": "2026-08-27T10:15:00Z",
    "is_noise": false,
    "confidence_interval": [85, 96]
  },
  {
    "id": "TIP-002",
    "score": 78,
    "priority": "CRITICAL",
    "source_type": "volunteer",
    "raw_text": "Field volunteer spotted subject carrying black backpack near Sector 12 bus stop.",
    "latitude": 18.9885,
    "longitude": 73.0030,
    "location_name": "Sector 12 Bus Stop",
    "observation_time": "2026-08-27T09:45:00Z",
    "is_noise": false,
    "confidence_interval": [72, 84]
  },
  {
    "id": "TIP-003",
    "score": 55,
    "priority": "MEDIUM",
    "source_type": "public_verified",
    "raw_text": "Public eyewitness report of a person sitting near Central Park entrance wearing dark jeans.",
    "latitude": 18.9820,
    "longitude": 72.9980,
    "location_name": "Central Park Entrance",
    "observation_time": "2026-08-27T08:30:00Z",
    "is_noise": false,
    "confidence_interval": [48, 62]
  },
  {
    "id": "TIP-004",
    "score": 28,
    "priority": "LOW",
    "source_type": "anonymous",
    "raw_text": "Unverified web report claiming sighting near highway toll plaza.",
    "latitude": 18.9650,
    "longitude": 72.9850,
    "location_name": "Highway Toll Plaza",
    "observation_time": "2026-08-27T06:00:00Z",
    "is_noise": false,
    "confidence_interval": [20, 35]
  }
]
```
