# STAGE-I PROJECT REPORT
## Title of the Project: SENTINEL - Multi-factor AI-Based Credibility Assessment for Missing Person Search Operations
**Name of the Project Group:** (Insert Names & Roll Nos.)
**Under the Guidance of:** Prof. (Insert Name)
**Submitted in partial fulfillment for the degree of Bachelor of Engineering**
**Department of (Insert Branch)**
**SIES Graduate School of Technology (Autonomous)**
**Navi Mumbai - 400 706 (AY 2025-26)**

---

## ABSTRACT
In critical missing person search operations, emergency responders are often overwhelmed by a high volume of unverified public tips, leading to wasted resources and lost time during the critical first 24 hours. This project proposes **SENTINEL**, a centralized Command, Control, and Intelligence platform designed to ingest civilian tips and autonomously evaluate them using a Multi-Factor AI-Based Credibility Assessment algorithm. The system bridges the gap between public reporting and secure law enforcement operations through a unified single-page application (SPA). Leveraging a Python FastAPI backend, PostgreSQL with PostGIS for spatial heatmapping, and dynamic case isolation, the platform scores and filters incoming civilian data before it reaches the command dashboard. Stage I of this project successfully establishes the secure asymmetric architecture, the interactive geographic command dashboard, the public tip ingestion portal, and the foundational zero-trust Master Admin authentication workflow required to support the future AI credibility engine.

---

# CHAPTER 1: INTRODUCTION

### 1.1 Need of Project
When a person goes missing, emergency responders are inundated with disjointed data spanning phone calls, social media tips, and ground-level police reports. Without a centralized geographic intelligence (GEOINT) system, mapping the subject's Last Known Position (LKP) and predicting their trajectory is a manual and error-prone process. Furthermore, if a disaster or missing person scenario occurs in an area with low cell coverage, traditional web apps fail. There is a critical need for a system that can ingest data from both the public internet and offline LoRa (Long Range) mesh networks seamlessly.

### 1.2 Existing System
Current systems utilized by local authorities often consist of generic IT ticketing platforms or disparate spreadsheets. Key disadvantages include:
* **Fragmentation:** Public tips are handled via different channels (hotlines, web forms) than internal police dispatch systems.
* **Lack of Spatial Intelligence:** Tips are recorded as text rather than instant, calculable map coordinates.
* **Low Security Interoperability:** Systems require multiple separate portals for public access vs. administrative access, increasing maintenance overhead and security vulnerabilities.

### 1.3 Proposed System (Problem Definition Broad)
Sentinel V2 is proposed as a unified C4I platform. It utilizes an asymmetric security model where a single unified UI dynamically adapts based on the user's clearance level. For the public, it serves as an anonymous, map-driven tip ingestion portal. For authenticated officers, it transforms into a highly secure, real-time command dashboard featuring interactive case directories, live Leaflet.js mapping, and automated event streams.

### 1.4 Objectives
* To develop a Multi-Factor AI-Based Credibility Assessment model to autonomously score and filter incoming civilian tips.
* To design and implement a unified web interface for both civilian tip ingestion and law enforcement command operations.
* To engineer a secure Python backend capable of handling automated email-based clearance workflows (Zero-Trust authorization).
* To integrate open-source Geographic Information Systems (GIS) for real-time visual tracking and heatmapping of high-credibility sightings.

### 1.5 Scope
The current scope encompasses the development of the frontend Command Dashboard, the Public Tip Intake portal, the Master Admin email-approval authentication loop, dynamic Case Folder logic, and the foundational FastAPI backend. Future phases will integrate PostGIS spatial queries, Twilio SMS alerts, and physical LoRaWAN mesh testing.

### 1.6 Application
* **Law Enforcement:** Missing person searches and fugitive tracking.
* **Disaster Response:** NDRF/FEMA operations requiring real-time civilian SOS ingestion.
* **Private Security:** High-value asset tracking across localized geographical boundaries.

### 1.7 Organization of the Report
Chapter 1 introduces the project need and scope. Chapter 2 reviews the existing literature on emergency software systems. Chapter 3 defines the precise problem and details the architectural design (UML). Chapter 4 outlines planned testing and Phase II implementations. Chapter 5 concludes the Stage-I report.

---

# CHAPTER 2: LITERATURE SURVEY
*Note for students: You will need to cite actual IEEE/Springer papers here based on your college research. Below is a framework of what the survey should argue based on our system.*

**1. Geographic Information Systems (GIS) in Emergency Response**
Recent studies highlight the necessity of visual spatial data in crisis management. While systems like Google Maps APIs provide high detail, they introduce restrictive API limits and privacy concerns for government data. Sentinel V2 addresses this by utilizing open-source frameworks (Leaflet.js and Esri/OpenStreetMap), ensuring data sovereignty without sacrificing geospatial precision.

**2. Asymmetric Role-Based Access Control (RBAC)**
Literature regarding web security often points to the vulnerabilities of maintaining parallel systems for public and internal use. The proposed Sentinel architecture mitigates this by maintaining a Single-Page Application (SPA) where JavaScript route-guards dynamically strip or inject sensitive UI components based on cryptographic clearance tokens, reducing the attack surface.

