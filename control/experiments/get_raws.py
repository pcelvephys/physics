#!/usr/bin/python
import LeCroy
import time
from sys import argv

channels = map(int, argv[1:])

path = "/home/lab/optomech" #raw_input("Where is server mounted? ")
filenames = {channel: "%s/data/timestamped/%s_CH%02u.raw" % (path, time.strftime("%Y-%m-%d_%H-%M-%S"), channel) for channel in channels}
for channel in channels:
    print("Will save CH%02u to %s" % (channel, filenames[channel]))

scope = LeCroy.WS3024()

print("Downloading data")
raws = {channel: scope.raw(channel) for channel in channels}

print("Saving")
for channel in channels:
    with open(filenames[channel], 'w') as h:
        h.write(raws[channel])

print("Done")
