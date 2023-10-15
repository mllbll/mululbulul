import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber, QLineEdit, QFontDialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from inst import Ui_Inst

db = sqlite3.connect("data.db")
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS "users" (
    "username"  TEXT,
    "password"  TEXT)""")
db.commit()


# chanse=input('У вас уже есть учётная запись Д/Н ', )
# if chanse=='Д':
#     login()
# else:
#     reg()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('untitled.ui', self)

    def vopros(self):
        uic.loadUi('vopros.ui', self)

    def initUI(self):
        self.pushButton_2.clicked.connect(self.login)
        self.pushButton.clicked.connect(self.reg)



    def reg(self):
        username = input("username>> ")
        password = input("password>> ")
        sql.execute(
            f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}'")

        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO users VALUES (?,?)", (username, password))
            db.commit()
            print('You have registered')

    def login(self):
        username = input("username>> ")
        password = input("password>> ")
        a = sql.execute(
            f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}'")
        db.commit()
        if not sql.fetchone():
            print("Нет такой записи")
        else:
            print('Hello , ', username)
class MyInst(QtWidgets.QWidget, Ui_Inst):                          # +++
    def __init__(self, parent=None):
        super(MyInst, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())