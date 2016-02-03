# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import zadatak

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
            data.append(row[0],row[1],row[2],row[3],row[4],row[5])
            list.append(data)
            row = self.cur.fetchone()   
        return list
    
    def login(self,ime,password):
        self.cur.execute("SELECT * FROM osoblje WHERE UNAME='"+ime+"'")
        rows = self.cur.fetchall()
        if (self.cur.rowcount != 1):
            return -1
        sifra = rows[0][6]
        pristup = rows[0][2]
        if(sifra != password):
            return -1
        return pristup


    def addNewOsoblje(self,ime,potpis,tip,password):
        try:
            query = "INSERT INTO osoblje(TIP,UNAME,PSW,POTPIS) VALUES(%s,%s,%s,%s)"
            args = (tip, ime, password, potpis)
            self.cur.execute(query, args)
            #self.cursor.executemany(query, books)
            self.cnx.commit()
            return True
        except Error as error:
            print(error)
            return False

    def delOsoblje(self,ime):
        try:
            query = "DELETE FROM osoblje WHERE UNAME = %s"
            self.cursor.execute(query, (ime,))
            self.cnx.commit()
            return True
        except Error as error:
            print(error)
            return False

