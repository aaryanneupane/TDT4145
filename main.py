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
('Trondheim-Steinkjer1', 1,'Nordlandsbanen', 120, 2, 'Trondheim', 'Steinkjer'),
('Trondheim-Steinkjer2', 2, 'Nordlandsbanen', 120, 2, 'Trondheim', 'Steinkjer'),
('Trondheim-Steinkjer3', 3, 'Nordlandsbanen', 120, 2, 'Trondheim', 'Steinkjer'),
('Steinkjer-Mosjøen1', 1, 'Nordlandsbanen', 280, 1, 'Steinkjer', 'Mosjøen'),
('Steinkjer-Mosjøen2', 2, 'Nordlandsbanen', 280, 1, 'Steinkjer', 'Mosjøen'),
('Steinkjer-Mosjøen3', 3, 'Nordlandsbanen', 280, 1, 'Steinkjer', 'Mosjøen'),
('Mosjøen-MoIRana1', 1, 'Nordlandsbanen', 90, 1, 'Mosjøen', 'MoIRana'),
('Mosjøen-MoIRana2', 2, 'Nordlandsbanen', 90, 1, 'Mosjøen', 'MoIRana'),
('Mosjøen-MoIRana3', 3, 'Nordlandsbanen', 90, 1, 'Mosjøen', 'MoIRana'),
('MoIRana-Fauske1', 1, 'Nordlandsbanen', 170, 1, 'MoIRana', 'Fauske'),
('MoIRana-Fauske2', 2, 'Nordlandsbanen', 170, 1, 'MoIRana', 'Fauske'),
('Fauske-Bodø1', 1, 'Nordlandsbanen', 60, 1, 'Fauske', 'Bodø'),
('Fauske-Bodø2', 2, 'Nordlandsbanen', 60, 1, 'Fauske', 'Bodø')
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
(2, 'True', 'Nordlandsbanen', 'SJ', 'alleDager', 'Trondheim', 'Bodø'),
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

def getTogruter(stasjon : str, ukedag : str):

    hverdager = ['mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag']
    alledager = ['mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag','lørdag', 'søndag']

    togruteID = set()

    if((ukedag.lower() in hverdager) and ukedag.lower() in alledager):
        
        c.execute('''SELECT tr.RuteID, tr.StartStasjon, tr.EndeStasjon, tr.Ukedager, ds.StartStasjon, ds.EndeStasjon 
        FROM Togrute as tr 
        INNER JOIN Delstrekning as ds 
        ON ds.RuteID = tr.RuteID 
        WHERE Ukedager = 'Hverdager' 
        AND (tr.StartStasjon = ? OR tr.EndeStasjon = ? or ds.StartStasjon = ?  OR ds.EndeStasjon = ?)''', (stasjon,stasjon,stasjon,stasjon,))
        
        rows = c.fetchall()
        
        for row in rows:
            togruteID.add(row[0])

    elif (ukedag.lower() in alledager):
        c.execute('''SELECT tr.RuteID, tr.StartStasjon, tr.EndeStasjon, tr.Ukedager, ds.StartStasjon, ds.EndeStasjon 
        FROM Togrute as tr 
        INNER JOIN Delstrekning as ds 
        ON ds.RuteID = tr.RuteID 
        WHERE Ukedager = 'AlleDager' 
        AND (tr.StartStasjon = ? OR tr.EndeStasjon = ? or ds.StartStasjon = ?  OR ds.EndeStasjon = ?)''', (stasjon,stasjon,stasjon,stasjon,))
        rows = c.fetchall()
        for row in rows:
            togruteID.add(row[0])

    output = ''

    if (len(togruteID) == 0):
            output += "Ingen togruter som passer til krav."
    for togrute in togruteID:
        if (togrute == 1):
            output += "Trondheim-Bodø, Dagtog"
        if (togrute == 2):
            output += "\nTrondheim-Bodø, Nattog"
        if (togrute == 3):
            output += "\nMo i Rana-Trondheim, Dagtog"

    print(output)


getTogruter('Mosjøen', 'Fredag')





# c.execute("SELECT * FROM Jernbanestasjon")
# c.execute("SELECT * FROM Delstrekning")
# c.execute("SELECT * FROM Banestrekning")
# c.execute("SELECT * FROM Operatør")
# rows = c.fetchall()
# print(rows)

con.commit()
con.close()

