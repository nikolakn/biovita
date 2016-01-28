from PyQt4 import QtGui, QtCore
#from time import sleep
from expanderi import expanderi
from led import Led
import serial 

class idQCheckBox(QtGui.QCheckBox):
    def setId(self,cid):
        self.cid = cid
        return self
    def getId(self):
        return self.cid  