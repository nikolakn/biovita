﻿'''
Created on Jan 15, 2016

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import sys
from ui import UiAuto
from sys import platform as _platform
import serial 

class autoProzor(QMainWindow,UiAuto.Ui_MainWindow):
    
    def __init__(self,state, parent=None):
        super(autoProzor,self).__init__()
        self.setupUi(self)
        if _platform == "linux" or _platform == "linux2":
            try:
                self.port = serial.Serial("/dev/ttyAMA0" ,9600 , parity=serial.PARITY_NONE , stopbits =serial.STOPBITS_ONE , bytesize=serial.EIGHTBITS,timeout=0)
                self.port.open()
            except:
                print("Greska seriski port")
                sys.exit(0)   
        self.state = state
        self.initUI()
        
    def initUI(self):
        self.setWindowIcon(QIcon('images/gear_blue.ico'))
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle('Biovita')
        self.show()
        self.ctimer = QTimer()
        QObject.connect(self.ctimer, SIGNAL("timeout()"), self.timerUpdate)
        self.ctimer.start(200)
        
    def timerUpdate(self):
        ulazi = self.state.updateSensors();
        if _platform == "linux" or _platform == "linux2":
            ch = self.port.readline();
            print(ch)
            #self.com1.setText("vaga")
        self.repaint()        