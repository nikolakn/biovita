
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport


class Ventil():
    

    def __init__(self,x,y,motor,naziv=''):
        self.crna = QColor(0, 0, 0)
        self.crvena = QColor(255, 0, 0)
        self.bela = QColor(255, 255, 255)
        self.ukljuceno = False;
        self.motor = motor       
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
        if(self.senzor==True):
            return False;
        self.senzor = True;
        return True;
    def senzorOff(self):
        if(self.senzor==False):
            return False;         
        self.senzor = False;
        return True;
    def click(self,x,y): 
        okvir = QRect(self.x,self.y,30,30)
        okvir2 = QRect(self.x-27,self.y+15-12,30,25)
        
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
        paint.setRenderHint(QPainter.Antialiasing)
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