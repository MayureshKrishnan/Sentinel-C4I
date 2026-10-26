# SIH 2026 Strategy Guide: "Hidden Gem" Problem Statements (Low Competition, High Winning Probability)

In the Smart India Hackathon (SIH), popular themes like **Generic Web Apps, Chatbots, E-commerce, Basic Agriculture, and Simple Road Safety** receive **400 to 500+ submissions per PS**, leading to brutal evaluation filters.

A **"Hidden Gem"** problem statement is one that:
1. **Deters Generic Submissions**: Requires specialized domain knowledge (GPU CUDA programming, signal processing, RF/Lidar, specialized GIS rasters, or custom C++/Rust system code) that 95% of standard college teams cannot build.
2. **Has Low Competition**: Typically receives **fewer than 15–25 total submissions nationally**.
3. **High Judge Value**: Evaluation panels (DRDO, NTRO, ISRO, MRPL, MoES) are composed of domain scientists who eagerly award top marks to teams demonstrating genuine low-level technical execution.

---

## 💎 The 6 Top "Hidden Gem" Problem Statements

Here are the 6 best high-impact, low-competition problem statements from the official list:

---

### 1. ⚙️ SIH26119 — Mangalore Refinery & Petrochemicals Ltd (MRPL)
* **Category**: Software | **PS Number**: SIH26119
* **Title**: *Indigenous GPU-Accelerated Optimization Solver (Sovereign Alternative to Express / CPLEX)*
* **Why it's a Hidden Gem**:
  - Most hackathon teams write basic Python web wrappers. This PS asks you to write a **CUDA / C++ parallel matrix solver** for Linear Programming (LP) problems.
  - 98% of teams will skip this because it sounds like heavy computer science math.
* **Winning Edge**: If your team builds even a basic working C++/CUDA simplex solver benchmarked against SciPy/PuLP, you will almost certainly reach the top 3 nationally due to near-zero competition.

---

### 2. 🛰️ SIH26142 — National Technical Research Organisation (NTRO)
* **Category**: Software | **PS Number**: SIH26142
* **Title**: *Deep Learning Based Super Resolution Mapping (SRM) from Medium Resolution Satellite Imageries*
* **Why it's a Hidden Gem**:
  - Generic AI teams will submit basic image upscaling (like Bicubic or ESRGAN). NTRO judges specifically want **Sub-Pixel Land Cover Super Resolution Mapping (SRM)** for multi-spectral GIS bands.
  - Requires understanding sub-pixel fractional land cover fractions, which deters casual ML submissions.
* **Winning Edge**: Combining a PyTorch Super-Resolution model with GIS `rasterio`/`GDAL` geospatial coordinate preservation guarantees a high score from NTRO scientists.

---

### 3. 🔊 SIH26052 — DRDO
* **Category**: Hardware | **PS Number**: SIH26052
* **Title**: *To Develop an AI/ML-Enabled Adaptive Noise Cancellation (ANC) System that Effectively Suppresses Stationary, Non-Stationary, and Impulsive Noise on Embedded Hardware*
* **Why it's a Hidden Gem**:
  - Suppressing simple white noise is easy, but suppressing **impulsive noise (gunfire, rotor bursts)** on sub-millisecond embedded hardware requires true Digital Signal Processing (DSP).
  - Web/Mobile app developers cannot attempt this.
* **Winning Edge**: Implementing an LMS (Least Mean Squares) or Lightweight TinyML noise filter on an STM32 or ESP32 micro-controller board will instantly impress DRDO judges.

---

### 4. 🌊 SIH26058 — Ministry of Earth Sciences (MoES)
* **Category**: Hardware | **PS Number**: SIH26058
* **Title**: *Development of a Low-Power, Real-Time Adaptive Software-Defined Sonar Transmitter Payload for Autonomous Underwater Vehicles (AUVs)*
* **Why it's a Hidden Gem**:
  - Focuses on **underwater acoustic communication and software-defined radio (SDR)**.
  - Extremely niche—less than 10-15 teams in India attempt underwater acoustics hardware.
* **Winning Edge**: Demonstrating a functional acoustic transducer driver circuit with adaptive signal modulation on an Arduino/ESP32 payload guarantees a top spot.

---

### 5. 📡 SIH26055 — DRDO
* **Category**: Software | **PS Number**: SIH26055
* **Title**: *Smart Scan Strategy for Electronic Warfare*
* **Why it's a Hidden Gem**:
  - Involves radio frequency (RF) spectrum monitoring and dynamic frequency hopping interception.
  - Requires understanding spectral density and RF signal processing math.
* **Winning Edge**: Simulating RF spectrum sweep strategies using Python `scipy.signal` / GNU Radio and visualizing frequency occupancy heatmaps.

---

### 6. 🕵️ SIH26148 — NTRO
* **Category**: Software | **PS Number**: SIH26148
* **Title**: *Creation of Scripts/Functions with New Programming Language to Commence Computer & Network Forensic Analysis without Triggering Security Solutions*
* **Why it's a Hidden Gem**:
  - Asks teams to write forensic memory/disk extraction tools in modern systems languages like **Rust, Zig, or Nim** to bypass EDR antivirus heuristics.
  - Most college teams only know Python/JS; system programming in Rust/Zig filters out 90%+ of competitors.
* **Winning Edge**: A clean Rust CLI tool that parses RAM artifacts or raw NTFS master file tables without triggering Windows Defender.

---

## 📊 Summary Comparison: Popular vs Hidden Gem PS

| Feature | Popular PS (e.g. Chatbots, Farm Apps) | 💎 Hidden Gem PS (e.g. GPU Solver, DRDO ANC, NTRO SRM) |
| :--- | :--- | :--- |
| **National Submission Count** | 🔴 300 to 500+ submissions | 🟢 **Fewer than 10 – 25 submissions** |
| **Evaluation Criteria** | 🔴 UI design, superficial features | 🟢 Core algorithm performance & domain math |
| **Shortlisting Rate** | 🔴 < 1% chance of making final round | 🟢 **20% to 50% chance of making final round** |
| **Judge Panel Type** | Generalist Evaluators | Specialized Scientists (DRDO, ISRO, NTRO, MoES) |
