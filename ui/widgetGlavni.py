
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
  
class GlavniProzor(QWidget):
    
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        self.crna = QColor(0, 0, 0)
        self.crvena = QColor(255, 0, 0)
        self.bela = QColor(255, 255, 255)
        self.ukljuceno = False;
        self.dx = 10;
        self.dy = 10;
        self.x = 4;
        self.y = 0;


    def paintEvent(self, QPaintEvent):
        paint = QPainter(self)
        paint.setPen(Qt.black);
        paint.setBrush(Qt.white);
        paint.drawRect(5, 5, 800, 25);
        paint.drawText(30,20,"Bin12")
        
        paint.drawRect(5, 110, 800, 25);
        paint.drawText(30,125,"Bin1")          
