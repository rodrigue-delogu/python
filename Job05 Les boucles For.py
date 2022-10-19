#Les deux valeurs
x = int(input("Valeur 1: "))
y = int(input("Valeur 2: "))

#Boucle
if x > y:
    for o in range(x-1, y, -1):
        print(o)

#Si x inférieur y
elif x < y:
    for a in range(x+1, y):
            print(a)

#Valeurs égales
if x == y:
    print("Valeurs égales")