'''
Created on Jan 15, 2016

@author: nikola
'''


import sys
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
from rucne import rucneKomande

            
def main():
    
    app = QApplication(sys.argv)
    ex = rucneKomande.rucneProzor()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

    