

class NkZadatak:
    def __init__(self):
        self.id = -1
        self.ime = ''
        self.kolicina = 0
        self.odvaga = 0
        self.poslednja = 0
        self.odradjeno = 0
        
    def append(self, id, ime,kolicina,odvaga,poslednja,odradjeno):
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