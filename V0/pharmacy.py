
class Pharmacy:
    
    def __init__(self):
        self.clients = [] # liste 
        self.medicaments = []

    def addClient(self, client):

        # vérification de l'objet client est il dans la liste ?
        # stop les programme !!!
        if client in self.clients:
            raise Exception("ce client {} est déjà dans la liste des clients".format(client.name))

        # si tu arrives ici c'est qu'il n'y a pas d'exception donc c'est un nouveau client
        self.clients.append(client) 

    def addMedicament(self, medicament):

        # todo faire la même chose avec raise pour vérifier que l'on a pas de nouveau un meme medicament

        if medicament not in self.medicaments:
            self.medicaments.append(medicament)