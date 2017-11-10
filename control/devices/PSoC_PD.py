import serial

PSoC = serial.Serial("/dev/ttyACM0", timeout=1, baudrate=115200)
channel = 1
points = 10

def readline(s):
	buffer = ''
	while not buffer.endswith('\n'):
		print ">%s<" % buffer
		buffer += s.read()
	return buffer

while True:
	PSoC.write("%d %d\n" % (channel, points))
	
	data = list()
	for n in range(points):
		print readline(PSoC)
#		data.append(int(PSoC.readline().strip()))
#		print data[-1]
