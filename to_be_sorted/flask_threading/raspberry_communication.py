#!/usr/bin/env python

#
# Simplest possible example of using RF24Network,
#
#  TRANSMITTER NODE
#  Sends messages from to receiver.
#
from __future__ import print_function
import time
from struct import *
from RF24 import *
from RF24Network import *

class RaspberyComNrf24:
	def __init__(self):
		# CE Pin, CSN Pin, SPI Speed

		# Setup for GPIO 22 CE and GPIO 25 CSN with SPI Speed @ 1Mhz
		#radio = radio(RPI_V2_GPIO_P1_22, RPI_V2_GPIO_P1_18, BCM2835_SPI_SPEED_1MHZ)

		# Setup for GPIO 22 CE and CE0 CSN with SPI Speed @ 4Mhz
		#radio = RF24(RPI_V2_GPIO_P1_15, BCM2835_SPI_CS0, BCM2835_SPI_SPEED_4MHZ)

		# Setup for GPIO 22 CE and CE1 CSN with SPI Speed @ 8Mhz
		#self.radio = RF24(RPI_V2_GPIO_P1_15, BCM2835_SPI_CS0, BCM2835_SPI_SPEED_8MHZ)
		self.radio = RF24(22,0)

		# Setup for GPIO 22 CE and CE0 CSN for RPi B+ with SPI Speed @ 8Mhz
		#radio = RF24(RPI_BPLUS_GPIO_J8_22, RPI_BPLUS_GPIO_J8_24, BCM2835_SPI_SPEED_8MHZ)

		#radio = RF24(RPI_V2_GPIO_P1_15, RPI_V2_GPIO_P1_24, BCM2835_SPI_SPEED_8MHZ)
		self.network = RF24Network(self.radio)

		self.millis = lambda: int(round(time.time() * 1000)) & 0xffffffff
		self.octlit = lambda n:int(n, 8)

		# Address of our node in Octal format (01,021, etc)
		self.this_node = self.octlit("01")

		# Address of the other node
		self.other_node = self.octlit("00")

		self.radio.begin()
		time.sleep(0.1)
		self.network.begin(90, self.this_node)    # channel 90
		self.radio.printDetails()
		self.msg = None
		self.new_msg = False
		print('finish initializing')

	def set_message(self, msg):
		self.msg = msg
		self.new_msg = True

	def send_message(self):
		print('Sending ..')
		payload = pack('<LL6s', self.millis(), self.msg, b'Hello')
		ok = self.network.write(RF24NetworkHeader(self.other_node), payload)
		return ok

	def run(self):
		packets_sent = 0
		last_sent = 0

		#ms -  How long to wait before sending the next message
		interval = 2000
		print('start run')
		while True:
			self.network.update()
			now = self.millis()
			# If it's time to send a message, send it!
			if self.new_msg:
				ok = self.send_message()
				if ok:
					self.new_msg = False
					print('ok.')
				else:
					count = 0
					while not ok and count < 3:
						print ('retrying...')
						ok = self.send_message()
						count += 1
					self.new_msg = False
					if not ok:
						print('failed.')

	def updateNetwork(self):
		self.network.update()

if __name__ == "__main__":
	com = RaspberyComNrf24()
	count = 0
	interval = 2000
	before = 0
	while True:
		com.updateNetwork()
		if (com.millis() - before >= interval):
			com.set_message(count)
			count += 1
			before = com.millis()
			ok = com.send_message()
			if ok:
				print('succeed')
			else:
				print('failure')
