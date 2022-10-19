#Ouverture du fichier domains.xml
f = open("domains.xml", "r")

#Lecture du fichier
kekw = f.read()

#Recherche de domain et on compte tout en l'affichant dans le terminal
print(kekw.count('name="domain"'))