#!/usr/bin/python
import matplotlib as mpl
mpl.use("Agg")
from sys import argv
filenames = argv[1:]

for filename in filenames:
	print("%s\t%i/%i" % (filename, filenames.index(filename), len(filenames)))
	with open(filename) as h:
		raw = h.read()

	import LeCroy
	(WAVEDESC, x, y, i) = LeCroy.InterpretWaveform(raw)
	import pylab as p
	from scipy import signal
	Fs = 1/(x[1]-x[0])
	f,t,Sxx = signal.spectrogram(y,Fs,nperseg=1<<15)
	p.pcolormesh(t,f/1e3,p.log10(Sxx))
	p.ylim([1.945e3,1.955e3])
	p.ylabel('Frequency/kHz')
	p.xlabel('Time/s')
	p.savefig(filename + '-spectrogram-zoom.png')
	p.ylim([1.7e3,2.3e3])
	p.savefig(filename + '-spectrogram-wide.png')
	p.close("All")
	#p.show()
