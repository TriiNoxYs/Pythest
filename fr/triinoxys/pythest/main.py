#from utils.math import table
#table(int(input("Quelle table voulez-vous afficher ?")), int(input("Combien de fois ?")))

v1 = 1.0
v2 = 2.0
v3 = 4.3

count = input("Combien de nombres ?")
count = int(count)
i = 1
while i <= count:
    if i == 1:
        print(v1)
    elif i == 2:
        print(v2)
    elif i == 3:
        print(v3)
    i += 1
    

