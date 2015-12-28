'''
Created on Dec 25, 2015

@author: nikola
'''
import wiringpi2 as wiringpi


class Expanderi:
    def __init__(self):
        self.pins1 = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]
        self.pins2 = [81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96]
        self.pins3 = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112]
        self.pins4 = [113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128]
        
        self.pins5 = [129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144]
        self.pins6 = [145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160]  
        
        self.svi = []
        self.svi =self.svi+ self.pins1 
        self.svi =self.svi+ self.pins2 
        self.svi =self.svi+ self.pins3 
        self.svi =self.svi+ self.pins4 
        self.svi =self.svi+ self.pins5 
        self.svi =self.svi+ self.pins6 
        
        wiringpi.wiringPiSetup()
        wiringpi.mcp23s17Setup(65,0,0) # first pin,spi port,i2c address
        wiringpi.mcp23s17Setup(81,0,1)
        wiringpi.mcp23s17Setup(97,0,2)
        wiringpi.mcp23s17Setup(113,0,3)

        for i in self.svi:
            wiringpi.pinMode(int(i),1)     # sets pin of mcp23s17-0 to output
             
    def ukljuci(self, port):            
        wiringpi.digitalWrite(self.svi[port],1)    
    def iskljuci(self, port):            
        wiringpi.digitalWrite(self.svi[port],0)       
        
    def close(self):
        for i in self.svi:   
            wiringpi.digitalWrite(i,0)
            wiringpi.pinMode(i,0)    
            pass
                