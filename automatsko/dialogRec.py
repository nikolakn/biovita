'''
Created on Jan 15, 2016

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import sys
from ui import UiDialog1

class dialogzaRecept(QDialog,UiDialog1.Ui_Dialog):
    
    def __init__(self, parent, rec):
        super(dialogzaRecept,self).__init__()
        self.setupUi(self)
    
        self.comboBox.clear()
        for r in rec:
            self.comboBox.addItem(r.ime)
        
    def getIme(self):
        return str(self.comboBox.currentText())
        
    def getKolicina(self):
        x = 0
        try:
            x = float(self.lineEdit.text());
        except:
            return 0
        return x
        


       
        
 