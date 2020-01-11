import sqlite3
con = sqlite3.connect('mydatabase.db')


def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('create table if not exists projects(id integer, name text)')
    con.commit()


sql_fetch(con)