#!/usr/bin/python
import socket
from time import sleep

class irc:
    def __init__(self, NICK, USER=None, REALNAME=None, HOST="192.168.0.10", PORT=6667, prefix='~/irc'):
        self.HOST = HOST
        self.PORT = PORT
        self.NICK = NICK
        if USER is not None:
            self.USER = USER
        else:
            self.USER = self.NICK
        if REALNAME is not None:
            self.REALNAME = REALNAME
        else:
            self.REALNAME = self.USER

        from subprocess import Popen
        from os.path import join, exists, expanduser
        from time import sleep

        self.path = expanduser(join(prefix, self.NICK))
        self.process = Popen(["ii", "-s", self.HOST, "-i", self.path, "-n", self.NICK, "-f", '"' + self.REALNAME + '"'])
        sleep(10)
        
        with open(join(self.path, self.HOST, "in"), 'w') as h:
            h.write("/j #logging\n")
                
        sleep(5)
        self.readhandle = open(join(self.path, self.HOST, "#logging", "out"), 'r')
        
    def write(self, string):
        from os.path import join
        if not string.endswith("\n"):
            string += "\n"
        with open(join(self.path, self.HOST, "#logging", "in"), 'w') as h:
            h.write(string)
        
    def readlines(self):
        return self.readhandle.readlines()
    
    def readline(self):
        return self.readhandle.readline()

    def close(self):
        try:
            self.readhandle.close()
        except BrokenPipeError:
            pass            
        self.process.kill()
        
if __name__=='__main__':
    NICK = "logbot"
    USER = "loguser"
    REALNAME = "log bot"

    a = irc(NICK, USER, REALNAME)

    #myirc.write("Hello world!")
