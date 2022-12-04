import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS users')
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
        )""")

# SELECT rowid, * FROM users
# INSERT INTO users VALUES(1, 'Михаил', 1, 19, 1000)
# INSERT INTO users (name, old, score) VALUES('Михаил', 19, 1000)
# SELECT name, old, score FROM users
# SELECT rowid, * FROM users WHERE score < 1000
# SELECT rowid, * FROM users WHERE score BETWEEN 500 AND 1000
# SELECT rowid, * FROM users WHERE score == 200
# SELECT rowid, * FROM users WHERE old > 20 AND score < 1000
# SELECT rowid, * FROM users WHERE old IN(19, 32) AND score < 1000 OR sex = 1

# SELECT rowid, * FROM users
# WHERE old IN(19, 32) AND (score < 1000 OR sex = 1)
# ORDER BY old DESC
# LIMIT 2
#
# SELECT rowid, * FROM users
# WHERE score > 100 ORDER BY score DESC LIMIT 5 OFFSET 2
