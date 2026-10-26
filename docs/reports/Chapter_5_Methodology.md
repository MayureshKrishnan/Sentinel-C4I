# CHAPTER 5
# METHODOLOGY

### 5.1 Overview of Project Methodology
The development of the Sentinel platform followed an Agile software engineering procedure, focusing on rapid iteration and the strict separation of concerns across a multi-tier client-server architecture. The methodology relies on integrating highly specialized, open-source tools to build a secure, geospatially aware application without incurring the prohibitive costs of proprietary enterprise systems.

### 5.2 Frontend Procedure & Tools
The user interface was constructed as an Asymmetric Single-Page Application (SPA) utilizing vanilla HTML5 and JavaScript. This approach was chosen to ensure maximum performance and minimal load times, which is critical for field operations in low-bandwidth areas where heavy frameworks (like React or Angular) might stall. 
* **Tailwind CSS:** Utilized via a lightweight CDN to rapidly style a responsive, dark-mode, frosted-glass tactical aesthetic. 
* **Leaflet.js & Esri Maps:** For the core geospatial components, Leaflet.js was integrated. Rather than relying on expensive Google Maps API keys (which are prone to restrictive rate-limiting), the methodology utilized free **Esri World Street Map** tiles. By applying advanced CSS matrix inversions, the system maintains a tactical dark-mode theme while providing granular, street-level map details to the public.

### 5.3 Backend Procedure & Tools
The logic tier was built to handle high-concurrency requests and robust security protocols.
* **Python FastAPI:** The backend was constructed using the Python FastAPI framework running on an asynchronous Uvicorn server. FastAPI was strictly selected over traditional frameworks like Django or Flask due to its extreme execution speed, native data validation (via Pydantic), and native support for asynchronous JSON webhooks. 
* **Zero-Trust SMTP Verification:** To enforce the Zero-Trust security protocol, the native Python **`smtplib`** library was utilized. This tool constructs an automated SMTP email loop, effectively bridging the gap between local frontend login forms and an external Master Admin's encrypted Gmail inbox, preventing brute-force database attacks.

### 5.4 Algorithmic Procedure
The core intelligence of the platform relies on a mathematically sound **Multi-factor AI Credibility Algorithm**. 
* **The Spatiotemporal Filter:** The procedure dictates that all ingested civilian tips are passed through a spatiotemporal filter using the **Haversine Formula**. By mathematically calculating the geographic distance between two sets of spherical coordinates (the Last Known Position and the Tip Location) and cross-referencing it with the exact time elapsed, the system systematically flags and purges physically impossible data points (e.g., a subject traveling 50 kilometers on foot in 30 minutes) as false positives.

### 5.5 Data Persistence Procedure (Phase II Tools)
The planned methodology for data storage involves migrating from temporary JavaScript state arrays to a highly structured relational database.
* **PostgreSQL & PostGIS:** The backend will be integrated with PostgreSQL. Crucially, the **PostGIS** extension will be utilized. This tool allows the backend to execute complex geographic radius queries directly on the SQL tables, vastly improving the speed of spatial sorting and case isolation.
* **Argon2id Hashing:** All operative passwords will be cryptographically hashed using Argon2id, the current industry-standard procedure for resisting GPU-based decryption attacks.
