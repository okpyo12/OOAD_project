# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/pyosangwoo/Documents/GitHub/OOAD_Project/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.parking_btn = QtWidgets.QPushButton(self.centralwidget)
        self.parking_btn.setGeometry(QtCore.QRect(210, 250, 131, 51))
        self.parking_btn.setObjectName("parking_btn")
        self.manager_btn = QtWidgets.QPushButton(self.centralwidget)
        self.manager_btn.setGeometry(QtCore.QRect(460, 250, 131, 51))
        self.manager_btn.setObjectName("manager_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
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
        self.parking_btn.setText(_translate("MainWindow", "주차장 들어가기"))
        self.manager_btn.setText(_translate("MainWindow", "주차 관리하기"))
