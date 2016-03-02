
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport

NKmotor = QImage() 
NKmotorUkljucen = QImage() 
NKmotor.load("images/motoffdes.png")
NKmotor=NKmotor.scaledToHeight(26, Qt.SmoothTransformation )
NKmotorUkljucen.load("images/motukdes.png")
NKmotorUkljucen=NKmotorUkljucen.scaledToHeight(26, Qt.SmoothTransformation)


      
class Motor():

    def __init__(self,x,y,rot):
        self.crna = QColor(0, 0, 0)
        self.crvena = QColor(255, 0, 0)
        self.bela = QColor(255, 255, 255)
        self.ukljuceno = False;

        self.x = x;
        self.y = y;
        self.dx = self.x+15;
        self.dy = self.y+15;
        self.rotacija = rot
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
        paint.save()
        if(self.rotacija == 0):
            if (self.ukljuceno == True):
                paint.drawImage(QPoint(self.x,self.y),NKmotorUkljucen)    
            else:
                paint.drawImage(QPoint(self.x,self.y),NKmotor)       
            if(self.senzor == False):
                paint.setBrush(QColor(255, 0, 0))
                paint.setPen(QColor(255, 0, 0))
                paint.drawRect(self.dx,self.dy,9,9)
        if(self.rotacija == 1):
            paint.rotate(90.0)
            if (self.ukljuceno == True):
                paint.drawImage(QPoint(self.y,-self.x),NKmotorUkljucen)    
            else:
                paint.drawImage(QPoint(self.y,-self.x),NKmotor)       
            if(self.senzor == False):
                paint.setBrush(QColor(255, 0, 0))
                paint.setPen(QColor(255, 0, 0))
                paint.drawRect(self.dy,-self.dx+30,9,9)
        if(self.rotacija == 2):
            #paint.translate(self.x,self.y);
            paint.rotate(180.0)
            if (self.ukljuceno == True):
                paint.drawImage(QPoint(-self.x,-self.y),NKmotorUkljucen)    
            else:
                paint.drawImage(QPoint(-self.x,-self.y),NKmotor)       
            if(self.senzor == False):
                paint.setBrush(QColor(255, 0, 0))
                paint.setPen(QColor(255, 0, 0))
                paint.drawRect(-self.dx+30,-self.dy+30,9,9)  
        if(self.rotacija == 3):
            #paint.translate(self.x,self.y);
            paint.rotate(270)
            if (self.ukljuceno == True):
                paint.drawImage(QPoint(-self.y,self.x),NKmotorUkljucen)    
            else:
                paint.drawImage(QPoint(-self.y,self.x),NKmotor)       
            if(self.senzor == False):
                paint.setBrush(QColor(255, 0, 0))
                paint.setPen(QColor(255, 0, 0))
                paint.drawRect(-self.dy+30,self.dx,9,9)                 
        paint.restore()
