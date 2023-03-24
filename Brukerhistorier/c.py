import sqlite3
con = sqlite3.connect("./Database/database.db")
c = con.cursor()

def getTogruter():
    hverdager = ['mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag']
    helg = ['lørdag', 'søndag']

    stasjon = input('Oppgi en stasjon: ')
    ukedag = input('Oppgi ukedagen du vil sjekke: ')

    #Ukedager
    if((ukedag.lower() in hverdager)):
        c.execute('''SELECT tr.ruteID, tr.ukedager, tr.startstasjon, tr.endestasjon, 
        ak.stasjonnavn ,ak.ankomsttid FROM togrute AS tr  INNER JOIN ankommerstasjon AS ak USING (ruteid)
        WHERE ak.stasjonnavn = ? AND (tr.ukedager = 'Hverdager' OR tr.ukedager = 'Alle dager') ''', (stasjon,))

        rows = c.fetchall()
        print('-------------------------------------------------------------------------------------------------------------------------------------------')
        for row in rows:
            if (row[0] == 3):
                print('\nMorgentog fra Mo i Rana til Trondheim. \n\nAnkommer ' + stasjon + ' kl: '+ row[-1] + ' på ' + ukedag + '.\n')
                print('-------------------------------------------------------------------------------------------------------------------------------------------')
            if (row[0] == 1):
                print('\nDagtog fra Trondheim til Bodø  \n\nAnkommer ' + stasjon + ' kl: '+ row[-1] + ' på ' + ukedag + '.\n')
                print('-------------------------------------------------------------------------------------------------------------------------------------------')
            if (row[0] == 2):
                print('\nNattog fra Trondheim til Bodø  \n\nAnkommer ' + stasjon + ' kl: '+ row[-1] + ' på ' + ukedag + '.\n')
                print('-------------------------------------------------------------------------------------------------------------------------------------------')
           
    #Helger
    if ((ukedag.lower() in helg)):
            c.execute('''SELECT tr.ruteID, tr.ukedager, tr.startstasjon, tr.endestasjon, 
            ak.stasjonnavn ,ak.ankomsttid 
            FROM togrute AS tr INNER JOIN ankommerstasjon AS ak USING (ruteid)
            WHERE ak.stasjonnavn = ? AND tr.ukedager = 'Alle dager' ''', (stasjon,))

            rows = c.fetchall()
            print('-------------------------------------------------------------------------------------------------------------------------------------------')
            for row in rows:
                if (row[0] == 2):
                    print('\nNattog fra Trondheim til Bodø  \n\nAnkommer ' + stasjon + ' kl: '+ row[-1] + ' på ' + ukedag + '.\n')
                    print('-------------------------------------------------------------------------------------------------------------------------------------------')

