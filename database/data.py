

class Bin:
    def __init__(self,bin = ''):
        self.artikl = bin
        self.kolicina = 0
        self.izmereno = 0
        self.max = 0
        self.koeficijent= 0
class NkBinovi:
    def __init__(self):
        
        self.binovi= []  
        for b in range(0,12):
            self.binovi.append(Bin(str(b+1))) 
                  
    def setBin(self, id, artikl,kolicina,max,koef):
        self.binovi[id].artikl = artikl        
        self.binovi[id].kolicina = kolicina   
        self.binovi[id].max = max
        self.binovi[id].koeficijent = koef        
    def __str__(self):
        rez = 'Binovi: \n'
        i = 1
        for b in self.binovi:
            rez = rez + str(i)+' '+ str(b.artikl) +'\n'
            i = i + 1
        return rez;
        
 