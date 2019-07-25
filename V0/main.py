from client import *
from pharmacy import *
from medicament import *

# Bootstrap de l'application

"""
print(Pharmacy())
print(Client('Alan', 1000))
"""

"""
Cours :

1/ Une classe un role unique Client, Medicament et Pharmacy

2/ Pharmacy c'est un container car il agrège les entités Client et Medicament, son rôle c'est d'appliquer
la logique algorithmique : le calcul d'une commande d'un client qui commande un medicament

Gestion des exceptions simples en utilisant raise, dans le fichier main on fera remonter les exceptions pour les gérer de 
manière centrale.

Les contraintes que l'on a appliqué : ne pas ajouter un client ou un médicament déjà présent dans la Pharmacy

"""

clients = [
    Client('Alan', 1000),
    Client('Alice', 5000),
    Client('Albert', 800)
]

medicaments = [
    Medicament(name = "Aconitum napelus", price = 7, quantity = 10),
    Medicament(name = "Aesculus Hippocastanum", price = 18, quantity = 8),
    Medicament(name = "Baryta Carbonica", price = 9.5, quantity = 12),
    Medicament(name = "Capsicum Annuum", price = 19, quantity = 5),
]

# création d'une instance de Pharmacy, container ~ logic algorithmique du projet
pharmacy = Pharmacy()

for client in clients:
    pharmacy.addClient(client)

# pour tester si mon client est déjà rentrer dans la liste ?
# pharmacy.addClient( clients[0] )

# liste dans Pharmacy des clients
for client in pharmacy.clients:
    print("name {}, credit {}".format(client.name, client.credit))

# ajouter les médicaments dans Pharmancy
for medicament in medicaments:
    pharmacy.addMedicament(medicament)