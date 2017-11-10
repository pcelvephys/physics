#!/usr/bin/python
import csv
import time
import matplotlib as mpl
#agg = raw_input("Use mpl.use('Agg')? [y/N]")
#if agg == "y":
mpl.use('Agg')
import pylab as pl
import numpy as np
from scipy.optimize import leastsq
import scipy.fftpack

"""file_number = raw_input("Add file number: ")
number_list = [int(file_number)]
while True:
	file_number = raw_input("Add file number? [y/N] ")
	if file_number != '':
		number_list.append(int(file_number))
	else:
		break
stab = ["Unstabilised", "Python stabilised"]
file_list = []
for i in number_list:
	#path = "/home/chris/Dropbox/Documents/University/Masters/long time PI/"
	#file_list.append(path+'PM_LogData'+str(i)+'.txt')
	#path = "/media/matterwave/2015-03-14_18-50-34/"
	
	
	file_list.append("PM_LogData"+str(i)+".txt")"""
logfile_directory = "/home/chris/"
logfile_name = "templog.txt"
	
file_list = [logfile_directory + logfile_name]
f, tfft = pl.subplots(4,figsize=(24, 36),dpi=1000)

def importing(file_name):
	temps = []
	times= []
	#levels = []
	humids = []
	preses = []
	with open(file_name) as csvfile:
		some_list = csv.reader(csvfile, delimiter = '\t', quotechar='|')
		
		for row in some_list:
			temps.append(float(row[0]))
			times.append(row[2])
			#levels.append(int(row[1]))
			humids.append(row[3])
			preses.append(row[4])
	times = np.linspace(0,len(temps)/60.0,len(temps))
	return (times, temps, humids, preses)
	
			
def plot(times, list, graph):
	
	colour_list = ["red", "blue", "green"]
	label_list = ["Temperature", "Humidity", "Air pressure"]
	
	tfft[graph].plot(times, list, label = label_list[graph], alpha=0.7, color = colour_list[graph])
	ylabel_list = ["Temperature [deg C]", "Humidity [%]", "Air pressure [mBar]"]

	#tfft[graph].plot(times,humids, label = "Humidity", alpha=0.7, color = "blue")
	#tfft[graph].plot(times,preses, label = "Air pressure", alpha=0.7, color = "green")
	#tfft[graph].plot(times, levels, label = "LED level", alpha = 0.7)
	tfft[graph].set_title(label_list[graph]+" over all time")
	tfft[graph].grid()
	tfft[graph].set_xlim(0,max(times))
	tfft[graph].set_xlabel('Time [hr]')
	tfft[graph].set_ylabel(ylabel_list[graph])
	tfft[graph].legend()
	
			
def fftplot(times, temps, humids, preses):			
	#F = scipy.fftpack.fft(temps)
	tfft[3].set_title('Temperature over the last 24 hours') 
	#tfft[graph].plot(times, np.log10((abs(F))**2), label = "Temp", alpha=0.7)
	tfft[3].plot( np.linspace(0,24,1440), temps[-1440:], label = "Temp (last 24h)", alpha=0.7, color = "red")
	#tfft[3].plot( np.linspace(0,24,1440), humids[-1440:], label = "Humidity (last 24h)", alpha=0.7, color = "blue")
	#tfft[3].plot( np.linspace(0,24,1440), preses[-1440:], label = "Air Pressure (last 24h)", alpha=0.7, color = "green")
	tfft[3].set_xlim(0,24)
	#tfft[graph].set_xlabel('Frequency, $\omega$ [Hz]')
	tfft[3].set_xlabel("Time [hr]")
	tfft[3].set_ylabel('Temperature [deg C]')
	tfft[3].grid()
	tfft[3].legend()

	
def main():
	for file in file_list:
		tup = importing(file)
		for graph in range(3):
			plot(tup[0],tup[graph+1],graph)
		fftplot(tup[0], tup[1], tup[2], tup[3])
	"""startTime = time.time()
	stamp = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(startTime))
	save_name = raw_input("Save name: ")
	pl.savefig(save_name+'.png')
	pl.show()"""
	pl.savefig(logfile_directory + "temp_plot.png")
	return 0

if __name__ == '__main__':
	main()

