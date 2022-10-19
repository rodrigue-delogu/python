#Variable 
larg = int(input("Largeur du rectangle : "))
haut = int(input("Hauteur du rectangle : "))
largeur = ""
hauteur = ""
remplissage = ""

#Uniquement des nombres entiers
if larg < 1 or haut < 1:
    print("Only positif numbers !")
else:

    #Variable larg*"-" larg*" "
    for n in range(larg):
        largeur += "-"
        remplissage += " "

    #Impression de la première ligne
    print("|" + largeur + "|")

    #Impression du corps*hauteur
    for n in range(haut-2):      
        print("|" + remplissage + "|")

    #Impression de la dernière ligne
    print("|" + largeur + "|")

#Merci à Félix pour les tips et l'explication ! |---|-',