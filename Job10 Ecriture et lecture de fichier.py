#Consigne
n = input("Voulez-vous écrire ou lire : ")

#Choix lecture
if n == "lire":

    #Lecture de fichier output.txt sur le terminal
    f = open("output.txt", "r")
    print(f.read())
    f.close()

#Choix écriture
elif n =="écrire":

    #Ecriture du texte, création du fichier ete sauvegarde la phrase
    n = input ("Ecrivez un texte :")
    f = open("output.txt", "w+")
    f.write(n)
    f.close()