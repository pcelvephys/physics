#!/usr/bin/python
import pylab as p
import LeCroy

from sys import argv
from os.path import exists

files = argv[1:]
files.sort()

for src in files[::-1]:
    dst = src[:-4] + '-homodyne.png'
    if not exists(dst):
        print src, dst
        (header,x,y,i) = LeCroy.InterpretWaveform(open(src).read())
        Fs = 1/(x[1]-x[0])
        p.psd(y,NFFT=1<<19,Fs=Fs/1e3)
        p.xlabel('Frequency/kHz')
        p.ylim([-100,+20])
        p.xlim([0,100])
        p.savefig(dst)
        p.close('all')
