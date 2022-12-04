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

    cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER)
    """)

    cur.executemany("INSERT INTO cars VALUES(NULL,?, ?)", cars)

    cur.execute("SELECT model, price FROM cars")
    # получить доступ к сформированной выборке
    # rows = cur.fetchall()  # список из кортежей
    # print(rows)
    # rows = cur.fetchone()  # только первая запись # ('Mercedes', 59127)
    # print(rows)
    # rows = cur.fetchmany(4)  # не более четырех первых записей
    # print(rows)  # [('Mercedes', 59127), ('Skoda', 11000), ('Volvo', 31000), ('Bentley', 352000)]
    for result in cur:  # записи в цикле
        print(result)



