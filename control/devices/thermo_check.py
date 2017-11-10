import loginspect
import pylab as p


start = raw_input("Start date/time [YYYY-MM-DD]:\t") + " 00:00:00"
logp = raw_input("Enter logpath (blank defaults to /media/optomech/logs/Optomech/):\t")

while True:
    while True:
            if logp == "":
                    try:
                            lines = loginspect.extractlines('thermocouples', startdatetime=start, logpath = '/media/optomech/logs/Optomech/')
                            break
                    except:
                            print("Invalid entry")
                            start = raw_input("Start date/time [YYYY-MM-DD]:\t") + " 00:00:00"
                            logp = raw_input("Enter logpath (blank defaults to /media/optomech/logs/Optomech/):\t")
            if logp == "silicon":
                    try:
                            lines = loginspect.extractlines('thermocouples', startdatetime=start, logpath = '/home/lab/optomech/logs/Optomech/')
                            break
                    except:
                            print("Invalid entry")
                            start = raw_input("Start date/time [YYYY-MM-DD]:\t") + " 00:00:00"
                            logp = raw_input("Enter logpath (blank defaults to /media/optomech/logs/Optomech/):\t")
            else:
                    try:
                            lines = loginspect.extractlines('thermocouples', startdatetime=start, logpath = logp)
                            break
                    except:
                            print("Invalid entry")
                            start = raw_input("Start date/time [YYYY-MM-DD]:\t") + " 00:00:00"
                            logp = raw_input("Enter logpath (blank defaults to /media/optomech/logs/Optomech/):\t")


    data = loginspect.thermocouples(lines)
    p.plot(data['A']['datetime'], data['A']['value'])
    p.plot(data['B']['datetime'], data['B']['value'])
    p.plot(data['C']['datetime'], data['C']['value'])
    p.plot(data['D']['datetime'], data['D']['value'])

    p.xlabel("Date/Time")
    p.ylabel("Temperature [Deg C]")
    p.grid()
    p.show()
