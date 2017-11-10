#!/usr/bin/python3
from sys import argv
try:
    nick = argv[1]
except IndexError:
    nick = "WS3024"

import LeCroy
import irc

conn = irc.irc(nick)
scope = LeCroy.WS3024(interface="USBTMC")
conn.write(scope.ask("*IDN?"))

from os.path import join
path = '/media/optomech/data/timestamped/'
import time

_ = conn.readlines()
while True:
    for line in conn.readlines():
        try:
            timestamp = line[:16]
            sender    = line[18:line.index('>')]
            message   = line[line.index('>') + 1:].strip()
        except ValueError:
            continue
        
        if sender != nick: # this message is not from me
            if message.startswith('>' + nick): # this message is to me              
                command = message[len('>' + nick):].strip()
                conn.write(nick + ' heard ' + command)
                if command.startswith("DOWNLOAD"):
                    print(command[8:])
                    channels = [int(c) for c in command[8:].split()]
                    filestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
                    conn.write('Will save channels [' + ','.join([str(c) for c in channels]) + '] to ' + join(path, filestamp + '_CHx.raw'))
                    for channel in channels:
                        conn.write('\tDownloading CH%u' % channel)
                        raw = scope.raw(channel)
                        conn.write('\tSaving CH%u' % channel)
                        filename = join(path, filestamp + '_CH%u' % channel + '.raw')
                        with open(filename, 'wb') as h:
                            h.write(raw)
                        conn.write('\tDone')
                else:
                    if command.endswith('?'):
                        conn.write(scope.ask(command))
                    else:
                        scope.write(command)
                    
