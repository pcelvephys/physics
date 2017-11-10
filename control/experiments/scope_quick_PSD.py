import LeCroy
import pandas as pd
import numpy as np
import time

scope = LeCroy.WS3024()
server_loc = raw_input("Where is server mounted? ")
#scope.ask('*IDN?') #to make beep
#scope.ask('trig_mode?')

channel = int(raw_input("Channel number:\t"))
(WAVEDESC, x,y,i) = scope.data(channel)
import pylab as p
#p.ion()

samplerate = float(raw_input("Sample rate:\t"))
dt = 1/(samplerate)
power5 = p.psd(y,Fs=1/dt,NFFT=0x10000)
#p.plot(x,y)
pdata = pd.DataFrame(data=np.array([x,y])).transpose()
pdata.to_csv("%s/data/%s.csv" % (server_loc, time.strftime("%Y-%m-%d_%H-%M-%S")))
p.grid()
p.show()
