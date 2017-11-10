#!/usr/bin/python
import irc
from BKtel import HPOA
from time import sleep, time

amp = HPOA()
sleep(2)

irclog = irc.irc('EDFA', 'EDFA', 'BKtel EDFA')


nextReport = time()

while True:
        if time() >= nextReport:
                nextReport = time() + 30

                powers = amp.RPM()
                mode = amp.RMODE()
                P_aim = amp.RPC()
                T_int = amp.RIT()
                V_in = amp.RV()
                currents = amp.RLC()
                I_aim = amp.RCC()
                alarms = amp.RA()
                message = "ALARMS: >{}<, Mode: {}, P_in: {} mw, P_out: {} mw, P_aim: {} mW, T_int: {} C, V_in: {} V, I_pre: {} mA, I_amp: {} mA, I_aim_pre: {}, I_aim_amp: {}".format(" ".join(alarms), mode, powers[2], powers[3], P_aim[1], T_int, V_in, currents[0], currents[1], I_aim[0], I_aim[1])
                print(message)
                irclog.write(message)
        for line in irclog.readlines():
                try:
                        msg = line.strip()
                except:
                        continue
                if '>EDFA ' in msg:
                        cmd = msg.split(">EDFA ")[1]
                        print(cmd)
                        irclog.write('EDFA heard: "%s"' % cmd)
                        for response in amp.ask(cmd):
                                irclog.write(response)
                        nextReport = time()
