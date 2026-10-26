# SENTINEL - Direct Satellite Dataset Links & Quick Reference Sheet

This Markdown document contains the **direct portal links and quick exploration steps** for the two core satellite datasets used in the **SENTINEL** project.

---

## 🛰️ 1. Sentinel-2 Multi-Spectral Imagery (ESA Copernicus)

### 🔗 Direct Portal Links:
* **Primary Live Portal**: [https://browser.dataspace.copernicus.eu/](https://browser.dataspace.copernicus.eu/)
* **Official Data Space Ecosystem**: [https://dataspace.copernicus.eu/](https://dataspace.copernicus.eu/)

### 📌 Quick Exploration Steps:
1. Open the [Copernicus Browser](https://browser.dataspace.copernicus.eu/).
2. Type **Navi Mumbai** (or coordinates `18.9876, 73.0021`) in the search bar.
3. Select **Sentinel-2** -> **L2A** on the left panel.
4. Click **Search** and select any scene with low cloud cover (< 10%).
5. **Explore Layers**:
   - **True Color (RGB)**: View 10-meter optical photos (roads, buildings, rivers, vegetation).
   - **NDVI (Vegetation Index)**: View dense forest patches (speed = $2.0 \text{ km/h}$) vs urban ground (speed = $5.0 \text{ km/h}$).
   - **NDWI (Water Index)**: View impassable water bodies (speed = $0.0 \text{ km/h}$).

---

## ⛰️ 2. SRTM DEM - Digital Elevation Model (NASA / USGS)

### 🔗 Direct Portal Links:
* **Primary USGS Portal**: [https://earthexplorer.usgs.gov/](https://earthexplorer.usgs.gov/)
* **OpenTopography Browser (Alternative)**: [https://portal.opentopography.org/](https://portal.opentopography.org/)

### 📌 Quick Exploration Steps:
1. Open [USGS EarthExplorer](https://earthexplorer.usgs.gov/).
2. Under **Search Criteria**, click **Coordinates** -> Enter Latitude `18.9876`, Longitude `73.0021` (Navi Mumbai).
3. Click the **Data Sets** tab at the top.
4. Expand **Digital Elevation** -> **SRTM** -> Check **SRTM 1 Arc-Second Global** (30m resolution).
5. Click **Results** to view the elevation tile coverage over hills (e.g., Parsik Hills / Western Ghats near Navi Mumbai) used to compute slope speed penalties ($\theta > 30^\circ$).

---

## 💡 Quick Summary for Panel Defense
> *"We use **Sentinel-2 L2A** for live 10m 2D land cover classification and **SRTM DEM** for 30m 3D elevation and slope angles. Together, they provide 100% of the geospatial intelligence required for SENTINEL at zero cost."*
