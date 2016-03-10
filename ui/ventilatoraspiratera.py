
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport


class VentilatorAspiratera():
    

    def __init__(self,x,y,naziv=''):
        self.crna = QColor(0, 0, 0)
        self.crvena = QColor(255, 0, 0)
        self.bela = QColor(255, 255, 255)
        self.ukljuceno = False;
        
 
        self.x = x;
        self.y = y;
        self.senzor = False
        
    def on(self):
        self.ukljuceno = True;  
    def off(self):
        self.ukljuceno = False; 
    def senzorOn(self):
        self.senzor = True;
    def senzorOff(self):
        self.senzor = False;
        
    def click(self,x,y): 
        okvir = QRect(self.x,self.y,102,80)
        
        if(okvir.contains(x,y)==True):
            if(self.ukljuceno==True):
                self.ukljuceno = False;
            else:
                self.ukljuceno = True;
            return True;
        return False  
        
    def nacrtaj(self, paint):

        pen = QPen(Qt.black, 1, Qt.SolidLine)
        paint.setPen(pen)
        
        if (self.ukljuceno == True):
            paint.setBrush(Qt.green) 
            paint.drawEllipse(self.x,self.y,50,50)
            paint.drawRect(self.x,self.y+25,50,25)
        else: 
            paint.setBrush(Qt.gray) 
            paint.drawEllipse(self.x,self.y,50,50)
            paint.drawRect(self.x,self.y+25,50,25)

        if (self.senzor == True):
            paint.setBrush(Qt.green) 
            paint.drawEllipse(self.x+15, self.y+15, 25, 25)

        else:
            paint.setBrush(Qt.red) 
            paint.drawEllipse(self.x+15, self.y+15, 25, 25)  
         