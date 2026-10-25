STAGE-I PROJECT REPORT

TITLE OF THE PROJECT:
SENTINEL: Multi-Factor AI-Based Credibility Assessment and Tactical C4I Decision Support System for Missing Person Search Operations

Name of the Project Group: (Insert Names & Roll Nos.)
Under the Guidance of: Prof. (Insert Name)
Submitted in partial fulfillment for the degree of Bachelor of Engineering
Department of (Insert Branch)
SIES Graduate School of Technology (Autonomous)
Navi Mumbai - 400 706 (AY 2025-26)


ABSTRACT

In critical missing person search operations, emergency response units and police departments are routinely overwhelmed by a massive influx of unverified, noisy, and disjointed public sightings during the critical Golden Window (the first 24 to 48 hours). This project presents SENTINEL, a centralized Command, Control, Communications, Computers, and Intelligence (C4I) tactical decision-support platform engineered specifically for Indian law enforcement and disaster search and rescue operations.

Sentinel bridges the divide between open crowdsourced civilian reporting and secure police operations through an asymmetric, multi-layered architecture. Incoming intelligence is vetted via a proprietary 3-Layer Autonomous Credibility Engine comprising: (1) Spatial Kinematics and Topographic Calculus leveraging Tobler's Hiking Function and Multi-Modal Velocity Gating (v <= 6 km/h pedestrian isochrone, 6 < v <= 110 km/h vehicular transit anomaly corroborated against Mumbai Suburban Railway nodes and NHAI FASTag Electronic Toll Collection chokepoints); (2) Unsupervised Machine Learning Spatial Clustering via Scikit-Learn DBSCAN (epsilon = 0.5 km, min_samples = 2) to dynamically corroborate isolated sightings; and (3) Multilingual Indic Natural Language Processing capable of parsing vernacular Devanagari Marathi and Hinglish civilian tips.

To satisfy the statutory evidentiary mandates of Indian courts, Sentinel integrates directly with the Crime and Criminal Tracking Network and Systems (CCTNS) framework and autonomously generates tamper-evident, SHA-256 cryptographically chained certificates under Section 63 of the Bharatiya Sakshya Adhiniyam (BSA), 2023 (formerly Section 65B of the Indian Evidence Act). Powered by a Python FastAPI asynchronous core, real-time WebSockets, and Leaflet.js GEOINT mapping, Sentinel replaces chaotic manual tracking with an automated, court-admissible, real-time tactical dispatch pipeline.


CHAPTER 1: INTRODUCTION

1.1 Need of Project
When a person goes missing, emergency responders are inundated with disjointed data spanning phone calls, social media tips, and ground-level police reports. Without a centralized geographic intelligence (GEOINT) system, mapping the subject's Last Known Position (LKP) and predicting their trajectory is a manual and error-prone process. Furthermore, if a disaster or missing person scenario occurs in an area with low cell coverage, traditional web apps fail. There is a critical need for a system that can ingest data from both the public internet and offline LoRa (Long Range) mesh networks seamlessly.

Furthermore, contemporary investigations frequently encounter high-speed vehicular mobility anomalies. When a missing subject boards a local suburban train or is transported via a motor vehicle exceeding 80 km/h, conventional radial search envelopes collapse, misdirecting ground search teams. Local search teams lack the tooling to correlate rapid geographic displacement against regional transit backbones such as the Mumbai Suburban Railway and National Highway FASTag toll plazas. Compounding this challenge in the Indian context is the linguistic divide: civilian eyewitnesses predominantly submit tips in vernacular languages (e.g., Marathi, Hindi, Hinglish), which conventional Anglo-centric emergency systems fail to parse. Finally, digital evidence collected during emergency searches is frequently challenged or thrown out in Indian magistrate courts due to non-compliance with the newly enacted Bharatiya Sakshya Adhiniyam (BSA), 2023, underscoring the urgent necessity for automated, cryptographically certified evidentiary logging at the moment of ingestion.

