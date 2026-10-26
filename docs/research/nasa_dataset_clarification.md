# SENTINEL - Clarification: The NASA SRTM DEM Dataset

## 🎯 Short Answer: **SRTM DEM IS THE NASA DATASET!**

Nothing happened to the NASA dataset—it is **Component 1 (the static downloaded dataset)** in our Hybrid Architecture!

Here is the exact identity breakdown:

```
+---------------------------------------------------------------------------------------------------+
|  SRTM DEM  =  Shuttle Radar Topography Mission Digital Elevation Model                           |
|  PRODUCED & OPERATED BY: NASA (National Aeronautics and Space Administration) & USGS              |
+---------------------------------------------------------------------------------------------------+
```

---

## 🏛️ How the Two Datasets Match the Hybrid Architecture

| Hybrid Component | Dataset Name | Agency / Provider | Role & Method |
| :--- | :--- | :--- | :--- |
| **Component 1 (Static Downloaded)** | **SRTM DEM 30m** | 🇺🇸 **NASA / USGS** | **Downloaded once & stored locally in PostGIS DB**. Calculates 3D elevation, slope angles ($\theta > 30^\circ$), and physical hill barriers offline. |
| **Component 2 (Live API Stream)** | **Sentinel-2 L2A 10m** | 🇪🇺 **ESA (European Space Agency)** | **Queried dynamically live via Copernicus API**. Calculates 2D land cover (forest, roads, water) and current ground truth. |

---

## 💡 Summary for your records
* **Dataset 1 (NASA)**: **NASA SRTM DEM** $\rightarrow$ Local Static Download for Elevation & Slope.
* **Dataset 2 (ESA)**: **ESA Sentinel-2** $\rightarrow$ Live API Query for Current Land Cover & Water.

So the NASA dataset is right here—it is our primary local elevation backbone!
