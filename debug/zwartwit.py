import RPi.GPIO as GPIO #
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

HOOFD = 17
ROMP_BOVEN = 27
ROMP_BENEDEN = 18
ARM = 22
BEEN = 23
GPIO.setup(HOOFD, GPIO.IN)
GPIO.setup(ROMP_BOVEN, GPIO.IN)
GPIO.setup(ROMP_BENEDEN, GPIO.IN)
GPIO.setup(ARM, GPIO.IN)
GPIO.setup(BEEN, GPIO.IN)

try:
	while True:
		if GPIO.input(HOOFD)==1:
			print('Ik zie HOOFD')
		if GPIO.input(ROMP_BOVEN)==1:
			print('Ik zie ROMP_BOVEN')
		if GPIO.input(ROMP_BENEDEN)==1:
			print('Ik zie ROMP_BENEDEN')
		if GPIO.input(ARM)==1:
			print('Ik zie ARM')
		if GPIO.input(BEEN)==1:
			print('Ik zie BEEN')

except KeyboardInterrupt:
	GPIO.cleanup()