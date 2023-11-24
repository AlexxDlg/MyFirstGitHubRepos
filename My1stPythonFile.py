# Ceci est un 1er code en Python

from random import *

print("Bonjour")

choice = input("Voulez-vous saisir le montant ? (y/n)")

if (choice == "y"):
    PrixADeviner = int(input("Saisir un montant à deviner : "))
else:
    PrixADeviner = randint(1, 100)

Trouvé = 0
essais = 0
while(Trouvé != 1):
    essais += 1
    PrixEntree = int(input("Devine le prix : "))
    if (PrixEntree > PrixADeviner):
        print("Essayes plus petit")
    if (PrixEntree < PrixADeviner):
        print("Essayes plus grand")
    if (PrixEntree == PrixADeviner):
        Trouvé = 1
        print("Gagné ! après ", essais, "essais.", "Bien joué !")
