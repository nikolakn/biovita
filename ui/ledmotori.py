
from PyQt4 import QtGui, QtCore

  
class LedMotor(QtGui.QWidget):
    
    def __init__(self,parent,text):
        QtGui.QWidget.__init__(self, parent)
        self.crna = QtGui.QColor(0, 0, 0)
        self.crvena = QtGui.QColor(255, 0, 0)
        self.bela = QtGui.QColor(255, 255, 255)
        self.zelena = QtGui.QColor(0, 255, 0)
        self.ukljuceno = False;
        self.dx = 10;
        self.dy = 10;
        self.x = 4;
        self.y = 0;
        self.text=text
        self.setMinimumSize(self.dx+len(text)*6.5, self.dy+13)
    def on(self):
        self.ukljuceno = True; 
        self.repaint() 
    def off(self):
        self.ukljuceno = False;
        self.repaint() 
    def setText(self,t):
        self.text = t
        self.setMinimumSize(self.dx+t.size()*6.5, self.dy+13)
    def setIconSize(self,size):
        pass;
    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        if (self.ukljuceno == True):
            qp.setPen(self.crna)
            qp.setBrush(self.zelena)
            qp.drawEllipse(self.dx/2-self.x, self.dy/2-5, self.dx, self.dy)
        else:
            qp.setPen(self.bela)
            qp.setBrush(self.crna)
            qp.drawEllipse(self.dx/2-self.x, self.dy/2-5, self.dx, self.dy)  
        qp.setPen(self.crna)            
        qp.drawText(self.dx/2+self.x+5, self.dy/2+5,self.text)    
        qp.end()       
