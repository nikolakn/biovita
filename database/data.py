

class Bin:
    def __init__(self,bin = ''):
        self.artikl = bin
        self.kolicina = 0
        self.izmereno = 0

class NkBinovi:
    def __init__(self):
        
        self.binovi= []  
        for b in range(0,12):
            self.binovi.append(Bin(str(b+1))) 
                  
        
    def __str__(self):
        rez = 'Binovi \n'
        for b in self.binovi:
            rez = rez + b.artikl +'\n'

        return rez;
        
 