from client import *
from pharmacy import *
from medicament import *

# Bootstrap de l'application

"""
eeeeeeeeeeeeeeeeeeeeee
1/ Une classe un role unique Client, Medicament et Pharmacy

2/ Pharmacy c'est un container car il agrège les entités Client et Medicament, son rôle c'est d'appliquer
la logique algorithmique : le calcul d'une commande d'un client qui commande un medicament

Gestion des exceptions simples en utilisant raise, dans le fichier main on fera remonter les exceptions pour les gérer de 
manière centrale.

Les contraintes que l'on a appliqué : ne pas ajouter un client ou un médicament déjà présent dans la Pharmacy

"""

"""
Menu souahitez :
1 Afficher-> Nom du client?
             Nom du médicament
             Quantité acheté par le client
             Combien le client paie la pharmacie
             
2 Afficher-> Nom du medicament:
             Nombre de boites achetées au fournisseur
             
3 Afficher-> Medicaments en stocks et leur quantité
             Clients dans la base de donnees de pharmacy ainsi que l'argent qui reste sur leur compte pharmacy

4 Afficher-> On quitte l'application 
"""            

def menu(self):


    print("1 : Achat de medicament")
    print("2 : Approvisionnement en medicaments")
    print("3 : Etats des stocks et des credits")
    print("4 : quitter")



clients = [
    Client('Alan', 1000),
    Client('Alice', 5000),
    Client('Albert', 800)
]

medicaments = [
    Medicament(name = "Aconitum ", price = 7, quantity = 10),
    Medicament(name = "Aesculus ", price = 18, quantity = 8),
    Medicament(name = "Baryta ", price = 9.5, quantity = 12),
    Medicament(name = "Capsicum ", price = 19, quantity = 5),
]

# création d'une instance de Pharmacy, container ~ logic algorithmique du projet
pharmacy = Pharmacy()

for client in clients:              # on ajoute les clients ("Alan","Alice",Albert" dans la liste client de la pharmacy)
    pharmacy.addClient(client)

# pour tester si mon client est déjà rentrer dans la liste ?
# pharmacy.addClient( clients[0] )

# liste dans Pharmacy des clients
for client in pharmacy.clients:
    print("name {}, credit {}".format(client.name, client.credit))

# ajouter les médicaments dans Pharmancy
for medicament in medicaments:
    pharmacy.addMedicament(medicament)


print(pharmacy)



