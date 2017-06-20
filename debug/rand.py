# Als de lichtsensor van het hoofd afgaat
# print('Hoofd:')
# print(GPIO.input(LedematenLS.HOOFD.value))
# print('Romp boven:')
# print(GPIO.input(LedematenLS.ROMP_BOVEN.value))
# print('Romp beneden:')
# print(GPIO.input(LedematenLS.ROMP_BENEDEN.value))
# print('Arm:')
# print(GPIO.input(LedematenLS.ARM.value))
# print('Been:')
# print(GPIO.input(LedematenLS.BEEN.value))
# time.sleep(1)

import numpy as np
import RPi.GPIO as GPIO
print(np.random.choice([GPIO.LOW,GPIO.HIGH]))