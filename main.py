import sqlite3
from datetime import datetime, timedelta
con = sqlite3.connect("database.db")


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
('Trondheim-Steinkjer1', 1,'Nordlandsbanen', 120, 2, 'Trondheim', 'Steinkjer'),
('Trondheim-Steinkjer2', 2, 'Nordlandsbanen', 120, 2, 'Trondheim', 'Steinkjer'),
('Trondheim-Mosjøen1', 1,'Nordlandsbanen', 400, 2, 'Trondheim', 'Mosjøen'),
('Trondheim-Mosjøen2', 2, 'Nordlandsbanen', 400, 2, 'Trondheim', 'Mosjøen'),
('Trondheim-MoIRana1', 1,'Nordlandsbanen', 490, 2, 'Trondheim', 'Mo i Rana'),
('Trondheim-MoIRana2', 2, 'Nordlandsbanen', 490, 2, 'Trondheim', 'Mo i Rana'),
('Trondheim-Fauske1', 1,'Nordlandsbanen', 660, 2, 'Trondheim', 'Fauske'),
('Trondheim-Fauske2', 2, 'Nordlandsbanen', 660, 2, 'Trondheim', 'Fauske'),
('Steinkjer-Mosjøen1', 1, 'Nordlandsbanen', 280, 1, 'Steinkjer', 'Mosjøen'),
('Steinkjer-Mosjøen2', 2, 'Nordlandsbanen', 280, 1, 'Steinkjer', 'Mosjøen'),
('Steinkjer-MoIRana1', 1, 'Nordlandsbanen', 370, 1, 'Steinkjer', 'Mo i Rana'),
('Steinkjer-MoIRana2', 2, 'Nordlandsbanen', 370, 1, 'Steinkjer', 'Mo i Rana'),
('Steinkjer-Fauske1', 1, 'Nordlandsbanen', 540, 1, 'Steinkjer', 'Fauske'),
('Steinkjer-Fauske2', 2, 'Nordlandsbanen', 540, 1, 'Steinkjer', 'Fauske'),
('Steinkjer-Bodø1', 1, 'Nordlandsbanen', 600, 1, 'Steinkjer', 'Bodø'),
('Steinkjer-Bodø2', 2, 'Nordlandsbanen', 600, 1, 'Steinkjer', 'Bodø'),
('Mosjøen-MoIRana1', 1, 'Nordlandsbanen', 90, 1, 'Mosjøen', 'Mo i Rana'),
('Mosjøen-MoIRana2', 2, 'Nordlandsbanen', 90, 1, 'Mosjøen', 'Mo i Rana'),
('Mosjøen-Fauske1', 1, 'Nordlandsbanen', 260, 1, 'Mosjøen', 'Fauske'),
('Mosjøen-Fauske2', 2, 'Nordlandsbanen', 260, 1, 'Mosjøen', 'Fauske'),
('Mosjøen-Bodø1', 1, 'Nordlandsbanen', 320, 1, 'Mosjøen', 'Bodø'),
('Mosjøen-Bodø2', 2, 'Nordlandsbanen', 320, 1, 'Mosjøen', 'Bodø'),
('MoIRana-Fauske1', 1, 'Nordlandsbanen', 170, 1, 'Mo i Rana', 'Fauske'),
('MoIRana-Fauske2', 2, 'Nordlandsbanen', 170, 1, 'Mo i Rana', 'Fauske'),
('MoIRana-Bodø1', 1, 'Nordlandsbanen', 230, 1, 'Mo i Rana', 'Bodø'),
('MoIRana-Bodø2', 2, 'Nordlandsbanen', 230, 1, 'Mo i Rana', 'Bodø'),
('Fauske-Bodø1', 1, 'Nordlandsbanen', 60, 1, 'Fauske', 'Bodø'),
('Fauske-Bodø2', 2, 'Nordlandsbanen', 60, 1, 'Fauske', 'Bodø'),
('MoIRana-Mosjøen1', 3, 'Nordlandsbanen', 90, 1, 'Mo i Rana', 'Mosjøen'),
('MoIRana-Steinkjer1', 3, 'Nordlandsbanen', 370, 1, 'Mo i Rana', 'Steinkjer'),
('Mosjøen-Steinkjer1', 3, 'Nordlandsbanen', 280, 1, 'Mosjøen', 'Steinkjer'),
('Mosjøen-Trondheim1', 3, 'Nordlandsbanen', 400, 1, 'Mosjøen', 'Trondheim'),
('Steinkjer-Trondheim1', 3, 'Nordlandsbanen', 120, 1, 'Steinkjer', 'Trondheim')
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
(1, 'MoIRana', '14.31'),
(1, 'Fauske', '16.49'),
(1, 'Trondheim', '07.49'),
(1, 'Bodø', '17.34'),
(2, 'Steinkjer', '00.57'),
(2, 'Mosjøen', '04.41'),
(2, 'MoIRana', '05.55'),
(2, 'Fauske', '08.19'),
(2, 'Trondheim', '23.05'),
(2, 'Bodø', '09.05'),
(3, 'Mosjøen', '09.14'),
(3, 'Steinkjer', '12.31'),
(3, 'Mo i Rana', '08.11'),
(3, 'Trondheim', '14.13')
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

