while True:
	voltage = input("Voltage:\t")
	pressure = 10 ** (( voltage - 7.75 ) / 0.75)
	print(pressure)
