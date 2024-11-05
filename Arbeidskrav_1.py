"""
Created on Tue Nov  5 18:49:17 2024

@author: tt
"""

#Enkelt program for å sammenligne årlig driftskostnader mellom EV og ICE biler 

import time 

print ("<< EV -VS- ICE >>")
print ("-->Fyll inn årlig kjørelengde i km")
time.sleep (0.5)
#Input
km = int(input ("-->"))                                     #Total kjørelengde i km

EV_C = (0.2 / 2)                                            #EV forbrukskostnad pr km i NOK
TEV_C = (km * EV_C)                                         #EV forbrukskostnad totalt pr år i NOK (basert på input)
ICE_C = (1.0)                                               #ICE forbrukskostnad pr km i NOK
TICE_C = (km * ICE_C)                                       #ICE forbrukskostnad totalt pr år i NOK (basert på input)
TFA = (8.38 * 365)                                          #Trafikkforsikringsavgift pr år i NOK
I_EV = (5000)                                               #EV forsikring pr år i NOK
I_ICE = (7500)                                              #ICE forsikring pr år i NOK
B_EV = (0.1)                                                #EV bomavgift pr km i NOK
TB_EV = (km * B_EV)                                         #EV Bomavgift totalt pr år i NOK (basert på input)
B_ICE = (0.3)                                               #ICE bomavgift pr km i NOK
TB_ICE = (km * B_ICE)                                       #ICE bomavgift totalt pr år i NOK (basert på input)

#Output
time.sleep (0.1)
print ()
print ("Totalkostnad ved",km,"km årlig kjørelengde")        #Print med km input variabel
print ()
time.sleep (0.1)
print ("EV  -> NOK -",int(TEV_C+TFA+I_EV+TB_EV),",-")       #Legger sammen aktuelle variabler for EV
print ("ICE -> NOK -",int(TICE_C+TFA+I_ICE+TB_ICE),",-")    #Legger sammen aktuelle variabler for ICE


