# CamJam EduKit 3 - Robotics
# SERVER

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
import socket

# TCP Connectie
HOST='10.0.0.1'
PORT=8013
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr=s.accept()
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
print('Connected by', addr)

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
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

# Turn left
def Left():
	GPIO.output(pinMotorAForwards, 0)
	GPIO.output(pinMotorABackwards, 1)
	GPIO.output(pinMotorBForwards, 1)
	GPIO.output(pinMotorBBackwards, 0)
# Turn Right
def Right():
	GPIO.output(pinMotorAForwards, 1)
	GPIO.output(pinMotorABackwards, 0)
	GPIO.output(pinMotorBForwards, 0)
	GPIO.output(pinMotorBBackwards, 1)	

piCarInput = '4'
try:
	StopMotors()
	while True:
		piCarInput = conn.recv(1024).decode()
		inputArr = []
		inputArr.append(piCarInput)
		piCarInput = inputArr[0][0]

		if piCarInput == '0':
			Forwards()
			print('Forwards')

		if piCarInput == '1':
			Backwards()
			print('Backwards')
		
		if piCarInput == '2':
			Left()
			print('Left')
		
		if piCarInput == '3':
			Right()
			print('Right')
		
		if piCarInput == '4':
			print('Los gelaten denk ik')
			StopMotors()

except KeyboardInterrupt:
	s.close()
	GPIO.cleanup()