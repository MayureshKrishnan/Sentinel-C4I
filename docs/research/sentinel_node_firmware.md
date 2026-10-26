#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <SoftwareSerial.h>
#include <TinyGPS++.h>

// Wi-Fi Credentials (Connect to Mobile Hotspot or Local Router)
const char* WIFI_SSID = "SENTINEL_HOTSPOT";
const char* WIFI_PASS = "sentinel2026";

// FastAPI Endpoint URL (Update IP to Member 1's local laptop IP)
const char* API_URL   = "http://192.168.1.50:8000/api/v1/hardware_ping";

// Hardware Node Identification
const char* NODE_ID   = "UNIT_B_FIELD";

// Pin Configuration (RX = GPIO 5 / D1, TX = GPIO 4 / D2)
SoftwareSerial gpsSerial(5, 4);
TinyGPSPlus gps;
WiFiClient client;

unsigned long lastPing = 0;
const unsigned long PING_INTERVAL = 60000; // Broadcast every 60 seconds

void setup() {
  Serial.begin(115200);
  gpsSerial.begin(9600);

  Serial.println("\n[SENTINEL IoT Node] Initializing...");
  WiFi.begin(WIFI_SSID, WIFI_PASS);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\n[SENTINEL IoT Node] Connected to Wi-Fi!");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  while (gpsSerial.available() > 0) {
    gps.encode(gpsSerial.read());
  }

  if (millis() - lastPing >= PING_INTERVAL) {
    if (gps.location.isValid()) {
      lastPing = millis();
      HTTPClient http;
      http.begin(client, API_URL);
      http.addHeader("Content-Type", "application/json");

      String payload = "{\"node_id\":\"" + String(NODE_ID) + 
                       "\",\"latitude\":" + String(gps.location.lat(), 6) + 
                       ",\"longitude\":" + String(gps.location.lng(), 6) + 
                       ",\"battery\":90}";

      Serial.print("[SENTINEL] Sending GPS Ping: ");
      Serial.println(payload);

      int httpCode = http.POST(payload);
      Serial.print("[SENTINEL] HTTP Response Code: ");
      Serial.println(httpCode);

      http.end();
    } else {
      Serial.println("[SENTINEL] Waiting for GPS lock...");
    }
  }
}
