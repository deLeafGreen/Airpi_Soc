#!/usr/bin/python

#import section
import RPi.GPIO as GPIO
import sys
from time import sleep 

#use P1 header pin numbering convention
GPIO.setmode(GPIO.BCM)


#GPIO Pin festlegen

frequency = 17

#set direction
GPIO.setup(frequency,GPIO.IN)


def windGeschwindigkeit():

    value = GPIO.input(frequency)
    
    sys.stdout.write("%s" % value)
    sys.stdout.flush()
    sleep(0.5)



while True:
    windGeschwindigkeit()