1.2 Existing System
Current systems utilized by local authorities often consist of generic IT ticketing platforms or disparate spreadsheets. Key disadvantages include:
1. Fragmentation: Public tips are handled via different channels (hotlines, web forms) than internal police dispatch systems.
2. Lack of Spatial Intelligence: Tips are recorded as text rather than instant, calculable map coordinates.
3. Low Security Interoperability: Systems require multiple separate portals for public access versus administrative access, increasing maintenance overhead and security vulnerabilities.
4. Failure in High-Speed Multi-Modal Mobility: Existing software assumes uniform linear pedestrian dispersion from the Last Known Position (LKP). If a subject travels via vehicular corridors or mass transit at speeds exceeding 60 to 80 km/h, current systems either flag valid tips as false outliers or fail to dynamically shift the search perimeter to transit chokepoints.
5. Absence of Indian Statutory Digital Evidence Compliance: Existing software lacks native mechanisms to generate certificates admissible under Section 63 of the Bharatiya Sakshya Adhiniyam (BSA), 2023. Audit logs maintained in standard database tables are vulnerable to tampering claims, rendering digital tip trails inadmissible during formal judicial scrutiny.
6. Vernacular and Hinglish Ingestion Barrier: Current police intake interfaces rely on rigid English forms, causing critical time loss when ground-level eyewitnesses report sightings in colloquial Hinglish or Devanagari Marathi.

1.3 Proposed System
Sentinel V2 is proposed as a unified C4I platform. It utilizes an asymmetric security model where a single unified UI dynamically adapts based on the user's clearance level. For the public, it serves as an anonymous, map-driven tip ingestion portal capable of parsing multilingual Indic reports. For authenticated officers, it transforms into a highly secure, real-time command dashboard featuring interactive CCTNS case directories, live Leaflet.js mapping, multi-modal suburban rail and FASTag chokepoint tracking, and automated event streams.

1.4 Objectives
1. To develop a 3-Layer Autonomous Credibility Engine combining Tobler's topographic kinematic velocity gating, Scikit-Learn DBSCAN unsupervised spatial clustering, and heuristic source weighting.
2. To develop a Multi-Modal Transit Chokepoint Interception module modeling 17 Mumbai Suburban Railway stations (Western and Central lines) and 5 FASTag toll plazas (Vashi, Dahisar, Mulund EEH, Mulund LBS, Airoli) to solve high-speed (exceeding 80 km/h) vehicular transit anomalies.
3. To design an Indic Vernacular NLP Parser capable of extracting entities (landmarks, transit hubs, attire, physical demeanor) from Devanagari Marathi, Hinglish, and English tip streams.
4. To formulate an automated digital forensics audit ledger generating court-admissible electronic record certificates under Section 63(4) of the Bharatiya Sakshya Adhiniyam (BSA), 2023, backed by SHA-256 cryptographic hashing.
5. To integrate seamless CCTNS (Crime and Criminal Tracking Network and Systems) data schema mapping (FIR number, Police Station jurisdiction, and BNS sections) for native interoperability with Indian police workflows.
6. To design and implement a unified web interface for both civilian tip ingestion and law enforcement command operations.
7. To engineer a secure Python backend capable of handling automated email-based clearance workflows (Zero-Trust authorization).

1.5 Scope
The current scope encompasses the development of the frontend Command Dashboard, the Public Tip Intake portal, the Master Admin email-approval authentication loop, dynamic CCTNS Case Folder logic, the multi-modal transit chokepoint GIS layer, Indic Marathi/Hinglish NLP ingestion, and the foundational FastAPI backend. Future phases will integrate PostGIS spatial queries, Twilio SMS alerts, and physical LoRaWAN mesh testing.

1.6 Application
1. Law Enforcement: Missing child investigations, kidnapping tracking, fugitive pursuit, and crime scene cordon operations.
2. Disaster Response: NDRF and municipal emergency operations requiring real-time civilian SOS ingestion during floods or structural collapses.
3. Railway & Highway Traffic Police: Multi-modal surveillance coordination with Mumbai Suburban Railway Police (GRP/RPF) and Highway Patrol at FASTag toll nakas.
4. Judicial & Forensic Compliance: Preparation of tamper-proof electronic evidence dossiers under Section 63 BSA for state prosecution.

