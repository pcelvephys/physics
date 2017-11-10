import LeCroy
import time
import numpy as np
import pylab as pl

scope = LeCroy.WS3024()

start_time = time.time()

times = []
means = []

for n in range(10000):
	print(n)
	time_point = time.time()
	data = scope.data(1)
	mean = np.mean(data[2])
	times.append(time_point)
	means.append(mean)
	time.sleep(5)

pl.plot(times, means)
try:
	pl.savefig("/home/lab/server/data/testing_stability_CCS_1.pdf")
except:
	pass
pl.show()
