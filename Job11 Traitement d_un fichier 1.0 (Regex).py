#Import REGEX
import re

#Ouverture du fichier domains.xml
data = open("domains.xml", "r")

#Lecture du fichier
kekw = data.read()

#Recherche de domain
x = re.findall("domain", kekw)

#Et on compte
nbr = len(x)

#Apercu du résultat
print(nbr)