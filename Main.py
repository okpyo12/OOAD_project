from re import T
import sys
from time import process_time_ns
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QTableWidgetItem
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from CarDB.CarDBController import CarDBController
from Manager.ManagerController import ManagerController

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
    def __init__(self) :
        super(ParkingWindow, self).__init__()
        loadUi("parking.ui", self)

        self.dc = CarDBController()
        self.dc.settingParkingLotArr()
        self.setbtn()
        
        widget.currentChanged.connect(self.setbtn)

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

    def addparkingcar(self, carnum, parkinglotnum):
        if self.dc.insertDB(carnum, parkinglotnum):
            self.dc.carDB.parkinglotarr[parkinglotnum] = 1
            QMessageBox.information(self,'Information Title','차량 주차가 완료되었습니다.')
            self.dc.saveParkingLotArr()
            self.carNum.clear()
            return False
        else:
            self.dc.carDB.parkinglotarr[parkinglotnum] = 0
            QMessageBox.information(self,'Information Title','차량 번호를 다시 입력해주세요.')
            self.carNum.clear()
            return True

    def delparkingcar(self, parkinglotnum):
        text, ok = QInputDialog.getText(self, 'Input CarNum', '차량 번호를 입력해주세요:')
        if self.dc.deleteDB(text, parkinglotnum):
            self.dc.carDB.parkinglotarr[parkinglotnum] = 0
            QMessageBox.information(self,'Information Title','주차 되어 있는 차량을 꺼냈습니다.')
            self.dc.saveParkingLotArr()
            return False
        else:
            self.dc.carDB.parkinglotarr[parkinglotnum] = 1
            QMessageBox.information(self,'Information Title','주차 되어 있는 차량과 입력하신 차량 번호가 일치하지 않습니다.')
            return True

    def changeParkingspace1(self):
        if self.dc.carDB.parkinglotarr[0] == 0:
            if self.addparkingcar(self.carNum.toPlainText(), 0):
                self.parkingspace1.setText("주차 가능")
            else:
                self.parkingspace1.setText("주차 중")
        elif self.dc.carDB.parkinglotarr[0] == 1:
            if self.delparkingcar(0):
                self.parkingspace1.setText("주차 중")
            else:
                self.parkingspace1.setText("주차 가능")
            
    def changeParkingspace2(self):
        if self.dc.carDB.parkinglotarr[1] == 0:
            if self.addparkingcar(self.carNum.toPlainText(), 1):
                self.parkingspace2.setText("주차 가능")
            else: 
                self.parkingspace2.setText("주차 중")
        elif self.dc.carDB.parkinglotarr[1] == 1:
            if self.delparkingcar(1):
                self.parkingspace2.setText("주차 중")
            else:
                self.parkingspace2.setText("주차 가능")

    def changeParkingspace3(self):
        if self.dc.carDB.parkinglotarr[2] == 0:
            if self.addparkingcar(self.carNum.toPlainText(), 2):
                self.parkingspace3.setText("주차 가능")
            else:
                self.parkingspace3.setText("주차 중")
        elif self.dc.carDB.parkinglotarr[2] == 1:
            if self.delparkingcar(2):
                self.parkingspace3.setText("주차 중")
            else:
                self.parkingspace3.setText("주차 가능")

    def changeParkingspace4(self):
        if self.dc.carDB.parkinglotarr[3] == 0:
            if self.addparkingcar(self.carNum.toPlainText(), 3):
                self.parkingspace4.setText("주차 가능")
            else:
                self.parkingspace4.setText("주차 중")
        elif self.dc.carDB.parkinglotarr[3] == 1:
            if self.delparkingcar(3):
                self.parkingspace4.setText("주차 중")
            else:
                self.parkingspace4.setText("주차 가능")

    def changeParkingspace5(self):
        if self.dc.carDB.parkinglotarr[4] == 0:
            if self.addparkingcar(self.carNum.toPlainText(), 4):
                self.parkingspace5.setText("주차 가능")
            else:
                self.parkingspace4.setText("주차 중")
        elif self.dc.carDB.parkinglotarr[4] == 1:
            if self.delparkingcar(4):
                self.parkingspace5.setText("주차 중")
            else:
                self.parkingspace5.setText("주차 가능")

    def changeParkingspace6(self):
        if self.dc.carDB.parkinglotarr[5] == 0:
            if self.addparkingcar(self.carNum.toPlainText(), 5):
                self.parkingspace6.setText("주차 가능")
            else:
                self.parkingspace6.setText("주차 중")
        elif self.dc.carDB.parkinglotarr[5] == 1:
            if self.delparkingcar(5):
                self.parkingspace6.setText("주차 중")
            else:
                self.parkingspace6.setText("주차 가능")

    def changeParkingspace7(self):
        if self.dc.carDB.parkinglotarr[6] == 0:
            if self.addparkingcar(self.carNum.toPlainText(), 6):
                self.parkingspace7.setText("주차 가능")
            else:
                self.parkingspace7.setText("주차 중")
        elif self.dc.carDB.parkinglotarr[6] == 1:
            if self.delparkingcar(6):
                self.parkingspace7.setText("주차 중")
            else:
                self.parkingspace7.setText("주차 가능")

    def changeParkingspace8(self):
        if self.dc.carDB.parkinglotarr[7] == 0:
            if self.addparkingcar(self.carNum.toPlainText(), 7):
                self.parkingspace8.setText("주차 가능")
            else:
                self.parkingspace8.setText("주차 중")
        elif self.dc.carDB.parkinglotarr[7] == 1:
            if self.delparkingcar(7):
                self.parkingspace8.setText("주차 중")
            else:
                self.parkingspace8.setText("주차 가능")

    def changeParkingspace9(self):
        if self.dc.carDB.parkinglotarr[8] == 0:
            if self.addparkingcar(self.carNum.toPlainText(), 8):
                self.parkingspace9.setText("주차 가능")
            else:
                self.parkingspace9.setText("주차 중")
        elif self.dc.carDB.parkinglotarr[8] == 1:
            if self.delparkingcar(8):
                self.parkingspace9.setText("주차 중")
            else:
                self.parkingspace9.setText("주차 가능")

    def changeParkingspace10(self):
        if self.dc.carDB.parkinglotarr[9] == 0:
            if self.addparkingcar(self.carNum.toPlainText(), 9):
                self.parkingspace10.setText("주차 가능")
            else:
                self.parkingspace10.setText("주차 중")
        elif self.dc.carDB.parkinglotarr[9] == 1:
            if self.delparkingcar(9):
                self.parkingspace10.setText("주차 중")
            else:
                self.parkingspace10.setText("주차 가능")

    def changeParkingspace11(self):
        if self.dc.carDB.parkinglotarr[10] == 0:
            if self.addparkingcar(self.carNum.toPlainText(), 10):
                self.parkingspace11.setText("주차 가능")
            else:
                self.parkingspace11.setText("주차 중")
        elif self.dc.carDB.parkinglotarr[10] == 1:
            if self.delparkingcar(10):
                self.parkingspace11.setText("주차 중")
            else:
                self.parkingspace11.setText("주차 가능")

    def changeParkingspace12(self):
        if self.dc.carDB.parkinglotarr[11] == 0:
            if self.addparkingcar(self.carNum.toPlainText(), 11):
                self.parkingspace12.setText("주차 가능")
            else:
                self.parkingspace12.setText("주차 중")
        elif self.dc.carDB.parkinglotarr[11] == 1:
            if self.delparkingcar(11):
                self.parkingspace12.setText("주차 중")
            else:
                self.parkingspace12.setText("주차 가능")

    def changeParkingspace13(self):
        if self.dc.carDB.parkinglotarr[12] == 0:
            if self.addparkingcar(self.carNum.toPlainText(), 12):
                self.parkingspace13.setText("주차 가능")
            else:
                self.parkingspace13.setText("주차 중")
        elif self.dc.carDB.parkinglotarr[12] == 1:
            if self.delparkingcar(12):
                self.parkingspace13.setText("주차 중")
            else:
                self.parkingspace13.setText("주차 가능")

    def changeParkingspace14(self):
        if self.dc.carDB.parkinglotarr[13] == 0:
            if self.addparkingcar(self.carNum.toPlainText(), 13):
                self.parkingspace14.setText("주차 가능")
            else:
                self.parkingspace14.setText("주차 중")
        elif self.dc.carDB.parkinglotarr[13] == 1:
            if self.delparkingcar(13):
                self.parkingspace14.setText("주차 중")
            else:
                self.parkingspace14.setText("주차 가능")

    def setbtn(self):
        with open("CarDB/LotDB.txt", 'r+') as f:
            i = 0
            lines = f.readlines()
            for line in lines:
                line = line.rstrip()
                self.dc.carDB.parkinglotarr[i] = int(line)
                i += 1

        if self.dc.carDB.parkinglotarr[0] == 0:
            self.parkingspace1.setText("주차 가능")
        elif self.dc.carDB.parkinglotarr[0] == 1:
            self.parkingspace1.setText("주차 중")
        else:
            self.parkingspace1.setText("고정 주차\n자리")
        if self.dc.carDB.parkinglotarr[1] == 0:
            self.parkingspace2.setText("주차 가능")
        elif self.dc.carDB.parkinglotarr[1] == 1:
            self.parkingspace2.setText("주차 중")
        else:
            self.parkingspace2.setText("고정 주차\n자리")
        if self.dc.carDB.parkinglotarr[2] == 0:
            self.parkingspace3.setText("주차 가능")
        elif self.dc.carDB.parkinglotarr[2] == 1:
            self.parkingspace3.setText("주차 중")
        else:
            self.parkingspace3.setText("고정 주차\n자리")
        if self.dc.carDB.parkinglotarr[3] == 0:
            self.parkingspace4.setText("주차 가능")
        elif self.dc.carDB.parkinglotarr[3] == 1:
            self.parkingspace4.setText("주차 중")
        else:
            self.parkingspace4.setText("고정 주차\n자리")
        if self.dc.carDB.parkinglotarr[4] == 0:
            self.parkingspace5.setText("주차 가능")
        elif self.dc.carDB.parkinglotarr[4] == 1:
            self.parkingspace5.setText("주차 중")
        else:
            self.parkingspace5.setText("고정 주차\n자리")
        if self.dc.carDB.parkinglotarr[5] == 0:
            self.parkingspace6.setText("주차 가능")
        elif self.dc.carDB.parkinglotarr[5] == 1:
            self.parkingspace6.setText("주차 중")
        else:
            self.parkingspace6.setText("고정 주차\n자리")
        if self.dc.carDB.parkinglotarr[6] == 0:
            self.parkingspace7.setText("주차 가능")
        elif self.dc.carDB.parkinglotarr[6] == 1:
            self.parkingspace7.setText("주차 중")
        else:
            self.parkingspace7.setText("고정 주차\n자리")
        if self.dc.carDB.parkinglotarr[7] == 0:
            self.parkingspace8.setText("주차 가능")
        elif self.dc.carDB.parkinglotarr[7] == 1:
            self.parkingspace8.setText("주차 중")
        else:
            self.parkingspace8.setText("고정 주차\n자리")
        if self.dc.carDB.parkinglotarr[8] == 0:
            self.parkingspace9.setText("주차 가능")
        elif self.dc.carDB.parkinglotarr[8] == 1:
            self.parkingspace9.setText("주차 중")
        else:
            self.parkingspace9.setText("고정 주차\n자리")
        if self.dc.carDB.parkinglotarr[9] == 0:
            self.parkingspace10.setText("주차 가능")
        elif self.dc.carDB.parkinglotarr[9] == 1:
            self.parkingspace10.setText("주차 중")
        else:
            self.parkingspace10.setText("고정 주차\n자리")
        if self.dc.carDB.parkinglotarr[10] == 0:
            self.parkingspace11.setText("주차 가능")
        elif self.dc.carDB.parkinglotarr[10] == 1:
            self.parkingspace11.setText("주차 중")
        else:
            self.parkingspace11.setText("고정 주차\n자리")
        if self.dc.carDB.parkinglotarr[11] == 0:
            self.parkingspace12.setText("주차 가능")
        elif self.dc.carDB.parkinglotarr[11] == 1:
            self.parkingspace12.setText("주차 중")
        else:
            self.parkingspace12.setText("고정 주차\n자리")
        if self.dc.carDB.parkinglotarr[12] == 0:
            self.parkingspace13.setText("주차 가능")
        elif self.dc.carDB.parkinglotarr[12] == 1:
            self.parkingspace13.setText("주차 중")
        else:
            self.parkingspace13.setText("고정 주차\n자리")
        if self.dc.carDB.parkinglotarr[13] == 0:
            self.parkingspace14.setText("주차 가능")
        elif self.dc.carDB.parkinglotarr[13] == 1:
            self.parkingspace14.setText("주차 중")
        else:
            self.parkingspace14.setText("고정 주차\n자리")
            
