import wiringpi2 as wiringpi
from time import sleep

wiringpi.wiringPiSetup()                      # initialise wiringpi
wiringpi.mcp23s17Setup(65,0,0)     # set up the pins, spi port, i2c address (mcp23s17-0)

wiringpi.pinMode(68,0)     # sets pin of mcp23s17-0 to input
wiringpi.pullUpDnControl(68, 1) #Pulldown
wiringpi.wiringPiISR(68, INT_EDGE_RISING, my_int)

wiringpi.pinMode(72,1)     # sets pin of mcp23s17-0 to output
wiringpi.digitalWrite(72,0) # sets  pin of mcp23s17-0 to 0 (0V, off)


def my_int():
    print('Receiving...')
    wiringpi.digitalWrite(72,1)
    return True

while True:
    time.sleep(1)
    print('Waiting...')
    wiringpi.wiringPiISR(68, INT_EDGE_RISING, my_int)
    wiringpi.digitalWrite(72,0)
