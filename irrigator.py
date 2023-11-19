# import sys

# pin - time
# 14 - 10s - flor noche
# 15 - 10 - sabila
# 18 - 8 - potos
# 23 - 5 - mini sabila


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
	plantPin = 0
	waterTime = 0
	def __init__(self, sigPin, wTime):
		self.plantPin = int(sigPin)
		self.waterTime = int(wTime)
		self.plantRelay = RelayController(self.plantPin)
		self.plantRelay.closeRelay()

	
	def waterPlant(self):
		self.plantRelay.openRelay() # start watering
		time.sleep(self.waterTime) # water for defined time
		self.plantRelay.closeRelay() # stop watering

#florNoche = RelayController(14)
#sabila = RelayController(15)
#potos = RelayController(18)
#miniSabila = RelayController(23)

def waitDays(numDays):
	secsPerDay = 86400
	daysWaited = 0
	while daysWaited < numDays:
		time.sleep(secsPerDay)
		daysWaited = daysWaited + 1


# Plants: signal pin, water time
GPIO.cleanup() #start with a clean setup
potos = Plant(18,8)
time.sleep(5)

sabila = Plant(15,10)
time.sleep(5)

florNoche = Plant(14,10)
time.sleep(5)

miniSabila = Plant(23,5)
time.sleep(5)

#try:
#	while True:
#	print("watering potos")
#	print(" ")
#	potos.waterPlant()
#	time.sleep(potos.waterTime)

#	print("watering sabila")
#	print(" ")
#	sabila.waterPlant()
#	time.sleep(sabila.waterTime)

#	print("watering flor de noche")
#	print(" ")
#	florNoche.waterPlant()
#	time.sleep(florNoche.waterTime)

#	print("watering mini sabila")
#	print(" ")
#	miniSabila.waterPlant()
#	time.sleep(miniSabila.waterTime)


print("watering potos")
print(" ")
potos.waterPlant()
time.sleep(potos.waterTime)

print("watering sabila")
print(" ")
sabila.waterPlant()
time.sleep(sabila.waterTime)

print("watering flor de noche")
print(" ")
florNoche.waterPlant()
time.sleep(florNoche.waterTime)

print("watering mini sabila")
print(" ")
miniSabila.waterPlant()
time.sleep(miniSabila.waterTime)

GPIO.cleanup()


#		potos.openRelay()
#		time.sleep(10)
#		potos.closeRelay()

#		time.sleep(5)

#		sabila.openRelay()
#		time.sleep(16)
#		sabila.closeRelay()

#		time.sleep(5)

#		florNoche.openRelay()
#		time.sleep(16)
#		florNoche.closeRelay()

#		time.sleep(5)

#		miniSabila.openRelay()
#		time.sleep(8)
#		miniSabila.closeRelay()

#		waitDays(7)
#except KeyboardInterrupt:
#	GPIO.cleanup()
	#sys.stdout.close()
#	pass

