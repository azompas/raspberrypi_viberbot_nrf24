#ifndef NRF24_COM_H
#define NRF24_COM_H

#include <RF24Network.h>
#include <RF24.h>
#include <SPI.h>
#include "definitions.h"
#include <string.h>
#include "data.h"

struct Message {
  //unsigned long ms;
  String sensor;
  String msg;
};

class NRF24COM {
  private:
    RF24 *radio = NULL;
    RF24Network *network = NULL;
    Data data;
    void setData(RF24NetworkHeader header, Message message);
  public:
    NRF24COM();
    NRF24COM(int cePin, int csnPin);
    void update();
    void check();
    bool available();
    void getData();
};


#endif
