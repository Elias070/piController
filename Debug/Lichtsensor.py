import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

LichtsensorHoofd = 17
LichtsensorArm = 27
LichtsensorRompBoven = 18
LichtsensorRompBeneden = 22
LichtsensorBeen = 23

GPIO.setup(LichtsensorHoofd,GPIO.IN)
GPIO.setup(LichtsensorArm,GPIO.IN)
GPIO.setup(LichtsensorRompBoven,GPIO.IN)
GPIO.setup(LichtsensorRompBeneden,GPIO.IN)
GPIO.setup(LichtsensorBeen,GPIO.IN)

try:
		while True:
			valLS1 = GPIO.input(LichtsensorHoofd)
			valLS2 = GPIO.input(LichtsensorArm)
			valLS3 = GPIO.input(LichtsensorRompBoven)
			valLS4 = GPIO.input(LichtsensorRompBeneden)
			valLS5 = GPIO.input(LichtsensorBeen)
			print(valLS1)
			print(valLS2)
			print(valLS3)
			print(valLS4)
			print(valLS5)

#CTRL + C
except KeyboardInterrupt:
		GPIO.cleanup()