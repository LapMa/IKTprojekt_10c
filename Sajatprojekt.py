import random

szamito_win = 0
sajat_win = 0 

opciok = ["kő","papír","olló"]

while True:
    sajat_valasz = input("kő,papír vagy olló? ")
    random_szam = random.randint(0,2)
    szamito_valasztas = opciok[random_szam]

    if sajat_valasz == "kő" and szamito_valasztas == "olló":
        print("Nyertél")
        sajat_win += 1
        

    elif sajat_valasz == "papír" and szamito_valasztas == "kő":
        print("Nyertél")
        sajat_win += 1
        

    elif sajat_valasz == "olló" and szamito_valasztas == "papír":
        print("Nyertél")
        sajat_win += 1
        

    else:
        print("Vesztettél")
        szamito_win += 1

    print("A nyereségeim", sajat_win)
    print("Az számítógépé", szamito_win)

    