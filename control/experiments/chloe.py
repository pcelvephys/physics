#!/usr/bin/python
import pylab as p
import LeCroy

f = '/home/lab/optomech/data/timestamped/2017-02-21_16-37-42.raw'
(header,t,V,i) = LeCroy.InterpretWaveform(open(f).read())

p.plot(t,V,".")

p.grid()

p.show()
