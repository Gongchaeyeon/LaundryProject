#-*- coding:utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Main import *
import pickle
course=''
total_price=0

class NewLaundry(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        label1 = QLabel('laundry 24 System', self)
        font1 = label1.font()
        font1.setPointSize(15)
        label1.setFont(font1)
        label1.setGeometry(95, 0, 300, 50)

        bt1 = QPushButton("75도 고온 (면 종류)\n+7500", self)
        bt2 = QPushButton("65도 중온 (혼방직물 종류)\n+7000", self)
        bt3 = QPushButton("45도 저온 (고급직물 종류)\n+6500", self)
        exit = QPushButton('Exit',self)

        bt1.resize(300, 60)
        bt2.resize(300, 60)
        bt3.resize(300, 60)
        exit.resize(300, 60)

        bt1.move(50, 70)
        bt2.move(50, 140)
        bt3.move(50, 210)
        exit.move(50, 280)

        self.setGeometry(300, 300, 400, 380)

        bt1.clicked.connect(self.ButtonClicked)
        bt2.clicked.connect(self.ButtonClicked)
        bt3.clicked.connect(self.ButtonClicked)
        exit.clicked.connect(self.ButtonClicked)

    def ButtonClicked(self):
        global course
        global total_price

        text = self.sender().text()
        course=text
        total_price = int(course.split('+')[1])

        if text == "Exit":
            option = QtWidgets.QMessageBox.warning(self, "경고", "프로그램을 종료하시겠습니까?",
                                                   QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
            if option == QtWidgets.QMessageBox.Yes:
                sys.exit(0)
        else:

            win = Detail()
            self.close()
            win.showModal()

    def showModal(self):
        return super().exec_()
#---------------------------------------------------------
class Detail(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global course

        label1 = QLabel('laundry 24 System', self)
        font1 = label1.font()
        font1.setPointSize(15)
        label1.setFont(font1)
        label1.setGeometry(95, 0, 300, 50)

        add1 = QPushButton("세탁추가\n+500", self)
        add2 = QPushButton("헹굼추가\n+500", self)
        add3 = QPushButton("탈수추가\n+500", self)
        add4 = QPushButton("섬유유연제\n+500", self)
        label2 = QLabel('상세정보',self)
        label2.setFont(font1)

        label2.setGeometry(300, 50, 300, 50)

        self.final = QLabel('기본 코스:{}\n'.format(course),self)
        self.final.setGeometry(300,100,300,300)

        back = QPushButton('뒤로가기',self)
        pay = QPushButton('결제하기',self)

        add1.resize(200, 60)
        add2.resize(200, 60)
        add3.resize(200, 60)
        add4.resize(200, 60)
        back.resize(100, 30)
        pay.resize(100, 30)

        add1.move(30, 70)
        add2.move(30, 140)
        add3.move(30, 210)
        add4.move(30, 280)
        back.move(370, 350)
        pay.move(480, 350)

        self.setGeometry(300, 300, 600, 400)

        add1.clicked.connect(self.ButtonClicked)
        add2.clicked.connect(self.ButtonClicked)
        add3.clicked.connect(self.ButtonClicked)
        add4.clicked.connect(self.ButtonClicked)
        back.clicked.connect(self.ButtonClicked)
        pay.clicked.connect(self.ButtonClicked)


    def ButtonClicked(self):
        global total_price

        text = self.sender().text()

        if text == "뒤로가기":
            win = NewLaundry()
            self.close()
            win.showModal()
        elif text == "결제하기":
            win = Pay()
            self.close()
            win.showModal()
        else:
            total_price+=500
            print(total_price)
            text = text.replace("\n", " ")
            self.final.setText(self.final.text()+'\n'+text)


    def showModal(self):
        return super().exec_()

#----------------------------------------------------
class Pay(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global total_price
        label1 = QLabel('laundry 24 System', self)
        font1 = label1.font()
        font1.setPointSize(15)
        label1.setFont(font1)
        label1.setGeometry(95, 0, 300, 50)

        k = total_price
        label2 = QLabel('금액:{}'.format(k), self)
        label2.setGeometry(130,50,300,100)
        font1 = label2.font()
        font1.setPointSize(15)
        label2.setFont(font1)

        label2 = QLabel('카드를 투입하여주세요', self)
        label2.setGeometry(125, 100, 200, 120)

        back = QPushButton('뒤로가기',self)
        pay = QPushButton('결제완료',self)

        back.setGeometry(200,200,90,30)
        pay.setGeometry(300, 200, 90, 30)

        pay.clicked.connect(self.ButtonClicked)
        back.clicked.connect(self.ButtonClicked)

        self.setGeometry(300,300,400,250)
    def ButtonClicked(self):

        text = self.sender().text()

        if text == "뒤로가기":
            win = Detail()
            self.close()
            win.showModal()

        else: # 결제완료
            win = StartLaundry()
            self.close()
            win.showModal()

    def showModal(self):
        return super().exec_()


# ----------------------------------------------------
class StartLaundry(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        label1 = QLabel('laundry 24 System', self)
        font1 = label1.font()
        font1.setPointSize(15)
        label1.setFont(font1)
        label1.setGeometry(95, 0, 300, 50)

        label2 = QLabel('* * * 세탁 진행중 * * *', self)
        font1 = label2.font()
        font1.setPointSize(15)
        label2.setFont(font1)
        label2.setGeometry(70, 100, 300, 40)

        label3 = QLabel('남은 시간: ', self)
        label3.setGeometry(10, 190, 100, 40)

        exit = QPushButton('강제종료', self)
        exit.setGeometry(300, 200, 90, 30)
        exit.clicked.connect(self.ButtonClicked)

        self.setGeometry(300, 300, 400, 250)

    def ButtonClicked(self):
        option = QtWidgets.QMessageBox.warning(self, "경고", "프로그램을 종료하시겠습니까?",
                                               QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
        if option == QtWidgets.QMessageBox.Yes:
            sys.exit(0)

    def showModal(self):
        return super().exec_()


# ----------------------------------------------------
class Done(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        label1 = QLabel('laundry 24 System', self)
        font1 = label1.font()
        font1.setPointSize(15)
        label1.setFont(font1)
        label1.setGeometry(95, 0, 300, 50)

        label2 = QLabel('세탁이 완료되었습니다.\n세탁물을 수거해주세요.', self)
        font1 = label2.font()
        font1.setPointSize(15)
        label2.setFont(font1)
        label2.setGeometry(70, 100, 300, 80)

        self.setGeometry(300, 300, 400, 250)

    def ButtonClicked(self):
        option = QtWidgets.QMessageBox.warning(self, "경고", "프로그램을 종료하시겠습니까?",
                                               QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
        if option == QtWidgets.QMessageBox.Yes:
            sys.exit(0)

    def showModal(self):
        return super().exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ma = NewLaundry()
    ma.show()
    sys.exit(app.exec_())