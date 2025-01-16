#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:10:46 2025

@author: tt

Har brukt AI for å forstå hvordan menysystem for valg av funksjoner kan kodes.
Har brukt AI for å forstå de betingede programløpene.
Har brukt AI for å forstå f string print.
Har brukt AI for å forstå hvordan man kan legge inn nye data i dictionary. 
Har brukt AI for å få eksempler på konfigurasjon av plot.

Valgte å kode alle oppgavene i samme program da det bare er mulig å linke til en fil for innlevering 
(Mangler muligens noe kunksap om GitHub).
"""

import math
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

#Oppgave 1: Sjekker alderen din ut fra fødeår og nåværende år
def oppgave_1():
    while True:
        try:
            print ("Oppgave 1")
            print ("--> Hvilket år er du født?")
            #input
            fødeår = int(input("--> "))                                         #Input fødeår
            årstall = int(datetime.now().strftime('%Y'))                        #Inneværende år
            alder = (årstall - fødeår)                                          #Utregning av alder
            #Output
            print ("--> Du er eller blir",(alder),"år gammel i år!")            #Skriver variabel alder
            break
        except ValueError:
            print("Ugyldig tall!")

#Oppgave 2: Regner ut antall pizza til festen
def oppgave_2():
    while True:
        try:
            print ("oppgave 2")
            print ("--> Skriv inn antall elever")
            #input
            antall_elever = int(input("--> "))                                  #Input antall elever
            ant_pizza = math.ceil(antall_elever * 0.25)                         #Utregning antall pizza rundet opp
            #output
            print ("-->",ant_pizza,"stk pizza må kjøpes til festen")
            break
        except ValueError:
            print("Ugyldig tall!")

#Oppgave 3: Omregning fra grader til radianer
def oppgave_3():
    while True:
        try:
            print ("Oppgave 3")
            print ("--> Skriv inn gradtallet")
            #Input
            v_grad = float(input("--> "))                                       #Input antall grader
            v_rad = v_grad*np.pi/180                                            #Utregning antall radianer
            #Output
            print ("-->",v_grad,"Grader tilsvarer",v_rad,"Radianer")
            break
        except ValueError:
            print("Ugyldig tall!")

#Oppgave 4: Dictionary
def oppgave_4():
    while True:
        try:
            #Dictionary dataset
            data = {
                "Norge": ["Oslo", 0.634],
                "England": ["London", 8.982],
                "Frankrike": ["Paris", 2.161],
                "Italia": ["Roma", 2.873]
                }
            
            #Funksjon for å printe alle keys (land) i dictionary
            def print_alle_land():
                print("\nTilgjenglige land:")
                for i, land in enumerate(data.keys(), 1):
                    print(f"{i}. {land}")                    
            
            #Funksjon for å printe innholdet i i dictionary for en valgt key (land)
            def print_land_info(land):
                if land in data:
                    hovedstad, befolkning = data[land]
                    print(f"\nLand: {land}")
                    print(f"Hovedstad: {hovedstad}")
                    print(f"Befolkning: {befolkning} millioner")
                else:
                    print("\nLand ikke funnet!")
            
            #Funksjon for input av nytt land i dictionary
            def add_new_country():
                land = input("\nSkriv inn navn på land: ")
                hovedstad = input("Skriv inn navn på hovedstad: ")
                while True:
                    try:
                        befolkning = float(input("Skriv inn befolkning i millioner: "))
                        break
                    except ValueError:
                        print("Ugyldig tall!")
                
                data[land] = [hovedstad, befolkning]
                print(f"\n{land} har blitt lagt til i dictionary!")
            
            #Undermeny for valg av tilgjengelige funksjoner
            def meny():
                while True:
                    print("\n=== Landinfo ===")
                    print("1. Vis alle land")
                    print("2. Vis info om land")
                    print("3. Legg til nytt land")
                    print("4. Avslutt")
                    
                    valg = input("\nSkriv inn ditt valg (1-4): ")
                    
                    if valg == "1":
                        print_alle_land()
                    
                    elif valg == "2":
                        print_alle_land()
                        land = list(data.keys())
                        while True:
                            try:
                                valg = int(input("\nVelg land nr: "))
                                if 1 <= valg <= len(land):
                                    print_land_info(land[valg-1])
                                    break
                                else:
                                    print("Ugyldig tall!")
                            except ValueError:
                                print("Ugyldig tall!")
                    
                    elif valg == "3":
                        add_new_country()
                    
                    elif valg == "4":
                        print("\nPå gjensyn")
                        break
                    
                    else:
                        print("\nUgyldig tall!")
            meny()            
            break
        except ValueError:
            print("Ugyldig tall!")

#Oppgave 5: Funksjon for omkrets og areal
def oppgave_5():
    while True:
        try:
            def kalk_a_o(a, b):
                areal = (np.pi * a**2)/2+(a * b)/2 
                omkrets = (np.pi * a)/2+b+np.sqrt(a**2+b**2)
                return (areal, omkrets)
                
            #Input
            a1 = int(input("\nSkriv inn verdien - a: "))
            b1 = int(input("Skriv inn verdien - b: "))
            #Kaller funksjonen kalk_a_o
            (areal, omkrets) = kalk_a_o(a1, b1)
            print ("Oppgave 5")
            print ("Areal ", areal)
            print ("Omkrets ", omkrets)     
            break
        except ValueError:
            print("Ugyldig tall!")

#Oppgave 6: Plot
def oppgave_6():
    while True:
        try:
            #Lage x verdier fra -10 til 10 med 200 punkter
            x = np.linspace(-10, 10, 200)
            #Kalkuler y verdi med gitt funksjon
            y = -x**2 - 5
            
            #Plot
            plt.figure(figsize=(10, 6))                                 # Set figur størrelse
            plt.plot(x, y,'b-', label='f(x) = -x² - 5')
            plt.grid(True, linestyle='--', alpha=0.7)
            #Tittel og x/y label
            plt.title('Funksjon: f(x) = -x² - 5')
            plt.xlabel('x')
            plt.ylabel('y')
            #Referanselinjer for x og y akser på 0
            plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
            plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
            #Vis plot
            plt.show()
            break
        except ValueError:
            print("Ugyldig tall!")

#Hovedmeny
def main():
    while True:
        print("\n=== Meny ===")
        print("1. Kalkuler alder")
        print("2. Kalkuler antall pizza")
        print("3. Konverter grader til radianer")
        print("4. Dictionary")
        print("5. Funksjon Areal/Omkrets")
        print("6. Plot f(x) = -x² - 5")
        print("7. Avslutt")
        print("===========")
        
        valg = input("Skriv inn ditt valg (1-7): ")
        
        if valg == "1":
            oppgave_1()
        elif valg == "2":
            oppgave_2()
        elif valg == "3":
            oppgave_3()
        elif valg == "4":
            oppgave_4()
        elif valg == "5":
            oppgave_5()
        elif valg == "6":
            oppgave_6()
        elif valg == "7":
            print("\nPå gjensyn!")
            break
        else:
            print("Ugyldig valg! Velg 1-7.")

if __name__ == "__main__":
    main()