
from PyQt4 import QtGui, QtCore

  
class Info(QtGui.QWidget):
    masinaklik = QtCore.pyqtSignal()
    def __init__(self,parent):
        QtGui.QWidget.__init__(self, parent)
        self.bsiva = QtGui.QColor(96, 96, 96)
        self.bcrvena = QtGui.QColor(255, 0, 0)
        self.bcrna = QtGui.QColor(0, 0, 0)
        self.bzelena = QtGui.QColor(0, 255, 0)
        
        self.setMinimumSize(60, 16)
        self.visina = 16
        self.boja = self.bcrna 
        
    def mousePressEvent(self, event):
        self.masinaklik.emit()
    def crvena(self):
        self.boja = QtCore.Qt.red 
    def siva(self):
        self.boja = QtCore.Qt.grey 
    def crna(self):
        self.boja = QtCore.Qt.black       
    def zelena(self):
        self.boja = QtCore.Qt.green
    def size(self,s):
        self.visina = s
    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.pen2 = QtGui.QPen(self.boja, 1,QtCore.Qt.SolidLine)
        qp.setPen(self.pen2)
        qp.setBrush(self.boja);
        qp.drawRect(0,0,60,self.visina )

        qp.end()       
