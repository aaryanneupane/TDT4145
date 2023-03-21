import sqlite3
con = sqlite3.connect("database.db")

#Create cursor
c = con.cursor()

#Jernbanestasjon
c.execute('''INSERT OR IGNORE INTO Jernbanestasjon VALUES
('Trondheim', 5.1),
('Steinkjer', 3.6),
('Mosjøen', 6.8),
('MoIRana', 3.5),
('Fauske', 34.0),
('Bodø', 4.1)
''')
          
#Delstrekning
c.execute('''INSERT OR IGNORE INTO Delstrekning VALUES 
('Trond-Stein', 120, 2, 'Trondheim', 'Steinkjer'),
('SteinMosjø', 280, 1, 'Steinkjer', 'Mosjøen'),
('MosjøMoIRa', 90, 1, 'Mosjøen', 'MoIRana'),
('MoIRaFaus', 170, 1, 'MoIRana', 'Fauske'),
('FausBod', 60, 1, 'Fauske', 'Bodø')
''')
          
#Banestrekning
c.execute('''INSERT OR IGNORE INTO Banestrekning VALUES 
('Nordlandsbanen', 0, 'Trondheim', 'Bodø')
''')

#Operatør      
c.execute('''INSERT INTO Operatør VALUES 
('SJ')
''')
          
#Togrute   Kan hende man bør ha tidspunkt her?
c.execute('''INSERT INTO Togrute VALUES 
('1', 'True', 'Nordlandsbanen', 'SJ', 'Trondheim', 'Bodø')
('2', 'False', 'Nordlandsbanen', 'SJ', 'MoIRana' , 'Trondheim')
''')

#TogruteForekomst 
c.execute('''INSERT INTO TogruteForekomst VALUES 
('1', 'SJ'  )
('2', 'SJ', ')
''')

#HarDelstrekning
c.execute('''INSERT INTO HarDelstrekning VALUES 
('1', 'SJ')
''')
        
c.execute("SELECT * FROM Banestrekning")
rows = c.fetchall()
print('All rows from Banestrekning')
print(rows)

con.commit()
con.close()

