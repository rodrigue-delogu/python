#Import Regex
import re

#Ouverture du fichier
data = open("data.txt", "r")

#Lecture du fichier
kekw = data.read()

#Ma recherche et mon filtre
x = re.findall("\W+", kekw)

#Résultat
print(len(x))
