import sqlite3
from datetime import datetime
con = sqlite3.connect("./Database/database.db")
c = con.cursor()


#Denne funksjonen skal kunne dele rute i delstrekninger
def delRute(ruteid : str, startStasjon : str, sluttStasjon : str):

    ruteEnde = {1: 'Bodø', 2: 'Bodø', 3: 'Trondheim'}
    ruteStart = {1: 'Trondheim', 2: 'Trondheim', 3: 'Mo i Rana'}

    stasjoner = ['Trondheim', 'Steinkjer', 'Mosjøen', 'Mo i Rana', 'Fauske', 'Bodø']
    stasjoner3 = ['Mo i Rana', 'Steinkjer', 'Mosjøen', 'Trondheim']

    c.execute('''SELECT ds.ruteid, ds.startstasjon, ds.endestasjon, ak.stasjonnavn, tr.endestasjon  
    FROM delstrekning AS ds
    INNER JOIN ankommerstasjon AS ak using (ruteid) 
    INNER JOIN togrute AS tr
    WHERE ds.ruteid = ? AND ds.startstasjon = ? AND ds.endestasjon = ? AND NOT tr.endestasjon = ? AND NOT ak.stasjonnavn = ? AND NOT ak.stasjonnavn = ? AND NOT ak.stasjonnavn = ? AND NOT ak.stasjonnavn = ?''', (ruteid, startStasjon, sluttStasjon, ruteEnde[int(ruteid)], startStasjon, sluttStasjon, ruteEnde[int(ruteid)], ruteStart[int(ruteid)]))
    # c.execute('''SELECT )
    rows = c.fetchall()
    print(rows)
    mellomStasjoner = set()

    for row in rows:
        mellomStasjoner.add(row[-2])
    return mellomStasjoner



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

    # mellomstasjoner = delRute(togrute, startStasjon, sluttStasjon)
    # if (len(mellomstasjoner) == 0): 
    #HOLDT PÅ Å LAGE DENNE FOR FUNKSJON MEN RAKK DET IKKE

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
    
    print('\n-------------------------------------------------------------------------------------------------------------------------------------------')
    print('Billett kjøp velykket!')
    print('-------------------------------------------------------------------------------------------------------------------------------------------\n')

    #Comitte til databasen
    con.commit()


    #Update plassen til opptatt


# #Denne funksjonen er ganske lik brukerhistorie d) men hensikten her er å finne hvilken reise kunden har lyst på.
def ledigeBilletter(togrute: str, startStasjon: str, sluttStasjon: str, dato : str, epost : str, passord : str):
    c.execute('''
        SELECT ruteid, vognnr, startstasjon, endestasjon, dato, plassnr
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
    
    vognTilRute = []
    if(togrute == '1'):
        vognTilRute = ['1', '2']
    if(togrute == '2'):
        vognTilRute = ['3', '4']
    if(togrute == '3'):
        vognTilRute = ['5']
    
    for row in vognTilRute:
        print('Du kan velge mellom følgende vogn: ' +  row)
    
    print('----------------------------------------------------------------------------------------------------------------------------------------------\n')
    
    vognNr = input('Velg ønsket vogn: ')

    c.execute('''SELECT ruteid, frastasjon, tilstasjon, kjørendetog.dato, plassnr, vognnr
    FROM billett
    NATURAL JOIN kundeordre
    NATURAL JOIN harvogner
    INNER JOIN kjørendetog USING (ruteid)
    WHERE frastasjon = ? AND tilstasjon = ? AND kjørendetog.dato = ? AND vognnr = ? ''', (startStasjon, sluttStasjon, dato, vognNr))

    billeter = c.fetchall()

    ledigePlasser = []

    for row in rows:
        for billett in billeter:
            if (row[-1] != billett[-2]):
                ledigePlasser.append(['Sete nr: '+ str(row[-1])])

    print('----------------------------------------------------------------------------------------------------------------------------------------------\n')
    print('Følgende plasser er ledig for reisen fra ' + startStasjon + ' til ' + sluttStasjon + '\n')
    print('----------------------------------------------------------------------------------------------------------------------------------------------\n')
    print(ledigePlasser)
    print('----------------------------------------------------------------------------------------------------------------------------------------------')
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


