﻿'''
Created on Jan 15, 2016

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import sys
from ui import UiDialogVreme

class dialogzaVreme(QDialog,UiDialogVreme.Ui_Dialog):
    
    def __init__(self):
        super(dialogzaVreme,self).__init__()
        self.setupUi(self)
    



       
        
 
