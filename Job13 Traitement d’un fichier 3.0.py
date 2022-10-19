#Import Regex
import re

#Input en only number pour la taille du mot
nbrmot = int(input("Entrez la taille de votre mot: "))

#Ouverture du fichier
data = open("data.txt", "r")

#Variable de la lecture du fichier
kekw = data.read()

#Variable de la recherche et le filtre
x = re.findall("\W+", kekw)

#Départ de ma boucle
end = 0
i = 0

#Boucle while, qui sera toujours supérieur à 0 
while i < len(x): 

    #On explique avec le if que le résultat affiché doit être dans le tri initial et dans la nouvelle variable qui rajoute un nombre de mot
    if nbrmot == len(x[i]):
        end += 1
        
    #Incrémentation de boucle
    i += 1 

#Résultat
print(end)