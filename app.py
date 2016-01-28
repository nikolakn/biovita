'''
Created on Jan 15, 2016

@author: nikola
'''

from expanderi import expanderi
   
#cuva podatke kroz celu applikaciju
#samo ova klasa moze da ukljucuje i iskljucuje expandere   
class AppState:
    
    def __init__(self):
        self.ulazi = {}
        self.motori = {}
        self.pneumatike = {}
        
        self.ulazi['u1']=0
        self.ulazi['u2']=0 
        self.ulazi['u3']=0
        self.ulazi['u4']=0
        self.ulazi['u5']=0 
        self.ulazi['u6']=0
        self.ulazi['u7']=0
        self.ulazi['u8']=0 
        self.ulazi['u9']=0
        self.ulazi['u10']=0
        self.ulazi['u11']=0 
        self.ulazi['u12']=0
        self.ulazi['u13']=0
        self.ulazi['u14']=0 
        self.ulazi['u15']=0
        self.ulazi['u16']=0
        self.ulazi['u17']=0 
        self.ulazi['u18']=0
        self.ulazi['u19']=0
        self.ulazi['u20']=0 
        self.ulazi['u21']=0
        self.ulazi['u22']=0
        self.ulazi['u23']=0 
        self.ulazi['u24']=0
        self.ulazi['u25']=0
        self.ulazi['u26']=0 
        self.ulazi['u27']=0
        self.ulazi['u28']=0
        self.ulazi['u29']=0 
        self.ulazi['u30']=0
        self.ulazi['u31']=0
        self.ulazi['u32']=0 

        self.pneumatike['p1']=0
        self.pneumatike['p2']=0 
        self.pneumatike['p3']=0
        self.pneumatike['p4']=0
        self.pneumatike['p5']=0 
        self.pneumatike['p6']=0
        self.pneumatike['p7']=0
        self.pneumatike['p8']=0 
        self.pneumatike['p9']=0
        self.pneumatike['p10']=0
        self.pneumatike['p11']=0 
        self.pneumatike['p12']=0
        self.pneumatike['p13']=0
        self.pneumatike['p14']=0 
        self.pneumatike['p15']=0
        self.pneumatike['p16']=0
        self.pneumatike['p17']=0 
        self.pneumatike['p18']=0
        self.pneumatike['p19']=0
        self.pneumatike['p20']=0 
        self.pneumatike['p21']=0
        self.pneumatike['p22']=0
        self.pneumatike['p23']=0 
        self.pneumatike['p24']=0
        self.pneumatike['p25']=0
        self.pneumatike['p26']=0 
        self.pneumatike['p27']=0
        self.pneumatike['p28']=0
        self.pneumatike['p29']=0 
        self.pneumatike['p30']=0
        self.pneumatike['p31']=0
        self.pneumatike['p32']=0 
        
        self.motori['m1']=0
        self.motori['m2']=0 
        self.motori['m3']=0
        self.motori['m4']=0
        self.motori['m5']=0 
        self.motori['m6']=0
        self.motori['m7']=0
        self.motori['m8']=0 
        self.motori['m9']=0
        self.motori['m10']=0
        self.motori['m11']=0 
        self.motori['m12']=0
        self.motori['m13']=0
        self.motori['m14']=0 
        self.motori['m15']=0
        self.motori['m16']=0
        self.motori['m17']=0 
        self.motori['m18']=0
        self.motori['m19']=0
        self.motori['m20']=0 
        self.motori['m21']=0
        self.motori['m22']=0
        self.motori['m23']=0 
        self.motori['m24']=0
        self.motori['m25']=0
        self.motori['m26']=0 
        self.motori['m27']=0
        self.motori['m28']=0
        self.motori['m29']=0 
        self.motori['m30']=0
        self.motori['m31']=0
        self.motori['m32']=0 
        
        self.expanderi = expanderi.Expanderi()
    def updateSensors(self):
        u = self.expanderi.getUlazi()
        n = 0;  
      
        for k,v in self.ulazi.iteritems():
            if (u[n]==1):
                self.ulazi[k] = 1

            else:
                self.ulazi[k] = 0
            n = n + 1;
        return self.ulazi.values()
        
    def close(self):
        self.expanderi.close();
        print('Izlaz')    
    '''
    mapiranje portova
    -m1     -p1  
    -m2     -p2
    -m3     -p3
    .       .
    .       .
    .       .
    -m30    -p30
    -m31    -p31
    -m32    -p32
    
    '''
    def ukljuciMotor(self,id):
        self.motori[id] = 1
        id = "m"+str(id)
        if (id=='m1'):
            self.expanderi.ukljuci(16)
        if (id=='m2'):
            self.expanderi.ukljuci(17)
        if (id=='m3'):
            self.expanderi.ukljuci(18)
        if (id=='m4'):
            self.expanderi.ukljuci(19)
        if (id=='m5'):
            self.expanderi.ukljuci(20)
        if (id=='m6'):
            self.expanderi.ukljuci(21)
        if (id=='m7'):
            self.expanderi.ukljuci(22)
        if (id=='m8'):
            self.expanderi.ukljuci(23)
        if (id=='m9'):
            self.expanderi.ukljuci(24)
        if (id=='m10'):
            self.expanderi.ukljuci(25)
        if (id=='m11'):
            self.expanderi.ukljuci(26)
        if (id=='m12'):
            self.expanderi.ukljuci(27)
        if (id=='m13'):
            self.expanderi.ukljuci(28)
        if (id=='m14'):
            self.expanderi.ukljuci(29)
        if (id=='m15'):
            self.expanderi.ukljuci(30)
        if (id=='m16'):
            self.expanderi.ukljuci(31)
        if (id=='m17'):
            self.expanderi.ukljuci(0)
        if (id=='m18'):
            self.expanderi.ukljuci(1)
        if (id=='m19'):
            self.expanderi.ukljuci(2)
        if (id=='m20'):
            self.expanderi.ukljuci(3)
        if (id=='m21'):
            self.expanderi.ukljuci(4)
        if (id=='m22'):
            self.expanderi.ukljuci(5)
        if (id=='m23'):
            self.expanderi.ukljuci(6)
        if (id=='m24'):
            self.expanderi.ukljuci(7)
        if (id=='m25'):
            self.expanderi.ukljuci(8)
        if (id=='m26'):
            self.expanderi.ukljuci(9)
        if (id=='m27'):
            self.expanderi.ukljuci(10)
        if (id=='m28'):
            self.expanderi.ukljuci(11)
        if (id=='m29'):
            self.expanderi.ukljuci(12)
        if (id=='m30'):
            self.expanderi.ukljuci(13)
        if (id=='m31'):
            self.expanderi.ukljuci(14)
        if (id=='m32'):
            self.expanderi.ukljuci(15)
            
    def iskljuciMotor(self,id):
        self.motori[id] = 0
        id = "m"+str(id)
        if (id=='m1'):
            self.expanderi.iskljuci(16)
        if (id=='m2'):
            self.expanderi.iskljuci(17)
        if (id=='m3'):
            self.expanderi.iskljuci(18)
        if (id=='m4'):
            self.expanderi.iskljuci(19)
        if (id=='m5'):
            self.expanderi.iskljuci(20)
        if (id=='m6'):
            self.expanderi.iskljuci(21)
        if (id=='m7'):
            self.expanderi.iskljuci(22)
        if (id=='m8'):
            self.expanderi.iskljuci(23)
        if (id=='m9'):
            self.expanderi.iskljuci(24)
        if (id=='m10'):
            self.expanderi.iskljuci(25)
        if (id=='m11'):
            self.expanderi.iskljuci(26)
        if (id=='m12'):
            self.expanderi.iskljuci(27)
        if (id=='m13'):
            self.expanderi.iskljuci(28)
        if (id=='m14'):
            self.expanderi.iskljuci(29)
        if (id=='m15'):
            self.expanderi.iskljuci(30)
        if (id=='m16'):
            self.expanderi.iskljuci(31)
        if (id=='m17'):
            self.expanderi.iskljuci(0)
        if (id=='m18'):
            self.expanderi.iskljuci(1)
        if (id=='m19'):
            self.expanderi.iskljuci(2)
        if (id=='m20'):
            self.expanderi.iskljuci(3)
        if (id=='m21'):
            self.expanderi.iskljuci(4)
        if (id=='m22'):
            self.expanderi.iskljuci(5)
        if (id=='m23'):
            self.expanderi.iskljuci(6)
        if (id=='m24'):
            self.expanderi.iskljuci(7)
        if (id=='m25'):
            self.expanderi.iskljuci(8)
        if (id=='m26'):
            self.expanderi.iskljuci(9)
        if (id=='m27'):
            self.expanderi.iskljuci(10)
        if (id=='m28'):
            self.expanderi.iskljuci(11)
        if (id=='m29'):
            self.expanderi.iskljuci(12)
        if (id=='m30'):
            self.expanderi.iskljuci(13)
        if (id=='m31'):
            self.expanderi.iskljuci(14)
        if (id=='m32'):
            self.expanderi.iskljuci(15)   

    def ukljuciPneumatiku(self,id):
        self.pneumatike[id] = 1
        id = "p"+str(id)
        if (id=='p1'):
            self.expanderi.ukljuci(63)
        if (id=='p2'):
            self.expanderi.ukljuci(62)
        if (id=='p3'):
            self.expanderi.ukljuci(61)
        if (id=='p4'):
            self.expanderi.ukljuci(60)
        if (id=='p5'):
            self.expanderi.ukljuci(59)
        if (id=='p6'):
            self.expanderi.ukljuci(58)
        if (id=='p7'):
            self.expanderi.ukljuci(57)
        if (id=='p8'):
            self.expanderi.ukljuci(56)
        if (id=='p9'):
            self.expanderi.ukljuci(55)
        if (id=='p10'):
            self.expanderi.ukljuci(54)
        if (id=='p11'):
            self.expanderi.ukljuci(53)
        if (id=='p12'):
            self.expanderi.ukljuci(52)
        if (id=='p13'):
            self.expanderi.ukljuci(51)
        if (id=='p14'):
            self.expanderi.ukljuci(50)
        if (id=='p15'):
            self.expanderi.ukljuci(49)
        if (id=='p16'):
            self.expanderi.ukljuci(48)
        if (id=='p17'):
            self.expanderi.ukljuci(47)
        if (id=='p18'):
            self.expanderi.ukljuci(46)
        if (id=='p19'):
            self.expanderi.ukljuci(45)
        if (id=='p20'):
            self.expanderi.ukljuci(44)
        if (id=='p21'):
            self.expanderi.ukljuci(43)
        if (id=='p22'):
            self.expanderi.ukljuci(42)
        if (id=='p23'):
            self.expanderi.ukljuci(41)
        if (id=='p24'):
            self.expanderi.ukljuci(40)
        if (id=='p25'):
            self.expanderi.ukljuci(39)
        if (id=='p26'):
            self.expanderi.ukljuci(38)
        if (id=='p27'):
            self.expanderi.ukljuci(37)
        if (id=='p28'):
            self.expanderi.ukljuci(36)
        if (id=='p29'):
            self.expanderi.ukljuci(35)
        if (id=='p30'):
            self.expanderi.ukljuci(34)
        if (id=='p31'):
            self.expanderi.ukljuci(33)
        if (id=='p32'):
            self.expanderi.ukljuci(32)  
        
    def iskljuciPneumatiku(self,id):
        self.pneumatike[id] = 0
        id = "p"+str(id)
        if (id=='p1'):
            self.expanderi.iskljuci(63)
        if (id=='p2'):
            self.expanderi.iskljuci(62)
        if (id=='p3'):
            self.expanderi.iskljuci(61)
        if (id=='p4'):
            self.expanderi.iskljuci(60)
        if (id=='p5'):
            self.expanderi.iskljuci(59)
        if (id=='p6'):
            self.expanderi.iskljuci(58)
        if (id=='p7'):
            self.expanderi.iskljuci(57)
        if (id=='p8'):
            self.expanderi.iskljuci(56)
        if (id=='p9'):
            self.expanderi.iskljuci(55)
        if (id=='p10'):
            self.expanderi.iskljuci(54)
        if (id=='p11'):
            self.expanderi.iskljuci(53)
        if (id=='p12'):
            self.expanderi.iskljuci(52)
        if (id=='p13'):
            self.expanderi.iskljuci(51)
        if (id=='p14'):
            self.expanderi.iskljuci(50)
        if (id=='p15'):
            self.expanderi.iskljuci(49)
        if (id=='p16'):
            self.expanderi.iskljuci(48)
        if (id=='p17'):
            self.expanderi.iskljuci(47)
        if (id=='p18'):
            self.expanderi.iskljuci(46)
        if (id=='p19'):
            self.expanderi.iskljuci(45)
        if (id=='p20'):
            self.expanderi.iskljuci(44)
        if (id=='p21'):
            self.expanderi.iskljuci(43)
        if (id=='p22'):
            self.expanderi.iskljuci(42)
        if (id=='p23'):
            self.expanderi.iskljuci(41)
        if (id=='p24'):
            self.expanderi.iskljuci(40)
        if (id=='p25'):
            self.expanderi.iskljuci(39)
        if (id=='p26'):
            self.expanderi.iskljuci(38)
        if (id=='p27'):
            self.expanderi.iskljuci(37)
        if (id=='p28'):
            self.expanderi.iskljuci(36)
        if (id=='p29'):
            self.expanderi.iskljuci(35)
        if (id=='p30'):
            self.expanderi.iskljuci(34)
        if (id=='p31'):
            self.expanderi.iskljuci(33)
        if (id=='p32'):
            self.expanderi.iskljuci(32)              
