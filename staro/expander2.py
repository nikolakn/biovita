#!/usr/bin/python
import wiringpi2 as wiringpi
from time import sleep
 

pins = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]
pins2 = [81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96]

wiringpi.wiringPiSetup()
#rezervise adrese pocevsi od 65 pa nadalje za expander podesen na 0x20
wiringpi.mcp23s17Setup(65,0,0x20) # first pin,spi port,i2c address
#adrese od 81 pa navise za expander na 1
wiringpi.mcp23s17Setup(81,0,0x21) # first pin,spi port,i2c address

for i in pins:
    wiringpi.pinMode(i,1)     # sets pin of mcp23s17-0 to output
for i in pins2:
    wiringpi.pinMode(i,1)
     
try:
 while True:
  for i in pins:   
      wiringpi.digitalWrite(i,1) # sets  pin of mcp23s17-0 to 1 (3,3V, on)
      sleep(0.1) 
      wiringpi.digitalWrite(i,0) # sets  pin of mcp23s17-0 to 0 (0V, off)
      sleep(.1)
  for i in pins2:   
      wiringpi.digitalWrite(i,1) # sets  pin of mcp23s17-0 to 1 (3,3V, on)
      sleep(0.1) 
      wiringpi.digitalWrite(i,0) # sets  pin of mcp23s17-0 to 0 (0V, off)
      sleep(.1)

except KeyboardInterrupt:
 for i in pins:   
     wiringpi.digitalWrite(i,0)
     wiringpi.pinMode(i,0)


