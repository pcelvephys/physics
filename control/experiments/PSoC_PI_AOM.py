import serial

PSoC = serial.Serial("/dev/ttyACM0", timeout=1, baudrate=115200)

def line(s):
	buffer = ''
	while not buffer.endswith('\n'):
		#print ">%s<" % buffer
		buffer += s.read()
	return buffer




while True:
	#PSoC.flush()
	PSoC.write("%s\n" % str(raw_input("Serial to PSoC:\t")))


	#reply = PSoC.read(20)

	reply = line(PSoC)

	print(reply)

