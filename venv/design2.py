# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(852, 522)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PgUp = QtWidgets.QPushButton(self.centralwidget)
        self.PgUp.setGeometry(QtCore.QRect(760, 400, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PgUp.setFont(font)
        self.PgUp.setObjectName("PgUp")
        self.PgDown = QtWidgets.QPushButton(self.centralwidget)
        self.PgDown.setGeometry(QtCore.QRect(800, 400, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.PgDown.setFont(font)
        self.PgDown.setObjectName("PgDown")
        self.showInp = QtWidgets.QLineEdit(self.centralwidget)
        self.showInp.setGeometry(QtCore.QRect(10, 30, 141, 31))
        self.showInp.setObjectName("showInp")
        self.showBtn = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn.setGeometry(QtCore.QRect(160, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.showBtn.setFont(font)
        self.showBtn.setObjectName("showBtn")
        self.xInp = QtWidgets.QLineEdit(self.centralwidget)
        self.xInp.setGeometry(QtCore.QRect(30, 70, 211, 31))
        self.xInp.setObjectName("xInp")
        self.yInp = QtWidgets.QLineEdit(self.centralwidget)
        self.yInp.setGeometry(QtCore.QRect(30, 110, 211, 31))
        self.yInp.setObjectName("yInp")
        self.xLab = QtWidgets.QLabel(self.centralwidget)
        self.xLab.setGeometry(QtCore.QRect(10, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.xLab.setFont(font)
        self.xLab.setObjectName("xLab")
        self.yLab = QtWidgets.QLabel(self.centralwidget)
        self.yLab.setGeometry(QtCore.QRect(10, 110, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yLab.setFont(font)
        self.yLab.setObjectName("yLab")
        self.mapLab = QtWidgets.QLabel(self.centralwidget)
        self.mapLab.setGeometry(QtCore.QRect(250, 0, 601, 391))
        self.mapLab.setText("")
        self.mapLab.setObjectName("mapLab")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(240, 0, 21, 501))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(250, 370, 611, 41))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PgUp.setText(_translate("MainWindow", "+"))
        self.PgDown.setText(_translate("MainWindow", "-"))
        self.showBtn.setText(_translate("MainWindow", "показать"))
        self.xLab.setText(_translate("MainWindow", "X:"))
        self.yLab.setText(_translate("MainWindow", "Y:"))
