# Sentinel Intelligence & Kinematics Engine (sentinel-engine)

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn%20DBSCAN-F7931E.svg)](https://scikit-learn.org/)
[![Indian Legal Compliance](https://img.shields.io/badge/Compliance-BSA%20Sec--63-darkred.svg)](https://www.mha.gov.in/)

The computational core of the Sentinel V2 Tactical C4I Platform. This module houses the spatial calculus, unsupervised machine learning, transit chokepoint models, and statutory digital evidence hashing.

---

## 📂 Module Architecture

```text
sentinel-engine/
├── __init__.py           # Package initializer
├── spatial_math.py       # Tobler's Hiking function & Haversine spherical kinematics
├── ml_clustering.py      # Scikit-Learn DBSCAN density clustering engine
├── indian_c4i.py         # Suburban rail, FASTag toll corridors, Indic NLP & BSA-63 cert
└── README.md             # Engine documentation
```

---

## ⚡ Core Computational Responsibilities

### 1. `spatial_math.py` — Topographic & Kinematic Calculus
* **Tobler's Hiking Function**:
  $$W = 6 \cdot e^{-3.5 \cdot |\tan(\theta) + 0.05|}$$
  Calculates human walking velocity over terrain slope angles ($\theta$).
* **Spherical Haversine Distance**: Computes great-circle distance on a spherical Earth ($R = 6371\text{ km}$).
* **Exhaustion Decay Calculus**: Models physiological human decay over elapsed search hours.

### 2. `ml_clustering.py` — Unsupervised Spatial Clustering
* **Scikit-Learn DBSCAN**: Density-Based Spatial Clustering of Applications with Noise.
* Parameters: $\varepsilon = 0.5\text{ km}$, $\text{min\_samples} = 2$.
* Distance Metric: Haversine radians on ball-tree spatial indexing.
* Automatically identifies corroborated multi-eyewitness sighting clusters and filters out isolated noise.

### 3. `indian_c4i.py` — Transit Chokepoints, Indic NLP & Legal Forensics
* **Mumbai Suburban Railway Model**: 17 major stations across Western & Central Railway corridors (Churchgate to Virar/Kalyan) solving rapid transit displacement.
* **FASTag NHAI Toll Plaza Interception**: 5 Mumbai entry nakas (Vashi, Dahisar, Mulund EEH, Mulund LBS, Airoli) to detect high-speed ($>80\text{ km/h}$) vehicular flight.
* **Vernacular Indic NLP Parser**: Extracts landmarks (*chowk, mandir, naka, station*), attire, and emotional states from Devanagari Marathi and Hinglish civilian tips.
* **Bharatiya Sakshya Adhiniyam (BSA), 2023 Section 63 Court Certificate Generator**: Generates statutory electronic evidence certificates backed by SHA-256 Merkle root hashing.

---

## 🛠️ Requirements & Standalone Testing
```bash
pip install numpy scikit-learn
```
