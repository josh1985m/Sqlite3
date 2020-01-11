import sqlite3
con = sqlite3.connect('mydatabase.db')


def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute("INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")
    con.commit()
    cursorObj.execute(
        'INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    con.commit()


entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
sql_insert(con, entities)