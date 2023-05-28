#-*- coding:utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Main import *
import pickle
from Data import *

class Login(QDialog):
    def __init__(self):
        super().__init__()

        self.dbfilename = 'Data/sales.txt'
        # self.ReadDB()
        # self.ViewDB()
        # self.WriteDB()
        # self.ViewSales()
        self.initUI()
    def initUI(self):

        label1 = QLabel('관리자 로그인', self)
        font1 = label1.font()
        font1.setPointSize(15)
        label1.setFont(font1)
        label1.setGeometry(120, 0, 300, 50)

        lb1 = QLabel("ID: ",self)
        lb1.setGeometry(10, 80, 100, 20)
        self.tf1 = QLineEdit(self)
        self.tf1.move(50, 80)

        lb2 = QLabel("PW: ", self)
        lb2.setGeometry(10, 120, 100, 20)
        self.tf2 = QLineEdit(self)
        self.tf2.move(50, 120)

        login = QPushButton("Login", self)
        login.move(270, 70)
        login.resize(120, 80)

        self.setGeometry(300, 300, 400, 200)

        login.clicked.connect(self.ButtonClicked)

    def ButtonClicked(self):
        if self.tf1.text() == 'admin' and self.tf2.text() == '1234':
            win = AdminMain()
            self.close()
            win.showModal()

    def showModal(self):
        return super().exec_()

