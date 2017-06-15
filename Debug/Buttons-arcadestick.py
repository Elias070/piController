import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

arcadeF = 12
arcadeB = 6
arcadeL = 13
arcadeR = 5
GPIO.setup(arcadeF,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(arcadeB,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(arcadeL,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(arcadeR,GPIO.IN,pull_up_down=GPIO.PUD_UP)

buttonPinA = 20
buttonPinB = 16
buttonPinC = 26
GPIO.setup(buttonPinA,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonPinB,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonPinC,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
		while True:
			valA = GPIO.input(buttonPinA)
			valB = GPIO.input(buttonPinB)
			valC = GPIO.input(buttonPinC)

			valAF = GPIO.input(arcadeF)
			valAB = GPIO.input(arcadeB)
			valAR = GPIO.input(arcadeR)
			valAL = GPIO.input(arcadeL)

			if valA == False:
				print('Button A')
			if valB == False:
				print('Button B')
			if valC == False:
				print('Button C')

			if valAF == False:
				print('Arcade Forward')
			if valAB == False:
				print('Arcade Backward')
			if valAR == False:
				print('Arcade Right')
			if valAL == False:
				print('Arcade Left')

#CTRL + C
except KeyboardInterrupt:
		GPIO.cleanup()