
from PyQt4 import QtGui, QtCore

  
class Bin(QtGui.QWidget):
    
    def __init__(self,parent):
        QtGui.QWidget.__init__(self, parent)
        self.crna = QtGui.QColor(0, 0, 0)
        self.crvena = QtGui.QColor(255, 0, 0)
        self.bela = QtGui.QColor(255, 255, 255)
        self.ukljuceno = False;
        self.dx = 10;
        self.dy = 10;
        self.x = 4;
        self.y = 0;
        self.setMinimumSize(40, 100)
        self.loadedImage = QtGui.QImage()
        self.loadedImage.load("images/bin.png")
    def on(self):
        self.ukljuceno = True; 
        self.repaint() 
    def off(self):
        self.ukljuceno = False;
        self.repaint() 

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)

        qp.setPen(self.crna)
        qp.setBrush(self.crna)
        qp.drawImage(QtCore.QPoint(0, 15),self.loadedImage)
        #qp.drawRect(0, 0, 40, 80);
   
        qp.end()       
