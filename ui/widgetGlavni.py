
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import widgetBin 
import widgetMasina
import widgetInfo

class GlavniProzor(QWidget):
    
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        self.crna = QColor(0, 0, 0)
        self.crvena = QColor(255, 0, 0)
        self.bela = QColor(255, 255, 255)
        self.ukljuceno = False;
        self.slike1 = [QImage(),QImage(),QImage(),QImage(),QImage(),QImage(),QImage()
                      ,QImage(),QImage(),QImage(),QImage(),QImage(),QImage(),QImage(),
                      QImage(),QImage(),QImage(),QImage()]
        self.slike2 = [QImage(),QImage(),QImage(),QImage(),QImage(),QImage(),QImage()
                        ,QImage(),QImage(),QImage(),QImage(),QImage(),QImage()]              
        for i in range(0,18):
            self.slike1[i].load("images/el1_"+str(i+1)+".png")
        #self.loadedImage2 = QImage()
        for i in range(0,9):
            self.slike2[i].load("images/el2_"+str(i+1)+".png")
        #self.loadedImage2 = QImage()
        self.slika1frame = 0;
        self.slika2frame = 0;
        #self.loadedImage2.load("images/el2.png")
        self.x = 28; #start
        self.y = 47; #izmedju dve susedne
        self.dx = 155; #izmedju dva para
        #bin1
        self.bin1 = widgetBin.Bin(self,1)
        self.bin1.move(self.x,30);
        
        self.bin7 = widgetBin.Bin(self,7)
        self.bin7.move(self.x+self.y,40);
       
        self.x = self.x + self.dx
        
        self.bin2 = widgetBin.Bin(self,2)
        self.bin2.move(self.x,30);
        
        self.bin8 = widgetBin.Bin(self,8)
        self.bin8.move(self.x+self.y,40);  
        #bin3
        self.x = self.x + self.dx
        
        self.bin3 = widgetBin.Bin(self,3)
        self.bin3.move(self.x,30);
        
        self.bin9 = widgetBin.Bin(self,9)
        self.bin9.move(self.x+self.y,40);
        #bin4
        self.x = self.x + self.dx
        
        self.bin4 = widgetBin.Bin(self,4)
        self.bin4.move(self.x,30);
        
        self.bin10 = widgetBin.Bin(self,10)
        self.bin10.move(self.x+self.y,40);
        #bin5
        self.x = self.x + self.dx
        
        self.bin5 = widgetBin.Bin(self,5)
        self.bin5.move(self.x,30);
        
        self.bin11 = widgetBin.Bin(self,11)
        self.bin11.move(self.x+self.y,40);
        #bin6
        self.x = self.x + self.dx
        
        self.bin6 = widgetBin.Bin(self,6)
        self.bin6.move(self.x,30);
        
        self.bin12 = widgetBin.Bin(self,12)
        self.bin12.move(self.x+self.y,40);
        
        
        self.vaga = widgetMasina.Masina(self)
        self.vaga.move(180,160);

        self.mlin = widgetMasina.Masina(self)
        self.mlin.move(140,294);
 

        self.mesaonaUlaz = widgetMasina.Masina(self)
        self.mesaonaUlaz.move(450,150);
        self.mesaona = widgetMasina.Masina(self)
        self.mesaona.setmax(25)
        self.mesaona.move(450,230);
        self.mesaonaIzalz = widgetMasina.Masina(self)
        self.mesaonaIzalz.move(450,310);
        
        self.i1 = widgetInfo.Info(self)
        self.i1.zelena()
        self.i1.size(32)
        self.i1.move(175,230);
        
        self.i2 = widgetInfo.Info(self)
        self.i2.crna()
        self.i2.move(165,250);
 
        self.ctimer = QTimer()
        QObject.connect(self.ctimer, SIGNAL("timeout()"), self.timerUpdate)
        self.ctimer.start(150)    
        self.vagaOn = False
    def timerUpdate(self):
        self.mesaonaUlaz.animate();
        self.mesaona.animate();
        self.mesaonaIzalz.animate();
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
        self.vaga.animate();
        self.mlin.animate();
        self.slika1frame = self.slika1frame + 1
        if(self.slika1frame>=18):
            self.slika1frame = 0;
        self.slika2frame = self.slika2frame + 1
        if(self.slika2frame>=9):
            self.slika2frame = 0;    
        self.repaint() 
        
    def paintEvent(self, QPaintEvent):
        paint = QPainter(self)
        paint.setPen(Qt.black);
        #paint.setBrush(Qt.white);
        '''
        paint.drawRect(180, 180, 100, 58);
        paint.setBrush(Qt.black);
        paint.drawRect(165, 245, 50, 15);
        
        if(self.vagaOn):
            paint.setBrush(Qt.green); 
        else:
            paint.setBrush(Qt.red);
        paint.drawRect(170, 225, 50, 25);
        '''
        
        paint.setBrush(Qt.transparent); 
        paint.setPen(Qt.black);
        #paint.drawRect(140, 320, 100, 60);
        
        #paint.drawRect(450, 180, 100, 60);
        #paint.drawRect(450, 250, 100, 60);
        #paint.drawRect(450, 335, 100, 60);
        
        #paint.drawLine(200, 395, 380, 395);
        #paint.drawLine(380, 395, 380, 168);
        #paint.drawLine(380, 168, 500, 168);
        #paint.drawText(30,20,"Bin12")
        paint.drawImage(QPoint(150,158),self.slike1[self.slika1frame])
        paint.drawImage(QPoint(500,160),self.slike2[self.slika2frame])
        #paint.drawRect(5, 110, 780, 25);
        paint.setBrush(Qt.green); 
        paint.drawRect(450, 245, 50, 15);
        paint.setBrush(Qt.black);
        paint.drawRect(450, 302, 50, 15);
