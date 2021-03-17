#ifndef HC_SR04_H
#define HC_SR04_H

#include "Arduino.h"


class HC_SR04 {
  private:
    int echoPin;
    int triggerPin;
    void clearTriggerPin();
  public:
    HC_SR04(int echoPin, int triggerPin);
    double getDistance();
};

#endif
