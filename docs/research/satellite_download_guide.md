# SENTINEL - Step-by-Step Satellite Dataset Download Guide

This guide walks Member 3 (or any team member) through downloading the raw **Sentinel-2 L2A GeoTIFF** and **SRTM DEM Elevation** files for the target demo patch (**Navi Mumbai, India**).

---

## 🛰️ 1. How to Download Sentinel-2 L2A GeoTIFF (ESA Copernicus)

### ⏱️ Time Required: 3 minutes (No registration required for basic download!)

1. Open the **Copernicus Browser**: 🔗 [https://browser.dataspace.copernicus.eu/](https://browser.dataspace.copernicus.eu/)
2. In the top search bar, type: **Navi Mumbai, India** (or coordinates `18.9876, 73.0021`).
3. On the left sidebar under **Search Criteria**:
   - Check **Sentinel-2** -> Select **L2A** (Surface Reflectance).
   - Set **Max Cloud Cover** slider to **< 10%**.
   - Click **Search**.
4. Select a clear scene from the search results (e.g., recent date).
5. On the **right-hand toolbar**, click the **Download Image** icon (or **Analytical Download** tab).
6. Configure Download Settings:
   - **Format**: `TIFF (8-bit or 16-bit)` or `GeoTIFF`
   - **Resolution**: `HIGH` (10m)
   - **Layers**: Select **True Color**, **NDVI**, or check individual Bands: **B02 (Blue), B03 (Green), B04 (Red), B08 (NIR)**.
7. Click **Download**. You now have the 10m land cover GeoTIFF file!

---

## ⛰️ 2. How to Download SRTM DEM Elevation Tile (USGS EarthExplorer)

### ⏱️ Time Required: 4 minutes (Requires free USGS account)

1. Open **USGS EarthExplorer**: 🔗 [https://earthexplorer.usgs.gov/](https://earthexplorer.usgs.gov/)
2. Click **Register** at the top right to create a **free USGS account** (takes 1 minute). Log in.
3. Under **Search Criteria** -> **Polygon / Circle** -> Click **Add Coordinate**:
   - Latitude: `18.9876`
   - Longitude: `73.0021` (Navi Mumbai center)
4. Click the **Data Sets** tab at the top.
5. Expand **Digital Elevation** -> Expand **SRTM** -> Check **SRTM 1 Arc-Second Global** (30m resolution).
6. Click **Results** at the bottom.
7. Locate the tile covering Navi Mumbai (Tile ID: `n18_e073_1arc_v3.tif`).
8. Click the **Download Options** icon (small green disk with down arrow).
9. Select **GeoTIFF 1 Arc-Second (24.7 MB)** and click **Download**.

---

## 📁 Where to Store Downloaded Files in Your Project Directory

Once downloaded, place both files into your project's `gis/` folder:

```
sentinel/
└── gis/
    ├── sentinel2_navi_mumbai_10m.tif   <-- ESA Sentinel-2 L2A File
    └── srtm_n18_e073_30m.tif           <-- NASA SRTM DEM Elevation File
```

These files will be loaded into **QGIS** by Member 3 to construct the unified **Terrain Cost Raster**!
