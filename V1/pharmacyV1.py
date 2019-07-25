
class Pharmacy:
    
    def __init__(self):
        self.clients = [] # liste clients [("toto",1000),("titi",500)...]
        self.medicaments = []  # exemple [obj("Advil",5),obj("Aspro",30),.....]   #liste medicament avec leur prix de vente
        self.stock_medicaments = {}      # stock de medicament avec leur quantite   

    def addClient(self, client):

        # vérification de l'objet client est il dans la liste ?
        # stop les programme !!!
        if client in self.clients:
            raise Exception("ce client {} est déjà dans la liste des clients".format(client.name))   #??????AURAIT ON PU METTRE PASS POUR NE RIEN FAIRE AU LIEU DE LEVER UNE EXCEPTION?   

        # si tu arrives ici c'est qu'il n'y a pas d'exception donc c'est un nouveau client
        self.clients.append(client) 

    def addMedicament(self, medicament):        #  On ajout le nom du medicament avec son prix de vente dans la BDD

        # todo faire la même chose avec raise pour vérifier que l'on a pas de nouveau un meme medicament

        if medicament not in self.medicaments:
            self.medicaments.append(medicament)
        else:
            raise Exception("le medicament {} est déja present dans la BDD".format(medicament.name)
              

    def stock_medicament(self,medicament):          # ??? je souhaite faire un stock ou ne figure que les nom des medicaments avec leur quantité présente
        if self.name not in self.stock_medicaments.keys:   
            self.stock_medicaments[name] = self.stock_medicaments.quantity
        else:
            self.stock_medicaments[name] += self.stock_medicaments.quantity
        
        
