#Importation de minidom
import xml.dom.minidom

#Variable pour parse le fichier
docs = xml.dom.minidom.parse("domains.xml")

#Variable pour savoir dans quoi allez chercher
domains = docs.getElementsByTagName("table")

#Variable pour compter les domains dans table
nbr = len(domains)

#Affichage du nombre de domains
print(nbr)
