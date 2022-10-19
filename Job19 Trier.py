#Ma fonction valeurs indéfinies only nombre
def my_function(*kekw:int):

    #Ma liste de nombre      
    num = [*kekw]

    #Création des boucles 
    for i in range(len(num)):
        for j in range(len(num)):

            #If ce nombre i est plus petit que le nombre j dans une liste
            if num[i] < num[j]:

                #Puis on inverse les nombres de la liste par ordre croissant
                num[i], num[j] = num[j], num[i]

    #Résultat
    print(num)

#Test
my_function(87, 897, 98, 3)

#Thanks to Abraham for the lesson "how to think in python", this guy is incredible !
