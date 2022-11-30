import sqlite3 as sq

con = sq.connect('test.db')
cur = con.cursor()
# cur.execute("CREATE TABLE user(name,lastname,birthdate,login,password,score)")
# res=cur.execute("SELECT name FROM sqlite_master")
# print(res.fetchall())
row = ['Phil', 'Collins', '15.03.1978', 'PhilColl', 'Qwerty123', 7]
param = """INSERT INTO user VALUES (?, ?, ?, ?, ?, ?)"""
cur.execute(param, row)
con.commit()
cur.close()

# cur.execute("""INSERT INTO user(name,lastname,birthdate,login,password,score) VALUES('Phil', 'Collins', '15.03.1978', 'PhilColl', 'Qwerty123', '7') """)