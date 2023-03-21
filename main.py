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
          
#Togrute  
c.execute('''INSERT INTO Togrute VALUES 
(1, 'True', 'Nordlandsbanen', 'SJ', 'Trondheim', 'Bodø'),
(2, 'True', 'Nordlandsbanen', 'SJ', 'Trondheim', 'Bodø'),
(3, 'False', 'Nordlandsbanen', 'SJ', 'MoIRana' , 'Trondheim')
''')

#TogruteForekomst 
c.execute('''INSERT INTO TogruteForekomst VALUES 
(1, 'SJ', '0749', '1734'),
(2, 'SJ', '2305', '0905'),
(3, 'SJ', '0811', '1413')
''')

#HarDelstrekning DENNE ingen ekstra data
c.execute('''INSERT INTO HarDelstrekning VALUES 
(1, 'SJ'),
(2, 'SJ'),
(3, 'SJ')
''')

#Kunde Dummydata
c.execute('''INSERT INTO Kunde VALUES 
(1, 'Erlend', 'erlend@gmail.com', '12345667'),
(2, 'Aaryan', 'aaryan@gmail.com', '12345687'),
(3, 'Joachim', 'joachim@gmail.com', '12345678')
''')

#Kundeordre Dummydata
c.execute('''INSERT INTO Kundeordre VALUES 
(1, '20230320', '1712', 1),
(2, '20230318', '1832', 2),
(3, '20230319', '1509', 2)
''')

#OrdreForekomst Dummydata
c.execute('''INSERT INTO OrdreForekomst VALUES 
(1, 2),
(2, 3),
(3, 3)
''')

#Billett Dummydata
c.execute('''INSERT INTO Billett VALUES 
(1, 1),
(2, 2),
(3, 3)
''')

# #HarTogruteForekomst Denne gir ikke mening
# c.execute('''INSERT INTO HarTogruteForekomst VALUES 
# (1, 1),
# (2, 2),
# (3, 3)
# ''')

#Vogn Dummydata
c.execute('''INSERT INTO Vogn VALUES 
(1002),
(1003),
(1005),
(1009)
''')
          
#HarVogner Dummydata
c.execute('''INSERT INTO HarVogner VALUES 
('SJ', 1002),
('SJ', 1003),
('SJ', 1005),
('SJ', 1009)
''')
          
#Sovevogn Dummydata
c.execute('''INSERT INTO Sovevogn VALUES 
(1002, 4),
(1005, 2)
''')

#Sittevogn Dummydata
c.execute('''INSERT INTO Sittevogn VALUES 
(1003, 12),
(1009, 10)
''')

#Plass Dummydata
c.execute('''INSERT INTO Plass VALUES 
(8, 1),
(9, 2),
(2, 3)
''') 

#Senger Dummydata
c.execute('''INSERT INTO Senger VALUES 
(3, 2)
''')

#Seter Dummydata
c.execute('''INSERT INTO Seter VALUES 
(12, 8),
(5, 9)
''')

c.execute("SELECT * FROM Jerbanestasjon")
c.execute("SELECT * FROM Delstrekning")
c.execute("SELECT * FROM Banestrekning")
c.execute("SELECT * FROM Operatør")
rows = c.fetchall()
print(rows)

con.commit()
con.close()

