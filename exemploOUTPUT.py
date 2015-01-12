#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

#GPIO7 
GPIO.setup(7, GPIO.OUT)
#GPIO0 
GPIO.setup(11, GPIO.OUT)
#GPIO1 
GPIO.setup(12, GPIO.OUT)
#GPIO2 
GPIO.setup(13, GPIO.OUT)
#GPIO3
GPIO.setup(15, GPIO.OUT)
#GPIO4
GPIO.setup(16, GPIO.OUT)
#GPIO5
GPIO.setup(18, GPIO.OUT)
#GPIO6
GPIO.setup(22, GPIO.OUT)

try:
	while 1:
	
		print "GPIO.output(7, True)"
		GPIO.output(7, True)
		time.sleep(.2)
		print "GPIO.output(7, False)"
		GPIO.output(7, False)
		time.sleep(.2)
	
		print "GPIO.output(11, True)"
		GPIO.output(11, True)
		time.sleep(.2)
		print "GPIO.output(11, False)"
		GPIO.output(11, False)
		time.sleep(.2)
	
		print "GPIO.output(12, True)"
		GPIO.output(12, True)
		time.sleep(.2)
		print "GPIO.output(12, False)"
		GPIO.output(12, False)
		time.sleep(.2)
	
		print "GPIO.output(13, True)"
		GPIO.output(13, True)
		time.sleep(.2)
		print "GPIO.output(13, False)"
		GPIO.output(13, False)
		time.sleep(.2)
	
		print "GPIO.output(15, True)"
		GPIO.output(15, True)
		time.sleep(.2)
		print "GPIO.output(15, False)"
		GPIO.output(15, False)
		time.sleep(.2)
	
		print "GPIO.output(16, True)"
		GPIO.output(16, True)
		time.sleep(.2)
		print "GPIO.output(16, False)"
		GPIO.output(16, False)
		time.sleep(.2)
	
		print "GPIO.output(18, True)"
		GPIO.output(18, True)
		time.sleep(.2)
		print "GPIO.output(18, False)"
		GPIO.output(18, False)
		time.sleep(.2)
	
		print "GPIO.output(22, True)"
		GPIO.output(22, True)
		time.sleep(.2)
		print "GPIO.output(22, False)"
		GPIO.output(22, False)
		time.sleep(.2)
	
except KeyboardInterrupt:
    pass	

GPIO.cleanup()
