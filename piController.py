# Importeren van enumeration 
from enum import Enum

# Importeren van GPIO
import RPi.GPIO as GPIO

# Importeren van pygame voor audio afspelen
import pygame
import time
import numpy as np

# Enum class State met states geordend op prioriteit
# Benummering: volgorde van prioriteit
class State(Enum):
	IDLE = 0
	DRIVING = 1
	INQUESTION = 2
	ANSWERINGQUESTION = 3
	FINISHED = 4

# Enum class voor de LED pins voor de Ledematen
# Benummering: pinnummers van de LED's
class LedematenLED(Enum):
	HOOFD = 2
	ROMP_BOVEN = 4
	ROMP_BENEDEN = 14
	ARM = 3
	BEEN = 15

# Enum class voor de lichtsensor pins voor de Ledematen
# Benummering: Pins van de Lichtsensor
class LedematenLS(Enum):
	HOOFD = 17
	ROMP_BOVEN = 27
	ROMP_BENEDEN = 18
	ARM = 22
	BEEN = 23

# Enum class voor de Arcaderichtingen
# Benummering: Pins van de Arcadestick
class ArcadeStick(Enum):
	FORWARD = 12
	BACKWARD = 6
	LEFT = 13
	RIGHT = 5

# Enum class voor RGB Leds
class vraagRGB(Enum):
	HOOFD_GOED = 25
	HOOFD_FOUT = 7
	ROMP_BOVEN_GOED = 8
	ROMP_BOVEN_FOUT = 9
	ARM_GOED = 10
	ARM_FOUT = 11
	ROMP_BENEDEN_GOED = 19
	ROMP_BENEDEN_FOUT = 21
	BEEN_GOED = 24
	BEEN_FOUT = 24

# Overige attributen met pinnummers
buttonAPin = 20
buttonBPin = 16
buttonCPin = 26

# GPIO klaarmaken
GPIO.setmode(GPIO.BCM) # BCM
GPIO.setwarnings(False) # Warnings uitschakelen

# Pins opzetten en klaar maken #
for ledPins in LedematenLED:
	GPIO.setup(ledPins.value,GPIO.LOW) # Standaard staan de LED's uit

for LSPins in LedematenLS:
	GPIO.setup(LSPins.value,GPIO.IN) # Standaard staan de LS's uit

for arcadePins in ArcadeStick:
	GPIO.setup(arcadePins.value,GPIO.IN,pull_up_down=GPIO.PUD_UP)

for rgbLed in vraagRGB:
	GPIO.setup(rgbLed.value,GPIO.LOW) # Standaard staan de LED's uit

