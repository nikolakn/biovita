
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
from motor import Motor
from ventil import Ventil
from ventilhor import VentilHor
from pneumatika import Pneumatika
from pneumatikadupla import PneumatikaDupla
from aspirater import Aspirater
from ventilatoraspiratera import VentilatorAspiratera

class noviWidget(QWidget):
    
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        self.slike1 = QImage()
        
        self.slike1.load("images/skica4.png")
        
        
        self.motori = {1: Motor(520,15,0,'e1'), 2 : Motor(693,15,0,'e2'),
        #3: Motor(500,200,0), 4 : Motor(500,200,1),5: Motor(500,200,2), 6 : Motor(500,200,3),
        3: Motor(426,505,3,'traka2'),4: Motor(426,898,3,'traka1'),5: Motor(106,492,1,'redler_izn_silosa'),
        6: Motor(372,956,0,'red_u_jami'),7: Motor(656,996,3,'puz_jama'), 8: Motor(868,226,0,'iznad_binova'),
        9: Motor(1364,311,2,'puz_89'),
        10: Motor(912,520,1,'bin1'),11: Motor(960,500,1,'bin6'),12: Motor(1045,520,1,'bin2'),
        13 : Motor(1095,500,1,'bin5'),14: Motor(1173,520,1,'bin3'),15: Motor(1223,500,1,'bin4'),
        16: Motor(1286,435,1,'bin9'),17: Motor(1323,435,1,'bin8'),18: Motor(1392,512,1,'bin7'),
        19: Motor(966,756,0,'vagapuz'),20: Motor(962,913,0,'mlin'),21: Motor(1168,618,0,'mlin_elevator'),
        22: Motor(1280,903,0,'mesaonapuz'),23: Motor(1458,377,0,'e3'),24: Motor(1191,753,2,'e_vaga'),
        25: Motor(1500,792,2,'mesaona'),26: Motor(1590,367,3,'gotov_mat'),27 : Aspirater(626,327,'aspirater'),
        28 : VentilatorAspiratera(678,277,"vent_asp")}
        
        self.ventili = {1: Ventil(125,174,'sil6gore'),2: Ventil(262,174,'sil5gore'),3: Ventil(401,174,'sil4gore'),
                4: Ventil(125,383,'sil6dole'),5: Ventil(262,383,'sil5dole'),6: Ventil(401,383,'sil4dole'),
                7: Ventil(125,566,'sil1gore'),8: Ventil(262,566,'sil2gore'),9: Ventil(401,566,'sil3gore'),
                10: Ventil(125,775,'sil1dole'),11: Ventil(262,775,'sil2dole'),12: Ventil(401,775,'sil3dole'),
                13: Ventil(907,282,'p1/6'),14: Ventil(1037,282,'p2/5'),15: Ventil(1170,282,'p2/4'),
                16: Ventil(1167,106,'pextruder'),
                17: VentilHor(1504,274,'got_ka_bin7'),18: VentilHor(1636,274,'pel_velika'),
                19: VentilHor(1534,196,'pel_mala'),
                20: Pneumatika(617,74,'Pne_e1_na_redler_iznadsil'),21: Pneumatika(644,74,'Pne_e1_utovarna_ramp'),
                22: Pneumatika(785,70,'Pne_e2_silos5'),23: Pneumatika(812,70,'Pne_e2_silos4'),
                24: Pneumatika(875,70,'Pne_e2_puz_binovi'),25: Pneumatika(904,70,'Pne_e2_extru'),
                26: PneumatikaDupla(677,74,10,0,'Pne_e1_binovi/asp'),28: PneumatikaDupla(842,70,10,1,'Pne_e1_binovi/asp'),
                29: PneumatikaDupla(922,339,20,1,'P1/6'), 30: PneumatikaDupla(1053,339,20,1,'P2/5'),
                31: PneumatikaDupla(1185,339,20,1,'P3/4'),
                32: PneumatikaDupla(1292,320,20,1,'P8/9'), 33: PneumatikaDupla(1362,254,20,1,'P7/puz'),
                34: PneumatikaDupla(1634,418,20,1,'Pvaga1/vaga2'),35: PneumatikaDupla(1603,153,20,2,'Pext/ext')}
        
        

        self.b1 = QPushButton("Otvori",self)
        self.b1.move(1325,670)
        self.b2 = QPushButton("Zatvori",self)
        self.b2.move(1325,700)
        self.b3 = QPushButton("Otvori",self)
        self.b3.move(1325,820)
        self.b4 = QPushButton("Zatvori",self)
        self.b4.move(1325,850)
        
        self.ctimer = QTimer()
        QObject.connect(self.ctimer, SIGNAL("timeout()"), self.timerUpdate)
        #self.ctimer.start(400)   
        

    def timerUpdate(self):
        pass
        #self.repaint() 
        
    def mousePressEvent(self, event):
        print 'x:'+str(event.x())+'y:'+str(event.y())
        for key, value in self.motori.iteritems():
            if(value.click(event.x(),event.y())==True):
                self.repaint()
                break
        for key, value in self.ventili.iteritems():
            if(value.click(event.x(),event.y())==True):
                self.repaint()
                break
            
    def paintEvent(self, QPaintEvent):
        
        paint = QPainter(self)
        paint.setRenderHint(QPainter.Antialiasing)
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