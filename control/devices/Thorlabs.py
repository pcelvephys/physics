#!/usr/bin/python
class PM100D:
	def __init__(self, idVendor=0x1313, idProduct=0x8072):
                self.idVendor  = idVendor
                self.idProduct = idProduct
                import usbtmc
                self.connection = usbtmc.Instrument(self.idVendor, self.idProduct)
                self.write = self.connection.write
                self.read  = self.connection.read
                self.ask   = self.connection.ask
                self.read_raw = self.connection.read_raw                
	        self.close = self.connection.close
                
	def power(self, N=10, dt=0.1):
		from time import sleep

		powers = list()
		for n in range(N):
			sleep(dt)
			powers.append(float(self.ask('READ?\n')))

		from pylab import array, mean, std
		powers = array(powers)

		return (mean(powers), std(powers))
		
	def wavelength(self, wavelength=None):
		if wavelength is not None:
			self.write(":SENSE:CORRECTION:WAVELENGTH %f\n" % wavelength)
		wavelength = float(self.ask(":SENSE:CORRECTION:WAVELENGTH?\n").strip())
		return wavelength
