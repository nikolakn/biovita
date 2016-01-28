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
        self.motori = [self.srednji_31.setId(31),self.srednji_31.setId(32)]
        self.pneumatika = [self.donji_p1.setId(1) ,self.donji_p2.setId(2)]
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
