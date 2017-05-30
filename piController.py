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
		self.amountOfQuestions = 5 # aantal vragen
		self.curQuestionCount = 0 # wat de current question is
		self.score = 0 # wat de score is
		self.curState = State.IDLE

	# Verander de current State
	# @param {State} [state]
	def changeState(self,curState):
		self.curState = curState

	# Deze functie wordt elke tick/frame uitgevoerd
	def update():
		if curState == State.IDLE:
			print('in IDLE mode')
			## Scherm op Idle mode zetten ##
			## Reset gamestatus ##
			## Bij beweging naar Driving mode ##
		elif curState == State.DRIVING:
			print('in DRIVING mode')
			## jfc ##
		elif curState == State.INQUESTION:
			print('in INQUESTION mode')
			## Alles op stop, vraag wordt gesteld ##
			## Naar answering mode ##
		elif curState == State.ANSWERINGQUESTION:
			print('in ANSWERINGQUESTION mode')
			## Wanneer er op knop gedrukt wordt checken of antwoord goed is ##
			## 7 second display updaten ##
			## next ##
		elif curState == State.FINISHED:
			print('in FINISHED mode')

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