#Boucle de 1 à 101
for n in range(1,101):

    #Multiple de 3 et 5
    if n % 15 == 0:
        print ("FizzBuzz")
        continue
    #Multiple de 3
    elif n % 3 == 0:
            print("Fizz")
            continue
    #Multiple de 5
    elif n % 5 == 0:
            print("Buzz")
            continue
    #Affiche le résultat
    print(n)