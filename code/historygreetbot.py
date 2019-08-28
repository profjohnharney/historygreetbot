# First attempt to unify code, I want the PIR to detect motion and then the RPi to generate an event response
# Code here is heavily dependent on work of seesunmoon

import RPi.GPIO as GPIO
import subprocess
from datetime import datetime
import time

import os
file = "file.mp3"

movie_length = 10 # The length of the movie in seconds

GPIO.setmode(GPIO.BOARD)
pir = 7 # Change to your connected GPIO pin
GPIO.setup(pir, GPIO.IN)

print "Sensor initialized at " + str(datetime.now())
time.sleep(3)

print "Detecting motion at " + str(datetime.now())

while True:
    if GPIO.input(pir):
        os.system("omxplayer " + file)
