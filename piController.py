# Importeren van enumeration 
from enum import Enum

# Enum class State met states geordend op prioriteit
class State(Enum):
	IDLE = 0
	DRIVING = 1
	INQUESTION = 2
	ANSWERINGQUESTION = 3
	FINISHED = 4

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
	def update():
		### Game Logic ###
		if self.curState == State.IDLE:
			resetGame()
			changePiCarAllowance(False)
			## If joystick is touched or button is pressed
				## Switch to DRIVING mode##
		elif self.curState == State.DRIVING:
			changePiCarAllowance(True)
			## Lampje moet branden en er kan gereden worden ##
			## Als er over de juiste drempel gereden wordt ##
				## Switch naar INQUESTION mode ##
		elif self.curState == State.INQUESTION:
			changePiCarAllowance(False)
			## Hier wordt de vraag fysiek gesteld (B is altijd goed!) ##

			## If B is pressed
				## updateScore(True)
			## elif A or C is pressed
				## updateScore(False)
				## 7 second display updaten ##
			## Naar answering mode ##
		elif self.curState == State.ANSWERINGQUESTION:
			## if curQuestionCount == amountOfQuestions go to FINISHED state
				## elif go to Driving mode
		elif self.curState == State.FINISHED:
			## Alle lampjes laten flikkeren voor 10 seconden
			## Go to IDLE state

		### Connectie naar piCar ###
		if self.piCarIsAllowedToDrive:
			## --> piCar.move(direction) ##

	# Verander de current State
	# @param {State} [state]
	def changeState(self,state):
		self.curState = state

	# Reset van game door attributen naar het origineel te veranderen
	def resetGame():
		print('Resetting game')
		self.curQuestionCount = 0
		self.score = 0

	# Veranderen of de auto mag rijden
	# @param {boolean} [allowance]
	def changePiCarAllowance(self,allowance)
		self.piCarIsAllowedToDrive = allowance

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