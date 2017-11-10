#!/usr/bin/python
print("Importing libraries")
from multiprocessing import Pool
import matplotlib as mpl
mpl.use("Agg")
from sys import argv
import pylab as plt
from scipy import signal
import LeCroy
import numpy as np

filenames = argv[1:]

def specfunct(filename):
	fig, ax = plt.subplots(figsize = (20,12))
        print("{}\t{}/{}".format(filename, filenames.index(filename), len(filenames)))

        with open(filename) as h:
                raw = h.read()

        (WAVEDESC, x, y, i) = LeCroy.InterpretWaveform(raw)

        Fs = 1/(x[1]-x[0])
        x=0
	i=0
	WAVEDESC = 0

	f,t,Sxx = signal.spectrogram(y,Fs,nperseg=1<<15)
	y=0
	Fs=0
        ax.pcolormesh(t,f/1e3, np.log10(Sxx))
        t=0
	f=0
	Sxx=0
	ax.set_ylim([245-15,245+15])
        ax.set_ylabel('Frequency/kHz')
        ax.set_xlabel('Time/s')
	plt.tight_layout()
        fig.savefig(filename + '-spectrogram-zoom.png')
        ax.set_ylim([0,750])
        fig.savefig(filename + '-spectrogram-wide.png')
        print("Finished %s\t%i/%i" % (filename, filenames.index(filename), len(filenames)))
	#fig.close()
	plt.close(fig)


print("Creating worker pool")
pool = Pool(8)

print("Begin map")
thing = pool.map(specfunct, filenames)
#pool.close(); pool.join()


