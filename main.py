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
          
#Mellomstasjon
c.execute('''INSERT OR IGNORE INTO Mellomstasjon VALUES 
(1, 'Steinkjer', '0951', '0956'),
(1, 'Mosjøen', '1320', '1325'),
(1, 'MoIRana', '1431', '1436'),
(1, 'Fauske', '1649', '1654'),
(2, 'Steinkjer', '0057', '0102'),
(2, 'Mosjøen', '0441', '0446'),
(2, 'MoIRana', '0555', '0600'),
(2, 'Fauske', '0819', '0824'),
(3, 'Mosjøen', '0914', '0919'),
(3, 'Steinkjer', '1231', '1236')
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


getTogruter('Mosjøen', 'Lørdag')


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


# Lager en funksjon for å finne tilgjengelige billetter
def ledige_billetter(RuteID, dato):
    c = con.cursor()
    query = "SELECT * FROM Billett WHERE RuteID = ? AND dato = ? AND is_reserved = 0"
    # is_reserved = 0 betyr at billetten ikke er reservert ennå
    params = (RuteID, dato)
    c.execute(query, params)
    result = c.fetchall()
    return result

# Lag en funksjon for å reservere en billett
def reserve_ticket(BillettID, Navn):
    c = con.cursor()
    query = "UPDATE tickets SET is_reserved = 1, Navn = ? WHERE BillettID = ?"
    # is_reserved = 1 betyr at billetten er reservert
    params = (Navn, BillettID)
    c.execute(query, params)
    con.commit()

# Eksempel på hvordan du kan bruke funksjonene
train_route = "Oslo - Bergen"
journey_date = "2023-04-15"
available_tickets = ledige_billetter(train_route, journey_date)
if len(available_tickets) > 0:
    # La kunden velge en billett fra listen over tilgjengelige billetter
    ticket_id = available_tickets[0][0]
    customer_name = "Ola Nordmann"
    reserve_ticket(ticket_id, customer_name)
    print("Billetten er reservert!")
else:
    print("Ingen billetter er tilgjengelige for denne ruten og datoen.")


con.commit()
con.close()

