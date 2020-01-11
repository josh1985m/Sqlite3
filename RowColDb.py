import sqlite3
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()
print(cursorObj.execute('SELECT * FROM employees').rowcount)
rows = cursorObj.fetchall()
print(len(rows))
print(cursorObj.execute('DELETE FROM employees').rowcount)




