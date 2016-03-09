from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
from ledmotori import LedMotor
  
class SenzMotori(QWidget):
    def __init__(self,parent):
        QWidget.__init__(self, parent)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(200,200,200))
        self.setPalette(p)
        
        hbox = QHBoxLayout()
        l1 = QVBoxLayout()
        l2 = QVBoxLayout()
        hbox.addLayout(l1)
        hbox.addLayout(l2)
        
        self.senz_motori = []
        
        tt = LedMotor(self,"BIN 1")
        self.senz_motori.append(tt)
        l1.addWidget(tt)
        
        tt = LedMotor(self,"BIN 2")
        self.senz_motori.append(tt)
        l1.addWidget(tt)

        tt = LedMotor(self,"BIN 3")
        self.senz_motori.append(tt)
        l1.addWidget(tt)

        tt = LedMotor(self,"BIN 4")
        self.senz_motori.append(tt)
        l1.addWidget(tt)

        tt = LedMotor(self,"BIN 5")
        self.senz_motori.append(tt)
        l1.addWidget(tt)

        tt = LedMotor(self,"BIN 6")
        self.senz_motori.append(tt)
        l1.addWidget(tt)

        tt = LedMotor(self,"BIN 7")
        self.senz_motori.append(tt)
        l1.addWidget(tt)

        tt = LedMotor(self,"BIN 8")
        self.senz_motori.append(tt)
        l1.addWidget(tt)

        tt = LedMotor(self,"BIN 9")
        self.senz_motori.append(tt)
        l1.addWidget(tt)

        tt = LedMotor(self,"Premix na vagu")
        self.senz_motori.append(tt)
        l1.addWidget(tt)
        l1.addWidget(QLabel("Mesaona klapna gore"))
        tt = LedMotor(self,"Otvorena")
        self.senz_motori.append(tt)
        l1.addWidget(tt)

        tt = LedMotor(self,"Zatvorena")
        self.senz_motori.append(tt)
        l1.addWidget(tt)        
        l1.addWidget(QLabel("Mesaona klapna dole"))
        tt = LedMotor(self,"Otvorena")
        self.senz_motori.append(tt)
        l1.addWidget(tt)

        tt = LedMotor(self,"Zatvorena")
        self.senz_motori.append(tt)
        l1.addWidget(tt)


        tt = LedMotor(self,"Redler u istovarnoj jami")
        self.senz_motori.append(tt)
        l2.addWidget(tt)           

        tt = LedMotor(self,"Puz u istovarnoj jami")
        self.senz_motori.append(tt)
        l2.addWidget(tt)  

        tt = LedMotor(self,"Elevator 1")
        self.senz_motori.append(tt)
        l2.addWidget(tt)        

        tt = LedMotor(self,"Elevator 2")
        self.senz_motori.append(tt)
        l2.addWidget(tt)
        
        tt = LedMotor(self,"Ventilator aspiratera")
        self.senz_motori.append(tt)
        l2.addWidget(tt)

        tt = LedMotor(self,"Aspirater precistac")
        self.senz_motori.append(tt)
        l2.addWidget(tt)

        tt = LedMotor(self,"Redler iznad silosa")
        self.senz_motori.append(tt)
        l2.addWidget(tt) 

        tt = LedMotor(self,"Puz za punjenje binova")
        self.senz_motori.append(tt)
        l2.addWidget(tt)

        tt = LedMotor(self,"Traka 1")
        self.senz_motori.append(tt)
        l2.addWidget(tt)        

        tt = LedMotor(self,"Traka 2")
        self.senz_motori.append(tt)
        l2.addWidget(tt)

        tt = LedMotor(self,"Mlin")
        self.senz_motori.append(tt)
        l2.addWidget(tt)

        tt = LedMotor(self,"Elevator Mlina")
        self.senz_motori.append(tt)
        l2.addWidget(tt)

        tt = LedMotor(self,"Dotok mat.u mlin")
        self.senz_motori.append(tt)
        l2.addWidget(tt)  


        tt = LedMotor(self,"Mesalica")
        self.senz_motori.append(tt)
        l2.addWidget(tt)

        tt = LedMotor(self,"Gotova roba iz mesalice")
        self.senz_motori.append(tt)
        l2.addWidget(tt)  

        tt = LedMotor(self,"Gotova roba prema ekst.")
        self.senz_motori.append(tt)
        l2.addWidget(tt)          
        self.setLayout(hbox) 
    def start(self,state):
        self.ctimer = QTimer()  
        QObject.connect(self.ctimer, SIGNAL("timeout()"), self.timerUpdate)
        self.state = state
        self.ctimer.start(330)
        
    def timerUpdate(self):
        i = self.state.getIndikator()
        n=0
        for ind in i:
            if(ind==1):
                self.senz_motori[n].on() 
            else:
                self.senz_motori[n].off()
            n=n+1
            if(n>=30):
                break;
        self.repaint();    
            
        
    
