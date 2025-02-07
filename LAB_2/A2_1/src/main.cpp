#include <Arduino.h>
#include <Arduino_LSM6DSOX.h>
#include <WiFiNINA.h>
#include <NTPClient.h>
#include <WiFiUdp.h>
#include <TimeLib.h>

#define TASK2_1 0
#define TASK2_2 0

#if TASK2_1 1
  void setup(){

  }

  void loop(){

  }

#endif

#if TASK2_2 1
  void setup(){

  }

  void loop(){

  }

#endif


const char* ssid = "Pixel_4585";
const char* password = "123456789";

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org", 3600, 60000);

unsigned long epochTime = 0;
unsigned long lastUpdate = 0;
unsigned long lastSampleTime = 0;


void printFormattedTime(unsigned long epochTime) {

    tmElements_t tm;
    breakTime(epochTime, tm);

    if (tm.Hour < 10) {
        Serial.print("0");
    }
    Serial.print(tm.Hour);
    Serial.print(":");
    if (tm.Minute < 10) {
        Serial.print("0");
    }
    Serial.print(tm.Minute);
    Serial.print(":");
    if (tm.Second < 10) {
        Serial.print("0");
    }
    Serial.print(tm.Second);
}


void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("Connecting to WIFI");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to WIFI");

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
  timeClient.begin();
  timeClient.update();

  epochTime = timeClient.getEpochTime();
  lastUpdate = millis();

  Serial.print("Time is: ");
  Serial.println(epochTime);

  WiFi.disconnect();
}

void loop() {
  if (millis() - lastSampleTime > 1000) {
    lastSampleTime = millis();
    if (IMU.temperatureAvailable()) {
      float temp = 0;
      IMU.readTemperatureFloat(temp);
      Serial.print("Time: ");
      printFormattedTime(epochTime + (millis() - lastUpdate) / 1000);
      Serial.print(" | Temp: ");
      Serial.println(temp);
    }
  }
}