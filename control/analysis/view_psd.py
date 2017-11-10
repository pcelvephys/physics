#!/usr/bin/python
#import matplotlib as mpl
#mpl.use("Agg")
import LeCroy
import pylab as p
from multiprocessing import Pool

from sys import argv
filenames = argv[1:]

def raw2psd(filename):
        fig, ax = p.subplots(figsize=(20,12))
	print('%5u/%5u %s' % (filenames.index(filename),len(filenames),filename))
	with open(filename) as h:
		raw = h.read()

	(WAVEDESC, x, y, i) = LeCroy.InterpretWaveform(raw)

	dt = (x[-1]-x[0])/(len(x)-1)

	Fs=1/dt

	(A,f) = p.psd(y,Fs=Fs,NFFT=1<<19)
	p.cla()
	ax.plot(f/1e3, 10*p.log10(A), label=filename)
	ax.set_xlabel('Frequency/kHz')
	ax.set_ylabel('PSD/dB/Hz')
	ax.set_ylim(-110, -40)
	ax.set_xlim(0, 200)
	p.tight_layout()
	ax.legend()
	ax.grid()
	#fig.savefig("{}-PSD.pdf".format(filename))
        #fig.savefig("{}-PSD.png".format(filename))
	p.show()
	p.close(fig)

	return 0

pool = Pool(8)
psds = pool.map(raw2psd, filenames)
