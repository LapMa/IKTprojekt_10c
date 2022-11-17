"""
#1Feladat
szam = 1
while szam <=20:
    if szam % 2 == 0:
        print(szam,"páros")
        szam += 1
    elif szam % 2 == 1:
        print(szam,"páratlan")
        szam += 1
"""


#2Feladat
list = []
szam = int(input("Kérek gy számot: "))
szam.append(list)
szam = 0
for a in list:
    szam += 1
    avg = szam / len(list)
        
print("A szám átlaga:",szam)