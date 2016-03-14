
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
        self.slike1.load("images/skica6.png")
        self.is_klapna_gore_otvorena = False;
        self.is_klapna_gore_zatvorena = False;
        self.is_klapna_dole_otvorena = False;
        self.is_klapna_dole_zatvorena = False;
        #motori koordinate,orjentacija,motor,naziv
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

        33: Motor(966,756,0,33,'vagapuz'),
        
        34: Motor(1280,903,0,34,'mesaonapuz')

        }
        
        self.map_motori=[]

        self.ventili = {
                1: PneumatikaDupla(677,74,10,0,1,'Pne_e1_binovi/asp'),
                2: PneumatikaDupla(842,70,10,1,2,'Pne_e2_red/asp'),
                3: Pneumatika(644,74,3,'Pne_e1_utovarna_ramp'),4: Pneumatika(875,70,4,'Pne_e2_puz_binovi'),
                5: Pneumatika(812,70,5,'Pne_e2_silos4'),6: Ventil(125,383,6,'sil6dole'),
                7: Pneumatika(785,70,7,'Pne_e2_silos5'),8: Pneumatika(904,70,8,'Pne_e2_extru'),
                9: PneumatikaDupla(1603,153,20,2,9,'Pext/ext'),10: Ventil(1037,282,10,'Reg2/5'),
                11: Pneumatika(617,74,11,'Pne_e1_na_redler_iznadsil'),12: Ventil(401,383,12,'sil4dole'),
                13: Ventil(262,383,13,'sil5dole'),14: Ventil(125,775,14,'sil1dole'),
                15: Ventil(262,775,15,'sil2dole'),16: Ventil(401,775,16,'sil3dole'),
                17: Ventil(907,282,17,'reg1/6'),
                
                18: Pneumatika(1653,418,18,'Pne_vaga2'),
                19: Pneumatika(1614,418,19,'Pne_vaga1'),
                
                20: PneumatikaDupla(1054,339,20,1,20,'P2/5'),
                21: Ventil(262,566,21,'sil2gore'),22: Ventil(125,566,22,'sil1gore'),
                23: VentilHor(1538,286,23,'got_ka_bin7'), #!!!!!
                24: VentilHor(1634,196,24,'pel_mala'), #!!!!!
                25: Ventil(401,566,25,'sil3gore'),   
                26: PneumatikaDupla(1481,300,20,3,26,'p26zasun iznad vage'), #!!!!!
                #27????     #premiks ne treba
                #28: PneumatikaDupla(1634,418,20,1,28,'Pvaga1/vaga2'), # ne treba vaga
                
                29: PneumatikaDupla(1292,320,20,0,29,'P8/9'),
                30: PneumatikaDupla(1185,339,20,1,30,'P3/4'),31: Ventil(1170,282,31,'reg3/4'),
                32: PneumatikaDupla(922,339,20,1,32,'P1/6'), 
                
                
                33: PneumatikaDupla(1362,254,20,0,33,'P7/puz'), ## treba 
                37: Ventil(125,174,0,'sil6gore'),38: Ventil(401,174,0,'sil4gore'), #ne treba
                42: Ventil(262,174,0,'sil5gore'),  #ne treba
                35: Ventil(1167,106,9,'pextruder')}
        
        self.bv1 = QPushButton("Vaga1",self)
        self.bv2 = QPushButton("Vaga2",self)
        self.bv1.setGeometry(QRect(1590,717, 60, 20))
        self.bv2.setGeometry(QRect(1625,594, 60, 20))
        self.bv1.clicked.connect(lambda:self.btn_vaga1()) 
        self.bv2.clicked.connect(lambda:self.btn_vaga2())

        self.bpeletirkavelika = QPushButton("Peletirka velika",self) 
        self.bpeletirkavelika.setGeometry(QRect(1405,190, 100, 40))        
        self.bextruderveliki = QPushButton("Ekstruder veliki",self) 
        self.bextruderveliki.setGeometry(QRect(1380,84, 100, 40))  
        self.bextrudermali = QPushButton("Ekstruder mali",self) 
        self.bextrudermali.setGeometry(QRect(1690,110, 100, 40)) 
        self.bpeletirkamala = QPushButton("Peletirka malia",self) 
        self.bpeletirkamala.setGeometry(QRect(1700,179, 90, 40)) 
        self.bv1.setStyleSheet("background-color: lightgray")
        self.bv2.setStyleSheet("background-color: lightgray")
        self.bpeletirkavelika.setStyleSheet("background-color: lightgray")
        self.bextruderveliki.setStyleSheet("background-color: lightgray")
        self.bextrudermali.setStyleSheet("background-color: lightgray")
        self.bpeletirkamala.setStyleSheet("background-color: lightgray")
        
        self.bpeletirkavelika.clicked.connect(lambda:self.btn_peletirkavelika()) 
        self.bextruderveliki.clicked.connect(lambda:self.btn_extruderveliki()) 
        self.bextrudermali.clicked.connect(lambda:self.btn_extrudermali()) 
        self.bpeletirkamala.clicked.connect(lambda:self.btn_peletirkamala()) 
        
        
        self.bextrudermali.setGeometry(QRect(1690,110, 100, 40))           
        self.b1 = QPushButton("Otvori",self)
        self.b1.setStyleSheet("background-color: lightgray")
        self.b1.setGeometry(QRect(1325,670, 60, 20))
        #self.b1.move(1325,670)
        self.b1.clicked.connect(lambda:self.btn_gornja_klapna_otvori()) 
        self.b2 = QPushButton("Zatvori",self)
        self.b2.setStyleSheet("background-color: lightgray")
        self.b2.setGeometry(QRect(1325,700, 60, 20))
        #self.b2.move(1325,700)
        self.b2.clicked.connect(lambda:self.btn_gornja_klapna_zatvori()) 
        self.b3 = QPushButton("Otvori",self)
        self.b3.setStyleSheet("background-color: lightgray")
        self.b3.clicked.connect(lambda:self.btn_donja_klapna_otvori()) 
        self.b3.setGeometry(QRect(1325,820, 60, 20))
        #self.b3.move(1325,820)
        self.b4 = QPushButton("Zatvori",self)
        self.b4.setStyleSheet("background-color: lightgray")
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
  
    def set_sate(self,state):
        self.state= state
        self.ucitajMotore()
        self.ctimer.start(300)
    def btn_gornja_klapna_otvori(self):
        if(self.is_klapna_gore_otvorena==False):
            self.b1.setStyleSheet("background-color: green")
            self.state.ukljuciMotor(22)
            self.is_klapna_gore_otvorena=True
        else:    
            self.b1.setStyleSheet("background-color: lightgray")
            self.state.iskljuciMotor(22)
            self.is_klapna_gore_otvorena=False            
    def btn_gornja_klapna_zatvori(self):
        if(self.is_klapna_gore_zatvorena==False):
            self.b2.setStyleSheet("background-color: green")
            self.state.ukljuciMotor(26)
            self.is_klapna_gore_zatvorena=True 
        else:
            self.b2.setStyleSheet("background-color: lightgray")
            self.state.iskljuciMotor(26)
            self.is_klapna_gore_zatvorena=False        
            
    def btn_donja_klapna_otvori(self):
        if(self.is_klapna_dole_otvorena==False):    
            self.b3.setStyleSheet("background-color: green")
            self.state.ukljuciMotor(16)
            self.is_klapna_dole_otvorena=True 
        else:
            self.b3.setStyleSheet("background-color: lightgray")
            self.state.iskljuciMotor(16)
            self.is_klapna_dole_otvorena=False 
            
    def btn_donja_klapna_zatvori(self):
        if(self.is_klapna_dole_zatvorena==False):    
            self.state.ukljuciMotor(17)
            self.b4.setStyleSheet("background-color: green")
            self.is_klapna_dole_zatvorena=True 
        else:
            self.b4.setStyleSheet("background-color: lightgray")
            self.state.iskljuciMotor(17)
            self.is_klapna_dole_zatvorena=False        

        
    def mousePressEvent(self, event):
        print 'x:'+str(event.x())+'y:'+str(event.y())
        for key, value in self.motori.iteritems():
            if(value.click(event.x(),event.y())==True):
                m = value.motor
                if(value.ukljuceno==True):
                    if(m==33):
                        m=29
                        self.motori[m].ukljuceno = True
                    if(m==34):
                        m=25
                        self.motori[m].ukljuceno = True
                        
                    self.state.ukljuciMotor(m)  #komanda motoru
                    if(m==29):
                        self.motori[33].ukljuceno = True; 
                    if(m==25):
                        self.motori[34].ukljuceno = True; 
                    if(m==19):
                        self.ventili[33].ukljuceno = True;
                    #binovi
                    if(m==11):
                        self.binovi.start(1)
                    if(m==14):
                        self.binovi.start(2)   
          
                    if(m==2):
                        self.binovi.start(3)   
          
                    if(m==8):
                        self.binovi.start(4)   
          
                    if(m==13):
                        self.binovi.start(5)   
          
                    if(m==6):
                        self.binovi.start(6) 
                    if(m==7):
                        self.binovi.start(7)
                    if(m==10):
                        self.binovi89.start(2)
                    if(m==4):
                        self.binovi89.start(1)
                else:
                    if(m==33):
                        m=29
                        self.motori[m].ukljuceno = False
                    if(m==34):
                        m=25
                        self.motori[m].ukljuceno = False 
                    self.state.iskljuciMotor(m) #komanda mototru
                    if(m==29):
                        self.motori[33].ukljuceno = False; 
                    if(m==25):
                        self.motori[34].ukljuceno = False;    
                    if(m==19):
                        self.ventili[33].ukljuceno = False;        
                    #binovi
                    if(m==11):
                        self.binovi.stop(1)   
                    if(m==14):
                        self.binovi.stop(2)   
          
                    if(m==2):
                        self.binovi.stop(3)   
          
                    if(m==8):
                        self.binovi.stop(4)   
          
                    if(m==13):
                        self.binovi.stop(5)   
          
                    if(m==6):
                        self.binovi.stop(6)   
          
                    if(m==7):
                        self.binovi.stop(7)   
          
                    if(m==10):
                        self.binovi89.stop(2)
                    if(m==4):
                        self.binovi89.stop(1)
                self.repaint()
                break
        for key, value in self.ventili.iteritems():
            if(value.click(event.x(),event.y())==True):
                v = value.motor
                if(v!=0):
                    if(value.ukljuceno==True):
                        self.state.ukljuciPneumatiku(v)
                        if(v==14):
                            self.silosi.start(1)   
                        if(v==15):
                            self.silosi.start(2)   
                        if(v==16):
                            self.silosi.start(3) 
                        if(v==12):
                            self.silosi.start(4) 
                        if(v==13):
                            self.silosi.start(5) 
                        if(v==6):
                            self.silosi.start(6) 
                       
                    else:
                        self.state.iskljuciPneumatiku(v)
                        if(v==14):
                            self.silosi.stop(1)   
                        if(v==15):
                            self.silosi.stop(2)   
                        if(v==16):
                            self.silosi.stop(3) 
                        if(v==12):
                            self.silosi.stop(4) 
                        if(v==13):
                            self.silosi.stop(5) 
                        if(v==6):
                            self.silosi.stop(6) 
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
        for key, value in self.motori.iteritems():
            value.ukljuceno = False;
        for key, value in self.ventili.iteritems():
            value.ukljuceno = False;
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
            self.ventili[33].ukljuceno = True;
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
           
        #pneumatike
        if(self.state.pneumatike['p1']==1):
            self.ventili[1].ukljuceno = True;       
        if(self.state.pneumatike['p2']==1):
            self.ventili[2].ukljuceno = True;            
        if(self.state.pneumatike['p3']==1):
            self.ventili[3].ukljuceno = True;       
        if(self.state.pneumatike['p4']==1):
            self.ventili[4].ukljuceno = True;  
        if(self.state.pneumatike['p5']==1):
            self.ventili[5].ukljuceno = True;       
        if(self.state.pneumatike['p6']==1):
            self.ventili[6].ukljuceno = True;            
        if(self.state.pneumatike['p7']==1):
            self.ventili[7].ukljuceno = True;       
        if(self.state.pneumatike['p8']==1):
            self.ventili[8].ukljuceno = True;  
        if(self.state.pneumatike['p9']==1):
            self.ventili[9].ukljuceno = True;       
        if(self.state.pneumatike['p10']==1):
            self.ventili[10].ukljuceno = True;            
        if(self.state.pneumatike['p11']==1):
            self.ventili[11].ukljuceno = True;       
        if(self.state.pneumatike['p12']==1):
            self.ventili[12].ukljuceno = True;  
        if(self.state.pneumatike['p13']==1):
            self.ventili[13].ukljuceno = True;       
        if(self.state.pneumatike['p14']==1):
            self.ventili[14].ukljuceno = True;            
        if(self.state.pneumatike['p15']==1):
            self.ventili[15].ukljuceno = True;       
        if(self.state.pneumatike['p16']==1):
            self.ventili[16].ukljuceno = True; 
        if(self.state.pneumatike['p17']==1):
            self.ventili[17].ukljuceno = True;       
        if(self.state.pneumatike['p18']==1):
            self.ventili[18].ukljuceno = True;  
            
        if(self.state.pneumatike['p19']==1):
            self.ventili[19].ukljuceno = True;        

            
        if(self.state.pneumatike['p20']==1):
            self.ventili[20].ukljuceno = True;  
        if(self.state.pneumatike['p21']==1):
            self.ventili[21].ukljuceno = True;  
        if(self.state.pneumatike['p22']==1):
            self.ventili[22].ukljuceno = True;  
        if(self.state.pneumatike['p23']==1):
            self.ventili[23].ukljuceno = True;  
        if(self.state.pneumatike['p24']==1):
            self.ventili[24].ukljuceno = True;  

        if(self.state.pneumatike['p25']==1):
            self.ventili[25].ukljuceno = True;
            
        if(self.state.pneumatike['p26']==1):
            self.ventili[26].ukljuceno = True; 
        #if(self.state.pneumatike['p28']==1):
        #    self.ventili[28].ukljuceno = True;  
        if(self.state.pneumatike['p29']==1):
            self.ventili[29].ukljuceno = True; 
        if(self.state.pneumatike['p30']==1):
            self.ventili[30].ukljuceno = True; 
        if(self.state.pneumatike['p31']==1):
            self.ventili[31].ukljuceno = True;             
        if(self.state.pneumatike['p32']==1):
            self.ventili[32].ukljuceno = True;  

            
    def timerUpdate(self):
        self.binovi.animate()
        self.binovi89.animate()
        self.silosi.animate()
        i = self.state.getIndikator()
        if(i[0]==1):
            self.motori[11].senzorOn()
        else:
            self.motori[11].senzorOff()
        if(i[1]==1):
            self.motori[14].senzorOn()
        else:
            self.motori[14].senzorOff()
        #bin3    
        if(i[2]==1):
            self.motori[2].senzorOn()
        else:
            self.motori[2].senzorOff()
        #bin4    
        if(i[3]==1):
            self.motori[8].senzorOn()
        else:
            self.motori[8].senzorOff()
        #bin5    
        if(i[4]==1):
            self.motori[13].senzorOn()
        else:
            self.motori[13].senzorOff()
        #bin6    
        if(i[5]==1):
            self.motori[6].senzorOn()
        else:
            self.motori[6].senzorOff()
        #bin7
        if(i[6]==1):
            self.motori[7].senzorOn()
        else:
            self.motori[7].senzorOff()
        #bin8
        if(i[7]==1):
            self.motori[10].senzorOn()
        else:
            self.motori[10].senzorOff()
        #bin9    
        if(i[8]==1):
            self.motori[4].senzorOn()
        else:
            self.motori[4].senzorOff()
        #premix na vagu
        if(i[9]==1):
            self.motori[12].senzorOn()
        else:
            self.motori[12].senzorOff()
        #mesaona gore otvorena    
        if(i[10]==1):
            self.kgo_senz.on()
        else:
            self.kgo_senz.off()
        #mesaona gore zat  
        if(i[11]==1):
            self.kgz_senz.on()
        else:
            self.kgz_senz.off()
        #mesaona dole otvorena  
        if(i[12]==1):
            self.kdo_senz.on()
        else:
            self.kdo_senz.off()
        #mesaona dole zat 
        if(i[13]==1):
            self.kdz_senz.on()
        else:
            self.kdz_senz.off()
            
            
        #Redler u istovarnoj jami
        if(i[14]==1):
            self.motori[1].senzorOn()
        else:
            self.motori[1].senzorOff()
        #Puz u istovarnoj jami
        if(i[15]==1):
            self.motori[3].senzorOn()
        else:
            self.motori[3].senzorOff()
        #e1
        if(i[16]==1):
            self.motori[23].senzorOn()
        else:
            self.motori[23].senzorOff()
        #e2
        if(i[17]==1):
            self.motori[18].senzorOn()
        else:
            self.motori[18].senzorOff()
            
        #Ventilator aspiratera
        if(i[18]==1):
            self.motori[21].senzorOn()
        else:
            self.motori[21].senzorOff()
        #aspirater
        if(i[19]==1):
            self.motori[9].senzorOn()
        else:
            self.motori[9].senzorOff()
            
        #Redler iznad silosa
        if(i[20]==1):
            self.motori[5].senzorOn()
        else:
            self.motori[5].senzorOff()
        #puz za punjenje binova
        if(i[21]==1):
            self.motori[30].senzorOn()
        else:
            self.motori[30].senzorOff()
        #t1
        if(i[22]==1):
            self.motori[24].senzorOn()
        else:
            self.motori[24].senzorOff()
        #t2
        if(i[23]==1):
            self.motori[20].senzorOn()
        else:
            self.motori[20].senzorOff()
        #mlin
        if(i[24]==1):
            self.motori[32].senzorOn()
        else:
            self.motori[32].senzorOff()
        #elevator mlina
        if(i[25]==1):
            self.motori[15].senzorOn()
        else:
            self.motori[15].senzorOff()
        #Dotok mat.u mlin
        if(i[26]==1):
            self.motori[29].senzorOn()
        else:
            self.motori[29].senzorOff()
        #mesalica
        if(i[27]==1):
            self.motori[31].senzorOn()
        else:
            self.motori[31].senzorOff()
        #Gotova roba iz mesalice
        if(i[28]==1):
            self.motori[25].senzorOn()
        else:
            self.motori[25].senzorOff()
        #Gotova roba prema ekst.
        if(i[29]==1):
            self.motori[28].senzorOn()
        else:
            self.motori[28].senzorOff()

            
        #pneumatike
        ulazi = self.state.updateSensors();
        if(ulazi[0]==1):
            self.ventili[1].senzorOn();
        else:
            self.ventili[1].senzorOff();
        if(ulazi[1]==1):
            self.ventili[2].senzorOn();
        else:
            self.ventili[2].senzorOff();
        if(ulazi[2]==1):
            self.ventili[3].senzorOn();
        else:
            self.ventili[3].senzorOff();
        if(ulazi[3]==1):
            self.ventili[4].senzorOn();
        else:
            self.ventili[4].senzorOff();
        if(ulazi[4]==1):
            self.ventili[5].senzorOn();
        else:
            self.ventili[5].senzorOff();
        if(ulazi[5]==1):
            self.ventili[6].senzorOn();
        else:
            self.ventili[6].senzorOff();
        if(ulazi[6]==1):
            self.ventili[7].senzorOn();
        else:
            self.ventili[7].senzorOff();
        if(ulazi[7]==1):
            self.ventili[8].senzorOn();
        else:
            self.ventili[8].senzorOff();
        if(ulazi[8]==1):
            self.ventili[9].senzorOn();
        else:
            self.ventili[9].senzorOff();
        if(ulazi[9]==1):
            self.ventili[10].senzorOn();
        else:
            self.ventili[10].senzorOff();
        if(ulazi[10]==1):
            self.ventili[11].senzorOn();
        else:
            self.ventili[11].senzorOff();
        if(ulazi[11]==1):
            self.ventili[12].senzorOn();
        else:
            self.ventili[12].senzorOff();
        if(ulazi[12]==1):
            self.ventili[13].senzorOn();
        else:
            self.ventili[13].senzorOff();
        if(ulazi[13]==1):
            self.ventili[14].senzorOn();
        else:
            self.ventili[14].senzorOff();
        if(ulazi[14]==1):
            self.ventili[15].senzorOn();
        else:
            self.ventili[15].senzorOff();
        if(ulazi[15]==1):
            self.ventili[16].senzorOn();
        else:
            self.ventili[16].senzorOff();
        if(ulazi[16]==1):
            self.ventili[17].senzorOn();
        else:
            self.ventili[17].senzorOff();
        if(ulazi[17]==1):
            self.ventili[18].senzorOn();
        else:
            self.ventili[18].senzorOff();
        if(ulazi[18]==1):
            self.ventili[19].senzorOn();
        else:
            self.ventili[19].senzorOff();
        if(ulazi[19]==1):
            self.ventili[20].senzorOn();
        else:
            self.ventili[20].senzorOff();
        if(ulazi[20]==1):
            self.ventili[21].senzorOn();
        else:
            self.ventili[21].senzorOff();
        if(ulazi[21]==1):
            self.ventili[22].senzorOn();
        else:
            self.ventili[22].senzorOff();
            
        if(ulazi[22]==1):
            self.ventili[23].senzorOn();
        else:
            self.ventili[23].senzorOff();
        if(ulazi[23]==1):
            self.ventili[24].senzorOn();
        else:
            self.ventili[24].senzorOff();
        if(ulazi[24]==1):
            self.ventili[25].senzorOn();
        else:
            self.ventili[25].senzorOff();
        if(ulazi[25]==1):
            self.ventili[26].senzorOn();
        else:
            self.ventili[26].senzorOff();

        if(ulazi[28]==1):
            self.ventili[29].senzorOn();
        else:
            self.ventili[29].senzorOff();
        if(ulazi[29]==1):
            self.ventili[30].senzorOn();
        else:
            self.ventili[30].senzorOff();  
        if(ulazi[30]==1):
            self.ventili[31].senzorOn();
        else:
            self.ventili[31].senzorOff();
        if(ulazi[31]==1):
            self.ventili[32].senzorOn();
        else:
            self.ventili[32].senzorOff();
            
        self.repaint()             
        
    def btn_vaga1(self):
    
        self.bv1.setStyleSheet("background-color: green")
        self.bv2.setStyleSheet("background-color: lightgray")
        self.bpeletirkavelika.setStyleSheet("background-color: lightgray")
        self.bextruderveliki.setStyleSheet("background-color: lightgray")
        self.bextrudermali.setStyleSheet("background-color: lightgray")
        self.bpeletirkamala.setStyleSheet("background-color: lightgray")
        
        self.state.iskljuciPId(19)
        self.state.iskljuciPId(23)
        self.state.iskljuciPId(26)
        self.state.iskljuciPId(9)
        self.state.iskljuciPId(18)
        self.state.iskljuciMotorId(28) 
        self.ucitajMotore() 
        self.repaint()     
        
    def btn_vaga2(self):
        self.bv1.setStyleSheet("background-color: lightgray")
        self.bv2.setStyleSheet("background-color: green")
        self.bpeletirkavelika.setStyleSheet("background-color: lightgray")
        self.bextruderveliki.setStyleSheet("background-color: lightgray")
        self.bextrudermali.setStyleSheet("background-color: lightgray")
        self.bpeletirkamala.setStyleSheet("background-color: lightgray")
        
        self.state.kreniPId(19)
        self.state.iskljuciPId(23)
        self.state.iskljuciPId(26)
        self.state.iskljuciPId(9)
        self.state.kreniPId(18)
        self.state.iskljuciMotorId(28)
        self.ucitajMotore() 
        self.repaint()   

    def btn_peletirkavelika(self):
        self.bv1.setStyleSheet("background-color: lightgray")
        self.bv2.setStyleSheet("background-color: lightgray")
        self.bpeletirkavelika.setStyleSheet("background-color: green")
        self.bextruderveliki.setStyleSheet("background-color: lightgray")
        self.bextrudermali.setStyleSheet("background-color: lightgray")
        self.bpeletirkamala.setStyleSheet("background-color: lightgray")
        self.state.kreniPId(19)    
        self.state.kreniPId(23)  
        self.state.iskljuciPId(26)
        self.state.iskljuciPId(9)
        self.state.iskljuciPId(18)
        self.state.kreniMotorId(28)      
        self.ucitajMotore() 
        self.repaint() 
    def btn_peletirkamala(self):
        self.bv1.setStyleSheet("background-color: lightgray")
        self.bv2.setStyleSheet("background-color: lightgray")
        self.bpeletirkavelika.setStyleSheet("background-color: lightgray")
        self.bextruderveliki.setStyleSheet("background-color: lightgray")
        self.bextrudermali.setStyleSheet("background-color: lightgray")
        self.bpeletirkamala.setStyleSheet("background-color: green")
        
        
    def btn_extruderveliki(self):
        self.bv1.setStyleSheet("background-color: lightgray")
        self.bv2.setStyleSheet("background-color: lightgray")
        self.bpeletirkavelika.setStyleSheet("background-color: lightgray")
        self.bextruderveliki.setStyleSheet("background-color: green")
        self.bextrudermali.setStyleSheet("background-color: lightgray")
        self.bpeletirkamala.setStyleSheet("background-color: lightgray")
        self.state.kreniPId(19) 
        self.state.iskljuciPId(23)
        self.state.iskljuciPId(26)
        self.state.iskljuciPId(9)
        self.state.iskljuciPId(18)
        self.state.kreniMotorId(28)
        self.ucitajMotore() 
        self.repaint()         
    def btn_extrudermali(self):    
        self.bv1.setStyleSheet("background-color: lightgray")
        self.bv2.setStyleSheet("background-color: lightgray")
        self.bpeletirkavelika.setStyleSheet("background-color: lightgray")
        self.bextruderveliki.setStyleSheet("background-color: lightgray")
        self.bextrudermali.setStyleSheet("background-color: green")
        self.bpeletirkamala.setStyleSheet("background-color: lightgray")
        self.state.kreniPId(19)    
        self.state.iskljuciPId(23)
        self.state.iskljuciPId(26)
        self.state.kreniPId(9)
        self.state.iskljuciPId(18)
        self.state.kreniMotorId(28)  
        self.ucitajMotore() 
        self.repaint() 
        