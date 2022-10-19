#Import Regex
import re

nbrmot = int(input("Entrez la taille de votre mot: "))
#Ouverture du fichier
data = open("data.txt", "r")

#Lecture du fichier
kekw = data.read()

#Ma recherche et mon filtre
x = re.findall("\W+", kekw)

#Départ de ma bouche
end = 0
i = 0

#Ma boucle
while i < len(x): 
    if nbrmot == len(x[i]):
        end += 1
        
    #Incrémentation de boucle
    i += 1 

#Résultat
print(end)