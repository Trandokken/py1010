"""
Created on Tue Nov  5 21:34:05 2024

@author: tt
"""

#Enkelt program som sjekker alderen din ut fra fødeår og nåværende år

from datetime import datetime

print ("-->Hvilket år er du født?")
#input
fødeår = int(input("-->"))                          #Input fødeår
årstall = int(datetime.now().strftime('%Y'))        #Inneværende år
alder = (årstall - fødeår)                          #Utregning av alder
#Output
print ("-->Du er nå",(alder),"år gammel!")          #Skriver variabel alder
