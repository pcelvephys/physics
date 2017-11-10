import loginspect
import pylab as p


start = raw_input("Start date/time [YYYY-MM-DD]:\t") + " 00:00:00"
logp = raw_input("Enter logpath (blank defaults to /media/optomech/logs/Optomech/):\t")

author = "Pressure"

while True:
	if logp == "":
		try:
			lines = loginspect.extractlines(author, startdatetime=start, logpath = '/media/optomech/logs/Optomech/')
			break
		except:
			print("Invalid entry")
			start = raw_input("Start date/time [YYYY-MM-DD]:\t") + " 00:00:00"
			logp = raw_input("Enter logpath (blank defaults to /media/optomech/logs/Optomech/):\t")
	if logp == "silicon":
                try:
                        lines = loginspect.extractlines(author, startdatetime=start, logpath = '/home/lab/optomech/logs/Optomech/')
                        break
                except:
                        print("Invalid entry")
                        start = raw_input("Start date/time [YYYY-MM-DD]:\t") + " 00:00:00"
                        logp = raw_input("Enter logpath (blank defaults to /media/optomech/logs/Optomech/):\t")
	else:
		try:
			lines = loginspect.extractlines(author, startdatetime=start, logpath = logp)
			break
		except:
			print("Invalid entry")
			start = raw_input("Start date/time [YYYY-MM-DD]:\t") + " 00:00:00"
			logp = raw_input("Enter logpath (blank defaults to /media/optomech/logs/Optomech/):\t")

data = loginspect.pressure(lines)

p.plot(data['datetime'], data['pressure'])
p.yscale('log')
p.xlabel("Date/Time")
p.ylabel("Pressure [mBar]")
p.grid()
p.show()
