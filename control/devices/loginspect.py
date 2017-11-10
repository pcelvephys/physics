#!/usr/bin/python

def datetimefromircline(line):
    """Assuming format 'yyyy-dd-mm hh:mm:ss ...', return datetime object"""
    from datetime import datetime
    string = line[:19]
    return datetime.strptime(string, '%Y-%m-%d %H:%M:%S')

def extractlines(author, startdatetime='2000-01-01 00:00:00', enddatetime='2099-12-31 23:59:59', logpath = '/home/lab/optomech/logs/Optomech/', logmask = '#logging.????-??-??.log'):
    """Extract lines from the IRC logs which were sent by the specified author and fall within the given date-time range"""

    # convert specified datetime range to a datetime object (for later comparison)
    def makedatetimeobj(string):
        """Make a datetime object, assuming format 'yyyy-mm-dd hh:mm:ss'"""
        from datetime import datetime
        return datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
    datetimerange = list(map(makedatetimeobj, [startdatetime, enddatetime]))

    # make a list of all log files
    from glob import glob
    logfiles = glob(logpath + logmask)

    # find all log files in the given date range
    def logfiledate(logfile):
        """Extracts date from specified filename, which is assumed to end thus: '...yyyy-mm-dd.log'"""
        from datetime import date
        return date(*list(map(int,logfile[logfile.index('.'):][1:11].split('-'))))
    filterlogfiles = list(filter(lambda d: datetimerange[0].date()<=logfiledate(d) and logfiledate(d)<=datetimerange[1].date(), logfiles))
    filterlogfiles.sort()

    # load log files in the given range, inject date (from filename) before time at start of each line, and keep only those for the specified author
    import re
    linesfromspecifiedauthor = []
    for filename in filterlogfiles:
        date = filename[filename.index('.'):][1:11]
        with open(filename) as h:
            lines = [date + ' ' + line for line in h.readlines()]
        linesfromspecifiedauthor.extend(filter(lambda line: re.search("^\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d\< %s\>" % author, line), lines))
    linesfromspecifiedauthor.sort() # sorts by timestamp because this is as the start of the line

    # return only those lines in the specified datetime range
    return list(filter(lambda l: datetimerange[0]<=datetimefromircline(l) and datetimefromircline(l)<=datetimerange[1], linesfromspecifiedauthor))

def edwards(lines):
    """Extract information for the Edwards scroll pump"""
    def getFloatParam(symbol,line):
        import re
        m = re.search(symbol + ' =\s+(?P<x>\d+\.\d+)', line)
        return float(m.groupdict()['x'])
    keys = 'T', 'V', 'I', 'P'
    data = {key:list(map(lambda l: getFloatParam(key, l), lines)) for key in keys}
    data['datetime'] = list(map(datetimefromircline, lines))
    return data

# import loginspect
# lines = loginspect.extractlines('edwards', startdatetime='2016-10-01 00:00:00')
# data = loginspect.edwards(lines)
# p.plot(data['datetime'],data['P'])
# p.show()

def thermocouples(lines):
    """Extract information for the thermocouples"""
    def extract(line):
        """For format 't/c D: 24 deg C', return ('D','24')"""
        import re
        m = re.search('t/c (?P<label>\w+): (?P<value>\d+) deg C', line)
        if m is not None:
            d = m.groupdict()
            return (d['label'], d['value'])
        else:
            return None
    keys = 'A', 'B', 'C', 'D'
    data = {key: {'datetime': [], 'value': []} for key in keys}
    for line in lines:
            datetime = datetimefromircline(line)
            try:
                (label, value) = extract(line)
                data[label]['datetime'].append(datetime)
                data[label]['value'].append(value)
            except TypeError:
                pass
    return data

# import loginspect
# lines = loginspect.extractlines('thermocouples')
# data = loginspect.thermocouples(lines)
# for x in data.keys():
#     p.plot(data[x]['datetime'], data[x]['value'], label=x)
# p.legend()
# p.show()
# history

def pressure(lines):
    """Extract information for the pressure logs"""
    def extract(line):
        """For format 'Pressure is 4.0156e-06 mBar', return float(4.0156e-06)"""
        N = line.index('Pressure is ')
        return float(line[N+12:].split(' ')[0])
    data = dict()
    data['pressure'] = list(map(extract, lines))
    data['datetime'] = list(map(datetimefromircline, lines))
    return data

def power(lines):
    """Extract information for the power logs"""
    def extract(line):
        """For format 'Power is 55.12 mW', return float(55.12*1e-3)"""
        
        N = line.index('Power is ')
        #print(N)
        #print(line[N:])
        num = float(line[N+9:].split(' ')[0])
        unit = line[N+9:].split(' ')[1]
        if unit == "mW":
            scaling = 1e-3
        elif unit == "uW":
            scaling = 1e-6
        elif unit == "nW":
            scaling = 1e-9
        power_val = num*scaling

        return power_val

    data = dict()
    data['power'] = list(map(extract, lines))
    data['datetime'] = list(map(datetimefromircline, lines))
    return data
# import loginspect
# lines = loginspect.extractlines('pressure', startdatetime='2016-10-01 00:00:00')
# data = loginspect.pressure(lines)
# import pylab as p
# p.plot(data['datetime'], data['pressure'])
# p.yscale('log')
# p.show()
