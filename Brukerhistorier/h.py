import sqlite3
con = sqlite3.connect("./Database/database.db")
c = con.cursor()

def mineBilletter(epost : str, passord : str):
    #Hente kundenr
    c.execute('''SELECT kundenr FROM kunde WHERE epost = ? AND passord = ?''', (epost, passord))
    kundeNr = c.fetchone()[0]
    #Hente info om billettkjøp
    c.execute('''SELECT dato, tidspunkt, vognnr, ruteid, kundenr, avgangstid, frastasjon, tilstasjon, plassnr 
    FROM kundeordre
    NATURAL JOIN billett
    NATURAL JOIN harvogner
    NATURAL JOIN togrute
    WHERE kundenr = ? ''', (str(kundeNr)))

    rows = c.fetchall()
    if(len(rows) == 0):
        print('----------------------------------------------------------------------------------------------------------------------------------------------\n')
        return print('Du har ingen bestillinger.\n\n----------------------------------------------------------------------------------------------------------------------------------------------')
    
    print('----------------------------------------------------------------------------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------------------------------------------------------------------------')
    print('\nDu har følgende billetter:\n')
    print('-------------------------------------------------------------------------------------------------------------------------------------------')
    for row in rows:
        print('----------------------------------------------------------------------------------------------------------------------------------------------\n')
        print(str(row[-3]) + ' - ' + str(row[-2]) + '\n\nDato kjøpt: ' + str(row[0]) + '\nTidspunktet ved kjøp: ' + str(row[1]) + '\nSete nr: ' + str(row[-1]) + '\nAvgang fra ' + str(row[-3]) + ' : ' + str(row[-4]) + '\n')
        print('----------------------------------------------------------------------------------------------------------------------------------------------\n')