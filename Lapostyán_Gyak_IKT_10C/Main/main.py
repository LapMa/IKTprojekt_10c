lista = []
def beolvasas():
    forras = open("Main/fob2016.txt","r",encoding="UTF-8")
    forras.readline()

    for line in forras:
        lista.append(line)
def personallenght():
    lenght = len(lista)
    print(f"Összesen {lenght} versenyző idnult a versenyen")

def womenarg():
    women_lista = []
    for item in lista:
        x = item.split(";") 
        if x[1] == "Noi":
            women_lista.append(x[1])
    arg = len(women_lista) / len(lista) * 100
    print(f"A női vesenyzők aránya {arg:.4}")

def allpoints_for_women():
    for item in lista:
        x = item.split(";") 
        if x[1] == "Noi":
            

            


beolvasas()
#personallenght()
#womenarg()
