from time import sleep
import numpy as np
class SPC:
	def __init__(self, address = '/dev/ttyS0', timeout = 4):
		self.address = address
		import serial
		self.SPC_serial = serial.Serial(address, timeout=timeout)
		self.connection = serial.Serial(self.address)

	def raw(self, bytes=100):
		self.connection.flushInput()
		return self.connection.read(bytes)

	def flush(self):
		self.SPC_serial.flush()

        def write(self, cmd):
                if not cmd.endswith('\r'):
                	print("Carriage return added")
		        cmd += '\r'
                self.SPC_serial.write(cmd)

        def readline(self):
                return self.SPC_serial.readline()

        def readlines(self):
                return self.SPC_serial.readlines()

	def ask(self, command_num):
		self.flush()
		message = "~ 05 " + command_num + " 00\r"
		print(message)
		print([ord(char) for char in message])
		print([hex(ord(char)) for char in message])
		self.write(message)
		return self.readlines()

#in ipython:

#In [1]: from ionpump import SPC; thing = SPC(); thing.flush(), thing.ask("01")

#~ 05 01 00
#[126, 32, 48, 53, 32, 48, 49, 32, 48, 48, 13]
#['0x7e', '0x20', '0x30', '0x35', '0x20', '0x30', '0x31', '0x20', '0x30', '0x30', '0xd']

#Out[1]: (None, [])

