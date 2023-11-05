# import sys
import time
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup() #start with a clean setup

class RelayController:
	signalPin = 0
	def __init__(self, sigPin):
		self.signalPin = sigPin
		GPIO.setup(self.signalPin, GPIO.OUT)
		
	def closeRelay(self):
		if GPIO.input(self.signalPin):
			#print("Relay is closed")
			print(" ")
		else:
			GPIO.output(self.signalPin, GPIO.HIGH)
	
	def openRelay(self):
		GPIO.output(self.signalPin, GPIO.LOW)
		
	def closeAndOpen(self):
		GPIO.output(self.signalPin, GPIO.HIGH)
		time.sleep(0.2)
		GPIO.output(self.signalPin, GPIO.LOW)
		

relay = RelayController(23)
print("opening relay")
relay.openRelay()

def waitDays(numDays):
	secsPerDay = 86400
	daysWaited = 0
	while daysWaited < numDays:
		time.sleep(secsPerDay)
		daysWaited = daysWaited + 1


try:
	while True:
		relay.close() # start watering
		time.sleep(10) # water for 10 secs
		relay.open() # stop watering
		waitDays(7)
except KeyboardInterrupt:
	GPIO.cleanup()
	#sys.stdout.close()
	pass