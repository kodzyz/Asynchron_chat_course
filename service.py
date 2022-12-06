from sqlalchemy import create_engine
import os

if os.path.exists("some.db"):
    os.remove("some.db")
e = create_engine("sqlite:///some.db")
e.execute("""
    create table employee (
        emp_id integer primary key,
        emp_name varchar
    )
""")

e.execute("""
    create table employee_of_month (
        emp_id integer primary key,
        emp_name varchar
    )
""")

e.execute("""insert into employee(emp_name) values ('ed')""")
e.execute("""insert into employee(emp_name) values ('jack')""")
e.execute("""insert into employee(emp_name) values ('fred')""")

# sqlite3 some.db
# SQLite version 3.36.0 2021-10-26 10:02:50
# Enter ".help" for usage hints.
# sqlite> .tables
# employee           employee_of_month
# sqlite> SELECT * FROM employee;
# 1|ed
# 2|jack
# 3|fred
# sqlite> SELECT * FROM employee_of_month;
# sqlite>

engine = create_engine("sqlite:///some.db")
result = engine.execute(
            "select emp_id, emp_name from "
            "employee where emp_id=:emp_id",
            emp_id=3)
row = result.fetchone()
print(row)  # (3, 'fred')
print(row['emp_name'])  # fred