class ManagerWindow(QMainWindow):

    def __init__(self) :
        super(ManagerWindow, self).__init__()
        loadUi("manager.ui", self)
        
        self.mc = ManagerController()
        
        self.mainmenu.clicked.connect(self.mainmenuBtn)

        self.FixedCarList.setRowCount(14)
        self.FixedCarList.setColumnCount(2)

        self.showfixedcar()

        self.addbtn.clicked.connect(self.addfixedcar)
        self.delbtn.clicked.connect(self.delfixedcar)

    def addfixedcar(self):
        if self.fixedcarnum.toPlainText() and self.fixedcarlotnum.toPlainText():
            if (self.mc.insertFixedCarDB(self.fixedcarnum.toPlainText(), self.fixedcarlotnum.toPlainText())):
                QMessageBox.information(self,'Information Title','고정 주차 차량이 등록되었습니다.')
                self.showfixedcar()
                self.fixedcarnum.clear()
                self.fixedcarlotnum.clear()
            else:
                QMessageBox.information(self,'Information Title','고정 주차 차량 등록에 실패했습니다.\n차량 번호와 주차 위치 번호를 다시 입력해주세요.')
                self.fixedcarnum.clear()
                self.fixedcarlotnum.clear()
        else:
            QMessageBox.information(self,'Information Title','고정 주차 차량 등록에 실패했습니다.\n차량 번호와 주차 위치 번호를 다시 입력해주세요.')
            self.fixedcarnum.clear()
            self.fixedcarlotnum.clear()
    
    def delfixedcar(self):
        if self.fixedcarnum.toPlainText() and self.fixedcarlotnum.toPlainText():
            if (self.mc.deleteFixecCarDB(self.fixedcarnum.toPlainText(), self.fixedcarlotnum.toPlainText())):
                QMessageBox.information(self,'Information Title','고정 주차 차량이 삭제되었습니다.')
                self.showfixedcar()
                self.fixedcarnum.clear()
                self.fixedcarlotnum.clear()
            else:
                QMessageBox.information(self,'Information Title','차량 번호 혹은 주차 위치 번호가 일치 하지 않습니다.\n차량 번호와 주차 위치 번호를 다시 입력해주세요.')
                self.showfixedcar()
                self.fixedcarnum.clear()
                self.fixedcarlotnum.clear()
        else:
            QMessageBox.information(self,'Information Title','차량 번호 혹은 주차 위치 번호가 일치 하지 않습니다.\n차량 번호와 주차 위치 번호를 다시 입력해주세요.')
            self.showfixedcar()
            self.fixedcarnum.clear()
            self.fixedcarlotnum.clear()

    def showfixedcar(self):
        self.mc.settingFixecCarDB()
        for i in range(14):
            for j in range(2):
                self.FixedCarList.setItem(i,j,QTableWidgetItem(''))

        for i in range(len(self.mc.gettingFixedCarDB())):
            for j in range(2):
                self.FixedCarList.setItem(i,j,QTableWidgetItem(self.mc.gettingFixedCarDB()[i][j]))

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