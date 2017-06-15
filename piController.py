# Importeren van enumeration 
from enum import Enum

# Importeren van GPIO
import RPi.GPIO as GPIO

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
	ROMP_BOVEN = 3
	ROMP_BENEDEN = 4
	ARM = 14
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

# Overige attributen met pinnummers
speakerPin = 21
buttonAPin = 20
buttonBPin = 16
buttonCPin = 26

# GPIO klaarmaken
GPIO.setmode(GPIO.BCM) # BCM
GPIO.setwarnings(False) # Warnings uitschakelen

# Pins opzetten en klaar maken #
for ledPins in LedematenLEDPins:
	GPIO.setup(ledPins.value,GPIO.LOW) # Standaard staan de LED's uit

for LSPins in LedematenLSPins:
	print('LS Pins moeten nog opgezet worden')
	# GPIO.setup(LSPins.value,GPIO.LOW) # Standaard staan de LED's uit

GPIO.setup(buttonAPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonBPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonCPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(speakerPin, GPIO.OUT)

# Game class
class Game(object):
	# Constructor -- Wordt aangeroepen als er een gameobject aangemaakt wordt
	def __init__(self):
		print('Initiating Gameobject')
		# Defining (global) variables
		self.amountOfQuestions = 5 # Aantal vragen
		self.curQuestionCount = 0 # Wat de current question is
		self.score = 0 # Wat de current score is
		self.curState = State.IDLE # Wat de current state is
		self.piCarIsAllowedToDrive = False # Of de piCar mag rijden default is false want status is IDLE

	# Deze functie wordt elke tick/frame uitgevoerd
	def update(self):
		### Game Logic ###
		buttonAVal = GPIO.input(buttonAPin)
		buttonBVal = GPIO.input(buttonBPin)
		buttonCVal = GPIO.input(buttonCPin)

		if self.curState == State.IDLE:
			self.resetGame() # !!! Deze functie wordt constant aangeroepen !!!
			## If joystick is touched or button is pressed
				## Switch to DRIVING mode##
		elif self.curState == State.DRIVING:
			self.changePiCarAllowance(True)
			## Lampje moet branden en er kan gereden worden ##
			## Als er over de juiste drempel gereden wordt ##
				## Switch naar INQUESTION mode ##
		elif self.curState == State.INQUESTION:
			self.changePiCarAllowance(False)
			## Hier wordt de vraag fysiek gesteld (B is altijd goed!) ##

			## If B is pressed
				## updateScore(True)
			## elif A or C is pressed
				## updateScore(False)
				## 7 second display updaten ##
			## Naar answering mode ##
		elif self.curState == State.ANSWERINGQUESTION:
			print('c')
			## if curQuestionCount == amountOfQuestions go to FINISHED state
				## elif go to Driving mode
		elif self.curState == State.FINISHED:
			print('c')
			## Alle lampjes laten flikkeren voor 10 seconden
			## Go to IDLE state

		### Connectie naar piCar ###
		if self.piCarIsAllowedToDrive:
			print('c')
			## Hier checken naar de input van de joystick ###
				## --> piCar.move(direction) ##

		# updaten van currentQuestion
		updateDisplay(curQuestionCount)

	# Verander de current State
	# @param {State} [state]
	def changeState(self,state):
		self.curState = state

	# Reset van game door attributen naar het origineel te veranderen
	def resetGame(self):
		#print('Resetting game')
		self.curState = State.IDLE # Om 100% zeker te zijn
		self.piCarIsAllowedToDrive = False
		self.curQuestionCount = 0
		self.score = 0

	# Veranderen of de auto mag rijden
	# @param {boolean} [allowance]
	def changePiCarAllowance(self,allowance):
		self.piCarIsAllowedToDrive = allowance

	# Updaten van currentQuestion
	def updateDisplay(number):
		print('updating 7SD')

# Instantiate system
try:
	# Instantieeren van het game object
	game = Game()
	while True:
		# Voor elke tick/frame de update functie uitvoeren
		game.update()

# Stoppen van programma dmv CTRL + C
except KeyboardInterrupt:
	print('Interrupted')