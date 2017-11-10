#!/usr/bin/python

from time import sleep
import edwards
import irc

irclog = irc.irc('edwards', 'edwards', 'Edwards nXDS6i Scroll')
irclog.login()
irclog.join('#logging')

pump = edwards.nXDS6i()

while True:
    T = pump.Temperature()
    V,I,P = pump.LinkParameters()

    message = 'T = %5.1f C; V = %5.1f V; I = %5.1f A; P = %5.1f W' % (T,V,I,P)
    irclog.privmsg('#logging', message)

    sleep(60)
