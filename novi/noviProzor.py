'''
Created on Jan 15, 2016

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import sys
import datetime
from ui import UiNovi
from sys import platform as _platform
import serial 
import time
from rucne import rucneKomande
from database import dbhelpers,data,zadatak


class Novi(QMainWindow,UiNovi.Ui_MainWindow):
    
    def __init__(self,state, parent=None):
        super(Novi,self).__init__()
        self.setupUi(self)

        self.initUI()
        
    def initUI(self):
        self.setWindowIcon(QIcon('images/gear_blue.ico'))
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle('BIOVITA')
        self.show()

        #timer
        #self.ctimer = QTimer()
        #QObject.connect(self.ctimer, SIGNAL("timeout()"), self.timerUpdate)
        #self.ctimer.start(100)
        
        self.vaga2timer = QTimer()
        QObject.connect(self.vaga2timer, SIGNAL("timeout()"), self.secundaTimerUpdate)
        self.vaga2timer.start(1000)
        #tajmeri    
        self.scrollArea.horizontalScrollBar().setValue(60);
    def secundaTimerUpdate(self): 
        pass
     

    def status(self,msg):
        pass
        
