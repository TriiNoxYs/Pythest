from utils.math import table
from audioop import reverse


choix = int(input("1.Table de multiplication \n2.Classer dans un certain ordre en donnant le nombre de nombres \n3.Classer dans un certain ordre\n"))
if choix == 1:
    nbrTable = int(input("Quelle table voulez-vous afficher ?\n"))
    nbrFois  = int(input("Combien de fois faut-il multiplier %s ?\n" % nbrTable))
    table(nbrTable, nbrFois)
    
if choix == 2:
    liste = []
    
    print("Dans quel ordre ?")
    ordre = int(input("1.Croissant \n2.Decroissant\n"))
    
    nbrNombres = int(input("Combien de nombres ?\n"))
    
    nbrActuel = int(input("Premier nombre: "))
    liste.append(nbrActuel)
    
    i = 1
    while i < nbrNombres-1:
        nbrActuel = int(input("Nombre suivant: "))
        liste.append(nbrActuel)
        i += 1
    
    nbrActuel = int(input("Dernier nombre: "))
    liste.append(nbrActuel)
    
    if ordre == 1:
        liste.sort(key=int, reverse=False)
    elif ordre == 2:
        liste.sort(key=int, reverse=True)
    
    print(liste)
    
if choix == 3:
    liste = []
    
    print("Dans quel ordre ?")
    ordre = int(input("1.Croissant \n2.Decroissant\n"))
    
    nbrActuel = int(input("Premier nombre: "))
    liste.append(nbrActuel)
    
    while True:
        rep = input("Nombre suivant: ")
        if rep.isdigit():
            rep = int(rep)
            liste.append(rep)
        else:
            if rep == "q" or rep == "quit":
                break;
    
    if ordre == 1:
        liste.sort(key=int, reverse=False)
    elif ordre == 2:
        liste.sort(key=int, reverse=True)
    
    print(liste)
