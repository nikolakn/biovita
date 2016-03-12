
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
from motor import Motor
from ventil import Ventil
from ventilhor import VentilHor
from pneumatika import Pneumatika
from pneumatikadupla import PneumatikaDupla
from aspirater import Aspirater
from ventilatoraspiratera import VentilatorAspiratera
from ledmotori import LedMotor
from cevi import Cevi
from cevi import Silosi
from cevi import Binovi
from cevi import Binovi89
class noviWidget(QWidget):
    
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        self.slike1 = QImage()
        self.state = None
        self.slike1.load("images/skica5.png")
        self.is_klapna_gore_otvorena = False;
        self.is_klapna_gore_zatvorena = False;
        self.is_klapna_dole_otvorena = False;
        self.is_klapna_dole_zatvorena = False;
        
        self.motori = {1:  Motor(372,956,0,1,'red_u_jami'), 2 : Motor(1173,520,1,2,'bin3'),
        3: Motor(656,996,3,3,'puz_jama'),4: Motor(1286,435,1,4,'bin9'),5: Motor(106,492,1,5,'redler_izn_silosa'),
        6: Motor(960,500,1,6,'bin6'),7: Motor(1392,512,1,7,'bin7'),8: Motor(1223,500,1,8,'bin4'),
        9 : Aspirater(626,327,9,'aspirater'),10: Motor(1323,435,1,10,'bin8'),11: Motor(912,520,1,11,'bin1'),
        12: Motor(-500,-520,1,12,'bin12'),13 : Motor(1095,500,1,13,'bin5'),14: Motor(1045,520,1,14,'bin2'),
        15: Motor(1168,618,0,15,'mlin_elevator'),18:Motor(693,15,0,18,'e2'),19: Motor(1364,311,2,19,'puz_89'),
        20: Motor(426,505,3,20,'traka2'),21 : VentilatorAspiratera(678,277,21,"vent_asp"),
        23: Motor(520,15,0,23,'e1'),24: Motor(426,898,3,24,'traka1'),25: Motor(1458,377,0,25,'e3'),
        28: Motor(1590,367,3,28,'gotov_mat'),29: Motor(1191,753,2,29,'e_vaga'),
        30: Motor(868,226,0,30,'iznad_binova'),31: Motor(1500,792,2,31,'mesaona'),32: Motor(962,913,0,32,'mlin'),

        33: Motor(966,756,0,'vagapuz'),
        
        34: Motor(1280,903,0,'mesaonapuz')

        }
        
        self.map_motori=[]
        
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
                29: PneumatikaDupla(922,339,20,1,'P1/6'), 30: PneumatikaDupla(1054,339,20,1,'P2/5'),
                31: PneumatikaDupla(1185,339,20,1,'P3/4'),
                32: PneumatikaDupla(1292,320,20,1,'P8/9'), 33: PneumatikaDupla(1362,254,20,1,'P7/puz'),
                34: PneumatikaDupla(1634,418,20,1,'Pvaga1/vaga2'),35: PneumatikaDupla(1603,153,20,2,'Pext/ext')}
        
        

        self.b1 = QPushButton("Otvori",self)
        self.b1.setStyleSheet("background-color: gray")
        self.b1.setGeometry(QRect(1325,670, 60, 20))
        #self.b1.move(1325,670)
        self.b1.clicked.connect(lambda:self.btn_gornja_klapna_otvori()) 
        self.b2 = QPushButton("Zatvori",self)
        self.b2.setStyleSheet("background-color: gray")
        self.b2.setGeometry(QRect(1325,700, 60, 20))
        #self.b2.move(1325,700)
        self.b2.clicked.connect(lambda:self.btn_gornja_klapna_zatvori()) 
        self.b3 = QPushButton("Otvori",self)
        self.b3.setStyleSheet("background-color: gray")
        self.b3.clicked.connect(lambda:self.btn_donja_klapna_otvori()) 
        self.b3.setGeometry(QRect(1325,820, 60, 20))
        #self.b3.move(1325,820)
        self.b4 = QPushButton("Zatvori",self)
        self.b4.setStyleSheet("background-color: gray")
        self.b4.clicked.connect(lambda:self.btn_donja_klapna_zatvori()) 
        self.b4.setGeometry(QRect(1325,850, 60, 20))
        #self.b4.move(1325,850)
        self.kgo_senz = LedMotor(self,"")
        self.kgo_senz.move(1390,674)
        self.kgz_senz = LedMotor(self,"")
        self.kgz_senz.move(1390,704)
        self.kdo_senz = LedMotor(self,"")
        self.kdo_senz.move(1390,824)
        self.kdz_senz = LedMotor(self,"")
        self.kdz_senz.move(1390,854)
        
        self.cevi = Cevi()
        self.silosi = Silosi()
        self.binovi = Binovi()
        self.binovi89 = Binovi89()
        
        
        
        self.ctimer = QTimer()
        QObject.connect(self.ctimer, SIGNAL("timeout()"), self.timerUpdate)
        #self.ctimer.start(400)   
    def set_sate(self,state):
        self.state= state
        self.ucitajMotore()
    def btn_gornja_klapna_otvori(self):
        if(self.is_klapna_gore_otvorena==False):
            self.b1.setStyleSheet("background-color: green")
            self.is_klapna_gore_otvorena=True
        else:    
            self.b1.setStyleSheet("background-color: gray")
            self.is_klapna_gore_otvorena=False            
    def btn_gornja_klapna_zatvori(self):
        if(self.is_klapna_gore_zatvorena==False):
            self.b2.setStyleSheet("background-color: green")
            self.is_klapna_gore_zatvorena=True 
        else:
            self.b2.setStyleSheet("background-color: gray")
            self.is_klapna_gore_zatvorena=False        
            
    def btn_donja_klapna_otvori(self):
        if(self.is_klapna_dole_otvorena==False):    
            self.b3.setStyleSheet("background-color: green")
            self.is_klapna_dole_otvorena=True 
        else:
            self.b3.setStyleSheet("background-color: gray")
            self.is_klapna_dole_otvorena=False 
            
    def btn_donja_klapna_zatvori(self):
        if(self.is_klapna_dole_zatvorena==False):    
            self.b4.setStyleSheet("background-color: green")
            self.is_klapna_dole_zatvorena=True 
        else:
            self.b4.setStyleSheet("background-color: gray")
            self.is_klapna_dole_zatvorena=False        
            
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
        self.cevi.nacrtaj(paint)
        self.silosi.nacrtaj(paint)
        self.binovi.nacrtaj(paint)
        self.binovi89.nacrtaj(paint)
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
        
    def ucitajMotore(self):
        if(self.state.motori['m1']==1):
            self.motori[1].ukljuceno = True;
        if(self.state.motori['m2']==1):
            self.motori[2].ukljuceno = True;
        if(self.state.motori['m3']==1):
            self.motori[3].ukljuceno = True;
        if(self.state.motori['m4']==1):
            self.motori[4].ukljuceno = True;
        if(self.state.motori['m5']==1):
            self.motori[5].ukljuceno = True;
        if(self.state.motori['m6']==1):
            self.motori[6].ukljuceno = True;
        if(self.state.motori['m7']==1):
            self.motori[7].ukljuceno = True;
        if(self.state.motori['m8']==1):
            self.motori[8].ukljuceno = True;
        if(self.state.motori['m9']==1):
            self.motori[9].ukljuceno = True;
        if(self.state.motori['m10']==1):
            self.motori[10].ukljuceno = True;
        if(self.state.motori['m11']==1):
            self.motori[11].ukljuceno = True;
        if(self.state.motori['m12']==1):
            self.motori[12].ukljuceno = True;                        
        if(self.state.motori['m13']==1):
            self.motori[13].ukljuceno = True;
        if(self.state.motori['m14']==1):
            self.motori[14].ukljuceno = True;
        if(self.state.motori['m15']==1):
            self.motori[15].ukljuceno = True;
        if(self.state.motori['m16']==1):
            self.btn_donja_klapna_otvori()
        if(self.state.motori['m17']==1):
            self.btn_donja_klapna_zatvori()
        if(self.state.motori['m18']==1):
            self.motori[18].ukljuceno = True;                                                
        if(self.state.motori['m19']==1):
            self.motori[19].ukljuceno = True;
        if(self.state.motori['m20']==1):
            self.motori[20].ukljuceno = True;
        if(self.state.motori['m21']==1):
            self.motori[21].ukljuceno = True;
        if(self.state.motori['m22']==1):
            self.btn_gornja_klapna_otvori()
        if(self.state.motori['m23']==1):
            self.motori[23].ukljuceno = True;
        if(self.state.motori['m24']==1):
            self.motori[24].ukljuceno = True;            
        if(self.state.motori['m25']==1):
            self.motori[25].ukljuceno = True;
            self.motori[34].ukljuceno = True;
        if(self.state.motori['m26']==1):
            self.btn_gornja_klapna_zatvori()
        if(self.state.motori['m27']==1):
            pass####
        if(self.state.motori['m28']==1):
            self.motori[28].ukljuceno = True;
        if(self.state.motori['m29']==1):
            self.motori[29].ukljuceno = True;
            self.motori[33].ukljuceno = True;
        if(self.state.motori['m30']==1):
            self.motori[30].ukljuceno = True;            
        if(self.state.motori['m31']==1):
            self.motori[31].ukljuceno = True;
        if(self.state.motori['m32']==1):
            self.motori[32].ukljuceno = True;
           
            
            
