import time
import RPi.GPIO as GPIO
import relay.py 
from relay import func, func2

#use GPIO 7 as noise senssor
#use GPIO 12 as relay

#decibel range for clap is 65 - 90 

noisePin = 7
relayPin = 12

pinList = [noisePin, relayPin]

for i in pinList:   
  GPIO.setup(i, GPIO.OUT)   
  GPIO.output(i, GPIO.HIGH) 


#if: clap, 
	#GPIO.output(relayPin) == HIGH, set GPIO.output(relayPin, GPIO.LOW)
#else: 
	#GPIO.output(relayPin) == LOW, set GPIO.output(relayPin, GPIO.HIGH)
