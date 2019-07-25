from client import *
from pharmacy import *
from medicament import *



medicaments = [
    Medicament(name="aspro", price=7, quantity=10),
    Medicament(name="inipomp", price=18, quantity=8),
    Medicament(name="rhino", price=9.5, quantity=12),
    Medicament(name="advil", price=19, quantity=5),
]

# création de la pharmacy
pharmacy = Pharmacy()

# je stock mes médicaments au départ
for medicament in medicaments:
    pharmacy.addMedicament(medicament)

"""
Modifier une quantité ou ajouter un nouveau médicament
"""
fervex = Medicament(name="fervex", price=11.5, quantity=5)

pharmacy.addMedicament(fervex)

print(pharmacy.medicaments["fervex"].quantity)

for k, m in pharmacy.medicaments.items():
    print(k, m.quantity)


"""
Ajouter des clients
"""

clients = [
    Client('Alan'), Client('Alice'), Client('Albert')
]

for client in clients:
    pharmacy.addClient(client)

"""

Implémentez une fonction buy qui prend un client un medicament avec une quantité
et qui stockera dans un panier l'achat.

Une méthode qui s'appelle total et qui donne le total de la commande

"""

pharmacy.client_buy_medicament(clients[0], medicaments[0], 17)
pharmacy.client_buy_medicament(clients[0], medicaments[0], 5)





client_buy_medicament(clients[0],medicaments[0],1)
print(pharmacy.commande_client)
