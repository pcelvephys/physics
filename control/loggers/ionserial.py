#!/usr/bin/python
import irc
from BKtel import HPOA
from time import sleep, time

amp = HPOA()

irclog = irc.irc('EDFA', 'EDFA', 'EDFA')
irclog.login()
irclog.join('#logging')

while True:
        powers = amp.RPM()
        mode = amp.RMODE()
        P_aim = amp.RPC()
        T_int = amp.RIT()
        V_in = amp.RV()
        currents = amp.RLC()
        I_aim = amp.RCC()
        alarms = amp.RA()
        message = "// ALARMS: %s \\\, Mode: %s, P_in: %g mw, P_out: %g mw, P_aim: %g mW, T_int: %g C, V_in: %g V, I_pre: %g mA, I_amp: %g mA, I_aim_pre: %g, I_aim_amp: %g" % (" ".join(alarms), mode, powers[2], powers[3], P_aim[1], T_int, V_in, currents[0], currents[1], I_aim[0], I_aim[1])
        print message
        irclog.privmsg('#logging', message)

        endTime = time() + 10
        while time() < endTime:
                lines = irclog.read()
                for line in lines:
                        try:
                                msg = irclog.extractPrivmsg(line)
                        except:
                                break
                        if msg['message'].startswith('EDFA ') and msg['nick'] != 'EDFA':
                                cmd = msg['message'][5:]
                                irclog.privmsg('#logging', 'EDFA heard: "%s"' % cmd)
                                for response in amp.ask(cmd):
                                        irclog.privmsg('#logging', response)
