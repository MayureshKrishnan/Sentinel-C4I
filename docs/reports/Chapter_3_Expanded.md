# CHAPTER 3
# PROBLEM DEFINITION & DESIGN

### 3.1 Problem Definition (Precise)
To engineer and deploy a **Multi-factor AI-Based Credibility Assessment Platform** for missing person search operations that unifies public tip reporting and law enforcement tactical visualization. The system must autonomously score civilian geospatial intelligence using algorithmic AI filtering, securely route the verified data into isolated dynamic Case Directories, and protect the overarching Command Dashboard behind a strict, Zero-Trust, human-in-the-loop email authentication webhook.

### 3.2 Proposed System & Overcoming Current Drawbacks
The current ecosystem of emergency response software suffers from extreme data fragmentation, a lack of autonomous data validation, and restrictive manual data-entry bottlenecks. 

**How Sentinel overcomes these drawbacks:**
1. **Overcoming the Verification Bottleneck:** Instead of forcing officers to manually read and verify thousands of civilian tips, Sentinel proposes a mathematical AI Credibility Algorithm. This algorithm calculates the spatial distance of the tip from the subject's Last Known Position (LKP) against the time elapsed, automatically dropping tips that violate the laws of physical travel speed, thereby preventing information overload.
2. **Overcoming Data Fragmentation:** Sentinel utilizes an Asymmetric Single-Page Application (SPA) architecture. Instead of maintaining one software suite for the police and a separate website for the public, Sentinel uses a singular, unified platform. Civilians interact with the front-facing geographic intake portal, while the system dynamically morphs into a high-security tactical dashboard for authenticated officers.
3. **Overcoming Manual Data Entry:** Instead of relying on text-based hotline calls ("I saw him near the mall"), the proposed system integrates free, open-source Geographic Information Systems (Leaflet.js and Esri Maps). Civilians visually drop pins on their mobile devices, instantly injecting mathematically precise Latitude and Longitude coordinates into the police database.

### 3.3 Objectives of the Proposed System
* To develop a mathematical AI algorithm capable of evaluating the credibility of crowdsourced spatial data in real-time.
* To design a web-based, map-driven UI that allows civilians to easily submit precise geolocation coordinates.
* To construct a secure Python FastAPI backend capable of handling automated SMTP email workflows for Zero-Trust officer registration.
* To implement a JavaScript-driven Case Management Engine that securely isolates incoming tips into specific operational folders (e.g., [CASE-01], [CASE-02]).

### 3.4 Present Report on Investigation (Stage-I Accomplishments)
During the Stage-I investigation and development phase, the core structural and frontend architecture was successfully implemented:
1. **Geospatial Intake Portal Developed:** The `submit_tip.html` interface was engineered to include Esri World Street Map tiles, allowing for interactive pin-dropping and dynamic coordinate generation.
2. **Command Dashboard Engineered:** A dark-mode, frosted-glass tactical interface was built using Tailwind CSS. It features a Live Tip Feed, dynamic Subject Profiles, and a centralized tracking map.
3. **Dynamic Folder Logic Implemented:** Custom JavaScript was written to allow officers to click through "Active Case Directories", dynamically hot-swapping the dashboard data to match the selected missing person without reloading the page.
4. **Backend Webhooks Initialized:** A Python FastAPI server was deployed to handle initial `/register` and `/approve` HTTP requests, successfully utilizing the `smtplib` library to dispatch secure HTML emails for admin authorization.

---

### 3.5 Design & Components of the System

#### A. Data Flow Diagram (DFD - Level 1)
The Data Flow Diagram illustrates how information traverses through the Sentinel ecosystem.
1. **Process 1 (Intake):** The Civilian inputs visual tip details and interacts with the Leaflet Map to generate (Lat, Lng) coordinates.
2. **Process 2 (Transmission):** The frontend packages this data into a JSON payload and transmits it via an HTTP POST request to the Python Backend.
3. **Process 3 (Algorithmic Processing):** The Backend passes the data through the Multi-factor Credibility Assessment engine. If the score is > 50%, it proceeds. If < 50%, it is archived.
4. **Process 4 (Routing):** The verified tip is stored in the PostgreSQL database and routed to the specific Case Folder matching the Target Subject ID.
5. **Process 5 (Visualization):** The Command Dashboard queries the database and renders the new coordinate as a glowing red node on the officer's Esri basemap.

