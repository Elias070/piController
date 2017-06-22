# CamJam EduKit 3 - Robotics
# SERVER

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
import socket

# TCP Connectie
HOST='10.0.0.1'
PORT=8015
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr=s.accept()
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
print('Connected by', addr)

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# How many times to turn the pin on and off each second
Frequency = 20
DutyCycle = 30
Stop = 0

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# Set the GPIO Pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)

# Turn all motors off
def StopMotors():
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn both motors forwards
def Forwards():
	pwmMotorAForwards.ChangeDutyCycle(DutyCycle)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycle)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
# Turn both motors backwards
def Backwards():
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycle)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycle)
# Turn left
def Left():
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycle)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycle)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
# Turn Right
def Right():
	pwmMotorAForwards.ChangeDutyCycle(DutyCycle)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycle)

piCarInput = '4'
try:
	StopMotors()
	while True:
		piCarInput = conn.recv(1).decode()

		if piCarInput == '1':
			Forwards()
			print('Forwards')
		elif piCarInput == '2':
			Backwards()
			print('Backwards')
		elif piCarInput == '3':
			Left()
			print('Left')
		elif piCarInput == '4':
			Right()
			print('Right')
		else:
			print('Los gelaten denk ik')
			StopMotors()


except KeyboardInterrupt:
	s.close()
	GPIO.cleanup()