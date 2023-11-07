# import sys
import time
import RPi.GPIO as GPIO
import sys, getopt
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
			print("Relay is closed")
			print(" ")
		else:
			GPIO.output(self.signalPin, GPIO.HIGH)
			print("closing relay")
			print(" ")

	
	def openRelay(self):
		GPIO.output(self.signalPin, GPIO.LOW)
		print("opening relay")
		print(" ")


		
	def closeAndOpen(self):
		GPIO.output(self.signalPin, GPIO.HIGH)
		time.sleep(0.2)
		GPIO.output(self.signalPin, GPIO.LOW)
		

def waitDays(numDays):
	secsPerDay = 86400
	daysWaited = 0
	while daysWaited < numDays:
		time.sleep(secsPerDay)
		daysWaited = daysWaited + 1


pinID = int(sys.argv[1])
sleepTime = int(sys.argv[2])
relay = RelayController(pinID)
if sleepTime > 0:
	relay.openRelay()
	time.sleep(sleepTime)
	relay.closeRelay()
else:
	relay.closeRelay()