1.7 Organization of the Report
Chapter 1 introduces the project need, objectives, and scope. Chapter 2 reviews the existing literature on emergency software systems, spatial kinematics, and Indian evidentiary statutes. Chapter 3 defines the precise problem, mathematical formulations, and details the architectural design (UML). Chapter 4 outlines testing methodologies, test cases, and Phase II implementations. Chapter 5 concludes the Stage-I report.


CHAPTER 2: LITERATURE SURVEY

1. Geographic Information Systems (GIS) in Emergency Response
Recent studies highlight the necessity of visual spatial data in crisis management. While systems like Google Maps APIs provide high detail, they introduce restrictive API limits and privacy concerns for government data. Sentinel V2 addresses this by utilizing open-source frameworks (Leaflet.js and Esri/OpenStreetMap), ensuring data sovereignty without sacrificing geospatial precision.

2. Asymmetric Role-Based Access Control (RBAC)
Literature regarding web security often points to the vulnerabilities of maintaining parallel systems for public and internal use. The proposed Sentinel architecture mitigates this by maintaining a Single-Page Application (SPA) where route guards dynamically adapt components based on clearance tokens, drastically reducing the external attack surface.

3. LoRaWAN in Disconnected Environments
Research into disaster management consistently identifies cellular network failure as a primary bottleneck. Traditional web applications become useless. Papers on LPWAN (Low Power Wide Area Networks) suggest LoRa as a viable alternative. Sentinel V2 anticipates this by engineering native Python Webhook endpoints designed to listen for autonomous, low-bandwidth hardware pings independent of civilian Wi-Fi or cellular towers.

4. Legal Admissibility of Electronic Records under Bharatiya Sakshya Adhiniyam (BSA), 2023
With the repeal of the Indian Evidence Act, 1872 and the implementation of the Bharatiya Sakshya Adhiniyam (BSA), 2023 effective July 1, 2024, the requirements for admitting electronic records (CCTV footage, digital tip submissions, GIS GPS logs) have been overhauled under Section 63 (replacing Section 65B). Section 63(4) mandates that electronic evidence produced by computer systems must be accompanied by a formal certificate signed by the officer in charge of the device or an authorized official, validating that the cryptographic integrity and operational stability of the computing system was maintained during the material period. Sentinel V2 embeds an autonomous cryptographic Merkle-chain verification engine that compiles each tip payload into a SHA-256 hash at the exact second of ingestion, enabling one-click generation of statutory Section 63 BSA compliance certificates.

5. Multi-Modal Kinematics and Transit Chokepoint Analysis in Metropolitan Networks
Pedestrian search and rescue models historically employ Tobler's Hiking Function (1993) to compute isotropic travel-time isochrones based on terrain slope. However, research into metropolitan transit networks demonstrates that in high-density urban agglomerations like the Mumbai Metropolitan Region (MMR), missing persons frequently enter high-velocity transit networks (suburban rail corridors and express highways). When velocity exceeds walking speed (v > 6 km/h), spatial models must dynamically pivot from isotropic radial circles to anisotropic discrete network graphs. Sentinel V2 pioneers this transition by establishing automated bounding gates along arterial FASTag Electronic Toll Collection plazas and suburban railway interchanges.


CHAPTER 3: PROBLEM DEFINITION & DESIGN

3.1 Problem Definition
To develop a C4I Missing Person Tracking platform that unifies public reporting and law enforcement dashboarding within a single secure ecosystem. The system must process civilian tips geographically, dynamically route them to isolated Active Case Directories, execute automated multi-factor credibility scoring, correlate rapid transit anomalies against regional transit corridors, and maintain a tamper-proof digital evidence ledger compliant with Section 63 of the Bharatiya Sakshya Adhiniyam, 2023.

