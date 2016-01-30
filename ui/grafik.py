
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
        self.font1 = QtGui.QFont("times", 12);
        self.font2 = QtGui.QFont("times", 8);
        self.fm = QtGui.QFontMetrics(self.font1);
        self.pixelsWide = self.fm.width("Grafikon odvage");
        self.pixelsHigh = self.fm.height();
        self.pixelsWide2 = self.fm.width("Tezina");
        self.pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        self.pen3 = QtGui.QPen(QtCore.Qt.black, 1,QtCore.Qt.DashLine)
        self.pen2 = QtGui.QPen(QtCore.Qt.red, 2,QtCore.Qt.SolidLine)
        self.dataT =[]
        #self.dataT = [(20,10),(30,20),(50,30),(70,40),(80,50),(120,offsetX),(230,70),(440,80),(5offsetX,90),(680,100)]
    def reset(self):
        self.dataT =[]
        self.repaint()
        
    def add(self,x,y):
        self.dataT.append((x,y))
        self.repaint()
        
    def paintEvent(self, e):
        h = self.height()
        w = self.width()
        offsetX = 60
        offsetY = 25
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setFont(self.font1)
        qp.setPen(self.crna)            
        qp.drawText(w/2-self.pixelsWide/2, 15 ,"Grafikon odvage") 
        qp.rotate(-90)
        qp.drawText(-h/2-self.pixelsWide2/2, 20, "Tezina")
        qp.rotate(90)        
        
        qp.setPen(self.pen)
        qp.drawLine(offsetX, 20, offsetX, h-offsetY)
        qp.drawLine(offsetX, h-offsetY, w-offsetY, h-offsetY)
        qp.setFont(self.font2)
        inc = (w-offsetY-offsetX)/10.0
        dx=offsetX+inc     
        qp.setPen(self.pen3)
        for i in range(100,1100,100):
            qp.drawLine(dx, 20, dx, h-20)
            qp.drawText(dx-10, h-10 ,str(i)) 
            dx = dx + inc  
            
        inc = (h-offsetY-20)/6.0
        dy=20       
        for i in range(1200,0,-200):
            qp.drawLine(55, dy, w-offsetY, dy)
            if(i>=1000):
                qp.drawText(30, dy+4 ,str(i)) 
            else:
                qp.drawText(35, dy+4 ,str(i)) 
            dy = dy + inc 
        
        qp.setPen(self.pen2)
        for x in range(0, len(self.dataT)-1):   
            prva=self.dataT[x]
            druga=self.dataT[x+1]  
            duzinaX = (w-offsetY-offsetX)
            duzinaY= (h-offsetY-20)
            pixelX = duzinaX/1000.0
            pixelY = duzinaY/1200.0
            x1=offsetX+prva[1]*pixelX
            y1= h-offsetY-prva[0]*pixelY
            x2=offsetX+druga[1]*pixelX
            y2= h-offsetY-druga[0]*pixelY  
            qp.drawLine(x1, y1, x2, y2)                   
        qp.end()       
