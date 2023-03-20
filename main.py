import sqlite3
con = sqlite3.connect("database.db")

#Create cursor
c = con.cursor()

c.execute('''INSERT OR IGNORE INTO Jernbanestasjon VALUES 
('Trondheim', 5.1)
''')
c.execute('''INSERT OR IGNORE INTO Delstrekning VALUES 
('Trond_Stein', 120, 2, 'Trondheim', 'Steinkjaer')
''')
c.execute('''INSERT OR IGNORE INTO Banestrekning VALUES 
('Nordlandsbanen', 0, 'Trondheim', 'Bodoe', 'Trond_Stein')
''')
c.execute('''INSERT OR IGNORE INTO Togrute VALUES 
('1', 0, 'Trondheim', 'Bodoe', 'Trond_Stein')
''')




          
c.execute("SELECT * FROM Jernbanestasjon")
c.execute("SELECT * FROM Delstrekning")
c.execute("SELECT * FROM Banestrekning")
rows = c.fetchall()
print(rows)

con.commit()
con.close()



# c.execute("SELECT * FROM Jernbanestasjon")
# rows = c.fetchall()
# print("All rows in the table Jernbasestasjon:")
# print(rows)
# con.commit()
# con.close()