**3. LoRaWAN in Disconnected Environments**
Research into disaster management consistently identifies cellular network failure as a primary bottleneck. Traditional web applications become useless. Papers on LPWAN (Low Power Wide Area Networks) suggest LoRa as a viable alternative. Sentinel V2 anticipates this by engineering native Python Webhook endpoints designed to listen for autonomous, low-bandwidth hardware pings independent of civilian Wi-Fi.

---

# CHAPTER 3: PROBLEM DEFINITION & DESIGN

### 3.1 Problem Definition (Precise)
To develop a C4I Missing Person Tracking platform that unifies public reporting and law enforcement dashboarding within a single secure ecosystem. The system must process civilian tips geographically, dynamically route them to isolated Active Case Directories, and protect the command interface behind a strict "Master Admin" human-in-the-loop email verification workflow.

### 3.2 Present Report on Investigation
Stage I development has successfully yielded:
1. **The Operational Dashboard:** A dark-mode, frosted-glass UI built with Tailwind CSS, featuring a dynamic Left-Sidebar "Case Explorer" that allows operators to seamlessly switch between active missing person profiles (e.g., swapping from "Case-01: Arjun Mehta" to "Case-02: Sarah Jenkins").
2. **Geospatial Intake Portal:** A public-facing form integrated with Esri Global Street Maps, allowing users to visually drop pins on a map to report sightings, generating precise Latitude/Longitude coordinates.
3. **Python Automation Engine:** A FastAPI backend equipped with an `smtplib` engine that intercepts unauthorized login attempts, quarantines the user, and dispatches an interactive HTML clearance email to the Commander for approval.

### 3.3 Design & Components of the System
*(Note: You will need to draw these in tools like Draw.io or StarUML for your final report. Below are the structural descriptions to include next to your diagrams).*

**A. System Architecture Diagram**
The architecture follows a Client-Server model. 
* **Client Tier:** HTML5/JS/Tailwind CSS Single Page Application.
* **Logic Tier:** Uvicorn/FastAPI Python Server handling Authentication Webhooks and LoRa hardware ingestion.
* **Data Tier:** PostgreSQL (planned for Phase II) for structured relational data and PostGIS for spatial geometries.

**B. Data Flow Diagram (DFD - Level 1: Tip Ingestion)**
1. Civilian accesses `submit_tip.html`.
2. Civilian selects Target Subject, inputs details, and clicks the interactive Map to generate coordinates.
3. Form data is transmitted via JSON payload to the FastAPI backend.
4. Backend verifies data integrity and pushes the update to the Command Dashboard via WebSocket (Phase II), automatically linking the tip to the corresponding Case Folder.

**C. UML Use Case Diagram**
* **Actor (Public):** Can Submit Tip, View Map.
* **Actor (Officer):** Can View Dashboard, Filter Cases, View Heatmaps.
* **Actor (Master Admin):** Can Approve/Reject new Officer registrations via Email Webhook.

---

# CHAPTER 4: PLANNED TASKS FOR NEXT PHASE & TESTING

### 4.1 Planned Tasks for Phase II
1. **Database Migration:** Transitioning from local JSON/Javascript arrays to a strict PostgreSQL database with Row-Level Security (RLS).
2. **Argon2id Security:** Implementing cryptographic hashing for all passkeys to ensure enterprise-grade database security.
3. **LoRa Hardware Integration:** Connecting physical ESP32/LoRa nodes to the `/api/v1/webhooks/lora` endpoint to test autonomous SOS signals from the field.
4. **Twilio SMS Alerts:** Automating SMS dispatches to field officers when a high-probability civilian tip is submitted to their assigned Case Folder.

### 4.2 Testing (Types & Test Cases)
Testing strategies implemented in Stage I and planned for Stage II include:

* **Unit Testing:** Validating that the FastAPI Webhook endpoint correctly processes and rejects unauthorized hardware signatures.
* **Integration Testing (Authentication Flow):** 
  * *Test Case 1:* Unregistered officer attempts login -> Expected: Quarantined, email dispatched.
  * *Test Case 2:* Master Admin clicks 'REJECT' -> Expected: LocalStorage wiped, user receives "CLEARANCE DENIED" screen.
  * *Test Case 3:* Master Admin clicks 'APPROVE' -> Expected: User granted access to Command Dashboard.
* **Usability Testing:** Verifying that the OpenStreetMap/Esri map tiles render correctly and precisely capture coordinates when clicked across various screen sizes.

---

# CHAPTER 5: CONCLUSION
Stage I of the Sentinel V2 project has successfully established the foundational architecture for a modern, highly secure missing person tracking system. By replacing fragmented, paper-based workflows with a unified, geospatially aware Command Dashboard, authorities can drastically reduce response times. The integration of dynamic Case Folders allows for scalable multi-operation management, while the Python FastAPI backend ensures that security remains uncompromised through strict email authorization loops. Phase II will solidify this infrastructure by binding it to a robust PostgreSQL spatial database and physical LoRa automation.

---

# REFERENCES
1. Goodchild, M. F. (2018). "Geographic Information Systems and Science: Today and Tomorrow." *Annals of GIS*, 24(1), 1-9.
2. Fielding, R. T., & Taylor, R. N. (2000). "Principled Design of the Modern Web Architecture." *ACM Transactions on Internet Technology (TOIT)*, 2(2), 115-150.
3. Adelantado, F., et al. (2017). "Understanding the Limits of LoRaWAN." *IEEE Communications Magazine*, 55(9), 34-40.
4. [Add any specific local police protocols or IT frameworks you are studying here]
