# SENTINEL - Comprehensive Dataset Inventory & Reference Guide

The **SENTINEL** platform utilizes three distinct categories of datasets: **IEEE GRSS Satellite Remote Sensing Datasets**, **NLP Text Classifier Training Datasets**, and the **Synthetic Tip Evaluation Dataset**.

---

## 🌍 Category 1: IEEE GRSS Satellite & GIS Terrain Datasets
Used to compute the terrain-adjusted mobility factor ($V_{\text{spatial}}$) by identifying land cover types, physical barriers, elevation, and terrain slope.

| Dataset Name | Provider / Source | Resolution / Format | Key Features / Information Provided | Access Link | Cost |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Sentinel-2 Multi-Spectral Imagery (MSI)** | ESA Copernicus | 10m spatial resolution, 5-day revisit | Band 2,3,4 (RGB) & Band 8 (NIR). Computes NDVI & NDWI to classify dense forest, open ground, roads, and water bodies. | [Copernicus Data Space](https://dataspace.copernicus.eu/) | Free (Open Access) |
| **SRTM DEM (Shuttle Radar Topography Mission)** | NASA / USGS | 30m spatial resolution (1 arc-sec) | Digital Elevation Model (DEM) data. Used to calculate terrain slope angles ($\theta > 30^\circ$) to apply movement speed penalties. | [USGS EarthExplorer](https://earthexplorer.usgs.gov/) | Free (Open Access) |
| **ISRO Bhuvan LULC (Land Use / Land Cover)** | ISRO NRSC | 1:50,000 scale / variable | High-precision Indian geography land cover classification. Differentiates urban structures, farmland, scrubland, and water bodies in India. | [ISRO Bhuvan Portal](https://bhuvan.nrsc.gov.in/) | Free (Registration required) |

---

## 💬 Category 2: NLP Naive Bayes Classifier Training Datasets
Used by Member 1 to train the `scikit-learn` Naive Bayes text classifier to separate actionable sighting leads from social media noise/spam.

| Dataset Name | Description / Composition | Purpose / Output Class | Keywords & Samples Included |
| :--- | :--- | :--- | :--- |
| **SENTINEL Tip Classification Corpus** | ~500 labeled text samples (synthetic & historical public tip feeds). | Binary Classifier: `SIGHTING` ($M_{\text{NB}} = 1.0$) vs `NOISE` ($M_{\text{NB}} = 0.1$). | **SIGHTING**: *saw, spotted, walking, wearing, blue jacket, heading north, near bus stop, timestamp*<br>**NOISE**: *hope they are found, pray, please share, post, retweet, Facebook link, news update* |

---

## 📍 Category 3: Synthetic Incident Tip Evaluation Dataset
Used by Member 3 to validate the system using **Precision@K** metrics, verifying that top-scored tips cluster around planted ground-truth coordinates.

| Dataset Name | Composition | Key Fields / Schema | Usage |
| :--- | :--- | :--- | :--- |
| **Navi Mumbai 250 Synthetic Tip Benchmark** | 250 tip entries with 15 planted ground-truth sightings near Last Known Position (LKP: Sector 12, Navi Mumbai). | `tip_id`, `latitude`, `longitude`, `observation_time`, `source_type`, `raw_text`, `ground_truth_flag` | Evaluates temporal decay (2h vs 8h tips), corroboration deduplication, and score accuracy. |

---

## 🛠️ How to Explore / Download These Datasets Right Now

1. **Sentinel-2 & SRTM DEM**:
   - Go to [USGS EarthExplorer](https://earthexplorer.usgs.gov/) or [Copernicus Data Space](https://dataspace.copernicus.eu/).
   - Search area: **Navi Mumbai, Maharashtra, India** (Coordinates: ~`18.9876° N, 73.0021° E`).
   - Download the Sentinel-2 L2A GeoTIFF and SRTM 1-Arc-Second DEM file.

2. **Synthetic Tip Benchmark Dataset**:
   - Member 3 can generate or open the 250-row CSV file containing sample tip submissions for local testing.
