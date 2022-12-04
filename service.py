import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()

    #cur.execute('SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5 OFFSET 2')
    # result = cur.fetchall()  # список из кортежей
    # print(result)  # [(2, 'Николай', 1, 22, 500), (3, 'Федор', 1, 32, 200), (5, 'Сергей ', 1, 33, 200)]
    # или
    #result1 = cur.fetchone()  # первая запись
    #result2 = cur.fetchmany(2)  # выбранное количество записей
    #print(result1)  # (2, 'Николай', 1, 22, 500)
    #print(result2)  # [(3, 'Федор', 1, 32, 200), (5, 'Сергей ', 1, 33, 200)]

    # for result in cur:
    #     print(result)
        # (2, 'Николай', 1, 22, 500)
        # (3, 'Федор', 1, 32, 200)
        # (5, 'Сергей ', 1, 33, 200)

    # cur.execute('DROP TABLE IF EXISTS users')
    # cur.execute("""CREATE TABLE IF NOT EXISTS users (
    #     user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     name TEXT NOT NULL,
    #     sex INTEGER NOT NULL DEFAULT 1,
    #     old INTEGER,
    #     score INTEGER
    #     )""")

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

# UPDATE users SET score = 1000 WHERE rowid = 1
# UPDATE users SET score = score + 500 WHERE sex = 2
# UPDATE users SET score = 1500 WHERE name LIKE 'Федор'
# UPDATE users SET score = score + 100 WHERE name LIKE 'М%'
# UPDATE users SET score = 700 WHERE name LIKE 'С_рг%'
# UPDATE users SET score = 800, old = 45 WHERE old > 40
#
# DELETE FROM users WHERE ROWID IN (2, 5)
# SELECT ROWID, * FROM users

    # cur.execute('DROP TABLE IF EXISTS games')
    # cur.execute("""CREATE TABLE IF NOT EXISTS games (
    #         user_id INTEGER,
    #         score INTEGER,
    #         time INTEGER
    #         )""")
    # cur.execute('INSERT INTO games VALUES(1, 200, 100000)')
    # cur.execute('INSERT INTO games VALUES(1, 300, 110010)')
    # cur.execute('INSERT INTO games VALUES(2, 500, 100010)')
    # cur.execute('INSERT INTO games VALUES(1, 400, 201034)')
    # cur.execute('INSERT INTO games VALUES(3, 100, 200010)')
    # cur.execute('INSERT INTO games VALUES(2, 600, 210000)')
    # cur.execute('INSERT INTO games VALUES(2, 300, 200010)')

# SELECT user_id FROM games WHERE user_id = 1
# агрегирование: count(), sum(), avr(), min(), max()
# SELECT count(user_id) FROM games WHERE user_id = 1
# SELECT count(user_id) as count FROM games WHERE user_id = 1
# количество уникальных user_id -> DISTINCT
# SELECT count(DISTINCT user_id) as count FROM games
# SELECT sum(score) as scores FROM games where user_id = 1
# группировка
# SELECT user_id, sum(score) as sum
# FROM games
# WHERE score > 300
# GROUP BY user_id
# ORDER BY sum DESC
# LIMIT 1

# INNER JOIN:
# SELECT name, sex, games.score FROM games
# JOIN users ON games.user_id = users.ROWID
#
# SELECT name, sex, games.score FROM users, games
#
# SELECT name, sex, sum(games.score) as score
# FROM games
# JOIN users ON games.user_id = users.rowid
# GROUP BY user_id
# ORDER BY score DESC

    cur.execute('DROP TABLE IF EXISTS tab1')
    cur.execute("""CREATE TABLE IF NOT EXISTS tab1 (                    
                        score INTEGER,
                        `from` TEXT
                        )""")
    cur.execute('INSERT INTO tab1 VALUES(100, "tab1")')
    cur.execute('INSERT INTO tab1 VALUES(200, "tab1")')
    cur.execute('INSERT INTO tab1 VALUES(300, "tab1")')

    cur.execute('DROP TABLE IF EXISTS tab2')
    cur.execute("""CREATE TABLE IF NOT EXISTS tab2 (                    
                        val INTEGER,
                        type TEXT
                        )""")
    cur.execute('INSERT INTO tab2 VALUES(200, "tab2")')
    cur.execute('INSERT INTO tab2 VALUES(300, "tab2")')
    cur.execute('INSERT INTO tab2 VALUES(400, "tab2")')

# UNION
# SELECT score, `from` FROM tab1
# UNION SELECT val, type FROM tab2


