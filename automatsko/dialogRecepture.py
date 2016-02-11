'''
Created on Jan 15, 2016

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import sys
from ui import UiDialogRecepture
from database import zadatak

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
        
        self.komponente = [self.comboKomp1,self.comboKomp2,self.comboKomp3,self.comboKomp4,
            self.comboKomp5,self.comboKomp6,self.comboKomp7,self.comboKomp8,
            self.comboKomp9,self.comboKomp10,self.comboKomp11,self.comboKomp12]
            
        self.procenti = [self.lineEdit_2,self.lineEdit_3,self.lineEdit_4,
            self.lineEdit_5,self.lineEdit_6,self.lineEdit_7,self.lineEdit_8,
            self.lineEdit_9,self.lineEdit_10,self.lineEdit_11,
            self.lineEdit_12,self.lineEdit_13]   
        self.ucitaj()  
        self.tableWidget.clicked.connect(self.viewClicked)
        self.clickId = 0
        
    def viewClicked(self):
        x = self.tableWidget.selectionModel().selectedRows()[0].row();
        rec = self.recepti[len(self.recepti)-x-1]
        self.lineEditIme.setText(rec.ime)
        self.clickId  = rec.id
        for x in range(0,12):
            self.komponente[x].setEditText(str(rec.komponente[x].ime))
            self.procenti[x].setText(str(rec.komponente[x].procenat))      

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
        list1 = ["KUKURUZ","SOJIN GRIZ","SOJIONA POGACA","SUNC SACMA 33%","SOJA",
            "PREMIX","SUNCOKRET ZRNO","PSENICA","EXT KUK"]
        for x in range(0,12):
            self.komponente[x].clear()
            self.komponente[x].addItems(list1)
            self.komponente[x].setCurrentIndex(-1);
    def novaReceptura(self):
        self.lineEditIme.setText('')
        for c in self.komponente:
            c.setCurrentIndex(-1);
        for p in self.procenti:
            p.setText('')
        self.clickId = 0
            
    def upisiRecepturu(self):
        if(self.clickId == 0):
            unos = zadatak.NkReceptura(0,str(self.lineEditIme.text()))
            for x in range(0,12):
                unos.komponente[x].ime = str(self.komponente[x].currentText())
                try:
                    if(self.procenti[x].text()!=None and self.procenti[x].text()!=''):
                        unos.komponente[x].procenat = float(self.procenti[x].text())
                except:
                    QMessageBox.about(self, "Greska", "Unesite ispravan broj")
                    return
            self.baza.insertRecepturu(unos)
            self.recepti = self.baza.receptureList()
            self.ucitaj()
        else:
            unos = zadatak.NkReceptura(self.clickId,str(self.lineEditIme.text()))
            for x in range(0,12):
                unos.komponente[x].ime = str(self.komponente[x].currentText())
                try:
                    if(self.procenti[x].text()!=None and self.procenti[x].text()!=''):
                        unos.komponente[x].procenat = float(self.procenti[x].text())
                except:
                    QMessageBox.about(self, "Greska", "Unesite ispravan broj")
                    return  
            self.baza.updateRecepturu(unos)
            self.recepti = self.baza.receptureList()
            self.ucitaj() 
        self.novaReceptura()
        
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