
from PyQt4 import QtGui, QtCore

  
class Masina(QtGui.QWidget):
    masinaklik = QtCore.pyqtSignal()
    def __init__(self,parent):
        QtGui.QWidget.__init__(self, parent)
        self.plava = QtGui.QColor(175, 249, 250)
        self.crvena = QtGui.QColor(255, 0, 0)
        self.crna = QtGui.QColor(0, 0, 0)
        self.ukljuceno = False;
        self.ispustanje = False;
        self.setMinimumSize(110, 97)
        self.loadedImage = QtGui.QImage()
        self.loadedImage.load("images/mas.png")
        self.nivo = 15
        self.maxnivo = 0
        self.pen2 = QtGui.QPen(self.plava, 1,QtCore.Qt.SolidLine)
        self.pen3 = QtGui.QPen(self.crna, 2,QtCore.Qt.SolidLine)
        self.isprazni()
        #self.napuni();
        #self.prazni();
    def isprazni(self):
        self.ukljuceno = False;
        self.ispustanje = False;
        self.nivo = 63-self.maxnivo
    def napuni(self):
        self.ukljuceno = False;
        self.ispustanje = False;
        self.nivo = 15
    def puni(self):
        self.ukljuceno = True;
    def prazni(self):
        self.ukljuceno = True;
        self.ispustanje = True ;   
        
    def mousePressEvent(self, event):
        self.masinaklik.emit()
    def on(self):
        self.ukljuceno = True; 
        self.repaint() 
    def off(self):
        self.ukljuceno = False;
        self.repaint() 
    def setmax(self,n):
        self.maxnivo = n
    def animate(self):
        if(self.ukljuceno==True):
            self.nivo = self.nivo + 2
            if (self.nivo > (60-self.maxnivo)):
                self.nivo = 15;
            self.repaint()
    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawImage(QtCore.QPoint(0, 15),self.loadedImage)
        qp.setPen(self.pen2)
        qp.setBrush(self.plava);
        qp.drawRect(2,17,97,self.nivo+self.maxnivo)
        
        #self.bin
        if(self.ukljuceno==True):
            qp.drawRect(2,17,97,self.nivo+self.maxnivo)
        if(self.ispustanje == False):
            qp.drawRect(0,82,101,200)
            qp.setPen(self.pen3)
            qp.drawLine(0,82,101,82)
        qp.end()       
