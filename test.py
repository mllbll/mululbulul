from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber, QLineEdit, QFontDialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from PyQt5 import uic
import sqlite3

db = sqlite3.connect("usersss.db")
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS "users" (
    "username"  TEXT,
    "password"  TEXT)""")
db.commit()


def reg(username,password,okno):
    sql.execute(f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}'")

    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?)", (username, password))
        db.commit()
        okno.setText('You have registered')
        login()
    else:
        print('Такая запись уже существует')
        for i in sql.execute('SELECT * FROM users'):
            print(i)


def login(username,password,okno):
    a = sql.execute(f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}'")
    db.commit()
    if not sql.fetchone():
        okno.setText("Нет такой записи")
        for i in sql.execute('SELECT * FROM users'):
            print(i)
        reg()
    else:
        okno.setText('Welcome')



class MainWindow(QMainWindow):
    def __init__(self):
      super(MainWindow, self).__init__()
      uic.loadUi('untitled.ui', self)

    def vopros(self):
        uic.loadUi('vopros.ui', self)

    def initUI(self):
        usname=self.lineEdit
        passw=self.lineEdit_2
        reg(self.lineEdit,self.lineEdit_2,self.okno)
        if self.sender().text()=='Создать аккаунт':
            login()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())