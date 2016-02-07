'''
Created on Jan 15, 2016

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import sys
from ui import UiDialogBin

class dialogzaBin(QDialog,UiDialogBin.Ui_Dialog):
    
    def __init__(self, parent,a,k):
        super(dialogzaBin,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Bin")
        self.artikl.setText(str(a))
        self.koeficijent.setText(str(k))
    def getArtikl(self):
        return str(self.artikl.text())
        
    def getKoeficijent(self):
        return str(self.koeficijent.text())
        


       
        
 