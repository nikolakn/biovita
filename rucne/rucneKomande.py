'''
Created on Nov 5, 2015

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import UiRucne

class rucneProzor(QMainWindow,UiRucne.Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(rucneProzor,self).__init__()
        self.setupUi(self)
        self.initUI()
    
        
    def initUI(self):
        self.setWindowIcon(QIcon('images/gear_blue.ico'))
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle('Biovita')
        self.show()
            
   
