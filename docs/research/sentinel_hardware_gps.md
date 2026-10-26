# SENTINEL: Hardware Field GPS Node Specification

## 1. Hardware Architecture & Bill of Materials (BOM)

The hardware module consists of two low-cost IoT nodes that auto-log coordinator and field volunteer coordinates into the pipeline as `source_type = volunteer` ($C_{\text{source}} = 0.8$).

| Component | SKU | Spec / Feature | Qty | Unit Price | Total Price | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **NEO-6M GPS Module** | 1270231 | u-blox NEO-6M, 5Hz, -162dBm, UART TTL, Ceramic Antenna | 2 | ₹267 | ₹534 | Robu.in |
| **NodeMCU ESP8266 V3** | 62160 | Wi-Fi 802.11 b/g/n, 4MB Flash, CH340 USB | 2 | ₹191 | ₹382 | Robocraze |
| **18650 Li-Ion Battery** | — | 3.7V, 2200mAh rechargeable cell | 1 | ₹137 | ₹137 | Robocraze |
| **1x18650 Cell Box + Wire**| R260099 | Single cell box with pre-soldered lead wires | 1 | ₹55 | ₹55 | Robu.in |
| **SS-12D00 Slide Switch** | 1883688 | 3-pin SPDT slide switch (Power ON/OFF) | 4 | ₹3 | ₹12 | Robu.in |
| **TOTAL HARDWARE COST** | — | — | — | — | **₹1,120** | — |

---

## 2. Unit Role Breakdown

### Unit A: Command Gateway Node
* **Power Source**: Powered directly via USB cable attached to coordinator laptop.
* **Role**: Placed at field base station / LKP. Pushes static base station location and acts as a gateway receiver.
* **Connectivity**: Connects to coordinator smartphone Wi-Fi hotspot.

### Unit B: Wireless Field Volunteer Node
* **Power Source**: 18650 3.7V Li-Ion Battery through SPDT slide switch into NodeMCU `VIN` pin.
* **Role**: Carried by field volunteer during active search grid sweeps.
* **Operation Time**: ~6 to 8 hours continuous broadcast on single charge.

---

## 3. Circuit Wiring & Schematic

```
[18650 Battery (+)] ---> [Slide Switch Pin 1 | Pin 2 Output] ---> NodeMCU VIN Pin
[18650 Battery (-)] --------------------------------------------> NodeMCU GND Pin

NEO-6M GPS Module Pinout:
VCC  ---> NodeMCU 3V3 Pin
GND  ---> NodeMCU GND Pin
TX   ---> NodeMCU Pin D1 (GPIO 5 - SoftwareSerial RX)
RX   ---> NodeMCU Pin D2 (GPIO 4 - SoftwareSerial TX)
```

---

## 4. NodeMCU ESP8266 Firmware (Arduino C++)

```cpp
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <SoftwareSerial.h>
#include <TinyGPS++.h>

const char* WIFI_SSID = "Coordinator_Hotspot";
const char* WIFI_PASS = "sentinel2026";
const char* API_URL   = "http://192.168.43.100:8000/api/v1/hardware_ping";

SoftwareSerial gpsSerial(5, 4); // RX = D1, TX = D2
TinyGPSPlus gps;
WiFiClient client;

unsigned long lastPing = 0;
const unsigned long INTERVAL = 60000; // 60 seconds

void setup() {
  Serial.begin(115200);
  gpsSerial.begin(9600);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void loop() {
  while (gpsSerial.available() > 0) {
    gps.encode(gpsSerial.read());
  }

  if (millis() - lastPing >= INTERVAL) {
    if (gps.location.isValid()) {
      lastPing = millis();
      HTTPClient http;
      http.begin(client, API_URL);
      http.addHeader("Content-Type", "application/json");

      String payload = "{\"node_id\":\"UNIT_B_FIELD\",\"latitude\":" + 
                       String(gps.location.lat(), 6) + ",\"longitude\":" + 
                       String(gps.location.lng(), 6) + ",\"battery\":85}";

      int httpCode = http.POST(payload);
      http.end();
    }
  }
}
```
