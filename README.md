# raspberrypi_viberbot_nrf24
Viberbot on raspberry pi is used to wirlessly control arduinos with nrf24l01 modules.

These examples use Viber Python Bot API from Viber and the RF24Network library from TMRh20.

## Getting started

### Viber Python Bot API
Instalation and example code can be found [here](https://developers.viber.com/docs/api/python-bot-api/)

### RF24Network library
Documentation for the library can be found [here](http://tmrh20.github.io/RF24Network/)

To install the library on raspberry pi and be able to use the python examples, the following steps have to be followed:
* Clone both RF24 and and RF24Network libraries as it is described [here](http://tmrh20.github.io/RF24Network/md_README.html)
* Use the python wrapper to install the libraries as it is described [here](http://tmrh20.github.io/RF24/Python.html)<br />
  (for each library the *setup.py* file is under *pyRF24* or *pyRF24Network* directory respectively)
 
## Running the code
To run the code on the arduino, simply upload the sketch to the microcontroller.__
To run the code on raspberry pi, you have to run it with **sudo**
  
## Usefull links
* [http://tmrh20.github.io/RF24/RPi.html](http://tmrh20.github.io/RF24/RPi.html)
* [http://tmrh20.github.io/RF24/](http://tmrh20.github.io/RF24/)
