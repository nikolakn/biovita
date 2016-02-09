'''
Created on Jan 15, 2016

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import sys
from ui import UiDialogGotove

class dialogGotoveOdvage(QDialog,UiDialogGotove.Ui_Dialog):
    
    def __init__(self,baza):
        super(dialogGotoveOdvage,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Gotove odvage")
        self.baza = baza;    
        self.gotoviZadaci = self.baza.gotoveOdvageList()
        self.ucitaj()
        
    def ucitaj(self):
        n = 0
        
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection);
        self.tableWidget.setRowCount(len(self.gotoviZadaci))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['Ime', 'Zadata Kolicina', 'Odvaga', 'vreme', 'datum'])
        for zad in reversed(self.gotoviZadaci):  
            newitem2 = QTableWidgetItem(zad.ime)
            self.tableWidget.setItem(n, 0, newitem2)
            
            newitem3 = QTableWidgetItem(str(zad.zadataKolicina))
            self.tableWidget.setItem(n, 1, newitem3)
            
            newitem4 = QTableWidgetItem(str(zad.tezinaOdvage))
            self.tableWidget.setItem(n, 2, newitem4)
            
            newitem5 = QTableWidgetItem(str(zad.vreme))
            self.tableWidget.setItem(n, 3, newitem5)
            
            newitem6 = QTableWidgetItem(str(zad.datum))
            self.tableWidget.setItem(n, 4, newitem6)
            n += 1
        self.tableWidget.resizeColumnsToContents()  