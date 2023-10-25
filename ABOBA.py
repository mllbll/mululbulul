import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber, QLineEdit, QFontDialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

db = sqlite3.connect("aboba.db")
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS "users" (
    "username"  TEXT,
    "password"  TEXT)""")
db.commit()

print("Если вы хотите зарегестрировать учетную запись нажмите 1")
print("Если вы хотите войти в учетную запись нажмите 2")

con=int(input())


def reg():
    username = input("username>> ")
    password = input("password>> ")
    sql.execute(f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}'")

    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?)", (username, password))
        db.commit()
        print('You have registered')
        login()
    else:
        print('Такая запись уже существует')
        for i in sql.execute('SELECT * FROM users'):
            print(i)


def login():
    username = input("username>> ")
    password = input("password>> ")
    a = sql.execute(f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}'")
    db.commit()
    if not sql.fetchone():
        print("Нет такой записи")
        for i in sql.execute('SELECT * FROM users'):
            print(i)
        reg()
    else:
        print('Welcome')


if con==1:
    reg()
else:
    login()
