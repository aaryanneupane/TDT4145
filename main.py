import sqlite3
con = sqlite3.connect("database.db")

#Create cursor
c = con.cursor()
c.execute("SELECT * FROM sqlite_master")

# #Banestrekning
# c.execute('''CREATE TABLE Banestrekning
# (BaneNavn TEXT, Fremdriftsenergi INTEGER, StartStasjon TEXT,
# EndeStasjon TEXT, DelSNavn TEXT,
# CONSTRAINT Banestreking_PK PRIMARY KEY (BaneNavn),
# CONSTRAINT Banestrekning_FK FOREIGN KEY (DelSNavn)
#         ON UPDATE CASCADE,
#         ON DELETE CASCADE
# )''')

# #Delstrekning
# c.execute('''CREATE TABLE Delstrekning
# (DelSNavn TEXT, LengdeIKm INTEGER, AntallSpor INTEGER NOT NULL,
# StartStasjon TEXT, EndeStasjon TEXT
# CONSTRAINT Delstrekning_PK PRIMARY KEY (DelSNavn)
# )''')

# #Jernbanestasjon
# c.execute('''CREATE TABLE Jernbanestasjon
# (StasjonNavn TEXT, moh INTEGER
# CONSTRAINT Jernbanestasjon_PK PRIMARY KEY (StasjonNavn)
# )''')
          
# #Togrute         
# c.execute('''CREATE TABLE Togrute
# (RuteID INTEGER NOT NULL, Retning INTEGER NOT NULL, BaneNavn TEXT,
# OperatorNavn TEXT
# )''')
          
# #TogruteForekomst          
# c.execute('''CREATE TABLE TogruteForekomst
# (TogruteForekomstID INTEGER NOT NULL, OperatorNavn TEXT
# CONSTRAINT TogruteForekomst_PK PRIMARY KEY (TogruteForekomstID)
# )''')
          


#Fecthall



c.execute("SELECT * FROM Jernbanestasjon")
rows = c.fetchall()
print("All rows in the table Jernbasestasjon:")
print(rows)
con.commit()
con.close()
