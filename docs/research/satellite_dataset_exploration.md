# SENTINEL - Satellite & GIS Dataset Exploration Guide

This guide provides direct links and step-by-step instructions to explore the **3 open IEEE GRSS Satellite & GIS datasets** used by SENTINEL.

---

## 🌐 1. Sentinel-2 Multi-Spectral Imagery (ESA Copernicus)

### 🔗 Direct Portal Links:
* **Copernicus Browser**: [https://browser.dataspace.copernicus.eu/](https://browser.dataspace.copernicus.eu/)
* **Copernicus Data Space Ecosystem**: [https://dataspace.copernicus.eu/](https://dataspace.copernicus.eu/)

### 🗺️ Step-by-Step Exploration (No Coding Needed):
1. Click the [Copernicus Browser](https://browser.dataspace.copernicus.eu/) link.
2. In the top-left search bar, type your target location: **Navi Mumbai, India** (or coordinates `18.9876, 73.0021`).
3. On the left panel under **Data Sources**, check **Sentinel-2** (Select **L2A** for surface reflectance).
4. Click **Search** and select the clearest image with **< 10% cloud cover**.
5. **Explore Land Cover Bands**:
   - Select **True Color (RGB)** to see optical satellite imagery (roads, buildings, rivers, forests).
   - Select **NDVI (Normalized Difference Vegetation Index)** visualization on the left menu:
     - 🟢 **Bright Green Areas**: Dense vegetation / forest (Reachable speed = $2.0 \text{ km/h}$).
     - 🟤 **Grey/Brown Areas**: Paved roads & urban land (Reachable speed = $5.0 \text{ km/h}$).
   - Select **NDWI (Normalized Difference Water Index)**:
     - 🔵 **Blue Areas**: Water bodies (Impassable barriers, speed = $0.0 \text{ km/h}$).
6. **Download GeoTIFF**: Click the **Analytical Download** button on the right sidebar -> Choose **Bands 2, 3, 4, 8** in **TIFF** format.

---

## ⛰️ 2. SRTM DEM - Digital Elevation Model (NASA / USGS)

### 🔗 Direct Portal Links:
* **USGS EarthExplorer**: [https://earthexplorer.usgs.gov/](https://earthexplorer.usgs.gov/)
* **OpenTopography (Alternative Browser)**: [https://portal.opentopography.org/](https://portal.opentopography.org/)

### 🗺️ Step-by-Step Exploration:
1. Go to [USGS EarthExplorer](https://earthexplorer.usgs.gov/).
2. Under **Search Criteria**, click **Coordinates** -> Enter Latitude `18.9876`, Longitude `73.0021` (Navi Mumbai).
3. Click the **Data Sets** tab at the top.
4. Expand **Digital Elevation** -> Expand **SRTM** -> Check **SRTM 1 Arc-Second Global** (30m resolution).
5. Click **Results** at the bottom.
6. Click the **Footprint / Browse Overlay** icon to see elevation coverage over hills/mountains (e.g., Parsik Hills / Western Ghats near Navi Mumbai).
7. **Download**: Create a free USGS account and click **Download Options** -> Select **GeoTIFF 1 Arc-Second**.

---

## 🇮🇳 3. ISRO Bhuvan LULC - India Land Use & Land Cover (ISRO NRSC)

### 🔗 Direct Portal Links:
* **ISRO Bhuvan 2D Portal**: [https://bhuvan.nrsc.gov.in/](https://bhuvan.nrsc.gov.in/)
* **Bhuvan Thematic Services (LULC)**: [https://bhuvan-app1.nrsc.gov.in/thematic/thematic/index.php](https://bhuvan-app1.nrsc.gov.in/thematic/thematic/index.php)

### 🗺️ Step-by-Step Exploration:
1. Open the [Bhuvan Thematic Portal](https://bhuvan-app1.nrsc.gov.in/thematic/thematic/index.php).
2. On the left sidebar, click **Select Sector** -> Choose **Land Use / Land Cover (LULC)**.
3. Select **Scale**: **1:50,000** (High Resolution).
4. Navigate the map to **Maharashtra** -> **Thane / Navi Mumbai**.
5. Observe the color-coded LULC Indian terrain classification legend:
   - 🟥 **Red**: Built-up / Urban settlements.
   - 🟩 **Green**: Deciduous Forest / Scrub forest.
   - 🟨 **Yellow**: Agricultural cropland.
   - 🟦 **Blue**: Water bodies / Lakes / Creeks (e.g., Thane Creek).
