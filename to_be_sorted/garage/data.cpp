#include "data.h"

Data::Data(RF24NetworkHeader header, String Sensor, String msg) {
  init(header, Sensor, msg);
}

Data::Data(RF24NetworkHeader header, String Sensor)
  :Data(header, sensor, "")
  {
}

Data::Data()
  :Data(RF24NetworkHeader(), "", "")
  {
}

void Data::init(RF24NetworkHeader header, String Sensor, String msg){
  header = header;
  sensor = sensor;
  msg = msg;
}

RF24NetworkHeader Data::getHeader() {
  return header;
}

String Data::getSensor() {
  return sensor;
}

String Data::getMessage() {
  return msg;
}

void Data::setHeader(RF24NetworkHeader header) {
  header = header;
}

void Data::setSensor(String sensor) {
  sensor = sensor;
}

void Data::setMessage(String msg) {
  msg = msg;
}
