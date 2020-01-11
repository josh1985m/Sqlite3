import sqlite3
con = sqlite3.connect('mydatabase.db')


def sql_update(con):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
    con.commit()


sql_update(con)