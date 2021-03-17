#include "pir.h"

PIR::PIR(int inputPin) {
  pinMode(inputPin, INPUT);
  detection = false;
}

String PIR::detect() {
  int val = digitalRead(inputPin);  // read input value
  if (val == HIGH) {            // check if the input is HIGH
    if (detection == LOW) {
      // we have just turned on
      return "Motion detected!";
      // We only want to print on the output change, not state
      detection = true;
    } else {
      return "Still Detecting...";
    }
  } else {
    if (detection == true){
      // we have just turned of
      return "Motion ended!";
      // We only want to print on the output change, not state
      detection = false;
    } else {
      return "";
    }
  }
}
