
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport

NKmotor = QImage() 
NKmotorUkljucen = QImage() 
NKmotor.load("images/motoffdes.png")
NKmotor=NKmotor.scaledToHeight(26, Qt.SmoothTransformation )
NKmotorUkljucen.load("images/motukdes.png")
NKmotorUkljucen=NKmotorUkljucen.scaledToHeight(26, Qt.SmoothTransformation)
      
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
            paint.drawImage(QPoint(self.x,self.y),NKmotorUkljucen)    
        else:
            paint.drawImage(QPoint(self.x,self.y),NKmotor)       
        if(self.senzor == True):
            paint.setBrush(QColor(255, 0, 0))
            paint.setPen(QColor(255, 0, 0))
            paint.drawRect(self.dx,self.dy,9,9)
