import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *
from Management import *
from Customer import *


class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('Data/세탁기.png'))
        self.setWindowTitle('Laundry 24')

        label1 = QLabel('laundry 24 System', self)
        font1 = label1.font()
        font1.setPointSize(20)
        label1.setFont(font1)
        label1.setGeometry(80, 0, 300, 50)

        admin = QPushButton("관리자", self)
        admin.move(30, 80)
        admin.resize(170, 170)

        customer = QPushButton("고객", self)
        customer.move(250, 80)
        customer.resize(170, 170)

        exit = QPushButton('Exit',self)
        exit.move(320, 300)
        exit.resize(100, 30)

        admin.clicked.connect(self.ButtonClicked)
        customer.clicked.connect(self.ButtonClicked)
        exit.clicked.connect(self.ButtonClicked)

        self.setGeometry(300, 300, 450, 350)

    def ButtonClicked(self):
        text = self.sender().text()

        if text == "관리자":
            win = Login()
            self.close()
            win.showModal()


        elif text == "고객":
            win = NewLaundry()
            self.close()
            win.showModal()

        elif text == "Exit":
            option = QtWidgets.QMessageBox.warning(self, "경고", "프로그램을 종료하시겠습니까?", QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
            if option == QtWidgets.QMessageBox.Yes:
                sys.exit(0)


    def show(self):
        super().show()
