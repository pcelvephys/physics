
from time import time, sleep, strftime
import LeCroy



scope = LeCroy.WS3024(interface="USBTMC", idVendor=0x05ff, idProduct=0x1023)

path = "/media/optomech"
channel=1

while True:
    print("Telling scope to take a single trace")
    scope.write('TRIG_MODE SINGLE')
    sleep(12)
    scope.waitOPC()
    filename = "%s/data/data/timestamped/%s-CH%u.raw" % (path, strftime("%Y-%m-%d_%H-%M-%S"), channel)
    print("Will save to %s" % filename)

    print("Downloading data")
    raw = scope.raw(channel)

    print("Saving...")
    with open(filename, 'wb') as h:
        h.write(raw)

    print("Returning scope to NORMAL trigger")
    scope.write('TRIG_MODE NORMAL')
    sleep(30)

