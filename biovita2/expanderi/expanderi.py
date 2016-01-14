'''
Created on Dec 25, 2015

@author: nikola
'''
import wiringpi2 as wiringpi


class Expanderi:
    def __init__(self):
        self.output_pins1 = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]
        self.output_pins2 = [81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96]
        self.output_pins3 = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112]
        self.output_pins4 = [113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128]
        
        self.input_pins1 = [129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144]
        self.input_pins2 = [145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160]  
        
        self.led_pins1 = [161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176]  
        
        self.ulazi = []
        for i in range(32):
            self.ulazi.append(0);
        
        
        self.svi = []
        self.svi =self.svi+ self.output_pins1 
        self.svi =self.svi+ self.output_pins2 
        self.svi =self.svi+ self.output_pins3 
        self.svi =self.svi+ self.output_pins4 
        self.svi =self.svi+ self.led_pins1        
        
        self.svi_ulazi = []
        self.svi_ulazi=self.svi+ self.input_pins1 
        self.svi_ulazi =self.svi+ self.input_pins2
        
        
        wiringpi.wiringPiSetup()
        wiringpi.mcp23s17Setup(65,0,0) # first pin,spi port,i2c address
        wiringpi.mcp23s17Setup(81,0,1)
        wiringpi.mcp23s17Setup(97,0,2)
        wiringpi.mcp23s17Setup(113,0,3)
        #ulazi
        wiringpi.mcp23s17Setup(129,1,0)
        wiringpi.mcp23s17Setup(145,1,1)
        #indikatori
        wiringpi.mcp23s17Setup(161,1,2) # za led na drugoj liniji
        
        for i in self.svi:
            wiringpi.pinMode(int(i),1)     # sets pin of mcp23s17-0 to output
        for i in self.svi_ulazi:
            wiringpi.pinMode(int(i),0)    
            
    def getUlazi(self):
        return self.ulazi;
    def proveriUlaze(self):
        n = 0;
        for i in self.svi_ulazi:
            self.ulazi[n] = wiringpi.digitalRead(i);
            n = n + 1;
         
    def ukljuci(self, port):            
        wiringpi.digitalWrite(self.svi[port],1)    
    def iskljuci(self, port):            
        wiringpi.digitalWrite(self.svi[port],0)       
        
    def close(self):
        for i in self.svi:   
            wiringpi.digitalWrite(i,0)
            wiringpi.pinMode(i,0)    
         
                