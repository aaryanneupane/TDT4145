import sqlite3
from datetime import datetime
con = sqlite3.connect("./Database/database.db")
c = con.cursor()


# #Denne funksjonen skal kunne dele rute i delstrekninger
# def delRute(ruteid : str, startStasjon : str, sluttStasjon : str):




#Denne funksjonen skal håndtere billett kjøp
def kjøpBillett(togrute: str, startStasjon: str, sluttStasjon: str, dato: str, vognNr : str, sete : str, epost : str, passord : str):
    c.execute('''SELECT ordrenr FROM kundeordre''')
    kundeOrdre = c.fetchall()
    nyID = len(kundeOrdre) + 1
    dagensTid = datetime.now().strftime('%H.%M')
    dagensDato = datetime.now().strftime('%d.%m.%Y')

    #Hente kundeinfo
    c.execute('''SELECT kundenr FROM kunde WHERE epost = ?  AND passord = ?''', (epost, passord))
    kundeNr = c.fetchone()[0]
    #Lage en kundeOrdre
    c.execute('''
    INSERT INTO kundeordre 
    VALUES (?, ?, ?, ?, ?, ?)''', (nyID, dagensDato, dagensTid, kundeNr, startStasjon, sluttStasjon))
    #Lage nytt billett
    c.execute('''SELECT billettid FROM billett''')
    totaltBilletter = c.fetchall()
    nyttBillettID = len(totaltBilletter) + 1
    c.execute('''
    INSERT INTO billett 
    VALUES (?, ?, ?, ?)''', (nyttBillettID, nyID, vognNr, sete))
    #Gjøre billetten kjøpt utilgjengelig
    c.execute('''
    UPDATE plass
    SET ledig = '1' 
    WHERE vognnr = ? AND plassnr = ?
    ''', (vognNr, sete))
    
    print('\n-------------------------------------------------------------------------------------------------------------------------------------------')
    print('Billett kjøp velykket!')
    print('-------------------------------------------------------------------------------------------------------------------------------------------\n')

    #Comitte til databasen
    con.commit()


    #Update plassen til opptatt


# #Denne funksjonen er ganske lik brukerhistorie d) men hensikten her er å finne hvilken reise kunden har lyst på.
def ledigeBilletter(togrute: str, startStasjon: str, sluttStasjon: str, dato : str, epost : str, passord : str):
    c.execute('''
        SELECT ruteid, vognnr, startstasjon, endestasjon, dato, plassnr, ledig 
        FROM harvogner 
        NATURAL JOIN vogn 
        NATURAL JOIN kjørendetog 
        NATURAL JOIN plass 
        NATURAL JOIN delstrekning 
        WHERE ruteid = ? AND dato = ? AND startstasjon = ? AND endestasjon = ?''', 
        (togrute, dato, startStasjon, sluttStasjon))

    rows = c.fetchall()
    if len(rows) == 0:
        print('----------------------------------------------------------------------------------------------------------------------------------------------\n')
        return print('Det er dessverre ingen ledige billetter.\n\n----------------------------------------------------------------------------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------------------------------------------------------------------------\n')
    
    ledigePlasser = []
    for row in rows: #Mappe ledige plasser vil nå ha en oversikt over ledige plasser i hver vogn
        if row[-1] == 0:
            ledigePlasser.append(['Vogn nr: ' + str(row[1]), 'Sete nr: '+ str(row[-2])])
    print('----------------------------------------------------------------------------------------------------------------------------------------------\n')
    print('Følgende plasser er ledig for reisen fra ' + startStasjon + ' til ' + sluttStasjon + '\n')
    print('----------------------------------------------------------------------------------------------------------------------------------------------\n')
    print(ledigePlasser)
    print('----------------------------------------------------------------------------------------------------------------------------------------------')
    vognNr = input('Velg ønsket vogn: ')
    seteNr = input('Velg ønsket sete: ')
    kjøpBillett(togrute, startStasjon, sluttStasjon, dato, vognNr, seteNr, epost, passord)

    
    

def findBillett(epost : str, passord : str):
    print('----------------------------------------------------------------------------------------------------------------------------------------------\n')
    print('For å finne ledige billetter, må du først velge en togrute.\n')
    print('----------------------------------------------------------------------------------------------------------------------------------------------')
    print('Tast [1] for dagtog fra Trondheim - Bodø')
    print('----------------------------------------------------------------------------------------------------------------------------------------------')
    print('Tast [2] for nattog fra Trondheim - Bodø')
    print('----------------------------------------------------------------------------------------------------------------------------------------------')
    print('Tast [3] for morgentog fra Mo i Rana - Trondheim')
    print('----------------------------------------------------------------------------------------------------------------------------------------------\n')
    togrute = input('Oppgi togruten du vil sjekke: ')
    startStasjon = input('Oppgi stasjonen du vil reise fra: ')
    sluttStasjon = input('Oppgi destinasjonen: ')
    dato = input('Oppgi dato du vil sjekke (dd.mm.yyy): ')
    ledigeBilletter(togrute, startStasjon, sluttStasjon, dato, epost, passord)



kjøpBillett('1', 'Trondheim', 'Fauske', '04.04.2023', '1', '3','aaryan@gmail.com', '1234')