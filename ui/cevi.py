
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport


            
class Cevi():
    
    crna = QColor(0, 0, 0)
    crvena = QColor(255, 0, 0)
    bela = QColor(255, 255, 255)
    zalena = QColor(0, 255, 0)
    plava = QColor(0, 175, 239)
    nar = QColor(245, 134, 52)
    def __init__(self):

        self.list_cevi = [Cev_E2_S5(),Cev_E2_R_iznad_S(),Cev_Ka_Elevatoru5(),Cev_E2_S4(),Cev_E1_R_iznad_S(),Cev_E1_URampa(),
            Cev_E1_Aspirater(),Cev_E1_binovi(),Cev_E2_aspirater(),Cev_E2_binovi(),Cev_E2_bin_ext(),
            Cev_Aspirater_E2(),Cev_Traka2_E2(),Cev_Traka2_E1(),Cev_puz_jama_E1(),Cev_redJama_puz(),
            Cev_puziznadbinova()]
        
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