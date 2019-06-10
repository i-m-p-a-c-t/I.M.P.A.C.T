import serial
arduino = serial.Serial('/dev/ttyACM0', 9600)
while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	str = data.decode("utf-8") 
	index = str.find("Current Position:")
	if index != -1:
		print(str[index:])
		#print(data)
		
