import sqlite3
from Brukerhistorier.d import searchTogrute
from Brukerhistorier.c import getTogruter
from Brukerhistorier.e import addKunde, login
con = sqlite3.connect("./Database/database.db")

#Innlogget meny
def menu(name : str):
    navn = name
    print('\nVelkommen, ' + name + '!\n')
    print('-------------------------------------------------------------------------------------------------------------------------------------------')
    print('Tast [1] for å få ut alle togruter som er innom en stasjon en gitt ukedag')
    print('-------------------------------------------------------------------------------------------------------------------------------------------')
    print('Tast [2] for søke etter togruter med dato og tid')
    print('-------------------------------------------------------------------------------------------------------------------------------------------')
    print('Tast [3] å søke etter ledige billetter for en oppgitt strekning')
    print('-------------------------------------------------------------------------------------------------------------------------------------------')
    print('Tast [0] for å \u0332a\u0332v\u0332s\u0332l\u0332u\u0332t\u0332t\u0332e\u0332') #Underline avslutte
    print('-------------------------------------------------------------------------------------------------------------------------------------------\n')
    
    svar = input('Velg et av alternativene: ')
    while(svar not in ['0','1', '2', '3',]):
        svar = input('Du må velge et av alternativene overfor: ')

    if(svar == '0'):
            return
    if(svar == '1'):
        getTogruter()
        menu(navn)
    if(svar == '2'):
        searchTogrute()
        menu(navn)
    if(svar == '3'):
        print('Må lage denne')
        menu(navn)
   
#Default main
def main():
    print('\n-------------------------------------------------------------------------------------------------------------------------------------------\n')
    print('Velkommen til Vy\n')
    print('-------------------------------------------------------------------------------------------------------------------------------------------')
    print('Tast [1] for å ny lage bruker')
    print('-------------------------------------------------------------------------------------------------------------------------------------------')
    print('Tast [2] for å logge inn med en eksisterende bruker')
    print('-------------------------------------------------------------------------------------------------------------------------------------------')
    print('Tast [3] for å få ut alle togruter som er innom en stasjon en gitt ukedag')
    print('-------------------------------------------------------------------------------------------------------------------------------------------')
    print('Tast [4] for søke etter togruter med dato og tid')
    print('-------------------------------------------------------------------------------------------------------------------------------------------')
    print('Tast [5] å søke etter ledige billetter for en oppgitt strekning')
    print('-------------------------------------------------------------------------------------------------------------------------------------------')
    print('Tast [0] for å \u0332a\u0332v\u0332s\u0332l\u0332u\u0332t\u0332t\u0332e\u0332') #Underline avslutte
    print('-------------------------------------------------------------------------------------------------------------------------------------------\n')
    svar = input('Velg et av alternativene: ')
    while(svar not in ['0','1', '2', '3', '4', '5']):
        svar = input('Du må velge et av alternativene overfor: ')
    if(svar == '0'):
            return
    if(svar == '1'):
        name = addKunde()
        menu(name)
    if(svar == '2'):
        name = login()
        if (name == 'Nope'):
            main()
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------')
        print('Innlogging vellykket')
        print('-------------------------------------------------------------------------------------------------------------------------------------------\n')
        menu(name)   
    if(svar == '3'):
        getTogruter()
        main()
    if(svar == '4'):
        searchTogrute()
        main()
    if(svar == '5'):
        print('-------------------------------------------------------------------------------------------------------------------------------------------\n')
        print('Du må være en innlogget bruker for å søke etter ledige billetter!')
        main()

con.close()