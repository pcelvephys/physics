import matplotlib as mpl
mpl.use("Agg")
import LeCroy
import pandas as pd
import numpy as np
import time

scope = LeCroy.WS3024()
server_loc = "/home/lab/optomech" #raw_input("Where is server mounted? ")
#scope.ask('*IDN?') #to make beep
#scope.ask('trig_mode?')

channel = 1 #int(raw_input("Channel number:\t"))
(WAVEDESC, x,y,i) = scope.data(channel)
import pylab as p
#p.ion()

samplerate = 500e6 #float(raw_input("Sample rate:\t"))
dt = 1/(samplerate)
power5 = p.psd(y,Fs=1/dt,NFFT=0x10000)
#p.plot(x,y)
pdata = pd.DataFrame(data=np.array([x,y])).transpose()
pdata.to_csv("%s/data/timestamped/%s.csv" % (server_loc, time.strftime("%Y-%m-%d_%H-%M-%S")))
p.grid()
#p.show()
#p.xlim(0,400e3)
p.savefig("%s/data/timestamped/%s_PSD.png" % (server_loc, time.strftime("%Y-%m-%d_%H-%M-%S")))

