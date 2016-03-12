
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport


class VentilHor():
    

    def __init__(self,x,y,motor,naziv=''):
        self.crna = QColor(0, 0, 0)
        self.crvena = QColor(255, 0, 0)
        self.bela = QColor(255, 255, 255)
        self.ukljuceno = False;
        self.motor = motor
        #self.points = [QPoint(x, y), QPoint(x+30, y), QPoint(x, y+30), QPoint(x+30, y+30)]
        self.points = [QPoint(x, y), QPoint(x, y+30), QPoint(x+30, y), QPoint(x+30, y+30)]
        self.x = x;
        self.y = y;
        self.dx = self.x+15-25/2;
        self.dy = self.y-28
  
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
        okvir = QRect(self.x,self.y,30,30)
        okvir2 = QRect(self.x+15-12,self.y-27,25,30)
        
        if(okvir.contains(x,y)==True or okvir2.contains(x,y)==True):
            if(self.ukljuceno==True):
                self.ukljuceno = False;
            else:
                self.ukljuceno = True;
            return True;
        return False 
        
    def nacrtaj(self, paint):
        
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        paint.setPen(pen)
        needle =QPolygon(self.points)  
        if (self.ukljuceno == True):
            paint.setBrush(Qt.green)        
            paint.drawPolygon(needle)
        else: 
            paint.setBrush(Qt.red) 
            paint.drawPolygon(needle)             
        if (self.senzor == True):
            paint.setBrush(Qt.green) 
            paint.drawEllipse(self.dx, self.dy, 25, 25)
            paint.setPen(QPen(Qt.black, 2, Qt.SolidLine))
            paint.drawLine(self.dx+12, self.y-2,self.dx+12,self.y+15)
        else:
            paint.setBrush(Qt.red) 
            paint.drawEllipse(self.dx, self.dy, 25, 25)  
            paint.setPen(QPen(Qt.black, 2, Qt.SolidLine))            
            paint.drawLine(self.dx+12, self.y-2,self.dx+12,self.y+15)            