'''
Created on Jan 15, 2016

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import sys
import UiRucne
import serial 

class rucneProzor(QMainWindow,UiRucne.Ui_MainWindow):
    
    def __init__(self,state, parent=None):
        super(rucneProzor,self).__init__()
        self.setupUi(self)
        '''
        try:
            self.port = serial.Serial("/dev/ttyAMA0" ,9600 , parity=serial.PARITY_NONE , stopbits =serial.STOPBITS_ONE , bytesize=serial.EIGHTBITS,timeout=0)
            self.port.open()
        except:
            print("Greska seriski port")
            sys.exit(0) 
        '''   
        self.state = state
        self.initUI()
        self.ctimer = QTimer()
        QObject.connect(self.ctimer, SIGNAL("timeout()"), self.ulaziUpdate)
        self.ctimer.start(200)
        self.senzori =[self.donji_p1e,self.donji_p3e,self.donji_p11e,self.donji_p7e,
                self.donji_p8e,self.donji_p4e,self.donji_p2e,self.donji_p5e,self.donji_p6e,
                self.donji_p14e,self.donji_p15e,self.donji_p16e,self.donji_p12e,
                self.donji_p13e,self.donji_p25e,self.donji_s2e,self.donji_s1e,
                self.donji_p17e,self.donji_p32e,self.donji_p27e,self.donji_p28e,
                self.donji_p10e,self.donji_p20e,self.donji_p18e,self.donji_gotovmat,
                self.donji_p19e,self.donji_p31e,self.donji_p30e,self.donji_puz24,
                self.donji_p26e,self.donji_puz29]
        self.motori = [self.srednji_c1.setId(1),self.gornji_bin3.setId(2),self.srednji_c3.setId(3),
            self.gornji_bin9.setId(4),self.srednji_c5.setId(5),self.gornji_bin6.setId(6),
            self.gornji_bin7.setId(7),self.gornji_bin4.setId(8),self.srednji_9.setId(9),
            self.gornji_bin8.setId(10),self.gornji_bin1.setId(11),self.gornji_bin12.setId(12),
            self.gornji_bin5.setId(13),self.gornji_bin2.setId(14),self.gornji_c15.setId(15),
            self.gornji_16.setId(16),self.gornji_17.setId(17),self.srednji_18.setId(18),
            self.srednji_19.setId(19),self.srednji_c20.setId(20),self.srednji_21.setId(21),
            self.gornji_22.setId(22),self.srednji_23.setId(23),self.srednji_c24.setId(24),
            self.srednji_25.setId(25),self.gornji_26.setId(26),self.srednji_27.setId(27),
            self.srednji_28.setId(28),self.gornji_c29.setId(29),self.srednji_30.setId(30),
            self.srednji_31.setId(31),self.srednji_31.setId(32)]
        #p9,p21,p22,p23,p24 imaju drugacij aimena
        self.pneumatika = [self.donji_p1.setId(1) ,self.donji_p2.setId(2),self.donji_p3.setId(3),
                    self.donji_p4.setId(4),self.donji_p5.setId(5),self.donji_p6.setId(6),self.donji_p7.setId(7),
                    self.donji_p8.setId(8),self.donji_p10.setId(10),self.donji_p11.setId(11),self.donji_p12.setId(12),
                    self.donji_p13.setId(13),self.donji_p14.setId(14),self.donji_p15.setId(15),self.donji_p16.setId(16),
                    self.donji_p17.setId(17),self.donji_p18.setId(18),self.donji_p19.setId(19),self.donji_p20.setId(20),
                    self.donji_p25.setId(25),self.donji_p26.setId(26),self.donji_p27.setId(27),self.donji_p28.setId(28),
                    self.donji_b29.setId(29),self.donji_p30.setId(30),self.donji_p31.setId(31),self.donji_p32.setId(32),
                    self.donji_s2.setId(21), self.donji_s1.setId(22) , self.donji_gotovpera.setId(9) ,
                    self.donji_gotmat3.setId(23) , self.donji_gotmat4.setId(24) ]
        for m in self.motori:
            m.stateChanged.connect(self.motori_state_changed)
        for p in self.motori:
            p.stateChanged.connect(self.pne_state_changed)            
    def initUI(self):
        self.setWindowIcon(QIcon('images/gear_blue.ico'))
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle('Biovita')
        self.show()
            
    def ulaziUpdate(self):
        #update senzore
        ulazi = self.state.updateSensors();
        n = 0
        for x in self.senzori:
            if(ulazi[n]==1):
                x.on();
            else:
                x.off();
            n = n + 1;
        #update ostale kontrole na prozoru    
        self.updateKomande()
        self.repaint() 
        
    def ulaziUpdate(self): 
        pass

    def motori_state_changed(self,ii):
        sender = self.sender()
        if(sender.isChecked()==True):
            self.state.ukljuciMotor(sender.getId())   
        else:
            self.state.iskljuciMotor(sender.getId()) 
            
    def pne_state_changed(self,ii):
        sender = self.sender()
        if(sender.isChecked()==True):
            self.state.ukljuciPneumatiku(sender.getId())   
        else:
            self.state.iskljuciPneumatiku(sender.getId()) 
