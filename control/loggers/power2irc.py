#!/usr/bin/python

from time import sleep
import Thorlabs
import irc

irclog = irc.irc('Thorlabs', 'Thorlabs', 'Thorlabs PM100D')
irclog.login()
irclog.join('#logging')
SI = {'nW': 1e-9, 'uW': 1e-6, 'mW': 1e-3}
PM = Thorlabs.PM100D()
PM.wavelength(1550)

while True:
    P, _ = PM.power(N=10)

    #p = PM.power(N=1)[0]
    if P < 1e-6:
    	scale = 'nW'
    elif P < 1e-3:
    	scale = 'uW'
    else:
    	scale = 'mW'
    message = '%.2f %s' % (P/SI[scale], scale)
    print (message)
    irclog.privmsg('#logging', message)

    sleep(2)
