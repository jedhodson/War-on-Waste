/*
   Basic AS7265X serial reader
*/

#include "SparkFun_AS7265X.h"
AS7265X sensor;
#include <Wire.h>
#define ACTION_BYTE 61

void setup() {
  Serial.begin(9600);
  // while(!Serial); // Wait for serial connection

  pinMode(LED_BUILTIN, OUTPUT);

  if (! sensor.begin() ) {
    digitalWrite(LED_BUILTIN, HIGH);
    while (true);
  }

  sensor.disableIndicator();
}

void loop() {
  // If theres something in the serial buffer respond. We dont care what
  if (Serial.available() > 0) {
    Serial.read(); // Discard
    sensor.takeMeasurementsWithBulb();

    Serial.println( // Its ugly but it works
      (String)sensor.getCalibratedA() + "," + // 410
      (String)sensor.getCalibratedB() + "," + // 435
      (String)sensor.getCalibratedC() + "," + // 460
      (String)sensor.getCalibratedD() + "," + // 485
      (String)sensor.getCalibratedE() + "," + // 510
      (String)sensor.getCalibratedF() + "," + // 535
      (String)sensor.getCalibratedG() + "," + // 560
      (String)sensor.getCalibratedH() + "," + // 585
      (String)sensor.getCalibratedI() + "," + // 610
      (String)sensor.getCalibratedJ() + "," + // 645
      (String)sensor.getCalibratedK() + "," + // 680
      (String)sensor.getCalibratedL() + "," + // 705
      (String)sensor.getCalibratedR() + "," + // 730
      (String)sensor.getCalibratedS() + "," + // 760
      (String)sensor.getCalibratedT() + "," + // 810
      (String)sensor.getCalibratedU() + "," + // 860
      (String)sensor.getCalibratedV() + "," + // 900
      (String)sensor.getCalibratedW()         // 940
    );
  }
}
