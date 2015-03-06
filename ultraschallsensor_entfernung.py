#!/usr/bin/env python

#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time
import sys
import csv

#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#GPIO Pins zuweisen
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distanz():
  # setze Trigger auf HIGH
  GPIO.output(GPIO_TRIGGER, True)

  # setze Trigger nach 0.01ms aus LOW
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)

  StartZeit = time.time()
  StopZeit = time.time()

  # speichere Startzeit
  while GPIO.input(GPIO_ECHO) == 0:
    StartZeit = time.time()

  # speichere Ankunftszeit
  while GPIO.input(GPIO_ECHO) == 1:
    StopZeit = time.time()

  # Zeit Differenz zwischen Start und Ankunft
  TimeElapsed = StopZeit - StartZeit
  # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
  # und durch 2 teilen, da hin und zurueck
  distanz = (TimeElapsed * 34300) / 2

  return distanz

if __name__ == '__main__':
  count = 0
  try:
    while True:
      abstand = distanz()
      count += 1
      with open('/home/pi/csv/ultra.csv','a') as csvfile:
		writer = csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
		writer.writerow([count,abstand])
      '''
      sys.stdout.write ("%d,%.1f\n" % (count,abstand))
      sys.stdout.flush()'''
      time.sleep(0.1)

  # Beim Abbruch durch STRG+C resetten
  except KeyboardInterrupt:
    print("Messung vom User gestoppt")
    GPIO.cleanup()
