import LeCroy
from time import sleep

scope = LeCroy.WS3024()

while True:
	output = scope.data()
	print(output[1], output[2])
	sleep(1)
