# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pacecalculator-qt.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(334, 203)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pacecalculator.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pacelabel = QtGui.QLabel(self.centralwidget)
        self.pacelabel.setGeometry(QtCore.QRect(20, 40, 59, 14))
        self.pacelabel.setObjectName(_fromUtf8("pacelabel"))
        self.distancelabel = QtGui.QLabel(self.centralwidget)
        self.distancelabel.setGeometry(QtCore.QRect(20, 80, 59, 14))
        self.distancelabel.setObjectName(_fromUtf8("distancelabel"))
        self.pace = QtGui.QLineEdit(self.centralwidget)
        self.pace.setGeometry(QtCore.QRect(110, 30, 113, 24))
        self.pace.setObjectName(_fromUtf8("pace"))
        self.distance = QtGui.QLineEdit(self.centralwidget)
        self.distance.setGeometry(QtCore.QRect(110, 80, 113, 24))
        self.distance.setObjectName(_fromUtf8("distance"))
        self.resultlabel = QtGui.QLabel(self.centralwidget)
        self.resultlabel.setGeometry(QtCore.QRect(30, 160, 59, 14))
        self.resultlabel.setObjectName(_fromUtf8("resultlabel"))
        self.result = QtGui.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(110, 160, 201, 20))
        self.result.setText(_fromUtf8(""))
        self.result.setObjectName(_fromUtf8("result"))
        self.submit = QtGui.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(230, 120, 89, 27))
        self.submit.setObjectName(_fromUtf8("submit"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pace Calculator", None))
        self.pacelabel.setText(_translate("MainWindow", "Pace:", None))
        self.distancelabel.setText(_translate("MainWindow", "Distance:", None))
        self.resultlabel.setText(_translate("MainWindow", "Result:", None))
        self.submit.setText(_translate("MainWindow", "Submit", None))

import pacecalculator_rc