# getTogruter('Mosjøen', 'Lørdag')


def addKunde():
#Hente informasjon from kunden
    epost = input('Oppgi gyldig epost adresse: ')
    passord = input('Oppgi passord: ')
    bekreftPassord = input('Bekreft passord: ')
#Passord verifikasjon
    while (bekreftPassord != passord):
        bekreftPassord = input('''(Tast 1 om du vil skrive passord på nytt) Passordene samsvarer ikke, vennligst tast inn samme passord: ''')
        if (bekreftPassord == '1'):
            passord = input('Oppgi nytt passord: ')
            bekreftPassord = input('Bekreft passord: ')
    navn = input('Vennligst oppgi fullt navn: ')
    tlf = input('Oppgi gyldig telefon nummer: ')
#Finne unik primærnøkkel for ny kunde
    c.execute('''SELECT KundeNr FROM Kunde''')
    rows = c.fetchall()
    nyID = len(rows) + 1
#Legge til i databasen
    c.execute('''INSERT INTO Kunde (KundeNr, Navn, epost, tlf, passord)
    VALUES (?, ?, ?, ?, ?)''', (nyID, navn, epost, tlf, passord))


def searchTogrute():
    startStasjon = input('Oppgi en startstasjon: ')
    sluttStasjon = input('Oppgi en endestasjon: ')
    dato = input('Oppgi en gyldig dato i format dd.mm.yyyy: ')
    dato_obj = datetime.strptime(dato, '%d.%m.%Y') # convert string to datetime object
    nesteDato_obj = dato_obj + timedelta(days=1) # add one day to the datetime object
    nesteDato = nesteDato_obj.strftime('%d.%m.%Y') # convert datetime object to string in required format
    tid = input('Oppgi et gyldig tidspunkt i format tt.mm (09.40): ')
    tid_mins = int(tid[:2]) * 60 + int(tid[3:])

    c.execute('''SELECT tr.ruteid, tr.startstasjon, tr.endestasjon, kt.dato ,tr.avgangstid, tr.ankomsttid 
    From togrute as tr INNER JOIN KjørendeTog as kt using (ruteID)
    WHERE tr.startstasjon = ? AND tr.endestasjon = ? AND (kt.dato = ? OR kt.dato = ?)''', (startStasjon, sluttStasjon, dato, nesteDato))
    bane = c.fetchall()
    #Håndtere en banestrekning
    if (len(bane) > 0):
        print('----------------------------------------------------------------------------------------------------------------------------------------------')
        print('\nSortert etter nærmest kl. ' + tid + ' går det følgende togruter for de oppgitte datoene.\n')
        bane_sorted = sorted(bane, key=lambda x: abs(int(x[-2][:2]) * 60 + int(x[-2][3:]) - tid_mins))
        for row in bane_sorted:
            print('-------------------------------------------------------------------------------------------------------------------------------------------')
            if (row[0] == 3):
                print('\nMorgentog fra Mo i Rana til Trondheim på datoen ' + row[-3] + ' \n\nAvgang ' + startStasjon + ' kl: '+ row[-2] + ' \n\nAnkomst ' + sluttStasjon + ' kl: '+ row[-1] + '\n')
                print('-------------------------------------------------------------------------------------------------------------------------------------------')
            if (row[0] == 1):
                print('\nDagtog fra Trondheim til Bodø på datoen ' + row[-3] + ' \n\nAvgang ' + startStasjon + ' kl: '+ row[-2] + ' \n\nAnkomst ' + sluttStasjon + ' kl: '+ row[-1] + '\n')
                print('-------------------------------------------------------------------------------------------------------------------------------------------')
            if (row[0] == 2):
                print('\nNattog fra Trondheim til Bodø på datoen ' + row[-3] + ' \n\nAvgang ' + startStasjon + ' kl: '+ row[-2] + ' \n\nAnkomst ' + sluttStasjon + ' kl: '+ row[-1] + '\n')
                print('-------------------------------------------------------------------------------------------------------------------------------------------')
    else: #Håndetere delstrekning
        c.execute('''SELECT tr.ruteid, ds.startstasjon, ds.endestasjon, kt.dato, ak.stasjonnavn, ak.ankomsttid
        FROM ((((togrute as tr INNER JOIN delstrekning as ds USING (ruteID)) INNER JOIN kjørendetog as kt USING (ruteID)) INNER JOIN ankommerstasjon as ak USING (ruteID))) 
        WHERE (((ds.startstasjon = ?) AND (ds.endestasjon = ?)) AND ak.stasjonnavn = ?  AND (kt.dato = ? OR kt.dato = ?))''', (startStasjon, sluttStasjon, startStasjon, dato, nesteDato,))
        
        rows = c.fetchall()

        if (len(rows) == 0):
            return print('Det går dessverre ingen tog fra ' + startStasjon + ' til ' + sluttStasjon + ' den oppgitte datoen.')
        
        print('----------------------------------------------------------------------------------------------------------------------------------------------')
        print('\nSortert etter nærmest kl. ' + tid + ' går det følgende togruter for de oppgitte datoene.\n')

        rows_sorted = sorted(rows, key=lambda x: abs(int(x[-1][:2]) * 60 + int(x[-1][3:]) - tid_mins))
        for row in rows_sorted:
            print('----------------------------------------------------------------------------------------------------------------------------------------------')
            if (row[0] == 3):
                print('\nMorgentog fra Mo i Rana til Trondheim på datoen ' + row[-3] + ' \n\nAvgang ' + startStasjon + ' kl: '+ row[-1]  + ' \n\nAnkomst ' + sluttStasjon + ' kl: '+ row[-1] + '\n')
                print('-------------------------------------------------------------------------------------------------------------------------------------------')
            if (row[0] == 1):
                print('\nDagtog fra Trondheim til Bodø på datoen ' + row[-3] + ' \n\nAvgang ' + startStasjon + ' kl: '+ row[-1]  + ' \n\nAnkomst ' + sluttStasjon + ' kl: '+ row[-1] + '\n')
                print('-------------------------------------------------------------------------------------------------------------------------------------------')
            if (row[0] == 2):
                print('\nNattog fra Trondheim til Bodø på datoen ' + row[-3] + ' \n\nAvgang ' + startStasjon + ' kl: '+ row[-1] + ' \n\nAnkomst ' + sluttStasjon + ' kl: '+ row[-1] + '\n')
                print('-------------------------------------------------------------------------------------------------------------------------------------------')

searchTogrute()



con.commit()
con.close()