#### B. UML Use Case Diagram
The Use Case modeling defines the interactions between the system's three primary actors:
* **Actor 1: Civilian (Public User)**
  * *Use Cases:* Search Location on Map, Drop Geographic Pin, Submit Missing Person Tip, Solve CAPTCHA.
* **Actor 2: Law Enforcement Officer (Authenticated)**
  * *Use Cases:* Request Clearance, View Command Dashboard, Switch Active Case Folders, View Live Tip Feed, Monitor Geographic Heatmap.
* **Actor 3: Master Admin (Commander)**
  * *Use Cases:* Receive Registration Webhook Email, Approve New Officer Access, Reject/Purge Unauthorized Access, Create New Case Folders.

#### C. Entity-Relationship (E-R) Diagram
The backend relational database (planned for PostgreSQL/PostGIS integration) requires the following structural relationships:
* **Entity 1: `Officers`** (Attributes: `operative_id` (PK), `passkey_hash`, `clearance_status`, `role`).
* **Entity 2: `Case_Folders`** (Attributes: `case_id` (PK), `subject_name`, `age`, `medical_notes`, `last_known_position`).
* **Entity 3: `Civilian_Tips`** (Attributes: `tip_id` (PK), `case_id` (FK), `latitude`, `longitude`, `timestamp`, `credibility_score`).
* **Relationship:** One `Case_Folder` can have *Many* `Civilian_Tips` (1:N). One `Officer` can oversee *Many* `Case_Folders` (1:N).

---

### 3.6 Algorithm Implementation (Department Specific)
**The Multi-factor AI Credibility Assessment Algorithm (Pseudocode)**
The core logic of the platform relies on mathematically scoring tips before they reach the officers. The algorithm utilizes a Spatiotemporal (Space and Time) verification formula.

**Step 1: Calculate Temporal Radius constraint**
When a tip arrives, the algorithm calculates the exact time difference (ΔT) between the Last Known Position (LKP) timestamp and the new Tip timestamp.
*If the missing person was last seen 2 hours ago (ΔT = 2), and the average human walking speed is 5 km/h, the maximum possible distance the subject could have traveled is 10 kilometers.*

**Step 2: Calculate Spatial Distance (Haversine Formula)**
The algorithm extracts the Latitude/Longitude of the LKP, and the Latitude/Longitude of the new tip. It applies the Haversine formula to calculate the exact geographical distance (D) between the two points on the Earth's curvature.

**Step 3: Credibility Scoring Logic**
```text
FUNCTION CalculateCredibility(Tip_Lat, Tip_Lng, Tip_Time, Case_LKP_Lat, Case_LKP_Lng, Case_LKP_Time):
    Max_Speed = 5 km/h  // Average human walking speed
    Delta_Time = Tip_Time - Case_LKP_Time
    Max_Possible_Distance = Max_Speed * Delta_Time
    
    Actual_Distance = Haversine(Tip_Lat, Tip_Lng, Case_LKP_Lat, Case_LKP_Lng)
    
    IF Actual_Distance > Max_Possible_Distance:
        // Tip is physically impossible (Subject cannot travel 50km in 1 hour on foot)
        Score = 10% (Flag as False Positive / Spam)
    ELSE IF Actual_Distance <= Max_Possible_Distance:
        // Tip is within the mathematical probability radius
        Base_Score = 75%
        
        IF Reporter_Type == "Police Officer":
            Base_Score = Base_Score + 20%  // High Trust Weight
            
        Score = Base_Score
        
    RETURN Score
END FUNCTION
```
By deploying this algorithmic logic in Phase II, Sentinel will systematically eliminate physically impossible geographic tips, ensuring the command dashboard only displays highly credible intelligence.
