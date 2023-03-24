import sqlite3
from datetime import datetime, timedelta
con = sqlite3.connect("./Database/database.db")
c = con.cursor()

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
                print('\nMorgentog fra Mo i Rana til Trondheim ' + row[-3] + ' \n\nAvgang ' + startStasjon + ' kl: '+ row[-2] + ' \n\nAnkomst ' + sluttStasjon + ' kl: '+ row[-1] + '\n')
                print('-------------------------------------------------------------------------------------------------------------------------------------------')
            if (row[0] == 1):
                print('\nDagtog fra Trondheim til Bodø på datoen ' + row[-3] + ' \n\nAvgang ' + startStasjon + ' kl: '+ row[-2] + ' \n\nAnkomst ' + sluttStasjon + ' kl: '+ row[-1] + '\n')
                print('-------------------------------------------------------------------------------------------------------------------------------------------')
            if (row[0] == 2):
                print('\nNattog fra Trondheim til Bodø på datoen ' + row[-3] + ' \n\nAvgang ' + startStasjon + ' kl: '+ row[-2] + ' \n\nAnkomst ' + sluttStasjon + ' kl: '+ row[-1] + '\n')
                print('-------------------------------------------------------------------------------------------------------------------------------------------')
    
    else: #Håndetere delstrekning
        c.execute('''SELECT tr.ruteid, ds.startstasjon, ds.endestasjon, kt.dato, ak.stasjonnavn, ak.ankomsttid, ds.ankomsttid
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
                print('\nMorgentog fra Mo i Rana til Trondheim på datoen ' + row[-4] + ' \n\nAvgang ' + startStasjon + ' kl: '+ row[-2]  + ' \n\nAnkomst ' + sluttStasjon + ' kl: '+ row[-1] + '\n')
                print('-------------------------------------------------------------------------------------------------------------------------------------------')
            if (row[0] == 1):
                print('\nDagtog fra Trondheim til Bodø på datoen ' + row[-4] + ' \n\nAvgang ' + startStasjon + ' kl: '+ row[-2]  + ' \n\nAnkomst ' + sluttStasjon + ' kl: '+ row[-1] + '\n')
                print('-------------------------------------------------------------------------------------------------------------------------------------------')
            if (row[0] == 2):
                print('\nNattog fra Trondheim til Bodø på datoen ' + row[-4] + ' \n\nAvgang ' + startStasjon + ' kl: '+ row[-2] + ' \n\nAnkomst ' + sluttStasjon + ' kl: '+ row[-1] + '\n')
                print('-------------------------------------------------------------------------------------------------------------------------------------------')

