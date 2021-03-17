#include "hc_sr04.h"


HC_SR04::HC_SR04(int echoPin, int triggerPin) {
  echoPin = echoPin;
  triggerPin = triggerPin;
  pinMode(echoPin, INPUT);
  pinMode(triggerPin, OUTPUT);
}

void HC_SR04::clearTriggerPin(){
  // Clears the triggerPin condition
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
}

double HC_SR04::getDistance() {
  clearTriggerPin();
  // Sets the triggerPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  double duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  double distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  return distance;
}
