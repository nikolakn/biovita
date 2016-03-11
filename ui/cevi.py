
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport


            
class Cevi():
    
    crna = QColor(0, 0, 0)
    crvena = QColor(255, 0, 0)
    bela = QColor(255, 255, 255)
    zalena = QColor(0, 255, 0)
    plava = QColor(0, 175, 239)
    nar = QColor(245, 134, 52)
    braon = QColor(164, 94, 77)
    zuta = QColor(255, 242, 18)
    def __init__(self):

        self.list_cevi = [Cev_E2_S5(),Cev_E2_R_iznad_S(),Cev_Ka_Elevatoru5(),Cev_E2_S4(),Cev_E1_R_iznad_S(),Cev_E1_URampa(),
            Cev_E1_Aspirater(),Cev_E1_binovi(),Cev_E2_aspirater(),Cev_E2_binovi(),Cev_E2_bin_ext(),
            Cev_Aspirater_E2(),Cev_Traka2_E2(),Cev_Traka2_E1(),Cev_puz_jama_E1(),Cev_redJama_puz(),
            Cev_puziznadbinova(),Cev_P1_6(), Cev_P2_5(),Cev_P3_4(),Cev_bin7(),Cev_zasun1(),Cev_zasun6(),
            Cev_zasun2(),Cev_zasun5(),Cev_zasun3(),Cev_zasun4(),Cev_vaga_binovi(),Cev_vaga1(),Cev_vaga2(),
            Cev_gotova_bin7()]
        
    def nacrtaj(self, paint):
        for c in self.list_cevi:
            c.nacrtaj(paint)
            
class Cev_Ka_Elevatoru5():
    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.plava
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(140, 70,140,170)
        else:
            pass

class Cev_E2_S5():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.plava
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(278,172,278, 115)
           paint.drawLine(278, 115,566,115)
           paint.drawLine(608, 115,785,115)
           paint.drawLine(785,115,785,98)

        else:
            pass   

class Cev_E2_S4():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.plava
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(416,170,416, 130)
           paint.drawLine(416, 130,566,130)
           paint.drawLine(608, 130,812,130)
           paint.drawLine(812,130,812,98)

        else:
            pass    

class Cev_E1_R_iznad_S():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.nar
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(617,104,617, 184)
           paint.drawLine(617, 184,540, 184)
           paint.drawLine(540, 184,540, 532)
           paint.drawLine(540, 532,450, 532)
        else:
            pass        

class Cev_E1_URampa():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.nar
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(644,104,644, 200)

        else:
            pass  

class Cev_E1_Aspirater():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.nar
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(665,104,665, 327)

        else:
            pass    

class Cev_E1_binovi():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.nar
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(686,104,686, 200)
           paint.drawLine(686, 200,925, 200)
           paint.drawLine(925, 200,925, 230)
        else:
            pass  

class Cev_E2_R_iznad_S():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.plava
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(832,98,832, 160)
           paint.drawLine(832, 160,520, 160)
           paint.drawLine(520, 160,520, 520)
           paint.drawLine(520, 520,450, 520)
        else:
            pass  

class Cev_E2_aspirater():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.plava
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(851,98,851, 191)
           paint.drawLine(851,210,851, 335)
           paint.drawLine(851, 335,727, 335)

        else:
            pass  

class Cev_E2_binovi():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.plava
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(874,98,874, 160)
           paint.drawLine(874, 160,939, 160)
           paint.drawLine(939, 160,939, 230)

        else:
            pass    

class Cev_E2_bin_ext():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.plava
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(903,98,903, 120)
           paint.drawLine(903, 120,1112, 120)
           paint.drawLine(1112, 120,1112, 13)
           paint.drawLine(1112, 13,1180, 13)
        else:
            pass   

class Cev_Aspirater_E2():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.plava
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(725,387,785,387)
           paint.drawLine(785,387,785, 840)

        else:
            pass   

class Cev_Traka2_E2():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.plava
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(433,426,510,426)
           paint.drawLine(552,426,564,426)
           paint.drawLine(610,426,730,426)
           paint.drawLine(730,426,730,840)
        else:
            pass   

class Cev_Traka2_E1():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.nar
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(433,819,540,819)
           paint.drawLine(540,819,540,840)

        else:
            pass     


class Cev_puz_jama_E1():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.nar
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(620,843,620,680)
           paint.drawLine(620,680,668,680)
           paint.drawLine(668,680,668,700)
        else:
            pass   

class Cev_redJama_puz():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.nar
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(601,949,656,949)
        else:
            pass    

class Cev_staticke():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.crna
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 7, Qt.SolidLine))   
           paint.drawLine(140,201,140,212)
           paint.drawLine(277,201,277,212)
           paint.drawLine(416,201,416,212)
           
           paint.drawLine(140,381,140,384)
           paint.drawLine(277,381,277,384)
           paint.drawLine(416,381,416,384)
        else:
            pass    

class Cev_puziznadbinova():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.crna
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 5, Qt.SolidLine))   
           paint.drawLine(916,254,1357,254)

        else:
            pass              
            
class Cev_P1_6():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.crna
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 5, Qt.SolidLine))   
           paint.drawLine(921,255,921,283)
           paint.drawLine(921,309,921,333)
        else:
            pass  

class Cev_P2_5():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.crna
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 5, Qt.SolidLine))   
           paint.drawLine(1053,255,1053,283)
           paint.drawLine(1053,309,1053,333)
        else:
            pass  

class Cev_P3_4():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.crna
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 5, Qt.SolidLine))   
           paint.drawLine(1184,255,1184,283)
           paint.drawLine(1184,309,1184,333)
        else:
            pass    

