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
"""
ism = int(input("Hanyszor"))
rep = 0
list = []
while rep != ism:
    rep += 1
    szamok = int(input("Szamok:"))
    list.append(szamok)

list2 = sum(list)
print(list / ism)"""
#3Feladat
also = int(input("Alső szám: "))
felso = int(input("Felső szám: "))

list = range(also,felso+1)
sum = 0
i = 0

for x in list:
    sum = sum + x
    i += 1

print(sum, sum/i)

#4Feladat
"""
szam1 =1
while szam1 <= 5:
    print(szam1)
    szam1 += 1"""

#5Feladat
"""
n = 1
list = []
while True:
    n = int(input("Kérek egy számot: "))
    n += 1
    list.append(n)
    if n != "":
        ossz = sum(n)
        print(ossz)
"""

