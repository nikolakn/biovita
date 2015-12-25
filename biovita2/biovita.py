#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui, QtCore
#from time import sleep
from expanderi import Expanderi

class idQCheckBox(QtGui.QCheckBox):
    def setId(self,cid):
        self.cid = cid
    def getId(self):
        return self.cid    
class Glavna(QtGui.QMainWindow):
    
    def __init__(self):
        super(Glavna, self).__init__()
        self.expanderi = Expanderi()
        self.initUI()
        
    def initUI(self):      
        self.komande = []
        x = 0
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

 
        #btn1.clicked.connect(self.l1Clicked)            
        
        self.statusBar()
        
        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Event sender')
        self.show()
        
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