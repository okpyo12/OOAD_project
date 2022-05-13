from cgitb import text
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from User.UserController import UserController
from CarDB.CarDBController import CarDBController

class MainWindow(QMainWindow):
    def __init__(self) :
        super(MainWindow, self).__init__()
        loadUi("main.ui", self)
        self.parking_btn.clicked.connect(self.parkingBtn)
        self.manager_btn.clicked.connect(self.managerBtn)

    def parkingBtn(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def managerBtn(self):
        widget.setCurrentIndex(widget.currentIndex()+2)

class ParkingWindow(QMainWindow) :
    parkinglot_num = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    def __init__(self) :
        super(ParkingWindow, self).__init__()
        loadUi("parking.ui", self)

        self.uc = UserController()
        self.dc = CarDBController()
        self.dc.clearDB()

        self.mainmenu.clicked.connect(self.mainmenuBtn)

        self.parkingspace1.clicked.connect(self.changeParkingspace1)
        self.parkingspace2.clicked.connect(self.changeParkingspace2)
        self.parkingspace3.clicked.connect(self.changeParkingspace3)
        self.parkingspace4.clicked.connect(self.changeParkingspace4)
        self.parkingspace5.clicked.connect(self.changeParkingspace5)
        self.parkingspace6.clicked.connect(self.changeParkingspace6)
        self.parkingspace7.clicked.connect(self.changeParkingspace7)
        self.parkingspace8.clicked.connect(self.changeParkingspace8)
        self.parkingspace9.clicked.connect(self.changeParkingspace9)
        self.parkingspace10.clicked.connect(self.changeParkingspace10)
        self.parkingspace11.clicked.connect(self.changeParkingspace11)
        self.parkingspace12.clicked.connect(self.changeParkingspace12)
        self.parkingspace13.clicked.connect(self.changeParkingspace13)
        self.parkingspace14.clicked.connect(self.changeParkingspace14)

    def mainmenuBtn(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def parkingcar(self, carnum, parkinglotnum):
        if self.dc.insertDB(carnum, parkinglotnum):
            self.parkinglot_num[parkinglotnum] = 1
            QMessageBox.information(self,'Information Title','차량 주차가 완료되었습니다.')
            self.carNum.clear()
            return False
        else:
            self.parkinglot_num[parkinglotnum] = 0
            QMessageBox.information(self,'Information Title','차량 번호를 다시 입력해주세요.')
            self.carNum.clear()
            return True

    def parkingoutcar(self, parkinglotnum):
        text, ok = QInputDialog.getText(self, 'Input CarNum', '차량 번호를 입력해주세요:')
        if self.dc.deleteDB(text, parkinglotnum):
            self.parkinglot_num[parkinglotnum] = 0
            QMessageBox.information(self,'Information Title','주차 되어 있는 차량을 꺼냈습니다.')
            return False
        else:
            self.parkinglot_num[parkinglotnum] = 1
            QMessageBox.information(self,'Information Title','주차 되어 있는 차량과 입력하신 차량 번호가 일치하지 않습니다.')
            return True

    def changeParkingspace1(self):
        if self.parkinglot_num[0] == 0:
            if self.parkingcar(self.carNum.toPlainText(), 0):
                self.parkingspace1.setText("주차 가능")
            else:
                self.parkingspace1.setText("주차 불가능")
        elif self.parkinglot_num[0] == 1:
            if self.parkingoutcar(0):
                self.parkingspace1.setText("주차 불가능")
            else:
                self.parkingspace1.setText("주차 가능")
    
    def changeParkingspace2(self):
        if self.parkinglot_num[1] == 0:
            if self.parkingcar(self.carNum.toPlainText(), 1):
                self.parkingspace2.setText("주차 가능")
            else: 
                self.parkingspace2.setText("주차 불가능")
        elif self.parkinglot_num[1] == 1:
            if self.parkingoutcar(1):
                self.parkingspace2.setText("주차 불가능")
            else:
                self.parkingspace2.setText("주차 가능")

    def changeParkingspace3(self):
        if self.parkinglot_num[2] == 0:
            if self.parkingcar(self.carNum.toPlainText(), 2):
                self.parkingspace3.setText("주차 가능")
            else:
                self.parkingspace3.setText("주차 불가능")
        elif self.parkinglot_num[2] == 1:
            if self.parkingoutcar(2):
                self.parkingspace3.setText("주차 불가능")
            else:
                self.parkingspace3.setText("주차 가능")

    def changeParkingspace4(self):
        if self.parkinglot_num[3] == 0:
            if self.parkingcar(self.carNum.toPlainText(), 3):
                self.parkingspace4.setText("주차 가능")
            else:
                self.parkingspace4.setText("주차 불가능")
        elif self.parkinglot_num[3] == 1:
            if self.parkingoutcar(3):
                self.parkingspace4.setText("주차 불가능")
            else:
                self.parkingspace4.setText("주차 가능")

    def changeParkingspace5(self):
        if self.parkinglot_num[4] == 0:
            if self.parkingcar(self.carNum.toPlainText(), 4):
                self.parkingspace5.setText("주차 가능")
            else:
                self.parkingspace4.setText("주차 불가능")
        elif self.parkinglot_num[4] == 1:
            if self.parkingoutcar(4):
                self.parkingspace5.setText("주차 불가능")
            else:
                self.parkingspace5.setText("주차 가능")

    def changeParkingspace6(self):
        if self.parkinglot_num[5] == 0:
            if self.parkingcar(self.carNum.toPlainText(), 5):
                self.parkingspace6.setText("주차 가능")
            else:
                self.parkingspace6.setText("주차 불가능")
        elif self.parkinglot_num[5] == 1:
            if self.parkingoutcar(5):
                self.parkingspace6.setText("주차 불가능")
            else:
                self.parkingspace6.setText("주차 가능")

    def changeParkingspace7(self):
        if self.parkinglot_num[6] == 0:
            if self.parkingcar(self.carNum.toPlainText(), 6):
                self.parkingspace7.setText("주차 가능")
            else:
                self.parkingspace7.setText("주차 불가능")
        elif self.parkinglot_num[6] == 1:
            if self.parkingoutcar(6):
                self.parkingspace7.setText("주차 불가능")
            else:
                self.parkingspace7.setText("주차 가능")

    def changeParkingspace8(self):
        if self.parkinglot_num[7] == 0:
            if self.parkingcar(self.carNum.toPlainText(), 7):
                self.parkingspace8.setText("주차 가능")
            else:
                self.parkingspace8.setText("주차 불가능")
        elif self.parkinglot_num[7] == 1:
            if self.parkingoutcar(7):
                self.parkingspace8.setText("주차 불가능")
            else:
                self.parkingspace8.setText("주차 가능")

    def changeParkingspace9(self):
        if self.parkinglot_num[8] == 0:
            if self.parkingcar(self.carNum.toPlainText(), 8):
                self.parkingspace9.setText("주차 가능")
            else:
                self.parkingspace9.setText("주차 불가능")
        elif self.parkinglot_num[8] == 1:
            if self.parkingoutcar(8):
                self.parkingspace9.setText("주차 불가능")
            else:
                self.parkingspace9.setText("주차 가능")

    def changeParkingspace10(self):
        if self.parkinglot_num[9] == 0:
            if self.parkingcar(self.carNum.toPlainText(), 9):
                self.parkingspace10.setText("주차 가능")
            else:
                self.parkingspace10.setText("주차 불가능")
        elif self.parkinglot_num[9] == 1:
            if self.parkingoutcar(9):
                self.parkingspace10.setText("주차 불가능")
            else:
                self.parkingspace10.setText("주차 가능")

    def changeParkingspace11(self):
        if self.parkinglot_num[10] == 0:
            if self.parkingcar(self.carNum.toPlainText(), 10):
                self.parkingspace11.setText("주차 가능")
            else:
                self.parkingspace11.setText("주차 불가능")
        elif self.parkinglot_num[10] == 1:
            if self.parkingoutcar(10):
                self.parkingspace11.setText("주차 불가능")
            else:
                self.parkingspace11.setText("주차 가능")

    def changeParkingspace12(self):
        if self.parkinglot_num[11] == 0:
            if self.parkingcar(self.carNum.toPlainText(), 11):
                self.parkingspace12.setText("주차 가능")
            else:
                self.parkingspace12.setText("주차 불가능")
        elif self.parkinglot_num[11] == 1:
            if self.parkingoutcar(11):
                self.parkingspace12.setText("주차 불가능")
            else:
                self.parkingspace12.setText("주차 가능")

    def changeParkingspace13(self):
        if self.parkinglot_num[12] == 0:
            if self.parkingcar(self.carNum.toPlainText(), 12):
                self.parkingspace13.setText("주차 가능")
            else:
                self.parkingspace13.setText("주차 불가능")
        elif self.parkinglot_num[12] == 1:
            if self.parkingoutcar(12):
                self.parkingspace13.setText("주차 불가능")
            else:
                self.parkingspace13.setText("주차 가능")

    def changeParkingspace14(self):
        if self.parkinglot_num[13] == 0:
            if self.parkingcar(self.carNum.toPlainText(), 13):
                self.parkingspace14.setText("주차 가능")
            else:
                self.parkingspace14.setText("주차 불가능")
        elif self.parkinglot_num[13] == 1:
            if self.parkingoutcar(13):
                self.parkingspace14.setText("주차 불가능")
            else:
                self.parkingspace14.setText("주차 가능")

class ManagerWindow(QMainWindow):
    def __init__(self) :
        super(ManagerWindow, self).__init__()
        loadUi("manager.ui", self)

        self.uc = UserController()
        self.dc = CarDBController()
        
        self.mainmenu.clicked.connect(self.mainmenuBtn)

    def mainmenuBtn(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = MainWindow()
    parkingwindow = ParkingWindow()
    managerwindow = ManagerWindow()
    widget.addWidget(mainwindow)
    widget.addWidget(parkingwindow)
    widget.addWidget(managerwindow)
    widget.setFixedHeight(600)
    widget.setFixedWidth(800)
    widget.show()
    app.exec_()