GPIO.setup(buttonAPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonBPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonCPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

# Game class
class Game(object):
	# Constructor -- Wordt aangeroepen als er een gameobject aangemaakt wordt
	def __init__(self):
		print('Initiating Gameobject')
		# Defining (global) variables
		self.amountOfQuestions = 5 # Aantal vragen
		self.currentQuestion = 0 # Wat de current question is
		self.curState = State.IDLE # Wat de current state is
		self.piCarIsAllowedToDrive = False # Of de piCar mag rijden default is false want status is IDLE

	# Deze functie wordt elke tick/frame uitgevoerd
	def update(self):
		buttonAVal = GPIO.input(buttonAPin)
		buttonBVal = GPIO.input(buttonBPin)
		buttonCVal = GPIO.input(buttonCPin)

		arcadeFVal = GPIO.input(ArcadeStick.FORWARD.value)
		arcadeBVal = GPIO.input(ArcadeStick.BACKWARD.value)
		arcadeLVal = GPIO.input(ArcadeStick.LEFT.value)
		arcadeRVal = GPIO.input(ArcadeStick.RIGHT.value)

		if self.curState == State.IDLE:
			self.resetGame() # !!! Deze functie wordt constant aangeroepen !!!

			## Als een van de buttons of Joysticks aangeraakt worden
			if buttonAVal == False or buttonBVal == False or buttonCVal == False:
				print('Button pressed, starting game!')
				self.changeState(State.DRIVING)
			if arcadeFVal == False or arcadeBVal == False or arcadeLVal == False or arcadeRVal == False:
				print('Arcade stick touched, starting game!')
				self.changeState(State.DRIVING)

			# Flikkeren van lampjes -- grappig geluidje afspelen
			self.ledFlikker()
			time.sleep(0.2)

		elif self.curState == State.DRIVING:
			# Auto mag rijden
			self.changePiCarAllowance(True)

			# Printen dat eerste vraag begint
			if self.currentQuestion == 0:
				print('Eerste vraag start')

			# Current Question verhogen naar 1, als het 0 is, ook toepasselijk
			self.currentQuestion = self.currentQuestion + 1
			print('start vraag')
			print(self.currentQuestion)

			while True:
				# vraag 1: Hoofd B
				# vraag 2: Romp boven B
				# vraag 3: Arm A
				# vraag 4: Romp beneden B
				# vraag 5: Been B
				if self.currentQuestion == 1:
					GPIO.output(LedematenLED.HOOFD.value,GPIO.HIGH) # Hoofd aan, rest uit
					GPIO.output(LedematenLED.ROMP_BOVEN.value,GPIO.LOW)
					GPIO.output(LedematenLED.ARM.value,GPIO.LOW)
					GPIO.output(LedematenLED.ROMP_BENEDEN.value,GPIO.LOW)
					GPIO.output(LedematenLED.BEEN.value,GPIO.LOW)

					if GPIO.input(LedematenLS.HOOFD.value) == 1:
						print('Bij vraag 1 gearriveerd')
						self.changeState(State.INQUESTION)
						self.turnOffAllLeds()
						break

				if self.currentQuestion == 2:
					print('looking for rompboven sensor')
					GPIO.output(LedematenLED.HOOFD.value,GPIO.LOW)
					GPIO.output(LedematenLED.ROMP_BOVEN.value,GPIO.HIGH)
					GPIO.output(LedematenLED.ARM.value,GPIO.LOW)
					GPIO.output(LedematenLED.ROMP_BENEDEN.value,GPIO.LOW)
					GPIO.output(LedematenLED.BEEN.value,GPIO.LOW)

					if GPIO.input(LedematenLS.ROMP_BOVEN.value) == 1:
						print('Bij vraag 2 gearriveerd')
						self.changeState(State.INQUESTION)
						self.turnOffAllLeds()
						break

				if self.currentQuestion == 3:
					GPIO.output(LedematenLED.HOOFD.value,GPIO.LOW)
					GPIO.output(LedematenLED.ROMP_BOVEN.value,GPIO.LOW)
					GPIO.output(LedematenLED.ARM.value,GPIO.HIGH)
					GPIO.output(LedematenLED.ROMP_BENEDEN.value,GPIO.LOW)
					GPIO.output(LedematenLED.BEEN.value,GPIO.LOW)

					if GPIO.input(LedematenLS.ARM.value) == 1:
						print('Bij vraag 3 gearriveerd')
						self.changeState(State.INQUESTION)
						self.turnOffAllLeds()
						break

				if self.currentQuestion == 4:
					GPIO.output(LedematenLED.HOOFD.value,GPIO.LOW)
					GPIO.output(LedematenLED.ROMP_BOVEN.value,GPIO.LOW)
					GPIO.output(LedematenLED.ARM.value,GPIO.LOW)
					GPIO.output(LedematenLED.ROMP_BENEDEN.value,GPIO.HIGH)
					GPIO.output(LedematenLED.BEEN.value,GPIO.LOW)

					if GPIO.input(LedematenLS.ROMP_BENEDEN.value) == 1:
						print('Bij vraag 4 gearriveerd')
						self.changeState(State.INQUESTION)
						self.turnOffAllLeds()
						break

				if self.currentQuestion == 5:
					GPIO.output(LedematenLED.HOOFD.value,GPIO.LOW)
					GPIO.output(LedematenLED.ROMP_BOVEN.value,GPIO.LOW)
					GPIO.output(LedematenLED.ARM.value,GPIO.LOW)
					GPIO.output(LedematenLED.ROMP_BENEDEN.value,GPIO.LOW)
					GPIO.output(LedematenLED.BEEN.value,GPIO.HIGH)

					if GPIO.input(LedematenLS.BEEN.value) == 1:
						print('Bij vraag 5 gearriveerd')
						self.changeState(State.INQUESTION)
						self.turnOffAllLeds()
						break

		elif self.curState == State.INQUESTION:
			print('Inquestion: Start afspelen van vraag')
			self.changePiCarAllowance(False)
			if self.currentQuestion == 1:
				# Speel info file 
				pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
				pygame.mixer.music.load("audio/vraag1info.mpeg")
				pygame.mixer.music.play()		
				while pygame.mixer.music.get_busy() == True:
					continue
				pygame.mixer.quit()

				# Vervolgens vraag file
				pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
				pygame.mixer.music.load("audio/vraag1.mpeg")
				pygame.mixer.music.play()		
				while pygame.mixer.music.get_busy() == True:
					continue
				pygame.mixer.quit()

				# Wachten en voorkomen dat de audio files heletijd afgespeeld wordt
				while True:
					print('waiting on button')
					self.updateControlsInput()
					buttonAVal = GPIO.input(buttonAPin)
					buttonBVal = GPIO.input(buttonBPin)
					buttonCVal = GPIO.input(buttonCPin)

					arcadeFVal = GPIO.input(ArcadeStick.FORWARD.value)
					arcadeBVal = GPIO.input(ArcadeStick.BACKWARD.value)
					arcadeLVal = GPIO.input(ArcadeStick.LEFT.value)
					arcadeRVal = GPIO.input(ArcadeStick.RIGHT.value)

					# Checken of er A, B of C gedrukt wordt en daarna beplen of het correct is
					if buttonAVal == False or buttonCVal == False:
						print('fout')
						pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
						pygame.mixer.music.load("audio/fout.mp3")
						pygame.mixer.music.play()		
						while pygame.mixer.music.get_busy() == True:
							continue
						pygame.mixer.quit()

						pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
						pygame.mixer.music.load("audio/fout_loes.mpeg")
						pygame.mixer.music.play()		
						while pygame.mixer.music.get_busy() == True:
							continue
						pygame.mixer.quit()
						## RGB ROOD AAN VAN vraagRGB.HOOFD ##
						GPIO.output(vraagRGB.HOOFD_FOUT.value,GPIO.HIGH)
						

					if buttonBVal == False:
						print('goed')
						pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
						pygame.mixer.music.load("audio/goed.mp3")
						pygame.mixer.music.play()		
						while pygame.mixer.music.get_busy() == True:
							continue
						pygame.mixer.quit()
						GPIO.output(vraagRGB.HOOFD_GOED.value,GPIO.HIGH)
						# Naar answering mode om keuze te maken
						self.changeState(State.ANSWERINGQUESTION)
						break

			if self.currentQuestion == 2:
				# Speel info file 
				pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
				pygame.mixer.music.load("audio/vraag2info.mpeg")
				pygame.mixer.music.play()		
				while pygame.mixer.music.get_busy() == True:
					continue
				pygame.mixer.quit()

				# Vervolgens vraag file
				pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
				pygame.mixer.music.load("audio/vraag2.mpeg")
				pygame.mixer.music.play()		
				while pygame.mixer.music.get_busy() == True:
					continue
				pygame.mixer.quit()

				# Wachten en voorkomen dat de audio files heletijd afgespeeld wordt
				while True:
					buttonAVal = GPIO.input(buttonAPin)
					buttonBVal = GPIO.input(buttonBPin)
					buttonCVal = GPIO.input(buttonCPin)

					arcadeFVal = GPIO.input(ArcadeStick.FORWARD.value)
					arcadeBVal = GPIO.input(ArcadeStick.BACKWARD.value)
					arcadeLVal = GPIO.input(ArcadeStick.LEFT.value)
					arcadeRVal = GPIO.input(ArcadeStick.RIGHT.value)
					print('Waiting for button press')
					# Checken of er A, B of C gedrukt wordt en daarna beplen of het correct is
					if buttonAVal == False or buttonCVal == False:
						pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
						pygame.mixer.music.load("audio/fout.mp3")
						pygame.mixer.music.play()		
						while pygame.mixer.music.get_busy() == True:
							continue
						pygame.mixer.quit()

						pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
						pygame.mixer.music.load("audio/fout_loes.mpeg")
						pygame.mixer.music.play()		
						while pygame.mixer.music.get_busy() == True:
							continue
						pygame.mixer.quit()

						GPIO.output(vraagRGB.ROMP_BOVEN_FOUT.value,GPIO.HIGH)

					if buttonBVal == False:
						pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
						pygame.mixer.music.load("audio/goed.mp3")
						pygame.mixer.music.play()		
						while pygame.mixer.music.get_busy() == True:
							continue
						pygame.mixer.quit()
						GPIO.output(vraagRGB.ROMP_BOVEN_GOED.value,GPIO.HIGH)
						# Naar answering mode om keuze te maken
						self.changeState(State.ANSWERINGQUESTION)
						break

			if self.currentQuestion == 3:
				# Speel info file 
				pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
				pygame.mixer.music.load("audio/vraag3info.mpeg")
				pygame.mixer.music.play()		
				while pygame.mixer.music.get_busy() == True:
					continue
				pygame.mixer.quit()

				# Vervolgens vraag file
				pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
				pygame.mixer.music.load("audio/vraag3.mpeg")
				pygame.mixer.music.play()		
				while pygame.mixer.music.get_busy() == True:
					continue
				pygame.mixer.quit()

				# Wachten en voorkomen dat de audio files heletijd afgespeeld wordt
				while True:
					buttonAVal = GPIO.input(buttonAPin)
					buttonBVal = GPIO.input(buttonBPin)
					buttonCVal = GPIO.input(buttonCPin)

					arcadeFVal = GPIO.input(ArcadeStick.FORWARD.value)
					arcadeBVal = GPIO.input(ArcadeStick.BACKWARD.value)
					arcadeLVal = GPIO.input(ArcadeStick.LEFT.value)
					arcadeRVal = GPIO.input(ArcadeStick.RIGHT.value)
					print('Waiting for button press')
					# Checken of er A, B of C gedrukt wordt en daarna beplen of het correct is
					if buttonBVal == False or buttonCVal == False:
						pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
						pygame.mixer.music.load("audio/fout.mp3")
						pygame.mixer.music.play()		
						while pygame.mixer.music.get_busy() == True:
							continue
						pygame.mixer.quit()

						pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
						pygame.mixer.music.load("audio/fout_loes.mpeg")
						pygame.mixer.music.play()		
						while pygame.mixer.music.get_busy() == True:
							continue
						pygame.mixer.quit()

						## RGB ROOD AAN VAN vraagRGB.HOOFD ##
						GPIO.output(vraagRGB.ARM_FOUT.value,GPIO.HIGH)

					if buttonAVal == False:
						pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
						pygame.mixer.music.load("audio/goed.mp3")
						pygame.mixer.music.play()		
						while pygame.mixer.music.get_busy() == True:
							continue
						pygame.mixer.quit()
						GPIO.output(vraagRGB.ARM_GOED.value,GPIO.HIGH)
						# Naar answering mode om keuze te maken
						self.changeState(State.ANSWERINGQUESTION)
						break

			if self.currentQuestion == 4:
				# Speel info file 
				pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
				pygame.mixer.music.load("audio/vraag4info.mpeg")
				pygame.mixer.music.play()		
				while pygame.mixer.music.get_busy() == True:
					continue
				pygame.mixer.quit()

				# Vervolgens vraag file
				pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
				pygame.mixer.music.load("audio/vraag4.mpeg")
				pygame.mixer.music.play()		
				while pygame.mixer.music.get_busy() == True:
					continue
				pygame.mixer.quit()

				# Wachten en voorkomen dat de audio files heletijd afgespeeld wordt
				while True:
					buttonAVal = GPIO.input(buttonAPin)
					buttonBVal = GPIO.input(buttonBPin)
					buttonCVal = GPIO.input(buttonCPin)

					arcadeFVal = GPIO.input(ArcadeStick.FORWARD.value)
					arcadeBVal = GPIO.input(ArcadeStick.BACKWARD.value)
					arcadeLVal = GPIO.input(ArcadeStick.LEFT.value)
					arcadeRVal = GPIO.input(ArcadeStick.RIGHT.value)
					print('Waiting for button press')
					# Checken of er A, B of C gedrukt wordt en daarna beplen of het correct is
					if buttonAVal == False or buttonCVal == False:
						pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
						pygame.mixer.music.load("audio/fout.mp3")
						pygame.mixer.music.play()		
						while pygame.mixer.music.get_busy() == True:
							continue
						pygame.mixer.quit()

						pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
						pygame.mixer.music.load("audio/fout_loes.mpeg")
						pygame.mixer.music.play()		
						while pygame.mixer.music.get_busy() == True:
							continue
						pygame.mixer.quit()

						## RGB ROOD AAN VAN vraagRGB.HOOFD ##
						GPIO.output(vraagRGB.ROMP_BENEDEN_FOUT.value,GPIO.HIGH)

					if buttonBVal == False:
						pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
						pygame.mixer.music.load("audio/goed.mp3")
						pygame.mixer.music.play()		
						while pygame.mixer.music.get_busy() == True:
							continue
						pygame.mixer.quit()
						GPIO.output(vraagRGB.ROMP_BENEDEN_GOED.value,GPIO.HIGH)
						# Naar answering mode om keuze te maken
						self.changeState(State.ANSWERINGQUESTION)
						break

			if self.currentQuestion == 5:
				# Speel info file 
				pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
				pygame.mixer.music.load("audio/vraag5info.mpeg")
				pygame.mixer.music.play()		
				while pygame.mixer.music.get_busy() == True:
					continue
				pygame.mixer.quit()

				# Vervolgens vraag file
				pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
				pygame.mixer.music.load("audio/vraag5.mpeg")
				pygame.mixer.music.play()		
				while pygame.mixer.music.get_busy() == True:
					continue
				pygame.mixer.quit()

				# Wachten en voorkomen dat de audio files heletijd afgespeeld wordt
				while True:
					buttonAVal = GPIO.input(buttonAPin)
					buttonBVal = GPIO.input(buttonBPin)
					buttonCVal = GPIO.input(buttonCPin)

					arcadeFVal = GPIO.input(ArcadeStick.FORWARD.value)
					arcadeBVal = GPIO.input(ArcadeStick.BACKWARD.value)
					arcadeLVal = GPIO.input(ArcadeStick.LEFT.value)
					arcadeRVal = GPIO.input(ArcadeStick.RIGHT.value)
					print('Waiting for button press')
					# Checken of er A, B of C gedrukt wordt en daarna beplen of het correct is
					if buttonAVal == False or buttonCVal == False:
						pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
						pygame.mixer.music.load("audio/fout.mp3")
						pygame.mixer.music.play()		
						while pygame.mixer.music.get_busy() == True:
							continue
						pygame.mixer.quit()

						pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
						pygame.mixer.music.load("audio/fout_loes.mpeg")
						pygame.mixer.music.play()		
						while pygame.mixer.music.get_busy() == True:
							continue
						pygame.mixer.quit()

						## RGB ROOD AAN VAN vraagRGB.HOOFD ##
						GPIO.output(vraagRGB.ROMP_BENEDEN_FOUT.value,GPIO.HIGH)

					if buttonBVal == False:
						pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
						pygame.mixer.music.load("audio/goed.mp3")
						pygame.mixer.music.play()		
						while pygame.mixer.music.get_busy() == True:
							continue
						pygame.mixer.quit()
						GPIO.output(vraagRGB.ROMP_BENEDEN_GOED.value,GPIO.HIGH)
						# Naar answering mode om keuze te maken
						self.changeState(State.ANSWERINGQUESTION)
						break

		elif self.curState == State.ANSWERINGQUESTION:
			print('Making decision...')
			if self.currentQuestion == self.amountOfQuestions:
				print('Laatste vraag beantwoord naar finished')
				self.changeState(State.FINISHED)
			else:
				print('Hoppa naar volgende vraag')
				self.changeState(State.DRIVING)

		elif self.curState == State.FINISHED:
			print('Finished')
			pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
			pygame.mixer.music.load("audio/finale.mpeg")
			pygame.mixer.music.play()		
			while pygame.mixer.music.get_busy() == True:
				continue
			pygame.mixer.quit()
			self.changeState(State.IDLE)

		### Connectie naar piCar ###
		if self.piCarIsAllowedToDrive:
			## Hier checken naar de input van de joystick ###
			if arcadeFVal == False:
				print('send car bluetooth forward')
			if arcadeBVal == False:
				print('send car bluetooth backward')
			if arcadeLVal == False:
				print('send car bluetooth left')
			if arcadeRVal == False:
				print('send car bluetooth right')
				## --> piCar.move(direction) ##

	# Verander de current State
	# @param {State} [state]
	def changeState(self,state):
		self.curState = state

	# Reset van game door attributen naar het origineel te veranderen
	def resetGame(self):
		#print('Resetting game')
		self.changeState(State.IDLE) # Om 100% zeker te zijn
		self.piCarIsAllowedToDrive = False
		self.currentQuestion = 0

	# Veranderen of de auto mag rijden
	# @param {boolean} [allowance]
	def changePiCarAllowance(self,allowance):
		self.piCarIsAllowedToDrive = allowance

	# Uitschakelen van alle LEDs
	def turnOffAllLeds(self):
		GPIO.output(LedematenLED.HOOFD.value,GPIO.LOW)
		GPIO.output(LedematenLED.ROMP_BOVEN.value,GPIO.LOW)
		GPIO.output(LedematenLED.ARM.value,GPIO.LOW)
		GPIO.output(LedematenLED.ROMP_BENEDEN.value,GPIO.LOW)
		GPIO.output(LedematenLED.ARM.value,GPIO.LOW)
	
	def ledFlikker(self):
		if self.randomLed() == 0:
			GPIO.output(LedematenLED.HOOFD.value,GPIO.HIGH)
		else:
			GPIO.output(LedematenLED.HOOFD.value,GPIO.LOW)
		if self.randomLed() == 0:
			GPIO.output(LedematenLED.ROMP_BOVEN.value,GPIO.HIGH)
		else:
			GPIO.output(LedematenLED.ROMP_BOVEN.value,GPIO.LOW)
		if self.randomLed() == 0:
			GPIO.output(LedematenLED.ROMP_BENEDEN.value,GPIO.HIGH)
		else:
			GPIO.output(LedematenLED.ROMP_BENEDEN.value,GPIO.LOW)
		if self.randomLed() == 0:
			GPIO.output(LedematenLED.ARM.value,GPIO.HIGH)
		else:
			GPIO.output(LedematenLED.ARM.value,GPIO.LOW)
		if self.randomLed() == 0:
			GPIO.output(LedematenLED.BEEN.value,GPIO.HIGH)
		else:
			GPIO.output(LedematenLED.BEEN.value,GPIO.LOW)

	def randomLed(self):
		return np.random.choice([0,1])

	def updateControlsInput(self):
		print('updating')
		


# Instantiate system
try:
	# Instantieeren van het game object
	game = Game()
	while True:
		# Voor elke tick/frame de update functie uitvoeren
		game.update()

# Stoppen van programma dmv CTRL + C
except KeyboardInterrupt:
	GPIO.cleanup()
	print('Interrupted')