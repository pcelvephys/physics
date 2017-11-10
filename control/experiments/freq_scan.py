# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 13:59:25 2017

@author: lab
"""

import LeCroy
import pylab as pl
import numpy as np
import time

freqs = np.linspace(1e3, 32e3, 10)

SG_idVendor = 0xf4ed
SG_idProduct = 0xee3a
import usbtmc

SG_connection = usbtmc.Instrument(SG_idVendor, SG_idProduct)

scope = LeCroy.WS3024()

save_path = "/home/lab/freq_scan"

def scope_read(filename, channel = 1):
    
    print("Will save to %s" % filename)

    print("Downloading data")
    raw = scope.raw(channel)

    print("Saving...")
    with open(filename, 'w') as h:
        h.write(raw)
    
Amps = []

for freq in freqs:
    current_ranges = []
    SG_connection.write("C1: BSWV FRQ, {}HZ".format(int(freq)))
    for n in range(3):
        filename = "%s/%s-CH%u.raw" % (save_path, time.strftime("%Y-%m-%d_%H-%M-%S"), channel)
        scope_read(filename)
        (WAVEDESC, x, y, i) = LeCroy.readfile(filename)
        R = y.max() - y.min()
        current_ranges.append(R)        
    Amps.append(max(current_ranges))
data = np.array([freqs,Amps])
np.savetxt("data.txt", data)

pl.plot(freqs, Amps)
pl.xlabel("Frequency")
pl.ylabel("Amplitude")
pl.savefig("output.png")
pl.savefig("output.pdf")
