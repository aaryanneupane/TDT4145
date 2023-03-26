
CREATE TABLE IF NOT EXISTS Jernbanestasjon (
	StasjonNavn	VARCHAR(30),
	moh	FLOAT,
	CONSTRAINT JernbaneS_PK PRIMARY KEY (StasjonNavn)
	);


CREATE TABLE IF NOT EXISTS Delstrekning (
	DelSNavn VARCHAR(30),
	RuteID 	INTEGER NOT NULL,
	BaneNavn VARCHAR(30), -- Lagt til BaneNavn
	LengdeIKm INTEGER NOT NULL,
	AntallSpor INTEGER NOT NULL,
	StartStasjon VARCHAR(30),
	EndeStasjon	VARCHAR(30),
	Ankomsttid VARCHAR(30),
	CONSTRAINT DelS_PK PRIMARY KEY (DelSNavn, BaneNavn)
	CONSTRAINT DelS_FK1 FOREIGN KEY (BaneNavn) REFERENCES Banestrekning(BaneNavn)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT DelS_FK2 FOREIGN KEY (RuteID) REFERENCES Togrute(RuteID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
	);

CREATE TABLE IF NOT EXISTS Banestrekning (
	BaneNavn VARCHAR(30),
	Fremdriftsenergi INTEGER, -- 0 for false og 1 for True
	StartStasjon VARCHAR(30),
	EndeStasjon VARCHAR(30),
	CONSTRAINT Bane_PK PRIMARY KEY (BaneNavn)
	);
	

CREATE TABLE IF NOT EXISTS Operatør(
	OperatørNavn VARCHAR(30),
	CONSTRAINT Operatør_PK PRIMARY KEY (OperatørNavn)
);


CREATE TABLE IF NOT EXISTS Togrute(
	RuteID 	INTEGER NOT NULL,
	Hovedretning VARCHAR(30), -- Endret til 'True'/'False' fremfor 1/0
	BaneNavn VARCHAR(30),
	OperatørNavn VARCHAR(30),
	Ukedager VARCHAR(30), --Lagt til Ukedager, viser til når togruten går
	StartStasjon VARCHAR(30), -- Lagt til Startstasjon
	EndeStasjon VARCHAR(30),  -- Lagt til endestasjon
	Avgangstid VARCHAR(30),
	Ankomsttid VARCHAR(30),
	CONSTRAINT Rute_PK PRIMARY KEY (RuteID)
	CONSTRAINT Rute_FK1 FOREIGN KEY (BaneNavn) REFERENCES Banestrekning(BaneNavn)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT Rute_FK2 FOREIGN KEY (OperatørNavn) REFERENCES Operatør(OperatørNavn)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS TogruteForekomst(
	TogruteForekomstID INTEGER NOT NULL,
	OperatørNavn VARCHAR(30),
	Avgangstid 	VARCHAR(30), -- lagt til avgansgstid
	Ankomsttid VARCHAR(30),  -- Lagt til ankomsttid
	CONSTRAINT Forekomst_PK PRIMARY KEY (TogruteForekomstID)
	CONSTRAINT Rute_FK1 FOREIGN KEY (OperatørNavn) REFERENCES Operatør(OperatørNavn)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS Kunde(
	KundeNr	INTEGER NOT NULL,
	Navn VARCHAR(30),
	epost VARCHAR(30),
	tlf	VARCHAR(10),
	passord VARCHAR(30),
	CONSTRAINT Kunde_PK PRIMARY KEY (KundeNr)
);


CREATE TABLE IF NOT EXISTS Kundeordre(
	OrdreNr	INTEGER NOT NULL,
	Dato VARCHAR(30), -- Endret fra integer til varchar blir på format dd.mm.yyy
	Tidspunkt VARCHAR(30), -- Endret fra integer til varchar blir på format tt.mm
	KundeNr	INTEGER NOT NULL,
	fraStasjon VARCHAR(30),
	tilStasjon VARCHAR(30),
	CONSTRAINT KundeO_PK PRIMARY KEY (OrdreNr)
	CONSTRAINT KundeO_FK1 FOREIGN KEY (KundeNr) REFERENCES Kunde(KundeNr)

);


-- Dropper denne relasjonen fullstendig
-- CREATE TABLE IF NOT EXISTS OrdreForekomst(
-- 	OrdreNr	INTEGER NOT NULL,
-- 	TogruteForekomstID INTEGER NOT NULL,
-- 	CONSTRAINT OrdreF_PK PRIMARY KEY (OrdreNr, TogruteForekomstID)
-- 	CONSTRAINT OrdreF_FK1 FOREIGN KEY (OrdreNr) REFERENCES Plass(OrdreNr)
-- 		ON UPDATE CASCADE
-- 		ON DELETE CASCADE,
-- 	CONSTRAINT OrdreF_FK2 FOREIGN KEY (TogruteForekomstID) REFERENCES TogruteForekomst(TogruteForekomstID)
-- 		ON UPDATE CASCADE
-- 		ON DELETE CASCADE
-- );


CREATE TABLE IF NOT EXISTS Billett(
	BillettID INTEGER NOT NULL,
	OrdreNr	INTEGER NOT NULL,
	VognNr INTEGER NOT NULL,
	PlassNr INTEGER NOT NULL,
	CONSTRAINT Billett_PK PRIMARY KEY (BillettID)
	CONSTRAINT Billett_FK1 FOREIGN KEY (OrdreNr) REFERENCES Kundeordre(OrdreNr)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT Billett_FK1 FOREIGN KEY (VognNr) REFERENCES Vogn(VognNr)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT Billett_FK1 FOREIGN KEY (PlassNr) REFERENCES Plass(PlassNr)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

-- Lagt til ny tabell, Må legge til ankomsttid og avgangstid pluss delstrekning
CREATE TABLE IF NOT EXISTS Kjører(
	KjørerID INTEGER NOT NULL,
	RuteID 	INTEGER NOT NULL,
	StasjonNavn	VARCHAR(30),
	Tidspunkt	VARCHAR(30),
	CONSTRAINT Kjører_PK PRIMARY KEY (KjørerID)
	CONSTRAINT Kjører_FK1 FOREIGN KEY (RuteID) REFERENCES Togrute(RuteID)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT Kjører_FK2 FOREIGN KEY (StasjonNavn) REFERENCES Jernbanestasjon(StasjonNavn)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);



CREATE TABLE IF NOT EXISTS Vogn(
	VognNr INTEGER NOT NULL,
	Vogntype VARCHAR(30),
	CONSTRAINT Vogn_PK PRIMARY KEY (VognNr)
);


CREATE TABLE IF NOT EXISTS HarVogner(
	OperatørNavn VARCHAR(30),
	RuteID 	INTEGER NOT NULL,
	VognNr INTEGER NOT NULL,
	CONSTRAINT HarV_PK PRIMARY KEY (OperatørNavn, RuteID, VognNr)
	CONSTRAINT HarV_FK1 FOREIGN KEY (OperatørNavn) REFERENCES Operatør(OperatørNavn)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT HarV_FK2 FOREIGN KEY (VognNr) REFERENCES Vogn(VognNr)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT DelS_FK2 FOREIGN KEY (RuteID) REFERENCES Togrute(RuteID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS Sovevogn(
	VognNr INTEGER NOT NULL,
	AntallKupe INTEGER NOT NULL,
	CONSTRAINT SoveV_PK PRIMARY KEY (VognNr)
	CONSTRAINT SoveV_FK1 FOREIGN KEY (VognNr) REFERENCES Vogn(VognNr)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

-- Lagt til ny tabell Sovekupe
CREATE TABLE IF NOT EXISTS Sovekupe(
	VognNr INTEGER NOT NULL,
	KupeNr INTEGER NOT NULL,
	SengerPerKupe INTEGER NOT NULL, 
	CONSTRAINT SoveKupe_PK PRIMARY KEY (VognNr, KupeNr)
	CONSTRAINT SoveKupe_FK1 FOREIGN KEY (VognNr) REFERENCES Vogn(VognNr)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Sittevogn(
	VognNr INTEGER NOT NULL,
	AntallRader INTEGER,--Lagt til antall rader
	SeterPerRad INTEGER,
	CONSTRAINT SitteV_PK PRIMARY KEY (VognNr)
	CONSTRAINT SitteV_FK1 FOREIGN KEY (VognNr) REFERENCES Vogn(VognNr)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Plass(
	VognNr	INTEGER NOT NULL,
	plassNR INTEGER NOT NULL,
	ledig INTEGER NOT NULL,
	CONSTRAINT Plass_PK PRIMARY KEY (plassNR, VognNr)
	CONSTRAINT Plass_FK1 FOREIGN KEY (VognNr) REFERENCES Vogn(VognNr)
		ON UPDATE CASCADE
		ON DELETE CASCADE	
);


CREATE TABLE IF NOT EXISTS Senger(
	KupeNR INTEGER NOT NULL,
	PlassNr	INTEGER NOT NULL,
	CONSTRAINT Senger_PK PRIMARY KEY (KupeNR, PlassNr)
	CONSTRAINT Senger_FK1 FOREIGN KEY (PlassNr) REFERENCES Plass(PlassNr)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS Seter(
	SeteNR INTEGER NOT NULL,
	PlassNr	INTEGER NOT NULL,
	CONSTRAINT Seter_PK PRIMARY KEY (SeteNR, PlassNr)
	CONSTRAINT Seter_FK1 FOREIGN KEY (PlassNr) REFERENCES Plass(PlassNr)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

-- Lagt til ny tabell AnkommerStasjon
CREATE TABLE IF NOT EXISTS AnkommerStasjon(
	RuteID 	INTEGER NOT NULL,
	StasjonNavn	VARCHAR(30),
	Ankomsttid VARCHAR(30),
	CONSTRAINT Mellomstasjon_PK PRIMARY KEY (RuteID, StasjonNavn)
	CONSTRAINT Mellomstasjon_FK1 FOREIGN KEY (StasjonNavn) REFERENCES Jerbanestasjon(StasjonNavn)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT Mellomstasjon_FK2 FOREIGN KEY (RuteID) REFERENCES Togrute(RuteID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

-- Lagt til ny tabell KjørendeTog
CREATE TABLE IF NOT EXISTS KjørendeTog(
	RuteID INTEGER NOT NULL,
	Dato VARCHAR(30) NOT NULL,
	CONSTRAINT KjørendeTog_PK PRIMARY KEY (RuteID, Dato)
);




	







