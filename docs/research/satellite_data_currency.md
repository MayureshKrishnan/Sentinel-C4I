# SENTINEL - Satellite Data Currency & Alternatives Analysis

## 1. Why ISRO Bhuvan LULC (2015–16) is Still Useful & Its Limitations

You correctly noted that **ISRO Bhuvan's 1:50,000 LULC map** published on the public portal is based on the 2015–16 cycle.

### Key Analysis for Panel Q&A:
* **Why it's valid for major terrain features**: Static geographical baselines (hills, rivers, forests, major highways, lakes, and administrative boundaries) **do not change** significantly over 8–10 years.
* **Where it falls short**: Rapid urban expansion, newly built roads, and deforestation in cities like Navi Mumbai post-2016 will not reflect on the 2015–16 static map.

---

## 2. Modern Open Alternatives for Up-to-Date 10m Resolution (2021–2024)

To ensure SENTINEL has current data, we integrate two modern, freely accessible 10m resolution satellite land cover layers:

| Dataset / Source | Resolution | Time Horizon / Currency | Provider | Access Link | Why It's Superior |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ESA WorldCover 10m** | **10 meters** | **2021 / 2023** | ESA Copernicus | [ESA WorldCover Viewer](https://worldcover2021.esa.int/) | Uses Sentinel-1 + Sentinel-2 to classify 11 land cover classes globally at 10m resolution up to 2023. |
| **Esri 10m Land Cover** | **10 meters** | **2050 (Updated Annual 2017–2023)** | Impact Observatory / Esri | [Esri Land Cover Portal](https://livingatlas.arcgis.com/landcover/) | Derived from Sentinel-2 10-meter imagery using deep learning AI models. Updated annually! |
| **Real-time Sentinel-2 NDVI/NDWI** | **10 meters** | **Live (5-day revisit)** | ESA Copernicus | [Copernicus Browser](https://browser.dataspace.copernicus.eu/) | Real-time vegetation density and water body detection computed directly from latest satellite pass. |

---

## 3. Recommended Hybrid Strategy for SENTINEL

For maximum accuracy and to satisfy the project panel, SENTINEL uses a **Hybrid GIS Strategy**:

```
                              +---------------------------------------+
                              |      HYBRID TERRAIN COST RASTER       |
                              +---------------------------------------+
                                                  |
                  +-------------------------------+-------------------------------+
                  |                                                               |
                  ▼                                                               ▼
   [ISRO Bhuvan LULC (2015-16)]                                   [ESA WorldCover 10m / Sentinel-2 L2A]
- Provides Indian administrative context                        - Provides 2023/2024 active land cover
- Major water body & forest boundaries                         - 10m resolution urban expansion & roads
- High-level zone baseline                                      - Live NDVI vegetation & NDWI water mask
```

---

## 4. How to View ESA WorldCover 10m (2021/2023) Right Now

1. Click: 🔗 **[ESA WorldCover Viewer](https://worldcover2021.esa.int/)**
2. In the top search bar, type: **Navi Mumbai** or **Mumbai**.
3. You will see an ultra-high resolution **10-meter land cover map** with modern 2021–2023 data:
   - 🟩 **Dark Green**: Tree cover / Forest
   - 🟥 **Red**: Built-up / Urban (Updated roads and buildings)
   - 🟦 **Blue**: Water bodies
   - 🟨 **Yellow**: Cropland
