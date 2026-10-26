# SENTINEL: Mathematical & AI Scoring Engine Specification

## 1. Master Credibility Scoring Formula

Every incoming lead is scored between $0$ and $100$ using the unified mathematical formulation:

$$S = \left( w_1 \cdot C_{\text{source}} + w_2 \cdot V_{\text{spatial}} + w_3 \cdot I_{\text{content}} \right) \times e^{-\lambda \cdot \Delta t}$$

### Factor Parameters & Weights

| Factor | Variable | Scale | Initial Weight | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Source Reliability** | $C_{\text{source}}$ | $0.0 - 1.0$ | $w_1 = 40$ | Trusted entity rating based on origin channel |
| **Spatial Proximity** | $V_{\text{spatial}}$ | $0.0 - 1.0$ | $w_2 = 35$ | Terrain-adjusted feasibility relative to LKP |
| **Content Richness** | $I_{\text{content}}$ | $0.0 - 1.0$ | $w_3 = 25$ | Specificity of description + Naive Bayes filter |
| **Temporal Decay** | $e^{-\lambda \cdot \Delta t}$ | $0.0 - 1.0$ | N/A | Exponential decay over elapsed time |

$$\sum w_i = w_1 + w_2 + w_3 = 40 + 35 + 25 = 100$$

---

## 2. Component Factor Calculations

### A. Source Reliability ($C_{\text{source}}$)
* **First Responder / Law Enforcement**: $C_{\text{source}} = 1.0$
* **Field Volunteer / IoT GPS Hardware Node**: $C_{\text{source}} = 0.8$
* **Verified Public Submission** (Mobile OTP verified): $C_{\text{source}} = 0.5$
* **Anonymous Public Web Lead**: $C_{\text{source}} = 0.2$

### B. Temporal Decay ($e^{-\lambda \cdot \Delta t}$)
* **Half-Life Period ($T_{1/2}$)**: Set to 6 hours ($360$ minutes).
* **Decay Constant ($\lambda$)**:
  $$\lambda = \frac{\ln(2)}{T_{1/2}} = \frac{0.693147}{6 \text{ hrs}} \approx 0.1155 \text{ hr}^{-1}$$
* **$\Delta t$**: Time difference (in hours) between tip observation timestamp and present incident time.

### C. Spatial Proximity & Terrain Mobility ($V_{\text{spatial}}$)
Rather than simple Haversine Euclidean distance, $V_{\text{spatial}}$ incorporates max reachable radius based on terrain speed bounds:

$$V_{\text{spatial}} = \max\left(0, 1 - \frac{D_{\text{haversine}}(LKP, Tip)}{R_{\text{max}}(\text{terrain}, \Delta t)}\right)$$

Where $R_{\text{max}}$ is calculated based on satellite terrain classification:
* **Road / Urban Paved Area**: $v_{\text{max}} = 5.0 \text{ km/h} \implies R_{\text{max}} = 5.0 \times \Delta t$
* **Forest / Dense Vegetation**: $v_{\text{max}} = 2.0 \text{ km/h} \implies R_{\text{max}} = 2.0 \times \Delta t$
* **Steep Slope (>30° SRTM DEM)**: Speed penalty coefficient $0.5\times$ applied.
* **Water Body**: Impassable barrier. If tip lies across an un-bridged water body from LKP, $V_{\text{spatial}} = 0.0$.

### D. Content Richness & Naive Bayes Filter ($I_{\text{content}}$)
* **Raw Content Score**:
  $$I_{\text{base}} = \text{Clothing Matches (+0.35)} + \text{Physical Features (+0.35)} + \text{Direction/Landmark (+0.30)}$$
* **Naive Bayes Noise Multiplier**:
  A trained Naive Bayes binary classifier analyzes the tip text:
  * **SIGHTING**: Keywords like *saw, spotted, walking, wearing, heading, blue jacket*. Multiplier = $1.0$.
  * **NOISE**: Keywords like *hope, pray, share, post, facebook, retweet, please find*. Multiplier = $0.1$.
  $$I_{\text{content}} = I_{\text{base}} \times M_{\text{NB}}$$

---

## 3. Active Learning Weight Adjustment (Human-in-the-Loop)

When search coordinators override a lead priority (e.g., upgrading a score 55 to CRITICAL or dismissing a score 80 lead):
1. The override is saved as a verified ground-truth training instance $(C_{\text{source}}, V_{\text{spatial}}, I_{\text{content}}, y_{\text{true}})$.
2. Periodically, a grid search or ridge regression updates weights $w_1, w_2, w_3$ to minimize mean squared error over local incident history:
$$\min_{w_1, w_2, w_3} \sum \left( y_{\text{true}} - \left(w_1 C_{\text{source}} + w_2 V_{\text{spatial}} + w_3 I_{\text{content}}\right) e^{-\lambda \Delta t} \right)^2 \quad \text{s.t. } \sum w_i = 100$$

---

## 4. PuLP Linear Programming Resource Optimizer

Given $N$ search zones with total credibility scores $S_z$ and required volunteer capacity $c_z$, and $M$ available field volunteer teams with team sizes $t_m$:

$$\max \sum_{z=1}^{N} \sum_{m=1}^{M} S_z \cdot x_{z,m}$$
$$\text{Subject to: } \sum_{m=1}^{M} x_{z,m} \le 1 \quad \forall z \in \{1 \dots N\}$$
$$\sum_{z=1}^{N} t_m \cdot x_{z,m} \le \text{Capacity}_m \quad \forall m \in \{1 \dots M\}$$
Where $x_{z,m} \in \{0, 1\}$ is a binary decision variable indicating assignment of Team $m$ to Zone $z$.
