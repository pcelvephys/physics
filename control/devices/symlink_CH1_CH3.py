#!/usr/bin/python3
import loginspect

# ###################################################
# Parse command line for start date and log file path
# ###################################################
import argparse
parser = argparse.ArgumentParser(description="Plot path through (Power,Pressure) space",  formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-s", "--start", action="store", dest="start",   help="Start date yyyy-mm-dd")
parser.add_argument("-l", "--log",   action="store", dest="logpath", help="Path to log files", default="/media/optomech/logs/Optomech/")
args = parser.parse_args()

startDate = args.start + " 00:00:00"
logpath   = args.logpath

# ###################################################
# Find times at which data was recorded
# ###################################################
def getFilenameAndPower(line):
    filename, power = line.split("Recorded filename: ")[1].split('at power')
    return filename.strip(), power.strip()
def isValid(line):
    return ("Recorded filename: " in line)
rampLines = loginspect.extractlines("Ramp", startdatetime=startDate, logpath = logpath)
rampLines = list(filter(isValid, rampLines))

def datetimefromfilename(filename):
    """Assuming format '/yyyy-dd-mm_hh-mm-ss-CH', return datetime object"""
    from datetime import datetime
    string = filename.split('timestamped/')[1].split('-CH')[0]
    return datetime.strptime(string, '%Y-%m-%d_%H-%M-%S')

# Collate relevant data and interpolated pressure at point when data was recorded
filenames, powers = zip(*map(getFilenameAndPower, rampLines))
filenames = list(map(lambda f: f.split('/')[-1], filenames))
#datetimes = map(datetimefromfilename, filenames)
datetimes = list(map(loginspect.datetimefromircline, rampLines))
powers = list(map(float, powers))

CH1s = filenames[::2]
CH1d = datetimes[::2]
CH3s = filenames[1::2]
CH3d = datetimes[1::2]

if len(list(filter(lambda f: not "-CH1-" in f, CH1s))) > 0:
    raise Exception("Found a filename which isn't CH1 when it should be")

if len(list(filter(lambda f: not "-CH3-" in f, CH3s))) > 0:
    raise Exception("Found a filename which isn't CH3 when it should be")

if len(CH1s) != len(CH3s):
    raise Exception("Different number of files!")

def delay(n):
    return (CH3d[n]-CH1d[n]).total_seconds()
    
delays = list(map(delay, range(len(CH1s))))

if len(list(filter(lambda t: t > 0.5, delays))) > 0:
    raise Exception("There was a significant delay between some candidate pairs of files being reported to IRC")

filesToSymlink = {CH3s[n]: CH1s[n].replace('-CH1-', '-CH3-') for n in range(len(CH1s))}

import os
cwd = os.getcwd()
for root, dirs, files in os.walk('/media/optomech/data/Tm ratio/raster/'):
    print(root)
    os.chdir(root)
    for f in files:
        try:
            linkname = filesToSymlink.pop(f)
            os.symlink(f, linkname)
            print("%s: linked %s to %s" % (root, f, linkname))
        except KeyError:
            pass
        except FileExistsError:
            pass

os.chdir(cwd)
print("")

print("Did not find the following files:")
print('\n'.join(filesToSymlink.keys()))
