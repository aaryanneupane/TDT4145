import sqlite3
from datetime import datetime, timedelta
con = sqlite3.connect("./Database/database.db")


#Create cursor
c = con.cursor()

#Jernbanestasjon
c.execute('''INSERT OR IGNORE INTO Jernbanestasjon VALUES
('Trondheim', 5.1),
('Steinkjer', 3.6),
('Mosjøen', 6.8),
('Mo i Rana', 3.5),
('Fauske', 34.0),
('Bodø', 4.1)
''')
          
#Delstrekning
c.execute('''INSERT OR IGNORE INTO Delstrekning VALUES 
('Trondheim-Steinkjer1', 1,'Nordlandsbanen', 120, 2, 'Trondheim', 'Steinkjer', '09.51'),
('Trondheim-Steinkjer2', 2, 'Nordlandsbanen', 120, 2, 'Trondheim', 'Steinkjer', '00.57'),
('Trondheim-Mosjøen1', 1,'Nordlandsbanen', 400, 2, 'Trondheim', 'Mosjøen', '13.20'),
('Trondheim-Mosjøen2', 2, 'Nordlandsbanen', 400, 2, 'Trondheim', 'Mosjøen', '04.41'),
('Trondheim-MoIRana1', 1,'Nordlandsbanen', 490, 2, 'Trondheim', 'Mo i Rana', '14.31'),
('Trondheim-MoIRana2', 2, 'Nordlandsbanen', 490, 2, 'Trondheim', 'Mo i Rana', '05.55'),
('Trondheim-Fauske1', 1,'Nordlandsbanen', 660, 2, 'Trondheim', 'Fauske', '16.49'),
('Trondheim-Fauske2', 2, 'Nordlandsbanen', 660, 2, 'Trondheim', 'Fauske', '08.19'),
('Steinkjer-Mosjøen1', 1, 'Nordlandsbanen', 280, 1, 'Steinkjer', 'Mosjøen', '13.20'),
('Steinkjer-Mosjøen2', 2, 'Nordlandsbanen', 280, 1, 'Steinkjer', 'Mosjøen', '04.41'),
('Steinkjer-MoIRana1', 1, 'Nordlandsbanen', 370, 1, 'Steinkjer', 'Mo i Rana', '14.31'),
('Steinkjer-MoIRana2', 2, 'Nordlandsbanen', 370, 1, 'Steinkjer', 'Mo i Rana', '05.55'),
('Steinkjer-Fauske1', 1, 'Nordlandsbanen', 540, 1, 'Steinkjer', 'Fauske', '16.49'),
('Steinkjer-Fauske2', 2, 'Nordlandsbanen', 540, 1, 'Steinkjer', 'Fauske', '08.19'),
('Steinkjer-Bodø1', 1, 'Nordlandsbanen', 600, 1, 'Steinkjer', 'Bodø', '17.34'),
('Steinkjer-Bodø2', 2, 'Nordlandsbanen', 600, 1, 'Steinkjer', 'Bodø', '09.05'),
('Mosjøen-MoIRana1', 1, 'Nordlandsbanen', 90, 1, 'Mosjøen', 'Mo i Rana', '14.31'),
('Mosjøen-MoIRana2', 2, 'Nordlandsbanen', 90, 1, 'Mosjøen', 'Mo i Rana', '05.55'),
('Mosjøen-Fauske1', 1, 'Nordlandsbanen', 260, 1, 'Mosjøen', 'Fauske', '16.49'),
('Mosjøen-Fauske2', 2, 'Nordlandsbanen', 260, 1, 'Mosjøen', 'Fauske', '08.19'),
('Mosjøen-Bodø1', 1, 'Nordlandsbanen', 320, 1, 'Mosjøen', 'Bodø', '17.30'),
('Mosjøen-Bodø2', 2, 'Nordlandsbanen', 320, 1, 'Mosjøen', 'Bodø', '09.05'),
('MoIRana-Fauske1', 1, 'Nordlandsbanen', 170, 1, 'Mo i Rana', 'Fauske', '16.49'),
('MoIRana-Fauske2', 2, 'Nordlandsbanen', 170, 1, 'Mo i Rana', 'Fauske', '08.19'),
('MoIRana-Bodø1', 1, 'Nordlandsbanen', 230, 1, 'Mo i Rana', 'Bodø', '17.34'),
('MoIRana-Bodø2', 2, 'Nordlandsbanen', 230, 1, 'Mo i Rana', 'Bodø', '09.05'),
('Fauske-Bodø1', 1, 'Nordlandsbanen', 60, 1, 'Fauske', 'Bodø', '17.34'),
('Fauske-Bodø2', 2, 'Nordlandsbanen', 60, 1, 'Fauske', 'Bodø', '09.05'),
('MoIRana-Mosjøen1', 3, 'Nordlandsbanen', 90, 1, 'Mo i Rana', 'Mosjøen', '09.14'),
('MoIRana-Steinkjer1', 3, 'Nordlandsbanen', 370, 1, 'Mo i Rana', 'Steinkjer', '12.31'),
('Mosjøen-Steinkjer1', 3, 'Nordlandsbanen', 280, 1, 'Mosjøen', 'Steinkjer', '12.31'),
('Mosjøen-Trondheim1', 3, 'Nordlandsbanen', 400, 1, 'Mosjøen', 'Trondheim', '14.13'),
('Steinkjer-Trondheim1', 3, 'Nordlandsbanen', 120, 1, 'Steinkjer', 'Trondheim', '14.13')
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
(1, 'True', 'Nordlandsbanen', 'SJ', 'Hverdager', 'Trondheim', 'Bodø', '07.49', '17.34'),
(2, 'True', 'Nordlandsbanen', 'SJ', 'Alle dager', 'Trondheim', 'Bodø', '23.05', '09.05'),
(3, 'False', 'Nordlandsbanen', 'SJ', 'Hverdager', 'Mo i Rana' , 'Trondheim', '08.11', '14.13')
''')

