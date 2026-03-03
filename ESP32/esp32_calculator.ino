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
