#include "nrf24_com.h"


NRF24COM::NRF24COM() {
  NRF24COM(7,8);
}

NRF24COM::NRF24COM(int cePin, int csnPin){
  radio = new RF24(cePin, csnPin);                // nRF24L01(+) radio attached using Getting Started board
  network = new RF24Network(*radio);      // Network uses that radio
  SPI.begin();
  radio->begin();
  network->begin(90, this_node);
}

void NRF24COM::update() {
  network->update();
}

bool NRF24COM::available() {
  network->available();
}

void NRF24COM::getData() {
  RF24NetworkHeader header;                          // If so, grab it and print it out
  Message message;
  uint16_t payloadSize = network->peek(header);       // Use peek() to get the size of the payload
  network->read(header,&message,payloadSize);      // Get the data
}

void NRF24COM::setData(RF24NetworkHeader header, Message message) {
  data.setHeader(header);
  data.setSensor(message.sensor);
  data.setMessage(message.msg);
}
