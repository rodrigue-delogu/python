#Ma fonction valeurs indéfinies only nombre
def Dalida(*kekw:int):

    #Ma liste de nombres     
    myList = []

    #Boucle si pas des nombres, on prévient !
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
Dalida(87, 897, 98, 3.2)