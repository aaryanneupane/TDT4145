import sqlite3
from datetime import datetime, timedelta
con = sqlite3.connect("./Database/database.db")
c = con.cursor()

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

con.commit()
con.close()