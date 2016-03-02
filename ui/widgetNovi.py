
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
from motor import Motor
from ventil import Ventil

class noviWidget(QWidget):
    
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        self.slike1 = QImage()
        
        self.slike1.load("images/skica4.png")
        
        
        self.motori = {1: Motor(520,15,0,'e1'), 2 : Motor(693,15,0,'e2'),
        #3: Motor(500,200,0), 4 : Motor(500,200,1),5: Motor(500,200,2), 6 : Motor(500,200,3),
        3: Motor(426,505,3,'traka2'),4: Motor(426,898,3,'redler_izn_silosa'),5: Motor(106,492,1,'traka1'),
        6: Motor(372,956,0,'red_u_jami'),7: Motor(656,996,3,'puz_jama'), 8: Motor(868,226,0,'iznad_binova'),
        9: Motor(1364,311,2,'puz_89')}
        
        self.ventili = {1: Ventil(125,174,'sil6gore'),2: Ventil(262,174,'sil5gore'),3: Ventil(401,174,'sil4gore'),
                        4: Ventil(125,383,'sil6dole'),5: Ventil(262,383,'sil5dole'),6: Ventil(401,383,'sil4dole'),
                        7: Ventil(125,566,'sil1gore'),8: Ventil(262,566,'sil2gore'),9: Ventil(401,566,'sil3gore'),
                        10: Ventil(125,775,'sil1dole'),11: Ventil(262,775,'sil2dole'),12: Ventil(401,775,'sil3dole'),
                        13: Ventil(907,282,'p1/6'),14: Ventil(1037,282,'p2/5'),15: Ventil(1170,282,'p2/4')}
        
        
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