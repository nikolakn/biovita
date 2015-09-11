#!/usr/bin/python
import wiringpi2 as wiringpi
from time import sleep
 

pins = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]

wiringpi.wiringPiSetup()
wiringpi.mcp23s17Setup(65,0,0) # first pin,spi port,i2c address
for i in pins:
    wiringpi.pinMode(i,1)     # sets pin of mcp23s17-0 to output
 
try:
 while True:
  for i in pins:   
      wiringpi.digitalWrite(i,1) # sets  pin of mcp23s17-0 to 1 (3,3V, on)
      sleep(1) 
      wiringpi.digitalWrite(i,0) # sets  pin of mcp23s17-0 to 0 (0V, off)
      sleep(1)
except KeyboardInterrupt:
 for i in pins:   
     wiringpi.digitalWrite(i,0)
     wiringpi.pinMode(i,0)

