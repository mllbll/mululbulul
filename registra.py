import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber, QLineEdit, QFontDialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from inst import Ui_Inst

db = sqlite3.connect("prikol.db")
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS "users" (
    "username"  TEXT,
    "password"  TEXT)""")
db.commit()

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         uic.loadUi('untitled.ui', self)
#
#
#
#     def reg(self):
#         username = self.lineEdit
#         password = self.lineEdit_2
#         sql.execute(
#             f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}'")
#
#         if sql.fetchone() is None:
#             sql.execute(f"INSERT INTO users VALUES (?,?)", (username, password))
#             db.commit()
#             print('You have registered')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MainWindow()
#     ex.show()
#     sys.exit(app.exec())
#
