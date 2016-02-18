
from PyQt4 import QtGui, QtCore

  
class Bin(QtGui.QWidget):
    binklik = QtCore.pyqtSignal(int)
    def __init__(self,parent,bin):
        QtGui.QWidget.__init__(self, parent)
        self.bin = bin
        self.plava = QtGui.QColor(216, 228, 248)
        self.crvena = QtGui.QColor(255, 0, 0)
        self.crna = QtGui.QColor(0, 0, 0)
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
        self.pen3 = QtGui.QPen(self.crna, 1,QtCore.Qt.SolidLine)
    def mousePressEvent(self, event):
        self.binklik.emit(self.bin)
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
        
        #self.bin
        if(self.ukljuceno==True):
            qp.drawRect(2,17,37,self.nivo)
        qp.setPen(self.pen3)
        qp.drawText(15,28,str(self.bin))
        qp.end()       
