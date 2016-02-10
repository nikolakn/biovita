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
import dialogBin
import dialogGotove
import dialogRecepture

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
        self.mera = 0
        self.simvag = 0
        self.zadataMera = 0
        self.prethodnaMera = 0
        self.scrollAreaWidgetContents.bin1.binklik.connect(self.on_bin_clicked)
        self.scrollAreaWidgetContents.bin2.binklik.connect(self.on_bin_clicked)
        self.scrollAreaWidgetContents.bin3.binklik.connect(self.on_bin_clicked)
        self.scrollAreaWidgetContents.bin4.binklik.connect(self.on_bin_clicked)
        self.scrollAreaWidgetContents.bin5.binklik.connect(self.on_bin_clicked)
        self.scrollAreaWidgetContents.bin6.binklik.connect(self.on_bin_clicked)
        self.scrollAreaWidgetContents.bin7.binklik.connect(self.on_bin_clicked)
        self.scrollAreaWidgetContents.bin8.binklik.connect(self.on_bin_clicked)
        self.scrollAreaWidgetContents.bin9.binklik.connect(self.on_bin_clicked)
        self.scrollAreaWidgetContents.bin10.binklik.connect(self.on_bin_clicked)
        self.scrollAreaWidgetContents.bin11.binklik.connect(self.on_bin_clicked)
        self.scrollAreaWidgetContents.bin12.binklik.connect(self.on_bin_clicked)
        
        self.radioButton_8.clicked.connect(lambda:self.btn_ispusti_1()) 
        self.radioButton_9.clicked.connect(lambda:self.btn_ispusti_2()) 
        self.radioButton_10.clicked.connect(lambda:self.btn_ispusti_3()) 
        self.radioButton_11.clicked.connect(lambda:self.btn_ispusti_4()) 
        self.radioButton_12.clicked.connect(lambda:self.btn_ispusti_5()) 
        self.radioButton_13.clicked.connect(lambda:self.btn_ispusti_6()) 
        self.radioButton_14.clicked.connect(lambda:self.btn_ispusti_7()) 
        
        
        self.initUI()
        
    def initUI(self):
        self.setWindowIcon(QIcon('images/gear_blue.ico'))
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle('BIOVITA')
        self.show()
        meniUnos = self.menubar.addAction("Recepture")
        meniUtovar = self.menubar.addAction("Gotove Odvage")
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
        self.dugmestopele.clicked.connect(lambda:self.stopelevator())
        self.checkBox_4.stateChanged.connect(self.ukljuciDotokMaterijala)
        self.checkBox_5.stateChanged.connect(self.ukljuciMlin)
        self.checkBox_6.stateChanged.connect(self.ukljuciElevatorMlina)
        
        self.pushButtonNapuni.clicked.connect(lambda:self.napuniMesaonuBut())
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
        #tajmeri    
        self._tvaga2 = 0
        self._isvaga2 = False
        self._tmlin = 0
        self._istmlin = False
        self._tmesaona = 0
        self._istmesaona = False
        self.ex = None
        
        self.ucitajizBaze()
        
    def napuniMesaonuBut(self):
        if(self._istmesaona == False):
            
            self._tmesaona = 0
            self._istmesaona = True            
            self.napuniMesaonu()
            
    def stopelevator(self):
        self.state.iskljuciElevator3();
        self.scrollAreaWidgetContents.elevator2 = False
        
    def ukljuciDotokMaterijala(self):
        if(self.checkBox_4.isChecked()==True):
            self.state.krenidotokMat() 
            self._tmlin = 0
            self._istmlin = True
            self.scrollAreaWidgetContents.MlinDotok()
        else:
            self.state.iskljucidotokMat()
            self._istmlin = False
            if(self.checkBox_5.isChecked()==False):
                self.scrollAreaWidgetContents.MlinDotokStop()
            else:
                self.scrollAreaWidgetContents.MlinPuni()  
            
    def ukljuciMlin(self):
        if(self.checkBox_5.isChecked()==True):
            self.state.kreniMlin()
            self.scrollAreaWidgetContents.MlinPuni()            
        else:
            self.state.iskljuciMlin()
            if(self.checkBox_4.isChecked()==False):
                self.scrollAreaWidgetContents.MlinDotokStop()
            else:
                self.scrollAreaWidgetContents.MlinDotok()
                
    def ukljuciElevatorMlina(self):
        if(self.checkBox_6.isChecked()==True):
            self.state.kreniElevatorMlina()
            self.scrollAreaWidgetContents.elevator1 = True          
        else:
            self.state.iskljuciElevatorMlina()
            self.scrollAreaWidgetContents.elevator1 = False 
    def vaga2timerUpdate(self): 
        if(self._isvaga2==True):
            self._tvaga2 = self._tvaga2 + 1
            self.widget_3.add(self.mera)
            self.vaga2edit.setText(str(self._tvaga2))
            
        if(self._istmlin==True):
            self._tmlin = self._tmlin + 1
            self.lineEdit_13.setText(str(self._tmlin))
            
        if(self._istmesaona==True):      
            self._tmesaona = self._tmesaona + 1
            self.napuniMesaonu()
     
    #start dugme    
    def startZadatak(self):
        if(len(self.dataZadaci)==0):
            return
            
        if(len(self.dataTrenutniZadatak)==0):
            self._odvagaBroj = 0;
            self.pocetakOdvage();            
        else:
            self.pocetakKomponente();    
        
    #ulazi samo na pocetku zadatka kada je lista
    #sa trenutnim zadatkom prazna
    def pocetakOdvage(self):
        
        if(len(self.dataZadaci)==0):
                return
        self.zadataMera = 0
        self.prethodnaMera = 0
        self.scrollAreaWidgetContents.vagaOn()
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
                
        self._trenutnaKomponenta = self.dataTrenutniZadatak[0]
        kol = self.dataZadaci[0].kolicina
        ostalo = kol-(self.dataZadaci[0].odradjeno*600)                
        self._ukupnaKolicina = ostalo
        if(self._ukupnaKolicina > 600):
            self._ukupnaKolicina = 600
            
        rez = self.odredjivanjeBinova(); 
        if(rez == False):
            self.dataTrenutniZadatak = []
            self._isvaga2 = False
            return;
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
    
    #za svaku komponentu posebno i ako lista trenutnih odvaga
    #nija prazna pri startovanju
    def pocetakKomponente(self):
        self.port.flushInput()
        self.scrollAreaWidgetContents.vagaOn()
 
        self.status("Pocetak komponente")
        id = 0
        zadatakZavrsen = True;
        self._isvaga2=True
        for komp in self.dataTrenutniZadatak:
            if (komp.izmereno==0.0):
                self._trenutnaKomponenta = komp
                zadatakZavrsen = False;
                self._trenutnaOdvaga = self.dataZadaci[0].odradjeno
                kol = self.dataZadaci[0].kolicina
                ostalo = kol-(self._trenutnaOdvaga*600)
                self._ukupnaKolicina = ostalo
                if( ostalo > 600):
                    ostalo = 600
                    self._ukupnaKolicina = 600
                #self.odredjivanjeBinova(); 
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
            
    # zavrsen zadatak
    # pripremi za novu odvagu
    def zavrsenZadatak(self):
        self.status("zadatak zavrsen!")
        self._isvaga2=False
        
        self.baza.upisiOdvagu(self.dataZadaci[0].ime,self._ukupnaKolicina,
            self.prethodnaMera )
        self.dataZadaci[0].ime
        odradjeno = self.dataZadaci[0].odradjeno+1
        zadato = self.dataZadaci[0].odvaga
        QMessageBox.about(self, "Informacija", "Vaga zavrsila i puna! SACEKATI DA MLIN ZAVRSI!")
        #otvori vagu
        self.checkBox_4.setChecked(True);
        self.checkBox_6.setChecked(True);
        self.state.otvoriVagu()
        #mesaona start
        self.napuniMesaonu()
        self._tmesaona = 0
        self._istmesaona = True 
        QMessageBox.about(self, "Informacija", "Mogu liu premiksi?")
        self.state.kreniPremix()
        self.scrollAreaWidgetContents.vagaPrazni()
        
        QMessageBox.about(self, "Informacija", "Sacekati da se vaga isprazni!")
        self.state.zatvoriVagu()
        self.state.iskljuciP26()
        self.state.iskljuciPremix()
        
        if(odradjeno == zadato):
            #vaganje gotovo
            self.baza.obrisiZadatak(self.dataZadaci[0].id)
            self.dataZadaci = self.baza.zadaciList()
            self.ucitajZadatake()
            self.baza.izbrisiTrenutneZadatke(); 
            self.dataTrenutniZadatak = []
            QMessageBox.about(self, "Informacija", "Zadatak zavrsen!")
            
        else:
            #odvaga gotova       
            self.dataZadaci[0].odradjeno = self.dataZadaci[0].odradjeno + 1
            self.baza.povecajOdradjeno(self.dataZadaci[0].id,self.dataZadaci[0].odradjeno)
            self.baza.updatePoslednja(self.dataZadaci[0].id,self.prethodnaMera)
            self.dataZadaci = self.baza.zadaciList()
            self.ucitajZadatake()
          
        self.baza.izbrisiTrenutneZadatke(); 
        self.dataTrenutniZadatak = []             
        self.simvag = 0    
        self.scrollAreaWidgetContents.vagaOff()
        self._isvaga2 = False
        self.ucitajTrenutniZadatak()
        self.pocetakOdvage()
        
    def napuniMesaonu(self): 
        self.state.kreniMotorId(31);
        if( self._tmesaona<28):
            self.lineEdit_14.setText(str(self._tmesaona))
            
        if( self._tmesaona == 4): 
            #otvaram gornji zasun
            self.scrollAreaWidgetContents.infoMesaonaGore.crvena();
            self.mesaonaInfo.setText("Otvaram gornji zasun")
            self.state.kreniMotorId(22) #gornji zasun
            self.scrollAreaWidgetContents.mesaonaUlaz.puni()
        if( self._tmesaona == 8):
            self.state.iskljuciMotorId(22) #gornji zasun
            self.mesaonaInfo.setText("UTOVAR MATERIJALA");
            
        if( self._tmesaona == 20):
            self.scrollAreaWidgetContents.infoMesaonaGore.zelena(); 
            self.mesaonaInfo.setText("Zatvaram zasun gornji");
            self.scrollAreaWidgetContents.mesaonaUlaz.isprazni()
            self.state.kreniMotorId(26)

        if( self._tmesaona == 28):
            self.scrollAreaWidgetContents.infoMesaonaGore.crna();
            self.mesaonaInfo.setText("MESANJE U TOKU");            
            self.state.iskljuciMotorId(26) #gornji zasun;
            self.scrollAreaWidgetContents.mesaona.puni()          
            
            
        if( self._tmesaona>28):    
            self.lineEdit_14.setText(str(421-self._tmesaona))
            
        if( self._tmesaona > 390):            
            self.scrollAreaWidgetContents.infoMesaonaDole.crvena();
            self.mesaonaInfo.setText("Otvaram donji zasun")
            self.state.kreniMotorId(16) #donji zasun
            self.scrollAreaWidgetContents.mesaona.prazni()
            
        if( self._tmesaona > 398): 
            self.scrollAreaWidgetContents.infoMesaonaDole.crvena();
            self.mesaonaInfo.setText("otvoren zasun donji")
            self.state.iskljuciMotorId(16)
            
        if( self._tmesaona > 415):    
            self.scrollAreaWidgetContents.infoMesaonaDole.crna();
            self.mesaonaInfo.setText("zatv zasun donji")
            self.state.kreniMotorId(17) 

        if( self._tmesaona > 421): 
            self.scrollAreaWidgetContents.infoMesaonaDole.crna();
            self.mesaonaInfo.setText("SPREMNA")
            self.scrollAreaWidgetContents.infoMesaonaGore.zelena();
            self.scrollAreaWidgetContents.mesaona.isprazni()
            self.state.iskljuciMotorId(17)
            self._tmesaona = 0
            self._istmesaona = False
            self.scrollAreaWidgetContents.mesaona.isprazni()
            self.state.kreniElevator3()   
            self.scrollAreaWidgetContents.elevator2 = True 
            self.state.iskljuciMotorId(31);    
            if(self.radioButton_10.isChecked()==True):
                self.state.kreniMotorId(32)     
            if(self.radioButton_13.isChecked()==True):
                self.state.kreniMotorId(32)  
            if(self.radioButton_14.isChecked()==True):
                self.state.kreniMotorId(32)                  
                            
    #mera dostignuta    
    def vaganjeZavrseno(self, mera):
        self.iskljuciBinove()
        self.status("vaganje zavrseno")
        self.vaganje = False
        if(mera!=-1):
            self._trenutnaKomponenta.izmereno = mera-self.prethodnaMera
            self.baza.updateIzmereno(self._id, mera-self.prethodnaMera)
            self.prethodnaMera = mera 
        else:
            self._trenutnaKomponenta.izmereno = 0.1
            self.baza.updateIzmereno(self._id,0.1)       
        #refesh tabelu
        self.ucitajTrenutniZadatak()       
        self.pocetakKomponente();
        
    def krajOdvage(self): 
        self.status("Kraj odvage!")
        self.vaganjeZavrseno(-1)
     
    def ocistiTabelu(self):
        self.iskljuciBinove()
        self.isStart = False
        self.baza.izbrisiTrenutneZadatke();
        self.dataTrenutniZadatak = []
        self.ucitajTrenutniZadatak()
 
    #koja komponenta je u kom binu i dali postoji zadata komponenta
    def odredjivanjeBinova(self):
        self.status("Odredjivanje binova!")
        for z in self.dataTrenutniZadatak:
            komp = z.komponenta
            nasao = False
            for b in range(0,12):
                bin = self.dataBinovi.getBin(b)
                if(bin.artikl==None):
                    continue;
                if(bin.artikl.lower() == komp.lower()):
                    nasao = True
                    z.bin = b+1
                    koef = bin.koeficijent
                    z.zadato = self._ukupnaKolicina * (z.procenat/100.0) - koef
                    break;
            if(nasao == False):
                QMessageBox.about(self, "Greska", "Komponenta %s se ne nalazi ni u jednom binu" % (komp))
                self.stopZadatak()
                return False;
        return True
        
    #stoip dugme     
    def stopZadatak(self): 
        self.status("Stop!")
        self.isStart = False
        self._tvaga2 = 0
        self._isvaga2 = False
        self.vaganje = False
        self.iskljuciBinove()
        self.scrollAreaWidgetContents.vagaPuna()
        self.simvag = 0
        self.zadataMera = 0
        self.prethodnaMera = 0
        
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
        self.tableWidget_2.resizeColumnsToContents()  
        
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
            if(zz.kolicina==0):
                QMessageBox.about(self, "Greska", "Kolicina ne moze biti nula")
                return;
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
            self.simvag = self.simvag +3
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
            if(self.vaganje == True and self.mera >= self.zadataMera):
                self.iskljuciBinove()    
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
            self.status('Bin1 aktiviran')
            self.scrollAreaWidgetContents.bin1.on()
            self.state.kreniBin1();
        if(bin == 2):
            self.status('Bin2 aktiviran')
            self.scrollAreaWidgetContents.bin2.on()
            self.state.kreniBin2();
        if(bin == 3):
            self.scrollAreaWidgetContents.bin3.on()
            self.state.kreniBin3();
            self.status('Bin3 aktiviran')
        if(bin == 4):
            self.scrollAreaWidgetContents.bin4.on()
            self.state.kreniBin4();
            self.status('Bin4 aktiviran')
        if(bin == 5):
            self.scrollAreaWidgetContents.bin5.on()
            self.state.kreniBin5();
            self.status('Bin5 aktiviran')
        if(bin == 6):
            self.scrollAreaWidgetContents.bin6.on()
            self.state.kreniBin6();
            self.status('Bin6 aktiviran')
        if(bin == 7):
            self.scrollAreaWidgetContents.bin7.on()
            self.state.kreniBin7();
            self.status('Bin7 aktiviran')
        if(bin == 8):
            self.scrollAreaWidgetContents.bin8.on()
            self.state.kreniBin8();
            self.status('Bin8 aktiviran')
        if(bin == 9):
            self.scrollAreaWidgetContents.bin9.on()
            self.state.kreniBin9();
            self.status('Bin9 aktiviran')
        if(bin == 10):
            self.scrollAreaWidgetContents.bin10.on()
            self.state.kreniBin10();
            self.status('Bin10 aktiviran')
        if(bin == 11):
            self.scrollAreaWidgetContents.bin11.on()
            self.state.kreniBin11();
            self.status('Bin11 aktiviran')
        if(bin == 12):
            self.scrollAreaWidgetContents.bin12.on()
            self.state.kreniBin12();
            self.status('Bin12 aktiviran')            

    def iskljuciBinove(self):
        self.status('Binovi iskljuceni')
        self.scrollAreaWidgetContents.bin1.off() 
        self.scrollAreaWidgetContents.bin2.off()
        self.scrollAreaWidgetContents.bin3.off() 
        self.scrollAreaWidgetContents.bin4.off()
        self.scrollAreaWidgetContents.bin5.off() 
        self.scrollAreaWidgetContents.bin6.off()
        self.scrollAreaWidgetContents.bin7.off() 
        self.scrollAreaWidgetContents.bin8.off()
        self.scrollAreaWidgetContents.bin9.off() 
        self.scrollAreaWidgetContents.bin10.off()
        self.scrollAreaWidgetContents.bin11.off() 
        self.scrollAreaWidgetContents.bin12.off()  
        self.state.iskljuciBinove()       

    def on_bin_clicked(self,bin):
        art = self.dataBinovi.getBin(bin-1).artikl
        koe = self.dataBinovi.getBin(bin-1).koeficijent
        if(art==None):
            art = "PRAZAN"
        if(koe==None):
            koe = 0
        unos = dialogBin.dialogzaBin(self,art,koe)
        if( unos.exec_() == QDialog.Accepted):
            k = 0
            try:
               k = float(unos.getKoeficijent())
            except:
               k = 0
            self.dataBinovi.getBin(bin-1).artikl = unos.getArtikl()
            self.dataBinovi.getBin(bin-1).koeficijent = k
            self.baza.updateBin(bin,unos.getArtikl(),k)
            self.ucitajBinove()
            
    def btn_ispusti_1(self):
        self.state.iskljuciPId(19)
        self.state.iskljuciPId(23)
        self.state.iskljuciPId(26)
        self.state.iskljuciPId(9)
        self.state.iskljuciPId(18)
        self.state.iskljuciMotorId(28)

    def btn_ispusti_2(self):
        self.state.kreniPId(19)
        self.state.iskljuciPId(23)
        self.state.iskljuciPId(26)
        self.state.iskljuciPId(9)
        self.state.iskljuciPId(18)
        self.state.iskljuciMotorId(28)
    def btn_ispusti_3(self):
        self.state.kreniPId(19)    
        self.state.kreniPId(23)  
        self.state.iskljuciPId(26)
        self.state.iskljuciPId(9)
        self.state.iskljuciPId(18)
        self.state.kreniMotorId(28)


    def btn_ispusti_4(self):
        self.state.kreniPId(19)    
        self.state.kreniPId(23) 
        self.state.kreniPId(26)
        self.state.iskljuciPId(9)
        self.state.iskljuciPId(18)
        self.state.kreniMotorId(28)
        
    def btn_ispusti_5(self):
        pass
    def btn_ispusti_6(self):
        self.state.kreniPId(19) 
        self.state.iskljuciPId(23)
        self.state.iskljuciPId(26)
        self.state.iskljuciPId(9)
        self.state.iskljuciPId(18)
        self.state.kreniMotorId(28)
        
    def btn_ispusti_7(self):
        self.state.kreniPId(19)    
        self.state.iskljuciPId(23)
        self.state.iskljuciPId(26)
        self.state.kreniPId(9)
        self.state.iskljuciPId(18)
        self.state.kreniMotorId(28)

    def unosWindow(self):
        unos = dialogRecepture.dialogRecept(self.baza)
        unos.exec_();
        self.dataRecepture = self.baza.receptureList()
        
    def utovarWindow(self):
        unos = dialogGotove.dialogGotoveOdvage(self.baza)
        unos.exec_();        
            