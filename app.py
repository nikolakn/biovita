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
        
    def ukljuciMotor(self,id):
        id = 'm'+str(id)
        self.motori[id] = 1
        self.expanderi.ukljuci(id-1) 
        