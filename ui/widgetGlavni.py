
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import widgetBin 

class GlavniProzor(QWidget):
    
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        self.crna = QColor(0, 0, 0)
        self.crvena = QColor(255, 0, 0)
        self.bela = QColor(255, 255, 255)
        self.ukljuceno = False;
        
        self.loadedImage = QImage()
        self.loadedImage.load("images/el1.png")
        self.loadedImage2 = QImage()
        self.loadedImage2.load("images/el2.png")
        self.x = 28; #start
        self.y = 47; #izmedju dve susedne
        self.dx = 155; #izmedju dva para
        #bin1
        self.bin1 = widgetBin.Bin(self)
        self.bin1.move(self.x,30);
        
        self.bin2 = widgetBin.Bin(self)
        self.bin2.move(self.x+self.y,40);
        #bin2
        self.x = self.x + self.dx
        
        self.bin3 = widgetBin.Bin(self)
        self.bin3.move(self.x,30);
        
        self.bin4 = widgetBin.Bin(self)
        self.bin4.move(self.x+self.y,40);  
        #bin3
        self.x = self.x + self.dx
        
        self.bin5 = widgetBin.Bin(self)
        self.bin5.move(self.x,30);
        
        self.bin6 = widgetBin.Bin(self)
        self.bin6.move(self.x+self.y,40);
        #bin4
        self.x = self.x + self.dx
        
        self.bin7 = widgetBin.Bin(self)
        self.bin7.move(self.x,30);
        
        self.bin8 = widgetBin.Bin(self)
        self.bin8.move(self.x+self.y,40);
        #bin5
        self.x = self.x + self.dx
        
        self.bin9 = widgetBin.Bin(self)
        self.bin9.move(self.x,30);
        
        self.bin10 = widgetBin.Bin(self)
        self.bin10.move(self.x+self.y,40);
        #bin6
        self.x = self.x + self.dx
        
        self.bin11 = widgetBin.Bin(self)
        self.bin11.move(self.x,30);
        
        self.bin12 = widgetBin.Bin(self)
        self.bin12.move(self.x+self.y,40);
        
        self.ctimer = QTimer()
        QObject.connect(self.ctimer, SIGNAL("timeout()"), self.timerUpdate)
        self.ctimer.start(250)    
        self.bin1.on()
        self.bin2.on()
        self.bin3.on()
    def timerUpdate(self):
        self.bin1.animate();
        self.bin2.animate();
        self.bin3.animate();
        self.bin4.animate();
        self.bin5.animate();
        self.bin6.animate();
        self.bin7.animate();
        self.bin8.animate();
        self.bin9.animate();
        self.bin10.animate();
        self.bin11.animate();
        self.bin12.animate();
        
        
    def paintEvent(self, QPaintEvent):
        paint = QPainter(self)
        paint.setPen(Qt.black);
        #paint.setBrush(Qt.white);
        paint.drawRect(180, 180, 100, 58);
        paint.setBrush(Qt.black);
        paint.drawRect(165, 245, 50, 15);
        paint.setBrush(Qt.green); 
        paint.drawRect(170, 225, 50, 25);
        paint.setBrush(Qt.transparent); 
        paint.setPen(Qt.black);
        paint.drawRect(140, 320, 100, 60);
        
        paint.drawRect(450, 180, 100, 60);
        paint.drawRect(450, 250, 100, 60);
        paint.drawRect(450, 340, 100, 60);
        
        #paint.drawLine(200, 395, 380, 395);
        #paint.drawLine(380, 395, 380, 168);
        #paint.drawLine(380, 168, 500, 168);
        #paint.drawText(30,20,"Bin12")
        paint.drawImage(QPoint(150,155),self.loadedImage)
        paint.drawImage(QPoint(500,155),self.loadedImage2)
        #paint.drawRect(5, 110, 780, 25);
        paint.setBrush(Qt.green); 
        paint.drawRect(450, 245, 50, 15);
