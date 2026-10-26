# SENTINEL: IEEE GRSS Satellite Terrain Layer Specification

## 1. Satellite Data Sources & Specifications

SENTINEL integrates three open, zero-licensing-cost remote sensing data products to replace uniform spatial radius assumptions with terrain-adjusted mobility models:

| Satellite / Sensor | Organization | Spatial Resolution | Revisit / Epoch | Features Extracted | Data Access URL |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Sentinel-2 (MSI)** | ESA Copernicus | 10 meters | 5 days | Land cover (Forest, Urban, Water, Roads, Open field) | `dataspace.copernicus.eu` |
| **SRTM DEM** | NASA / USGS | 30 meters (1 arc-sec) | Static (2000) | Elevation, slope angle, physical ridge barriers | `earthexplorer.usgs.gov` |
| **ISRO Bhuvan LULC** | ISRO NRSC | 1:50,000 / 10m | India Specific | Regional land use classification optimized for India | `bhuvan.nrsc.gov.in` |

---

## 2. Preprocessing & Terrain Cost Raster Construction

To maintain real-time performance (< 1s API responses), satellite data is **preprocessed offline** into a unified **Terrain Cost Raster** using Python `rasterio`, `GDAL`, and `QGIS`.

### Workflow Steps:
1. **Download Scene**: Download Sentinel-2 geotiff (Bands 2, 3, 4, 8) and SRTM DEM tiles for target area (e.g., 10x10 km patch around Navi Mumbai).
2. **Compute NDVI & Land Cover**:
   $$\text{NDVI} = \frac{\text{NIR (Band 8)} - \text{Red (Band 4)}}{\text{NIR (Band 8)} + \text{Red (Band 4)}}$$
   * $\text{NDVI} > 0.6 \implies$ Dense Forest / Vegetation (Max Speed: $2.0 \text{ km/h}$)
   * $\text{NDVI} < 0.1 \land \text{Reflectance} > \text{Threshold} \implies$ Paved Road / Urban (Max Speed: $5.0 \text{ km/h}$)
   * NDWI (Water Index) $> 0.2 \implies$ Water Body (Impassable: Speed $0.0 \text{ km/h}$)
3. **Compute Slope Angle**:
   Using SRTM DEM, compute slope gradient $\theta$:
   $$\text{Slope Factor} = \begin{cases} 1.0 & \theta \le 15^\circ \\ 0.7 & 15^\circ < \theta \le 30^\circ \\ 0.3 & \theta > 30^\circ \end{cases}$$
4. **Export GeoTIFF & Ingest into PostGIS**:
   ```bash
   raster2pgsql -s 4326 -I -C -M terrain_cost_navi_mumbai.tif public.terrain_raster | psql -d sentinel_db
   ```

---

## 3. Runtime PostGIS Spatial Query Integration

FastAPI executes a spatial lookup query to extract local terrain mobility limits for any given tip coordinate:

```sql
SELECT ST_Value(rast, ST_SetSRID(ST_MakePoint(:tip_lng, :tip_lat), 4326)) AS terrain_speed_kmh
FROM terrain_raster
WHERE ST_Intersects(rast, ST_SetSRID(ST_MakePoint(:tip_lng, :tip_lat), 4326));
```

This dynamic terrain speed value replaces static distance assumptions, penalizing tips reported in physically unreachable locations given the elapsed time $\Delta t$.
