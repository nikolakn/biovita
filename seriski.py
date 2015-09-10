#!/usr/bin/python
import RPi.GPIO as GPIO
import serial 
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

def readlineCR(port):
    rv = ""
    p = True
    port.flushInput()
    while True:
        ch = port.read()
        
        if (ch == '\n') and p == False:
            return rv
        if ch == '\n' and p==True:
            p = False
        rv += ch    
try:
  port = serial.Serial("/dev/ttyAMA0",9600)
  port.open()
 
  #time.sleep(1) # allow serial to connect
  
  #port.isOpen()

  for x in range(0,50):
      #Turn LEDs on
      GPIO.output(17,GPIO.HIGH)
      GPIO.output(27,GPIO.LOW)
      time.sleep(0.1)
      rcv = readlineCR(port)
      try:
        r= float(rcv+"\r")
        print(r)
      except:
          pass
      #Turn LEDs off
      GPIO.output(17,GPIO.LOW)
      GPIO.output(27,GPIO.HIGH)
      time.sleep(0.1)
      rc2 = readlineCR(port)
      try:
        r= float(rc2+"\r")
        print(r)
      except:
          pass   
except:
  print("reska seriski port")
  port.close()

port.close()
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
