'''
Created on Jan 15, 2016

@author: nikola
'''


import sys
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
from rucne import rucneKomande
from app import AppState
            
def main():
    state = AppState()
    #state.sim();
    app = QApplication(sys.argv)
    ex = rucneKomande.rucneProzor(state)
    rez = app.exec_()
    state.close();
    sys.exit(rez)
    


if __name__ == '__main__':
    main()

    