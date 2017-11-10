#!/usr/bin/python

from time import sleep
import leybold
import irc


irclog = irc.irc('Pressure', 'pressure', 'Leybold ITR90')
itr90 = leybold.itr90()

while True:
    pressure = itr90.pressure()
    message = "Pressure is %g mBar" % pressure
    print(message)
    irclog.write(message)
    sleep(5)
