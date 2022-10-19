#Ma fonction valeurs indéfinies only nombre
def my_function(*kekw:int):

    #Ma liste de nombre      
    myList = [*kekw]
    myList.sort()
        
    #Affichage du résultat           
    print(myList)

#Test
my_function(87, 897, 98, 3)