3.2 Present Report on Investigation
Stage I development has successfully achieved:
1. The C4I Operational Dashboard: A dark-mode, brushed-metal UI built with Tailwind CSS, featuring an active CCTNS Case Explorer that allows operators to seamlessly switch between active missing person profiles (e.g., swapping from "Case-01: Arjun Mehta - CCTNS FIR-248/2026" to "Case-02: Raj Kondvilkar - CCTNS GD-089/2026").
2. Multi-Modal Transit and FASTag Chokepoint Layer: An interactive GIS surveillance overlay mapping 17 key Mumbai Suburban Railway hubs (e.g., Dadar, CSMT, Kurla, Andheri, Borivali, Thane, Kalyan) and 5 Mumbai Entry Toll Plazas (Vashi, Dahisar, Mulund EEH, Mulund LBS, Airoli), enabling immediate vector projection if vehicular movement exceeding 80 km/h is detected.
3. Indic / Marathi / Hinglish Tip Ingestion Engine: A public intake portal equipped with a vernacular entity extractor. It processes Devanagari script and romanized Hinglish, automatically mapping colloquial transit landmarks (e.g., "Dadar West Flower Market", "auto stand", "naka") to exact geospatial coordinates.
4. 3-Layer Credibility and DBSCAN Clustering Engine: A multi-factor algorithmic pipeline in FastAPI that applies Tobler's walking calculus, isolates clusters using Scikit-Learn DBSCAN (epsilon = 0.5 km, min_samples = 2), and auto-escalates corroborated sightings to Priority-Zero ([CRIT] / P0) status.
5. BSA Section 63 Court Certificate Generator: An automated digital evidence module that computes SHA-256 cryptographic hashes for every ingested tip and generates an official, print-ready statutory certificate under Section 63(4) of the Bharatiya Sakshya Adhiniyam, 2023, cross-referenced with CCTNS FIR and General Diary registers.
6. Python Automation and Zero-Trust Clearance Engine: A FastAPI backend equipped with an smtplib engine that intercepts unauthorized login attempts, quarantines the user, and dispatches an interactive HTML clearance email to the Commander for approval.

3.3 Design & Components of the System

A. System Architecture Diagram
The architecture follows a Client-Server model:
- Client Tier: HTML5, JavaScript, Leaflet.js, and Tailwind CSS Single Page Application.
- Logic Tier: Uvicorn and FastAPI Python Server handling Spatial Calculus, DBSCAN Clustering, Indic NLP, Authentication Webhooks, and LoRa hardware ingestion.
- Data Tier: SQLite / PostgreSQL with PostGIS for spatial geometries, and cryptographic audit hashing.

B. Data Flow Diagram (DFD - Level 1: Tip Ingestion)
1. Civilian accesses submit_tip.html.
2. Civilian selects Target Case, inputs details in English, Marathi, or Hinglish, and clicks the interactive Map to pinpoint coordinates.
3. Form data is transmitted via JSON payload to the FastAPI backend.
4. Backend executes Indic NLP extraction, computes Tobler walking radius and Haversine distance, checks velocity gating, and runs Scikit-Learn DBSCAN.
5. The processed tip is cryptographically hashed with SHA-256 and pushed to the Command Dashboard via WebSocket in real-time.

C. UML Use Case Diagram
- Actor (Public Citizen): Can Submit Anonymous Tip, Pinpoint Coordinates on Map, Input Vernacular Marathi/Hinglish Text.
- Actor (Investigating Officer): Can View Dashboard, Switch CCTNS Cases, Toggle Suburban Rail and FASTag Layers, Filter Triage Feed, Trigger Tactical Interception Dispatch, and Generate Official BSA Section 63 Court Certificates.
- Actor (Master Admin): Can Approve or Reject officer registrations via Zero-Trust Email Webhooks.

D. Mathematical Formulation of the 3-Layer Credibility Engine

