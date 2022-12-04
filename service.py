import sqlite3 as sq


def readAva(n):
    try:
        with open(f"avas/{n}.png", "rb") as f:
            return f.read()
    except IOError as e:
        print(e)
        return False


def writeAva(name, data):
    try:
        with open(name, "wb") as f:
            f.write(data)
    except IOError as e:
        print(e)
        return False

    return True


with sq.connect("cars.db") as con:
    con.row_factory = sq.Row  # вариантом выходных данных является словарь
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        ava BLOB, 
        score INTEGER)
    """)  # BLOB данные в бинарнов виде

    img = readAva(1)
    if img:
        binary = sq.Binary(img)
        cur.execute("INSERT INTO users VALUES ('Николай', ?, 1000)", (binary,))

        cur.execute("SELECT ava FROM users LIMIT 1")
        img = cur.fetchone()['ava']

        writeAva("out.png", img)
