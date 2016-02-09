'''
Created on Jan 15, 2016

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import sys
from ui import UiDialogGotove

class dialogGotoveOdvage(QDialog,UiDialogGotove.Ui_Dialog):
    
    def __init__(self):
        super(dialogGotoveOdvage,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Gotove odvage")
    