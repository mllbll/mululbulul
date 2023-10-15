# my first calculator
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber, QLineEdit, QFontDialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.flag = 0
        self.razchet = ''
        self.initUI()
        self.result = 0
        self.setStyleSheet("background-color: purple;")

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Calculator')

        self.label1 = QLineEdit(self)
        self.label1.move(40, 30)
        self.label1.resize(320, 70)
        self.label1.setFont(QFont('Times new Roman', 25))
        self.label1.setStyleSheet("background-color: orange;")

        self.btn = QPushButton('1', self)
        self.btn.resize(60, 60)
        self.btn.move(90, 150)
        self.btn.clicked.connect(self.one)
        self.btn.setStyleSheet("background-color: orange;")

        self.btn1 = QPushButton('2', self)
        self.btn1.resize(60, 60)
        self.btn1.move(150, 150)
        self.btn1.clicked.connect(self.two)
        self.btn1.setStyleSheet("background-color: orange;")

        self.btn3 = QPushButton('3', self)
        self.btn3.resize(60, 60)
        self.btn3.move(210, 150)
        self.btn3.clicked.connect(self.three)
        self.btn3.setStyleSheet("background-color: orange;")

        self.btnsqrt = QPushButton('sqrt(x)', self)
        self.btnsqrt.resize(60, 60)
        self.btnsqrt.move(270, 150)
        self.btnsqrt.clicked.connect(self.koren)
        self.btnsqrt.setStyleSheet("background-color: orange;")

        self.btn4 = QPushButton('4', self)
        self.btn4.resize(60, 60)
        self.btn4.move(90, 210)
        self.btn4.clicked.connect(self.fore)
        self.btn4.setStyleSheet("background-color: orange;")

        self.btn5 = QPushButton('5', self)
        self.btn5.resize(60, 60)
        self.btn5.move(150, 210)
        self.btn5.clicked.connect(self.five)
        self.btn5.setStyleSheet("background-color: orange;")

        self.btn6 = QPushButton('6', self)
        self.btn6.resize(60, 60)
        self.btn6.move(210, 210)
        self.btn6.clicked.connect(self.six)
        self.btn6.setStyleSheet("background-color: orange;")

        self.btnstepen = QPushButton('x^2', self)
        self.btnstepen.resize(60, 60)
        self.btnstepen.move(270, 210)
        self.btnstepen.clicked.connect(self.kvadrat)
        self.btnstepen.setStyleSheet("background-color: orange;")

        self.btn7 = QPushButton('7', self)
        self.btn7.resize(60, 60)
        self.btn7.move(90, 270)
        self.btn7.clicked.connect(self.seven)
        self.btn7.setStyleSheet("background-color: orange;")

        self.btn8 = QPushButton('8', self)
        self.btn8.resize(60, 60)
        self.btn8.move(150, 270)
        self.btn8.clicked.connect(self.eight)
        self.btn8.setStyleSheet("background-color: orange;")

        self.btn9 = QPushButton('9', self)
        self.btn9.resize(60, 60)
        self.btn9.move(210, 270)
        self.btn9.clicked.connect(self.nine)
        self.btn9.setStyleSheet("background-color: orange;")

        self.btnumnozhenie = QPushButton('*', self)
        self.btnumnozhenie.resize(60, 60)
        self.btnumnozhenie.move(270, 270)
        self.btnumnozhenie.clicked.connect(self.umnozhenie)
        self.btnumnozhenie.setStyleSheet("background-color: orange;")

        self.btnplus = QPushButton('+', self)
        self.btnplus.resize(60, 60)
        self.btnplus.move(90, 330)
        self.btnplus.clicked.connect(self.plus)
        self.btnplus.setStyleSheet("background-color: orange;")

        self.btnminus = QPushButton('-', self)
        self.btnminus.resize(60, 60)
        self.btnminus.move(210, 330)
        self.btnminus.clicked.connect(self.minus)
        self.btnminus.setStyleSheet("background-color: orange;")

        self.btnravno = QPushButton('=', self)
        self.btnravno.resize(60, 60)
        self.btnravno.move(270, 330)
        self.btnravno.clicked.connect(self.ravno)
        self.btnravno.setStyleSheet("background-color: orange;")

        self.btn0 = QPushButton('0', self)
        self.btn0.resize(60, 60)
        self.btn0.move(150, 330)
        self.btn0.clicked.connect(self.zero)
        self.btn0.setStyleSheet("background-color: orange;")

        self.btnclear = QPushButton('AC', self)
        self.btnclear.resize(60, 60)
        self.btnclear.move(20, 180)
        self.btnclear.clicked.connect(self.allclear)
        self.btnclear.setStyleSheet("background-color: orange;")

        self.btnudalit = QPushButton('DEL', self)
        self.btnudalit.resize(60, 60)
        self.btnudalit.move(20, 250)
        self.btnudalit.clicked.connect(self.udalenie)
        self.btnudalit.setStyleSheet("background-color: orange;")

    def ravno(self):
        otvet = self.label1.text()
        try:
            ans = eval(otvet)
            self.label1.setText('Ответ:   {}'.format(str(ans)))
        except:
            self.label1.setText('Ошибка')

    def plus(self):
        text = self.label1.text()
        self.label1.setText(text + "+")

    def minus(self):
        text = self.label1.text()
        self.label1.setText(text + "-")

    def umnozhenie(self):
        text = self.label1.text()
        self.label1.setText(text + "*")

    def kvadrat(self):
        text = self.label1.text()
        self.label1.setText(text + "**2")

    def koren(self):
        text = self.label1.text()
        self.label1.setText(text + "**0.5")

    def one(self):
        text = self.label1.text()
        self.label1.setText(text + "1")

    def two(self):
        text = self.label1.text()
        self.label1.setText(text + "2")

    def three(self):
        text = self.label1.text()
        self.label1.setText(text + "3")

    def fore(self):
        text = self.label1.text()
        self.label1.setText(text + "4")

    def five(self):
        text = self.label1.text()
        self.label1.setText(text + "5")

    def six(self):
        text = self.label1.text()
        self.label1.setText(text + "6")

    def seven(self):
        text = self.label1.text()
        self.label1.setText(text + "7")

    def eight(self):
        text = self.label1.text()
        self.label1.setText(text + "8")

    def nine(self):
        text = self.label1.text()
        self.label1.setText(text + "9")

    def zero(self):
        text = self.label1.text()
        self.label1.setText(text + "0")

    def allclear(self):
        self.label1.setText('')

    def udalenie(self):
        text = self.label1.text()
        self.label1.setText(text[:len(text) - 1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())