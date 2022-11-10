import random
from string import printable
#1Feladat
"""
str1 = input("Jó napod van? igen/nem:  ")
if str1 == "igen":
    print("Akkor jó napod van.")
if str1 == "nem":
    print("Szar lehet.")"""
#1.2Feladat
"""
elif str1 != "nem" and str1 != "igen":
    print("Nem értem a válaszodat")"""

#-----------------------------------------

#2Feladat
"""
szam = int(input("Kérek egy számot: "))
if szam % 2 ==0:
    print("A szám páros!")
else:
    print("A szám páratlan!")"""

#-----------------------------------------

#3Feladat
"""
szam2 = int(input("Kérek egy számot: "))
random1 = random.randint(1,5)
if szam2 == random1:
    print("A két szám egynelő:")
if szam2 > random1:
    print("A szám nagyobb mint a dondolt szám ")
if szam2 < random1:
    print("A szám kisebb mint a gondolt szám ")"""


#-----------------------------------------
#1CIKLUS

#1Feladat

for paros in range(10):
    if paros % 2 ==  0:
        print(paros)

#2Feladat
