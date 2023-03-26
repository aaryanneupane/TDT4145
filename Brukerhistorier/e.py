import sqlite3
con = sqlite3.connect("./Database/database.db")
c = con.cursor()

def addKunde():

#Hente informasjon from kunden
    epost = input('Oppgi gyldig epost adresse: ')
    passord = input('Oppgi passord: ')
    bekreftPassord = input('Bekreft passord: ')

#Passord verifikasjon
    while (bekreftPassord != passord):
        bekreftPassord = input('''(Tast 1 om du vil skrive passord på nytt)\nPassordene samsvarer ikke, vennligst tast inn samme passord: ''')
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
    
#Commit til databasen før funksjon slutt
    con.commit()
    return [navn, epost, passord]


def login():
    epost = input('Oppgi brukerens epost adresse: ')
    passord = input('Oppgi brukerens passord: ')
    notExist = 'Nope'
    
    c.execute('''SELECT epost, passord, navn from Kunde WHERE epost = ? AND passord = ?''', (epost,passord))
    rows = c.fetchall()


    if (len(rows) == 0):
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------\n')
        print('Denne brukeren finnes ikke.')
        return notExist
    
    return rows[0][-1]