#ifndef DATA_H
#define DATA_H

#include <RF24Network.h>
#include <string.h>


class Data {
  private:
    void init(RF24NetworkHeader header, String Sensor, String msg);
    RF24NetworkHeader header;
    String sensor;
    String msg;
  public:
    Data();
    Data(RF24NetworkHeader header, String Sensor);
    Data(RF24NetworkHeader header, String Sensor, String msg);
    RF24NetworkHeader getHeader();
    void setHeader(RF24NetworkHeader header);
    void setSensor(String sensor);
    void setMessage(String msg);
    String getSensor();
    String getMessage();
};

#endif
