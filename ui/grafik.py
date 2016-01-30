
from PyQt4 import QtGui, QtCore

  
class NkGrafik(QtGui.QWidget):
    
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

    def paintEvent(self, e):
        h = self.height()
        w = self.width()
        font1 = QtGui.QFont("times", 12);
        font2 = QtGui.QFont("times", 8);
        fm = QtGui.QFontMetrics(font1);
        pixelsWide = fm.width("Grafikon odvage");
        pixelsHigh = fm.height();
        pixelsWide2 = fm.width("Tezina");
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setFont(font1)
        qp.setPen(self.crna)            
        qp.drawText(w/2-pixelsWide/2, 15 ,"Grafikon odvage") 
        qp.rotate(-90)
        qp.drawText(-h/2-pixelsWide2/2, 20, "Tezina")
        qp.rotate(90)        
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(60, 20, 60, h-25)
        qp.drawLine(60, h-25, w-25, h-25)
        qp.setFont(font2)
        inc = (w-25-60)/10.0
        dx=60+inc
        pen = QtGui.QPen(QtCore.Qt.black, 1,QtCore.Qt.DashLine)
        qp.setPen(pen)
        for i in range(100,1100,100):
            qp.drawLine(dx, 20, dx, h-20)
            qp.drawText(dx-10, h-10 ,str(i)) 
            dx = dx + inc  
            
        inc = (h-25-20)/6.0
        dy=20
        
        for i in range(1400,0,-200):
            qp.drawLine(55, dy, w-25, dy)
            #qp.drawText(dx-10, h-10 ,str(i)) 
            dy = dy + inc 
        #qp.setPen(self.crna)
        #qp.setBrush(self.crvena)
        #qp.drawEllipse(self.dx/2-self.x, self.dy/2-5, self.dx, self.dy)         
        qp.end()       
