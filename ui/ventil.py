
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport


class Ventil():
    

    def __init__(self,x,y):
        self.crna = QColor(0, 0, 0)
        self.crvena = QColor(255, 0, 0)
        self.bela = QColor(255, 255, 255)
        self.ukljuceno = False;
        
        self.points = [QPoint(x, y), QPoint(x+30, y), QPoint(x, y+30), QPoint(x+30, y+30)]
        self.x = x;
        self.y = y;
        self.dx = self.x-28;
        self.dy = self.y+15-25/2;
  
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
        paint.setRenderHint(QPainter.Antialiasing)
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
            paint.drawLine(self.dx+27, self.y+15,self.x+15,self.y+15)
        else:
            paint.setBrush(Qt.red) 
            paint.drawEllipse(self.dx, self.dy, 25, 25)  
            paint.setPen(QPen(Qt.black, 2, Qt.SolidLine))            
            paint.drawLine(self.dx+27, self.y+15,self.x+15,self.y+15)            