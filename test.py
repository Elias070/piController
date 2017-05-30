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

# Defining (global) variables
curState = State.IDLE

# Veranderd de current State
# @param {State} [state]
def changeState(state):
	global curState
	curState = state

# Instantiate system
try:
	# Start loop
	while True:
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

except KeyboardInterrupt:
	print('Interrupted')