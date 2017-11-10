#!/usr/bin/python

def setEDFA(SPCmW=5000, allowDrop=False):
    print("Setting to %u mW" % SPCmW)
    if SPCmW < 1000:
        if allowDrop is False:
            raise Exception('Tried to drop particle! Low power setting not allowed!')

    from subprocess import check_output
    cmd = 'curl --data "SPCmW=%u&SMODE=PC" http://192.168.0.106:8080/' % SPCmW
    print cmd
    check_output(cmd, shell=True)

def getraw(SPCmW):
    import LeCroy
    import time

    path = "/home/lab/optomech" #raw_input("Where is server mounted? ")
    filename = "%s/data/ramp-heterodyne-raw/%s-%05umW.raw" % (path, time.strftime("%Y-%m-%d_%H-%M-%S"), SPCmW)
    print("Will save to %s" % filename)

    scope = LeCroy.WS3024()

    print("Telling scope to take a single trace")
    scope.write('ARM_ACQUISITION')
    scope.write('*TRG')

    print("Wait a second...")
    time.sleep(10)
    try:
        scope.waitOPC()
    except:
        print("waitOPC timed out; retrying...")
        time.sleep(10)
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

if __name__=='__main__':
    from time import sleep
    SPCmWrange = range(5000,1000,-100)

    for SPCmW in SPCmWrange:
        setEDFA(SPCmW)
        sleep(10)
        for n in range(5):
            getraw(SPCmW)
            sleep(10)

    for SPCmW in SPCmWrange[::-1]:
        setEDFA(SPCmW)
        sleep(10)
        for n in range(5):
            getraw(SPCmW)
            sleep(10)

