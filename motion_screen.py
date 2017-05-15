#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from datetime import datetime, timedelta
from subprocess import call

MOTION_PIN = 7
SHUTOFF_DELAY = timedelta(minutes=30)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTION_PIN, GPIO.IN,  pull_up_down=GPIO.PUD_UP)

monitor_on = True
last_motion = datetime.now()


while True:
  if (GPIO.input(MOTION_PIN)):
    if monitor_on and datetime.now() > last_motion + SHUTOFF_DELAY:
      call(["vcgencmd", "display_power", "0"])
      monitor_on = False
  else:
    last_motion = datetime.now()
    if not monitor_on:
      call(["vcgencmd", "display_power", "1"])
      monitor_on = True

  time.sleep(0.2)

