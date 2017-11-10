#!/usr/bin/python
from sys import argv

if argv[1] in ["True", "true", "y", "save", "1", "Y", "s", "S", "save"]:
	print("Mode: save")
	save = True
elif argv[1] in ["False", "false", "n", "0", "N", "d", "D", "disp", "display"]:
	print("Mode: display")
	save = False
else:
	print("Invalid save bool argument")
	raise Exception("Enter save bool as argument 1")

filenames = argv[2:]

import matplotlib as mpl



if save == True:
	mpl.use("Agg")

import LeCroy
import pylab as p
from multiprocessing import Pool
from time import time

#save_location = "." #raw_input("Save location [save_loc/date.raw] :\t")

start_time = time()

def raw2psd(filename, save=True):
	fig, ax = p.subplots(figsize=(16,8))
	print('%5u/%5u %s' % (filenames.index(filename),len(filenames),filename))
	with open(filename) as h:
		raw = h.read()

	(WAVEDESC, x, y, i) = LeCroy.InterpretWaveform(raw)

	dt = (x[-1]-x[0])/(len(x)-1)

	Fs=1/dt
	slice = int(-1)
	(A,f) = p.psd(y[:slice],Fs=Fs,NFFT=1<<19)
	p.cla()
	ax.plot(f/1e3, 10*p.log10(A), label=filename)
	ax.set_xlabel('Frequency/kHz')
	ax.set_ylabel('PSD/dB/Hz')
	ax.set_ylim(-140, -40)
	ax.set_xlim(0, 1000)
	p.tight_layout()
	ax.legend()
	ax.grid()
	save_location = "/".join(filename.split("/")[:-1])
	file_date = filename.split("/")[-1][:-4]
	#print("save location: {}".format(save_location))
	#print("file date: {}".format(file_date))
	if save:
		if save_location != "":
			fig.savefig("{}/{}-PSD.pdf".format(save_location, file_date))
			fig.savefig("{}/{}-PSD.png".format(save_location, file_date))
			print("Saved as {}/{}-PSD.pdf".format(save_location, file_date))
		else:
			fig.savefig("{}-PSD.pdf".format(file_date))
			fig.savefig("{}-PSD.png".format(file_date))
			print("Saved as {}-PSD.pdf".format(file_date))
	else:
		print("displaying")
                p.show()
	p.cla()
	ax.plot(f/1e3, 10*p.log10(A), label=filename)
        ax.set_xlabel('Frequency/kHz')
        ax.set_ylabel('PSD/dB/Hz')
        ax.set_ylim(-140, -40)
        ax.set_xlim(250-20, 250+20)
        p.tight_layout()
        ax.legend()
        ax.grid()
        save_location = "/".join(filename.split("/")[:-1])
        file_date = filename.split("/")[-1][:-4]
        #print("save location: {}".format(save_location))
        #print("file date: {}".format(file_date))
        if save == True:
                if save_location != "":
                        fig.savefig("{}/{}-PSD_zoom.pdf".format(save_location, file_date))
                        fig.savefig("{}/{}-PSD_zoom.png".format(save_location, file_date))
                        print("Saved as {}/{}-PSD_zoom.pdf".format(save_location, file_date))
                else:
                        fig.savefig("{}-PSD_zoom.pdf".format(file_date))
                        fig.savefig("{}-PSD_zoom.png".format(file_date))
                        print("Saved as {}-PSD_zoom.pdf".format(file_date))
        else:
                print("displaying_")
                p.show()


	p.close(fig)

	return 0

pool = Pool(8)
psds = pool.map(raw2psd, filenames)

end_time = time()

elap_time = end_time - start_time
#print(start_time)
#print(end_time)
print("Elapsed time: {} seconds".format(elap_time))