class AdminMain(QDialog): #관리자 main 화면
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        label1 = QLabel('Laundry24 (admin)', self)

        font1 = label1.font()
        font1.setPointSize(15)
        label1.setFont(font1)
        label1.setGeometry(120, 0, 300, 50)


        Inventory = QPushButton("재고관리", self)
        Inventory.move(30, 80)
        Inventory.resize(170, 170)

        Sales = QPushButton("매출확인", self)
        Sales.move(250, 80)
        Sales.resize(170, 170)

        exit = QPushButton('Exit',self)
        exit.move(320, 300)
        exit.resize(100, 30)

        Inventory.clicked.connect(self.ButtonClicked)
        Sales.clicked.connect(self.ButtonClicked)
        exit.clicked.connect(self.ButtonClicked)

        self.setGeometry(300, 300, 450, 350)

    def ButtonClicked(self):
        text = self.sender().text()

        if text == "재고관리":
            win = InventoryCheck()
            self.close()
            win.showModal()
        elif text == "매출확인":
            win = SalesCheck()
            self.close()
            win.showModal()

        elif text == "Exit":
            option = QtWidgets.QMessageBox.warning(self, "경고", "프로그램을 종료하시겠습니까?",QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
            if option == QtWidgets.QMessageBox.Yes:
                sys.exit(0)
    def showModal(self):
        return super().exec_()

class SalesCheck(QDialog): #매출 확인
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        cnt=0
        price = 0

        label1 = QLabel('매출표', self)
        font1 = label1.font()
        font1.setPointSize(15)
        label1.setFont(font1)
        label1.setGeometry(20, 20, 300, 25)

        label2 = QLabel(' test ', self)
        font1 = label1.font()
        font1.setPointSize(10)
        label2.setFont(font1)
        label2.setGeometry(20, 280, 300, 25)

        self.ta1 = QTableWidget(self)
        self.ta1.resize(200, 200)
        self.ta1.setGeometry(20, 50, 400, 200)
        self.ta1.setColumnCount(3)

        table_column=["번호", "날짜", "가격"]

        datalist=[]
        f = open("Data\Sale.txt", 'r')

        while True:
            data = f.readline()
            if data == '\n': break
            a,b,c = data.split('\t')
            price+=int(c)
            datalist.append(a)
            datalist.append(b)
            datalist.append(c[:-1])
            cnt+=1
        f.close()

        self.ta1.setRowCount(cnt)

        r=0; c=0
        for i in range(len(datalist)):
            self.ta1.setItem(r, c, QTableWidgetItem(datalist[i]))
            self.ta1.item(r,c).setTextAlignment(Qt.AlignCenter)
            c += 1
            if c%3==0: r+=1; c=0
        label2.setText('총매출액: {}'.format(price))
        self.ta1.setColumnWidth(0,90)
        self.ta1.setHorizontalHeaderLabels(table_column)

        #       버튼 ------------------------------------------
        back = QPushButton('뒤로가기', self)
        back.move(210, 280)
        back.resize(100, 30)
        back.clicked.connect(self.ButtonClicked)
        exit = QPushButton('Exit', self)
        exit.move(320, 280)
        exit.resize(100, 30)
        exit.clicked.connect(self.ButtonClicked)
        #       -----------------------------------------------
        self.setGeometry(300, 300, 450, 350)

    def ButtonClicked(self):
        text = self.sender().text()

        if text == "뒤로가기":
            win = AdminMain()
            self.close()
            win.showModal()
        elif text == "Exit":
            option = QtWidgets.QMessageBox.warning(self, "경고", "프로그램을 종료하시겠습니까?",QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
            if option == QtWidgets.QMessageBox.Yes:
                sys.exit(0)

    def showModal(self):
        return super().exec_()

class InventoryCheck(QDialog): #재고 확인
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        cnt=0
        label1 = QLabel('재고관리', self)
        font1 = label1.font()
        font1.setPointSize(15)
        label1.setFont(font1)
        label1.setGeometry(20, 20, 300, 25)

        self.ta1 = QTableWidget(self)
        self.ta1.setColumnCount(3)

        table_column=["상품ID", "상품", "재고"]

        datalist=[]
        f = open("Data\Inventory.txt", 'r')
        while True:
            data = f.readline()
            if data == '\n': break
            a,b,c = data.split('\t')
            datalist.append(a)
            datalist.append(b)
            datalist.append(c[:-1])
            cnt+=1
        f.close()

        self.ta1.setRowCount(cnt)

        r=0; c=0
        for i in range(len(datalist)):
            self.ta1.setItem(r, c, QTableWidgetItem(datalist[i]))
            self.ta1.item(r,c).setTextAlignment(Qt.AlignCenter)
            c += 1
            if c%3==0: r+=1; c=0

        self.ta1.setColumnWidth(0,90)
        self.ta1.resize(200, 200)
        self.ta1.setGeometry(20, 50, 400, 200)
        self.ta1.setHorizontalHeaderLabels(table_column)

        back = QPushButton('뒤로가기',self)
        exit = QPushButton('Exit',self)
        edit = QPushButton('Edit',self)

        back.move(210, 280)
        exit.move(320, 280)
        edit.move(320,10)

        back.resize(100, 30)
        exit.resize(100, 30)
        edit.resize(100, 30)

        back.clicked.connect(self.ButtonClicked)
        exit.clicked.connect(self.ButtonClicked)
        edit.clicked.connect(self.ButtonClicked)

        self.setGeometry(300, 300, 450, 350)

    def ButtonClicked(self):
        text = self.sender().text()
        if text == "Edit":
            win = Edit()
            self.close()
            win.showModal()
        elif text == "뒤로가기":
            win = AdminMain()
            self.close()
            win.showModal()
        elif text == "Exit":
            option = QtWidgets.QMessageBox.warning(self, "경고", "프로그램을 종료하시겠습니까?",QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
            if option == QtWidgets.QMessageBox.Yes:
                sys.exit(0)
    def showModal(self):
        return super().exec_()

class Edit(QDialog): #재고 수량 수정
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        label1 = QLabel('수정할 ID와 수량을 입력하세요.', self)
        font1 = label1.font()
        font1.setPointSize(10)
        label1.setFont(font1)
        label1.setGeometry(10, 20, 300, 50)
        
        lb1 = QLabel("상품ID: ", self)
        lb1.setGeometry(10, 80, 80, 20)
        self.tf1 = QLineEdit(self)
        self.tf1.move(80, 80)

        lb2 = QLabel("재고: ", self)
        lb2.setGeometry(15, 120, 80, 20)
        self.tf2 = QLineEdit(self)
        self.tf2.move(80, 120)

        edit = QPushButton("수정", self)
        edit.move(290, 70)
        edit.resize(80, 80)

        self.setGeometry(300, 300, 400, 200)

        edit.clicked.connect(self.ButtonClicked)

    def ButtonClicked(self):
        if self.tf1.text() == '' and self.tf2.text() == '':
            print("공백X")
        #ID가 없을 때 -> try문으로 할 것
        #혹은 제대로 되었을 때 완료되었음 표시
        win = AdminMain()
        self.close()
        win.showModal()

    def showModal(self):
        return super().exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ma = AdminMain()
    ma.show()
    sys.exit(app.exec_())