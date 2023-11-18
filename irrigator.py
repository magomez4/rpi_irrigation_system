# import sys

# pin - time
# 14 - 16s - flor noche
# 15 - 16 - sabila
# 18 - 10 - potos
# 23 - 8 - mini sabila


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

class Plant:
	pantPin = 0
	waterTime = 0
	def __init__(self, sigPin, wTime):
		self.plantPin = sigPin
		self.waterTime = wTime
		self.plantRelay = RelayController(self.pantPin)

	
	def waterPlant(self):
		self.plantRelay.openRelay() # start watering
		time.sleep(self.waterTime) # water for defined time
		self.plantRelay.closeRelay() # stop watering

		
		
# Plants: signal pin, water time
florNoche = Plant(14,16)
sabila = Plant(15,16)
potos = Plant(18,10)
miniSabila = Plant(23,8)

def waitDays(numDays):
	secsPerDay = 86400
	daysWaited = 0
	while daysWaited < numDays:
		time.sleep(secsPerDay)
		daysWaited = daysWaited + 1

try:
	while True:
		potos.waterPlant()
		sabila.waterPlant()
		florNoche.waterPlant()
		miniSabila.waterPlant()
		waitDays(7)
except KeyboardInterrupt:
	GPIO.cleanup()
	#sys.stdout.close()
	pass
