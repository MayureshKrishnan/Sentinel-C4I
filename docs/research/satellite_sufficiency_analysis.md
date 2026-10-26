# SENTINEL - Final Satellite Dataset Architecture & Sufficiency Analysis

## 🎯 Short Answer: **NO, you need EXACTLY TWO datasets (Sentinel-2 + SRTM DEM)**

You cannot rely *only* on optical imagery (Sentinel-2 and NASA Worldview) because **optical imagery only sees 2D surface features from above (flat ground)**. It cannot measure 3D elevation height or hill steepness!

To calculate terrain mobility ($V_{\text{spatial}}$), you need **2 complementary dimensions**:

```
                  +-------------------------------------------------------------+
                  |         SENTINEL FULL TERRAIN MOBILITY ENGINE              |
                  +-------------------------------------------------------------+
                                                 |
         +---------------------------------------+---------------------------------------+
         |                                                                               |
         ▼                                                                               ▼
[DATASET 1: Sentinel-2 L2A (10m Live)]                                  [DATASET 2: SRTM DEM (30m Elevation)]
- Surface Type & Cover (2D)                                            - Elevation & Slope Angle (30m 3D)
- NDVI: Forest vs Open field                                           - Slope $\theta > 30^\circ$ Steep Hill Penalty
- NDWI: Rivers & Impassable Water                                      - Cliff / Ridge Barriers
- Paved Roads vs Unpaved Terrain                                       - Elevation contour energy burn factor
```

---

## 🔬 Why Optical Imagery Alone Fails in Search & Rescue

Imagine a missing person is reported near a hill (e.g., Parsik Hills in Navi Mumbai):

1. **What Sentinel-2 sees**: "Green trees / Forest".
2. **What Sentinel-2 MISSED**: Is that forest on flat ground (walkable at 2 km/h) or on a **60-degree steep cliff / drop-off** (physically impassable or requires crawling at 0.2 km/h)?

Optical satellite photos cannot see vertical steepness. **SRTM DEM (Shuttle Radar Topography Mission)** supplies the 3D elevation map required to compute slope angles ($\theta$):

$$\text{Slope Angle } \theta = \arctan\left(\frac{\Delta \text{Elevation}}{\Delta \text{Distance}}\right)$$

$$\text{Speed Multiplier } M_{\text{slope}} = \begin{cases} 1.0 & \text{if } \theta \le 15^\circ \text{ (Gentle slope)} \\ 0.5 & \text{if } 15^\circ < \theta \le 30^\circ \text{ (Steep climb)} \\ 0.1 & \text{if } \theta > 30^\circ \text{ (Cliff / Impassable)} \end{cases}$$

---

## 🏆 The Ultimate 2-Dataset Stack for SENTINEL

You only need **2 FREE Datasets** to cover 100% of the project's GIS requirements:

| # | Dataset Name | What It Provides | Why It Is Mandatory |
| :--- | :--- | :--- | :--- |
| **1** | **Sentinel-2 L2A (ESA)** | Live 10m surface land cover (forest, roads, water) | Identifies land type & speed limits ($2\text{ km/h}$ forest vs $5\text{ km/h}$ road). |
| **2** | **SRTM DEM (NASA/USGS)** | 30m 3D elevation & slope angles ($\theta$) | Identifies steep hills, cliffs, and mountain slope penalties. |

*(Note: NASA Worldview and ISRO Bhuvan can be used as optional visual verification layers, but **Sentinel-2 + SRTM DEM** is the complete functional engine).*

---

## 💡 Bulletproof Panel Answer
> *"We use a **2-dataset combination**: **Sentinel-2 L2A** for live 10-meter surface land cover (forests, roads, water) and **SRTM DEM** for 3D elevation and slope angles. Together, they provide 100% of the geospatial data needed for terrain-adjusted search radii without needing expensive enterprise tools."*
