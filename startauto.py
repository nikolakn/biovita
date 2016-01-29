'''
Created on Jan 15, 2016

@author: nikola
'''


import sys
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
from automatsko import autoKomande
from app import AppState
            
def main():
    state = AppState()
    app = QApplication(sys.argv)
    ex = autoKomande.autoProzor(state)
    rez = app.exec_()
    state.close();
    sys.exit(rez)
    


if __name__ == '__main__':
    main()

    