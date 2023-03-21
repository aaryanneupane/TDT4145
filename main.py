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
('Trondheim-Steinkjer', 120, 2, 'Trondheim', 'Steinkjer'),
('Steinkjer-Mosjøen', 280, 1, 'Steinkjer', 'Mosjøen'),
('Mosjøen-MoIRana', 90, 1, 'Mosjøen', 'MoIRana'),
('MoIRana-Fauske', 170, 1, 'MoIRana', 'Fauske'),
('Fauske-Bodø', 60, 1, 'Fauske', 'Bodø')
''')
          
#Banestrekning
c.execute('''INSERT OR IGNORE INTO Banestrekning VALUES 
('Nordlandsbanen', 0, 'Trondheim', 'Bodø')
''')

#Operatør      
c.execute('''INSERT OR IGNORE INTO Operatør VALUES
('SJ')
''')
          
#Togrute  
c.execute('''INSERT OR IGNORE INTO Togrute VALUES 
(1, 'True', 'Nordlandsbanen', 'SJ', 'Hverdager', 'Trondheim', 'Bodø'),
(2, 'True', 'Nordlandsbanen', 'SJ', 'Alle dager', 'Trondheim', 'Bodø'),
(3, 'False', 'Nordlandsbanen', 'SJ', 'Hverdager', 'MoIRana' , 'Trondheim')
''')

#TogruteForekomst 
c.execute('''INSERT OR IGNORE INTO TogruteForekomst VALUES 
(1, 'SJ', '0749', '1734'),
(2, 'SJ', '2305', '0905'),
(3, 'SJ', '0811', '1413')
''')

#Kunde Dummydata
c.execute('''INSERT OR IGNORE INTO Kunde VALUES 
(1, 'Erlend', 'erlend@gmail.com', '12345667'),
(2, 'Aaryan', 'aaryan@gmail.com', '12345687'),
(3, 'Joachim', 'joachim@gmail.com', '12345678')
''')

#Kundeordre Dummydata
c.execute('''INSERT OR IGNORE INTO Kundeordre VALUES 
(1, '20230320', '1712', 1),
(2, '20230318', '1832', 2),
(3, '20230319', '1509', 2)
''')

#OrdreForekomst Dummydata
c.execute('''INSERT OR IGNORE INTO OrdreForekomst VALUES 
(1, 2),
(2, 3),
(3, 3)
''')

#Billett Dummydata
c.execute('''INSERT OR IGNORE INTO Billett VALUES 
(1, 1),
(2, 2),
(3, 3)
''')

# #HarTogruteForekomst Denne gir ikke mening
# c.execute('''INSERT OR IGNORE INTO HarTogruteForekomst VALUES 
# (1, 1),
# (2, 2),
# (3, 3)
# ''')

#Vogn (1001 tilsvarer SJ-sittevogn-1) og (2001 tilsvarer SJ-sovevogn-1)
c.execute('''INSERT OR IGNORE INTO Vogn VALUES 
(1001),  
(2001)
''')
          
#HarVogner 
c.execute('''INSERT OR IGNORE INTO HarVogner VALUES 
('SJ', 1001),
('SJ', 2001)
''')
          
#Sittevogn 
c.execute('''INSERT OR IGNORE INTO Sittevogn VALUES 
(1001, 3, 4)
''')
          
#Sovevogn 
c.execute('''INSERT OR IGNORE INTO Sovevogn VALUES 
(2001, 4, 2)
''')

#Plass Dummydata
c.execute('''INSERT OR IGNORE INTO Plass VALUES 
(8, 1),
(9, 2),
(2, 3)
''') 

#Senger Dummydata
c.execute('''INSERT OR IGNORE INTO Senger VALUES 
(1, 2)
''')

#Seter Dummydata
c.execute('''INSERT OR IGNORE INTO Seter VALUES 
(12, 8),
(5, 9)
''')

c.execute("SELECT * FROM Jernbanestasjon")
c.execute("SELECT * FROM Delstrekning")
c.execute("SELECT * FROM Banestrekning")
c.execute("SELECT * FROM Operatør")
rows = c.fetchall()
print(rows)

con.commit()
con.close()

