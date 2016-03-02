
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
from motor import Motor
from ventil import Ventil

class noviWidget(QWidget):
    
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        self.slike1 = QImage()
        
        self.slike1.load("images/skica4.png")
        
        
        self.motori = {1: Motor(520,15,0), 2 : Motor(693,15,0),
        #3: Motor(500,200,0), 4 : Motor(500,200,1),5: Motor(500,200,2), 6 : Motor(500,200,3),
        3: Motor(426,505,3),4: Motor(426,898,3),5: Motor(106,492,1),
        6: Motor(372,956,0),7: Motor(656,996,3)}
        
        self.ventili = {1: Ventil(125,174),2: Ventil(262,174),3: Ventil(401,174),
                        4: Ventil(125,383),5: Ventil(262,383),6: Ventil(401,383),
                        7: Ventil(125,566),8: Ventil(262,566),9: Ventil(401,566),
                        10: Ventil(125,775),11: Ventil(262,775),12: Ventil(401,775)}
        
        
        self.motori[2].on()
        self.motori[2].senzorOn()
        
        self.ctimer = QTimer()
        QObject.connect(self.ctimer, SIGNAL("timeout()"), self.timerUpdate)
        self.ctimer.start(200)   
        

    def timerUpdate(self):
        self.repaint() 
        
    def paintEvent(self, QPaintEvent):
        paint = QPainter(self)
        paint.setPen(Qt.black);

        paint.drawImage(QPoint(0,0),self.slike1)
        
        for key, value in self.motori.iteritems():
            value.nacrtaj(paint)
        for key, value in self.ventili.iteritems():
            value.nacrtaj(paint)        
        #pen = QPen(Qt.black, 7, Qt.SolidLine)
        #paint.setPen(pen)
        
        #paint.drawLine(10, 40, 500, 40)
        #paint.drawLine( 500, 40, 500, 500)
        '''
        for i in range(0,2500,50):
            paint.drawLine(i, 40, i, 60)
            paint.drawLine(i+25, 40, i+25, 60)
            paint.drawText(i, 50 ,str(i)) 
        for i in range(0,2500,50):
            paint.drawLine(40, i, 60, i)
            paint.drawLine(40, i+25, 60, i+25)
            paint.drawText(50, i ,str(i)) 
        '''  