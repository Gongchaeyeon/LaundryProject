import sys
from PyQt5.QtWidgets import *

class Login(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('laundry 24 System', self)
        font1 = label1.font()
        font1.setPointSize(20)
        label1.setFont(font1)
        label1.setGeometry(80, 0, 300, 50)

    def onOKButtonClicked(self):
        self.accept()

    def onCancelButtonClicked(self):
        self.reject()

    def showModal(self):
        return super().exec_()