import sqlite3 as sq

with sq.connect("cars.db") as con:
    cur = con.cursor()

    # for sql in con.iterdump():
    #     print(sql)  # бэкап БД
        # BEGIN TRANSACTION;
        # CREATE TABLE cars (
        #         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         model TEXT,
        #         price INTEGER
        #     );
        # INSERT INTO "cars" VALUES(2,'Mercedes',59127);
        # INSERT INTO "cars" VALUES(3,'Skoda',11000);
        # INSERT INTO "cars" VALUES(4,'Volvo',31000);

    with open("sql_damp.sql", "w") as f:
        for sql in con.iterdump():
            f.write(sql)

    with open("sql_damp.sql", "r") as f:
        sql = f.read()
        cur.executescript(sql)  # восстановить БД
