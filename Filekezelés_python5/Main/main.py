import os
from posixpath import split

os.system('cls')

array_lista = []
def beolvasas():
    forras = open("text.txt","r",encoding="utf-8")
    forras.readline()
        
    for line in forras:
        array_lista.append(line)

def lenght():
    total_nobel = len(array_lista)
    print(f"Az összesen {total_nobel} nobel díjas van")

def last_award():
    valtozo = 0
    for item in array_lista:
        x = item[0].split(";")
        min = array_lista[0]
        for number in array_lista:
            if number < min:
                min = number
        last = min.split(";")
    print(f" {last[0]} ez az év amikor az első Nobel díjat kiosztották ")

def oldset_member_live():
    total_years_live = []
    total_years = []
    index = 0
    for item in array_lista:
        x = item.split(";")
        elem = x[2]
        y = elem.split("-")
        first = y[0]
        if y[1] == "":
            total_years_live.append(y[0])
        #Kivonja 2023-ból az adott éveket
    for x in total_years_live:
        minusnumbers = 2023 - int(total_years_live[index])
        index += 1
        total_years.append(minusnumbers)
    max = int(0)
    id = int(0)
    i = int(0)
    if int(x[0]) > max:
        max = int(x[0])
        id = i
        i += 1
    print("A legidősebb ember a ki é sés nobel díjas", total_years[id].split(';')[1] ,"és életkora " ,max)
    
   

        
            




beolvasas()
#lenght()
#last_award()
oldset_member_live()
