#!/usr/bin/python
try:
    from sys import argv
    filename = argv[1]
except IndexError:
    from glob import glob
    filename = reduce(lambda a,b: {True: a, False: b}[a>b], glob('*.raw'))
with open(filename) as h:
    raw = h.read()

import LeCroy
(WAVEDESC, x, y, i) = LeCroy.InterpretWaveform(raw)
import pylab as p
from scipy import signal
Fs = 1/(x[1]-x[0])
f,t,Sxx = signal.spectrogram(y,Fs,nperseg=1<<15)
p.pcolormesh(t,f/1e3,p.log10(Sxx))
p.ylim([36,46])
p.ylabel('Frequency/kHz')
p.xlabel('Time/s')
p.savefig(filename + '-spectrogram-zoom.png')
p.ylim([0,150])
p.savefig(filename + '-spectrogram-wide.png')
p.show()
