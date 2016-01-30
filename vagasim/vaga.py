'''
Created on Jan 15, 2016

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import sys
import serial 
import random

class sim(QMainWindow):
    def __init__(self):
        super(sim,self).__init__()
        try:
            self.port = serial.Serial("COM1" ,9600 , parity=serial.PARITY_NONE , stopbits =serial.STOPBITS_ONE , bytesize=serial.EIGHTBITS,timeout=0)
            self.port.close()
            self.port.open()
        except:
            print("Greska seriski port")
            print sys.exc_info()
            sys.exit(0)   
        self.initUI()
        
    def initUI(self):
        lab1 = QLabel("Vaga:",self)
        lab1.move(5,0);
        self.com1 =  QLineEdit(self)
        btn1 = QPushButton("start", self)
        btn1.move(10, 50)
        btn2 = QPushButton("stop", self)
        btn2.move(150, 50)
        btnr1 = QPushButton("reset", self)
        btnr1.move(10, 150)
        self.com1.move(35,0);
        btn1.clicked.connect(self.l1Clicked)            
        btn2.clicked.connect(self.l2Clicked)
        btnr1.clicked.connect(self.r1Clicked)  
        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('Biovita')
        self.show()
        self.num = 0.0
        self.raste = False
        self.ctimer = QTimer()
        QObject.connect(self.ctimer, SIGNAL("timeout()"), self.timerUpdate)
        self.ctimer.start(100)
        self.moving=True
    def l1Clicked(self):
        self.raste = True
        self.moving=True
    def l2Clicked(self):
        self.raste = False
        self.moving=False
    def r1Clicked(self):  
        self.num = 0.0
        self.raste = False
        self.moving=False
    def timerUpdate(self):
        if (self.raste):
            self.num = self.num + 0.33
        s=chr(2)
        q=chr(71)
        e=chr(77)
        
        nustr =  '%6.2f' % self.num
        nustr = "        " + nustr
        nustr = nustr[-8:]
        #rr = random.randint(1, 10)
        if (self.moving==False):
            mess = s+nustr+q+ '\r\n'
        else:
            mess = s+nustr+e+ '\r\n'      
        ch = self.port.write(mess )
        self.com1.setText(mess)


def main():
    
    app = QApplication(sys.argv)
    ex = sim()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()        