# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import zadatak
import data
import time

class db(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        
    def open(self):
        try:   
            self.con = lite.connect('biovita.db')

            self.cur = self.con.cursor()    

        except:
            print('greska ne mogu da otvorim bazu ', sys.exc_info())
            return False

        return True
        
    def close(self):
        self.cur.close()
        self.con.close()       
        
    def zadaciList(self):
        list = []
        self.cur.execute("SELECT * FROM zadaci")
        row = self.cur.fetchone()
        while row is not None:
            data = zadatak.NkZadatak()
            data.set(row[0],row[1],row[2],row[3],row[4],row[5])
            list.append(data)
            row = self.cur.fetchone()   
        return list
        
    def getBinovi(self):
        rez = data.NkBinovi()
        self.cur.execute("SELECT * FROM binovi")
        row = self.cur.fetchone()
        i = 0
        while row is not None:
            rez.setBin(i,row[1],row[2],row[3],row[4])
            row = self.cur.fetchone() 
            i = i + 1
        return rez  

    def receptureList(self):
        list = []
        self.cur.execute("SELECT * FROM recepture")
        row = self.cur.fetchone()
        while row is not None:
            data = zadatak.NkReceptura(row[0],row[1])
            for b in range(0,12):
                data.addKomponente(b,row[2*b+2],row[2*b+3])
            list.append(data)
            row = self.cur.fetchone()   
        return list
        
    def gotoveOdvageList(self):
        list = []
        self.cur.execute("SELECT * FROM gotoveOdvage")
        row = self.cur.fetchone()
        while row is not None:
            data = zadatak.NkGotoveOdvage()
            data.id=row[0]
            data.ime=row[1]
            data.zadataKolicina=row[2]
            data.tezinaOdvage=row[3]
            data.vreme=row[4]
            data.datum=row[5]
            list.append(data)
            row = self.cur.fetchone()   
        return list
        
    def trenutniZadatakList(self):
        list = []
        self.cur.execute("SELECT * FROM trenutniZadatak")
        row = self.cur.fetchone()
        while row is not None:
            data = zadatak.NkTrenutniZadatak()
            data.set(row[0],row[1],row[2],row[3],row[4])
            list.append(data)
            row = self.cur.fetchone()   
        return list 

    def obrisiZadatak(self,id):
        try:
            query = "DELETE FROM zadaci WHERE id ="+str(id)+""
            self.cur.execute(query)
            self.con.commit() 
            return True
        except:
            print('greska , ne mogu da obrisem zadatak ',sys.exc_info())
            return False        
    def insertZadatak(self,zadatak):
        try:
            query = "INSERT INTO zadaci(ime,kolicina,odvaga,poslednja,odradjeno) VALUES(?,?,?,?,?)"
            args = (zadatak.ime,zadatak.kolicina,zadatak.odvaga,zadatak.poslednja,zadatak.odradjeno)
            self.cur.execute(query, args)
            #self.cursor.executemany(query, books)
            self.con.commit()
            return True
        except:
            print('greska nije uspelo upisivanje u bazu',sys.exc_info())
            return False  


    def insertTrnutniZadatak(self,zadatak):
        try:
            query = "INSERT INTO trenutniZadatak (komponenta,bin,zadato,izmereno) VALUES(?,?,?,?)"
            args = (zadatak.komponenta,zadatak.bin,zadatak.zadato,zadatak.izmereno)
            self.cur.execute(query, args)
            #self.cursor.executemany(query, books)
            self.con.commit()
            return True
        except:
            print('greska nije uspelo upisivanje u bazu',sys.exc_info())
            return False 

    def izbrisiTrenutneZadatke(self):
        try:
            query = "DELETE FROM trenutniZadatak"
            self.cur.execute(query)
            self.con.commit() 
            return True
        except:
            print('greska , ne mogu da obrisem zadatak ',sys.exc_info())
            return False   

    def updateIzmereno(self, id, izmereno):
        try:  
            query ="UPDATE trenutniZadatak set izmereno = "+str(izmereno)+" where id="+str(id)
            self.cur.execute(query)
            self.con.commit()
            return True
        except:
            print('greska , ne mogu da updatujem meru ',sys.exc_info())
            return False 
            
    def upisiOdvagu(self,ime,zad,m):
        try:
            query = "INSERT INTO gotoveOdvage (imeRecepta,zadataKolicina,tezinaOdvage,vreme,datum) VALUES(?,?,?,?,?)"
            args = (ime,zad,m,time.strftime("%H:%M:%S"),time.strftime("%d/%m/%Y"))
            self.cur.execute(query, args)
            self.con.commit()
            return True
        except:
            print('greska nije uspelo upisivanje u bazu',sys.exc_info())
            return False   

    def povecajOdradjeno(self,id,odradjeno):
         try:  
            query ="UPDATE zadaci set odradjeno = "+str(odradjeno)+" where id="+str(id)
            self.cur.execute(query)
            self.con.commit()
            return True
         except:
            print('greska , ne mogu da updatujem meru ',sys.exc_info())
            return False   
    def updatePoslednja(self,id,poslednja):
         try:  
            query ="UPDATE zadaci set poslednja = "+str(poslednja)+" where id="+str(id)
            self.cur.execute(query)
            self.con.commit()
            return True
         except:
            print('greska , ne mogu da updatujem meru ',sys.exc_info())
            return False   
    def updateBin(self,id,artikl,koef):
         try:  
            query ="UPDATE binovi set artikl = '"+str(artikl)+"', koeficijent="+str(koef)+" where id="+str(id)
            self.cur.execute(query)
            self.con.commit()
            return True
         except:
            print('greska , ne mogu da updatujem bin ',sys.exc_info())
            return False        