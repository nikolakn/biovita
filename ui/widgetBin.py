
from PyQt4 import QtGui, QtCore

  
class Bin(QtGui.QWidget):
    
    def __init__(self,parent):
        QtGui.QWidget.__init__(self, parent)
        self.plava = QtGui.QColor(216, 228, 248)
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
        self.nivo = 15
        self.pen2 = QtGui.QPen(self.plava, 1,QtCore.Qt.SolidLine)
    def on(self):
        self.ukljuceno = True; 
        self.repaint() 
    def off(self):
        self.ukljuceno = False;
        self.repaint() 
        
    def animate(self):
        self.nivo = self.nivo + 2
        if (self.nivo > 50):
            self.nivo = 15;
        self.repaint()
    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawImage(QtCore.QPoint(0, 15),self.loadedImage)
        qp.setPen(self.pen2)
        qp.setBrush(self.plava);
        qp.drawRect(2,17,37,15)
        if(self.ukljuceno==True):
            qp.drawRect(2,17,37,self.nivo)
       
   
        qp.end()       
