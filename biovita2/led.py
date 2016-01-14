
from PyQt4 import QtGui, QtCore

  
class Led(QtGui.QWidget):
    
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.crna = QtGui.QColor(0, 0, 0)
        self.crvena = QtGui.QColor(255, 0, 0)
        self.bela = QtGui.QColor(255, 255, 255)
        self.on = False;
        self.dx = 10;
        self.dy = 10;
        self.setMinimumSize(self.dx, self.dy)
    def on(self):
        self.on = True;    
    def off(self):
        self.on = False;
    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        if (self.on == True):
            qp.setPen(self.crna)
            qp.setBrush(self.crvena)
            qp.drawEllipse(self.dx/2, self.dy/2, self.dx, self.dy)
        else:
            qp.setPen(self.crna)
            qp.setBrush(self.bela)
            qp.drawEllipse(self.dx/2, self.dy/2, self.dx, self.dy)       
        qp.end()       