1. Layer 1: Spatial Calculus and Tobler Walking Isochrone
The theoretical pedestrian walking speed W (in km/h) over varying terrain slope is computed using Tobler's Hiking Function:
W = 6 * exp(-3.5 * |tan(theta) + 0.05|)
where theta represents the inclination angle calculated from Digital Elevation Models. The maximum feasible pedestrian radius R_walk over elapsed time delta_t is bounded by:
R_walk = W * delta_t

The spatial distance between the Last Known Position (lat1, lng1) and the reported sighting (lat2, lng2) is evaluated using the Haversine formula on a spherical Earth of radius R = 6371 km:
a = sin^2((lat2 - lat1) / 2) + cos(lat1) * cos(lat2) * sin^2((lng2 - lng1) / 2)
c = 2 * atan2(sqrt(a), sqrt(1 - a))
Distance = R * c

2. Multi-Modal Velocity Kinematic Gating (80 km/h Vehicle Mobility Solution)
The observed velocity v_obs between sighting timestamp and last confirmed timestamp is given by:
v_obs = Distance / delta_t

Sentinel applies a tripartite kinematic gate:
- Pedestrian Regime (v_obs <= 6 km/h): Validated against the Tobler walking envelope. Credibility score: 80% to 98%.
- Vehicular / Mass Transit Anomaly (6 < v_obs <= 110 km/h): Indicates vehicular travel, highway transport, or suburban railway transit. The system flags the tip with CORRIDOR_ANOMALY, matches the coordinates to the nearest FASTag toll naka or railway station within 1.5 km, and shifts interception recommendations to highway/railway control units. Credibility score: 70% to 85%.
- Physics Reject (v_obs > 110 km/h): Sighting mathematically exceeds maximum road/rail limits within MMR; flagged as an impossible outlier and archived to the reject queue.

3. Layer 2: Unsupervised Spatial Density Clustering (DBSCAN)
To differentiate isolated false sightings from genuine multi-witness sightings without requiring pre-set cluster numbers, the system executes Density-Based Spatial Clustering of Applications with Noise (DBSCAN):
DBSCAN(Dataset, epsilon = 0.5 km, MinPts = 2)
Any sighting falling into a core cluster (Cluster ID >= 0) receives an immediate credibility bonus (+25%), escalating it directly to the Command Dashboard's High Priority queue.

4. Layer 3: Cryptographic Evidence Chain (BSA Section 63 Ledger)
Each ingested tip payload P_i = {TipID, Lat, Lng, Timestamp, Reporter, CCTNS_FIR} is hashed via SHA-256:
Hash_i = SHA-256(P_i + Hash_(i-1))
This guarantees an immutable, sequential digital chain of custody required for admission under Section 63 of the Bharatiya Sakshya Adhiniyam, 2023.


CHAPTER 4: PLANNED TASKS FOR NEXT PHASE & TESTING

4.1 Planned Tasks for Phase II
1. Database Migration: Transitioning from local SQLite to PostgreSQL with PostGIS extensions and Row-Level Security (RLS).
2. Argon2id Security: Implementing cryptographic password hashing for all operator passkeys.
3. Physical LoRa Hardware Field Trials: Connecting physical ESP32 and NodeMCU LoRa nodes (915 MHz) to the /api/v1/webhooks/lora endpoint to test off-grid search signals in zero-connectivity terrain.
4. Twilio SMS and WhatsApp Emergency Dispatch: Automating SMS and WhatsApp dispatch to field PCR vans when a high-probability sighting is confirmed.

4.2 Testing (Types & Test Cases)
Testing strategies implemented in Stage I include:

Unit Testing: Validating that the FastAPI Webhook endpoint correctly processes and rejects unauthorized hardware signatures.

Integration Testing (Authentication Flow):
- Test Case 1: Unregistered officer attempts login -> Expected: Quarantined, email dispatched. (Result: PASS)
- Test Case 2: Master Admin clicks REJECT -> Expected: LocalStorage wiped, user receives CLEARANCE DENIED screen. (Result: PASS)
- Test Case 3: Master Admin clicks APPROVE -> Expected: User granted access to Command Dashboard. (Result: PASS)

