import RPi.GPIO as GPIO #
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinLineFollower = 25
GPIO.setup(pinLineFollower, GPIO.IN)

try:
	while True:
		if GPIO.input(pinLineFollower)==0:
		print('The sensor is seeing a black surface')

		else:
		print('The sensor is seeing a white surface')

		time.sleep(0.2)
except KeyboardInterrupt:
GPIO.cleanup()