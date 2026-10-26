# SENTINEL - Satellite Dataset Comparison Matrix

## Comprehensive Comparison Table

| Evaluation Aspect | **ISRO Bhuvan LULC** (Historical Baseline) | **SRTM DEM** (Elevation Data) | **ESA WorldCover 10m** (Static Modern) | **Sentinel-2 L2A** (Live 5-Day) | **NASA Worldview** (Daily Live) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Data Currency / Age** | 🔴 Dated (2015–16) | ⚪ Static (2000 Baseline) | 🟢 Recent (2023) | 🚀 **Live (Updated every 5 days)** | 🚀 **Live (Updated daily / 24h)** |
| **Spatial Resolution** | 🟡 1:50,000 (~30m) | 🟡 30 meters | 🟢 **10 meters** | 🟢 **10 meters** | 🟡 15–30 meters |
| **Cost** | 🟢 Free (Registration) | 🟢 Free (USGS) | 🟢 Free (ESA) | 🟢 **Free (Open Access)** | 🟢 **Free (NASA)** |
| **Primary Feature Extracted** | Indian Land Use categories | Elevation, slope angle ($\theta > 30^\circ$) | Modern urban, road & forest boundaries | Live NDVI (vegetation) & NDWI (water) | Near-real-time global optical view |
| **Urban Expansion Accuracy** | 🔴 Low (Misses 2016–2026 growth) | N/A (Terrain elevation only) | 🟢 High (Captures up to 2023) | 🟢 **Highest (Captures current week)** | 🟡 Medium (Lower resolution) |
| **Processing Effort** | 🟢 Low (Pre-classified) | 🟢 Low (Geotiff) | 🟢 Low (Pre-classified) | 🟡 Medium (Requires NDVI computation) | 🟢 Low (Visual inspection) |
| **Role in SENTINEL** | Regional Indian baseline | Slope speed penalty ($\theta > 30^\circ$) | Multi-year terrain land cover | **Primary live terrain cost raster** | Visual verification layer |

---

## Key Takeaways: Why Sentinel-2 L2A (Live 5-Day) & ESA WorldCover 10m Win

1. **Resolution Advantage**: Both **Sentinel-2** and **ESA WorldCover** offer **10-meter spatial resolution**, allowing the system to distinguish narrow paved roads from surrounding dense forest patches.
2. **Currency Advantage**: **Sentinel-2 L2A** updates **every 5 days**, reflecting current seasonal water levels (e.g., monsoon floods vs dry creek beds) and recent urban development that **ISRO Bhuvan 2015–16** misses completely.
3. **Slope Precision**: **SRTM DEM** remains essential because elevation/slope does not change over time, and it provides the exact slope angle needed to apply speed penalties ($\theta > 30^\circ$).
