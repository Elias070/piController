# CamJam EduKit 3 - Robotics

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
import sys, termios, tty, os

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

inputCarForwards = 26
inputCarBackwards = 21
inputCarLeft = 16
inputCarRight = 20

GPIO.setup(inputCarForwards, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(inputCarBackwards, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(inputCarLeft, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(inputCarRight, GPIO.IN,pull_up_down=GPIO.PUD_UP)

# Set the GPIO Pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Turn all motors off
def StopMotors():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)

# Turn both motors forwards
def Forwards():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

# Turn both motors backwards
def Backwards():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

def Left():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

def Right():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

StopMotors()

button_delay = 0

try:
    while True:

        if (GPIO.input(inputCarLeft) == 0):
            print ('Left pressed')
            Left()
            time.sleep(button_delay)

        if (GPIO.input(inputCarRight) == 0):
            print ('Right pressed')
            Right()
            time.sleep(button_delay)          

        elif (GPIO.input(inputCarForwards) == 0):
            print ('Up pressed') 
            Forwards()       
            time.sleep(button_delay)          
        
        elif (GPIO.input(inputCarBackwards) == 0):
            print ('Down pressed')      
            Backwards()
            time.sleep(button_delay)  
        
        StopMotors()
except KeyboardInterrupt:
    GPIO.cleanup()