#include "hc_sr04.h"
#include "pir.h"


HC_SR04 frontDoor = HC_SR04(2, 3);
HC_SR04 sideDoor = HC_SR04(4, 5);
PIR pir = PIR(6);

void setup() {
  //frontDoor.clearTriggerPin();
  //sideDoorDoor.clearTriggerPin();
  
}
void loop(){
  frontDoor.getDistance();
  sideDoor.getDistance();
  String msg = pir.detect();
  
}
