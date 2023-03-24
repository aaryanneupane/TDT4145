import sqlite3
from datetime import datetime, timedelta
con = sqlite3.connect("database.db")
c = con.cursor()

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

con.commit()
con.close()