import sqlite3
con = sqlite3.connect('mydatabase.db')


def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('DROP table if exists employees')
    con.commit()


sql_fetch(con)