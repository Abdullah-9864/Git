## ESP Code

// ESP32 Calculator - Receives numbers from PC, tracks sum & product
// Upload this to your ESP32

float numbers[100];   // Store up to 100 entered numbers
int count = 0;
String inputBuffer = "";

void setup() {
  Serial.begin(115200);
  Serial.println("ESP32 READY");
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();

    if (c == '\n') {
      inputBuffer.trim();

      if (inputBuffer == "CLEAR") {
        // Reset everything
        count = 0;
        Serial.println("CLEARED");

      } else if (inputBuffer.length() > 0) {
        float num = inputBuffer.toFloat();

        if (count < 100) {
          numbers[count] = num;
          count++;

          // Calculate sum
          float sum = 0;
          for (int i = 0; i < count; i++) {
            sum += numbers[i];
          }

          // Calculate product
          float product = 1;
          for (int i = 0; i < count; i++) {
            product *= numbers[i];
          }

          // Calculate average
          float avg = sum / count;

          // Send results back to PC
          Serial.print("COUNT:");
          Serial.print(count);
          Serial.print("|SUM:");
          Serial.print(sum, 2);
          Serial.print("|PRODUCT:");
          Serial.print(product, 2);
          Serial.print("|AVG:");
          Serial.println(avg, 2);
        } else {
          Serial.println("ERROR:Memory full (100 numbers max)");
        }
      }

      inputBuffer = "";
    } else {
      inputBuffer += c;
    }
  }
}



## VScode terminal

pip install pyserial
python keypad_app.py





## wifi setup

192.168.100.64

https://script.google.com/macros/s/AKfycbxUR0W_91pa4UaxMSXpvbLqMT4BR33K--JALOonZcA71btgRqJf7W0BrZrXAiQCyfIG/exec

AKfycbxUR0W_91pa4UaxMSXpvbLqMT4BR33K--JALOonZcA71btgRqJf7W0BrZrXAiQCyfIG





In telecommunications and electronics, Baud is named after Émile Baudot, the inventor of the Baudot code for telegraphy.


// ─── ESP32 WiFi Calculator ───────────────────────────────────────────────────
// Connects to WiFi, receives numbers from browser, returns calculations
// Upload this to your ESP32

#include <WiFi.h>
#include <WebServer.h>
#include <ArduinoJson.h>

// ─── YOUR WIFI ───────────────────────────────────────────────────────────────
const char* WIFI_SSID     = "CS-Lab2FF";
const char* WIFI_PASSWORD = "Admin123@";

// ─── SERVER ──────────────────────────────────────────────────────────────────
WebServer server(80);

// ─── DATA STORAGE ────────────────────────────────────────────────────────────
float numbers[100];
int   count   = 0;
float sum     = 0;
float product = 1;

// ─── CORS HELPER ─────────────────────────────────────────────────────────────
void addCORS() {
  server.sendHeader("Access-Control-Allow-Origin",  "*");
  server.sendHeader("Access-Control-Allow-Methods", "POST,GET,OPTIONS");
  server.sendHeader("Access-Control-Allow-Headers", "Content-Type");
}

// ─── ROUTE: OPTIONS (preflight) ──────────────────────────────────────────────
void handleOptions() {
  addCORS();
  server.send(204);
}

// ─── ROUTE: POST /add ────────────────────────────────────────────────────────
void handleAdd() {
  addCORS();

  if (!server.hasArg("plain")) {
    server.send(400, "application/json", "{\"error\":\"No body\"}");
    return;
  }

  StaticJsonDocument<128> req;
  DeserializationError err = deserializeJson(req, server.arg("plain"));
  if (err) {
    server.send(400, "application/json", "{\"error\":\"Bad JSON\"}");
    return;
  }

  float num = req["number"].as<float>();

  if (count >= 100) {
    server.send(400, "application/json", "{\"error\":\"Memory full (100 max)\"}");
    return;
  }

  numbers[count++] = num;
  sum     += num;
  product *= num;
  float avg = sum / count;

  StaticJsonDocument<256> res;
  res["count"]   = count;
  res["number"]  = num;
  res["sum"]     = sum;
  res["product"] = product;
  res["avg"]     = avg;

  String out;
  serializeJson(res, out);
  server.send(200, "application/json", out);

  Serial.printf("Added: %.2f | Count: %d | Sum: %.2f | Avg: %.2f\n",
                num, count, sum, avg);
}

// ─── ROUTE: POST /clear ──────────────────────────────────────────────────────
void handleClear() {
  addCORS();
  count   = 0;
  sum     = 0;
  product = 1;
  server.send(200, "application/json", "{\"status\":\"cleared\"}");
  Serial.println("Data cleared!");
}

// ─── ROUTE: GET /status ──────────────────────────────────────────────────────
void handleStatus() {
  addCORS();
  StaticJsonDocument<128> res;
  res["status"]  = "online";
  res["count"]   = count;
  res["sum"]     = sum;
  res["product"] = product;
  res["avg"]     = count > 0 ? sum / count : 0;
  String out;
  serializeJson(res, out);
  server.send(200, "application/json", out);
}

// ─── SETUP ───────────────────────────────────────────────────────────────────
void setup() {
  Serial.begin(115200);
  Serial.println("\n\nESP32 Starting...");

  // Connect to WiFi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\n✅ WiFi Connected!");
  Serial.print("📡 ESP32 IP Address: ");
  Serial.println(WiFi.localIP());
  Serial.println("👆 Enter this IP in the keypad app!");

  // Register routes
  server.on("/add",     HTTP_POST,    handleAdd);
  server.on("/clear",   HTTP_POST,    handleClear);
  server.on("/status",  HTTP_GET,     handleStatus);
  server.on("/add",     HTTP_OPTIONS, handleOptions);
  server.on("/clear",   HTTP_OPTIONS, handleOptions);

  server.begin();
  Serial.println("🚀 Server running on port 80");
}

// ─── LOOP ─────────────────────────────────────────────────────────────────────
void loop() {
  server.handleClient();
}
