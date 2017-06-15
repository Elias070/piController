# Importeren van enumeration 
from enum import Enum

# Importeren van GPIO
import RPi.GPIO as GPIO
import time

# Enum class voor de LED pins voor de Ledematen
# Benummering: pinnummers van de LED's
class LedematenLED(Enum):
	HOOFD = 2
	ROMP_BOVEN = 3
	ROMP_BENEDEN = 4
	ARM = 14
	BEEN = 15

class VragenLED(Enum):
	HOOFD = 10
	ROMP_BOVEN = 9
	ROMP_BENEDEN = 11
	ARM = 19
	BEEN = 25

# GPIO klaarmaken
GPIO.setmode(GPIO.BCM) # BCM
GPIO.setwarnings(False) # Warnings uitschakelen

# Pins opzetten en klaar maken #
for ledPins in LedematenLED:
	GPIO.setup(ledPins.value,GPIO.LOW) # Standaard staan de LED's uit
for vraagPins in VragenLED:
	GPIO.setup(vraagPins.value,GPIO.LOW) # Standaard staan de LED's uit

try:
	print('Testing LEDs')
	while True:
		print('Led HOOFD')
		GPIO.output(LedematenLED.HOOFD.value,GPIO.HIGH)
		GPIO.output(LedematenLED.ROMP_BOVEN.value,GPIO.LOW)
		GPIO.output(LedematenLED.ROMP_BENEDEN.value,GPIO.LOW)
		GPIO.output(LedematenLED.BEEN.value,GPIO.LOW)
		GPIO.output(LedematenLED.ARM.value,GPIO.LOW)
		GPIO.output(VragenLED.HOOFD.value,GPIO.HIGH)
		time.sleep(2)

		print('Led ROMP_BOVEN')
		GPIO.output(LedematenLED.HOOFD.value,GPIO.LOW)
		GPIO.output(LedematenLED.ROMP_BOVEN.value,GPIO.HIGH)
		GPIO.output(LedematenLED.ROMP_BENEDEN.value,GPIO.LOW)
		GPIO.output(LedematenLED.BEEN.value,GPIO.LOW)
		GPIO.output(LedematenLED.ARM.value,GPIO.LOW)
		GPIO.output(VragenLED.ROMP_BOVEN.value,GPIO.HIGH)
		time.sleep(2)

		print('Led ROMP_BENEDEN')
		GPIO.output(LedematenLED.HOOFD.value,GPIO.LOW)
		GPIO.output(LedematenLED.ROMP_BOVEN.value,GPIO.LOW)
		GPIO.output(LedematenLED.ROMP_BENEDEN.value,GPIO.HIGH)
		GPIO.output(LedematenLED.BEEN.value,GPIO.LOW)
		GPIO.output(LedematenLED.ARM.value,GPIO.LOW)
		GPIO.output(VragenLED.ROMP_BENEDEN.value,GPIO.HIGH)
		time.sleep(2)

		print('Led BEEN')
		GPIO.output(LedematenLED.HOOFD.value,GPIO.LOW)
		GPIO.output(LedematenLED.ROMP_BOVEN.value,GPIO.LOW)
		GPIO.output(LedematenLED.ROMP_BENEDEN.value,GPIO.LOW)
		GPIO.output(LedematenLED.BEEN.value,GPIO.HIGH)
		GPIO.output(LedematenLED.ARM.value,GPIO.LOW)
		GPIO.output(VragenLED.BEEN.value,GPIO.HIGH)
		time.sleep(2)

		print('Led ARM')
		GPIO.output(LedematenLED.HOOFD.value,GPIO.LOW)
		GPIO.output(LedematenLED.ROMP_BOVEN.value,GPIO.LOW)
		GPIO.output(LedematenLED.ROMP_BENEDEN.value,GPIO.LOW)
		GPIO.output(LedematenLED.BEEN.value,GPIO.LOW)
		GPIO.output(LedematenLED.ARM.value,GPIO.HIGH)
		GPIO.output(VragenLED.ARM.value,GPIO.HIGH)
		time.sleep(2)

# Stoppen van programma dmv CTRL + C
except KeyboardInterrupt:
	print('Interrupted')