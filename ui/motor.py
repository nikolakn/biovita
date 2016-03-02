
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport

  
class Motor():
    
    def __init__(self,x,y):
        self.crna = QColor(0, 0, 0)
        self.crvena = QColor(255, 0, 0)
        self.bela = QColor(255, 255, 255)
        self.ukljuceno = False;

        self.x = x;
        self.y = y;
        self.dx = self.x+15;
        self.dy = self.y+15;
        self.motor = QImage() 
        self.motorUkljucen = QImage() 
        self.motor.load("images/motor1.png")
        self.motor=self.motor.scaledToHeight(26, Qt.FastTransformation)
        self.motorUkljucen.load("images/motorukljucen.png")
        self.motorUkljucen=self.motorUkljucen.scaledToHeight(26, Qt.FastTransformation)   
        self.senzor = False
    def on(self):
        self.ukljuceno = True;  
    def off(self):
        self.ukljuceno = False; 
    def senzorOn(self):
        self.senzor = True;
    def senzorOff(self):
        self.senzor = False;
    def nacrtaj(self, paint):

        if (self.ukljuceno == True):
            paint.drawImage(QPoint(self.x,self.y),self.motorUkljucen)    
        else:
            paint.drawImage(QPoint(self.x,self.y),self.motor)       
        if(self.senzor == True):
            paint.setBrush(QColor(255, 0, 0))
            paint.setPen(QColor(255, 0, 0))
            paint.drawRect(self.dx,self.dy,9,9)
