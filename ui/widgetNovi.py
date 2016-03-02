
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
from motor import Motor

class noviWidget(QWidget):
    
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        self.slike1 = QImage()
        
        self.slike1.load("images/skica3.png")
        
        
        self.motori = {1: Motor(520,15), 2 : Motor(693,15)}
        
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
        
        pen = QPen(Qt.black, 7, Qt.SolidLine)
        paint.setPen(pen)
        
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