#TogruteForekomst 
c.execute('''INSERT OR IGNORE INTO TogruteForekomst VALUES 
(1, 'SJ', '0749', '1734'),
(2, 'SJ', '2305', '0905'),
(3, 'SJ', '0811', '1413')
''')

#Kunde Dummydata
c.execute('''INSERT OR IGNORE INTO Kunde VALUES 
(1, 'Erlend', 'erlend@gmail.com', '12345667', '1234'),
(2, 'Aaryan', 'aaryan@gmail.com', '12345687' , '1234'),
(3, 'Joachim', 'joachim@gmail.com', '12345678', '1234')
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


#Vogn (1001 og 1002 tilsvarer SJ-sittevogn-1) og (2001 tilsvarer SJ-sovevogn-1)
c.execute('''INSERT OR IGNORE INTO Vogn VALUES 
(1001), 
(1002), 
(2001)
''')
          
#HarVogner 
c.execute('''INSERT OR IGNORE INTO HarVogner VALUES 
('SJ', 1, 1001),
('SJ', 1, 1002),
('SJ', 2, 1001),
('SJ', 2, 2001),
('SJ', 3, 1001)
''')
          
#Sittevogn 
c.execute('''INSERT OR IGNORE INTO Sittevogn VALUES 
(1001, 3, 4),
(1002, 3, 4)
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

#KjørendeTog DummyData
c.execute('''INSERT OR IGNORE INTO KjørendeTog VALUES
(1, '03.04.2023'),
(2, '03.04.2023'),
(3, '03.04.2023'),
(1, '04.04.2023'),
(2, '04.04.2023'),
(3, '04.04.2023')
''')
          
#Mellomstasjon
c.execute('''INSERT OR IGNORE INTO AnkommerStasjon VALUES 
(1, 'Steinkjer', '09.51'),
(1, 'Mosjøen', '13.20'),
(1, 'Mo i Rana', '14.31'),
(1, 'Fauske', '16.49'),
(1, 'Trondheim', '07.49'),
(1, 'Bodø', '17.34'),
(2, 'Steinkjer', '00.57'),
(2, 'Mosjøen', '04.41'),
(2, 'Mo i Rana', '05.55'),
(2, 'Fauske', '08.19'),
(2, 'Trondheim', '23.05'),
(2, 'Bodø', '09.05'),
(3, 'Mosjøen', '09.14'),
(3, 'Steinkjer', '12.31'),
(3, 'Mo i Rana', '08.11'),
(3, 'Trondheim', '14.13')
''')

con.commit()
con.close()

