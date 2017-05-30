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
		self.curState = State.IDLE
		

	# Verander de current State
	# @param {State} [state]
	def changeState(self,curState):
		self.curState = curState

# Instantiate system
try:
	game = Game()
	print(game.curState)
	game.changeState(State.DRIVING)
	print(game.curState)

except KeyboardInterrupt:
	print('Interrupted')