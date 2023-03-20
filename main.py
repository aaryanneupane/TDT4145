import sqlite3
con = sqlite3.connect("database.db")

#Create cursor
c = con.cursor()

c.execute('''INSERT OR IGNORE INTO Jernbanestasjon VALUES 
('Trondheim', 5.1),
('Steinkjer', 3.6),
('Mosjøen', 6.8),
('MoIRana', 3.5),
('Fauske', 34.0),
('Bodø', 4.1),
''')
c.execute('''INSERT OR IGNORE INTO Delstrekning VALUES 
('TrondStein', 120, 2, 'Trondheim', 'Steinkjer')
('SteinMosjø', 280, 1, 'Steinkjer', 'Mosjøen')
('MosjøMoIRa', 90, 1, 'Mosjøen', 'MoIRana')
('MoIRaFaus', 170, 1, 'MoIRana', 'Fauske')
('FausBod', 60, 1, 'Fauske', 'Bodø')
''')
c.execute('''INSERT OR IGNORE INTO Banestrekning VALUES 
('Nordlandsbanen', 0, 'Trondheim', 'Bodoe', 'TrondStein')
''')
c.execute('''INSERT OR IGNORE INTO Togrute VALUES 
('1', 0, 'Trondheim', 'Bodoe', 'Trond_Stein')
''')





        
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
