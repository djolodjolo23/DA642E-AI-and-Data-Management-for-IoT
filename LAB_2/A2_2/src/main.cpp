#include <Arduino.h>
#include <Arduino_LSM6DSOX.h>
#include <WiFiNINA.h>
#include <NTPClient.h>
#include <WiFiUdp.h>
#include <TimeLib.h>
#include "secrets.h"

const char* ssid = SSID;
const char* password = PASSWORD;

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, NTP_SERVER, 3600, 60000);

unsigned long epochTime = 0;
unsigned long lastUpdate = 0;
unsigned long lastSampleTime = 0;


void printFormattedDate(unsigned long epochTime) {
    tmElements_t tm;
    breakTime(epochTime, tm);

    Serial.print((int)tm.Year + 1970);
    Serial.print("-");
    if (tm.Month < 10) {
        Serial.print("0");
    }
    Serial.print(tm.Month);
    Serial.print("-");
    if (tm.Day < 10) {
        Serial.print("0");
    }
    Serial.print(tm.Day);
}

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
  if (millis() - lastSampleTime > 500) {
    lastSampleTime = millis();
    if (IMU.accelerationAvailable() && IMU.gyroscopeAvailable()) {
      float accX, accY, accZ;
      float gyroX, gyroY, gyroZ;
      IMU.readAcceleration(accX, accY, accZ);
      IMU.readGyroscope(gyroX, gyroY, gyroZ);
      Serial.print("Date: ");
      printFormattedDate(epochTime + (millis() - lastUpdate) / 1000);
      Serial.print(" | Time: ");
      printFormattedTime(epochTime + (millis() - lastUpdate) / 1000);
      Serial.print(" | Acc: ");
      Serial.print(accX);
      Serial.print(", ");
      Serial.print(accY);
      Serial.print(", ");
      Serial.print(accZ);
      Serial.print(" | Gyro: ");
      Serial.print(gyroX);
      Serial.print(", ");
      Serial.print(gyroY);
      Serial.print(", ");
      Serial.println(gyroZ);
    }
  }
}