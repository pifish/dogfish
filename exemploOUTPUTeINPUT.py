#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


#OUTPUT
#GPIO7 
GPIO.setup(7, GPIO.OUT)
#GPIO0 
GPIO.setup(11, GPIO.OUT)
#GPIO2 
GPIO.setup(13, GPIO.OUT)
#GPIO3
GPIO.setup(15, GPIO.OUT)


#INPUT
#GPIO1 
GPIO.setup(12, GPIO.IN)
#GPIO4
GPIO.setup(16, GPIO.IN)
#GPIO5
GPIO.setup(18, GPIO.IN)
#GPIO6
GPIO.setup(22, GPIO.IN)

try:
	while 1:
		if (GPIO.input(12)):
		        print "GPIO.input(12) pressionado!"
		
		if (GPIO.input(16)):
		        print "GPIO.input(16) pressionado!"
		
		if (GPIO.input(18)):
		        print "GPIO.input(18) pressionado!"
		
		if (GPIO.input(22)):
		        print "GPIO.input(22) pressionado!"
		
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

except KeyboardInterrupt:
    pass	

GPIO.cleanup()
