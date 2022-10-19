#Les deux valeurs
x = int(input("Valeur 1: "))
y = int(input("Valeur 2: "))

#Boucle si x est supérieur à y alors elle va afficher les nombres entre 
if x > y:
    for o in range(x-1, y, -1):
        print(o)

#Si x inférieur y alors elle va afficher les nombres entre
elif x < y:
    for a in range(x+1, y):
            print(a)

#Valeurs égales, message d'impossibilité 
if x == y:
    print("Valeurs égales")