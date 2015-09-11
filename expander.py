#!/usr/bin/python
import wiringpi2 as wiringpi
from time import sleep
 
wiringpi.wiringPiSetup()
wiringpi.mcp23s17Setup(65,0,0) # first pin,spi port,i2c address
wiringpi.pinMode(72,1)     # sets pin of mcp23s17-0 to output
 
try:
 while True:
  wiringpi.digitalWrite(72,1) # sets  pin of mcp23s17-0 to 1 (3,3V, on)
  sleep(2)
  wiringpi.digitalWrite(72,0) # sets  pin of mcp23s17-0 to 0 (0V, off)
  sleep(2)
except KeyboardInterrupt:
 wiringpi.digitalWrite(72,0)
 wiringpi.pinMode(72,0)

