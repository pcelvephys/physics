#!/usr/bin/python
import pylab as p
from glob import glob
import LeCroy
import time
from bisect import bisect
MHz = 1e6
kHz = 1e3
tau = 2*p.pi

freqRange = [1*MHz + 1*kHz, 1*MHz + 100*kHz] # heterodyne (preferable)
#freqRange = [1*kHz, 100*kHz] # homodyne
psds = dict()

while True:
    files = glob('/home/lab/optomech/data/timestamped/*raw')
    files.sort()
    files = files[-5:]

    for f in files:
        if not f in psds.keys():
            print(f)
            with open(f) as h:
                (header,x,y,i) = LeCroy.InterpretWaveform(h.read())
            Fs = 1/(x[1]-x[0])
            psd, freq = p.psd(y,NFFT=1<<17,Fs=Fs)
            p.close('all')
            nRange = [bisect(freq, fx) for fx in freqRange]
            psds[f] = [a[nRange[0]:nRange[1]] for a in freq,psd]

    dropkeys = set(psds.keys()) - set(files)
    for k in dropkeys:
        psds.pop(k)

    for f in files:
        print(f)
        freq,psd = psds[f]
        p.plot(freq, psd, label=f.split('/')[-1])
    p.legend()
    p.yscale('log'); p.grid();
    p.show()


    #from subprocess import check_output
    #check_output("python get_raw.py nope", shell=True)

    path = "/home/lab/optomech" #raw_input("Where is server mounted? ")
    filename = "%s/data/timestamped/%s.raw" % (path, time.strftime("%Y-%m-%d_%H-%M-%S"))

    scope = LeCroy.WS3024()
    print("Telling scope to take a single trace")
    scope.write('ARM_ACQUISITION')
    scope.write('*TRG')

    print("Wait a second...")
    time.sleep(2)
    scope.waitOPC()

    print("Downloading data")
    channel = 1
    raw = scope.raw(channel)

    print("Returning scope to NORMAL trigger")
    scope.write('TRIG_MODE NORMAL')

    print("Saving")
    with open(filename, 'w') as h:
        h.write(raw)

    print("Done")
