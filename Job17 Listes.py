#Ma fonction valeurs indéfinies only nombre
def my_function(*kekw:int):

    #Ma liste de nombre      
    myList = []

    #Boucle si pas numérique
    for lol in kekw:
        if isinstance(lol,(int)):
            myList.append(lol)
        else:
            print("PAS NUM GO REFAIRE !!")

    #Ma boucle 
    for num in kekw:

        #Trier les nombres pairs
        if num % 2 == 0:

            #Affichage du résultat sur un seul ligne d'où le end=" "
            print(num, end=" ")

#Test
my_function(87, 897, 98, 3.2)