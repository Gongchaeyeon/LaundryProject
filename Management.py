import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Main import *

class Login(QDialog):
    def __init__(self):
        super().__init__()
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

        lb2 = QLabel("ID: ", self)
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


        Inventory = QPushButton("재고확인", self)
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

        if text == "재고확인":
            print("재고확인")
            win = InventoryCheck()
            self.close()
            win.showModal()
        elif text == "매출확인":
            print("매출확인")
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

        label1 = QLabel('매출표', self)

        font1 = label1.font()
        font1.setPointSize(15)
        label1.setFont(font1)
        label1.setGeometry(20, 20, 300, 25)


        self.ta1 = QTableWidget(self)
        self.ta1.resize(200, 200)
        self.ta1.setGeometry(20, 50, 500, 200)

        self.ta1.setColumnCount(4)

        table_column=["번호", "상품", "수량", "가격"]

        self.ta1.setHorizontalHeaderLabels(table_column)

#       버튼 ------------------------------------------
        back = QPushButton('뒤로가기',self)
        back.move(310, 280)
        back.resize(100, 30)
        back.clicked.connect(self.ButtonClicked)
        exit = QPushButton('Exit',self)
        exit.move(420, 280)
        exit.resize(100, 30)
        exit.clicked.connect(self.ButtonClicked)
#       -----------------------------------------------
        self.setGeometry(300, 300, 550, 350)

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

        label1 = QLabel('재고확인', self)

        font1 = label1.font()
        font1.setPointSize(15)
        label1.setFont(font1)
        label1.setGeometry(20, 20, 300, 25)


        self.ta1 = QTableWidget(self)
        self.ta1.resize(200, 200)
        self.ta1.setGeometry(20, 50, 400, 200)

        self.ta1.setColumnCount(3)

        table_column=["상품ID", "상품", "재고"]

        self.ta1.setHorizontalHeaderLabels(table_column)

#       버튼 ------------------------------------------
        back = QPushButton('뒤로가기',self)
        back.move(210, 280)
        back.resize(100, 30)
        back.clicked.connect(self.ButtonClicked)
        exit = QPushButton('Exit',self)
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ma = InventoryCheck()
    ma.show()
    sys.exit(app.exec_())