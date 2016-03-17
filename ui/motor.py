
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport

NKmotor = QImage() 
NKmotorUkljucen = QImage() 
NKmotor.load("images/motoffdes.png")
NKmotor=NKmotor.scaledToHeight(26, Qt.SmoothTransformation )
NKmotorUkljucen.load("images/motukdes.png")
NKmotorUkljucen=NKmotorUkljucen.scaledToHeight(26, Qt.SmoothTransformation)
NKcrna = QColor(0, 0, 0)
NKcrvena = QColor(255, 0, 0)
NKbela = QColor(255, 255, 255)
NKzelena = QColor(0, 255, 0)

      
class Motor():

    def __init__(self,x,y,rot,motor,naziv=''):

        self.ukljuceno = False;

        self.x = x;
        self.y = y;
        self.dx = self.x+15;
        self.dy = self.y+15;
        self.rotacija = rot
        self.senzor = False
        self.naziv = naziv
        self.motor = motor
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
        if(self.rotacija == 0):
            okvir = QRect(self.x,self.y,52,26)
            if(okvir.contains(x,y)==True):
                if(self.ukljuceno==True):
                    self.ukljuceno = False;
                else:
                    self.ukljuceno = True;
                return True;
            return False
        if(self.rotacija == 1):
            okvir = QRect(self.x-26,self.y,26,52)
            if(okvir.contains(x,y)==True):
                if(self.ukljuceno==True):
                    self.ukljuceno = False;
                else:
                    self.ukljuceno = True;
                return True;
            return False
        if(self.rotacija == 2):       
            okvir = QRect(self.x-52,self.y-26,52,26)
            if(okvir.contains(x,y)==True):
                if(self.ukljuceno==True):
                    self.ukljuceno = False;
                else:
                    self.ukljuceno = True;
                return True;
            return False
        if(self.rotacija == 3):
            okvir = QRect(self.x,self.y-52,26,52)
            if(okvir.contains(x,y)==True):
                if(self.ukljuceno==True):
                    self.ukljuceno = False;
                else:
                    self.ukljuceno = True;
                return True;
            return False
             
    def nacrtaj(self, paint):
        paint.save()
        if(self.rotacija == 0):
            #okvir = QRect(self.x,self.y,52,26)
            #paint.drawRect(okvir)    

            if (self.ukljuceno == True):
                paint.drawImage(QPoint(self.x,self.y),NKmotorUkljucen)    
            else:
                paint.drawImage(QPoint(self.x,self.y),NKmotor)       
            if(self.senzor == True):
                paint.setBrush(NKzelena)
                paint.setPen(NKzelena)
                paint.drawRect(self.dx,self.dy,9,9)
                
        if(self.rotacija == 1):
            #okvir = QRect(self.x-26,self.y,26,52)
            #paint.drawRect(okvir) 
            paint.rotate(90.0)
            if (self.ukljuceno == True):
                paint.drawImage(QPoint(self.y,-self.x),NKmotorUkljucen)    
            else:
                paint.drawImage(QPoint(self.y,-self.x),NKmotor)       
            if(self.senzor == True):
                paint.setBrush(NKzelena)
                paint.setPen(NKzelena)
                paint.drawRect(self.dy,-self.dx+30,9,9)
        if(self.rotacija == 2):
            #paint.translate(self.x,self.y);
            #okvir = QRect(self.x-52,self.y-26,52,26)
            #paint.drawRect(okvir) 
            paint.rotate(180.0)
            if (self.ukljuceno == True):
                paint.drawImage(QPoint(-self.x,-self.y),NKmotorUkljucen)    
            else:
                paint.drawImage(QPoint(-self.x,-self.y),NKmotor)       
            if(self.senzor == True):
                paint.setBrush(NKzelena)
                paint.setPen(NKzelena)
                paint.drawRect(-self.dx+30,-self.dy+30,9,9)  
        if(self.rotacija == 3):
            #okvir = QRect(self.x,self.y-52,26,52)
            #paint.drawRect(okvir)
            paint.rotate(270)
            if (self.ukljuceno == True):
                paint.drawImage(QPoint(-self.y,self.x),NKmotorUkljucen)    
            else:
                paint.drawImage(QPoint(-self.y,self.x),NKmotor)       
            if(self.senzor == True):
                paint.setBrush(NKzelena)
                paint.setPen(NKzelena)
                paint.drawRect(-self.dy+30,self.dx,9,9)                 
        paint.restore()
