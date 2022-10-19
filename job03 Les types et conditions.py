#Question pour l'âge
print("Quel âge as-tu ? ")

#Age avec nombre entier
age = float(input())

#Conditions
#Si l'âge est inférieur à 18
if age < 18:
    #Alors
    print("Tu es mineur.")
else: 
    #Si non alors :
    print("Tu es majeur.")