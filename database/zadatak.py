

class NkZadatak:
    def __init__(self):
        self.id = -1
        self.ime = ''
        self.kolicina = 0
        self.odvaga = 0
        self.poslednja = 0
        self.odradjeno = 0
        
    def set(self, id, ime,kolicina,odvaga,poslednja,odradjeno):
        self.id = id
        self.ime = ime
        self.kolicina = kolicina
        self.odvaga = odvaga
        self.poslednja = poslednja
        self.odradjeno = odradjeno        
        
    def __str__(self):
        rez = 'zadatak \n'
        rez = rez + 'id: ' +str(self.id) +'\n'
        rez = rez +  'ime: ' +self.ime+'\n'
        rez = rez +  'kolicina: ' +str(self.kolicina )+'\n'
        rez = rez +  'odvaga: ' +str(self.odvaga)  +'\n'
        rez = rez +  'poslednja: ' +str(self.poslednja) +'\n'
        rez = rez +  'odradjeno: ' +str(self.odradjeno ) +'\n'
        return rez;
 
class NkTrenutniZadatak:
    def __init__(self):
        self.id = -1
        self.komponenta = ''
        self.bin = 0
        self.zadato = 0
        self.izmereno = 0

        
    def set(self, id, komponenta,bin,zadato,izmereno):
        self.id = id
        self.komponenta = komponenta
        self.bin = bin
        self.zadato = zadato
        self.izmereno = izmereno
       

        
class NkKomponenta:
    def __init__(self):
        self.ime = ''
        self.procenat = 0.0
   
 
class NkReceptura:
    def __init__(self):
        self.id = -1
        self.ime = ''
        self.komponente= []  
        for b in range(0,12):
            self.komponente.append(NkKomponenta()) 
        
    def addKomponente(self, id, ime,procenat):
        self.komponente[id].ime = ime        
        self.komponente[id].procenat = procenat 
    def __str__(self):
    
        rez = 'Receptura \n'
        rez = rez + 'id: ' +str(self.id) +'\n'
        rez = rez +  'ime: ' +self.ime+'\n'
        for b in self.komponente:
            rez = rez + b.ime +" "+b.procenat+'\n '
        return rez;