class Cev_bin7():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.crna
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 5, Qt.SolidLine))   
           paint.drawLine(1383,284,1383,381)
        else:
            pass 

class Cev_zasun1():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.crna
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 6, Qt.SolidLine))   
           paint.drawLine(898,365,898,391)
        else:
            pass    

class Cev_zasun6():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.crna
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 6, Qt.SolidLine))   
           paint.drawLine(945,366,945,370)
        else:
            pass  

class Cev_zasun2():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.crna
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 6, Qt.SolidLine))   
           paint.drawLine(1030,365,1030,391)
        else:
            pass   

class Cev_zasun5():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.crna
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 6, Qt.SolidLine))   
           paint.drawLine(1078,367,1078,370)
        else:
            pass    

class Cev_zasun3():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.crna
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 6, Qt.SolidLine))   
           paint.drawLine(1161,366,1161,391)
        else:
            pass   

class Cev_zasun4():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.crna
        
    def nacrtaj(self,paint):
        if(self.radi == False):

           paint.setPen(QPen(self.boja, 6, Qt.SolidLine))   
           paint.drawLine(1207,367,1207,370)
        else:
            pass   

class Cev_vaga_binovi():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.crna
        
    def nacrtaj(self,paint):
        if(self.radi == False):
            
           paint.setPen(QPen(self.boja, 6, Qt.DashLine))   
           paint.drawLine(878,594,1400,594)
           paint.drawLine(1054,603,1054,621)
        else:
            pass
        
class Cev_vaga1():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.braon
        
    def nacrtaj(self,paint):
        if(self.radi == False):
            
           paint.setPen(QPen(self.boja, 6, Qt.SolidLine))   
           paint.drawLine(1614,447,1614,665)
        else:        
            pass  

class Cev_vaga2():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.braon
        
    def nacrtaj(self,paint):
        if(self.radi == False):
            
           paint.setPen(QPen(self.boja, 6, Qt.SolidLine))   
           paint.drawLine(1653,447,1653,562)
        else:        
            pass  

class Cev_gotova_bin7():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.braon
        
    def nacrtaj(self,paint):
        if(self.radi == False):
            
           paint.setPen(QPen(self.boja, 6, Qt.SolidLine))   
           paint.drawLine(1535,288,1590,288)
           paint.drawLine(1505,288,1397,288)
           paint.drawLine(1397,288,1397,382)
        else:        
            pass     

class SilosData():
    def __init__(self,x,y):
        self.anim = True;
        self.nivo = 20;
        self.x = x
        self.y = y
class Silosi():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.crna
        self.sil=[SilosData(170,642),SilosData(308,642),SilosData(448,642),
                  SilosData(448,247),SilosData(308,247), SilosData(170,247)]
                    
    def start(self,silos):
        self.sil[silos+1].animn = True
        self.sil[silos+1].nivo = 20
    def stop(self,silos):
        self.sil[silos+1].animn = False
        self.sil[silos+1].nivo = 20
        
    def animate(self):
        for x in  self.sil:  
            if(x.anim == True):
                x.nivo=x.nivo + 1
                if(x.nivo>=120):
                    x.nivo = 20
    def nacrtaj(self,paint):
        self.animate()
        if(self.radi == False):
           for x in  self.sil:
               paint.setPen(QPen(Cevi.crna, 1, Qt.SolidLine))
               paint.setBrush(Qt.gray)               
               paint.drawRect(x.x,x.y,14,120)
               paint.setBrush(QColor(255, 242, 18))
               paint.drawRect(x.x,x.y+x.nivo,14,120-x.nivo)
           
        else:        
            pass  

class Binovi():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.crna
        self.sil=[SilosData(906,401),SilosData(1039,401),SilosData(1167,401),
            SilosData(1217,383),SilosData(1089,383),SilosData(956,383),SilosData(1390,390)]
                    
    def start(self,silos):
        self.sil[silos+1].animn = True
        self.sil[silos+1].nivo = 20
    def stop(self,silos):
        self.sil[silos+1].animn = False
        self.sil[silos+1].nivo = 20
        
    def animate(self):
        for x in  self.sil:  
            if(x.anim == True):
                x.nivo=x.nivo + 1
                if(x.nivo>=100):
                    x.nivo = 20
    def nacrtaj(self,paint):
        self.animate()
        if(self.radi == False):
           for x in  self.sil:
               paint.setPen(QPen(Cevi.crna, 1, Qt.SolidLine))
               paint.setBrush(Qt.gray)               
               paint.drawRect(x.x,x.y,12,100)
               paint.setBrush(QColor(255, 242, 18))
               paint.drawRect(x.x,x.y+x.nivo,12,100-x.nivo)
           
        else:        
            pass    

class Binovi89():

    
    def __init__(self): 
        self.radi = False
        self.boja = Cevi.crna
        self.sil=[SilosData(1278,354),SilosData(1314,354)]
                    
    def start(self,silos):
        self.sil[silos+1].animn = True
        self.sil[silos+1].nivo = 20
    def stop(self,silos):
        self.sil[silos+1].animn = False
        self.sil[silos+1].nivo = 20
        
    def animate(self):
        for x in  self.sil:  
            if(x.anim == True):
                x.nivo=x.nivo + 1
                if(x.nivo>=60):
                    x.nivo = 20
    def nacrtaj(self,paint):
        self.animate()
        if(self.radi == False):
           for x in  self.sil:
               paint.setPen(QPen(Cevi.crna, 1, Qt.SolidLine))
               paint.setBrush(Qt.gray)               
               paint.drawRect(x.x,x.y,10,60)
               paint.setBrush(QColor(255, 242, 18))
               paint.drawRect(x.x,x.y+x.nivo,10,60-x.nivo)
           
        else:        
            pass             