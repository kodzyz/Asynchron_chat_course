import sqlite3 as sq

cars = [
    ('Audi', 52642),
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bentley', 350000)
]

with sq.connect("cars.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )""")

    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)
    #cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)
    # именованные параметры
    #cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'A%'", {'Price': 0})
    # несколько отдельных SQL-команд
    cur.executescript("""DELETE FROM cars WHERE model LIKE 'A%';
        UPDATE cars SET price = price+1000
    """)
