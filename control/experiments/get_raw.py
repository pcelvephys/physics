#!/usr/bin/python
import LeCroy
import time
from sys import argv

if len(argv) > 1:
    refresh = False
else:
    refresh = True

path = "/media/optomech" #raw_input("Where is server mounted? ")
channels = [4] #list(map(int, raw_input("Channel number:\t").split()))

scope = LeCroy.WS3024(interface="USBTMC")

if refresh:
    print("Telling scope to take a single trace")
    scope.write('TRIG_MODE SINGLE')
    scope.write('ARM_ACQUISITION')
    scope.write('*TRG')

    print("Wait a second...")
    time.sleep(10)
    scope.waitOPC()


for channel in channels:
    filename = "%s/data/data/timestamped/%s-CH%u.raw" % (path, time.strftime("%Y-%m-%d_%H-%M-%S"), channel)
    print("Will save to %s" % filename)

    print("Downloading data")
    raw = scope.raw(channel)

    print("Saving...")
    with open(filename, 'wb') as h:
        h.write(raw)

print("Returning scope to NORMAL trigger")
scope.write('TRIG_MODE NORMAL')

print("Done")
