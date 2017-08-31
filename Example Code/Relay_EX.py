#!/usr/bin/python  
import RPi.GPIO as GPIO  
import time  
  
GPIO.setmode(GPIO.BCM)  
  
# init list with pin numbers  
  
#pinList = [17, 23]  
pin = 17
  
# loop through pins and set mode and state to 'low'  
  
#for i in pinList:   
  #GPIO.setup(i, GPIO.OUT)   
  #GPIO.output(i, GPIO.HIGH) 
GPIO.setup(pin, GPOI.OUT)
GPIO.output(pin, GPIO.HIGH) 
  
# time to sleep between operations in the main loop  
  
SleepTime = 2  
  
# main loop  
  
try:  
  GPIO.output(17, GPIO.LOW)  
  print "ONE"  
  time.sleep(SleepTime);   

  #GPIO.output(23, GPIO.LOW)  
  #print "TWO"  
  #time.sleep(SleepTime);    
  GPIO.cleanup()  
  print "Good bye!"  
  
# End program cleanly with keyboard  
except KeyboardInterrupt:  
  print " Quit"  
  
  # Reset GPIO settings  
  GPIO.cleanup()  