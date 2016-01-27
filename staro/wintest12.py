#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui, QtCore
import wiringpi2 as wiringpi
from time import sleep


pins = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]
pins2 = [81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96]

dioda1=95
dioda2=96

rele1=65
rele2=66
rele3=67
rele4=68

wiringpi.wiringPiSetup()
#rezervise adrese pocevsi od 65 pa nadalje za expander podesen na 0x20
wiringpi.mcp23s17Setup(65,0,0x20) # first pin,spi port,i2c address
#adrese od 81 pa navise za expander na 1
wiringpi.mcp23s17Setup(81,1,0x20) # first pin,spi port,i2c address

for i in pins:
    wiringpi.pinMode(i,1)     # sets pin of mcp23s17-0 to output
for i in pins2:
    wiringpi.pinMode(i,1)

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        self.sl1 = False
        self.sl2 = False
        self.sr1 = False
        self.sr2 = False
        self.sr3 = False
        self.sr4 = False
        self.initUI()
        
    def initUI(self):      

        btn1 = QtGui.QPushButton("led 1", self)
        btn1.move(10, 50)

        btn2 = QtGui.QPushButton("led 2", self)
        btn2.move(150, 50)
  
        btnr1 = QtGui.QPushButton("rele 1", self)
        btnr1.move(10, 150)

        btnr2 = QtGui.QPushButton("rele 2", self)
        btnr2.move(150, 150)

        btnr3 = QtGui.QPushButton("rele 3", self)
        btnr3.move(300, 150)

        btnr4 = QtGui.QPushButton("rele 4", self)
        btnr4.move(450, 150) 
   
        btn1.setStyleSheet("background-color: #696969")
        btn2.setStyleSheet("background-color: #696969")
        btnr1.setStyleSheet("background-color: #696969")
        btnr2.setStyleSheet("background-color: #696969")
        btnr3.setStyleSheet("background-color: #696969")
        btnr4.setStyleSheet("background-color: #696969")

        btn1.clicked.connect(self.l1Clicked)            
        btn2.clicked.connect(self.l2Clicked)
        btnr1.clicked.connect(self.r1Clicked)  
        btnr2.clicked.connect(self.r2Clicked)  
        btnr3.clicked.connect(self.r3Clicked)  
        btnr4.clicked.connect(self.r4Clicked)  

        
        self.statusBar()
        
        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Event sender')
        self.show()
        
    def l1Clicked(self):   
        sender = self.sender()
        if self.sl1== False:
            sender.setStyleSheet("background-color: green")
            wiringpi.digitalWrite(dioda1,1)
            self.sl1 = True
        else:
            sender.setStyleSheet("background-color: #696969")
            wiringpi.digitalWrite(dioda1,0)
            self.sl1 = False			
        
    def l2Clicked(self):  
        sender = self.sender()
        if self.sl2== False:
            wiringpi.digitalWrite(dioda2,1)
            sender.setStyleSheet("background-color: green")
            self.sl2 = True
        else:
            wiringpi.digitalWrite(dioda2,0)
            sender.setStyleSheet("background-color: #696969")
            self.sl2 = False

    def r1Clicked(self):  
        sender = self.sender()
        if self.sr1== False:
            wiringpi.digitalWrite(rele1,1)
            sender.setStyleSheet("background-color: green")
            self.sr1 = True
        else:
            sender.setStyleSheet("background-color: #696969")
            wiringpi.digitalWrite(rele1,0)
            self.sr1 = False
    def r2Clicked(self):  
        sender = self.sender()
        if self.sr2== False:
            wiringpi.digitalWrite(rele2,1)
            sender.setStyleSheet("background-color: green")
            self.sr2 = True
        else:
            sender.setStyleSheet("background-color: #696969")
            wiringpi.digitalWrite(rele2,0)
            self.sr2 = False
    def r3Clicked(self):  
        sender = self.sender()
        if self.sr3== False:
            sender.setStyleSheet("background-color: green")
            wiringpi.digitalWrite(rele3,1)
            self.sr3 = True
        else:
            sender.setStyleSheet("background-color: #696969")
            wiringpi.digitalWrite(rele3,0)
            self.sr3 = False
    def r4Clicked(self):  
        sender = self.sender()
        if self.sr4== False:
            sender.setStyleSheet("background-color: green")
            wiringpi.digitalWrite(rele4,1)
            self.sr4 = True
        else:
            sender.setStyleSheet("background-color: #696969")
            wiringpi.digitalWrite(rele4,0)
            self.sr4 = False

    def closeEvent(self, event):
        for i in pins:   
            wiringpi.digitalWrite(i,0)
            wiringpi.pinMode(i,0)
    

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