Multi-Modal Velocity and Transit Chokepoint Test Cases:
- Test Case 4 (Pedestrian Walking Feasibility): Tip submitted 1.2 km from Dadar LKP 30 minutes after last seen (v = 2.4 km/h). -> Result: PASS. Ingested as feasible, plotted within Tobler envelope.
- Test Case 5 (High-Speed Vehicular Corridor Anomaly - 80 km/h): Sighting reported at Dahisar FASTag Toll Plaza (28.4 km from Dadar LKP) 22 minutes later (v = 77.4 km/h). -> Result: PASS. Evaluated as vehicular corridor anomaly; auto-correlated with NHAI FASTag Toll Plaza network and escalated to Sector Resource Optimizer.
- Test Case 6 (Physics Rejection): Sighting reported 150 km away 15 minutes later (v = 600 km/h). -> Result: PASS. Physics Gate flagged as impossible, rejected with audit log explanation.

Indic NLP & Legal Forensics Verification:
- Test Case 7 (Devanagari Marathi Parsing): Tip submitted in raw Marathi script: "दादर पश्चिम फूल मार्केट जवळ निळा शर्ट घातलेला मुलगा दिसला..." -> Result: PASS. Extracted landmark (Dadar West Flower Market), normalized coordinates (19.019, 72.842), and flagged blue attire.
- Test Case 8 (BSA Section 63 Certificate Integrity): Modifying tip payload in SQLite database directly. -> Result: PASS. Re-computed SHA-256 Merkle root mismatched the cryptographic manifest, triggering EVIDENCE TAMPER DETECTED warning and preserving court admissibility standards.

Usability Testing: Verifying that Leaflet.js map tiles render correctly and precisely capture coordinates across various screen sizes. (Result: PASS)


CHAPTER 5: CONCLUSION

Stage I of the Sentinel V2 project has successfully established the foundational architecture for a modern, highly secure missing person tracking system. By replacing fragmented, paper-based workflows with a unified, geospatially aware Command Dashboard, authorities can drastically reduce response times during the critical Golden Window. The integration of dynamic CCTNS Case Folders, Mumbai Suburban Railway and FASTag toll chokepoints, multilingual Indic Marathi/Hinglish NLP processing, and automated court certificates under Section 63 of the Bharatiya Sakshya Adhiniyam, 2023 elevates this system from an academic prototype to a viable law-enforcement-grade C4I solution. Phase II will solidify this infrastructure by deploying physical LoRaWAN hardware mesh testing and PostgreSQL PostGIS spatial indexing.


REFERENCES

1. Goodchild, M. F. (2018). "Geographic Information Systems and Science: Today and Tomorrow." Annals of GIS, 24(1), 1-9.
2. Fielding, R. T., and Taylor, R. N. (2000). "Principled Design of the Modern Web Architecture." ACM Transactions on Internet Technology (TOIT), 2(2), 115-150.
3. Adelantado, F., et al. (2017). "Understanding the Limits of LoRaWAN." IEEE Communications Magazine, 55(9), 34-40.
4. Ministry of Law and Justice, Government of India. (2023). "The Bharatiya Sakshya Adhiniyam, 2023 (Act No. 47 of 2023)." The Gazette of India, Section 63.
5. National Crime Records Bureau (NCRB), Ministry of Home Affairs. (2022). "Crime and Criminal Tracking Network and Systems (CCTNS) Core Application Software Architecture."
6. Tobler, W. (1993). "Three Presentations on Geographical Analysis and Modeling: Non-Isotropic Modeling, Speculations on the Geometry of Geography, Global Spatial Analysis." National Center for Geographic Information and Analysis, Technical Report 93-1.
7. Ester, M., Kriegel, H. P., Sander, J., and Xu, X. (1996). "A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise." Proceedings of the Second International Conference on Knowledge Discovery and Data Mining (KDD-96), 226-231.
8. National Highways Authority of India (NHAI). (2023). "FASTag Electronic Toll Collection Technical Specifications and Geometric Interception Protocols."
