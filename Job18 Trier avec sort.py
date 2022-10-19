#Ma fonction valeurs indéfinies only nombre
def ClaudeFrançois(*kekw:int):

    #Ma liste de nombres
    myList = [*kekw]
    myList.sort()
        
    #Affichage du résultat           
    print(myList)

#Test
ClaudeFrançois(87, 897, 98, 3)