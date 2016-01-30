'''
Created on Jan 15, 2016

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import sys
from ui import UiRucne
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
            self.srednji_31.setId(31),self.srednji_32.setId(32)]
            
        self.senzori =[self.donji_p1e,self.donji_p2e,self.donji_p3e,self.donji_p4e,
            self.donji_p5e,self.donji_p6e,self.donji_p7e,self.donji_p8e,self.donji_gotovmat,
            self.donji_p10e,self.donji_p11e,self.donji_p12e,self.donji_p13e,self.donji_p14e,
            self.donji_p15e,self.donji_p16e,self.donji_p17e,self.donji_p18e,self.donji_p19e,
            self.donji_p20e,self.donji_s2e,self.donji_s1e,self.donji_puz24,self.donji_p25e,
            self.donji_p26e,self.donji_p27e,self.donji_p28e,self.donji_puz29,
            self.donji_p30e,self.donji_p31e,self.donji_p32e]            
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
        for p in self.pneumatika:
            p.stateChanged.connect(self.pne_state_changed)    

        self.srednji_ispusti_1.clicked.connect(lambda:self.btn_ispusti_1()) 
        self.srednji_ispusti_2.clicked.connect(lambda:self.btn_ispusti_2()) 
        self.srednji_ispusti_3.clicked.connect(lambda:self.btn_ispusti_3()) 
        self.srednji_ispusti_4.clicked.connect(lambda:self.btn_ispusti_4()) 
        self.srednji_ispusti_5.clicked.connect(lambda:self.btn_ispusti_5()) 
        self.srednji_ispusti_6.clicked.connect(lambda:self.btn_ispusti_6())         
        self.srednji_dugme_zatvorisve.clicked.connect(lambda:self.btn_ispusti_zatvorisve()) 
        
        self.srednji_ele2_1.clicked.connect(lambda:self.btn_ele2_1()) 
        self.srednji_ele2_2.clicked.connect(lambda:self.btn_ele2_2()) 
        self.srednji_ele2_3.clicked.connect(lambda:self.btn_ele2_3()) 
        self.srednji_ele2_4.clicked.connect(lambda:self.btn_ele2_4()) 
        self.srednji_ele2_5.clicked.connect(lambda:self.btn_ele2_5()) 
        self.srednji_ele2_6.clicked.connect(lambda:self.btn_ele2_6()) 
        
        self.srednji_ele1_1.clicked.connect(lambda:self.btn_ele1_1())
        self.srednji_ele1_2.clicked.connect(lambda:self.btn_ele1_2())
        self.srednji_ele1_3.clicked.connect(lambda:self.btn_ele1_3())
        self.srednji_ele1_4.clicked.connect(lambda:self.btn_ele1_4())
        
        self.srednji_psilosa_1.clicked.connect(lambda:self.btn_psilosa_1())
        self.srednji_psilosa_2.clicked.connect(lambda:self.btn_psilosa_2())
        self.srednji_psilosa_3.clicked.connect(lambda:self.btn_psilosa_3())
        
        self.srednji_dugme_start.clicked.connect(lambda:self.btn_start()) 
        self.srednji_dugme_stop.clicked.connect(lambda:self.btn_stop()) 
        
        self.srednji_bin1.clicked.connect(lambda:self.btn_bin1())
        self.srednji_bin2.clicked.connect(lambda:self.btn_bin2())
        self.srednji_bin3.clicked.connect(lambda:self.btn_bin3())
        self.srednji_bin4.clicked.connect(lambda:self.btn_bin4())
        self.srednji_bin5.clicked.connect(lambda:self.btn_bin5())
        self.srednji_bin6.clicked.connect(lambda:self.btn_bin6())
        self.srednji_bin7.clicked.connect(lambda:self.btn_bin7())
        self.srednji_bin8.clicked.connect(lambda:self.btn_bin8())
        self.srednji_bin9.clicked.connect(lambda:self.btn_bin9())
        
        self.srednji_dugme_ukljuci.clicked.connect(lambda:self.btn_ukljuci()) 
        self.srednji_dugme_iskljuci.clicked.connect(lambda:self.btn_iskljuci())
    def initUI(self):
        self.setWindowIcon(QIcon('images/gear_blue.ico'))
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle('Biovita')
        self.show()
        self.ctimer = QTimer()
        QObject.connect(self.ctimer, SIGNAL("timeout()"), self.ulaziUpdate)
        self.ctimer.start(200)

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
        
    def updateKomande(self): 
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
            
    def btn_ispusti_1(self):
        self.donji_p14.setChecked(True);
        self.donji_p15.setChecked(False);
        self.donji_p16.setChecked(False);
        self.donji_p12.setChecked(False);
        self.donji_p13.setChecked(False);
        self.donji_p6.setChecked(False);

    def btn_ispusti_2(self):
        self.donji_p14.setChecked(False);
        self.donji_p15.setChecked(True);
        self.donji_p16.setChecked(False);
        self.donji_p12.setChecked(False);
        self.donji_p13.setChecked(False);
        self.donji_p6.setChecked(False);
    def btn_ispusti_3(self):
        self.donji_p14.setChecked(False);
        self.donji_p15.setChecked(False);
        self.donji_p16.setChecked(True);
        self.donji_p12.setChecked(False);
        self.donji_p13.setChecked(False);
        self.donji_p6.setChecked(False);
    def btn_ispusti_4(self):
        self.donji_p14.setChecked(False);
        self.donji_p15.setChecked(False);
        self.donji_p16.setChecked(False);
        self.donji_p12.setChecked(True);
        self.donji_p13.setChecked(False);
        self.donji_p6.setChecked(False);
    def btn_ispusti_5(self):
        self.donji_p14.setChecked(False);
        self.donji_p15.setChecked(False);
        self.donji_p16.setChecked(False);
        self.donji_p12.setChecked(False);
        self.donji_p13.setChecked(True);
        self.donji_p6.setChecked(False);
    def btn_ispusti_6(self):
        self.donji_p14.setChecked(False);
        self.donji_p15.setChecked(False);
        self.donji_p16.setChecked(False);
        self.donji_p12.setChecked(False);
        self.donji_p13.setChecked(False);
        self.donji_p6.setChecked(True);    
        
    def btn_ispusti_zatvorisve(self):
        self.donji_p14.setChecked(False);
        self.donji_p15.setChecked(False);
        self.donji_p16.setChecked(False);
        self.donji_p12.setChecked(False);
        self.donji_p13.setChecked(False);
        self.donji_p6.setChecked(False);  
        self.srednji_ispusti_1.setCheckable(False);
        self.srednji_ispusti_2.setCheckable(False);
        self.srednji_ispusti_3.setCheckable(False);
        self.srednji_ispusti_4.setCheckable(False);
        self.srednji_ispusti_5.setCheckable(False);
        self.srednji_ispusti_6.setCheckable(False);
        self.srednji_ispusti_1.setCheckable(True);
        self.srednji_ispusti_2.setCheckable(True);
        self.srednji_ispusti_3.setCheckable(True);
        self.srednji_ispusti_4.setCheckable(True);
        self.srednji_ispusti_5.setCheckable(True);
        self.srednji_ispusti_6.setCheckable(True);
        
    def btn_ele2_1(self):
        self.donji_p7.setChecked(False);
        self.donji_p8.setChecked(False);
        self.donji_p4.setChecked(False);
        self.donji_p2.setChecked(False);
        self.donji_p5.setChecked(True);         
    def btn_ele2_2(self):
        self.donji_p7.setChecked(True);
        self.donji_p8.setChecked(False);
        self.donji_p4.setChecked(False);
        self.donji_p2.setChecked(False);
        self.donji_p5.setChecked(False);
    def btn_ele2_3(self):
        self.donji_p7.setChecked(False);
        self.donji_p8.setChecked(True);
        self.donji_p4.setChecked(False);
        self.donji_p2.setChecked(False);
        self.donji_p5.setChecked(False);
    def btn_ele2_4(self):
        self.donji_p7.setChecked(False);
        self.donji_p8.setChecked(False);
        self.donji_p4.setChecked(True);
        self.donji_p2.setChecked(False);
        self.donji_p5.setChecked(False);
    def btn_ele2_5(self):
        self.donji_p7.setChecked(False);
        self.donji_p8.setChecked(False);
        self.donji_p4.setChecked(False);
        self.donji_p2.setChecked(True);
        self.donji_p5.setChecked(False);
    def btn_ele2_6(self):
        self.donji_p7.setChecked(False);
        self.donji_p8.setChecked(False);
        self.donji_p4.setChecked(False);
        self.donji_p2.setChecked(False);
        self.donji_p5.setChecked(False);  

    def btn_ele1_1(self):
        self.donji_p1.setChecked(False);
        self.donji_p3.setChecked(False);
        self.donji_p11.setChecked(False);
    def btn_ele1_2(self):
        self.donji_p1.setChecked(False);
        self.donji_p3.setChecked(False);
        self.donji_p11.setChecked(True);
    def btn_ele1_3(self):
        self.donji_p1.setChecked(False);
        self.donji_p3.setChecked(True);
        self.donji_p11.setChecked(False);
    def btn_ele1_4(self):
        self.donji_p1.setChecked(True);
        self.donji_p3.setChecked(False);
        self.donji_p11.setChecked(False);        
        
    def btn_psilosa_1(self):
        self.donji_s2.setChecked(False);
        self.donji_s1.setChecked(True);
        self.donji_p25.setChecked(False);    
    def btn_psilosa_2(self):
        self.donji_s2.setChecked(True);
        self.donji_s1.setChecked(False);
        self.donji_p25.setChecked(False); 
    def btn_psilosa_3(self):
        self.donji_s2.setChecked(False);
        self.donji_s1.setChecked(False);
        self.donji_p25.setChecked(True);         
        
    def btn_start(self):
        self.srednji_25.setChecked(True); 
        self.srednji_dugme_start.setEnabled(False)
        self.srednji_dugme_stop.setEnabled(True)
    def btn_stop(self):
        self.srednji_25.setChecked(False); 
        self.srednji_dugme_start.setEnabled(True)
        self.srednji_dugme_stop.setEnabled(False)        

    def btn_bin1(self):
        self.donji_p17.setChecked(True);
        self.donji_p32.setChecked(False);
        self.donji_p10.setChecked(False);
        self.donji_p20.setChecked(False);
        self.donji_p31.setChecked(False);
        self.donji_p30.setChecked(False);
           
        self.donji_b29.setChecked(False);
        self.srednji_19.setChecked(False);
        
    def btn_bin2(self):
        self.donji_p17.setChecked(False);
        self.donji_p32.setChecked(False);
        self.donji_p10.setChecked(True);
        self.donji_p20.setChecked(False);
        self.donji_p31.setChecked(False);
        self.donji_p30.setChecked(False);
           
        self.donji_b29.setChecked(False);
        self.srednji_19.setChecked(False);

    def btn_bin3(self):
        self.donji_p17.setChecked(False);
        self.donji_p32.setChecked(False);
        self.donji_p10.setChecked(False);
        self.donji_p20.setChecked(False);
        self.donji_p31.setChecked(True);
        self.donji_p30.setChecked(False);
           
        self.donji_b29.setChecked(False);
        self.srednji_19.setChecked(False);
    def btn_bin4(self):
        self.donji_p17.setChecked(False);
        self.donji_p32.setChecked(False);
        self.donji_p10.setChecked(False);
        self.donji_p20.setChecked(False);
        self.donji_p31.setChecked(True);
        self.donji_p30.setChecked(True);
           
        self.donji_b29.setChecked(False);
        self.srednji_19.setChecked(False);
    def btn_bin5(self):
        self.donji_p17.setChecked(False);
        self.donji_p32.setChecked(False);
        self.donji_p10.setChecked(True);
        self.donji_p20.setChecked(True);
        self.donji_p31.setChecked(False);
        self.donji_p30.setChecked(False);
           
        self.donji_b29.setChecked(False);
        self.srednji_19.setChecked(False);
    def btn_bin6(self):
        self.donji_p17.setChecked(True);
        self.donji_p32.setChecked(True);
        self.donji_p10.setChecked(False);
        self.donji_p20.setChecked(False);
        self.donji_p31.setChecked(False);
        self.donji_p30.setChecked(False);
           
        self.donji_b29.setChecked(False);
        self.srednji_19.setChecked(False);
    def btn_bin7(self):
        self.donji_p17.setChecked(False);
        self.donji_p32.setChecked(False);
        self.donji_p10.setChecked(False);
        self.donji_p20.setChecked(False);
        self.donji_p31.setChecked(False);
        self.donji_p30.setChecked(False);
           
        self.donji_b29.setChecked(False);
        self.srednji_19.setChecked(False);
    def btn_bin8(self):
        self.donji_p17.setChecked(False);
        self.donji_p32.setChecked(False);
        self.donji_p10.setChecked(False);
        self.donji_p20.setChecked(False);
        self.donji_p31.setChecked(False);
        self.donji_p30.setChecked(False);
           
        self.donji_b29.setChecked(False);
        self.srednji_19.setChecked(True);
    def btn_bin9(self):
        self.donji_p17.setChecked(False);
        self.donji_p32.setChecked(False);
        self.donji_p10.setChecked(False);
        self.donji_p20.setChecked(False);
        self.donji_p31.setChecked(False);
        self.donji_p30.setChecked(False);
           
        self.donji_b29.setChecked(True);
        self.srednji_19.setChecked(True);        
    def btn_ukljuci(self):
        self.srednji_dugme_ukljuci.setEnabled(False);
        self.srednji_dugme_iskljuci.setEnabled(True);
        self.srednji_30.setChecked(True);

    def btn_iskljuci(self):  
        self.srednji_dugme_ukljuci.setEnabled(True);
        self.srednji_dugme_iskljuci.setEnabled(False);
        self.srednji_30.setChecked(False);   