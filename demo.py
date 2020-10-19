#!/usr/bin/python

from picamera import PiCamera
from time import sleep
from fractions import Fraction

with PiCamera() as camera:
  camera.framerate = 2.5
  camera.shutter_speed = 400000
  sleep(30) # Camera warm-up time
    for i, filename in enumerate(camera.capture_continuous('/data/image{counter:02d}.jpg')):
      print('Captured %s' % filename)
        #sleep(1)
        if i >= 59:
          break

print('Pictures taken')
time.sleep(10)
