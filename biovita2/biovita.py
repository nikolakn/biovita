#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui, QtCore
#from time import sleep
from expanderi import expanderi
from led import Led
import serial 

class idQCheckBox(QtGui.QCheckBox):
    def setId(self,cid):
        self.cid = cid
    def getId(self):
        return self.cid    
class Glavna(QtGui.QMainWindow):
    
    def __init__(self):
        super(Glavna, self).__init__()
        self.expanderi = expanderi.Expanderi()
        self.initUI()
        try:
            self.port = serial.Serial("/dev/ttyAMA0" ,9600 , parity=serial.PARITY_NONE , stopbits =serial.STOPBITS_ONE , bytesize=serial.EIGHTBITS,timeout=0)
            self.port.open()
        except:
            print("reska seriski port")
            self.port.close()     
   
    def initUI(self):      
        self.komande = []
        x = 0;
        y = 10
        for i in range(0,64):         
            temp = idQCheckBox(self)
            temp.move(x*25+10, y)
            temp.setId(i)
            self.komande.append(temp)
            self.komande[i].stateChanged.connect(self.state_changed)
            x = x + 1
            if (x >=16):
                x = 0
                y =y +40
        self.ulazi = []
        y = 200;
        x = 0;
        for i in range(0,32): 
            temp = Led(self)
            self.ulazi.append(temp)
            temp.move(x*25+10, y)
            x = x + 1
            if (x >=16):
                x = 0
                y =y +40          
        
        self.statusBar()
        
        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('Event sender')
        self.show()
        self.ctimer = QtCore.QTimer()
        QtCore.QObject.connect(self.ctimer, QtCore.SIGNAL("timeout()"), self.ulaziUpdate)
        self.ctimer.start(100)
        
    def ulaziUpdate(self):
        u = self.expanderi.getUlazi()
        n = 0;        
        for i in self.ulazi:
            if (u[n]==1):
                i.on();
            else:
                i.off();
            n = n + 1;
        ch = self.port.readline();
        print(ch)
        self.repaint()      
    def state_changed(self,ii):
        sender = self.sender()
        if(sender.isChecked()==True):
            self.expanderi.ukljuci(sender.getId())   
        else:
            self.expanderi.iskljuci(sender.getId()) 

    def closeEvent(self, event):
        self.expanderi.close()

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Glavna()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
