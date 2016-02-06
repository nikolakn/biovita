'''
Created on Jan 15, 2016

@author: nikola
'''
#import mysql.connector
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
import sys
from ui import UiAuto
from sys import platform as _platform
import serial 
import time
from rucne import rucneKomande
from database import dbhelpers,data,zadatak
import dialogRec
class autoProzor(QMainWindow,UiAuto.Ui_MainWindow):
    
    def __init__(self,state, parent=None):
        super(autoProzor,self).__init__()
        self.setupUi(self)
        if _platform == "linux" or _platform == "linux2":
            try:
                self.port = serial.Serial("/dev/ttyAMA0" ,9600 , parity=serial.PARITY_NONE , stopbits =serial.STOPBITS_ONE , bytesize=serial.EIGHTBITS,timeout=0)
                self.port.open()
            except:
                print("Greska seriski port ")
                sys.exit(0)   
        self.state = state
        self.isStart = False
        self.vaganje = False
        self.simvag = 0
        self.zadataMera = 0
        self.prethodnaMera = 0
        self.initUI()
        
    def initUI(self):
        self.setWindowIcon(QIcon('images/gear_blue.ico'))
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle('BIOVITA')
        self.show()
        meniUnos = self.menubar.addAction("Unos i promena podataka")
        meniUtovar = self.menubar.addAction("UTOVAR")
        meniPretovar = self.menubar.addAction("PRETOVAR")
        meniRucne = self.menubar.addAction("RUCNE KOMANDE")
        meniProzori = self.menubar.addAction("PROZORI")
        meniRucne.triggered.connect(self.rucneWindow)
        meniUnos.triggered.connect(self.unosWindow)
        meniUtovar.triggered.connect(self.utovarWindow)
        
        self.dugme_brisizadatak.clicked.connect(lambda:self.brisiZadatak())
        self.dugme_novizadatak.clicked.connect(lambda:self.noviZadatak())
        
        self.startdugme.clicked.connect(lambda:self.startZadatak())
        self.stopdugme.clicked.connect(lambda:self.stopZadatak())
        self.dugme_krajodvage.clicked.connect(lambda:self.krajOdvage())
        self.pushButton.clicked.connect(lambda:self.ocistiTabelu())
        #baza
        self.baza = dbhelpers.db()
        self.baza.open()
        #timer
        self.ctimer = QTimer()
        QObject.connect(self.ctimer, SIGNAL("timeout()"), self.timerUpdate)
        self.ctimer.start(100)
        
        self.vaga2timer = QTimer()
        QObject.connect(self.vaga2timer, SIGNAL("timeout()"), self.vaga2timerUpdate)
        self.vaga2timer.start(1000)
        self._tvaga2 = 0
        self._isvaga2 = False
        self._tmlin = 0
        self._istmlin = False
        self._tmesaona = 0
        self._istmesaona = False
        self.ex = None
        
        self.ucitajizBaze()
        
    def vaga2timerUpdate(self): 
        if(self._isvaga2==True):
            self._tvaga2 = self._tvaga2 + 1
            self.widget_3.add(self.mera,self._tvaga2)
            self.vaga2edit.setText(str(self._tvaga2))
            
        if(self._istmlin==True):
            self._tmlin = self._tmlin + 1
            self.vaga2edit.setText(str(self._tmlin))
            
        if(self._istmesaona==True):      
            self._istmesaona = self._istmesaona + 1
            self.vaga2edit.setText(str(self._istmesaona))
            
    def startZadatak(self):
        if(len(self.dataZadaci)==0):
            return
            
        if(len(self.dataTrenutniZadatak)==0):
            self._odvagaBroj = 0;
            self.pocetakOdvage();            
        else:
            self.pocetakKomponente();    
        
        
    def pocetakOdvage(self):
        self.zadataMera = 0
        self.prethodnaMera = 0
        self.baza.izbrisiTrenutneZadatke();
        tzadatak = self.dataZadaci[0]
        self.status("Startovanje odvage")
        self._isvaga2 = True
        ime = tzadatak.ime
        receptura = None
        for rec in self.dataRecepture:
            if (rec.ime == ime):
                receptura = rec
        if(receptura == None):
            self.status("Receptura ne postoji!")
            return;
        else:
            self.status("start recepture: "+ime)
        #citaj komponente i odredi binove
        self._trenutnaOdvaga = self.dataZadaci[0].odradjeno
        
        self.dataTrenutniZadatak = []
        for komp in receptura.komponente:
            komponenta = komp.ime
            procenat = komp.procenat;
            if(komponenta!='' and procenat!=0 and komponenta!=None):
                k = zadatak.NkTrenutniZadatak()
                k.komponenta = komponenta
                k.bin = 0
                k.zadato = 0
                k.izmereno = 0
                k.procenat =  procenat
                self.dataTrenutniZadatak.append(k)  
                
        self._ukupnaKolicina = self.dataZadaci[0].kolicina
        if(self._ukupnaKolicina > 600):
            self._ukupnaKolicina = 600
            
        self.odredjivanjeBinova(); 

        for z in self.dataTrenutniZadatak:
            self.baza.insertTrnutniZadatak(z);
        
        self.dataTrenutniZadatak = self.baza.trenutniZadatakList()
        self.ucitajTrenutniZadatak();
        #print tzadatak
        #kolicina za merenje

        
        self.imerecepture.setText(self.dataZadaci[0].ime)
        self.brojodvagauz.setText(str(int(self.dataZadaci[0].odvaga)))
        self.lineEdit_5.setText(str(int(self._trenutnaOdvaga+1)))
        self.lineEdit_6.setText(str(self._ukupnaKolicina))
        self.isStart = True
        #self.repaint()        
        self.pocetakKomponente()
            
    def pocetakKomponente(self):
        self.status("Pocetak komponente")
        id = 0
        zadatakZavrsen = True;
        self._isvaga2=True
        for komp in self.dataTrenutniZadatak:
            if (komp.izmereno==0):
                self._trenutnaKomponenta = komp
                zadatakZavrsen = False;
                self._trenutnaOdvaga = self.dataZadaci[0].odradjeno
                self._ukupnaKolicina = self.dataZadaci[0].kolicina
                ostalo = self._ukupnaKolicina-(self._trenutnaOdvaga*600)
                if( ostalo > 600):
                    ostalo = 600
                self.lineEdit_3.setText(str(komp.bin));
                self.lineEdit_4.setText(str(komp.zadato));
                
                self.imerecepture.setText(self.dataZadaci[0].ime)
                self.brojodvagauz.setText(str(int(self.dataZadaci[0].odvaga)))
                self.lineEdit_5.setText(str(int(self._trenutnaOdvaga+1)))
                self.lineEdit_6.setText(str(ostalo))
        
                self.tableWidget.selectRow(id);    
                self._id = komp.id;
                self.zadataMera = self.prethodnaMera  + komp.zadato
                
                self.vaganje = True
                self.ukljuciBin(komp.bin)

                break
            id = id + 1
         #dali je ostalo komponenata za vaganje
        if(zadatakZavrsen == True ):
           self.vaganje = False
           self.zavrsenZadatak()
            
    
    def zavrsenZadatak(self):
        self.status("zadatak zavrsen!")
        self._isvaga2=False
        
    #mera dostignuta    
    def vaganjeZavrseno(self, mera):
        self.status("vaganje zavrseno")
        self.vaganje = False
        self._trenutnaKomponenta.izmereno = mera-self.prethodnaMera
        self.baza.updateIzmereno(self._id, mera-self.prethodnaMera)
        self.prethodnaMera = mera
         #refesh tabelu
        self.ucitajTrenutniZadatak()       
        self.pocetakKomponente();
        
    def krajOdvage(self): 
        if(self.isStart):
            self.vaganjeZavrseno(0.1)
     
    def ocistiTabelu(self):
        self.isStart = False
        self.baza.izbrisiTrenutneZadatke();
        self.dataTrenutniZadatak = []
        self.ucitajTrenutniZadatak()
        
    def odredjivanjeBinova(self):
        for z in self.dataTrenutniZadatak:
            komp = z.komponenta
            for b in range(0,12):
                bin = self.dataBinovi.getBin(b)
                if(bin.artikl == komp):
                    z.bin = b+1
                    koef = bin.koeficijent
                    z.zadato = self._ukupnaKolicina * (z.procenat/100.0) - koef
                    break;
                    
        
    def stopZadatak(self):   
        self.isStart = False
    #ucitaj podatke iz baze
    def ucitajizBaze(self):    
        self.dataRecepture = self.baza.receptureList()
        self.dataZadaci = self.baza.zadaciList()
        self.dataBinovi = self.baza.getBinovi() 
        self.dataTrenutniZadatak = self.baza.trenutniZadatakList()

        self.ucitajBinove()
        self.ucitajZadatake()
        self.ucitajTrenutniZadatak() 
        
    def ucitajBinove(self):
        self.binlab = [self.label_bin1,self.label_bin2,self.label_bin3,
                       self.label_bin4,self.label_bin5,self.label_bin6,
                       self.label_bin7,self.label_bin8,self.label_bin9,
                       self.label_bin10,self.label_bin11,self.label_bin12]
        
        index = 0;
        for bin in self.binlab:
            if(self.dataBinovi.getBin(index).artikl != None):
                bin.setText(self.dataBinovi.getBin(index).artikl)
            else:
                bin.setText('')
            index = index + 1   
            
    def ucitajZadatake(self):
        n = 0
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SingleSelection);
        self.tableWidget_2.setRowCount(len(self.dataZadaci))
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setHorizontalHeaderLabels(['Ime', 'Kolicina', 'Odvaga', 'Poslednja odvaga', 'Odradjeno'])
        for zad in self.dataZadaci:  
            newitem2 = QTableWidgetItem(zad.ime)
            self.tableWidget_2.setItem(n, 0, newitem2)
            
            newitem3 = QTableWidgetItem(str(zad.kolicina))
            self.tableWidget_2.setItem(n, 1, newitem3)
            
            newitem4 = QTableWidgetItem(str(zad.odvaga))
            self.tableWidget_2.setItem(n, 2, newitem4)
            
            newitem5 = QTableWidgetItem(str(zad.poslednja))
            self.tableWidget_2.setItem(n, 3, newitem5)
            
            newitem6 = QTableWidgetItem(str(zad.odradjeno))
            self.tableWidget_2.setItem(n, 4, newitem6)
            n += 1
    def brisiZadatak(self):
        x = self.tableWidget_2.selectedIndexes ()
        if(len(x)==0):
            return
        x = self.tableWidget_2.selectionModel().selectedRows()[0].row();
        id = self.dataZadaci[x].id
        del self.dataZadaci[x]
        #obrisati iz baze   
        self.baza.obrisiZadatak(id)
        self.dataZadaci = self.baza.zadaciList()
        self.ucitajZadatake()

            
    def noviZadatak(self):
        unos = dialogRec.dialogzaRecept(self,self.dataRecepture)
        if( unos.exec_() == QDialog.Accepted):
            zz = zadatak.NkZadatak()
            zz.ime = unos.getIme()
            zz.kolicina = unos.getKolicina()
            if(zz.kolicina%600 == 0):
                zz.odvaga = int(zz.kolicina/600)
            else:    
                zz.odvaga = int(zz.kolicina/600)+1
            self.dataZadaci.append(zz) 
                
            self.baza.insertZadatak(zz)  
            self.dataZadaci = self.baza.zadaciList()            
            self.ucitajZadatake()
        
    def ucitajTrenutniZadatak(self):
        n = 0
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection);
        self.tableWidget.setRowCount(len(self.dataTrenutniZadatak))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Komponenta', 'Bin', 'Zadato', 'Izmereno'])
        for zad in self.dataTrenutniZadatak:  
            newitem2 = QTableWidgetItem(zad.komponenta)
            newitem2.setFlags(newitem2.flags() ^ Qt.ItemIsEditable);
            self.tableWidget.setItem(n, 0, newitem2)
            
            newitem3 = QTableWidgetItem(str(zad.bin))
            newitem3.setFlags(newitem3.flags() ^ Qt.ItemIsEditable);
            self.tableWidget.setItem(n, 1, newitem3)
            
            newitem4 = QTableWidgetItem(str(zad.zadato))
            newitem4.setFlags(newitem4.flags() ^ Qt.ItemIsEditable);
            self.tableWidget.setItem(n, 2, newitem4)
            
            newitem5 = QTableWidgetItem(str(zad.izmereno))
            newitem5.setFlags(newitem5.flags() ^ Qt.ItemIsEditable);           
            self.tableWidget.setItem(n, 3, newitem5)
            
            n += 1
        self.tableWidget.resizeColumnsToContents()    
    def unosWindow(self):
        print("unos");
    def utovarWindow(self):
        print("utovar");        
    def rucneWindow(self):
        if isinstance(self.ex, rucneKomande.rucneProzor):
            self.ex.close()
            self.ex = rucneKomande.rucneProzor(self.state)
        else:
            self.ex = rucneKomande.rucneProzor(self.state)
    def timerUpdate(self):
        ulazi = self.state.updateSensors();
        mera =''
        if _platform == "linux" or _platform == "linux2":
            ch = self.port.readline();
            mera = self.vagaMera(ch);
        else:
            self.simvag = self.simvag +1
            if (self.simvag>600):
                self.simvag = 0
            m = "%08d" % (self.simvag,)
            ch = chr(2)+m+"G"
            mera = self.vagaMera(ch);
        if(mera!=''):
            self.vagamera_2.setText(str(mera))
        self.labelvreme.setText('Vreme: '+time.strftime("%H:%M:%S"))
        self.labeldatum.setText('Datum: '+time.strftime("%d/%m/%Y"))
        if(self.dobramera == True):
            if(self.vaganje == True and float(mera) >= float(self.zadataMera)):
                self.vaganje = False
                self.vaganjeZavrseno(mera);
        self.repaint()    

    def vagaMera(self,st):
        s= st.find(chr(2))
        Q= st.find(chr(71));
        e= st.find(chr(77));
        if(s==-1):
            self.dobramera = False;
            return ''
        mera = st[s+1:s+9]
        palette = self.vagamera_2.palette()
        palette.setColor(QPalette.Active, QPalette.Text, QColor(255, 255, 255))
        try: 
            self.mera = float(mera);
        except :
            #self.mera = 0         
            #palette.setColor(QPalette.Active, QPalette.Base, QColor(255, 0, 0))
            #self.vagamera_2.setPalette(palette)
            self.dobramera = False;
            return ''
        if(e==-1 and Q!=-1):
            self.dobramera = True;
            palette.setColor(QPalette.Active, QPalette.Base, QColor(0, 255, 0))
            self.vagamera_2.setPalette(palette)
            return self.mera
        else:
            self.dobramera = False;
            palette.setColor(QPalette.Active, QPalette.Base, QColor(255, 0, 0))
            self.vagamera_2.setPalette(palette)
            return self.mera

    def status(self,msg):
        self.statustext.setText(msg)

    def ukljuciBin(self,bin):
        if(bin == 1):
            self.scrollAreaWidgetContents.bin1.on()
        if(bin == 2):
            self.scrollAreaWidgetContents.bin2.on()
        if(bin == 3):
            self.scrollAreaWidgetContents.bin3.on()
        if(bin == 4):
            self.scrollAreaWidgetContents.bin4.on()
        if(bin == 5):
            self.scrollAreaWidgetContents.bin5.on()
        if(bin == 6):
            self.scrollAreaWidgetContents.bin6.on()
        if(bin == 7):
            self.scrollAreaWidgetContents.bin7.on()
        if(bin == 8):
            self.scrollAreaWidgetContents.bin8.on()
        if(bin == 9):
            self.scrollAreaWidgetContents.bin9.on()
        if(bin == 10):
            self.scrollAreaWidgetContents.bin10.on()
        if(bin == 11):
            self.scrollAreaWidgetContents.bin11.on()
        if(bin == 12):
            self.scrollAreaWidgetContents.bin12.on()            