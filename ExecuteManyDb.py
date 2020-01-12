import sqlite3
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()
cursorObj.execute('create table if not exists projects(id integer, name text)')
data = [(1, "Ridesharing"), (2, "Water Purifying"), (3, "Forensics"), (4, "Botany")]
cursorObj.executemany("INSERT INTO projects VALUES(?, ?)", data)
#Be careful of injection attacks                   ^  ^    ^^^^#
con.commit()