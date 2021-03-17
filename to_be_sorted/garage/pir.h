#ifndef PIR_H
#define PIR_H

#include "Arduino.h"


class PIR {
  public:
    PIR(int inputPin);
    String detect();
  private:
    int inputPin;
    boolean detection;
};

#endif
