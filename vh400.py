import serial

#vh400 Feuchtigkeitssensor

ser = serial.Serial('/dev/ttyACM0',9600)

while 1:
	wert=int(ser.readline())
    	
	#Volt
	v = 3/614.0 * wert
	str_v=str(v)
	if(v >= 0 and v < 1.1):
		result = 10 * v - 1

	if(v >= 1.1 and v < 1.3 ):
		result = 25*v - 17.5
	
	elif(v >= 1.3 and v < 1.82):
		result = 48.08*v - 47.5
	
	#eig von 1.82 bis 2.2
	else:
		result = 26.32*v - 7.89
	str_res = str(result)
	print("Volt:"+str_v+","+str_res)
	
