# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vreme.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(306, 188)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 130, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.dan = QtGui.QLineEdit(Dialog)
        self.dan.setGeometry(QtCore.QRect(90, 40, 51, 20))
        self.dan.setObjectName(_fromUtf8("dan"))
        self.mesec = QtGui.QLineEdit(Dialog)
        self.mesec.setGeometry(QtCore.QRect(150, 40, 51, 20))
        self.mesec.setObjectName(_fromUtf8("mesec"))
        self.godina = QtGui.QLineEdit(Dialog)
        self.godina.setGeometry(QtCore.QRect(210, 40, 71, 20))
        self.godina.setObjectName(_fromUtf8("godina"))
        self.sati = QtGui.QLineEdit(Dialog)
        self.sati.setGeometry(QtCore.QRect(90, 80, 61, 20))
        self.sati.setObjectName(_fromUtf8("sati"))
        self.minuti = QtGui.QLineEdit(Dialog)
        self.minuti.setGeometry(QtCore.QRect(180, 80, 61, 20))
        self.minuti.setObjectName(_fromUtf8("minuti"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 57, 14))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 57, 14))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 20, 57, 14))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(150, 20, 57, 14))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(220, 20, 57, 14))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(160, 80, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Datum", None))
        self.label_2.setText(_translate("Dialog", "Vreme", None))
        self.label_3.setText(_translate("Dialog", "Dan", None))
        self.label_4.setText(_translate("Dialog", "Mesec", None))
        self.label_5.setText(_translate("Dialog", "Godina", None))
        self.label_6.setText(_translate("Dialog", ":", None))

