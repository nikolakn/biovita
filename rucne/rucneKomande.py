'''
Created on Nov 5, 2015

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import sys
from PyQt4 import QtGui, QtCore
import UiRucne

class rucneProzor(QMainWindow,UiRucne.Ui_MainWindow):
    
    def __init__(self,state, parent=None):
        super(rucneProzor,self).__init__()
        self.setupUi(self)
        self.state = state
        self.initUI()
        self.ctimer = QtCore.QTimer()
        QtCore.QObject.connect(self.ctimer, SIGNAL("timeout()"), self.ulaziUpdate)
        self.ctimer.start(200)
        self.senzori =[self.donji_p1e,self.donji_p3e,self.donji_p11e,self.donji_p7e,
                self.donji_p8e,self.donji_p4e,self.donji_p2e,self.donji_p5e,self.donji_p6e,
                self.donji_p14e,self.donji_p15e,self.donji_p16e,self.donji_p12e,
                self.donji_p13e,self.donji_p25e,self.donji_s2e,self.donji_s1e,
                self.donji_p17e,self.donji_p32e,self.donji_p27e,self.donji_p28e,
                self.donji_p10e,self.donji_p20e,self.donji_p18e,self.donji_gotovmat,
                self.donji_p19e,self.donji_p31e,self.donji_p30e,self.donji_puz24,
                self.donji_p26e,self.donji_puz29]
    def initUI(self):
        self.setWindowIcon(QIcon('images/gear_blue.ico'))
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle('Biovita')
        self.show()
            
    def ulaziUpdate(self):
        ulazi = self.state.updateSensors();
        n = 0
        for x in self.senzori:
            if(ulazi[n]==1):
                x.on();
            else:
                x.off();
            n = n + 1;
        self.repaint() 


