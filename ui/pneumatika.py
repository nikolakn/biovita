
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import math

class Pneumatika():
    
    Pi = math.pi
    TwoPi = 2.0 * Pi
    def __init__(self,x,y,motor,naziv=''):
        self.crna = QColor(0, 0, 0)
        self.crvena = QColor(255, 0, 0)
        self.bela = QColor(255, 255, 255)
        self.ukljuceno = False;
        
        self.points = [QPoint(x, y), QPoint(x+30, y), QPoint(x, y+30), QPoint(x+30, y+30)]
        self.x = x;
        self.y = y;
        self.dx = self.x-28;
        self.dy = self.y+15-25/2;
        self.motor = motor
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
        okvir = QRect(self.x-8, self.y-8,16,34)
        
        if(okvir.contains(x,y)==True):
            if(self.ukljuceno==True):
                self.ukljuceno = False;
            else:
                self.ukljuceno = True;
            return True;
        return False  
        
    def nacrtaj(self, paint):

        paint.setRenderHint(QPainter.Antialiasing)
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        
        
        #needle =QPolygon(self.points)  
        if(self.motor==19):


            if (self.ukljuceno == True):
                paint.setBrush(Qt.red) 
                paint.setPen(QPen(Qt.red, 1, Qt.SolidLine,Qt.RoundCap, Qt.RoundJoin))            
                self.strelica(paint,QPointF(self.x, self.y),QPointF(self.x, self.y+24))
            else: 
                paint.setBrush(Qt.green) 
                paint.setPen(QPen(Qt.green, 1, Qt.SolidLine,Qt.RoundCap, Qt.RoundJoin)) 
                self.strelica(paint,QPointF(self.x, self.y),QPointF(self.x, self.y+24))   
        else:

            if (self.ukljuceno == True):
                paint.setBrush(Qt.green) 
                paint.setPen(QPen(Qt.green, 1, Qt.SolidLine,Qt.RoundCap, Qt.RoundJoin))            
                self.strelica(paint,QPointF(self.x, self.y),QPointF(self.x, self.y+24))
            else: 
                paint.setBrush(Qt.red) 
                paint.setPen(QPen(Qt.red, 1, Qt.SolidLine,Qt.RoundCap, Qt.RoundJoin)) 
                self.strelica(paint,QPointF(self.x, self.y),QPointF(self.x, self.y+24))  
            
        if (self.senzor == True):
            paint.setPen(pen)
            paint.setBrush(Qt.green) 
            paint.drawEllipse(self.x-8, self.y-8, 16, 16)
        else:
            paint.setPen(pen)
            paint.setBrush(Qt.red) 
            paint.drawEllipse(self.x-8, self.y-8, 16, 16)  
             

    def strelica(self,paint,prva,druga):
        self.arrowSize = 10.0
        line = QLineF(prva, druga)

        if line.length() == 0.0:
            return
            
        #paint.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        paint.drawLine(line)
        # Draw the arrows if there's enough room.
        angle = math.acos(line.dx() / line.length())
        if line.dy() >= 0:
            angle = Pneumatika.TwoPi - angle

        #sourceArrowP1 = prva + QPointF(math.sin(angle + Pneumatika.Pi / 3) * self.arrowSize,
        #                                                  math.cos(angle + Pneumatika.Pi / 3) * self.arrowSize)
        #sourceArrowP2 = prva + QPointF(math.sin(angle + Pneumatika.Pi - Pneumatika.Pi / 3) * self.arrowSize,
        #                                                  math.cos(angle + Pneumatika.Pi - Pneumatika.Pi / 3) * #self.arrowSize);   

        destArrowP1 = druga + QPointF(math.sin(angle - Pneumatika.Pi / 3) * self.arrowSize,
                                                      math.cos(angle - Pneumatika.Pi / 3) * self.arrowSize)
        destArrowP2 = druga + QPointF(math.sin(angle - Pneumatika.Pi + Pneumatika.Pi / 3) * self.arrowSize,
                                                      math.cos(angle - Pneumatika.Pi + Pneumatika.Pi / 3) * self.arrowSize)

        #paint.drawPolygon(QPolygonF([line.p1(), sourceArrowP1, sourceArrowP2]))
        paint.drawPolygon(QPolygonF([line.p2(), destArrowP1, destArrowP2]))