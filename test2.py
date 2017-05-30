# To do:
	# Als er 2 minuten niks gedaan wordt -> Idle mode
	# Game status bijhouden

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
	# Constructor
	def __init__(self):
		# Defining (global) variables
		self.curState = State.IDLE
		print('init')

	# Verander de current State
	# @param {State} [state]
	def changeState(self,curState):
		self.curState = curState

# Instantiate system
try:
	start()
	while True:
		draw()

except KeyboardInterrupt:
	print('Interrupted')

def start():
	game = Game()
	print(game.curState)
	game.changeState(State.DRIVING)
	print(game.curState)

def draw():
