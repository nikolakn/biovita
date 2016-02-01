
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
        
        self.bin3 = widgetBin.Bin(self)
        self.bin3.move(self.x,30);
        
        self.bin4 = widgetBin.Bin(self)
        self.bin4.move(self.x+self.y,40);
        #bin4
        self.x = self.x + self.dx
        
        self.bin3 = widgetBin.Bin(self)
        self.bin3.move(self.x,30);
        
        self.bin4 = widgetBin.Bin(self)
        self.bin4.move(self.x+self.y,40);
        self.bin4.move(self.x+self.y,40);
        #bin5
        self.x = self.x + self.dx
        
        self.bin3 = widgetBin.Bin(self)
        self.bin3.move(self.x,30);
        
        self.bin4 = widgetBin.Bin(self)
        self.bin4.move(self.x+self.y,40);
        self.bin4.move(self.x+self.y,40);
        #bin6
        self.x = self.x + self.dx
        
        self.bin3 = widgetBin.Bin(self)
        self.bin3.move(self.x,30);
        
        self.bin4 = widgetBin.Bin(self)
        self.bin4.move(self.x+self.y,40);
                
    def paintEvent(self, QPaintEvent):
        paint = QPainter(self)
        paint.setPen(Qt.black);
        paint.setBrush(Qt.white);
        #paint.drawRect(5, 5, 780, 25);
        #paint.drawText(30,20,"Bin12")
        
        #paint.drawRect(5, 110, 780, 25);
         
