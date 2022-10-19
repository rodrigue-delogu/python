#Import Regex
import re

#Ouverture du fichier
data = open("data.txt", "r")

#Lecture du fichier
kekw = data.read()

#Variable de la recherche et le filtre
x = re.findall("\W+", kekw)

#Résultat
print(len(x))
