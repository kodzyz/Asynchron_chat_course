import sqlite3 as sq

con = sq.connect('saper.db')
cur = con.cursor()
con.close()
