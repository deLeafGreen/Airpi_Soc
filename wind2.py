#!/usr/bin/python
import serial
import time
import sys
import csv


#wind zeugs

ser = serial.Serial('/dev/ttyACM0',9600)

def frequency():
    
    try:
        while True:
            wert = ser.readline()
            clock = strftime("%Y-%m_%d %H:%M:%S",gmtime())
            with open('/home/pi/csv/wind.csv','a') as csvfile:
                    writer = csv.writer(csvfile,delimiter=',',quotechar = '|',quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([wert,clock])
    
    except KeyboardInterrupt:
        print("User interrupted windspeed")


print(frequency())
