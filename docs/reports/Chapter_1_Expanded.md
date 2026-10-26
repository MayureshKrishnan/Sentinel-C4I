# CHAPTER 1
# INTRODUCTION

### 1.1 Need of Project
In the domain of public safety and emergency response, the disappearance of an individual triggers a highly time-sensitive operation where the first 24 to 48 hours—often referred to as the "golden window"—are absolutely critical for a successful recovery. During this period, emergency responders, local law enforcement agencies, and volunteer search parties are heavily reliant on intelligence gathered from the civilian population. However, this reliance introduces a massive logistical bottleneck. 

When a high-profile missing person case is initiated, authorities are typically inundated with a colossal volume of civilian tips generated through fragmented channels such as emergency hotline phone calls, unverified social media posts, direct messages, and unstructured web forms. The primary challenge is no longer the acquisition of data, but rather the validation and spatial processing of that data. Currently, human operators must manually read, interpret, verify, and geographically plot each tip. Due to the high probability of human error, panic, or malicious misinformation, statistics show that nearly 70% to 80% of reported civilian sightings are either inaccurate, highly delayed, or entirely false. This severe "information overload" paralyzes search operations, leading to wasted operational hours, the deployment of limited resources to incorrect geographic quadrants, and drastically increased response times. 

Therefore, there is an urgent and critical need for a centralized, intelligent platform that can autonomously ingest civilian reports and instantly evaluate their credibility without human intervention. By developing an automated system capable of filtering out false positives and isolating high-probability sightings through geospatial tracking, law enforcement can redirect their focus from data entry to active tactical deployment.

### 1.2 Existing System
The existing infrastructure utilized by most regional and local authorities to manage missing person cases is largely outdated, heavily siloed, and heavily dependent on manual administrative labor. The fundamental characteristics and drawbacks of the current operational systems include:

**1. Extreme Data Fragmentation:** 
Presently, civilian tips are collected across disparate mediums. A tip received via a telephone call is logged into a completely different software application than a tip submitted via an email or a police website. This fragmentation prevents investigators from seeing a unified, big-picture view of the data. 

**2. Lack of Native Spatial Intelligence (GIS):**
Current ticketing platforms and police databases are predominantly text-based. When a citizen reports a sighting "near the central train station," it is recorded as a raw text string rather than a calculable mathematical coordinate. This forces law enforcement analysts to manually convert text-based locations into map pins, which is incredibly slow and highly prone to geographic errors.

**3. Absence of Credibility Assessment:**
Existing systems treat all incoming data points equally. A highly detailed tip submitted by an off-duty police officer is given the exact same weight in the database as a vague, unverified rumor submitted anonymously on the internet. There is no algorithmic mechanism to prioritize tips based on their statistical likelihood of being accurate.

**4. Low Security Interoperability:**
Many current architectures rely on completely separate software ecosystems for public interaction versus internal police administration. Maintaining parallel systems drastically increases maintenance overhead, server costs, and potential security vulnerabilities, while slowing down the transfer of data from the public to the commanding officers.

### 1.3 Proposed System (Problem Definition Broad)
To completely resolve the bottlenecks identified in the existing infrastructure, this project proposes the development of **SENTINEL: A Multi-factor AI-Based Credibility Assessment for Missing Person Search Operations.** 

Sentinel is designed as a unified Command, Control, Communications, Computers, and Intelligence (C4I) platform. Instead of utilizing fragmented applications, the proposed system operates on an asymmetric, Single-Page Application (SPA) architecture. This means the exact same digital platform serves both the public and the police, but dynamically alters its interface and security permissions based on the user's cryptographic clearance level. 

For the civilian public, the system presents an anonymous, highly intuitive intake portal integrated with interactive geographic maps (Esri/OpenStreetMap), allowing users to drop a precise pin on their exact location to generate automatic Latitude/Longitude coordinates. For authenticated law enforcement officers, the platform transforms into a high-security tactical dashboard. The core innovation of the proposed system is its backend automation: as civilian tips are ingested, they are routed through a Multi-Factor AI-Based Credibility Assessment algorithm that evaluates the spatial distance from the Last Known Position (LKP), the time elapsed, and the reporter's reputation. Only highly credible, verified data points are passed through to the officer's dashboard, effectively eliminating information overload.

### 1.4 Objective
The primary objectives of the Sentinel platform are strictly defined as follows:
* **To design and implement a Multi-Factor AI-Based Credibility Assessment algorithm** capable of autonomously scoring and prioritizing incoming civilian tips (from 0 to 100) based on mathematical spatial proximity and temporal validity.
* **To engineer a unified, asymmetric web interface** that seamlessly handles both anonymous civilian tip ingestion and highly classified law enforcement command operations within a single application state.
* **To integrate open-source Geographic Information Systems (GIS)**, specifically Leaflet.js and Esri basemaps, to facilitate real-time visual tracking, heatmapping, and pinpointing of high-credibility sightings without relying on paid enterprise APIs.
* **To implement a Zero-Trust security architecture** utilizing Python FastAPI and automated SMTP webhooks to enforce a strict human-in-the-loop email verification workflow for administrative access.
* **To develop a dynamic case management system** utilizing isolated digital directories, ensuring that intelligence data from multiple concurrent missing person operations remains strictly segregated.

### 1.5 Scope
The current scope of Stage-I encompasses the complete architectural design and frontend implementation of the Sentinel platform. This includes the development of the geospatial Command Dashboard, the interactive Public Tip Intake portal, the Master Admin email-based authorization pipeline, and the dynamic JavaScript-driven Case Folder engine. The scope extends to the deployment of the Python FastAPI server to handle secure routing and SMTP generation. 

The scope for Stage-II will expand into backend data persistence and algorithmic processing. This will include migrating the local state to a PostgreSQL database equipped with PostGIS for complex spatial radius queries, the mathematical implementation of the AI credibility scoring logic, and the integration of physical LoRaWAN (Long Range Wide Area Network) hardware nodes to test offline distress signal ingestion via automated webhooks.

### 1.6 Application
The Sentinel platform is engineered for rapid deployment across multiple critical sectors:
* **Law Enforcement & Police Departments:** Assisting local and state police in rapidly crowd-sourcing and mapping verified intelligence during AMBER alerts or active fugitive manhunts.
* **Disaster Response & Federal Agencies:** Providing organizations like the National Disaster Response Force (NDRF) or FEMA with a tool to manage civilian SOS signals and survivor sightings during large-scale natural disasters where traditional comms are overwhelmed.
* **Private Security & Search and Rescue (SAR):** Enabling volunteer organizations and private security firms to coordinate localized grid searches using military-grade spatial intelligence.

### 1.7 Organization of the Report
The remainder of this project report is systematically organized as follows:
* **Chapter 2 (Literature Survey):** Explores and reviews previously published research papers, existing disaster management systems, and current methodologies regarding GIS integration and AI credibility filtering, highlighting the specific research gaps Sentinel aims to fill.
* **Chapter 3 (Problem Definition & Design):** Provides a highly precise problem statement and details the exact software engineering methodology, including comprehensive Data Flow Diagrams (DFD), System Architecture diagrams, and UML Use Case modeling.
* **Chapter 4 (Planned Tasks & Testing):** Outlines the specific unit testing, integration testing, and usability testing protocols executed during development, alongside a roadmap of remaining tasks for the Phase II AI implementation.
* **Chapter 5 (Conclusion):** Summarizes the accomplishments, technical milestones, and the overall impact of the Stage-I system development. 
* **References:** A chronological academic bibliography of all research material cited throughout the document.
