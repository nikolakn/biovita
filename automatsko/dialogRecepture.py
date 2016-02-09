'''
Created on Jan 15, 2016

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import sys
from ui import UiDialogRecepture

class dialogRecept(QDialog,UiDialogRecepture.Ui_Dialog):
    
    def __init__(self, baza):
        super(dialogRecept,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Recepture")
        self.baza = baza;
        self.recepti = self.baza.receptureList()

        self.pushButton_3.clicked.connect(lambda:self.novaReceptura()) 
        self.pushButton_2.clicked.connect(lambda:self.upisiRecepturu()) 
        self.pushButton.clicked.connect(lambda:self.obrisiRecepturu()) 
        self.ucitaj()
        self.komponente = [self.comboKomp1,self.comboKomp2,self.comboKomp3,self.comboKomp4,
            self.comboKomp5,self.comboKomp6,self.comboKomp7,self.comboKomp8,
            self.comboKomp9,self.comboKomp10,self.comboKomp11,self.comboKomp12]
            
        self.procenti = [self.lineEdit_2,self.lineEdit_3,self.lineEdit_4,
            self.lineEdit_5,self.lineEdit_6,self.lineEdit_7,self.lineEdit_8,
            self.lineEdit_9,self.lineEdit_10,self.lineEdit_11,
            self.lineEdit_12,self.lineEdit_13]    
    def ucitaj(self):
        n = 0
        
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection);
        self.tableWidget.setRowCount(len(self.recepti))
        self.tableWidget.setColumnCount(25)
        self.tableWidget.setHorizontalHeaderLabels(['Ime', 'Komp1', 'Proc1', 'Komp2', 'Proc2',
            'Komp3', 'Proc3', 'Komp4', 'Proc4','Komp5', 'Proc5', 'Komp6', 'Proc6',
            'Komp7', 'Proc7', 'Komp8', 'Proc8','Komp9', 'Proc9', 'Komp10', 'Proc10',
            'Komp11', 'Proc11', 'Komp12', 'Pro12'])
        for zad in reversed(self.recepti):  
            newitem2 = QTableWidgetItem(zad.ime)
            self.tableWidget.setItem(n, 0, newitem2)
            kolona = 1
            for indkomp in range(0,12):
         
                newitem6 = QTableWidgetItem(str(zad.komponente[indkomp].ime))
                self.tableWidget.setItem(n, kolona, newitem6)
                kolona = kolona + 1
                newitem7 = QTableWidgetItem(str(zad.komponente[indkomp].procenat))
                self.tableWidget.setItem(n, kolona, newitem7)
                kolona = kolona + 1
            n += 1
        self.tableWidget.resizeColumnsToContents()        


    def novaReceptura(self):
        self.lineEditIme.setText('')
        for c in self.komponente:
            c.setCurrentIndex(-1);
        for p in self.procenti:
            p.setText('')
    def upisiRecepturu(self):
        pass
    def obrisiRecepturu(self):   
        x = self.tableWidget.selectedIndexes ()
        if(len(x)==0):
            return
        x = self.tableWidget.selectionModel().selectedRows()[0].row();
        id = self.recepti[len(self.recepti)-x-1].id
        del self.recepti[len(self.recepti)-x-1]
        
        #obrisati iz baze   
        self.baza.obrisiRecepturu(id)
        self.recepti = self.baza.receptureList()
        self.ucitaj()