from utils.math import showTable

redo = 1
while redo == 1:
    print("\nQue voulez-vous faire ?")
    mod = int(input("1.Table de multiplication \n2.Classer dans un certain order en donnant le nombre de nombres \n3.Classer dans un certain order\n"))
    if mod == 1:
        table = int(input("Table a afficher: "))
        count  = int(input("Nombre de fois a multiplier %s: " % table))
        showTable(table, count)
        
    if mod == 2:
        nbrList = []
        
        print("Dans quel ordre ?")
        order = int(input("1.Croissant \n2.Decroissant\n"))
        
        nbrCount = int(input("Total de nombres: "))
        
        nbr = int(input("Premier nombre: "))
        nbrList.append(nbr)
        
        i = 1
        while i < nbrCount-1:
            nbr = int(input("Nombre suivant: "))
            nbrList.append(nbr)
            i += 1
        
        nbr = int(input("Dernier nombre: "))
        nbrList.append(nbr)
        
        if order == 1:
            nbrList.sort(key=int, reverse=False)
        elif order == 2:
            nbrList.sort(key=int, reverse=True)
        
        print(nbrList)
        
    if mod == 3:
        nbrList = []
        
        print("Dans quel ordre ?")
        order = int(input("1.Croissant \n2.Decroissant\n"))
        
        nbr = int(input("Premier nombre: "))
        nbrList.append(nbr)
        
        while True:
            rep = input("Nombre suivant: ")
            if rep.isdigit():
                rep = int(rep)
                nbrList.append(rep)
            else:
                if rep == "q" or rep == "quit":
                    break;
        
        if order == 1:
            nbrList.sort(key=int, reverse=False)
        elif order == 2:
            nbrList.sort(key=int, reverse=True)
        
        print(nbrList)
        
    print("\nQue voulez-vous faire ?")
    redo = int(input("1.Continuer \n2.Quitter\n"))
    
print("Merci d'avoir utilise ce programme.")


