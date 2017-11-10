#!/usr/bin/python
print("Begin.")

import LeCroy
from sys import argv
import pylab as p
p.ion()
from scipy import signal
import numpy as np
from scipy.optimize import curve_fit
from time import sleep

def import_from_raw(filename):
	with open(filename) as h:
	    raw = h.read()
	return LeCroy.InterpretWaveform(raw) 

def time2psd(x,y):
	dt = (x[-1]-x[0])/(len(x)-1)

	Fs=1/dt

	(A,f) = p.psd(y,Fs=Fs,NFFT=1<<19)
	#p.xlim(0,150e3)
	#p.show()
	#p.close('all')

	return (A,f)

def lorentzian(f, scale, f0, gamma):
		#print(scale, f0, gamma)
		return scale*gamma/((f0**2-f**2)**2+(gamma*f)**2)

filenames = argv[1:]
#filenames = ["/media/optomech/data/timestamped/2016-10-18_17-23-53.raw"]

p0 = [5e6,2e6,500]
freqs = []
fig = p.figure()
ax = fig.add_subplot(111)

display = True

for filename in filenames:
	(WAVEDESC, x, y, i) = import_from_raw(filename)
	num_points = len(x)
	print("File %s contains %i datapoints over a %gs time window" % (filename, len(x), x[-1] - x[0]))

	chunk_length=1e5

	for start_index in np.linspace(0,len(x)- chunk_length, 1e2):
		end_index = start_index + chunk_length
		(A,f) = time2psd(x[start_index:end_index],y[start_index:end_index])

		#find the peak frequencies and save them
		Nmin = sum(f < 1.95e6)
		Nmax = sum(f < 2.05e6)
		try:
			popt, pcov = curve_fit(lorentzian, f[Nmin:Nmax], A[Nmin:Nmax], p0=p0)
			print(popt)
			print("%i / %i - %g percent" % (start_index, num_points, float(start_index)/float(num_points)*100.))
			freqs.append(popt[1])
			if display == True:
				p.cla()
				p.plot(f, 10*np.log10(A))
				p.plot(f[Nmin:Nmax],10*np.log10(lorentzian(f[Nmin:Nmax],*popt)))
				#p.xlim(0,150e3)
				#p.ylim(-200, -110)
				p.grid()
				p.draw()
				p.pause(0.01)
		except:
			print("error")

	p.cla()

	p.plot(freqs)
	p.grid()
	p.draw()
	p.savefig("changing_f.png")
	p.pause(100)

