import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

pulse = 0.1

try:
	while True:
		GPIO.output(18, GPIO.HIGH)
		time.sleep(pulse)
		GPIO.output(18, GPIO.LOW)
		time.sleep(pulse)
except:
	GPIO.cleanup() 
